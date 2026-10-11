# IT Support Handbook

**Document Type:** Enterprise IT Support Knowledge Base  
**Version:** 4.2  
**Effective Date:** October 2026  
**Classification:** Internal Use  
**Organization:** Northstar Technologies Pvt. Ltd.  
**Primary Support Region:** India  
**Support Hours:** 08:00–20:00 IST, Monday–Friday; 24×7 support for P1 incidents  
**Document Owner:** IT Service Management Team

---

## 1. Purpose and Scope

This handbook is a practical reference for employees, service-desk analysts, desktop-support engineers, infrastructure engineers, application-support teams, and IT managers. It describes standard procedures for diagnosing, resolving, documenting, escalating, and preventing common enterprise technology problems.

The handbook is intentionally written as operational knowledge rather than as a product manual. Procedures may vary by business unit, operating system version, device model, security policy, or application version. When a procedure conflicts with an approved security policy, change-management record, vendor instruction, or emergency directive, the approved policy takes precedence.

This handbook covers:

- User accounts, passwords, MFA, SSO, and identity services
- Windows and macOS endpoint support
- Laptops, desktops, monitors, docks, keyboards, mice, and headsets
- Corporate Wi-Fi, wired LAN, DNS, DHCP, proxy, and VPN
- Microsoft 365 services including Outlook, Teams, OneDrive, and SharePoint
- Printers, scanners, meeting rooms, and conferencing equipment
- Approved software installation and application troubleshooting
- Endpoint security, phishing, malware, and suspicious activity
- Remote support
- IT asset management
- Employee onboarding, transfers, and offboarding
- Ticket handling, SLAs, prioritization, escalation, and communication
- Backup, recovery, data-loss incidents, and business continuity
- Incident, problem, request, and change management
- Common troubleshooting runbooks
- Frequently asked questions and realistic ticket examples

This handbook uses fictional organization names, systems, hostnames, ticket numbers, employee names, IP ranges, and examples. They are safe test data and must not be interpreted as real credentials or production configuration.


## 2. Support Operating Model

### 2.1 Support Tiers

**Tier 0 – Self Service**

Employees use the IT portal, password-reset portal, knowledge base, software catalog, and automated diagnostics. Examples include password reset, approved software installation, VPN setup, and printer mapping.

**Tier 1 – Service Desk**

Tier 1 validates the requester, gathers symptoms, checks known incidents, performs standard troubleshooting, documents the ticket, and resolves common issues. Tier 1 should not make unauthorized infrastructure or security changes.

**Tier 2 – Specialist Support**

Tier 2 handles problems requiring deeper technical knowledge. Typical teams include:

- Endpoint Engineering
- Network Operations
- Identity and Access Management
- Microsoft 365 Administration
- Server and Infrastructure Operations
- Database Administration
- Application Support
- Security Operations

**Tier 3 – Engineering/Vendor**

Tier 3 handles software defects, infrastructure architecture, complex outages, vendor escalation, source-code issues, and changes requiring engineering ownership.

### 2.2 Service Desk Workflow

1. Receive request through approved channel.
2. Create or identify the ticket.
3. Validate requester identity when required.
4. Classify the ticket.
5. Determine impact and urgency.
6. Search for known incidents and existing knowledge articles.
7. Collect exact symptoms and timestamps.
8. Perform approved troubleshooting.
9. Document each meaningful action and result.
10. Resolve, escalate, or create a problem record.
11. Confirm resolution when practical.
12. Record final resolution and closure code.

### 2.3 Ticket Documentation Standard

Every ticket should answer:

- Who is affected?
- What service is affected?
- What exactly is failing?
- When did it start?
- Is the problem reproducible?
- What changed before the issue appeared?
- What troubleshooting has already been performed?
- What was the result of each test?
- What is the business impact?
- What is the next action?
- Who owns the next action?

Avoid notes such as "fixed", "done", or "user issue". Instead write observable facts.

**Weak note:**

> Internet fixed.

**Good note:**

> User reported inability to access internal applications from office Wi-Fi beginning at approximately 10:15 IST. Device received 10.20.14.83 from DHCP. Gateway 10.20.14.1 responded to ping, but DNS queries to the corporate resolver timed out. Reconnected to Wi-Fi and renewed DHCP lease. DNS resolution recovered and user confirmed access to intranet and Teams. No further action required.


## 3. Incident Priority and SLA

### P1 – Critical

A widespread or business-critical outage with severe operational impact.

Examples:

- Corporate identity service unavailable for most users
- Internet connectivity unavailable across a major office
- Production business application unavailable
- Confirmed ransomware or major security incident
- Company-wide email outage

**Target:** Immediate response; continuous communication; senior escalation.

### P2 – High

A significant issue affecting a department, critical employee group, or important business process.

Examples:

- Finance team unable to access ERP during month-end
- VPN unavailable for an entire remote team
- Several users unable to authenticate
- Critical executive presentation-room failure shortly before an external meeting

**Target:** Rapid response and frequent updates.

### P3 – Normal

A standard issue affecting one user or a small number of users without major business disruption.

Examples:

- Outlook search not returning results
- Printer not appearing
- One laptop running slowly
- Application installation failure

### P4 – Low / Request

Low-impact requests or general assistance.

Examples:

- Standard software request
- Keyboard replacement
- Documentation request
- Non-urgent configuration assistance

### Impact Assessment

Consider:

- Number of users affected
- Business criticality
- Revenue impact
- Regulatory impact
- Security impact
- Availability of workaround
- Duration
- Time sensitivity

Never lower priority simply because the user is senior. Priority is determined by business impact and urgency, while executive assistance may be handled through appropriate management channels.


## 4. Identity, Accounts, Passwords, and MFA

### 4.1 Password Reset

Before resetting a password, follow the approved identity-verification procedure. Never reset an account based solely on an email request from an unknown sender.

Standard process:

1. Verify the user's identity using an approved method.
2. Check whether the account is active.
3. Determine whether the account is locked or disabled.
4. Use the approved password-reset mechanism.
5. Require the user to establish a new password according to policy.
6. Confirm synchronization to required identity providers.
7. Test sign-in where appropriate.
8. Document the reset without recording the new password.

Never place passwords, recovery codes, or MFA backup codes in ticket notes.

### 4.2 Account Locked

Common causes:

- Repeated incorrect password attempts
- Old password stored in Outlook or mobile mail
- Mapped network drive using old credentials
- Scheduled task running under an old password
- Mobile device attempting authentication repeatedly
- Cached credentials
- Potential credential compromise

Troubleshooting:

1. Confirm the user cannot authenticate.
2. Check identity-system logs for lockout source if available.
3. Unlock the account using approved administrative tools.
4. Identify devices or services generating repeated failures.
5. Ask the user to update saved credentials.
6. If suspicious authentication originates from an unexpected location, escalate to Security Operations before repeatedly unlocking the account.

### 4.3 MFA Failure

Symptoms include:

- Push notification does not arrive
- Authenticator application displays an error
- One-time code is rejected
- User replaced their phone
- MFA registration was lost
- Number matching prompt does not appear

Initial checks:

- Verify device has network connectivity.
- Confirm device date and time are correct.
- Check whether the authentication service has a known outage.
- Confirm the user is using the correct registered account.
- Ask whether the phone was recently replaced or reset.
- Do not request the user to disclose MFA codes.

For a lost or replaced device, use the approved identity-verification and MFA re-registration process. High-risk resets may require identity-team approval.

### 4.4 Single Sign-On

When SSO fails:

1. Confirm whether the failure affects one application or all applications.
2. Test the identity portal.
3. Test another browser or private window.
4. Check browser time/date and cookie restrictions.
5. Capture the exact error message.
6. Record the timestamp.
7. Check known service health.
8. Escalate with correlation/request IDs if present.

Do not disable security controls simply to bypass an authentication problem.


## 5. Windows 11 Endpoint Troubleshooting

### 5.1 Computer Is Slow

First determine whether the issue is:

- Slow startup
- Slow application launch
- High CPU
- High memory usage
- High disk utilization
- Network latency
- Thermal throttling
- Storage capacity
- Background updates
- Malware/security scanning

Procedure:

1. Restart the computer if uptime is unusually long.
2. Open Task Manager.
3. Check CPU, memory, disk, and network utilization.
4. Identify applications with abnormal resource usage.
5. Check available storage.
6. Review startup applications.
7. Confirm Windows Update status.
8. Check whether endpoint-security scans are active.
9. Ask when the performance issue occurs.
10. Reproduce the issue if possible.

Do not terminate a process blindly if it is an operating-system, security, or business-critical process.

### 5.2 Windows Update Failure

Collect:

- Windows version
- Update number
- Exact error code
- Last successful update
- Available disk space
- Whether the device is managed
- Whether VPN/proxy is required

Standard steps:

1. Restart.
2. Confirm adequate storage.
3. Run the approved Windows Update troubleshooter.
4. Check update history.
5. Retry the update.
6. If managed, verify device management and policy status.
7. Capture the exact error code.
8. Escalate if repeated failures occur.

### 5.3 Blue Screen

Record the stop code and approximate time.

Collect:

- Stop code
- Recent hardware changes
- Recent driver updates
- Recent software installations
- Crash frequency
- Minidump availability
- Device model
- Windows build

If the device repeatedly crashes, protect user data first and avoid repeatedly forcing production work on unstable hardware.

### 5.4 No Audio

1. Check physical mute controls.
2. Verify Windows output device.
3. Test built-in speakers and headset separately.
4. Confirm application-specific audio settings.
5. Disconnect and reconnect USB/Bluetooth devices.
6. Restart the audio service only through approved procedures.
7. Check driver status.
8. Test with a known-good headset.

### 5.5 External Monitor Not Detected

