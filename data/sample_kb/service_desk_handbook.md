# Service Desk Handbook

**Organization:** Meridian Digital Services Pvt. Ltd.  
**Document Type:** Enterprise Service Desk Knowledge Base  
**Version:** 5.0  
**Effective Date:** October 2026  
**Classification:** Internal Use  
**Primary Region:** India  
**Service Desk Hours:** 08:00–20:00 IST, Monday–Friday  
**Critical Incident Coverage:** 24×7  
**Document Owner:** IT Service Management Office

---

# 1. Introduction

The Service Desk is the primary point of contact between employees and the organization's technology services. Its responsibilities include incident intake, service requests, troubleshooting, user communication, ticket ownership, knowledge management, escalation, and service restoration.

The Service Desk does not exist only to "fix computers." It provides a controlled operational process for maintaining employee productivity while protecting information security, availability, compliance, and user experience.

This handbook provides operational guidance for:

- Ticket creation and classification
- Incident management
- Service request management
- User verification
- Incident prioritization
- SLA management
- First-contact resolution
- Troubleshooting
- Escalation
- Major incident handling
- Identity and access support
- Endpoint support
- Network support
- Microsoft 365 support
- Application support
- Hardware support
- Security-event intake
- Onboarding and offboarding
- Asset handling
- Remote support
- Knowledge management
- Ticket quality
- Service-desk metrics
- Realistic service-desk scenarios

All names, ticket numbers, hostnames, email addresses, IP addresses, employee records, and examples in this handbook are fictional training data.

---

# 2. Service Desk Mission

The Service Desk mission is:

> Restore user productivity safely, quickly, consistently, and transparently while creating useful operational records.

The Service Desk should optimize for:

1. Correct identification of the problem.
2. Appropriate priority.
3. Fast restoration when possible.
4. Secure handling of identity and data.
5. Clear communication.
6. Accurate documentation.
7. Appropriate escalation.
8. Prevention of recurring incidents.

A fast but undocumented workaround is not necessarily good service. A technically correct solution that violates security policy is not a successful resolution.

---

# 3. Service Desk Roles

## 3.1 Service Desk Analyst – L1

Typical responsibilities:

- Receive calls, portal requests, chat requests, and emails.
- Verify users when required.
- Create and classify tickets.
- Perform standard troubleshooting.
- Search the knowledge base.
- Resolve common incidents.
- Fulfill standard requests.
- Communicate ticket status.
- Escalate complex issues.
- Document troubleshooting.

L1 should not perform unauthorized production changes.

## 3.2 Desktop Support – L2

Typical responsibilities:

- Endpoint troubleshooting.
- Hardware replacement.
- Advanced Windows/macOS troubleshooting.
- Device enrollment.
- Application deployment.
- Local network troubleshooting.
- Peripheral support.
- Advanced user-profile issues.

## 3.3 Infrastructure Support

Responsibilities include:

- Servers.
- Network infrastructure.
- DNS.
- DHCP.
- VPN infrastructure.
- Storage.
- Backup.
- Virtualization.

## 3.4 Identity and Access Management

Responsibilities:

- User identity.
- SSO.
- MFA.
- Access groups.
- Application permissions.
- Conditional access.
- Privileged access.

## 3.5 Security Operations

Responsibilities:

- Phishing.
- Malware.
- Credential compromise.
- Suspicious authentication.
- Endpoint alerts.
- Security incidents.
- Threat investigation.

## 3.6 Application Support

Responsibilities:

- Business applications.
- ERP.
- CRM.
- Internal applications.
- Application integrations.
- Application-specific failures.

---

# 4. Ticket Types

Every interaction should be classified correctly.

## Incident

An unplanned interruption or degradation of an IT service.

Examples:

- Outlook stopped receiving email.
- VPN is unavailable.
- Laptop cannot connect to Wi-Fi.
- ERP application is unavailable.

## Service Request

A standard request for something that is not necessarily broken.

Examples:

- Request approved software.
- Request a monitor.
- Request access to a standard application.
- Request a new keyboard.

## Access Request

A request to obtain access to a system or resource.

Examples:

- Access to Finance SharePoint.
- Access to Git repository.
- VPN access.
- Application role assignment.

## Security Incident

An event that may affect confidentiality, integrity, or availability.

Examples:

- Phishing.
- Lost corporate laptop.
- Suspicious login.
- Malware alert.
- Unauthorized MFA request.

## Problem

The underlying cause of one or more recurring incidents.

Example:

> The same VPN failure has occurred every Monday for four weeks.

---

# 5. Ticket Lifecycle

Standard lifecycle:

`New → Assigned → In Progress → Pending → Resolved → Closed`

## New

Ticket has been received but not yet worked.

## Assigned

Ticket has an owner.

## In Progress

Analyst is actively investigating or resolving the issue.

## Pending User

Additional information or user action is required.

## Pending Vendor

A third-party supplier is required.

## Pending Change

Resolution requires an approved change.

## Resolved

The technical issue has been addressed and validation completed.

## Closed

The ticket has passed the closure criteria.

