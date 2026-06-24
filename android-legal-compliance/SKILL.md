---
name: android-legal-compliance
description: Use this skill for ANY Android (or cross-platform mobile) app project — when building a new app, adding a permission/SDK/ad network, writing a Privacy Policy or Terms of Service, filling Google Play's Data Safety form, integrating AdMob/analytics, before every Play Console submission, or whenever the user asks if their app is "legal", "compliant", "safe to publish", or mentions GDPR, CCPA, DPDP, COPPA, privacy policy, account deletion, or data safety. Trigger this proactively even if the user only describes app features — every app that collects any data, shows ads, or lets users sign up has compliance obligations the moment it is uploaded to a store. Covers global privacy law (GDPR, CCPA/US states, India's DPDP Act, LGPD, PIPEDA), Google Play Developer Program Policy, Apple App Store rules, AdMob/ad-consent requirements, children's privacy, accessibility law, and security baselines.
---

# Android App Legal & Compliance Skill

Engineering-facing compliance reference for indie/solo Android developers. Goal: ship apps that won't get rejected, fined, or banned — globally, not just in one country. This is **not legal advice** (see Disclaimer at the bottom) — it is a practical, current (2026) checklist built from public regulator and platform documentation, written so an AI coding agent can act on it directly.

## How to use this skill

1. **Auto-Install Guardrails** — Run `python scripts/install.py <project_path>` to copy `.cursorrules` and the compliance scanner to the project root.
2. **Data Inventory** — Answer the questions in Step 1 below for the specific app.
3. **Decision Tree** — Step 2 tells you which legal regimes actually apply to this app.
4. **Universal baseline & Scanner** — Step 3 applies to every app, no exceptions. Run the scanner `python scripts/audit.py <project_path>` to automatically detect issues.
5. **Conditional modules** — Step 4 points to `references/*.md` for whichever regimes triggered.
6. **Before every Play Console submission** — Run `references/prelaunch-audit-checklist.md` top to bottom.
7. **Generate documents** — Ask the AI to write a Privacy Policy or Terms of Service dynamically (using `/privacypolicy` or `/terms` commands).

Don't just summarize this file back to the user — apply it: draft the actual Privacy Policy text, fill the actual Data Safety form answers, write the actual `network_security_config.xml`, flag the actual permission that needs a Contact Picker swap, etc.

---

## Step 1 — Data Inventory (always do this first)

For the app being built/audited, determine:

- **Permissions/data sources used**: camera, photos/media, precise or coarse location, contacts, SMS, microphone, body sensors / health & fitness (incl. ML Kit pose/face detection output), call logs, files, Bluetooth/nearby devices.
- **Identifiers collected**: Advertising ID (AAID), Android ID, App Set ID, IP address, device fingerprint.
- **Accounts**: does the app let users create an account (email, Google Sign-In, phone)?
- **Third-party SDKs**: AdMob/mediation, Firebase (Analytics, Crashlytics, Auth, Firestore), ML Kit, any analytics SDK. Each one collects data on your behalf — you are responsible for declaring what *they* collect too.
- **Monetization**: ads (which network/mediation), in-app purchases/subscriptions, no monetization.
- **Audience**: could children under 13 (US) / under 18 (India, EU minors codes) realistically use or be drawn to this app, even if not the primary target?
- **Distribution**: Google Play only, or also Apple App Store / other stores? Which countries (Play Store defaults to ~global distribution unless you restrict countries in Console)?

This inventory drives every decision below. Re-run it whenever a new permission, SDK, or feature is added — that's the #1 way apps drift out of compliance after launch.

---

## Step 2 — Decision Tree: which regimes apply

| If... | Then this applies | Reference |
|---|---|---|
| You publish on Google Play at all | **Google Play Developer Program Policy** — non-negotiable, applies regardless of where your users are | `references/play-store-policy.md` |
| App collects *any* personal data, from *any* user, anywhere | Treat GDPR-grade discipline (consent, minimization, deletion rights) as your **default baseline** — it's the strictest major regime and Play/Apple already require a global privacy policy | `references/global-privacy-laws.md` |
| You have EEA/UK/Switzerland users | GDPR + UK GDPR + Swiss FADP + ePrivacy (cookie/local-storage consent). If you show ads, **Google-certified CMP (UMP SDK) is mandatory**, not optional | `references/global-privacy-laws.md`, `references/ad-monetization.md` |
| You have Indian users (you almost certainly do) | IT Act 2000 + SPDI Rules apply now; DPDP Act 2023 + DPDP Rules 2025 are phasing in through May 2027 and apply **extraterritorially with no minimum-user threshold** — one Indian user is enough | `references/global-privacy-laws.md` |
| You have US users at meaningful scale (~100k+ in a given state, or selling data) | CCPA/CPRA + ~20 state privacy laws (thresholds usually exempt small/early apps — verify per state) | `references/global-privacy-laws.md` |
| You have Brazilian / Canadian users | LGPD / PIPEDA | `references/global-privacy-laws.md` |
| Children could plausibly use the app, or it could appeal to them | COPPA (US) + Google Play Families Policy + child-specific state/EU codes — this is the **strictest path**, follow it even if children aren't your primary audience | `references/children-accessibility.md` |
| You use AdMob or any ad network | UMP SDK (EEA/UK/CH), RDP/GPP signal (US states), TFUA tag if mixed/child audience | `references/ad-monetization.md` |
| You serve EU consumers | European Accessibility Act — WCAG 2.1 AA / EN 301 549 is the technical bar. Solo devs/micro-enterprises (<10 employees, <€2M turnover) are currently **exempt**, but build accessible by default since exemption ends the moment you scale | `references/children-accessibility.md` |
| You also (or will) ship on Apple App Store | App Privacy "Nutrition Label" + App Tracking Transparency if you do any cross-app tracking | `references/app-store-policy.md` |

