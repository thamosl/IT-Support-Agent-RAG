# IT Support Knowledge Base — KB Articles

> Synthetic enterprise IT Support knowledge for RAG development. Validate all procedures, policies, commands, contacts, vendors, and SLA values against the real organization before production use.

## KB-0001: Password Reset

**Category:** Identity

### Symptoms
User cannot sign in after forgetting or expiring a password.

### Diagnostic sequence
1. Verify requester identity and business impact.
2. Capture exact error text, timestamp and affected resource.
3. Determine whether one user/device or multiple users are affected.
4. Check recent changes and known incidents.
5. Follow the applicable troubleshooting runbook.
6. Record every diagnostic result.
7. Apply only approved remediation.
8. Reproduce the original business task to verify recovery.

### Resolution guidance
Verify identity, check account state, use the approved reset flow, require MFA where applicable, and verify sign-in.

### Escalation criteria
Escalate when the issue is widespread, security-related, privileged, production-impacting, vendor-dependent, or unresolved after the approved procedure.

### Required ticket fields
User, department, device/hostname, platform, application/version, error code, impact, urgency, diagnostics, resolution, workaround, verification, assignment group, timestamps.
## KB-0002: Account Lockout

**Category:** Identity

### Symptoms
Account repeatedly becomes locked.

### Diagnostic sequence
1. Verify requester identity and business impact.
2. Capture exact error text, timestamp and affected resource.
3. Determine whether one user/device or multiple users are affected.
4. Check recent changes and known incidents.
5. Follow the applicable troubleshooting runbook.
6. Record every diagnostic result.
7. Apply only approved remediation.
8. Reproduce the original business task to verify recovery.

### Resolution guidance
Verify identity, determine whether stale credentials exist on phones, mapped drives or applications, unlock/reset through the approved workflow, then verify.

### Escalation criteria
Escalate when the issue is widespread, security-related, privileged, production-impacting, vendor-dependent, or unresolved after the approved procedure.

### Required ticket fields
User, department, device/hostname, platform, application/version, error code, impact, urgency, diagnostics, resolution, workaround, verification, assignment group, timestamps.
## KB-0003: MFA Failure

**Category:** Identity

### Symptoms
User cannot complete multi-factor authentication.

### Diagnostic sequence
1. Verify requester identity and business impact.
2. Capture exact error text, timestamp and affected resource.
3. Determine whether one user/device or multiple users are affected.
4. Check recent changes and known incidents.
5. Follow the applicable troubleshooting runbook.
6. Record every diagnostic result.
7. Apply only approved remediation.
8. Reproduce the original business task to verify recovery.

### Resolution guidance
Verify identity, inspect registered methods, device time/connectivity, authentication policy and approved recovery options.

### Escalation criteria
Escalate when the issue is widespread, security-related, privileged, production-impacting, vendor-dependent, or unresolved after the approved procedure.

### Required ticket fields
User, department, device/hostname, platform, application/version, error code, impact, urgency, diagnostics, resolution, workaround, verification, assignment group, timestamps.
## KB-0004: VPN Failure

**Category:** Network

### Symptoms
Remote employee cannot establish a VPN connection.

### Diagnostic sequence
1. Verify requester identity and business impact.
2. Capture exact error text, timestamp and affected resource.
3. Determine whether one user/device or multiple users are affected.
4. Check recent changes and known incidents.
5. Follow the applicable troubleshooting runbook.
6. Record every diagnostic result.
7. Apply only approved remediation.
8. Reproduce the original business task to verify recovery.

### Resolution guidance
Check Internet, identity, MFA, VPN profile, DNS, firewall/network path and client logs.

### Escalation criteria
Escalate when the issue is widespread, security-related, privileged, production-impacting, vendor-dependent, or unresolved after the approved procedure.

### Required ticket fields
User, department, device/hostname, platform, application/version, error code, impact, urgency, diagnostics, resolution, workaround, verification, assignment group, timestamps.
## KB-0005: Wi-Fi No Internet

**Category:** Network

### Symptoms
Device says connected but cannot reach services.

### Diagnostic sequence
1. Verify requester identity and business impact.
2. Capture exact error text, timestamp and affected resource.
3. Determine whether one user/device or multiple users are affected.
4. Check recent changes and known incidents.
5. Follow the applicable troubleshooting runbook.
6. Record every diagnostic result.
7. Apply only approved remediation.
8. Reproduce the original business task to verify recovery.

