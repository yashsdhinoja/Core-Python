"""
LocalServer - a small HTTP web server written from scratch.

It does NOT use http.server, socketserver, Flask or any web framework.
Everything about HTTP (reading the request, sending the response, finding
files, directory pages, MIME types, URL decoding) is written by hand below.
The only tools it uses are the low-level ones every program needs:
    socket     -> to talk over the network (the "phone line")
    threading  -> to serve many browsers at the same time
    os / sys / time -> files & folders, command-line arguments, clock

Run it:        python server.py            (default port 8000)
Another port:  python server.py 9000
Stop it:       press Ctrl + C
"""

import os          # work with files and folders
import socket      # low-level networking
import sys         # read command-line arguments (sys.argv)
import threading   # one thread per browser connection
import time        # print the time in the log

# ======================================================================
# 1. SETTINGS  (change these if you want)
# ======================================================================

HOST = "0.0.0.0"   # "0.0.0.0" = listen on ALL network cards, so other devices can connect
PORT = 8000        # the "door number" of the server: http://ip:8000

# folder where THIS file (server.py) lives
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# only the files inside this "www" folder are shown to browsers
WEB_ROOT = os.path.join(BASE_DIR, "www")

MAX_HEADER_BYTES = 16 * 1024   # refuse requests whose header is bigger than 16 KB
CHUNK_SIZE = 64 * 1024         # send big files in pieces of 64 KB
CLIENT_TIMEOUT = 10            # seconds to wait for a silent browser before giving up

# Meaning of the numbers the server sends back (HTTP status codes)
STATUS_TEXT = {
    200: "OK",
    301: "Moved Permanently",
    400: "Bad Request",
    403: "Forbidden",
    404: "Not Found",
    405: "Method Not Allowed",
    500: "Internal Server Error",
}

# Tells the browser what kind of file it receives, based on the file ending.
# Text-like files carry "charset=utf-8" so Chrome shows letters correctly.
MIME_TYPES = {
    ".html": "text/html; charset=utf-8",
    ".htm": "text/html; charset=utf-8",
    ".css": "text/css; charset=utf-8",
    ".js": "text/javascript; charset=utf-8",
    ".mjs": "text/javascript; charset=utf-8",
    ".json": "application/json; charset=utf-8",
    ".map": "application/json; charset=utf-8",
    ".webmanifest": "application/manifest+json; charset=utf-8",
    ".xml": "application/xml; charset=utf-8",
    ".txt": "text/plain; charset=utf-8",
    ".md": "text/plain; charset=utf-8",
    ".csv": "text/csv; charset=utf-8",
    # source-code files are shown as plain text (never executed by the server)
    ".py": "text/plain; charset=utf-8",
    ".sql": "text/plain; charset=utf-8",
    ".c": "text/plain; charset=utf-8",
    ".cpp": "text/plain; charset=utf-8",
    ".h": "text/plain; charset=utf-8",
    ".java": "text/plain; charset=utf-8",
    ".ipynb": "application/json; charset=utf-8",
    # images
    ".svg": "image/svg+xml",
    ".png": "image/png",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".gif": "image/gif",
    ".webp": "image/webp",
    ".ico": "image/x-icon",
    # fonts, audio, video, other
    ".woff": "font/woff",
    ".woff2": "font/woff2",
    ".ttf": "font/ttf",
    ".wasm": "application/wasm",
    ".mp3": "audio/mpeg",
    ".mp4": "video/mp4",
    ".pdf": "application/pdf",
    ".zip": "application/zip",
    ".docx": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    ".pptx": "application/vnd.openxmlformats-officedocument.presentationml.presentation",
    ".xlsx": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
}

# Letters that never need to be "percent-encoded" inside a web address
SAFE_URL_CHARS = (
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    "abcdefghijklmnopqrstuvwxyz"
    "0123456789-._~"
)
HEX_DIGITS = "0123456789abcdefABCDEF"