1. Confirm monitor power.
2. Check cable seating.
3. Test another cable if available.
4. Check Windows display settings.
5. Use the appropriate display-detection function.
6. Test another port.
7. If using a dock, reconnect the dock.
8. Verify dock firmware/driver status according to endpoint standards.
9. Test the monitor with a known-good computer.

### 5.6 BitLocker Recovery

A BitLocker recovery prompt may occur after firmware, boot configuration, security, or hardware changes.

Do not ask the user to send a recovery key through normal chat or email. Follow the organization's secure recovery process. Verify the device and user identity, retrieve the key only through approved administrative systems, document the event, and investigate unexpected repeated recovery prompts.


## 6. macOS Endpoint Troubleshooting

### 6.1 Mac Running Slowly

Check:

- CPU utilization
- Memory pressure
- Available storage
- Login items
- Background synchronization
- OS update state
- Browser extensions
- Endpoint security status

Restart the Mac before making invasive changes. If a particular application causes the slowdown, test without that application and compare behavior.

### 6.2 Wi-Fi Problems on macOS

1. Confirm Wi-Fi is enabled.
2. Verify the correct SSID.
3. Forget and reconnect to the corporate network if permitted.
4. Check IP configuration.
5. Test gateway reachability.
6. Test DNS.
7. Compare with another device on the same network.
8. Escalate if multiple users are affected.

### 6.3 External Display

Check:

- Display power
- USB-C/Thunderbolt connection
- Adapter compatibility
- Display arrangement
- Resolution and refresh rate
- Dock functionality

Use approved adapters and docking stations. Unknown third-party drivers should not be installed on managed endpoints without approval.


## 7. Network Troubleshooting

### 7.1 Basic Network Diagnostic Sequence

Use the following order:

**Layer 1 – Physical**

- Cable connected?
- Wi-Fi enabled?
- Link light present?
- Dock connected?
- Switch port active?

**Layer 2 – Local Network**

- Correct SSID?
- Correct VLAN?
- MAC authentication successful?
- Device received a valid IP?

**Layer 3 – IP**

- Valid address?
- Correct subnet?
- Default gateway present?
- Gateway reachable?

**Layer 4 – DNS and Services**

- Can hostname resolve?
- Can known IP address be reached?
- Can required TCP service be reached?
- Is the remote application available?

Avoid assuming that "internet is down" means the internet itself is unavailable. The fault may be local DNS, DHCP, Wi-Fi authentication, VPN routing, proxy configuration, or an application service.

### 7.2 DHCP Problems

Symptoms:

- 169.254.x.x address
- No default gateway
- Duplicate address warning
- Intermittent connectivity

Checks:

1. Verify physical/Wi-Fi connection.
2. Disconnect/reconnect.
3. Renew DHCP lease using approved endpoint procedures.
4. Check whether other devices on the same network receive addresses.
5. If multiple devices fail, escalate to Network Operations.

### 7.3 DNS Problems

Symptoms:

- Websites fail by name but work by IP
- Internal applications cannot resolve
- "Server not found"
- Intermittent name resolution

Tests may include resolving a known internal hostname and a permitted public hostname. Record the resolver address and exact result.

If only internal names fail, investigate corporate DNS, VPN, split DNS, or routing. If public names fail while internal names work, investigate upstream DNS or resolver policy.

### 7.4 VPN Problems

Before troubleshooting:

- Confirm user has valid account access.
- Confirm MFA works.
- Confirm internet access without VPN.
- Check VPN client version.
- Record the exact error.

Common causes:

- Expired credentials
- MFA failure
- VPN profile corruption
- Client version mismatch
- Certificate issue
- Network blocking
- DNS/routing problem
- Concurrent session limit
- VPN gateway outage

Never request or store a user's VPN password.

### 7.5 VPN Connected but Internal Application Fails

Check:

1. VPN assigned IP.
2. Internal DNS resolution.
3. Route to the application subnet.
4. Application port reachability.
5. Whether the user is authorized for the application.
6. Whether the application itself is available.

A successful VPN connection does not prove that all internal routes and applications are working.


## 8. Microsoft 365 Support

### 8.1 Outlook Cannot Send Email

Check:

- Internet connectivity
- Outlook account status
- Outlook work offline mode
- Mailbox quota
- Recipient address
- Attachment size
- SMTP/service health
- Whether all recipients are affected
- Exact bounce-back message

If an email generates a non-delivery report, preserve the exact error text. Do not paraphrase an SMTP or Exchange error code when escalating.

### 8.2 Outlook Cannot Receive Email

1. Send a test message from a known account.
2. Check Outlook connection status.
3. Check webmail.
4. Check mailbox quota.
5. Check rules and focused/other folders.
6. Check junk/quarantine where appropriate.
7. Determine whether the issue is Outlook-client-specific or mailbox-wide.

If webmail receives mail but desktop Outlook does not, focus on the client profile, synchronization, cached mode, or local configuration.

### 8.3 Outlook Search Not Working

1. Test search in webmail.
2. Determine whether all folders or only one mailbox are affected.
3. Restart Outlook.
4. Check indexing status.
5. Verify local storage availability.
6. Rebuild the search index only through approved procedures.
7. Escalate if the problem persists across multiple devices.

### 8.4 Microsoft Teams Problems

Common symptoms:

- Cannot join meeting
- Microphone unavailable
- Camera unavailable
- Messages delayed
- Presence incorrect
- Screen sharing unavailable

Troubleshoot in this order:

1. Confirm service status if widespread.
2. Test Teams web client if allowed.
3. Verify microphone/camera permissions.
4. Check selected devices.
5. Restart Teams.
6. Restart the endpoint if necessary.
7. Test another meeting.
8. Determine whether the issue follows the user or the device.

### 8.5 OneDrive Synchronization

Symptoms:

- Red X
- Cloud icon stuck
- Files not updating
- Duplicate files
- Sync paused

Check:

- Account signed in
- Storage availability
- File path length
- Unsupported characters
- File size
- File locked by another process
- Sync client state
- Internet connection

Do not delete the local OneDrive folder to "fix sync" without confirming synchronization status and protecting unsynchronized files.


## 9. Printers and Scanners

### 9.1 Printer Not Printing

1. Confirm printer power.
2. Check physical/network connectivity.
3. Confirm correct printer selected.
4. Check print queue.
5. Clear only stuck jobs belonging to the affected user unless broader intervention is authorized.
6. Print a test page.
7. Test another application.
8. Compare with another user.
9. Check printer status and consumables.

### 9.2 Network Printer Offline

Determine whether:

- One user sees offline
- Several users see offline
- Printer responds on network
- Printer display reports an error

If multiple users cannot print, treat it as a potential shared-service incident rather than repeatedly reinstalling printer drivers on individual machines.

### 9.3 Scanner Not Detected

Check USB/network connection, scanner power, approved driver/software, device selection, permissions, and whether scanning works from the manufacturer's approved utility.

Never install unknown scanner software downloaded from unofficial websites.


## 10. Software Installation and Application Support

### 10.1 Approved Software

Software must come from:

- Corporate software portal
- Approved package repository
- Managed application deployment
- Official vendor source when specifically authorized

Users should not install cracked, pirated, repackaged, or unknown software.

### 10.2 Application Crashes

Collect:

- Application name/version
- OS version
- Exact error
- Crash frequency
- User account
- Device
- Recent updates
- Recent configuration changes
- Whether another user experiences the same issue

Troubleshooting:

1. Reproduce the crash.
2. Restart the application.
3. Restart the endpoint.
4. Check application updates.
5. Check disk space.
6. Test with another user/profile where appropriate.
7. Review application logs.
8. Escalate with logs and timestamps.

### 10.3 Browser Problems

For browser-specific issues:

- Test another approved browser.
- Test private/incognito mode.
- Disable extensions one at a time if policy permits.
- Clear site-specific data before clearing all browser data.
- Confirm system date/time.
- Check proxy settings.
- Check certificate warnings.

Never instruct users to ignore certificate warnings for corporate applications unless explicitly directed by the security/infrastructure team.


## 11. Cybersecurity and Suspicious Activity

### 11.1 Phishing Email

If a user suspects phishing:

1. Do not click additional links.
2. Do not open additional attachments.
3. Do not reply to the sender.
4. Report using the approved phishing-report mechanism.
5. Preserve the message where possible.
6. If credentials were entered, immediately follow the credential-compromise procedure.
7. If malware may have executed, disconnect the endpoint from networks only according to incident-response guidance and contact Security Operations.

### 11.2 User Entered Password into a Suspicious Website

Treat this as a potential credential compromise.

Immediate actions:

- Tell the user not to interact further with the suspicious site.
- Initiate approved password reset.
- Revoke active sessions/tokens when required.
- Review recent sign-in activity.
- Verify MFA registration has not been changed.
- Escalate to Security Operations.
- Determine whether other corporate accounts used the same password.

Do not blame or shame the user. Fast reporting reduces damage.

### 11.3 Malware Suspected

Indicators may include:

- Unexpected security alerts
- Unknown processes
- Browser redirects
- Sudden encryption of files
- Disabled security tools
- Unusual outbound connections
- Fake antivirus warnings
- Numerous files renamed unexpectedly

Do not casually delete suspicious files or run random cleanup tools. Preserve evidence and follow the incident-response playbook.

### 11.4 Lost Laptop

Collect:

- Asset tag
- Device serial number
- Last known location
- Last known time
- User
- Whether device encryption is enabled
- Whether sensitive data may be stored locally

Immediately notify the appropriate security and asset-management teams. Remote lock/wipe actions must follow the organization's approved device-management procedure.

### 11.5 Suspected Ransomware

Potential ransomware should be treated as a security incident.

Actions:

1. Stop normal user activity on the affected device.
2. Follow security team's containment instructions.
3. Do not reconnect disconnected systems without authorization.
4. Do not delete encrypted files.
5. Do not negotiate or make payment decisions through the service desk.
6. Preserve relevant evidence.
7. Record timeline and affected systems.
8. Escalate immediately.



## 12. Hardware Support

### 12.1 Laptop Does Not Power On

Check:

- Charger connected
- Power outlet
- Dock power
- Charging indicator
- Physical damage
- Battery condition
- External monitor behavior
- Whether keyboard lights respond

Disconnect unnecessary peripherals and test with the approved power adapter. If there is burning smell, liquid exposure, swelling battery, smoke, or unusual heat, stop using the device and follow hardware safety procedures.

### 12.2 Overheating

Symptoms:

- Fan constantly running
- Device becomes unusually hot
- Performance drops
- Unexpected shutdowns

Check workload, vents, environment, fan noise, and hardware diagnostics. Do not open a managed device unless authorized.

### 12.3 Battery Health

For degraded batteries, collect:

- Device model
- Battery health report
- Cycle count if available
- Approximate runtime
- Swelling or physical damage

A swollen battery is a safety issue and should not be treated as an ordinary replacement request.

### 12.4 Keyboard and Mouse

Try:

- Reconnect
- Replace batteries for wireless devices
- Test USB port
- Test known-good keyboard/mouse
- Check Bluetooth pairing
- Test another user/device

If the issue follows the peripheral, replace the peripheral. If it follows the endpoint, investigate the endpoint.

### 12.5 Webcam

Check:

- Privacy shutter
- Physical camera switch
- OS privacy permissions
- Application permissions
- Correct camera selected
- Another application using camera
- Driver/device state



## 13. Employee Onboarding

### Standard Onboarding Checklist

Before the employee's first day:

- HR record received
- Manager identified
- Department and cost center recorded
- Account created
- Appropriate group membership assigned
- Email provisioned
- MFA enrollment prepared
- Laptop assigned
- Asset tag recorded
- Standard applications installed
- VPN access assigned where required
- Collaboration groups assigned
- Security training requirements communicated

On the first day:

1. Verify employee identity.
2. Provide device.
3. Assist with initial sign-in.
4. Complete MFA registration.
5. Confirm email.
6. Confirm Teams/collaboration access.
7. Confirm required business applications.
8. Confirm network/VPN access.
9. Explain support channels.
10. Confirm asset acceptance.

Access should follow least privilege. Do not provide administrative rights merely because an application installation is inconvenient.

## 14. Employee Transfer

When an employee changes department or role:

- Review current access.
- Remove obsolete group memberships.
- Add required new access.
- Update application roles.
- Update device requirements.
- Confirm manager approval.
- Record effective date.
- Ensure access changes follow approved authorization.

Role changes are an access-management event and should not be treated as simple account updates.

## 15. Employee Offboarding

Offboarding requires coordination between HR, IT, Security, Facilities, and the employee's manager.

Typical actions:

- Disable account at approved time.
- Revoke sessions and authentication tokens.
- Remove VPN access.
- Disable application access.
- Recover company laptop and accessories.
- Record asset condition.
- Preserve business data according to policy.
- Handle mailbox according to retention and legal requirements.
- Transfer approved files and ownership.
- Disable building access through Facilities.
- Document completion.

Do not delete accounts or data prematurely when retention, legal hold, investigation, or business-continuity requirements apply.


## 16. Asset Management

Every managed device should have:

- Asset ID
- Serial number
- Assigned user
- Department
- Location
- Purchase date
- Warranty status
- Device model
- Operating system
- Encryption state
- Management state
- Lifecycle status

### Asset Lifecycle

**Ordered → Received → Tagged → Imaged/Enrolled → Assigned → In Service → Repair/Replacement → Returned → Sanitized → Retired**

When a laptop is returned:

1. Verify asset tag and serial number.
2. Inspect physical condition.
3. Record accessories.
4. Check for damage.
5. Secure the device.
6. Process data according to approved retention procedures.
7. Remove the device from user assignment.
8. Update lifecycle status.

Never dispose of storage media without approved data sanitization or destruction.


## 17. Remote Support

Remote support should use approved enterprise tools only.

Before connecting:

- Obtain user consent where required.
- Verify identity.
- Explain what you will do.
- Avoid viewing unrelated personal information.
- Never request passwords through the remote session.
- Do not silently install unauthorized tools.

During support:

- Narrate important actions.
- Avoid accessing personal files unless required for troubleshooting.
- Stop if sensitive information is unexpectedly displayed.
- Document actions taken.

After support:

- Close the remote session.
- Confirm the user can operate normally.
- Remove temporary tools if policy requires.
- Document the result.

Never ask a user to install an unknown remote-access application received from an unsolicited caller or email.


## 18. Backup and Data Recovery

### 18.1 Accidental File Deletion

Determine:

- Where the file was stored
- Approximate deletion time
- Whether synchronization was enabled
- Whether the file was shared
- Whether recycle/trash recovery is available
- Whether backup exists

Do not overwrite the affected storage unnecessarily.

### 18.2 OneDrive/SharePoint Recovery

Check recycle-bin or version-history mechanisms according to organizational policy. Confirm the correct file, owner, path, and timestamp before restoring.

### 18.3 Local Device Data

If data exists only locally, escalate to the approved endpoint recovery process. Do not promise that deleted data can be recovered.

### 18.4 Backup Principle

A backup is useful only if it can be restored. Backup systems should be periodically tested through approved recovery exercises.


## 19. Change Management

Changes affecting production or shared services should follow approved change-management procedures.

A normal change record should include:

- Business reason
- Scope
- Systems affected
- Risk
- Implementation plan
- Validation plan
- Rollback plan
- Maintenance window
- Stakeholders
- Owner
- Approval
- Communication plan

Examples:

- Firewall rule change
- DNS modification
- Server patching
- Identity-policy change
- Network switch replacement
- Microsoft 365 configuration change
- Endpoint security-policy modification

Emergency changes may use an expedited process but must still be documented and reviewed afterward.

Never make production changes solely because a user says, "It is urgent."


## 20. Incident Management

### Major Incident Communication

A major incident update should state:

- Current impact
- Affected services
- Start time
- Current investigation
- Known workaround
- Next update time
- Owner/team

Avoid speculation.

**Poor update:**

> The database is probably broken and the vendor is fixing it.

**Better update:**

> The finance reporting service is currently unavailable for approximately 180 users. Infrastructure and application teams are investigating authentication and database connectivity. No data loss has been identified at this time. The next status update will be provided at 14:30 IST.

### Incident Closure

Before closure:

- Service restored
- User/business owner informed
- Monitoring confirms stability
- Resolution documented
- Related problem identified if recurring
- Required communications completed

### Problem Management

A recurring incident should trigger problem investigation when appropriate.

Examples:

- Same VPN failure occurs every Monday
- A specific laptop model repeatedly loses Wi-Fi
- Monthly application crashes after patching
- Printer queue repeatedly corrupts

Problem management seeks root cause and permanent prevention rather than repeatedly fixing symptoms.


## 21. Troubleshooting Methodology

A strong support analyst follows a controlled process.

### Step 1 – Define the Symptom

Do not start with a presumed cause.

User says:

> "Teams is broken."

Clarify:

> "What happens when you open Teams? Does it launch? Can you sign in? Can you send messages? Can you join meetings? Is the issue occurring on both desktop and web?"

### Step 2 – Establish Scope

Determine:

- One user or many?
- One device or many?
- One location or multiple?
- One application or multiple?
- Internal network or external network?
- Started after a change?

### Step 3 – Establish Timeline

Ask:

- When was it last working?
- When did it first fail?
- What changed immediately before failure?

### Step 4 – Test the Simplest Hypothesis

Check power, connectivity, sign-in state, storage, obvious error messages, and service status before complex interventions.

### Step 5 – Change One Variable at a Time

If five changes are made simultaneously, it becomes difficult to identify which change solved or caused the problem.

### Step 6 – Validate

A fix is not complete until the relevant function works.

### Step 7 – Document

Record symptoms, evidence, actions, results, and final resolution.


## 22. Common Error Reference

### Error: "Access Denied"

Possible causes:

- Missing authorization
- Expired session
- Incorrect account
- Conditional-access policy
- Resource permissions
- Application role missing

Do not automatically grant elevated permissions.

### Error: "The network path was not found"

Possible causes:

- Network unavailable
- DNS failure
- VPN disconnected
- Server unavailable
- SMB/service restriction
- Incorrect path

### Error: "Credential prompt keeps appearing"

Possible causes:

- Cached old password
- Wrong account
- Stored credential
- Service using old credentials
- Conditional-access issue
- Application session problem

### Error: "No Internet"

Possible causes:

- Wi-Fi disconnected
- DHCP failure
- DNS failure
- Gateway issue
- Proxy issue
- VPN routing
- ISP outage
- Endpoint firewall/policy

### Error: "Certificate warning"

Do not simply bypass it. Check hostname, certificate validity, device time, trust chain, proxy interception, and whether the service is expected.


## 23. Knowledge Base Article Format

Every new IT knowledge article should use this structure:

### Title

Use a searchable title such as:

> Outlook cannot send email from Windows 11

### Symptoms

Describe what the user sees.

### Environment

Specify operating system, application, or service.

### Cause

List confirmed causes separately from possible causes.

### Resolution

Provide numbered steps.

### Validation

Explain how to verify the fix.

### Escalation

State when the service desk should escalate.

### Related Articles

Link to related internal articles where available.

### Revision History

Record significant changes.

Avoid publishing undocumented workarounds as official procedures.


## 24. Frequently Asked Questions