### Resolution guidance
Check IP, gateway, DNS, proxy and DHCP, then compare with a known-good device.

### Escalation criteria
Escalate when the issue is widespread, security-related, privileged, production-impacting, vendor-dependent, or unresolved after the approved procedure.

### Required ticket fields
User, department, device/hostname, platform, application/version, error code, impact, urgency, diagnostics, resolution, workaround, verification, assignment group, timestamps.
## KB-0006: DNS Failure

**Category:** Network

### Symptoms
Hostname does not resolve.

### Diagnostic sequence
1. Verify requester identity and business impact.
2. Capture exact error text, timestamp and affected resource.
3. Determine whether one user/device or multiple users are affected.
4. Check recent changes and known incidents.
5. Follow the applicable troubleshooting runbook.
6. Record every diagnostic result.
7. Apply only approved remediation.
8. Reproduce the original business task to verify recovery.

### Resolution guidance
Test direct IP reachability, gateway and resolver behavior with approved tools; determine whether failure is client or infrastructure.

### Escalation criteria
Escalate when the issue is widespread, security-related, privileged, production-impacting, vendor-dependent, or unresolved after the approved procedure.

### Required ticket fields
User, department, device/hostname, platform, application/version, error code, impact, urgency, diagnostics, resolution, workaround, verification, assignment group, timestamps.
## KB-0007: DHCP Failure

**Category:** Network

### Symptoms
Device has no valid corporate IP address.

### Diagnostic sequence
1. Verify requester identity and business impact.
2. Capture exact error text, timestamp and affected resource.
3. Determine whether one user/device or multiple users are affected.
4. Check recent changes and known incidents.
5. Follow the applicable troubleshooting runbook.
6. Record every diagnostic result.
7. Apply only approved remediation.
8. Reproduce the original business task to verify recovery.

### Resolution guidance
Inspect adapter and address, renew lease, verify network segment/VLAN and escalate to Network Operations if required.

### Escalation criteria
Escalate when the issue is widespread, security-related, privileged, production-impacting, vendor-dependent, or unresolved after the approved procedure.

### Required ticket fields
User, department, device/hostname, platform, application/version, error code, impact, urgency, diagnostics, resolution, workaround, verification, assignment group, timestamps.
## KB-0008: Outlook Disconnected

**Category:** Microsoft 365

### Symptoms
Outlook displays Disconnected or repeatedly asks for credentials.

### Diagnostic sequence
1. Verify requester identity and business impact.
2. Capture exact error text, timestamp and affected resource.
3. Determine whether one user/device or multiple users are affected.
4. Check recent changes and known incidents.
5. Follow the applicable troubleshooting runbook.
6. Record every diagnostic result.
7. Apply only approved remediation.
8. Reproduce the original business task to verify recovery.

### Resolution guidance
Check connectivity, service health, authentication, cached mode, profile and recent changes.

### Escalation criteria
Escalate when the issue is widespread, security-related, privileged, production-impacting, vendor-dependent, or unresolved after the approved procedure.

### Required ticket fields
User, department, device/hostname, platform, application/version, error code, impact, urgency, diagnostics, resolution, workaround, verification, assignment group, timestamps.
## KB-0009: Outlook Mail Not Sending

**Category:** Microsoft 365

### Symptoms
Messages remain queued or fail to send.

### Diagnostic sequence
1. Verify requester identity and business impact.
2. Capture exact error text, timestamp and affected resource.
3. Determine whether one user/device or multiple users are affected.
4. Check recent changes and known incidents.
5. Follow the applicable troubleshooting runbook.
6. Record every diagnostic result.
7. Apply only approved remediation.
8. Reproduce the original business task to verify recovery.

### Resolution guidance
Check connectivity, mailbox state, attachment restrictions, service health, authentication and error text.

### Escalation criteria
Escalate when the issue is widespread, security-related, privileged, production-impacting, vendor-dependent, or unresolved after the approved procedure.

### Required ticket fields
User, department, device/hostname, platform, application/version, error code, impact, urgency, diagnostics, resolution, workaround, verification, assignment group, timestamps.
## KB-0010: Teams Audio Failure

**Category:** Microsoft 365

### Symptoms
Microphone or speaker does not work in Teams.

### Diagnostic sequence
1. Verify requester identity and business impact.
2. Capture exact error text, timestamp and affected resource.
3. Determine whether one user/device or multiple users are affected.
4. Check recent changes and known incidents.
5. Follow the applicable troubleshooting runbook.
6. Record every diagnostic result.
7. Apply only approved remediation.
8. Reproduce the original business task to verify recovery.