# HTML skeleton used for the folder pages and the error pages.
# {{TITLE}}, {{HEADING}} and {{BODY}} are replaced later with real text.
# It uses only system fonts and no outside links, so it works fully offline.
PAGE_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{{TITLE}}</title>
<style>
  :root {
    color-scheme: light dark;
    --bg: #f3f5f4; --panel: #ffffff; --text: #17201d; --muted: #5d6b66;
    --line: #d9e0dd; --accent: #0b7a64; --hover: #e8f2ef;
  }
  @media (prefers-color-scheme: dark) {
    :root {
      --bg: #101513; --panel: #171e1b; --text: #e4ebe8; --muted: #8fa098;
      --line: #28332f; --accent: #4cc9a8; --hover: #1f2a26;
    }
  }
  * { box-sizing: border-box; }
  body {
    margin: 0; padding: 24px 16px 48px; background: var(--bg); color: var(--text);
    font-family: "Segoe UI", system-ui, -apple-system, Roboto, "Helvetica Neue", Arial, sans-serif;
    line-height: 1.5;
  }
  main { max-width: 720px; margin: 0 auto; }
  h1 { font-size: 1.5rem; margin: 0 0 4px; overflow-wrap: anywhere; }
  p.note { margin: 0 0 20px; color: var(--muted); }
  ul { list-style: none; margin: 0; padding: 0; background: var(--panel);
       border: 1px solid var(--line); border-radius: 8px; overflow: hidden; }
  li + li { border-top: 1px solid var(--line); }
  li a { display: flex; justify-content: space-between; gap: 16px; padding: 12px 16px;
         color: var(--text); text-decoration: none; }
  li a:hover, li a:focus-visible { background: var(--hover); outline: none; }
  li.folder a span:first-child { color: var(--accent); font-weight: 600; }
  li span:first-child { overflow-wrap: anywhere; }
  li span.size { color: var(--muted); white-space: nowrap; font-variant-numeric: tabular-nums; }
  .empty { padding: 16px; color: var(--muted); }
</style>
</head>
<body>
<main>
<h1>{{HEADING}}</h1>
{{BODY}}
</main>
</body>
</html>
"""


# ======================================================================
# 2. SMALL HELPER FUNCTIONS (text tools written by hand)
# ======================================================================

def html_escape(text):
    """Make text safe to place inside HTML (so '<' cannot become a tag)."""
    text = text.replace("&", "&amp;")    # must be first, or we would double-escape
    text = text.replace("<", "&lt;")
    text = text.replace(">", "&gt;")
    text = text.replace('"', "&quot;")
    text = text.replace("'", "&#39;")
    return text


def url_decode(text):
    """Turn '%20' into a space, '%41' into 'A', and so on (percent-decoding)."""
    raw = bytearray()                    # we collect BYTES first, then turn them into text
    i = 0
    while i < len(text):
        ch = text[i]
        # a percent sign followed by two hex digits, e.g. %2F
        if ch == "%" and i + 2 < len(text):
            pair = text[i + 1:i + 3]
            if pair[0] in HEX_DIGITS and pair[1] in HEX_DIGITS:
                raw.append(int(pair, 16))    # "2F" -> 47 (one byte)
                i += 3                       # we used 3 characters: % + 2 digits
                continue
        raw.extend(ch.encode("utf-8"))       # normal character: keep as it is
        i += 1
    return raw.decode("utf-8", errors="replace")


def url_encode(text):
    """Opposite of url_decode: make a file name safe to use inside a link."""
    out = []
    for byte in text.encode("utf-8", errors="replace"):
        ch = chr(byte)
        if byte < 128 and ch in SAFE_URL_CHARS:
            out.append(ch)                   # safe letter: keep
        else:
            out.append("%{:02X}".format(byte))   # anything else: %XX
    return "".join(out)


def format_size(num_bytes):
    """12345 -> '12.1 KB' so humans can read file sizes."""
    size = float(num_bytes)
    for unit in ("B", "KB", "MB", "GB"):
        if size < 1024 or unit == "GB":
            if unit == "B":
                return "{} B".format(int(size))
            return "{:.1f} {}".format(size, unit)
        size = size / 1024


def get_content_type(file_path):
    """Look at the file ending (.png, .pdf ...) and return its MIME type."""
    extension = os.path.splitext(file_path)[1].lower()
    return MIME_TYPES.get(extension, "application/octet-stream")   # unknown -> download


def get_lan_ips():
    """Find this laptop's address(es) on the local network. Works with no internet."""
    found = []

    def add(ip):
        # ignore useless addresses: localhost, 0.0.0.0, and "no DHCP" 169.254.x.x
        if ip.startswith("127.") or ip == "0.0.0.0" or ip.startswith("169.254."):
            return
        if ip not in found:
            found.append(ip)

    # Way 1: ask the OS which address it would use to reach the network.
    # A UDP "connect" sends NO data, it only makes the OS choose a network card.
    probe = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        probe.connect(("10.255.255.255", 1))
        add(probe.getsockname()[0])
    except OSError:
        pass                                 # no network at all -> try way 2
    finally:
        probe.close()

    # Way 2: ask for every address that belongs to this computer's name
    try:
        for ip in socket.gethostbyname_ex(socket.gethostname())[2]:
            add(ip)
    except OSError:
        pass
    return found


