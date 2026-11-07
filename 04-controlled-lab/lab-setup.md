# Controlled Local Reconnaissance Lab

## Scope

Target: `127.0.0.1` (your own computer)

Service: Python standard-library HTTP server

Port: TCP `8000`

The server is explicitly bound to loopback, so it is not exposed to other devices on the LAN.

## Requirements

- Windows, Linux, or macOS
- Python 3
- Optional: Nmap, Wireshark, Burp Suite Community, OWASP ZAP

## 1. Start the local server

From this folder, run:

```bash
python start-local-server.py
```

Alternatively:

```bash
python -m http.server 8000 --bind 127.0.0.1
```

Keep the terminal open.

## 2. Open the lab page

Visit:

```text
http://127.0.0.1:8000
```

## 3. Verify the port

Windows CMD:

```cmd
netstat -ano | findstr :8000
```

Windows PowerShell:

```powershell
Test-NetConnection 127.0.0.1 -Port 8000
```

Linux/macOS:

```bash
ss -ltnp
```

## 4. Nmap check

```bash
nmap -p 8000 127.0.0.1
```

Expected while the server is running: TCP port 8000 should be reported as open.

## 5. Stop the server

Press `Ctrl+C` in the terminal running the server.

## Troubleshooting

- If port 8000 is already in use, stop the other local service or choose a different port and update the commands.
- If `python` is not recognized on Windows, install Python from https://www.python.org/downloads/windows/ and select the option to add Python to PATH. Open a new terminal afterwards.
- If Nmap is not recognized, confirm it is installed and open a new terminal.
- Loopback packet capture may require a dedicated loopback interface in Wireshark/Npcap.

## Safety

Do not bind the server to `0.0.0.0` for this exercise. Do not scan other devices or public addresses. Use active web scanning only on a purpose-built lab target with permission.
