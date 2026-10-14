# Offline Study Hub (Python)

A small offline-first dashboard served by Python's standard library. It needs no third-party Python packages.

## 1. Requirements
- Windows 10/11
- Python 3.10+ installed and available as `py` or `python`
- Chrome (or another browser)

## 2. Create and activate a virtual environment

Open PowerShell in this folder:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, use this for the current terminal only:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

There are no third-party packages to install. The app uses Python's standard library.

## 3. Add your materials

Copy files into:
- `materials\react-project\`
- `materials\dsa-python\`
- `materials\advanced-dbms\`

You can keep subfolders. Refresh the dashboard after copying files.

### React project
- Copying React source lets you store and browse its files, but Chrome cannot run JSX/TSX source directly.
- If you already have Node.js installed, build the React project using its own instructions, then copy the production build output (often `dist` or `build`) into `materials\react-project\`.
- This starter provides file listing and opening. It does not yet provide a React development/build toolchain.

## 4. Run on this PC only (recommended first)

```powershell
python app.py
```

Open Chrome at:

`http://127.0.0.1:8000`

Keep the terminal open while using the site. Press `Ctrl+C` to stop it.

## 5. Use from another device on the same Wi-Fi or hotspot

Only do this on a trusted local network:

```powershell
python app.py --host 0.0.0.0
```

Find the PC's IPv4 address with:

```powershell
ipconfig
```

On the other device, open `http://PC-IP-ADDRESS:8000`, replacing the example with the PC's actual IPv4 address.

Both devices must be on a network that permits device-to-device traffic. College Wi-Fi may block it. If Windows Firewall prompts you, allow access only on a trusted Private network. Do not expose this server to public networks or the internet.

## Security and limitations
- This app is intended for personal use on your own computer or trusted local network.
- It does not bypass a college Wi-Fi captive portal or network access policy.
- It does not execute `.py` files from the browser. That feature should be added separately with strict safeguards if needed.
- Do not put passwords, private keys, or confidential files in the materials folders.
