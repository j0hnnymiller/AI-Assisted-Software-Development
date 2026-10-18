---
name: assess-compliance
description: "Assess architecture and control evidence against applicable standards, regulations, and organizational requirements. Use for privacy, security, governance, or technical compliance reviews; identify evidenced controls, gaps, unknowns, and legal-review questions."

ai_generated: true
model: "OpenAI/GPT-6@Luna"
operator: "johnmillerATcodemag-com"
chat_id: "convert-prompt-files-to-skills-20261016"
prompt: |
  help me convert the prompt files in the prompts folder into skills.
started: "2026-10-16T21:25:07.811Z"
ended: "2026-10-16T21:43:11.234Z"
task_durations:
  - task: "Converting repository prompt files to skills"
    duration: "00:18:03"
total_duration: "00:18:03"
ai_log: "ai-logs/2026/10/16/convert-prompt-files-to-skills-20261016/conversation.md"
source: ".github/prompts/compliance-check.prompt.md"
revisions:
  - chat_id: "0ee42cac-b369-4e34-9193-397eba0fac7a"
    model: "unknown/unknown@unknown"
    date: "2026-10-17"
    change: "Added scope/applicability checks, evidence-status classification, and legal/certification claim boundaries.; Added IEC 62304 scope/evidence boundaries and linked clause-level assessment workflow."
    ai_log: "ai-logs/2026/10/17/0ee42cac-b369-4e34-9193-397eba0fac7a/conversation.md"
  - chat_id: "skill-naming-convention-20261018"
    model: "unknown/unknown@unknown"
    date: "2026-10-18"
    change: "Applied approved skill naming decisions and updated active references; preserved workflow behavior and historical provenance."
    ai_log: "ai-logs/2026/10/18/skill-naming-convention-20261018/conversation.md"
---
# Compliance Validation and Standards Alignment

Assess architecture and implementation evidence against the frameworks and organizational requirements in scope.

## Compliance Frameworks

### Security & Privacy Standards

- **SOC 2 Type II**: Security control framework and audit
- **ISO 27001**: Information security management system
- **NIST Cybersecurity Framework**: Comprehensive security guidance
- **PCI-DSS**: Payment card industry security standard
- **HITRUST**: Healthcare security and compliance

### Privacy Regulations

- **GDPR**: EU General Data Protection Regulation (EU residents)
- **CCPA/CPRA**: California Consumer Privacy Act
- **HIPAA**: Health Insurance Portability and Accountability Act (US healthcare)
- **PIPEDA**: Personal Information Protection and Electronic Documents Act (Canada)
- **LGPD**: Lei Geral de Proteção de Dados (Brazil)

### Industry Standards

- **COBIT**: IT governance and management framework
- **ITIL**: IT service management practices
- **TOGAF**: Enterprise architecture framework
- **CAF**: Cloud Adoption Framework

### Technical Standards

- **OWASP Top 10**: Web application security risks
- **Cloud Security Alliance**: Cloud-specific security controls
- **API Security Standards**: OpenAPI, REST best practices
- **Accessibility Standards**: WCAG 2.1 for accessibility

## Compliance Assessment Framework

### Regulatory Analysis

- Identify applicable regulations and frameworks
- Map to industry and geographic requirements
- Understand control requirements
- Identify gaps and compliance risks

### Architectural Review

- Assess architecture against compliance requirements
- Identify control implementations
- Validate design patterns for compliance
- Evaluate gaps and mitigation strategies

### Implementation Validation

- Verify control implementation
- Assess control effectiveness
- Validate evidence and documentation
- Identify gaps requiring remediation

### Continuous Monitoring

- Establish ongoing compliance assessment
- Regular audit and testing schedule
- Metrics and monitoring for compliance
- Incident reporting and remediation

## Evidence and Assurance Boundaries

- Confirm the jurisdiction, industry, data types, applicable frameworks, review scope, and date. Ask for missing applicability details or mark them unknown; do not infer applicability from examples in this document.
- Map each in-scope requirement to observed architecture, implementation, documentation, and control evidence. A design statement alone does not establish operational implementation or effectiveness.
- Classify each control as **evidenced**, **partially evidenced**, **not evidenced**, **not applicable** (with rationale), or **needs expert verification**.
- Distinguish facts, assumptions, gaps, and unknowns. Mark owners, costs, deadlines, and audit or certification dates unknown unless supplied or verified.
- Treat this as a structured gap review, not legal advice, an audit, or certification. Refer legal, privacy, security, or audit determinations to qualified reviewers.
- For medical-device software lifecycle assessments against IEC 62304, confirm the exact edition, amendments, software scope/classification, and controlled requirement source. Use [`iec62304-compliance-assessment`](../iec62304-compliance-assessment/SKILL.md) for clause-level mapping; this general skill should capture applicability, evidence status, risk, and assurance boundaries without duplicating the clause checklist.
- A cross-clause summary may group evidence for legacy-software assessment, development, maintenance, software risk management, configuration management, and problem resolution, then synthesize executive priorities and remediation phases. Treat these as assessment topics, not a substitute for the controlled clause text or qualified quality/regulatory review.

