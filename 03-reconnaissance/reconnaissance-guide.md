# Reconnaissance: Passive, Active, DNS, and Enumeration

## 1. Reconnaissance

Reconnaissance is information gathering performed before or during an authorized security assessment.

### Passive reconnaissance

Collects information from public or third-party sources without directly probing the target's systems. Examples include reviewing public documentation, public registration data, and published DNS information. Public services may still log queries.

### Active reconnaissance

Interacts directly with the target, for example by testing connectivity, checking ports, or requesting service information. It is more likely to be logged and requires explicit authorization.

## 2. DNS record types

| Record | Meaning |
|---|---|
| A | Domain to IPv4 address |
| AAAA | Domain to IPv6 address |
| MX | Mail exchange server |
| NS | Authoritative name server |
| CNAME | Canonical name / alias |
| TXT | Text data, often used for verification and email policy |
| SOA | DNS zone authority information |

Example lookups for a domain you are allowed to research:

```bash
nslookup example.com
nslookup -type=MX example.com
nslookup -type=NS example.com
```

On systems with `dig`:

```bash
dig example.com A
dig example.com MX
dig example.com NS
```

WHOIS/RDAP registration data can be checked through the ICANN lookup service: https://lookup.icann.org/

## 3. Network enumeration concepts

- Host discovery: identify reachable systems.
- Port enumeration: determine which ports accept connections.
- Service identification: infer what service may be listening.
- Version detection: identify software versions where authorized.

A port state is time-dependent. `open` means a service accepted the probe; `closed` means reachable but no application accepted it; `filtered` means a firewall or network behavior prevented a clear result.

## 4. Safe local examples

Check loopback:

```bash
ping 127.0.0.1
```

Check a local TCP port:

```bash
nmap -p 8000 127.0.0.1
```

On Windows PowerShell:

```powershell
Test-NetConnection 127.0.0.1 -Port 8000
```

On Windows CMD:

```cmd
netstat -ano
```

## 5. Rules of engagement

Before any active test, document:

- Written authorization and scope.
- Exact target IPs/domains.
- Allowed tools and scan intensity.
- Approved time window.
- Prohibited actions.
- Emergency contact and stop condition.

Never scan public or third-party targets just because they respond to a ping or appear in search results.
