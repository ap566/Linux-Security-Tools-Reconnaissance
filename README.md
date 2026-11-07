# Linux, Security Tools & Reconnaissance

A beginner-friendly cybersecurity learning repository covering Linux fundamentals, essential security tools, passive and active reconnaissance, and a controlled local reconnaissance lab.

> **Authorized-use only:** Run active scans and security tests only against systems you own or have explicit permission to assess. The examples in this repository use localhost (`127.0.0.1`) wherever possible.

## Learning objectives

- Navigate Linux files and directories.
- Understand Linux permissions, users, groups, and processes.
- Practice basic Linux security and system administration.
- Use Nmap for authorized port discovery.
- Use Wireshark to inspect network traffic.
- Use Burp Suite Community to inspect HTTP requests.
- Use OWASP ZAP to review a deliberately local web target.
- Understand passive vs active reconnaissance and DNS records.
- Build and document a controlled localhost lab.

## Repository structure

```text
Linux-Security-Tools-Reconnaissance/
├── README.md
├── 01-linux-fundamentals/
│   └── linux-basics.md
├── 02-security-tools/
│   └── tools-guide.md
├── 03-reconnaissance/
│   └── reconnaissance-guide.md
├── 04-controlled-lab/
│   ├── lab-setup.md
│   └── start-local-server.py
├── 05-reports/
│   └── findings-template.md
└── screenshots/
    └── README.md
```

## Getting started

1. Read `01-linux-fundamentals/linux-basics.md`.
2. Review installation and usage notes in `02-security-tools/tools-guide.md`.
3. Study passive and active reconnaissance in `03-reconnaissance/reconnaissance-guide.md`.
4. Follow `04-controlled-lab/lab-setup.md`.
5. Record only observations you actually verified in `05-reports/findings-template.md`.
6. Add your own screenshots to `screenshots/`.

## Lab target

The starter lab uses a Python HTTP server bound to `127.0.0.1` on TCP port `8000`. Binding to loopback keeps the service reachable only from the same computer.

## Tools

- Linux shell utilities
- Nmap
- Wireshark
- Burp Suite Community Edition
- OWASP ZAP
- Python 3

## Disclaimer

This repository is for education and authorized defensive security testing. Do not use these techniques to scan, intercept, or test third-party systems without permission. Tool output can be incomplete or misleading; validate findings before reporting them.
