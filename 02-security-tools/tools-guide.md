# Essential Security Tools

Use these tools only on your own systems or targets for which you have explicit permission.

## 1. Nmap

Purpose: discover hosts, ports, and services during authorized assessments.

Check installation:

```bash
nmap --version
```

Scan only the local machine:

```bash
nmap 127.0.0.1
```

Check the controlled lab's port:

```bash
nmap -p 8000 127.0.0.1
```

Save a normal text report:

```bash
nmap -p 8000 127.0.0.1 -oN nmap-results.txt
```

An `open` result means a TCP service accepted the connection at scan time. A service label is an estimate, not proof of the application identity.

Official site: https://nmap.org/

## 2. Wireshark

Purpose: capture and inspect network packets.

Basic workflow:

1. Open Wireshark.
2. Select the correct capture interface.
3. Start capture.
4. Generate traffic in your own lab.
5. Stop capture and apply a display filter.

Useful display filters:

```text
dns
tcp
icmp
http
```

Loopback traffic may require a loopback capture interface/driver. A Wi-Fi capture interface may not show traffic sent to `127.0.0.1`. HTTPS application content is encrypted in normal captures.

Official site: https://www.wireshark.org/

## 3. Burp Suite Community Edition

Purpose: inspect web requests and responses through an intercepting proxy.

Beginner workflow:

1. Start Burp Suite Community Edition.
2. Create a temporary project and use defaults.
3. Open Burp's built-in browser.
4. Browse only to your local lab URL: `http://127.0.0.1:8000`.
5. Inspect Proxy > HTTP history.
6. Review request methods, paths, status codes, and headers.

Official site: https://portswigger.net/burp/communitydownload

## 4. OWASP ZAP

Purpose: test web application security and review potential findings.

Beginner workflow:

1. Start ZAP and create a temporary session.
2. Browse your own local lab site through ZAP.
3. Review the Sites and Alerts panels.
4. Record the alert, evidence, and context.
5. Do not treat every alert as a confirmed vulnerability.

Active scanning sends test requests and may alter application data. Use it only against a deliberately created lab application or a system you are authorized to test.

Official site: https://www.zaproxy.org/

## Comparison

| Tool | Main purpose |
|---|---|
| Nmap | Network and port discovery |
| Wireshark | Packet capture and protocol analysis |
| Burp Suite | Manual web request/response inspection |
| OWASP ZAP | Web application security testing |