def show_qr(url):
    """OPTIONAL: draw a QR code in the terminal (needs:  pip install qrcode)."""
    try:
        import qrcode                        # only works if you installed it
    except ImportError:
        print("  (Tip: run  pip install qrcode  to see a QR code here for your phone)")
        return
    try:
        qr = qrcode.QRCode(border=1)
        qr.add_data(url)
        qr.make(fit=True)
        qr.print_ascii(invert=True)          # invert=True looks right on dark terminals
    except Exception:
        print("  (Could not draw the QR code in this terminal - the links above still work)")


# ======================================================================
# 3. BUILDING AND SENDING HTTP RESPONSES
# ======================================================================

def build_headers(status_code, content_type, content_length, extra=None):
    """Create the 'header' part of an HTTP response (the text before the file)."""
    lines = ["HTTP/1.1 {} {}".format(status_code, STATUS_TEXT.get(status_code, "Unknown"))]
    lines.append("Content-Type: " + content_type)
    lines.append("Content-Length: " + str(content_length))   # how many bytes follow
    lines.append("Cache-Control: no-cache")                    # always show your latest edits
    lines.append("X-Content-Type-Options: nosniff")            # browser must trust our type
    lines.append("Connection: close")                          # one request per connection
    if extra:
        for name, value in extra.items():
            lines.append(name + ": " + value)
    # HTTP says: lines end with \r\n, and a blank line ends the header
    return ("\r\n".join(lines) + "\r\n\r\n").encode("iso-8859-1")


def render_page(title, heading, body):
    """Fill the HTML skeleton with real content."""
    page = PAGE_TEMPLATE.replace("{{TITLE}}", html_escape(title))
    page = page.replace("{{HEADING}}", html_escape(heading))
    page = page.replace("{{BODY}}", body)
    return page


def send_page(conn, status_code, html, head_only=False, extra=None):
    """Send an HTML page (folder list or error message) to the browser."""
    body = html.encode("utf-8")
    header = build_headers(status_code, "text/html; charset=utf-8", len(body), extra)
    if head_only:
        conn.sendall(header)                 # HEAD request: header only, no body
    else:
        conn.sendall(header + body)
    return status_code


def send_error_page(conn, status_code, message, head_only=False, extra=None):
    """Send a friendly error page such as '404 Not Found'."""
    title = "{} {}".format(status_code, STATUS_TEXT.get(status_code, "Error"))
    body = '<p class="note">' + html_escape(message) + "</p>"
    body += '<p><a href="/">Back to home</a></p>'
    html = render_page(title, title, body)
    return send_page(conn, status_code, html, head_only, extra)


def send_file(conn, file_path, head_only):
    """Send one file. Big files are streamed in chunks so memory stays small."""
    try:
        file_obj = open(file_path, "rb")     # "rb" = read the raw bytes
    except PermissionError:
        return send_error_page(conn, 403, "You are not allowed to open this file.", head_only)
    except OSError:
        return send_error_page(conn, 404, "This file could not be opened.", head_only)

    with file_obj:                           # "with" closes the file automatically
        size = os.path.getsize(file_path)
        conn.sendall(build_headers(200, get_content_type(file_path), size))
        if not head_only:
            while True:
                chunk = file_obj.read(CHUNK_SIZE)
                if not chunk:                # empty chunk = end of file
                    break
                conn.sendall(chunk)
    return 200


