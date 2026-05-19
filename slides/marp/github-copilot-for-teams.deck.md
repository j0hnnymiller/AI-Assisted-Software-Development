---
marp: true
theme: default
paginate: true
---

# GitHub Copilot for Teams || Deploying AI Without Deploying Chaos

---

## GitHub Copilot for Teams

Key Considerations for Adoption

Empowering developers with AI while protecting your codebase

::: notes
Outline governance, admin controls, and adoption factors (training, policy, developer onboarding).
:::

---

## Risks to Consider

IP Leakage Concerns
  - Copilot may suggest code similar to public repositories
  - Risk of inadvertently using copyrighted or licensed code
  - Mitigation: Enable public code filters and review suggestions carefully
Code Quality and Accuracy
  - AI-generated code may contain bugs, inefficiencies, or security flaws
  - Always validate and test before deployment
  - Treat Copilot as a drafting tool, not a source of truth
Developer Overreliance
  - Risk of reduced understanding or critical thinking
  - Encourage code reviews and pair programming to maintain rigor

::: notes
Cover IP leakage, code quality risks, and developer overreliance; suggest mitigations for each.
:::

---

## Governance and Compliance Risks

Regulatory Compliance
  - Generated code may not meet industry-specific standards (e.g., HIPAA, PCI-DSS)
  - Organizations must enforce coding policies and audits
Data Privacy and Security
  - Sensitive data should never be typed into prompts
  - Use Copilot in secure environments with clear usage guidelines
Licensing Ambiguity
  - Copilot suggestions may resemble code under restrictive licenses
  - Legal teams should define acceptable use policies and monitor compliance

::: notes
Discuss regulatory impacts, auditability, and how to enforce coding policies with automated checks.
:::

---

## IP and Data Protection

- Your code is not used to retrain the model (with Copilot for Business/Enterprise)
- Suggestions are generated locally — no code is shared unless feedback is submitted
- No leakage between users: your private code is not exposed to others
- Admins can disable suggestions matching public code for added safety
- In April 2026, GitHub made this opt-out

::: notes
Clarify data flows, model retraining policy for enterprise plans, and recommended org controls to protect IP.
:::

---

## Licensing and Legal Considerations

- Copilot may suggest code similar to public repositories
- GitHub provides a filter to block matching public code
- Organizations should review Copilot's Terms of Service and Privacy Statement

::: notes
Explain risks of suggested code resembling public repos and recommend legal review and filter settings.
:::

---

## Deployment Options

| Plan                           | Key Features                       | IP Protection |
| ------------------------------ | ---------------------------------- | ------------- |
| Copilot Individual (Pro, Pro+) | Personal use, no admin controls    | Limited       |
| Copilot for Business           | Admin controls, policy enforcement | Strong        |
| Copilot for Enterprise         | Org-wide policy, audit tools       | Strongest     |

::: notes
Summarize plan differences and pick considerations (control, audit, scale) for each offering.
:::

---

## Resources

- Copilot Documentation:
  https://docs.github.com/en/copilot
- Copilot for Business Overview
  https://github.com/features/copilot-for-business
- Security and Privacy FAQ
  https://docs.github.com/en/copilot/security

::: notes
Point attendees to official docs and FAQs; recommend follow-up reading links on the slide.
:::