### How do I reset my corporate password?

Use the approved self-service password-reset portal. If self-service recovery fails, contact the service desk and complete identity verification.

### Why does my VPN connect but internal websites do not open?

The VPN tunnel may be established while internal DNS or routes are unavailable. Check internal name resolution and connectivity and contact IT if the issue persists.

### Why is Outlook asking for my password repeatedly?

Possible causes include expired credentials, stale cached credentials, account synchronization issues, conditional-access requirements, or an Outlook profile problem.

### Can IT see my password?

IT support personnel must never request or record your password. Authentication credentials should be entered only into approved authentication interfaces.

### What should I do if I receive a suspicious email?

Do not click links or open attachments. Use the approved phishing-reporting method and contact Security Operations if you entered credentials or opened a suspicious file.

### Why is my laptop slow?

High CPU/memory usage, insufficient storage, updates, security scanning, applications, browser tabs, thermal throttling, and hardware problems can all contribute. Restart and contact IT if the issue continues.

### Can I install any software I want?

Only approved software should be installed on company-managed devices. Use the corporate software catalog or request approval.

### Why does my printer say offline?

The printer may be powered off, disconnected, unavailable on the network, or incorrectly mapped. If multiple users are affected, report it as a shared printer/service issue.

### How long does IT support take?

Resolution time depends on priority, business impact, complexity, dependencies, and whether another team or vendor is required.

### What information should I provide when opening a ticket?

Provide the service, exact error, time the issue started, affected device, screenshots when safe, recent changes, and whether other users are affected.


## 25. Detailed Runbooks

### Runbook: User Cannot Log In to Windows

**Symptoms:** User enters credentials and receives a sign-in failure.

**Checks:**
1. Confirm username format.
2. Confirm keyboard layout and Caps Lock.
3. Determine whether the account works on another approved service.
4. Check whether the device has network connectivity.
5. Determine whether cached login is expected.
6. Check account lockout status through approved tools.
7. Check whether password recently changed.
8. If password changed, confirm device can contact identity infrastructure.
9. If device is offline and cached credentials should work, test approved offline sign-in behavior.
10. Escalate if account appears disabled or compromised.

**Resolution examples:**
- Unlock account.
- Reset password.
- Reconnect device to corporate network.
- Repair identity synchronization.
- Escalate suspicious authentication.

### Runbook: User Cannot Access Internal Website

1. Confirm exact URL.
2. Test public website.
3. Test internal site from another device.
4. Check VPN status.
5. Resolve hostname.
6. Test connectivity to expected service.
7. Check browser behavior.
8. Determine whether only the user's account is affected.
9. Escalate to network/application team with timestamp and error.

### Runbook: Teams Meeting Audio Failure

1. Verify user is not muted.
2. Check selected microphone.
3. Check Windows/macOS permissions.
4. Test microphone in system settings.
5. Test another headset.
6. Test Teams web client.
7. Determine whether the issue is device-specific.
8. Check service health if multiple participants report failures.

### Runbook: New Laptop Setup

1. Confirm asset record.
2. Apply standard image or enrollment procedure.
3. Install management agent.
4. Confirm encryption.
5. Apply security policies.
6. Install approved applications.
7. Run updates.
8. Verify endpoint protection.
9. Confirm identity registration.
10. Test Wi-Fi.
11. Test VPN.
12. Test email and collaboration.
13. Record assigned user.
14. Obtain asset acknowledgment.

### Runbook: Employee Reports Lost Phone

1. Verify employee identity.
2. Determine whether the device contains corporate authentication or management profiles.
3. Notify security/identity team when required.
4. Revoke or suspend corporate access according to policy.
5. Remove/re-register MFA using secure identity verification.
6. Report device to mobile/asset management.
7. Document the timeline.


## 26. Realistic Support Ticket Examples

### Ticket INC-2026-10482 – VPN Authentication Failure

**Requester:** Priya N., Finance  
**Priority:** P2  
**Opened:** 07-Oct-2026 08:41 IST  
**Summary:** Finance users unable to connect to corporate VPN.

**Initial symptoms:** Four finance employees reported that the VPN client accepted usernames but returned an MFA-related failure.

**Investigation:** Internet connectivity was confirmed. MFA worked against the identity portal. Endpoint troubleshooting showed the VPN client was communicating with the gateway, but authentication requests were rejected after approximately 30 seconds.

**Scope:** Four users in the same department. Other departments were connecting normally.

**Action:** Identity Operations compared authentication logs and found a policy assignment applied to the Finance VPN group at 08:17 IST.

**Resolution:** Policy assignment was corrected through approved change procedure. All four users successfully connected.

**Closure:** 09:26 IST. Problem record recommended because the policy change caused unexpected access impact.

---

### Ticket INC-2026-10511 – Outlook Search Empty

**Requester:** Arun K., Engineering  
**Priority:** P3  
**Summary:** Outlook search returns no recent messages.

**Investigation:** Webmail search returned expected messages. Desktop Outlook did not. Local indexing status indicated an incomplete index.

**Action:** Restarted Outlook, checked storage, verified indexing service, and rebuilt the approved local index.

**Validation:** Search returned recent and historical mail.

**Resolution:** Local search index rebuilt successfully.

---

### Ticket INC-2026-10539 – Office Wi-Fi Intermittent

**Requester:** Multiple users, Chennai office  
**Priority:** P2  
**Symptoms:** Users in the second-floor conference area repeatedly disconnected from corporate Wi-Fi.

**Investigation:** Wired users were unaffected. Access-point logs showed repeated client reassociation events. Signal quality was poor in a specific area.

**Resolution:** Network team adjusted access-point configuration and replaced a failing access point during the maintenance window.

**Validation:** 12 test devices maintained connectivity for 45 minutes.

---

### Ticket INC-2026-10601 – Suspicious Attachment

**Requester:** Sales employee  
**Priority:** P1 Security  
**Summary:** User opened a spreadsheet received from an unknown external sender.

**Actions:** User stopped interacting with the file and contacted IT immediately. Security Operations isolated the endpoint using approved tooling, reviewed endpoint telemetry, and checked authentication activity.

**Result:** No confirmed malicious execution was identified. The attachment was submitted for analysis and the sender was blocked according to security procedure.

**Lesson:** Rapid reporting reduced investigation time and allowed the endpoint to be isolated before further activity occurred.

---

### Ticket SR-2026-22417 – New Employee Setup

**Requester:** HR  
**Priority:** P3  
**Employee:** Fictional employee record  
**Department:** Product Engineering  
**Start Date:** 12-Oct-2026

**Tasks:** Laptop assignment, identity account, MFA, standard engineering software, Teams, email, VPN, and asset acknowledgment.

**Completion:** Device delivered and all required access validated before start date.

---

### Ticket INC-2026-10672 – Printer Unavailable

**Requester:** Accounts Payable  
**Priority:** P3  
**Symptoms:** Four users unable to print invoices.

**Investigation:** Printer displayed "Ready", but the print server queue was not processing jobs. Direct printer network connectivity was available.

**Resolution:** Print service team restarted the affected queue service after verifying no other critical queues would be impacted. Pending jobs were reprocessed.

**Validation:** Three test invoices printed successfully.

---

### Ticket INC-2026-10708 – Laptop Will Not Boot

**Requester:** Marketing  
**Priority:** P2  
**Symptoms:** Laptop displays manufacturer logo and restarts continuously.

**Investigation:** Issue began immediately after a firmware update. Hardware diagnostics passed. Recovery environment was accessible.

**Action:** Endpoint Engineering followed approved firmware recovery procedure.

**Resolution:** Firmware recovery completed and Windows booted successfully.

**Follow-up:** Firmware deployment was reviewed for other devices of the same model.


## 27. Escalation Matrix

| Issue | Primary Team | Escalate When |
|---|---|---|
| Password reset | Service Desk | Identity verification fails or compromise suspected |
| MFA failure | Identity Operations | Registration issue, policy failure, or suspicious activity |
| VPN single user | Service Desk | Standard troubleshooting fails |
| VPN many users | Network/Identity | Multiple users affected |
| Wi-Fi one user | Service Desk | Endpoint troubleshooting fails |
| Wi-Fi many users | Network Operations | Shared infrastructure suspected |
| Outlook single user | Service Desk | Client troubleshooting fails |
| Microsoft 365 widespread | M365/Cloud Operations | Multiple services/users affected |
| Malware | Security Operations | Any confirmed or suspected malicious execution |
| Lost laptop | Security + Asset Management | Device contains corporate data |
| Printer single user | Service Desk | Mapping/driver problem persists |
| Printer many users | Infrastructure | Shared printer/server failure |
| Business application | Application Support | Application/service defect suspected |
| Hardware failure | Endpoint/Hardware | Device diagnostics indicate physical failure |
| Data recovery | Backup/Infrastructure | User cannot recover through approved self-service |
| Production outage | Major Incident Team | Critical service unavailable |

Escalation should include evidence, not just a statement that "IT cannot fix it."


## 28. Security Principles for IT Support

1. Never ask users to provide passwords.
2. Never store credentials in tickets.
3. Verify identity before sensitive account actions.
4. Follow least privilege.
5. Use approved administrative tools.
6. Do not disable endpoint protection to make troubleshooting easier unless Security explicitly authorizes it.
7. Do not install unauthorized remote-access software.
8. Treat unexpected MFA prompts as potentially suspicious.
9. Report suspected compromise immediately.
10. Preserve evidence during security incidents.
11. Do not expose confidential information in screenshots.
12. Use secure channels for sensitive information.
13. Follow retention and privacy policies.
14. Never bypass access controls because a request appears urgent.
15. Document security-relevant actions.

### Unexpected MFA Prompt

If a user receives an MFA request they did not initiate:

- Do not approve it.
- Deny or reject it if the interface provides that option.
- Report the event.
- Change the password if directed by Security.
- Review sign-in activity when authorized.
- Escalate repeated prompts.

Repeated unexpected MFA prompts can indicate that an attacker knows the password and is attempting to complete authentication.


## 29. Business Continuity and Disaster Recovery

IT support may participate in continuity events such as:

- Office power outage
- Internet-provider outage
- Cloud service disruption
- Data-center incident
- Cybersecurity incident
- Severe weather
- Hardware failure
- Identity-service outage

During a major outage:

1. Protect people and safety first.
2. Establish incident command.
3. Determine affected services.
4. Identify critical business functions.
5. Activate approved continuity procedures.
6. Communicate regularly.
7. Avoid unapproved emergency changes.
8. Track decisions and timestamps.
9. Validate recovery.
10. Conduct a post-incident review.

### Recovery Priority

Critical identity, communication, network, and business systems should be restored according to the organization's approved business-impact analysis and recovery objectives.

Do not invent recovery time or recovery point objectives during an incident. Refer to the approved service continuity documentation.


## 30. Service Desk Communication Templates

### Initial Response

> Hello,  
> We have received your IT support request and are reviewing the reported issue. We have recorded the affected service, device, and symptoms. We will update the ticket after the initial investigation.

### Request for Information

> To continue troubleshooting, please provide the exact error message, the approximate time the issue started, and whether the issue occurs on another device or application. Please do not send passwords, MFA codes, or other authentication secrets.

### Resolution Confirmation

> The reported issue has been resolved. We validated the affected service using the troubleshooting steps documented in the ticket. Please contact the service desk if the same problem returns.

### Major Incident Update

> **Service Update:** The reported service interruption is affecting multiple users. The infrastructure and application teams are investigating. Current testing indicates that authentication and network connectivity are being reviewed. The next update will be provided at the scheduled communication interval.

### Security Incident Guidance

> Please do not interact further with the suspicious message or attachment. Do not provide credentials or MFA codes. The security team has been notified and will provide additional instructions.


## 31. Diagnostic Command Reference

The following commands are examples for authorized troubleshooting. Commands must be used according to organizational policy and operating-system permissions.

### Windows

`ipconfig /all` – Display IP configuration.

`ipconfig /flushdns` – Clear local DNS resolver cache.

`ipconfig /renew` – Request DHCP configuration again.

`nslookup hostname` – Test DNS resolution.

`ping hostname` – Test basic ICMP reachability when permitted.

`tracert hostname` – Review network path.

`whoami` – Display the current Windows identity.

`hostname` – Display the computer hostname.

`systeminfo` – Display system information.

`tasklist` – List running processes.

`netstat` – Review network connections according to approved troubleshooting procedures.

### macOS

`ifconfig` – Display network interfaces.

`scutil --dns` – Review DNS configuration.

`ping hostname` – Test reachability where permitted.

`traceroute hostname` – Review network path.

`whoami` – Display current account.

`sw_vers` – Display macOS version.

Commands that modify system configuration should be used only when appropriate and authorized.


## 32. Root Cause Analysis Example

### Incident

Corporate VPN became unavailable to approximately 75 remote employees.

### Immediate Cause

VPN authentication requests were rejected.

### Investigation

- Internet service was healthy.
- VPN gateways were reachable.
- MFA service was healthy.
- Endpoint clients were healthy.
- Authentication logs showed policy evaluation failures.
- A configuration change had been made earlier that morning.

### Root Cause

A newly applied access policy contained an incorrect group condition.

### Contributing Factors

- Change validation did not include a representative Finance and Engineering user.
- Monitoring detected gateway health but not successful end-user authentication.
- Rollback documentation was incomplete.

### Corrective Actions

- Correct policy condition.
- Add representative authentication tests to change validation.
- Improve monitoring.
- Update rollback documentation.
- Conduct post-change review.

### Lesson

Infrastructure health does not always equal user-service health. Monitoring should test the actual user journey where practical.


## 33. IT Support Quality Checklist

Before closing a ticket, ask:

- Did I identify the actual symptom?
- Did I determine scope?
- Did I check for a known incident?
- Did I protect user/security information?
- Did I document evidence?
- Did I avoid unauthorized changes?
- Did I validate the solution?
- Did I explain the resolution?
- Did I identify a recurring problem?
- Did I escalate with sufficient evidence?
- Did I record the correct category and resolution code?

A high-quality ticket should allow another support analyst to understand what happened without asking the original analyst to explain it verbally.


## 34.1 Knowledge Article: Wi-Fi connected but no internet

**Category:** Network  
**Article ID:** KB-NETWORK-001

### Symptoms

The user reports: **Wi-Fi connected but no internet**.

### Initial Questions

1. When did the issue begin?
2. Was it working previously?
3. What changed immediately before the issue?
4. Is another user affected?
5. Is another device affected?
6. What exact error appears?
7. Is there a workaround?

### Standard Troubleshooting

Check IP address, gateway, DNS, and whether other users are affected. Compare access to internal and external services.

### Evidence to Collect

Record the device name, user, timestamp, exact error message, affected service, network/location context, and relevant screenshots when safe.

### Validation

Repeat the failed operation after the corrective action. Confirm the expected business function rather than assuming that a technical component being online means the issue is resolved.

### Escalation

Escalate when standard troubleshooting is unsuccessful, multiple users are affected, security concerns exist, infrastructure changes are required, or the issue exceeds service-desk authority.



## 34.2 Knowledge Article: VPN disconnects every few minutes

**Category:** VPN  
**Article ID:** KB-VPN-002

### Symptoms

The user reports: **VPN disconnects every few minutes**.

### Initial Questions

1. When did the issue begin?
2. Was it working previously?
3. What changed immediately before the issue?
4. Is another user affected?
5. Is another device affected?
6. What exact error appears?
7. Is there a workaround?

### Standard Troubleshooting

Check client version, network stability, sleep/power settings, gateway status, and authentication logs. Compare another network.

### Evidence to Collect

Record the device name, user, timestamp, exact error message, affected service, network/location context, and relevant screenshots when safe.

### Validation

Repeat the failed operation after the corrective action. Confirm the expected business function rather than assuming that a technical component being online means the issue is resolved.

### Escalation

Escalate when standard troubleshooting is unsuccessful, multiple users are affected, security concerns exist, infrastructure changes are required, or the issue exceeds service-desk authority.



## 34.3 Knowledge Article: Outlook profile repeatedly asks for password

**Category:** Microsoft 365  
**Article ID:** KB-MICROSOFT-36-003

### Symptoms

The user reports: **Outlook profile repeatedly asks for password**.

### Initial Questions

1. When did the issue begin?
2. Was it working previously?
3. What changed immediately before the issue?
4. Is another user affected?
5. Is another device affected?
6. What exact error appears?
7. Is there a workaround?

### Standard Troubleshooting

Check account state, recent password change, cached credentials, conditional access, and whether webmail works.

### Evidence to Collect

Record the device name, user, timestamp, exact error message, affected service, network/location context, and relevant screenshots when safe.

### Validation

Repeat the failed operation after the corrective action. Confirm the expected business function rather than assuming that a technical component being online means the issue is resolved.

### Escalation

Escalate when standard troubleshooting is unsuccessful, multiple users are affected, security concerns exist, infrastructure changes are required, or the issue exceeds service-desk authority.



## 34.4 Knowledge Article: Teams microphone not detected

**Category:** Collaboration  
**Article ID:** KB-COLLABORATIO-004

### Symptoms

The user reports: **Teams microphone not detected**.

### Initial Questions

1. When did the issue begin?
2. Was it working previously?
3. What changed immediately before the issue?
4. Is another user affected?
5. Is another device affected?
6. What exact error appears?
7. Is there a workaround?

### Standard Troubleshooting

Check OS permissions, selected microphone, hardware connection, application selection, and another conferencing application.

### Evidence to Collect

Record the device name, user, timestamp, exact error message, affected service, network/location context, and relevant screenshots when safe.

### Validation

Repeat the failed operation after the corrective action. Confirm the expected business function rather than assuming that a technical component being online means the issue is resolved.

### Escalation

Escalate when standard troubleshooting is unsuccessful, multiple users are affected, security concerns exist, infrastructure changes are required, or the issue exceeds service-desk authority.



## 34.5 Knowledge Article: Laptop fan constantly running

**Category:** Endpoint  
**Article ID:** KB-ENDPOINT-005

### Symptoms

The user reports: **Laptop fan constantly running**.

### Initial Questions

1. When did the issue begin?
2. Was it working previously?
3. What changed immediately before the issue?
4. Is another user affected?
5. Is another device affected?
6. What exact error appears?
7. Is there a workaround?

### Standard Troubleshooting

Check CPU usage, background processes, updates, endpoint security scanning, thermal state, and available storage.

### Evidence to Collect

Record the device name, user, timestamp, exact error message, affected service, network/location context, and relevant screenshots when safe.

### Validation

Repeat the failed operation after the corrective action. Confirm the expected business function rather than assuming that a technical component being online means the issue is resolved.

### Escalation

Escalate when standard troubleshooting is unsuccessful, multiple users are affected, security concerns exist, infrastructure changes are required, or the issue exceeds service-desk authority.



## 34.6 Knowledge Article: Printer queue stuck

**Category:** Printing  
**Article ID:** KB-PRINTING-006

### Symptoms

The user reports: **Printer queue stuck**.

### Initial Questions

1. When did the issue begin?
2. Was it working previously?
3. What changed immediately before the issue?
4. Is another user affected?
5. Is another device affected?
6. What exact error appears?
7. Is there a workaround?

### Standard Troubleshooting