### Resolution guidance
Check OS permissions, Teams device selection, mute state, drivers and alternate client testing.

### Escalation criteria
Escalate when the issue is widespread, security-related, privileged, production-impacting, vendor-dependent, or unresolved after the approved procedure.

### Required ticket fields
User, department, device/hostname, platform, application/version, error code, impact, urgency, diagnostics, resolution, workaround, verification, assignment group, timestamps.
## KB-0011: OneDrive Sync Failure

**Category:** Microsoft 365

### Symptoms
Files remain pending or fail to synchronize.

### Diagnostic sequence
1. Verify requester identity and business impact.
2. Capture exact error text, timestamp and affected resource.
3. Determine whether one user/device or multiple users are affected.
4. Check recent changes and known incidents.
5. Follow the applicable troubleshooting runbook.
6. Record every diagnostic result.
7. Apply only approved remediation.
8. Reproduce the original business task to verify recovery.

### Resolution guidance
Check sign-in, storage, filename/path restrictions, sync state, conflicts and client health.

### Escalation criteria
Escalate when the issue is widespread, security-related, privileged, production-impacting, vendor-dependent, or unresolved after the approved procedure.

### Required ticket fields
User, department, device/hostname, platform, application/version, error code, impact, urgency, diagnostics, resolution, workaround, verification, assignment group, timestamps.
## KB-0012: SharePoint Access Denied

**Category:** Microsoft 365

### Symptoms
User cannot open a site, library or document.

### Diagnostic sequence
1. Verify requester identity and business impact.
2. Capture exact error text, timestamp and affected resource.
3. Determine whether one user/device or multiple users are affected.
4. Check recent changes and known incidents.
5. Follow the applicable troubleshooting runbook.
6. Record every diagnostic result.
7. Apply only approved remediation.
8. Reproduce the original business task to verify recovery.

### Resolution guidance
Verify URL, identity, membership, permissions and owner approval; distinguish authentication from authorization.

### Escalation criteria
Escalate when the issue is widespread, security-related, privileged, production-impacting, vendor-dependent, or unresolved after the approved procedure.

### Required ticket fields
User, department, device/hostname, platform, application/version, error code, impact, urgency, diagnostics, resolution, workaround, verification, assignment group, timestamps.
## KB-0013: Printer Offline

**Category:** Endpoint

### Symptoms
Network printer shows Offline.

### Diagnostic sequence
1. Verify requester identity and business impact.
2. Capture exact error text, timestamp and affected resource.
3. Determine whether one user/device or multiple users are affected.
4. Check recent changes and known incidents.
5. Follow the applicable troubleshooting runbook.
6. Record every diagnostic result.
7. Apply only approved remediation.
8. Reproduce the original business task to verify recovery.

### Resolution guidance
Check power, network reachability, queue, spooler, driver and print-server state.

### Escalation criteria
Escalate when the issue is widespread, security-related, privileged, production-impacting, vendor-dependent, or unresolved after the approved procedure.

### Required ticket fields
User, department, device/hostname, platform, application/version, error code, impact, urgency, diagnostics, resolution, workaround, verification, assignment group, timestamps.
## KB-0014: Laptop Slow

**Category:** Endpoint

### Symptoms
Laptop is slow during normal work.

### Diagnostic sequence
1. Verify requester identity and business impact.
2. Capture exact error text, timestamp and affected resource.
3. Determine whether one user/device or multiple users are affected.
4. Check recent changes and known incidents.
5. Follow the applicable troubleshooting runbook.
6. Record every diagnostic result.
7. Apply only approved remediation.
8. Reproduce the original business task to verify recovery.

### Resolution guidance
Measure CPU, RAM, disk, storage, startup applications, updates and security status before changing anything.

### Escalation criteria
Escalate when the issue is widespread, security-related, privileged, production-impacting, vendor-dependent, or unresolved after the approved procedure.

### Required ticket fields
User, department, device/hostname, platform, application/version, error code, impact, urgency, diagnostics, resolution, workaround, verification, assignment group, timestamps.
## KB-0015: Blue Screen

**Category:** Endpoint

### Symptoms
Windows crashes with a stop code.