A ticket should not be placed into "Resolved" merely because the analyst has stopped working on it.

---

# 6. Required Ticket Fields

A useful ticket normally contains:

- Ticket ID
- Requester
- Department
- Location
- Contact method
- Service
- Category
- Subcategory
- Priority
- Impact
- Urgency
- Description
- Start time
- Affected device
- Affected application
- Troubleshooting performed
- Evidence collected
- Resolution
- Escalation history
- Related incident/problem/change
- Closure code

Never record:

- Passwords
- MFA codes
- Private keys
- Authentication secrets
- Unnecessary personal information

---

# 7. Ticket Writing Standard

## Poor Ticket Note

> User laptop problem. Fixed.

## Good Ticket Note

> User reported that the laptop could not connect to the corporate Wi-Fi beginning at approximately 10:20 IST. Device was connected to the correct SSID but had no valid IPv4 address. DHCP renewal failed. Other users on the same floor were also affected. Network Operations was contacted and identified a DHCP service issue on the affected VLAN. Service was restored at 10:57 IST. User confirmed access to internal applications and internet.

A good note allows another analyst to understand the incident without calling the original analyst.

---

# 8. User Verification

Verification is required before sensitive actions.

Sensitive actions include:

- Password reset.
- MFA reset.
- Access changes.
- Account unlock.
- Device wipe.
- Data recovery involving confidential data.
- Privileged access.

Approved verification may include:

- Corporate identity verification workflow.
- Manager confirmation through approved channel.
- Identity verification application.
- Help-desk callback to registered contact information.

Never use:

- "The user knows their employee ID, so that is enough."
- Personal social-media profiles.
- Unverified caller ID.
- Information supplied by an unknown external caller.

---

# 9. Incident Priority

## P1 – Critical

A critical service or large population is affected.

Examples:

- Corporate identity unavailable.
- Company-wide internet outage.
- Production platform unavailable.
- Ransomware event.
- Major email outage.

Expected behavior:

- Immediate ownership.
- Major incident process.
- Frequent updates.
- Management notification.
- Continuous investigation.

## P2 – High

Significant business impact.

Examples:

- Entire Finance department cannot access ERP.
- Remote workforce cannot connect to VPN.
- Major office network outage.
- Critical executive meeting-room outage shortly before an external event.

## P3 – Normal

Single-user or small-group issue.

Examples:

- Outlook problem.
- Printer issue.
- Slow laptop.
- Application crash.

## P4 – Low

Non-urgent request.

Examples:

- Standard software request.
- Keyboard replacement.
- General assistance.
- Documentation request.

---

# 10. Impact and Urgency

Priority should be based on business impact and urgency.

## High Impact

- Many employees affected.
- Critical business process unavailable.
- Security incident.
- Revenue-impacting system unavailable.
- Regulatory impact.

## High Urgency

- Payroll deadline.
- Financial close.
- Customer presentation.
- Production deployment.
- Legal/compliance deadline.

A single-user issue can become P2 if the user is performing a critical time-sensitive function and no workaround exists.

However, job title alone should not determine priority.

---

# 11. SLA Management

SLA measurements may include:

- Time to acknowledge.
- Time to first response.
- Time to resolution.
- Time to restore service.
- Time in pending state.

Analysts should monitor tickets approaching SLA breach.

A ticket should not be manipulated between statuses merely to make SLA reporting look better.

---

# 12. First Contact Resolution

First Contact Resolution (FCR) measures whether the issue is resolved during the initial support interaction.

Good candidates for FCR:

- Password reset.
- Standard printer mapping.
- Approved software installation.
- Basic VPN configuration.
- Common Outlook configuration.
- Basic Wi-Fi troubleshooting.

Poor candidates for forced FCR:

- Major network outages.
- Security incidents.
- Complex application defects.
- Infrastructure changes.

FCR should never be increased by prematurely closing tickets.

---

# 13. Service Desk Call Handling

## Opening

Example:

> "Good morning, Meridian IT Service Desk. This is Ananya. How can I help you today?"

## Clarification

Ask:

- What is happening?
- What were you expecting?
- When did it start?
- What error do you see?
- Is anyone else affected?
- What changed before the issue?

## Confirmation

Repeat the issue:

> "Just to confirm, Outlook opens normally, but new messages have not appeared since approximately 09:30, and webmail also shows the same behavior. Is that correct?"

## Troubleshooting

Explain significant actions before performing them.

## Closing

Confirm:

> "Can you please test the process that originally failed?"

Do not close until the user confirms the service works when confirmation is practical.

---

# 14. Chat Support

Chat support should be concise but complete.

Example:

**User:** My VPN doesn't work.

**Analyst:**  
"Sure. Are you able to access the internet normally without VPN?"

**User:** Yes.

**Analyst:**  
"Thanks. What exact message does the VPN client display after you sign in?"

**User:** "Authentication failed."

**Analyst:**  
"Does your MFA work when you sign into the company portal?"

This approach narrows the fault without asking ten unrelated questions.

---

# 15. Email Support

A service-desk email should contain:

- Ticket reference.
- Current status.
- Required user action.
- Expected next step.
- Security reminder when relevant.

Avoid:

> Please send password.

Use:

> Please sign in through the approved password-reset portal. Do not send your password or MFA code to the service desk.

---

# 16. Remote Support

Before remote access:

1. Verify the user.
2. Explain why remote access is needed.
3. Obtain consent where required.
4. Use approved remote-support software.
5. Avoid unrelated personal information.
6. Do not request passwords.
7. Stop when troubleshooting is complete.

After remote support:

- End the session.
- Confirm functionality.
- Document actions.

Never install an unknown remote-access application because a caller says "Microsoft Support" instructed the user to do so.

---

# 17. Windows Service Desk Troubleshooting

## Windows Computer Slow

Ask:

- When did it start?
- Is the whole system slow?
- Which application is slow?
- Does restarting help?
- Is disk space low?

Check:

- CPU.
- Memory.
- Disk.
- Startup applications.
- Updates.
- Endpoint-security activity.
- Storage.

## Windows Update Failure

Collect:

- Windows version.
- Update number.
- Error code.
- Storage availability.
- Last successful update.

Procedure:

1. Restart.
2. Confirm storage.
3. Review update history.
4. Retry.
5. Run approved troubleshooter.
6. Escalate persistent failures.

## Blue Screen

Record:

- Stop code.
- Time.
- Recent drivers.
- Hardware changes.
- Software installations.
- Crash frequency.

Do not repeatedly force the user to continue working on a system that is unstable.

---

# 18. macOS Service Desk Troubleshooting

## Mac Slow

Check:

- Memory pressure.
- CPU.
- Storage.
- Login items.
- Browser tabs/extensions.
- Updates.
- Background synchronization.

## Mac Wi-Fi

Check:

1. Wi-Fi enabled.
2. Correct corporate network.
3. IP address.
4. Gateway.
5. DNS.
6. VPN.
7. Other devices.

## External Display

Check:

- Cable.
- Adapter.
- Dock.
- Display input.
- macOS display settings.
- Another monitor/device.

---

# 19. Password Issues

## Password Forgotten

Use the approved self-service reset process.

If self-service fails:

1. Verify identity.
2. Check account state.
3. Reset using approved administrative workflow.
4. Do not record the password.
5. Confirm sign-in.

## Account Locked

Potential causes:

- Incorrect password attempts.
- Old credentials stored on phone.
- Scheduled task.
- Mapped drive.
- Mail client.
- Potential compromise.

If lockouts occur repeatedly from an unknown source, escalate to Identity/Security.

---

# 20. MFA Issues

## MFA Push Missing

Check:

- Phone internet connection.
- Authenticator app.
- Registered device.
- Notifications.
- Device time.
- Identity service status.

Do not ask the user to send an MFA code.

## Unexpected MFA Request

Tell the user:

> Do not approve the request. If you did not initiate the sign-in, reject it and report it to IT Security.

Repeated unexpected prompts may indicate credential compromise.

---

# 21. Account Access

## User Cannot Access Application

Determine:

- Does SSO work?
- Does the user have an entitlement?
- Does another user have access?
- Did the user's role change?
- Is the application available?

Do not grant access merely because the user says their manager approved it verbally.

Use the approved authorization workflow.

---

# 22. Network Support

## No Internet

Check:

1. Wi-Fi or Ethernet connection.
2. IP address.
3. Gateway.
4. DNS.
5. Proxy.
6. VPN.
7. Service outage.

## DHCP Failure

Possible indicators:

- 169.254.x.x address.
- No gateway.
- Multiple devices affected.

If multiple users have the same problem, escalate to Network Operations.

## DNS Failure

Symptoms:

- Website does not resolve.
- Internal applications unavailable.
- IP access works but hostname fails.

Test approved DNS resolution and compare with another device.

---

# 23. VPN Support

## VPN Does Not Connect

Collect:

- VPN client version.
- Exact error.
- Internet status.
- MFA status.
- Username/account state.
- Time of failure.

Potential causes:

- Credential issue.
- MFA issue.
- Expired certificate.
- Client issue.
- Gateway issue.
- Policy.
- Network restriction.

## VPN Connected but Internal Application Fails

Check:

- Assigned VPN IP.
- Internal DNS.
- Routing.
- Application availability.
- User authorization.

A successful VPN connection does not guarantee application access.

---

# 24. Outlook Support

## Outlook Does Not Open

Check:

- Device health.
- Updates.
- Profile.
- Add-ins.
- Disk space.
- Webmail availability.

## Outlook Cannot Send

Check:

- Connectivity.
- Account state.
- Mailbox quota.
- Recipient.
- Attachment.
- Bounce-back message.

## Outlook Search Not Working

Compare:

- Desktop Outlook.
- Webmail.

If webmail search works but desktop search fails, investigate local indexing/profile issues.

---

# 25. Microsoft Teams

## Cannot Join Meeting

Check:

- Internet.
- Account.
- Meeting link.
- Teams status.
- Browser/web client.
- Camera/microphone permissions.

