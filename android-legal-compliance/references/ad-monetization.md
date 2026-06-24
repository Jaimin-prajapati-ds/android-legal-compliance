# Ad Monetization Consent — Reference

Read this if you show ads (AdMob, AppLovin, Unity Ads, ironSource, etc.) in your app. Third-party ad networks collect user identifiers for tracking, which triggers strict legal consent requirements.

---

## 1. Mandatory CMP (User Messaging Platform SDK)

Under EEA (European Economic Area), UK, and Swiss regulations, you must collect certified user consent before showing personalized or non-personalized ads.
- **The Mandate**: Google requires all publishers serving users in the EEA, UK, or Switzerland to use a **Google-certified Consent Management Platform (CMP)**. 
- **The SDK**: Integrate Google's **User Messaging Platform (UMP) SDK** (part of the Google Mobile Ads SDK).
- **Consent Collection Flow**:
  1. Initialize the UMP SDK on app startup.
  2. Request consent information from the server (`UserMessagingPlatform.requestConsentInfoUpdate`).
  3. If consent is required, load and show the consent form (`UserMessagingPlatform.loadAndShowConsentFormIfRequired`).
  4. Only initialize the Mobile Ads SDK and request ads *after* the consent flow has completed.
- **Consequences**: If you do not use a certified CMP, Google will serve zero ads (100% fill rate drop) to EEA/UK/CH users, and your account may be flagged for policy violations.

---

## 2. US State Consent Signals (CCPA/CPRA & GPP)

To comply with California's CCPA/CPRA and the ~20 other active state privacy laws:
- **Restricted Data Processing (RDP)**: You must signal to your ad network if a user has opted out of the sale or sharing of their personal data.
- **Global Privacy Platform (GPP)**: Modern ad networks support GPP—a unified protocol to transmit privacy signals. Ensure your CMP or ad network SDK is configured to parse and forward GPP signals automatically.
- **AdMob Action**: Enable Restricted Data Processing in the AdMob console for US states, or handle it in code for users who toggle their privacy choices.

---

## 3. Children's Privacy Tags (COPPA & Play Families Policy)

If your app is directed to children (under 13 in the US, under 18 in India/EU):
- **Ad Customization**: You must set specific flags in your ad request config to tell the ad network that the user is a child.
- **AdMob Code Snippet**:
  ```java
  RequestConfiguration requestConfiguration = MobileAds.getRequestConfiguration()
      .toBuilder()
      // COPPA: Tag for child-directed treatment (true = directed to children)
      .setTagForChildDirectedTreatment(RequestConfiguration.TAG_FOR_CHILD_DIRECTED_TREATMENT_TRUE)
      // GDPR: Tag for users under the age of consent (true = under age)
      .setTagForUnderAgeOfConsent(RequestConfiguration.TAG_FOR_UNDER_AGE_OF_CONSENT_TRUE)
      // Limit ad content rating
      .setMaxAdContentRating(RequestConfiguration.MAX_AD_CONTENT_RATING_G)
      .build();
  MobileAds.setRequestConfiguration(requestConfiguration);
  ```
- **Prohibitions**: Never request targeted/personalized ads for children. The ad network must only serve contextual ads.

---

## 4. Mediation Partner Consent Pass-Through

If you use AdMob Mediation (or AppLovin MAX) to serve ads from other networks (e.g., Unity Ads, Liftoff, Meta):
- **Consent Propagation**: The mediation SDK must pass the CMP consent strings (TCF v2.2 strings) to all mediated networks automatically.
- **Verification**: Ensure your mediation adapter versions are up to date. Outdated adapters will fail to forward consent strings, causing ad loading failures and compliance compliance violations on mediated networks.
