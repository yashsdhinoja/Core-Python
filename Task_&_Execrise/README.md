# LocalServer

A small HTTP server written from scratch in Python (raw sockets, no web framework).
It shares everything inside the `www/` folder and works with no internet.

## Folder structure

```
LocalServer/
|-- venv/                  <- created by you (step 2 below)
|-- server.py              <- the server (all the code)
|-- requirements.txt       <- optional package (qrcode)
|-- start.bat              <- Windows: double-click to start
|-- start.sh               <- Mac/Linux: ./start.sh
|-- README.md
`-- www/                   <- ONLY this folder is shared
    |-- react-app/         <- contents of your React build (dist/ or build/)
    |-- dsa/               <- your DSA .py files (shown as text)
    `-- adv-dbms/          <- your Adv. DBMS PDF / SQL / notes
```

## Setup (one time)

Windows (Command Prompt):
```
cd LocalServer
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

Mac / Linux:
```
cd LocalServer
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

`pip install` needs internet only this one time. The server itself works fully offline,
and also runs if the optional qrcode package is missing.

## Run

```
python server.py          # port 8000
python server.py 9000     # another port
```

Open `http://127.0.0.1:8000/` in Chrome on the same laptop.
Other devices: open one of the "Other devices" links printed in the terminal
(they must be on the same network / hotspot as the laptop).
Stop with Ctrl + C.

## React project

1. In your React project run `npm run build`.
2. Vite: set `base: './'` in `vite.config.js` before building.
   Create React App: add `"homepage": "."` to `package.json` before building.
3. Copy everything inside `dist/` (or `build/`) into `www/react-app/`.
4. Use HashRouter instead of BrowserRouter if your app has several pages.
5. Open `http://127.0.0.1:8000/react-app/`.