## Microphone Not Working

Check:

1. OS permission.
2. Selected input device.
3. Headset connection.
4. Teams device selection.
5. Another application.
6. Another headset.

## Camera Not Working

Check:

- Privacy shutter.
- OS permission.
- Teams selection.
- Other applications using camera.
- Device state.

---

# 26. OneDrive

## Files Not Syncing

Check:

- Account signed in.
- Storage.
- Internet.
- Sync status.
- File naming restrictions.
- File path.
- Service health.

Never tell the user to delete their OneDrive folder without verifying that all important data is synchronized.

## Missing File

Determine:

- File location.
- Last known time.
- User/device.
- Whether another person moved it.
- Version history.
- Recycle bin.

---

# 27. Printer Support

## Printer Not Printing

Check:

1. Printer power.
2. Network.
3. Correct printer.
4. Queue.
5. Test page.
6. Other applications.
7. Other users.

## Multiple Users Cannot Print

Do not repeatedly reinstall printer drivers.

Investigate:

- Print server.
- Network.
- Printer availability.
- Queue service.
- Printer status.

---

# 28. Hardware Requests

## Keyboard Replacement

Standard request if:

- Keys are physically damaged.
- Device fails on known-good computer.
- Cable/Bluetooth troubleshooting fails.

## Monitor Request

Check:

- Existing monitor.
- Business requirement.
- Available equipment.
- Approved model.
- Manager approval where required.

## Laptop Replacement

Replacement should consider:

- Age.
- Warranty.
- Hardware failure.
- Business requirements.
- Repair history.
- Security state.
- Approved lifecycle.

---

# 29. Software Requests

Standard software requests should include:

- Software name.
- Version if relevant.
- Business purpose.
- User.
- Manager approval.
- License requirement.

Software should be installed from approved sources.

Never install pirated software, unauthorized cracks, or unknown executables.

---

# 30. Application Troubleshooting

When an application fails:

1. Reproduce.
2. Capture exact error.
3. Check application version.
4. Check service health.
5. Test another user.
6. Test another device.
7. Review recent changes.
8. Review logs if accessible.
9. Escalate with evidence.

The distinction between:

> "The application is broken"

and

> "The application opens, but the Invoice Search page returns HTTP 503 only for Finance users"

is critical for escalation quality.

---

# 31. Security Event Intake

## Phishing

If user reports phishing:

1. Tell user not to click further.
2. Preserve the message.
3. Report through approved method.
4. Ask whether credentials were entered.
5. Ask whether an attachment was executed.
6. Escalate based on risk.

## Credential Compromise

If credentials may have been exposed:

- Follow password reset process.
- Revoke sessions where required.
- Check MFA.
- Escalate Security.
- Record timeline.

## Lost Laptop

Collect:

- Asset number.
- Serial number.
- Last known location.
- Last known time.
- User.
- Whether encryption is enabled.

Escalate immediately.

---

# 32. Malware Report

Potential indicators:

- Unexpected antivirus alert.
- Files changing unexpectedly.
- Browser redirects.
- Unknown applications.
- Security controls disabled.
- Unusual pop-ups.
- Suspicious network activity.

Do not tell users to download random antivirus tools.

Follow the security incident procedure.

---

# 33. Employee Onboarding

Before start date:

- Account created.
- MFA prepared.
- Laptop assigned.
- Device enrolled.
- Encryption verified.
- Standard software installed.
- Email enabled.
- Teams enabled.
- Required application access assigned.
- VPN configured where required.
- Asset record completed.

On first day:

1. Verify identity.
2. Complete initial sign-in.
3. Configure MFA.
4. Test email.
5. Test Teams.
6. Test required applications.
7. Confirm network.
8. Explain IT support process.

---

# 34. Employee Offboarding

Actions depend on approved HR instructions and effective time.

Possible actions:

- Disable identity.
- Revoke sessions.
- Disable VPN.
- Remove application access.
- Recover equipment.
- Transfer business data.
- Process mailbox.
- Update asset records.
- Notify Security.
- Confirm completion.

Do not disable an account based on an informal request without proper authorization.

---

# 35. Access Requests

An access request should identify:

- User.
- System.
- Requested role.
- Business justification.
- Manager/owner approval.
- Start date.
- End date if temporary.

For privileged access, use the dedicated privileged-access process.

---

# 36. Shared Folder Access

Troubleshooting:

1. Confirm network/VPN.
2. Confirm path.
3. Test DNS.
4. Test another folder.
5. Check permissions.
6. Confirm group membership.
7. Check whether server is available.

Do not simply grant "Full Control" to solve a permissions issue.

---

# 37. Remote Worker Support

Remote users may experience:

- Home Wi-Fi issues.
- ISP problems.
- VPN problems.
- DNS issues.
- Latency.
- Video-conference problems.

First separate:

> Is the user's home internet unavailable?

from:

> Is the corporate service unavailable?

The distinction determines escalation.

---

# 38. Meeting Room Support

Before an important meeting:

- Display powered on.
- Correct input selected.
- Room computer working.
- Camera detected.
- Microphone detected.
- Speakers working.
- Network working.
- Teams/Zoom application signed in as designed.
- HDMI/USB-C cable available.

For executive or customer meetings, a known-good backup cable and presentation device should be available where business policy permits.

---

# 39. Mobile Device Support

## Corporate Phone Lost

1. Verify identity.
2. Record device.
3. Notify mobile-management/security team.
4. Suspend or wipe according to approved policy.
5. Reset/re-register MFA if required.
6. Record incident.

## Phone Cannot Receive MFA

Check:

- Internet.
- Phone number.
- Authenticator registration.
- Notifications.
- Device replacement.
- Time synchronization.

---

# 40. Service Request Fulfillment

A standard request should follow:

`Request → Approval → Fulfillment → Validation → Closure`

Examples:

- Software.
- Hardware.
- Access.
- Distribution-list membership.
- Shared mailbox.
- VPN access.

Requests requiring approval should not be fulfilled before approval.

---

# 41. Major Incident Management

A major incident is an incident requiring coordinated response due to scale or business impact.

Typical process:

1. Identify.
2. Declare.
3. Assign incident commander.
4. Establish communication channel.
5. Identify technical leads.
6. Establish timeline.
7. Investigate.
8. Communicate.
9. Restore.
10. Validate.
11. Close.
12. Conduct post-incident review.

The incident commander coordinates. Technical teams investigate.

---

# 42. Major Incident Communication

Good communication:

> **14:00 IST – Service Update**  
> Corporate VPN access is currently unavailable for a significant number of remote users. Internet connectivity outside the corporate VPN remains available. Network and Identity teams are investigating authentication failures. Users should not repeatedly reset passwords. The next update will be provided at 14:30 IST.

Avoid speculation such as:

> The firewall definitely broke.

unless confirmed.

---

# 43. Escalation Rules

Escalate when:

- Security concern exists.
- Multiple users are affected.
- Infrastructure change is required.
- Privileged access is required.
- Standard procedure failed.
- Vendor support is required.
- SLA risk is high.
- Business impact is increasing.

A good escalation includes:

- Summary.
- Impact.
- Timeline.
- Error.
- Tests performed.
- Results.
- Current state.
- Requested assistance.

---

# 44. Escalation Example

## Poor

> VPN doesn't work. Please check.

## Good

> P2 – VPN authentication failure affecting 27 remote Finance users since 08:35 IST. Internet connectivity and MFA portal access are working. VPN client reaches gateway but authentication returns error AUTH-4032. Two non-Finance users successfully connected during testing. Issue appears limited to Finance VPN group. No endpoint-specific pattern identified. Identity Operations assistance requested to review policy evaluation logs.

---

# 45. Vendor Escalation

Vendor cases should include:

- Product.
- Version.
- Tenant/account identifier where appropriate.
- Timestamp.
- Error.
- Reproduction steps.
- Logs.
- Business impact.
- Troubleshooting performed.
- Contact details according to contract.

Do not send confidential data to vendors unless authorized.

---

# 46. Knowledge Management

A knowledge article should contain:

## Title

Specific and searchable.

## Symptoms

What the user sees.

## Cause

Known confirmed cause.

## Resolution

Numbered steps.

## Validation

How to verify.

## Escalation

When to escalate.

## Related Articles

Links or article IDs.

## Owner

Team responsible for accuracy.

## Review Date

Date the article should be reviewed.

---

# 47. Knowledge Article Example

## KB-SD-001: VPN Connected but Internal Website Does Not Open

### Symptoms

User reports VPN is connected but internal websites fail.

### Checks

1. Confirm VPN assigned an IP.
2. Resolve internal hostname.
3. Test approved internal service.
4. Check route.
5. Compare another internal application.

### Possible Causes

- DNS.
- Routing.
- Authorization.
- Application outage.
- VPN policy.

### Resolution

Resolve the specific failed layer rather than reinstalling the VPN client immediately.

### Escalation

Escalate to Network or Application Support when infrastructure or service-side investigation is required.

---

# 48. Service Desk Metrics

Useful metrics include:

- Ticket volume.
- First Contact Resolution.
- Mean Time to Resolve.
- Mean Time to Respond.
- SLA compliance.
- Reopen rate.
- Customer satisfaction.
- Backlog.
- Aging tickets.
- Escalation rate.
- Knowledge-article usage.
- Major incident count.

Metrics should be interpreted together.

For example, extremely high FCR combined with high ticket reopen rate may indicate that analysts are closing tickets too quickly.

---

# 49. Customer Satisfaction

After resolution, users may provide feedback.

Factors influencing satisfaction:

- Speed.
- Clarity.
- Professionalism.
- Ownership.
- Communication.
- Resolution quality.

A technically correct answer delivered disrespectfully is still poor service.

---

# 50. Difficult User Conversations

## User Is Angry

Do:

- Listen.
- Acknowledge impact.
- Clarify the problem.
- Explain next action.
- Set realistic expectations.

Avoid:

- Arguing.
- Blaming.
- Saying "that's not my problem."
- Making unsupported promises.

