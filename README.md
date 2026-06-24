# Android App Legal and Compliance Guard

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Platform: Android](https://img.shields.io/badge/Platform-Android-3DDC84.svg?style=flat&logo=android)](https://developer.android.com)
[![AI Rules: Ready](https://img.shields.io/badge/AI%20Rules-Ready-blueviolet.svg)](#universal-ai-rules)
[![DPDP: 2027 Compliant](https://img.shields.io/badge/India%20DPDP-2027%20Compliant-FF9933.svg)](#global-jurisdictions-covered)
[![GDPR: Compliant](https://img.shields.io/badge/EEA%20GDPR-Compliant-003399.svg)](#global-jurisdictions-covered)

A localized, AI-driven compliance shield for independent Android developers. This toolkit helps you compile, verify, and generate the necessary legal requirements to publish applications without risking regulatory rejections, platform bans, or fines.

This repository compiles complex global data-protection laws, Google Play Policies, and security standards into a pure, Markdown-based local AI skill and universal AI guardrails updated for the 2026/2027 regulatory landscape.

---

## Quick Start Installation

### 1. Global AI Agent Integration (Antigravity IDE / Claude Desktop)
Install this repository as a global compliance skill in your AI assistant configurations directory using the command matching your operating system:

#### Windows PowerShell:
```powershell
git clone https://github.com/Jaimin-prajapati-ds/android-legal-compliance.git "$env:USERPROFILE\.gemini\config\skills\android-legal-compliance"
```

#### macOS and Linux:
```bash
git clone https://github.com/Jaimin-prajapati-ds/android-legal-compliance.git ~/.gemini/config/skills/android-legal-compliance
```

Once installed, your AI agent will automatically reference this skill whenever you ask compliance, permission, or privacy-related questions.

### 2. Project-Level Guardrails (.airules)
Drop the `.airules` file into the root of your Android repository. Any modern AI coding assistant (Cursor, Windsurf, Aider, Copilot, ChatGPT, etc.) will automatically detect the rules and enforce compliance baselines as you write code.

---

## Core Components

### 1. Universal AI Rules (.airules)
The `.airules` file configures your AI coding assistant to operate as a developer-compliance auditor. It enforces secure-by-default code generation and supports interactive chat shortcuts:

| Command | Action | Expected Output |
|---|---|---|
| `/legal [query]` | Analyze compliance risks of a specific permission, SDK, or feature. | Risk assessment referencing GDPR/DPDP/CCPA and remediation code (e.g. replacing READ_CONTACTS with a native Contact Picker). |
| `/privacypolicy` | Dynamically compile a professional Privacy Policy matching your app's actual data footprint. | Customized Privacy Policy containing developer console identity, third-party SDK tables, and India's DPDP 1-year log retention clauses. |
| `/terms` | Draft a tailored Terms of Service / EULA for your application. | Professional ToS containing licensing limits, intellectual property definitions, and fitness/financial disclaimers. |

### 2. Reference Guidelines (references/)
Detailed engineering-focused reference files covering specific compliance domains:

- [references/play-store-policy.md](references/play-store-policy.md): Target SDK versions, developer identity verification, and permissions policies.
- [references/global-privacy-laws.md](references/global-privacy-laws.md): Localized analysis of EU GDPR, India DPDP Act 2023, US state laws (CCPA), LGPD, and PIPEDA.
- [references/children-accessibility.md](references/children-accessibility.md): COPPA compliance, Families Policy, and European Accessibility Act (WCAG 2.1 AA) mobile requirements.
- [references/ad-monetization.md](references/ad-monetization.md): AdMob integration, UMP consent SDK, COPPA flags, and consent pass-through.
- [references/security-baseline.md](references/security-baseline.md): Secrets management, local encrypted storage, and network security configs.
- [references/legal-documents.md](references/legal-documents.md): Clause references and structural requirements for dynamic document generation.
- [references/prelaunch-audit-checklist.md](references/prelaunch-audit-checklist.md): A step-by-step verification checklist to review before submitting an app update.

---

## Directory Structure
```
Repository Root
├── README.md (Usage Guide)
├── .airules (Universal AI System Rules)
├── SKILL.md (Claude/IDE Skill Orchestrator)
└── references/ (Domain-Specific Guidelines)
    ├── ad-monetization.md
    ├── app-store-policy.md
    ├── children-accessibility.md
    ├── global-privacy-laws.md
    ├── legal-documents.md
    ├── play-store-policy.md
    ├── prelaunch-audit-checklist.md
    └── security-baseline.md
```

---

## Global Jurisdictions Covered

- **European Union and United Kingdom (GDPR / ePrivacy):** Enforces strict explicit user consent, cookie/identifier tracking consent, and the right to delete/be forgotten.
- **India (DPDP Act 2023 / DPDP Rules 2025):** Fully covers extraterritorial rules, mandatory standalone consent notices, Grievance Officer details, and the 1-year transaction/processing log retention requirement.
- **United States (CCPA/CPRA patchwork):** Supports opt-out of data sale/sharing, Global Privacy Control (GPC) signals, and minor protection amendments.
- **Brazil (LGPD) & Canada (PIPEDA/Law 25):** Core data subject rights and local processing conditions.
- **Accessibility (EAA):** Mobile layout accessibility, TalkBack compatibility, font scaling, and minimum touch target requirements.

---

## Disclaimer

This project is an engineering-focused reference guide and is not legal advice. Data protection laws, platform developer terms, and regulatory enforcement thresholds change frequently. Always cross-reference facts with official government and platform documentation before publishing. For high-risk applications (e.g. financial transaction processing or biometric tracking), consult a qualified legal professional.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