def build_listing_body(url_path, full_path):
    """Create the clickable list of files and folders for a directory."""
    entries = []
    for name in os.listdir(full_path):
        is_dir = os.path.isdir(os.path.join(full_path, name))
        # sort key: folders first (False < True), then A-Z ignoring upper/lower case
        entries.append((not is_dir, name.lower(), name, is_dir))
    entries.sort()

    rows = []
    if url_path != "/":
        rows.append('<li class="folder"><a href="../"><span>.. (parent folder)</span>'
                    '<span class="size"></span></a></li>')

    for _, _, name, is_dir in entries:
        if is_dir:
            link = url_encode(name) + "/"
            label = html_escape(name) + "/"
            size_text = "folder"
            css_class = "folder"
        else:
            link = url_encode(name)
            label = html_escape(name)
            css_class = "file"
            try:
                size_text = format_size(os.path.getsize(os.path.join(full_path, name)))
            except OSError:
                size_text = "?"
        rows.append('<li class="{}"><a href="{}"><span>{}</span><span class="size">{}</span></a></li>'
                    .format(css_class, link, label, size_text))

    if not entries:
        rows.append('<li class="empty">This folder is empty. Copy your files into it.</li>')

    note = '<p class="note">{} item(s)</p>'.format(len(entries))
    return note + "<ul>" + "".join(rows) + "</ul>"


# ======================================================================
# 4. UNDERSTANDING A REQUEST AND CHOOSING WHAT TO SEND
# ======================================================================

def resolve_path(url_path):
    """
    Turn '/dsa/sort.py' into the real file path on disk, but ONLY if it is
    inside the www folder. Returns None if someone tries to escape with '../'.
    """
    relative = url_path.lstrip("/")                          # '/dsa/a.py' -> 'dsa/a.py'
    full = os.path.realpath(os.path.join(WEB_ROOT, relative))  # clean '..' and shortcuts
    root = os.path.realpath(WEB_ROOT)
    full_cmp = os.path.normcase(full)                        # Windows ignores upper/lower case
    root_cmp = os.path.normcase(root)
    if full_cmp == root_cmp or full_cmp.startswith(root_cmp + os.sep):
        return full                                          # inside www: allowed
    return None                                              # outside www: blocked


def handle_request(conn, method, raw_target):
    """Decide what to answer. Always returns the status code that was sent."""
    # Only reading is supported: GET (page+body) and HEAD (header only)
    if method not in ("GET", "HEAD"):
        return send_error_page(conn, 405, "This server only supports GET and HEAD.",
                               extra={"Allow": "GET, HEAD"})
    head_only = (method == "HEAD")

    # '/dsa/a%20b.py?x=1' -> '/dsa/a%20b.py' (cut off ?query and #fragment)
    raw_path = raw_target.split("?", 1)[0].split("#", 1)[0]
    if not raw_path.startswith("/"):
        return send_error_page(conn, 400, "The address must start with '/'.", head_only)

    url_path = url_decode(raw_path)                          # '/dsa/a b.py'
    if "\x00" in url_path:                                   # NUL byte = attack attempt
        return send_error_page(conn, 400, "Bad characters in the address.", head_only)

    full_path = resolve_path(url_path)
    if full_path is None:
        return send_error_page(conn, 403, "Access outside the shared folder is blocked.", head_only)
    if not os.path.exists(full_path):
        return send_error_page(conn, 404, "Nothing exists at " + url_path, head_only)

    if os.path.isdir(full_path):
        # a folder address must end with '/', otherwise relative links would break
        if not raw_path.endswith("/"):
            location = "/" + raw_path.lstrip("/") + "/"
            return send_error_page(conn, 301, "Moved to " + location, head_only,
                                   extra={"Location": location})
        index_file = os.path.join(full_path, "index.html")
        if os.path.isfile(index_file):                       # a website folder (e.g. React build)
            return send_file(conn, index_file, head_only)
        heading = "Index of " + url_path                     # no index.html -> list the files
        html = render_page(heading, heading, build_listing_body(url_path, full_path))
        return send_page(conn, 200, html, head_only)

    return send_file(conn, full_path, head_only)             # it is a normal file