Determine whether one or many users are affected, inspect queue status, and escalate shared-service issues.

### Evidence to Collect

Record the device name, user, timestamp, exact error message, affected service, network/location context, and relevant screenshots when safe.

### Validation

Repeat the failed operation after the corrective action. Confirm the expected business function rather than assuming that a technical component being online means the issue is resolved.

### Escalation

Escalate when standard troubleshooting is unsuccessful, multiple users are affected, security concerns exist, infrastructure changes are required, or the issue exceeds service-desk authority.



## 34.7 Knowledge Article: OneDrive files stuck syncing

**Category:** Cloud Storage  
**Article ID:** KB-CLOUD-STORAG-007

### Symptoms

The user reports: **OneDrive files stuck syncing**.

### Initial Questions

1. When did the issue begin?
2. Was it working previously?
3. What changed immediately before the issue?
4. Is another user affected?
5. Is another device affected?
6. What exact error appears?
7. Is there a workaround?

### Standard Troubleshooting

Check account status, storage, path restrictions, sync state, and service health.

### Evidence to Collect

Record the device name, user, timestamp, exact error message, affected service, network/location context, and relevant screenshots when safe.

### Validation

Repeat the failed operation after the corrective action. Confirm the expected business function rather than assuming that a technical component being online means the issue is resolved.

### Escalation

Escalate when standard troubleshooting is unsuccessful, multiple users are affected, security concerns exist, infrastructure changes are required, or the issue exceeds service-desk authority.



## 34.8 Knowledge Article: Browser certificate warning

**Category:** Browser/Security  
**Article ID:** KB-BROWSER/SECU-008

### Symptoms

The user reports: **Browser certificate warning**.

### Initial Questions

1. When did the issue begin?
2. Was it working previously?
3. What changed immediately before the issue?
4. Is another user affected?
5. Is another device affected?
6. What exact error appears?
7. Is there a workaround?

### Standard Troubleshooting

Verify hostname, date/time, certificate validity, trust chain, and proxy behavior. Never blindly bypass the warning.

### Evidence to Collect

Record the device name, user, timestamp, exact error message, affected service, network/location context, and relevant screenshots when safe.

### Validation

Repeat the failed operation after the corrective action. Confirm the expected business function rather than assuming that a technical component being online means the issue is resolved.

### Escalation

Escalate when standard troubleshooting is unsuccessful, multiple users are affected, security concerns exist, infrastructure changes are required, or the issue exceeds service-desk authority.



## 34.9 Knowledge Article: Employee cannot access shared drive

**Category:** File Services  
**Article ID:** KB-FILE-SERVICE-009

### Symptoms

The user reports: **Employee cannot access shared drive**.

### Initial Questions

1. When did the issue begin?
2. Was it working previously?
3. What changed immediately before the issue?
4. Is another user affected?
5. Is another device affected?
6. What exact error appears?
7. Is there a workaround?

### Standard Troubleshooting

Check VPN/network, DNS, path, authorization, group membership, and server availability.

### Evidence to Collect

Record the device name, user, timestamp, exact error message, affected service, network/location context, and relevant screenshots when safe.

### Validation

Repeat the failed operation after the corrective action. Confirm the expected business function rather than assuming that a technical component being online means the issue is resolved.

### Escalation

Escalate when standard troubleshooting is unsuccessful, multiple users are affected, security concerns exist, infrastructure changes are required, or the issue exceeds service-desk authority.



## 34.10 Knowledge Article: New employee missing application

**Category:** Access Management  
**Article ID:** KB-ACCESS-MANAG-010

### Symptoms

The user reports: **New employee missing application**.

### Initial Questions

1. When did the issue begin?
2. Was it working previously?
3. What changed immediately before the issue?
4. Is another user affected?
5. Is another device affected?
6. What exact error appears?
7. Is there a workaround?

### Standard Troubleshooting

Verify approved role, application entitlement, licensing, deployment status, and manager authorization.

### Evidence to Collect

Record the device name, user, timestamp, exact error message, affected service, network/location context, and relevant screenshots when safe.

### Validation

Repeat the failed operation after the corrective action. Confirm the expected business function rather than assuming that a technical component being online means the issue is resolved.

### Escalation

Escalate when standard troubleshooting is unsuccessful, multiple users are affected, security concerns exist, infrastructure changes are required, or the issue exceeds service-desk authority.



## 34.11 Knowledge Article: Laptop battery drains rapidly

**Category:** Hardware  
**Article ID:** KB-HARDWARE-011

### Symptoms

The user reports: **Laptop battery drains rapidly**.

### Initial Questions

1. When did the issue begin?
2. Was it working previously?
3. What changed immediately before the issue?
4. Is another user affected?
5. Is another device affected?
6. What exact error appears?
7. Is there a workaround?

### Standard Troubleshooting

Check battery health, power profile, background applications, firmware, and physical battery condition.

### Evidence to Collect

Record the device name, user, timestamp, exact error message, affected service, network/location context, and relevant screenshots when safe.

### Validation

Repeat the failed operation after the corrective action. Confirm the expected business function rather than assuming that a technical component being online means the issue is resolved.

### Escalation

Escalate when standard troubleshooting is unsuccessful, multiple users are affected, security concerns exist, infrastructure changes are required, or the issue exceeds service-desk authority.



## 34.12 Knowledge Article: External monitor flickers

**Category:** Hardware  
**Article ID:** KB-HARDWARE-012

### Symptoms

The user reports: **External monitor flickers**.

### Initial Questions

1. When did the issue begin?
2. Was it working previously?
3. What changed immediately before the issue?
4. Is another user affected?
5. Is another device affected?
6. What exact error appears?
7. Is there a workaround?

### Standard Troubleshooting

Test cable, port, dock, monitor, refresh rate, and another device.

### Evidence to Collect

Record the device name, user, timestamp, exact error message, affected service, network/location context, and relevant screenshots when safe.

### Validation

Repeat the failed operation after the corrective action. Confirm the expected business function rather than assuming that a technical component being online means the issue is resolved.

### Escalation

Escalate when standard troubleshooting is unsuccessful, multiple users are affected, security concerns exist, infrastructure changes are required, or the issue exceeds service-desk authority.



## 34.13 Knowledge Article: Windows update fails

**Category:** Endpoint  
**Article ID:** KB-ENDPOINT-013

### Symptoms

The user reports: **Windows update fails**.

### Initial Questions

1. When did the issue begin?
2. Was it working previously?
3. What changed immediately before the issue?
4. Is another user affected?
5. Is another device affected?
6. What exact error appears?
7. Is there a workaround?

### Standard Troubleshooting

Collect exact update error, check storage, restart, review update history, and verify management policy.

### Evidence to Collect

Record the device name, user, timestamp, exact error message, affected service, network/location context, and relevant screenshots when safe.

### Validation

Repeat the failed operation after the corrective action. Confirm the expected business function rather than assuming that a technical component being online means the issue is resolved.

### Escalation

Escalate when standard troubleshooting is unsuccessful, multiple users are affected, security concerns exist, infrastructure changes are required, or the issue exceeds service-desk authority.



## 34.14 Knowledge Article: Account locked repeatedly

**Category:** Identity  
**Article ID:** KB-IDENTITY-014

### Symptoms

The user reports: **Account locked repeatedly**.

### Initial Questions

1. When did the issue begin?
2. Was it working previously?
3. What changed immediately before the issue?
4. Is another user affected?
5. Is another device affected?
6. What exact error appears?
7. Is there a workaround?

### Standard Troubleshooting

Review lockout source, saved credentials, mobile devices, mapped drives, and possible compromise.

### Evidence to Collect

Record the device name, user, timestamp, exact error message, affected service, network/location context, and relevant screenshots when safe.

### Validation

Repeat the failed operation after the corrective action. Confirm the expected business function rather than assuming that a technical component being online means the issue is resolved.

### Escalation

Escalate when standard troubleshooting is unsuccessful, multiple users are affected, security concerns exist, infrastructure changes are required, or the issue exceeds service-desk authority.



## 34.15 Knowledge Article: MFA push does not arrive

**Category:** Identity  
**Article ID:** KB-IDENTITY-015

### Symptoms

The user reports: **MFA push does not arrive**.

### Initial Questions

1. When did the issue begin?
2. Was it working previously?
3. What changed immediately before the issue?
4. Is another user affected?
5. Is another device affected?
6. What exact error appears?
7. Is there a workaround?

### Standard Troubleshooting

Check network, registered device, notification state, time synchronization, and identity service status.

### Evidence to Collect

Record the device name, user, timestamp, exact error message, affected service, network/location context, and relevant screenshots when safe.

### Validation

Repeat the failed operation after the corrective action. Confirm the expected business function rather than assuming that a technical component being online means the issue is resolved.

### Escalation

Escalate when standard troubleshooting is unsuccessful, multiple users are affected, security concerns exist, infrastructure changes are required, or the issue exceeds service-desk authority.



## 34.16 Knowledge Article: Internal website unavailable

**Category:** Network/Application  
**Article ID:** KB-NETWORK/APPL-016

### Symptoms

The user reports: **Internal website unavailable**.

### Initial Questions

1. When did the issue begin?
2. Was it working previously?
3. What changed immediately before the issue?
4. Is another user affected?
5. Is another device affected?
6. What exact error appears?
7. Is there a workaround?

### Standard Troubleshooting

Compare users, resolve DNS, test VPN, check service availability, and collect exact errors.

### Evidence to Collect

Record the device name, user, timestamp, exact error message, affected service, network/location context, and relevant screenshots when safe.

### Validation

Repeat the failed operation after the corrective action. Confirm the expected business function rather than assuming that a technical component being online means the issue is resolved.

### Escalation

