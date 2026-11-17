# 🛡️ Security Incident Response Report
**Analyst:** Thitsadaphone (Yayee) Phiakeo  
**Framework Used:** NIST Cybersecurity Framework (Detect, Respond, Recover)  
**Tools:** SIEM Log Analyzer, Network Packet Inspector  

---

## 1. Executive Summary
On November 10, 2026, SIEM monitoring tools triggered a high-severity alert indicating repeated failed SSH login attempts followed by a successful authentication from an unrecognized external IP address (`203.0.113.45`). Immediate containment measures were executed to block the malicious IP and secure the compromised workstation.

## 2. Incident Timeline (UTC+7)
* **08:14 AM:** SIEM detected 45 failed login attempts targeting `admin_user` within 2 minutes (Brute-force pattern).
* **08:16 AM:** Successful login recorded from external IP `203.0.113.45` on internal host `WS-FINANCE-04`.
* **08:19 AM:** Alert triaged and escalated to Tier 1 SOC Analyst; network traffic isolated.
* **08:25 AM:** Malicious IP blocked at the perimeter firewall; compromised user credentials revoked and reset.

## 3. Root Cause Analysis
The targeted account lacked Multi-Factor Authentication (MFA) and utilized a weak password policy, allowing an automated brute-force script to gain unauthorized access via an exposed SSH port.

## 4. Remediation & Recommendations
1. **Immediate Containment:** Blocked IP `203.0.113.45` across all firewalls and terminated active sessions.
2. **Access Control:** Enforced mandatory Multi-Factor Authentication (MFA) for all remote and administrative accounts.
3. **Hardening:** Disabled direct root login over SSH and implemented an account lockout policy after 5 failed attempts.
4. 
