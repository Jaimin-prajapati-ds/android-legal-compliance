# Apple App Store Policy — Reference

Read this if you publish your app on iOS (e.g., using Flutter, React Native, or Unity) alongside Android. Apple enforces a separate set of privacy and security mandates that are reviewed by manual reviewers.

---

## 1. Apple Privacy Manifests (Fully Enforced)

Apple requires developers and third-party SDKs to declare their privacy practices programmatically.
- **The Mandate**: If your app uses specific third-party SDKs (such as Firebase, analytics, or ads), those SDKs must contain a **Privacy Manifest** (`PrivacyInfo.xcprivacy`) detailing the data they collect and the reasons for doing so.
- **Required Signatures**: High-risk third-party SDKs must be **digitally signed** by their developer. Apps containing unsigned or unapproved versions of these SDKs will be rejected during upload to App Store Connect.
- **Action**: Keep all iOS dependencies updated to versions that support Apple's digital signatures and privacy manifests.

---

## 2. App Tracking Transparency (ATT) Framework

Apple requires explicit user consent before tracking users across apps and websites.
- **Tracking Definition**: Sharing user data (like device identifier IDFA, email, or IP address) with third-party ad networks or brokers for targeted advertising or measurement.
- **The Prompt**: You must show the native ATT prompt (`AppTrackingTransparency` framework) and receive permission before fetching the IDFA.
- **EEA Exception**: Under GDPR, the ATT prompt alone does not constitute valid legal consent. You must integrate a certified Consent Management Platform (CMP) to collect GDPR-compliant consent before showing the ATT prompt.
- **Consequences**: If the user selects "Ask App not to Track", you must not read the IDFA or perform any cross-app tracking.

---

## 3. App Privacy "Nutrition" Labels

Developers must manually disclose their data practices in App Store Connect.
- **Accuracy**: Your disclosures in the App Store Connect questionnaire must match what your app (and your SDKs) actually do. Apple automatically scans uploaded binaries for tracking API calls and flags undeclared data collection.
- **Account Deletion Link**: If you collect user accounts, you must provide a way to delete the account and all associated personal data from within the app and via a web portal.

---

## 4. 2026/2027 App Review Focus Areas

Apple Reviewers are strictly auditing the following categories:
- **Generative AI Features**: If your app includes AI text/image generation, you must:
  - Implement strict content filtering and safety moderations to prevent illegal or harmful outputs.
  - Provide a clear report/block mechanism for user-generated AI content.
  - Set an appropriate age rating (typically 12+ or 17+ depending on the content risk).
- **Subscription Transparency**: Clear pricing disclosures before prompting for In-App Purchases. You must clearly state the billing cycle, renewal price, and cancellation mechanism.