Escalate when standard troubleshooting is unsuccessful, multiple users are affected, security concerns exist, infrastructure changes are required, or the issue exceeds service-desk authority.



## 34.17 Knowledge Article: Computer cannot boot

**Category:** Hardware/Endpoint  
**Article ID:** KB-HARDWARE/END-017

### Symptoms

The user reports: **Computer cannot boot**.

### Initial Questions

1. When did the issue begin?
2. Was it working previously?
3. What changed immediately before the issue?
4. Is another user affected?
5. Is another device affected?
6. What exact error appears?
7. Is there a workaround?

### Standard Troubleshooting

Check power, diagnostics, recent changes, boot messages, recovery environment, and hardware status.

### Evidence to Collect

Record the device name, user, timestamp, exact error message, affected service, network/location context, and relevant screenshots when safe.

### Validation

Repeat the failed operation after the corrective action. Confirm the expected business function rather than assuming that a technical component being online means the issue is resolved.

### Escalation

Escalate when standard troubleshooting is unsuccessful, multiple users are affected, security concerns exist, infrastructure changes are required, or the issue exceeds service-desk authority.



## 34.18 Knowledge Article: Application crashes at startup

**Category:** Application  
**Article ID:** KB-APPLICATION-018

### Symptoms

The user reports: **Application crashes at startup**.

### Initial Questions

1. When did the issue begin?
2. Was it working previously?
3. What changed immediately before the issue?
4. Is another user affected?
5. Is another device affected?
6. What exact error appears?
7. Is there a workaround?

### Standard Troubleshooting

Collect version and logs, reproduce, check dependencies and recent changes, and compare another user/device.

### Evidence to Collect

Record the device name, user, timestamp, exact error message, affected service, network/location context, and relevant screenshots when safe.

### Validation

Repeat the failed operation after the corrective action. Confirm the expected business function rather than assuming that a technical component being online means the issue is resolved.

### Escalation

Escalate when standard troubleshooting is unsuccessful, multiple users are affected, security concerns exist, infrastructure changes are required, or the issue exceeds service-desk authority.



## 34.19 Knowledge Article: USB device not recognized

**Category:** Hardware  
**Article ID:** KB-HARDWARE-019

### Symptoms

The user reports: **USB device not recognized**.

### Initial Questions

1. When did the issue begin?
2. Was it working previously?
3. What changed immediately before the issue?
4. Is another user affected?
5. Is another device affected?
6. What exact error appears?
7. Is there a workaround?

### Standard Troubleshooting

Test another port/device, inspect device state, verify policy restrictions, and test on a known-good system.

### Evidence to Collect

Record the device name, user, timestamp, exact error message, affected service, network/location context, and relevant screenshots when safe.

### Validation

Repeat the failed operation after the corrective action. Confirm the expected business function rather than assuming that a technical component being online means the issue is resolved.

### Escalation

Escalate when standard troubleshooting is unsuccessful, multiple users are affected, security concerns exist, infrastructure changes are required, or the issue exceeds service-desk authority.



## 34.20 Knowledge Article: Email attachment rejected

**Category:** Email  
**Article ID:** KB-EMAIL-020

### Symptoms

The user reports: **Email attachment rejected**.

### Initial Questions

1. When did the issue begin?
2. Was it working previously?
3. What changed immediately before the issue?
4. Is another user affected?
5. Is another device affected?
6. What exact error appears?
7. Is there a workaround?

### Standard Troubleshooting

Check attachment type, size, security policy, recipient limits, and exact non-delivery message.

### Evidence to Collect

Record the device name, user, timestamp, exact error message, affected service, network/location context, and relevant screenshots when safe.

### Validation

Repeat the failed operation after the corrective action. Confirm the expected business function rather than assuming that a technical component being online means the issue is resolved.

### Escalation

Escalate when standard troubleshooting is unsuccessful, multiple users are affected, security concerns exist, infrastructure changes are required, or the issue exceeds service-desk authority.



## 34.21 Knowledge Article: Shared mailbox unavailable

**Category:** Microsoft 365  
**Article ID:** KB-MICROSOFT-36-021

### Symptoms

The user reports: **Shared mailbox unavailable**.

### Initial Questions

1. When did the issue begin?
2. Was it working previously?
3. What changed immediately before the issue?
4. Is another user affected?
5. Is another device affected?
6. What exact error appears?
7. Is there a workaround?

### Standard Troubleshooting

Check permissions, service health, web access, and Outlook client behavior.

### Evidence to Collect

Record the device name, user, timestamp, exact error message, affected service, network/location context, and relevant screenshots when safe.

### Validation

Repeat the failed operation after the corrective action. Confirm the expected business function rather than assuming that a technical component being online means the issue is resolved.

### Escalation

Escalate when standard troubleshooting is unsuccessful, multiple users are affected, security concerns exist, infrastructure changes are required, or the issue exceeds service-desk authority.



## 34.22 Knowledge Article: Remote desktop unavailable

**Category:** Remote Access  
**Article ID:** KB-REMOTE-ACCES-022

### Symptoms

The user reports: **Remote desktop unavailable**.

### Initial Questions

1. When did the issue begin?
2. Was it working previously?
3. What changed immediately before the issue?
4. Is another user affected?
5. Is another device affected?
6. What exact error appears?
7. Is there a workaround?

### Standard Troubleshooting

Check network, VPN, authorization, endpoint availability, and remote service status.

### Evidence to Collect

Record the device name, user, timestamp, exact error message, affected service, network/location context, and relevant screenshots when safe.

### Validation

Repeat the failed operation after the corrective action. Confirm the expected business function rather than assuming that a technical component being online means the issue is resolved.

### Escalation

Escalate when standard troubleshooting is unsuccessful, multiple users are affected, security concerns exist, infrastructure changes are required, or the issue exceeds service-desk authority.



## 34.23 Knowledge Article: Mobile device cannot enroll

**Category:** Mobile Management  
**Article ID:** KB-MOBILE-MANAG-023

### Symptoms

The user reports: **Mobile device cannot enroll**.

### Initial Questions

1. When did the issue begin?
2. Was it working previously?
3. What changed immediately before the issue?
4. Is another user affected?
5. Is another device affected?
6. What exact error appears?
7. Is there a workaround?

### Standard Troubleshooting

Verify identity, enrollment eligibility, operating-system version, management profile, and licensing.

### Evidence to Collect

Record the device name, user, timestamp, exact error message, affected service, network/location context, and relevant screenshots when safe.

### Validation

Repeat the failed operation after the corrective action. Confirm the expected business function rather than assuming that a technical component being online means the issue is resolved.

### Escalation

Escalate when standard troubleshooting is unsuccessful, multiple users are affected, security concerns exist, infrastructure changes are required, or the issue exceeds service-desk authority.



## 34.24 Knowledge Article: Meeting room display blank

**Category:** Conference Room  
**Article ID:** KB-CONFERENCE-R-024

### Symptoms

The user reports: **Meeting room display blank**.

### Initial Questions

1. When did the issue begin?
2. Was it working previously?
3. What changed immediately before the issue?
4. Is another user affected?
5. Is another device affected?
6. What exact error appears?
7. Is there a workaround?

### Standard Troubleshooting

Check display power, input source, cable, room computer, dock, and known-good source.

### Evidence to Collect

Record the device name, user, timestamp, exact error message, affected service, network/location context, and relevant screenshots when safe.

### Validation

Repeat the failed operation after the corrective action. Confirm the expected business function rather than assuming that a technical component being online means the issue is resolved.

### Escalation

Escalate when standard troubleshooting is unsuccessful, multiple users are affected, security concerns exist, infrastructure changes are required, or the issue exceeds service-desk authority.



## 34.25 Knowledge Article: Keyboard keys intermittently fail

**Category:** Hardware  
**Article ID:** KB-HARDWARE-025

### Symptoms

The user reports: **Keyboard keys intermittently fail**.

### Initial Questions

1. When did the issue begin?
2. Was it working previously?
3. What changed immediately before the issue?
4. Is another user affected?
5. Is another device affected?
6. What exact error appears?
7. Is there a workaround?

### Standard Troubleshooting

Test external keyboard, inspect physical damage, check layout, and determine whether issue follows device.

### Evidence to Collect

Record the device name, user, timestamp, exact error message, affected service, network/location context, and relevant screenshots when safe.

### Validation

Repeat the failed operation after the corrective action. Confirm the expected business function rather than assuming that a technical component being online means the issue is resolved.

### Escalation

Escalate when standard troubleshooting is unsuccessful, multiple users are affected, security concerns exist, infrastructure changes are required, or the issue exceeds service-desk authority.



## 34.26 Knowledge Article: Corporate proxy blocks application

**Category:** Network  
**Article ID:** KB-NETWORK-026

### Symptoms

The user reports: **Corporate proxy blocks application**.

### Initial Questions

1. When did the issue begin?
2. Was it working previously?
3. What changed immediately before the issue?
4. Is another user affected?
5. Is another device affected?
6. What exact error appears?
7. Is there a workaround?

### Standard Troubleshooting

Confirm application requirement, proxy policy, URL/category, logs, and approved exception process.

### Evidence to Collect

Record the device name, user, timestamp, exact error message, affected service, network/location context, and relevant screenshots when safe.

### Validation

Repeat the failed operation after the corrective action. Confirm the expected business function rather than assuming that a technical component being online means the issue is resolved.

### Escalation

Escalate when standard troubleshooting is unsuccessful, multiple users are affected, security concerns exist, infrastructure changes are required, or the issue exceeds service-desk authority.



## 34.27 Knowledge Article: DNS resolves incorrectly

**Category:** Network  
**Article ID:** KB-NETWORK-027

### Symptoms

The user reports: **DNS resolves incorrectly**.

### Initial Questions