### Diagnostic sequence
1. Verify requester identity and business impact.
2. Capture exact error text, timestamp and affected resource.
3. Determine whether one user/device or multiple users are affected.
4. Check recent changes and known incidents.
5. Follow the applicable troubleshooting runbook.
6. Record every diagnostic result.
7. Apply only approved remediation.
8. Reproduce the original business task to verify recovery.

### Resolution guidance
Capture stop code, recent changes, driver/update history, Event Viewer/minidump and hardware diagnostics.

### Escalation criteria
Escalate when the issue is widespread, security-related, privileged, production-impacting, vendor-dependent, or unresolved after the approved procedure.

### Required ticket fields
User, department, device/hostname, platform, application/version, error code, impact, urgency, diagnostics, resolution, workaround, verification, assignment group, timestamps.
## KB-0016: Laptop Boot Failure

**Category:** Hardware

### Symptoms
Laptop will not start normally.

### Diagnostic sequence
1. Verify requester identity and business impact.
2. Capture exact error text, timestamp and affected resource.
3. Determine whether one user/device or multiple users are affected.
4. Check recent changes and known incidents.
5. Follow the applicable troubleshooting runbook.
6. Record every diagnostic result.
7. Apply only approved remediation.
8. Reproduce the original business task to verify recovery.

### Resolution guidance
Check power, charger, external devices, POST indicators and recovery environment before hardware escalation.

### Escalation criteria
Escalate when the issue is widespread, security-related, privileged, production-impacting, vendor-dependent, or unresolved after the approved procedure.

### Required ticket fields
User, department, device/hostname, platform, application/version, error code, impact, urgency, diagnostics, resolution, workaround, verification, assignment group, timestamps.
## KB-0017: Shared Folder Access

**Category:** IAM

### Symptoms
User receives Access Denied on a corporate folder.

### Diagnostic sequence
1. Verify requester identity and business impact.
2. Capture exact error text, timestamp and affected resource.
3. Determine whether one user/device or multiple users are affected.
4. Check recent changes and known incidents.
5. Follow the applicable troubleshooting runbook.
6. Record every diagnostic result.
7. Apply only approved remediation.
8. Reproduce the original business task to verify recovery.

### Resolution guidance
Verify exact path, identity, connectivity, group membership, ACL ownership and approval.

### Escalation criteria
Escalate when the issue is widespread, security-related, privileged, production-impacting, vendor-dependent, or unresolved after the approved procedure.

### Required ticket fields
User, department, device/hostname, platform, application/version, error code, impact, urgency, diagnostics, resolution, workaround, verification, assignment group, timestamps.
## KB-0018: Phishing

**Category:** Security

### Symptoms
Employee receives suspicious email or link.

### Diagnostic sequence
1. Verify requester identity and business impact.
2. Capture exact error text, timestamp and affected resource.
3. Determine whether one user/device or multiple users are affected.
4. Check recent changes and known incidents.
5. Follow the applicable troubleshooting runbook.
6. Record every diagnostic result.
7. Apply only approved remediation.
8. Reproduce the original business task to verify recovery.

### Resolution guidance
Do not click, preserve the message, report it, determine exposure and escalate to Security.

### Escalation criteria
Escalate when the issue is widespread, security-related, privileged, production-impacting, vendor-dependent, or unresolved after the approved procedure.

### Required ticket fields
User, department, device/hostname, platform, application/version, error code, impact, urgency, diagnostics, resolution, workaround, verification, assignment group, timestamps.
## KB-0019: Malware Alert

**Category:** Security

### Symptoms
Endpoint security reports malicious behavior.

### Diagnostic sequence
1. Verify requester identity and business impact.
2. Capture exact error text, timestamp and affected resource.
3. Determine whether one user/device or multiple users are affected.
4. Check recent changes and known incidents.
5. Follow the applicable troubleshooting runbook.
6. Record every diagnostic result.
7. Apply only approved remediation.
8. Reproduce the original business task to verify recovery.

### Resolution guidance
Preserve evidence, isolate according to policy, capture alert details and escalate.

### Escalation criteria
Escalate when the issue is widespread, security-related, privileged, production-impacting, vendor-dependent, or unresolved after the approved procedure.

### Required ticket fields
User, department, device/hostname, platform, application/version, error code, impact, urgency, diagnostics, resolution, workaround, verification, assignment group, timestamps.
## KB-0020: Lost Corporate Device

**Category:** Security

### Symptoms
Company laptop or mobile device is missing.

