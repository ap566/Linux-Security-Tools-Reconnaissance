# Reconnaissance Lab – Findings Record

**Student:**  
**Date:**  
**Operating system:**  
**Lab scope:** `127.0.0.1` only  
**Authorization:** Personal localhost lab

## Tools used

- [ ] Nmap
- [ ] Wireshark
- [ ] Burp Suite Community
- [ ] OWASP ZAP
- [ ] Windows CMD / PowerShell or Linux shell

## Test log

| Date/time | Tool | Target | Command/action | Actual result | Evidence file |
|---|---|---|---|---|---|
| | | | | | |

## Finding record

**Finding ID:**  
**Title:**  
**Affected asset:**  
**Tool and method:**  
**Evidence:**  
**Observed result:**  
**Security impact:**  
**Severity:** Informational / Low / Medium / High / Critical  
**Recommendation:**  
**Validation status:** Confirmed / Needs review / False positive

## Example informational observation

**Title:** Local HTTP service detected on TCP port 8000

**Target:** `127.0.0.1`

**Evidence:** Nmap reported TCP port 8000 as open while the local Python server was running.

**Impact:** A listening service is a network entry point. Its exposure should match the intended scope.

**Recommendation:** Stop development services when not needed and bind local-only services to loopback when remote access is unnecessary.

**Severity:** Informational

## Conclusion

Summarize what was tested, what was actually observed, any limitations, and recommended defensive improvements. Do not claim that a vulnerability exists unless evidence supports it.