1. When did the issue begin?
2. Was it working previously?
3. What changed immediately before the issue?
4. Is another user affected?
5. Is another device affected?
6. What exact error appears?
7. Is there a workaround?

### Standard Troubleshooting

Compare authoritative and corporate resolver results, verify cached records, and escalate DNS changes.

### Evidence to Collect

Record the device name, user, timestamp, exact error message, affected service, network/location context, and relevant screenshots when safe.

### Validation

Repeat the failed operation after the corrective action. Confirm the expected business function rather than assuming that a technical component being online means the issue is resolved.

### Escalation

Escalate when standard troubleshooting is unsuccessful, multiple users are affected, security concerns exist, infrastructure changes are required, or the issue exceeds service-desk authority.



## 34.28 Knowledge Article: Slow file transfer

**Category:** Network/File Services  
**Article ID:** KB-NETWORK/FILE-028

### Symptoms

The user reports: **Slow file transfer**.

### Initial Questions

1. When did the issue begin?
2. Was it working previously?
3. What changed immediately before the issue?
4. Is another user affected?
5. Is another device affected?
6. What exact error appears?
7. Is there a workaround?

### Standard Troubleshooting

Compare file size, location, VPN status, latency, packet loss, and server performance.

### Evidence to Collect

Record the device name, user, timestamp, exact error message, affected service, network/location context, and relevant screenshots when safe.

### Validation

Repeat the failed operation after the corrective action. Confirm the expected business function rather than assuming that a technical component being online means the issue is resolved.

### Escalation

Escalate when standard troubleshooting is unsuccessful, multiple users are affected, security concerns exist, infrastructure changes are required, or the issue exceeds service-desk authority.



## 34.29 Knowledge Article: Unauthorized software detected

**Category:** Security  
**Article ID:** KB-SECURITY-029

### Symptoms

The user reports: **Unauthorized software detected**.

### Initial Questions

1. When did the issue begin?
2. Was it working previously?
3. What changed immediately before the issue?
4. Is another user affected?
5. Is another device affected?
6. What exact error appears?
7. Is there a workaround?

### Standard Troubleshooting

Record software, device, user, and detection source; follow software-removal and security policy.

### Evidence to Collect

Record the device name, user, timestamp, exact error message, affected service, network/location context, and relevant screenshots when safe.

### Validation

Repeat the failed operation after the corrective action. Confirm the expected business function rather than assuming that a technical component being online means the issue is resolved.

### Escalation

Escalate when standard troubleshooting is unsuccessful, multiple users are affected, security concerns exist, infrastructure changes are required, or the issue exceeds service-desk authority.



## 34.30 Knowledge Article: Suspicious login notification

**Category:** Security/Identity  
**Article ID:** KB-SECURITY/IDE-030

### Symptoms

The user reports: **Suspicious login notification**.

### Initial Questions

1. When did the issue begin?
2. Was it working previously?
3. What changed immediately before the issue?
4. Is another user affected?
5. Is another device affected?
6. What exact error appears?
7. Is there a workaround?

### Standard Troubleshooting

Do not approve unexpected authentication. Verify activity and escalate possible credential compromise.

### Evidence to Collect

Record the device name, user, timestamp, exact error message, affected service, network/location context, and relevant screenshots when safe.

### Validation

Repeat the failed operation after the corrective action. Confirm the expected business function rather than assuming that a technical component being online means the issue is resolved.

### Escalation

Escalate when standard troubleshooting is unsuccessful, multiple users are affected, security concerns exist, infrastructure changes are required, or the issue exceeds service-desk authority.



## 34.31 Knowledge Article: Deleted file needs recovery

**Category:** Data Recovery  
**Article ID:** KB-DATA-RECOVER-031

### Symptoms

The user reports: **Deleted file needs recovery**.

### Initial Questions

1. When did the issue begin?
2. Was it working previously?
3. What changed immediately before the issue?
4. Is another user affected?
5. Is another device affected?
6. What exact error appears?
7. Is there a workaround?

### Standard Troubleshooting

Identify location, timestamp, version history, recycle bin, and backup availability.

### Evidence to Collect

Record the device name, user, timestamp, exact error message, affected service, network/location context, and relevant screenshots when safe.

### Validation

Repeat the failed operation after the corrective action. Confirm the expected business function rather than assuming that a technical component being online means the issue is resolved.

### Escalation

Escalate when standard troubleshooting is unsuccessful, multiple users are affected, security concerns exist, infrastructure changes are required, or the issue exceeds service-desk authority.



## 35. User Symptom Phrase Dictionary

Users rarely describe technical problems using technical terminology. Support analysts should map everyday language to technical hypotheses without assuming the cause.

| User wording | Possible technical area |
|---|---|
| "Wi-Fi is connected but nothing loads" | DNS, gateway, DHCP, routing |
| "The internet icon has a warning sign" | Network connectivity |
| "VPN says connected but I can't open company sites" | Internal DNS/routing |
| "It keeps asking me to sign in" | Authentication/session/credentials |
| "My password suddenly stopped working" | Password expiration, lockout, identity sync |
| "Teams can't hear me" | Microphone permissions/device |
| "I can hear them but they can't hear me" | Microphone/input selection |
| "The screen is black" | Display, graphics, power, docking |
| "Laptop is burning hot" | Thermal/hardware issue |
| "Everything is extremely slow" | CPU, memory, disk, network, endpoint health |
| "The printer is there but won't print" | Queue, spooler, network, printer state |
| "My files have little red X marks" | OneDrive synchronization |
| "I clicked something and now I'm worried" | Security incident |
| "I got a login approval I didn't request" | Possible credential compromise |
| "The website says connection is not private" | Certificate/security |
| "My files disappeared" | Sync, deletion, permissions, recovery |
| "The meeting room TV isn't working" | Conference-room equipment |
| "I can't access the shared folder anymore" | Authorization/network/VPN |
| "The update is stuck" | Windows Update/application update |
| "The camera doesn't work" | Camera permissions/device |
| "My laptop won't start" | Power/boot/hardware |
| "I lost my work phone" | Mobile security/identity |
| "I changed my password and now Outlook is broken" | Credential cache/synchronization |
| "Only one website doesn't open" | DNS, proxy, application service |
| "Everyone on my floor has the same issue" | Shared infrastructure |
| "It works at home but not in office" | LAN/Wi-Fi/proxy/policy |
| "It works on my phone but not laptop" | Endpoint/browser/client |


## 36. Support Analyst Decision Trees

### Login Failure

**Can the user sign in anywhere?**

- **No:** Check account state, password, lockout, MFA, and identity service.
- **Yes:** Continue.

**Does the issue occur on another device?**

- **Yes:** Focus on identity/application access.
- **No:** Focus on endpoint configuration.

### Network Failure

**Is Wi-Fi connected?**

- **No:** Resolve Wi-Fi/physical/authentication issue.
- **Yes:** Check IP configuration.

**Does the device have a valid IP and gateway?**

- **No:** Investigate DHCP/network access.
- **Yes:** Test gateway.

**Can gateway be reached?**

- **No:** Investigate local network/VLAN/Wi-Fi.
- **Yes:** Test DNS.

**Can internal hostname resolve?**

- **No:** Investigate DNS/VPN.
- **Yes:** Test application connectivity.

### Application Failure

**Does the application open?**

- **No:** Check installation, dependencies, updates, profile, and endpoint health.
- **Yes:** Continue.

**Does another user have the same problem?**

- **Yes:** Investigate application/service.
- **No:** Investigate user profile, permissions, or local configuration.

### Security Event

**Did the user provide credentials to a suspicious site?**

- **Yes:** Start credential-compromise procedure and Security escalation.
- **No:** Continue investigation.

**Did suspicious software execute?**

- **Yes/Unknown:** Treat as potential security incident and follow containment guidance.
- **No:** Report and analyze according to phishing procedure.


## 37. Glossary

**AD:** Active Directory.

**API:** Application Programming Interface.

**BYOD:** Bring Your Own Device.

**DHCP:** Dynamic Host Configuration Protocol.

**DNS:** Domain Name System.

**EDR:** Endpoint Detection and Response.

**ERP:** Enterprise Resource Planning.

**IAM:** Identity and Access Management.

**IP:** Internet Protocol.

**LAN:** Local Area Network.

**MFA:** Multi-Factor Authentication.

**M365:** Microsoft 365.

**MDM:** Mobile Device Management.

**P1/P2/P3/P4:** Incident priority classifications.

**RCA:** Root Cause Analysis.

**RDP:** Remote Desktop Protocol.

**SLA:** Service Level Agreement.

**SSO:** Single Sign-On.

**VPN:** Virtual Private Network.

**VLAN:** Virtual Local Area Network.

**Wi-Fi:** Wireless networking technology.

**Zero Trust:** Security model that requires explicit verification rather than assuming trust based on network location.


## 38. Final Support Principles

A professional IT support organization does more than make computers work. It protects business operations, users, data, security, and trust.

The core principles are:

1. **Understand before changing.**
2. **Verify before granting access.**
3. **Document before closing.**
4. **Protect credentials and sensitive data.**
5. **Treat security symptoms seriously.**
6. **Use evidence rather than assumptions.**
7. **Change one variable at a time when possible.**
8. **Validate the actual business outcome.**
9. **Escalate early when impact is high.**
10. **Look for recurring problems instead of repeatedly treating symptoms.**
11. **Prefer approved, repeatable procedures.**
12. **Communicate clearly and respectfully.**
13. **Never trade security for convenience without explicit authorization.**
14. **Improve the knowledge base after meaningful incidents.**

This handbook is a synthetic training and RAG dataset. Production environments require organization-specific policies, approved tooling, current vendor documentation, security controls, and formally authorized procedures.
