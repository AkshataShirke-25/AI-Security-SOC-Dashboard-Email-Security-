# 🚀 Agent Enrollment Guide

This guide explains how to connect a team member's laptop (Endpoint) to the central SOC Manager hosted by Akshata.

### 1. Prerequisites
* **Operating System:** Windows 10/11 or Linux.
* **Network:** Ensure you are on the same network as the Manager or have VPN access.

### 2. Installation Steps
1. **Download the Agent:** Get the Wazuh Agent installer (MSI for Windows) from the official Wazuh website.
2. **Run Installer:** Follow the setup wizard.
3. **Configure Manager IP:** When prompted for the Manager Address, enter: `192.168.0.101`
4. **Protocol:** Ensure the protocol is set to **TCP** (default).

### 3. Service Verification
* **Windows:** Open 'Services.msc', find **Wazuh**, and click **Start**.
* **Linux:** Run `sudo systemctl start wazuh-agent`.

### 4. Final Handshake
Once the service is running, message the **Project Lead (Akshata)** with your PC name. I will verify your "Active" status in the dashboard to confirm the connection is secure.
