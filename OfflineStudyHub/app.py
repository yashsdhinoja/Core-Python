from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
from urllib.parse import unquote, urlparse
import argparse
import html
import mimetypes
import os
import socket

ROOT = Path(__file__).resolve().parent
WEB_DIR = ROOT / "web"
MATERIALS_DIR = ROOT / "materials"
HOST = "127.0.0.1"
PORT = 8000

class StudyHubHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        parsed = urlparse(self.path)
        if parsed.path == "/api/files":
            from urllib.parse import parse_qs
            section = parse_qs(parsed.query).get("section", [""])[0]
            allowed = {"react-project", "dsa-python", "advanced-dbms"}
            if section not in allowed:
                self.send_error(400, "Unknown section")
                return
            folder = (MATERIALS_DIR / section).resolve()
            root = MATERIALS_DIR.resolve()
            if root not in folder.parents:
                self.send_error(400, "Invalid section")
                return
            entries = []
            for item in sorted(folder.rglob("*"), key=lambda p: str(p).lower()):
                try:
                    resolved = item.resolve()
                    if not (resolved == folder or folder in resolved.parents):
                        continue
                    if item.is_file() and item.name != "PLACE_FILES_HERE.txt":
                        rel = item.relative_to(MATERIALS_DIR).as_posix()
                        entries.append({
                            "name": item.name,
                            "path": rel,
                            "url": "/materials/" + "/".join(
                                __import__("urllib.parse", fromlist=["quote"]).quote(part)
                                for part in rel.split("/")
                            )
                        })
                except (OSError, ValueError):
                    continue
            import json
            payload = json.dumps(entries).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(payload)))
            self.end_headers()
            self.wfile.write(payload)
            return
        return super().do_GET()

    def translate_path(self, path):
        # Route the dashboard itself to web/, and all study material to materials/.
        parsed = urlparse(path)
        route = unquote(parsed.path)

        if route == "/api/files":
            return str(WEB_DIR / "index.html")
        if route == "/" or route == "/index.html":
            return str(WEB_DIR / "index.html")
        if route.startswith("/assets/"):
            safe = (WEB_DIR / route.lstrip("/")).resolve()
            if safe == WEB_DIR.resolve() or WEB_DIR.resolve() in safe.parents:
                return str(safe)
            return str(WEB_DIR / "index.html")
        if route.startswith("/materials/"):
            relative = route[len("/materials/"):]
            candidate = (MATERIALS_DIR / relative).resolve()
            if candidate == MATERIALS_DIR.resolve() or MATERIALS_DIR.resolve() in candidate.parents:
                return str(candidate)
            return str(MATERIALS_DIR)
        return str(WEB_DIR / "index.html")

    def list_directory(self, path):
        # Do not expose raw directory listings; the dashboard provides navigation.
        self.send_error(403, "Directory listing is disabled.")
        return None

    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        super().end_headers()

    def log_message(self, fmt, *args):
        print("[%s] %s" % (self.log_date_time_string(), fmt % args))

def local_ip():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        sock.connect(("192.0.2.1", 80))
        return sock.getsockname()[0]
    except OSError:
        return "YOUR-PC-IP"
    finally:
        sock.close()

def main():
    parser = argparse.ArgumentParser(description="Offline Study Hub local web server")
    parser.add_argument("--host", default=HOST, help="127.0.0.1 for this PC only; 0.0.0.0 for local-network devices")
    parser.add_argument("--port", type=int, default=PORT)
    args = parser.parse_args()

    MATERIALS_DIR.mkdir(exist_ok=True)
    WEB_DIR.mkdir(exist_ok=True)
    server = ThreadingHTTPServer((args.host, args.port), StudyHubHandler)
    print("\\nOffline Study Hub is running.")
    print(f"On this PC: http://127.0.0.1:{args.port}")
    if args.host == "0.0.0.0":
        print(f"On another device on the same network: http://{local_ip()}:{args.port}")
        print("Only use this on a trusted network. Windows Firewall may ask for permission.")
    print("Keep this terminal open while using the site.")
    print("Press Ctrl+C to stop the server.\\n")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\\nStopping Offline Study Hub...")
    finally:
        server.server_close()

if __name__ == "__main__":
    main()