Example:

> "I understand this is blocking your work. I'll first confirm whether this is limited to your laptop or affecting the shared service. Once I establish that, I'll either work through the standard fix or escalate it to the appropriate team."

---

# 51. User Demands Immediate Access

If approval is missing:

> "I understand the access is urgent. The request requires authorization from the application owner before we can grant it. I can route the request through the expedited approval process if the business deadline requires it."

Never bypass authorization because a user is under time pressure.

---

# 52. User Gives Password to Analyst

The analyst should immediately instruct:

> "Please do not share passwords with IT staff. I will not use or record that password. Please change it using the approved password-reset process."

Do not copy the password into the ticket.

If the password may have been exposed, follow credential-compromise procedures.

---

# 53. Common Service Desk Mistakes

Avoid:

1. Closing without validation.
2. Asking for passwords.
3. Reinstalling software without understanding the issue.
4. Blaming the user.
5. Escalating without evidence.
6. Ignoring security indicators.
7. Changing production settings without approval.
8. Writing vague ticket notes.
9. Treating every issue as P1.
10. Treating every executive request as P1.
11. Deleting data during troubleshooting.
12. Repeating the same unsuccessful procedure.
13. Ignoring recurring incidents.
14. Failing to communicate during delays.

---

# 54. Troubleshooting Philosophy

Use evidence.

### Symptom

> User cannot access payroll application.

### Hypothesis 1

Network problem.

### Test

Can user access other internal applications?

### Result

Yes.

### Hypothesis 2

Payroll application problem.

### Test

Can another payroll user access it?

### Result

No.

### Conclusion

Likely application-side issue.

This approach is better than immediately resetting the user's password.

---

# 55. Decision Tree – User Cannot Access Application

**Step 1:** Can user access the internet?

- No → Network troubleshooting.
- Yes → Continue.

**Step 2:** Can user access corporate SSO?

- No → Identity troubleshooting.
- Yes → Continue.

**Step 3:** Can another application work?

- No → Network/identity issue.
- Yes → Continue.

**Step 4:** Can another user access the application?

- No → Application/service issue.
- Yes → User authorization/profile issue.

---

# 56. Decision Tree – Email Failure

**Can webmail open?**

- No → Identity/network/service.
- Yes → Continue.

**Can webmail send?**

- No → Mailbox/service issue.
- Yes → Continue.

**Can desktop Outlook send?**

- No → Outlook client/profile issue.
- Yes → Continue.

**Does only one recipient fail?**

- Yes → Recipient/address/delivery issue.
- No → Broader mail issue.

---

# 57. Decision Tree – Wi-Fi

**Wi-Fi visible?**

- No → Adapter/access-point investigation.
- Yes → Continue.

**Authentication succeeds?**

- No → Credentials/certificate/network authentication.
- Yes → Continue.

**Valid IP assigned?**

- No → DHCP/network.
- Yes → Continue.

**Gateway reachable?**

- No → Local network.
- Yes → Continue.

**DNS works?**

- No → DNS.
- Yes → Application/internet routing.

---

# 58. Realistic Ticket Examples

## INC-2026-40081 – Finance VPN Failure

**Priority:** P2  
**Requester:** Finance Operations  
**Affected Users:** 31  
**Start:** 08:22 IST

### Symptoms

Multiple Finance users could connect to the internet but received "Authentication policy rejected" when connecting to VPN.

### Investigation

MFA portal worked. VPN gateway was reachable. Non-Finance users connected successfully.

### Escalation

Identity Operations reviewed group-policy logs.

### Resolution

An incorrect group condition was identified in an access policy. Approved change restored access.

### Validation

Five Finance users successfully connected from different networks.

---

## INC-2026-40102 – Outlook Search Failure

**Priority:** P3  
**User:** Engineering  
**Symptoms:** Search returns only messages older than six months.

### Investigation

Webmail returned current messages. Desktop client indexing was incomplete.

### Resolution

Approved index repair procedure completed.

### Validation

Search returned current messages.

---

## INC-2026-40115 – Suspicious MFA Requests

**Priority:** P1 Security

User reported receiving five MFA prompts within ten minutes without attempting to sign in.

### Action

User denied prompts. Security Operations was notified. Identity team reviewed authentication logs and forced credential reset according to incident procedure.

### Result

Suspicious authentication attempts stopped.

---

## INC-2026-40127 – Floor Wi-Fi Outage

**Priority:** P2

Approximately 70 users on the third floor experienced intermittent connectivity.

### Investigation

Multiple endpoints showed valid configurations but repeated disconnections. Network team identified an access-point configuration issue.

### Resolution

Configuration corrected and access point restarted under approved procedure.

---

## INC-2026-40141 – Laptop Not Booting

**Priority:** P2

Laptop repeatedly restarted after firmware update.

### Investigation

Hardware diagnostics passed. Recovery environment available.

### Resolution

Endpoint Engineering restored approved firmware and validated boot.

---

# 59. Service Request Examples

## SR-2026-50021 – Adobe Reader Installation