### Diagnostic sequence
1. Verify requester identity and business impact.
2. Capture exact error text, timestamp and affected resource.
3. Determine whether one user/device or multiple users are affected.
4. Check recent changes and known incidents.
5. Follow the applicable troubleshooting runbook.
6. Record every diagnostic result.
7. Apply only approved remediation.
8. Reproduce the original business task to verify recovery.

### Resolution guidance
Report immediately, identify asset, protect account/device using approved controls and document incident.

### Escalation criteria
Escalate when the issue is widespread, security-related, privileged, production-impacting, vendor-dependent, or unresolved after the approved procedure.

### Required ticket fields
User, department, device/hostname, platform, application/version, error code, impact, urgency, diagnostics, resolution, workaround, verification, assignment group, timestamps.
## KB-0021: Application Crash

**Category:** Application

### Symptoms
Business application closes or becomes unresponsive.

### Diagnostic sequence
1. Verify requester identity and business impact.
2. Capture exact error text, timestamp and affected resource.
3. Determine whether one user/device or multiple users are affected.
4. Check recent changes and known incidents.
5. Follow the applicable troubleshooting runbook.
6. Record every diagnostic result.
7. Apply only approved remediation.
8. Reproduce the original business task to verify recovery.

### Resolution guidance
Reproduce, confirm version, check recent changes and logs, compare known-good state, then escalate.

### Escalation criteria
Escalate when the issue is widespread, security-related, privileged, production-impacting, vendor-dependent, or unresolved after the approved procedure.

### Required ticket fields
User, department, device/hostname, platform, application/version, error code, impact, urgency, diagnostics, resolution, workaround, verification, assignment group, timestamps.
## KB-0022: Certificate Warning

**Category:** Infrastructure

### Symptoms
Browser or application reports certificate warning.

### Diagnostic sequence
1. Verify requester identity and business impact.
2. Capture exact error text, timestamp and affected resource.
3. Determine whether one user/device or multiple users are affected.
4. Check recent changes and known incidents.
5. Follow the applicable troubleshooting runbook.
6. Record every diagnostic result.
7. Apply only approved remediation.
8. Reproduce the original business task to verify recovery.

### Resolution guidance
Do not bypass security warning; capture hostname, expiry/chain details and escalate to certificate owner.

### Escalation criteria
Escalate when the issue is widespread, security-related, privileged, production-impacting, vendor-dependent, or unresolved after the approved procedure.

### Required ticket fields
User, department, device/hostname, platform, application/version, error code, impact, urgency, diagnostics, resolution, workaround, verification, assignment group, timestamps.
## KB-0023: Remote Desktop Failure

**Category:** Infrastructure

### Symptoms
RDP connection cannot be established.

### Diagnostic sequence
1. Verify requester identity and business impact.
2. Capture exact error text, timestamp and affected resource.
3. Determine whether one user/device or multiple users are affected.
4. Check recent changes and known incidents.
5. Follow the applicable troubleshooting runbook.
6. Record every diagnostic result.
7. Apply only approved remediation.
8. Reproduce the original business task to verify recovery.

### Resolution guidance
Check target availability, VPN/network, permission, RDP service, firewall and NLA.

### Escalation criteria
Escalate when the issue is widespread, security-related, privileged, production-impacting, vendor-dependent, or unresolved after the approved procedure.

### Required ticket fields
User, department, device/hostname, platform, application/version, error code, impact, urgency, diagnostics, resolution, workaround, verification, assignment group, timestamps.
## KB-0024: Mobile Enrollment

**Category:** MDM

### Symptoms
Corporate mobile device cannot enroll.

### Diagnostic sequence
1. Verify requester identity and business impact.
2. Capture exact error text, timestamp and affected resource.
3. Determine whether one user/device or multiple users are affected.
4. Check recent changes and known incidents.
5. Follow the applicable troubleshooting runbook.
6. Record every diagnostic result.
7. Apply only approved remediation.
8. Reproduce the original business task to verify recovery.

### Resolution guidance
Verify ownership, OS, identity, enrollment policy, management status and network.

### Escalation criteria
Escalate when the issue is widespread, security-related, privileged, production-impacting, vendor-dependent, or unresolved after the approved procedure.

### Required ticket fields
User, department, device/hostname, platform, application/version, error code, impact, urgency, diagnostics, resolution, workaround, verification, assignment group, timestamps.
## KB-0025: Database Connection

**Category:** Database

### Symptoms
Application cannot connect to database.

