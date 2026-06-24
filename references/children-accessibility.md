# Children's Privacy & Accessibility — Reference

Read this if your app targets children (even partially) or if you distribute your app to EU consumers under the European Accessibility Act (EAA).

---

## Part A: Children's Privacy & Families Policy

Google Play and international laws (COPPA in the US, GDPR in Europe, DPDP in India) enforce extremely strict rules for apps used by children.

### 1. Determining Your Audience (Google Play)
In the Play Console, you must declare your target age group:
- **Children Only**: Only children under 13 (or under 18 depending on region).
- **Mixed Audience**: Appeal to both children and adults. You must implement an **Age Gate** or check the user's age before collecting data or loading personal identifiers.
- **Adults Only**: Under no circumstances should the app appeal to children. If it does, Google will force you to change your target age group or reject your app.

### 2. Strict Child Protections
If children can use your app, you must:
- **Zero Tracking**: Never collect precise location data (`ACCESS_FINE_LOCATION`), Advertising IDs (AAID), or device fingerprints.
- **Self-Certified Ads**: Use ONLY ad networks and SDK versions that are approved for Google Play Families.
- **Age Signals API**: Integrate the Age Signals API to communicate the user's age category (child/adult) dynamically to Firebase and AdMob.
- **No Social Logins**: Do not allow Google Sign-In, Facebook Login, or other social login buttons for child users.
- **Verifiable Parental Consent (VPC)**: Under COPPA, you must obtain verifiable consent from a parent (e.g., verifying a credit card or ID) before collecting any personal data from children under 13.

---

## Part B: Accessibility & EAA Compliance (Enforced Since June 2025)

Under the **European Accessibility Act (EAA)**, active since **June 28, 2025**, commercial mobile applications offered to EU consumers must be accessible. The technical baseline is aligned with **WCAG 2.1 Level AA** standards.

### Android Accessibility Checklist

#### 1. Content Descriptions (Screen Readers)
- Every interactive visual element (buttons, clickable images) must have an accessibility label for TalkBack.
- **Jetpack Compose**:
  ```kotlin
  IconButton(onClick = { /* ... */ }) {
      Icon(
          imageVector = Icons.Default.Delete,
          contentDescription = "Delete account" // Actionable description
      )
  }
  ```
- **Decorative Images**: Set `contentDescription = null` on icons or illustrations that are purely decorative. This prevents TalkBack from reading out useless information.

#### 2. Touch Target Sizes
- All interactive components (buttons, links, text inputs) must be large enough to press easily.
- **The Standard**: Minimum **`48.dp` x `48.dp`** (or `48dp` in XML layouts).
- **Jetpack Compose**: Compose automatically pads clickable elements to 48.dp. Verify custom touch targets using:
  ```kotlin
  Modifier.size(48.dp)
  ```

#### 3. Text & Layout Scaling
- Never hardcode font sizes or layouts in absolute pixels (`px` or `dp` for text).
- **sp for Typography**: Always use scale-independent pixels (`sp`) for text sizes, which respects the system font scaling chosen by the user.
- **Layout Flexibility**: Ensure your layout uses scrollable columns (`LazyColumn` or `VerticalScroll`) so that when the user increases font scale to 200%, text does not clip or overflow off the screen.

#### 4. Color Contrast Ratios
- Ensure text is legible against the background color.
- **Ratios (WCAG 2.1 AA)**:
  - **4.5:1** minimum contrast ratio for body/normal text.
  - **3.0:1** minimum contrast ratio for large text (18pt+ / 24sp+ or bold text).
- **Action**: Use contrast checking tools or the Android Studio Layout Inspector to test color values.