---

## Step 3 — Universal non-negotiables (every app, every country)

These apply even to a single-developer app with 10 downloads:

1. **Privacy Policy** — public URL, entered in Play Console *and* visible inside the app. Must name the actual developer/entity exactly as it appears on the Play Console listing, list every data type collected/shared and why, describe retention & deletion, and give a contact mechanism. This is required by **Google Play policy itself**, independent of any data-protection law.
2. **Data Safety form** (Play Console → App content → Data safety) — must match what the binary *actually* does, including what your SDKs do. Google auto-scans your APK/AAB and flags undeclared data access before human review. "Collected" = transmitted off-device and accessible for longer than needed to serve the request in real time. "Shared" = any third party gets it, including an SDK vendor using it for their own purposes (ad targeting, benchmarking).
3. **Account deletion** — if the app supports account creation, you need (a) an in-app deletion path AND (b) a working web link, both submitted in Play Console, before the app goes live. Deactivation/freezing does not count as deletion.
4. **Permissions hygiene** — request only what the feature needs. Sensitive permissions (location, contacts, SMS, camera, mic, health) need a clear runtime rationale. As of April 2026, broad **Contacts** access requires using the Android Contact Picker unless you can justify full access.
5. **Target API level** — new apps/updates must target within 1 year of the latest major Android release (Android 16 / API 36 from Aug 31 2026); existing apps must stay within 2 years or lose visibility to new users on newer devices. Check the current number at submission time — it moves every year.
6. **Security baseline** — HTTPS-only (Network Security Config blocks cleartext by default on API 28+), no secrets/API keys committed to a public repo, encrypt sensitive local data, don't log PII. Full detail: `references/security-baseline.md`.

---

## Step 4 — Conditional modules

Read the matching file only when Step 2 flagged it relevant:

- `references/global-privacy-laws.md` — GDPR, CCPA/CPRA + 20-state US patchwork, India DPDP Act/Rules, LGPD, PIPEDA, and the cross-regime universal rights table.
- `references/play-store-policy.md` — Data Safety form mechanics, account deletion, permissions policy, Families Policy badge, target API level, ads policy, SDK Index, developer verification.
- `references/app-store-policy.md` — Apple Privacy Nutrition Label, App Tracking Transparency, 2026 App Review focus areas (AI disclosure, pricing transparency).
- `references/ad-monetization.md` — AdMob UMP SDK setup, GDPR/CCPA/US-state consent signals, TFUA for children, mediation partner consent pass-through.
- `references/children-accessibility.md` — COPPA 2025 amendments, Play Families Policy, Age Signals API rules, age-appropriate design codes, European Accessibility Act + practical Android accessibility checklist.
- `references/security-baseline.md` — secrets management, encrypted storage, network security config, logging hygiene, dependency/SDK hygiene.
- `references/legal-documents.md` — dynamic AI-generation instructions for Privacy Policy and Terms of Service.
- `references/prelaunch-audit-checklist.md` — the final linear checklist to run before hitting "submit for review."

---

## Output checklist (what using this skill should produce)

- [ ] Data inventory documented for this app/version
- [ ] List of applicable jurisdictions/regimes generated from Step 2
- [ ] Automated compliance scan run using `scripts/audit.py`
- [ ] `.cursorrules` placed in project root for automated AI guardrails
- [ ] Privacy Policy dynamically generated and hosted at a stable URL
- [ ] Data Safety form answers drafted, matching the actual binary
- [ ] Account deletion flow (in-app + web) implemented if accounts exist
- [ ] AdMob/UMP consent flow implemented if ads are used
- [ ] Children's-data path applied if relevant
- [ ] Security baseline checked (HTTPS, no leaked secrets, encrypted storage)
- [ ] Accessibility basics checked (contentDescription, contrast, touch targets)
- [ ] Final pre-submission audit run

---

## Disclaimer

This skill compiles publicly available regulator and platform documentation as of mid-2026 into an actionable engineering checklist. It is **not legal advice**, and laws/thresholds/deadlines change — re-verify dates and numeric thresholds against the official source (linked in each reference file) before relying on them in a real dispute or regulatory inquiry. For anything high-stakes — handling health/biometric data at scale, facing a regulator notice, drafting a contract, or expanding into a new country's payments/fintech rules — consult an actual lawyer in that jurisdiction.