### Diagnostic sequence
1. Verify requester identity and business impact.
2. Capture exact error text, timestamp and affected resource.
3. Determine whether one user/device or multiple users are affected.
4. Check recent changes and known incidents.
5. Follow the applicable troubleshooting runbook.
6. Record every diagnostic result.
7. Apply only approved remediation.
8. Reproduce the original business task to verify recovery.

### Resolution guidance
Confirm host/port, account, network, database state and logs without making destructive changes.

### Escalation criteria
Escalate when the issue is widespread, security-related, privileged, production-impacting, vendor-dependent, or unresolved after the approved procedure.

### Required ticket fields
User, department, device/hostname, platform, application/version, error code, impact, urgency, diagnostics, resolution, workaround, verification, assignment group, timestamps.
## KB-0026: Cloud Resource Unavailable

**Category:** Cloud

### Symptoms
Cloud resource cannot be reached.

### Diagnostic sequence
1. Verify requester identity and business impact.
2. Capture exact error text, timestamp and affected resource.
3. Determine whether one user/device or multiple users are affected.
4. Check recent changes and known incidents.
5. Follow the applicable troubleshooting runbook.
6. Record every diagnostic result.
7. Apply only approved remediation.
8. Reproduce the original business task to verify recovery.

### Resolution guidance
Confirm resource and subscription, service health, identity, network, recent changes and dependency status.

### Escalation criteria
Escalate when the issue is widespread, security-related, privileged, production-impacting, vendor-dependent, or unresolved after the approved procedure.

### Required ticket fields
User, department, device/hostname, platform, application/version, error code, impact, urgency, diagnostics, resolution, workaround, verification, assignment group, timestamps.
## KB-0027: Disk Full

**Category:** Endpoint

### Symptoms
System disk is nearly full.

### Diagnostic sequence
1. Verify requester identity and business impact.
2. Capture exact error text, timestamp and affected resource.
3. Determine whether one user/device or multiple users are affected.
4. Check recent changes and known incidents.
5. Follow the applicable troubleshooting runbook.
6. Record every diagnostic result.
7. Apply only approved remediation.
8. Reproduce the original business task to verify recovery.

### Resolution guidance
Identify volume and approved cleanup candidates, check retention rules, remove/archive safely or request capacity expansion.

### Escalation criteria
Escalate when the issue is widespread, security-related, privileged, production-impacting, vendor-dependent, or unresolved after the approved procedure.

### Required ticket fields
User, department, device/hostname, platform, application/version, error code, impact, urgency, diagnostics, resolution, workaround, verification, assignment group, timestamps.
## KB-0028: Browser Certificate/Proxy

**Category:** Network

### Symptoms
Corporate browser cannot open an internal or external site.

### Diagnostic sequence
1. Verify requester identity and business impact.
2. Capture exact error text, timestamp and affected resource.
3. Determine whether one user/device or multiple users are affected.
4. Check recent changes and known incidents.
5. Follow the applicable troubleshooting runbook.
6. Record every diagnostic result.
7. Apply only approved remediation.
8. Reproduce the original business task to verify recovery.

### Resolution guidance
Check DNS, proxy, certificate chain, browser policy and alternate supported browser.

### Escalation criteria
Escalate when the issue is widespread, security-related, privileged, production-impacting, vendor-dependent, or unresolved after the approved procedure.

### Required ticket fields
User, department, device/hostname, platform, application/version, error code, impact, urgency, diagnostics, resolution, workaround, verification, assignment group, timestamps.
## KB-0029: Shared Mailbox

**Category:** Microsoft 365

### Symptoms
User cannot open or send from shared mailbox.

### Diagnostic sequence
1. Verify requester identity and business impact.
2. Capture exact error text, timestamp and affected resource.
3. Determine whether one user/device or multiple users are affected.
4. Check recent changes and known incidents.
5. Follow the applicable troubleshooting runbook.
6. Record every diagnostic result.
7. Apply only approved remediation.
8. Reproduce the original business task to verify recovery.

### Resolution guidance
Verify mailbox existence, permissions, licensing requirements and Outlook/OWA behavior.

### Escalation criteria
Escalate when the issue is widespread, security-related, privileged, production-impacting, vendor-dependent, or unresolved after the approved procedure.

### Required ticket fields
User, department, device/hostname, platform, application/version, error code, impact, urgency, diagnostics, resolution, workaround, verification, assignment group, timestamps.