**Type:** Software Request  
**User:** Legal Department  
**Approval:** Manager approved  
**Action:** Installed from corporate software portal.

## SR-2026-50034 – New Monitor

**Type:** Hardware Request  
**User:** Design Team  
**Business Reason:** Required for dual-display workflow.

## SR-2026-50046 – SharePoint Access

**Type:** Access Request  
**Approval:** Site owner approved  
**Action:** Added user to approved group.

## SR-2026-50059 – VPN Access

**Type:** Access Request  
**Approval:** Manager and application owner approved  
**Action:** VPN entitlement assigned.

---

# 60. Security Ticket Examples

## SEC-2026-70018 – Phishing Email

User reported an email pretending to be from the HR department.

The message requested login information through an external website.

The user did not click the link.

### Action

Message submitted to Security Operations. Sender/domain blocked according to security process.

---

## SEC-2026-70029 – Credentials Entered on Suspicious Site

User entered corporate username and password into a website that appeared to be a Microsoft login page.

### Action

Credential-compromise procedure initiated. Password reset performed through approved workflow. Sessions revoked. Security investigation opened.

---

## SEC-2026-70044 – Lost Corporate Laptop

User reported laptop missing after travel.

### Action

Asset identified. Security notified. Device-management team initiated approved remote protection procedure.

---

# 61. Onboarding Ticket Example

## SR-2026-50121 – New Employee

**Start Date:** 15-Oct-2026  
**Department:** Data Engineering

### Checklist

- Identity account.
- Email.
- MFA.
- Laptop.
- Encryption.
- Endpoint management.
- Python development tools.
- Git client.
- Teams.
- VPN.
- Internal repositories.
- Asset assignment.

### Validation

User successfully authenticated and accessed all approved resources.

---

# 62. Offboarding Ticket Example

## SR-2026-50198 – Employee Departure

**Effective Time:** 18:00 IST

### Checklist

- Identity disabled at approved time.
- Sessions revoked.
- VPN disabled.
- Application access removed.
- Laptop recovered.
- Asset updated.
- Business data handled according to retention policy.
- Security notified.

---

# 63. Hardware Replacement Workflow

`Report → Diagnose → Warranty Check → Approval → Replacement → Data Protection → Validation → Asset Update`

Before replacing:

- Confirm failure.
- Attempt approved diagnostics.
- Protect user data.
- Check warranty.
- Verify replacement eligibility.

After replacement:

- Update asset record.
- Configure device.
- Apply security controls.
- Restore approved data.
- Validate user applications.

---

# 64. Data Recovery

When a user reports a deleted file:

Ask:

- Where was it stored?
- What was the filename?
- When was it last seen?
- Was it local, OneDrive, SharePoint, or network storage?
- Was it shared?
- Is there a known version?

Do not promise recovery before confirming backup/version availability.

---

# 65. Service Desk Handoff

When transferring a ticket:

Include:

- Why it is being transferred.
- What has already been tested.
- Results.
- Business impact.
- User availability.
- Required next action.

Poor:

> Please take this.

Good:

> Transferring to Network Operations because three users in Building B cannot obtain DHCP addresses. Local endpoint checks completed on two devices. Both show 169.254.x.x addresses. Users on another floor are unaffected. Issue began at approximately 11:40 IST.

---

# 66. Pending Ticket Management

Tickets should not remain pending indefinitely.

For Pending User:

- State what information is needed.
- Give a response deadline when appropriate.
- Follow up according to SLA/process.

Example:

> We need the exact error displayed by the VPN client to continue. Please reply with the error text when convenient. Do not send your password or MFA code.

For Pending Vendor:

- Record vendor case number.
- Record next vendor update.
- Track SLA.
- Continue communicating with user.

---

# 67. Reopened Tickets

A ticket should be reopened when:

- The original issue returns.
- Resolution was incomplete.
- The user reports the same unresolved symptom.

A new ticket may be appropriate when:

- The original issue is unrelated.
- A separate incident occurred later.
- Different service is affected.

Repeated reopenings may indicate poor resolution quality or an underlying problem.

---

# 68. Problem Management

Create a problem record when:

- Same incident repeatedly occurs.
- Root cause is unknown.
- Workaround exists but permanent fix is required.
- Multiple users experience similar failures.

Example:

### Incident Pattern

Every Monday morning, approximately 20 remote users cannot connect to VPN.

### Problem Investigation

Possible causes:

- Certificate expiration.
- Scheduled identity policy.
- Capacity.
- Network provider.
- Authentication policy.
- Endpoint update.

The problem team investigates the underlying cause rather than treating each Monday ticket independently.

---

# 69. Change Management for Service Desk

The Service Desk should understand whether a proposed resolution requires a change.

Examples requiring change:

- Firewall modification.
- DNS record update.
- Production configuration change.
- Network switch configuration.
- Identity policy modification.
- Server restart outside approved procedure.

The analyst should not say:

> "I'll just change the firewall rule."

Instead:

> "This requires a network change. I will create/escalate the approved change request and associate it with this incident."

---

# 70. Emergency Changes

Emergency changes are used only when necessary to restore or protect critical services.