def read_request(conn):
    """Read bytes from the browser until the blank line that ends the header."""
    data = b""
    while b"\r\n\r\n" not in data:
        chunk = conn.recv(4096)                              # wait for up to 4096 bytes
        if not chunk:                                        # browser closed without finishing
            return None
        data += chunk
        if len(data) > MAX_HEADER_BYTES:                     # too big -> refuse
            return None
    return data


def handle_client(conn, addr):
    """Runs in its own thread: serve ONE browser request, then close."""
    status = None
    request_line = "-"
    try:
        conn.settimeout(CLIENT_TIMEOUT)                      # do not wait forever
        data = read_request(conn)
        if data is None:
            return                                           # nothing useful received
        # first line looks like:  GET /dsa/sort.py HTTP/1.1
        header_text = data.split(b"\r\n\r\n", 1)[0].decode("iso-8859-1")
        request_line = header_text.split("\r\n", 1)[0]
        parts = request_line.split(" ")
        if len(parts) != 3 or not parts[2].startswith("HTTP/"):
            status = send_error_page(conn, 400, "This does not look like an HTTP request.")
        else:
            method, target, _version = parts
            status = handle_request(conn, method, target)
    except OSError:
        pass                                                 # browser left / timed out: ignore
    except Exception as error:                               # our own bug: tell the browser
        print("  [error] {}: {}".format(type(error).__name__, error))
        try:
            status = send_error_page(conn, 500, "Something went wrong inside the server.")
        except OSError:
            pass
    finally:
        try:
            conn.shutdown(socket.SHUT_WR)                    # say "I'm done sending"
        except OSError:
            pass
        try:
            conn.close()                                     # free the connection
        except OSError:
            pass
        if status is not None:                               # one log line per request
            print("{}  {:<15} {:<3}  {}".format(
                time.strftime("%H:%M:%S"), addr[0], status, request_line))


# ======================================================================
# 5. STARTING THE SERVER
# ======================================================================

def main():
    port = PORT
    if len(sys.argv) > 1:                                    # python server.py 9000
        try:
            port = int(sys.argv[1])
        except ValueError:
            print("The port must be a number, for example:  python server.py 9000")
            return
        if port < 1 or port > 65535:
            print("The port must be between 1 and 65535.")
            return

    os.makedirs(WEB_ROOT, exist_ok=True)                     # create www/ if it is missing

    # Create the listening socket: AF_INET = IPv4, SOCK_STREAM = TCP
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if os.name == "nt":
        # Windows: forbid two programs from using the same port
        server.setsockopt(socket.SOL_SOCKET, socket.SO_EXCLUSIVEADDRUSE, 1)
    else:
        # Mac/Linux: allow quick restart of the server on the same port
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    try:
        server.bind((HOST, port))                            # claim the port number
    except OSError as error:
        print("Could not start on port {}: {}".format(port, error))
        print("Maybe it is already in use. Try another one:  python server.py 9000")
        server.close()
        return

    server.listen(50)                                        # allow 50 waiting visitors
    server.settimeout(1.0)                                   # wake up every second so Ctrl+C works

    print("=" * 60)
    print(" LocalServer is running")
    print(" Sharing folder : " + WEB_ROOT)
    print(" On this laptop : http://127.0.0.1:{}/".format(port))
    ips = get_lan_ips()
    if ips:
        for ip in ips:
            print(" Other devices  : http://{}:{}/".format(ip, port))
    else:
        print(" No network found, so only this laptop can open the server.")
    print(" Press Ctrl + C to stop")
    print("=" * 60)
    if ips:
        show_qr("http://{}:{}/".format(ips[0], port))

    try:
        while True:
            try:
                conn, addr = server.accept()                 # wait for a browser to knock
            except socket.timeout:
                continue                                     # nobody yet: loop again
            worker = threading.Thread(target=handle_client, args=(conn, addr), daemon=True)
            worker.start()                                   # serve it in the background
    except KeyboardInterrupt:
        print("\nServer stopped. Bye!")
    finally:
        server.close()


if __name__ == "__main__":     # run main() only when we start this file directly
    main()
