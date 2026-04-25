# AI-Security-SOC-Dashboard-Email-Security-
# 🛠️ How the Project Works (The SOC Lifecycle)

Our system follows a 4-stage process to ensure continuous security monitoring and automated response.

### 1. Data Collection (The Sensors) 📡
We use two primary "eyes" to watch for threats:
* **Microsoft Defender for Office 365:** Monitors incoming emails for phishing links, malicious attachments, and spoofing.
* **Wazuh SIEM:** Monitors our laptops (endpoints). It tracks if a virus is downloaded, if a USB is plugged in, or if unauthorized files are modified.

### 2. The Logic Engine (The Brain) 🧠
A **Python-based engine** acts as the central processor.
* It uses the **Microsoft Graph API** to "fetch" alerts from the cloud.
* It "cleans" the data using the **Pandas** library to remove noise.
* It applies a **Risk Scoring Algorithm** (AI-based):
  * Low Risk (1-30): Normal activity.
  * Medium Risk (31-70): Suspicious login or spam.
  * High Risk (71-100): Confirmed malware or data theft attempt.

### 3. Visualization (The Dashboard) 📊
The security data is displayed on a **Web-Based Dashboard** (React.js).
* **Live Threat Feed:** Shows every alert as it happens.
* **Department Health Score:** A circular gauge showing the overall security status.
* **Top Targets:** Displays which users are being attacked the most.

### 4. Incident Response (The Action) ⚡
When a **High Risk** score is detected:
* **Instant Notification:** A message is sent via **WhatsApp/Telegram API** to the security lead.
* **Automated Playbook:** The dashboard suggests actions like "Reset User Password" or "Isolate Device" to stop the attack immediately.

---

## 📅 Project Roadmap (1 Month)
* **Week 1:** Research & Environment Setup (E5 Sandbox & GitHub).
* **Week 2:** API Integrations & Data Collection.
* **Week 3:** AI Model Development & Dashboard UI.
* **Week 4:** Integration, Testing, and Final Documentation.