Even emergency changes should have:

- Reason.
- Owner.
- Risk.
- Action.
- Validation.
- Rollback.
- Post-change review.

Emergency does not mean undocumented.

---

# 71. Vendor Management

When a ticket requires a vendor:

Record:

- Vendor.
- Case number.
- Contact.
- Date opened.
- Current status.
- Next action.
- Expected response.
- Business impact.

Do not let vendor tickets disappear from the internal queue.

The organization still owns communication with the employee even when a supplier performs the technical fix.

---

# 72. Service Desk Knowledge Search

Before troubleshooting from memory:

1. Search exact error.
2. Search service.
3. Search symptom.
4. Search recent incidents.
5. Check service status.
6. Use approved article.

Example search terms:

- "Outlook authentication loop"
- "VPN AUTH-4032"
- "Windows 11 printer offline"
- "Teams microphone missing"
- "OneDrive red X"
- "MFA push not received"

---

# 73. Knowledge Article Quality

A good article is:

- Accurate.
- Current.
- Searchable.
- Specific.
- Tested.
- Safe.
- Easy to follow.

A bad article:

> Restart everything and see if it works.

A better article:

> Restart the Teams client, confirm the correct microphone is selected under Settings → Devices, and test the microphone using the operating-system audio test. If the microphone remains unavailable, test with a known-good headset and record the result.

---

# 74. Service Desk Training Scenarios

## Scenario 1

User says:

> "My internet is not working."

Ask:

- Is Wi-Fi connected?
- Is the problem on one device?
- Can the user access the company portal?
- Can the user access any public website?
- Does another device work?

Do not immediately reboot the router or change DNS settings.

## Scenario 2

User says:

> "My manager told me to give myself admin access."

Response:

> "Administrative access requires the approved authorization workflow. I can help submit or route the request."

## Scenario 3

User says:

> "I got an MFA request but didn't log in."

Response:

> "Do not approve it. Please reject the request and report it so Security can review the authentication activity."

---

# 75. Common User Language

Users may say:

| User Statement | Possible Area |
|---|---|
| "Internet is dead" | Network |
| "Wi-Fi keeps dropping" | Wi-Fi |
| "VPN is stuck" | VPN |
| "Mail is not coming" | Outlook/M365 |
| "Teams can't hear me" | Audio |
| "My screen is gone" | Display |
| "Computer is freezing" | Endpoint |
| "Everything is slow" | Endpoint/network |
| "I can't get into the folder" | Access |
| "It keeps asking for password" | Identity |
| "Someone is trying to log in to me" | Security |
| "Files have red crosses" | OneDrive |
| "Printer disappeared" | Printing |
| "Camera doesn't exist" | Endpoint permissions |
| "Laptop is not charging" | Hardware |
| "The website says unsafe" | Certificate/security |
| "I clicked a strange email" | Security |
| "I lost my phone" | Mobile security |

---

# 76. Service Desk Glossary

**Incident:** Unplanned interruption or degradation.

**Request:** Standard user request.

**Problem:** Underlying cause of incidents.

**Change:** Controlled modification to an IT environment.

**SLA:** Service Level Agreement.

**FCR:** First Contact Resolution.

**MTTR:** Mean Time to Resolve/Restore.

**P1:** Critical priority.

**P2:** High priority.

**P3:** Normal priority.

**P4:** Low priority.

**SSO:** Single Sign-On.

**MFA:** Multi-Factor Authentication.

**VPN:** Virtual Private Network.

**DNS:** Domain Name System.

**DHCP:** Dynamic Host Configuration Protocol.

**EDR:** Endpoint Detection and Response.

**IAM:** Identity and Access Management.

**RCA:** Root Cause Analysis.

**KB:** Knowledge Base.

**L1:** First-line support.

**L2:** Specialist support.

**L3:** Engineering/vendor-level support.

---

# 77. Final Service Desk Principles

1. Own the ticket.
2. Verify before changing.
3. Never request passwords.
4. Treat unexpected MFA activity seriously.
5. Prioritize business impact.
6. Communicate before users have to ask.
7. Document facts.
8. Escalate with evidence.
9. Validate the actual business outcome.
10. Protect user data.
11. Use approved tools.
12. Follow change control.
13. Learn from recurring incidents.
14. Improve knowledge articles.
15. Never sacrifice security for convenience.
16. Treat users respectfully.
17. Do not guess when evidence can be collected.
18. Do not close tickets just to reduce backlog.
19. Keep ownership clear during escalation.
20. A successful Service Desk restores productivity safely and leaves a useful record of what happened.

---

# 78. Synthetic Dataset Notice

This handbook is designed as a synthetic enterprise Service Desk dataset for:

- RAG systems.
- Semantic search.
- Knowledge-base retrieval.
- IT support chatbot development.
- Ticket classification.
- Intent classification.
- Question answering.
- Embedding evaluation.
- Chunking experiments.
- Agent evaluation.
- Service-desk workflow demonstrations.

All organizations, employees, ticket IDs, addresses, IP addresses, system names, and examples are fictional.