## Output Structure

1. **📋 Regulatory Requirements Summary**
   - Applicable regulations and frameworks, with scope and applicability evidence
   - Geographic applicability
   - Key requirements and mandates
   - Verified or supplied compliance deadlines and milestones

2. **🔍 Architecture Compliance Assessment**
   - Requirements-to-architecture mapping
   - Control implementation approach
   - Current evidence status and confidence
   - Gaps and risk areas

3. **🛡️ Security & Privacy Controls**
   - Authentication and authorization controls
   - Data protection and encryption
   - Access logging and audit trails
   - Incident response and breach notification
   - Business continuity and disaster recovery

4. **📊 Data Protection & Privacy**
   - Personal data inventory
   - Data classification and handling
   - Consent and lawful basis mapping
   - Data retention and deletion policies
   - International data transfer compliance
   - Privacy impact assessment results

5. **🔐 Access Control & Governance**
   - Identity and access management controls
   - Role-based access control (RBAC)
   - Segregation of duties
   - Access review and attestation
   - Privileged access management

6. **📈 Audit & Monitoring Controls**
   - Audit logging and retention
   - Monitoring and alerting
   - Incident logging and reporting
   - User activity monitoring
   - Configuration change tracking

7. **⚠️ Compliance Gaps & Risks**
   - Identified gaps by requirement
   - Risk assessment for each gap
   - Prioritization and impact analysis
   - Remediation effort and costs

8. **✅ Remediation Plan**
   - Control implementation for each gap
   - Timeline and phasing
   - Resource requirements
   - Validation and testing approach
   - Success criteria

9. **📚 Documentation & Evidence**
   - Required documentation by regulation
   - Evidence collection approach
   - Documentation maintenance process
   - Audit trail requirements

10. **🔄 Ongoing Compliance**
    - Monitoring and assessment schedule
    - Regular audit approach (internal/external)
    - Change management for compliance
    - Incident response procedures
    - Continuous improvement process

11. **📅 Compliance Calendar**
    - Supplied or verified dates and deadlines only
    - Audit and assessment timing
    - Regulatory update monitoring
    - Certification renewal dates

## Common Compliance Requirements

### GDPR Requirements (if EU residents)

- Lawful basis for data processing
- Data subject rights (access, deletion, portability)
- Privacy by design and by default
- Data protection impact assessments
- Breach notification within 72 hours
- Data processing agreements (DPA)

### SOC 2 Requirements (if serving enterprises)

- Security controls and monitoring
- Availability and system performance
- Processing integrity and completeness
- Confidentiality and encryption
- Privacy and data protection

### HIPAA Requirements (if healthcare data)

- PHI protection and encryption
- Access controls and audit logs
- Business associate agreements
- Breach notification procedures
- Minimum necessary principle

### PCI-DSS Requirements (if credit card data)

- Secure network architecture
- Cardholder data protection
- Vulnerability management
- Access control and monitoring
- Security testing and compliance

## Compliance Validation Checklist

### Security Controls

- [ ] Authentication method documented and implemented
- [ ] Authorization model defined and enforced
- [ ] Encryption in transit (TLS/SSL) enabled
- [ ] Encryption at rest implemented
- [ ] Access logging enabled and monitored
- [ ] Change management procedures defined
- [ ] Incident response plan documented
- [ ] Business continuity plan tested

### Privacy Controls

- [ ] Data inventory maintained
- [ ] Data classification implemented
- [ ] Retention policies defined and enforced
- [ ] Deletion procedures in place
- [ ] Consent mechanisms implemented
- [ ] Privacy impact assessment completed
- [ ] Data processing agreements in place
- [ ] Third-party processor agreements executed

### Governance Controls

- [ ] Policies and procedures documented
- [ ] Training and awareness programs
- [ ] Regular auditing and testing schedule
- [ ] Asset inventory maintained
- [ ] Vulnerability assessment process
- [ ] Security patches applied timely
- [ ] Incident reporting procedures
- [ ] Regulatory monitoring process

## Standards Alignment Strategies

- **Incremental Adoption**: Implement controls progressively
- **Quick Wins First**: Address high-risk/low-effort gaps first
- **Automation**: Automate compliance where possible
- **Vendor Solutions**: Leverage managed compliance tools
- **External Audit**: Engage auditors for gap assessment
- **Certification**: Pursue recognized certifications


