# Global Privacy Laws — Reference

Read this when Step 2 of SKILL.md flags any data-protection regime. Covers the laws that actually matter for an indie Android app with a global user base.

## Contents
- [Universal rights table](#universal-rights-table-applies-across-almost-every-regime-below)
- [EU/UK/Switzerland — GDPR family](#eu-uk-switzerland--gdpr-family)
- [India — DPDP Act 2023 + DPDP Rules 2025](#india--dpdp-act-2023--dpdp-rules-2025)
- [United States — CCPA/CPRA + 20-state patchwork](#united-states--ccpacpra--20-state-patchwork)
- [Brazil — LGPD](#brazil--lgpd)
- [Canada — PIPEDA](#canada--pipeda)
- [European Union — European Accessibility Act (EAA)](#european-union--european-accessibility-act-eaa)
- [Other notable regimes](#other-notable-regimes)

---

## Universal rights table (applies across almost every regime below)

Build these as app features once, reuse everywhere — it's cheaper than bolting on per-region logic later:

| Right | What to build |
|---|---|
| Right to know / access | A way to show the user what data you hold on them (export endpoint or settings screen) |
| Right to delete | Account deletion (in-app + web link) that actually erases data, not just deactivates |
| Right to correct | Editable profile fields |
| Right to withdraw consent | A "Privacy choices" screen that re-opens the consent flow / ad personalization toggle |
| Right to opt out of sale/sharing/targeted ads | A toggle that flips your AdMob/analytics SDKs into non-personalized mode |
| Breach notification | An internal incident process — most regimes require notifying a regulator within 72 hours of becoming aware of a serious breach |
| Data minimization | Don't collect a permission/field "just in case" — every collected field needs to map to a stated purpose |

---

## EU, UK, Switzerland — GDPR family

- **Applies to:** anyone offering an app to people in the EEA/UK/Switzerland, regardless of where you (the developer) are based. No revenue or user-count threshold — one EU user is enough.
- **Lawful basis required** for every processing activity — consent, contract necessity, or legitimate interest are the common ones for indie apps. Ad personalization and analytics almost always need **consent**, not legitimate interest.
- **Consent must be**: freely given, specific, informed, unambiguous, and as easy to withdraw as to give. Pre-ticked boxes and "consent walls" that block app use are not valid.
- **DPO (Data Protection Officer)**: only mandatory for large-scale/high-risk processing — a solo dev with a small app usually doesn't need one, but should still have a named contact point in the Privacy Policy.
- **Ads in EEA/UK/CH**: a Google-certified Consent Management Platform (Google's own UMP SDK qualifies) is **mandatory**, not best practice — see `ad-monetization.md`.
- **Fines**: up to €20M or 4% of global annual turnover, whichever is higher.
- **Cross-border transfer**: if your backend (Firebase, AWS, etc.) is outside the EEA, you're generally fine using major US cloud providers under current adequacy/SCC mechanisms — but don't build your own ad-hoc data pipe to a non-adequate country without checking current Standard Contractual Clauses status.

---

## India — DPDP Act 2023 + DPDP Rules 2025

This is the one most developers underestimate, and it directly applies to any developer with any Indian user.

- **Implementation Timeline (2025–2027)**:
  - **Phase I (November 14, 2025)**: The Act and Rules were brought into force, establishing the regulatory foundation and the Data Protection Board (DPB) of India.
  - **Mid-2026 (June – August 2026)**: Focuses on the operationalization of the **Consent Manager ecosystem**. Interoperable platforms for managing user consent are rolled out.
  - **November 2026**: Initial "soft enforcement" or preparatory phase ends, with the Data Protection Board transitioning toward active regulatory supervision.
  - **May 14, 2027 (Hard Compliance Deadline)**: All substantive provisions of the DPDP Act and Rules must be fully implemented. Organizations must ensure complete compliance by this date to avoid significant penalties.
- **Extraterritorial, no threshold**: applies to any entity (anywhere in the world) processing digital personal data of people in India in connection with offering goods/services in India. A solo developer publishing on Play Store is squarely in scope from day one.
- **Core obligations**:
  - Consent must be **free, specific, informed, unconditional, and unambiguous** — affirmative action required, no dark patterns.
  - **Standalone privacy notice** separate from your ToS — must state what's collected, why, and how to withdraw consent (withdrawal must be as easy as giving it).
  - **Children's data**: verifiable parental consent required before processing a child's (under 18) personal data; no targeted advertising directed at children.
  - **Breach notification**: notify the DPBI promptly, then all affected users, with a detailed report to the Board within 72 hours.
  - **Data retention**: erase personal data once the stated purpose is no longer served. Separately, **all data fiduciaries must retain personal data, traffic data, and processing logs for at least 1 year** — a requirement under the 2025 Rules.
  - **Security safeguards**: "reasonable security safeguards" is the statutory phrase — encryption, access control, logging, and breach-detection capability are the practical baseline.
  - **Grievance officer**: every data fiduciary needs a grievance redressal mechanism; large/"Significant Data Fiduciary" status (high-volume apps, fintech, social platforms) adds a DPO requirement — most solo/indie apps won't hit this tier, but still need a grievance contact.
  - **Penalties**: up to ₹250 crore (~$30M) for security-safeguard failures, up to ₹200 crore for consent/children's-data violations — per violation, and they compound across multiple violations.
  - **Cross-border transfer**: permitted by default unless the government publishes a "negative list" of restricted countries — none published as of mid-2026, so using AWS/GCP/Firebase abroad is fine today, but keep the architecture flexible.
  - **Until DPDP is fully enforced**, the older **IT Act 2000 + SPDI Rules 2011** still govern — so don't treat the gap before May 2027 as a free pass.

---

## United States — CCPA/CPRA + 20-state patchwork

- **No general federal privacy law.** Instead, over 20 states have their own comprehensive laws active in 2026: California (CCPA/CPRA), Virginia, Colorado, Connecticut, Utah, Texas, Oregon, Montana, Florida (narrower), Delaware, Iowa, Nebraska, New Hampshire, New Jersey, Minnesota, Maryland, Tennessee, Kentucky, Indiana, Rhode Island, and more.
- **Applicability thresholds matter** — most state laws only kick in once you hit revenue or volume thresholds, e.g.:
  - California (CPRA): generally $25M+ annual revenue, OR buy/sell/share 100k+ consumers'/households' data, OR derive 50%+ revenue from selling personal data.
  - Virginia/Indiana/Kentucky-style: control/process 100k+ state residents' data, or 25k+ residents while deriving 50%+ revenue from selling data.
  - Rhode Island/Maryland: lower thresholds (~35k residents, or 10k if 20%+ revenue from data sales) — easier to trigger.
  - **Practical read for a solo/early-stage app**: you likely fall below most thresholds until you have real scale in a given state. Re-check this as your install base grows — don't assume permanent exemption.
- **Common obligations once a threshold is hit**: privacy notice, opt-out of sale/sharing/targeted ads, sensitive-data opt-in consent, data minimization, right to access/delete/correct/port data, honor **Universal Opt-Out Mechanisms (Global Privacy Control - GPC)** signals.
- **Children/minors**: several 2026 amendments (Connecticut, Arkansas) add age-appropriate-design requirements and restrict selling minors' data — relevant if your app could plausibly attract under-18 users.
- **Health data**: California's separate Consumer Health Data law restricts collection/use/sharing of health-adjacent data and bans geofencing around health facilities — relevant if you build any fitness/health-adjacent feature.
- **Ads**: even below the comprehensive-law thresholds, if you use AdMob you should still pass a CPRA/US-states consent signal — see `ad-monetization.md`. It's nearly free to implement and removes ambiguity as you scale.

---

## Brazil — LGPD

GDPR-equivalent structure: lawful basis for processing, data subject rights (access/correction/deletion/portability), breach notification, fines up to 2% of Brazil revenue (capped per violation). Applies to any app processing data of people in Brazil, regardless of where you're based.

---

## Canada — PIPEDA

Requires meaningful consent, purpose limitation, and breach notification for any organization processing Canadians' personal data in commercial activity. Quebec has its own stricter law (Law 25) layered on top.

---

## European Union — European Accessibility Act (EAA)

- **Status**: Enforceable since **June 28, 2025**. Mobile apps offering commercial services to EU consumers are expected to be in full compliance.
- **Scope**: Private-sector digital services including e-commerce, banking, e-books, and travel booking.
- **Exemptions**: Micro-enterprises with fewer than 10 employees and under €2 million annual turnover are exempt.
- **Technical standard**: Aligned with **EN 301 549**, which relies on **WCAG 2.1 Level AA** compliance. TalkBack screen readers, text scaling without layout breaks, and color contrast must be fully supported.
- **Fines & Enforcement**: EU member state authorities have the mandate to audit apps, request compliance records, and fine non-compliant developers.

---

## Other notable regimes

- **UK**: UK GDPR + Data Protection Act 2018 (near-identical obligations to EU GDPR, separate ICO enforcement).
- **Australia**: Privacy Act 1988 (APPs) — consent, notification, access/correction rights.
- **Singapore**: PDPA — consent-based, similar core obligations.
- **South Korea**: PIPA — among the stricter Asian regimes, includes data localization considerations for some categories.
- **China**: PIPL is a materially different regime (data localization, security assessments, separate consent for cross-border transfer). If you ever distribute through Chinese app stores, treat this as a separate compliance project, not an extension of your global Privacy Policy.

**Source note**: thresholds, phase dates, and fine amounts above reflect public regulator/law-firm reporting as of mid-2026 (DLA Piper, IAPP, Fisher Phillips, Mayer Brown, MultiState, Osano, Ketch). Re-verify against official government sources before relying on a specific number in a dispute.
