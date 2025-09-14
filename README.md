<h1 align="center">🌍 SWIFT GPI (Global Payments Innovation)</h1>

<p align="center">
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-green.svg"></a>
  <a href="https://github.com/kongali1720/SWIFT-GPI-Tracker/stargazers"><img src="https://img.shields.io/github/stars/kongali1720/SWIFT-GPI-Tracker?style=social"></a>
  <a href="https://github.com/kongali1720/SWIFT-GPI-Tracker/network"><img src="https://img.shields.io/github/forks/kongali1720/SWIFT-GPI-Tracker?style=social"></a>
  <a href="https://github.com/kongali1720/SWIFT-GPI-Tracker/issues"><img src="https://img.shields.io/github/issues/kongali1720/SWIFT-GPI-Tracker"></a>
  <a href="https://github.com/kongali1720/SWIFT-GPI-Tracker/commits"><img src="https://img.shields.io/github/last-commit/kongali1720/SWIFT-GPI-Tracker"></a>
  <a href="https://github.com/kongali1720/SWIFT-GPI-Tracker"><img src="https://img.shields.io/github/languages/top/kongali1720/SWIFT-GPI-Tracker"></a>
</p>

<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/4/40/SWIFT_2023_logo.svg" width="180" alt="SWIFT Logo">
</p>


<p align="center">
  <img src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExYzg4OXJ1NjlrM200YXcwNzVmbmJqeTRuZW15cndpa3ZwdWNtb3RqdiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/5qRIZcO2la5rxa45uj/giphy.gif" width="200" alt="SWIFT Animation">
</p>

---

## 📌 Overview
**SWIFT gpi (Global Payments Innovation)** is an industry standard developed by SWIFT to improve the speed, transparency, and traceability of cross-border payments.  
It enables banks and financial institutions to provide **real-time visibility** on international transactions, ensuring faster settlements and higher customer satisfaction.

💡 *Every bank involved is required to update the transaction status in the SWIFT gpi Tracker. This ensures that both the sender and the beneficiary can monitor the movement of funds in real time.*

---

## 🚀 Key Features
- **Speed**: Same-day or near-instant international payments.  
- **Transparency**: Clear visibility of fees and charges across the payment chain.  
- **Traceability**: End-to-end payment tracking with a unique reference (UETR).  
- **Certainty**: Confirmation when funds are credited to the beneficiary’s account.  

---

## 🔑 Core Components
1. **gpi Tracker**  
   - A centralized cloud-based database maintained by SWIFT.  
   - Tracks transactions end-to-end across multiple banks.  

2. **Unique End-to-End Transaction Reference (UETR)**  
   - A UUID assigned to every transaction, enabling real-time tracking.  

3. **gpi Directory**  
   - A global database of gpi-enabled banks and financial institutions.  

---

## 📊 How It Works
1. The sender initiates a cross-border payment via their bank.  
2. Each intermediary bank updates the payment status in the **SWIFT gpi Tracker**.  
3. The transaction can be monitored in real-time using the **UETR**.  
4. Both the sender and beneficiary are notified once the funds are credited.  

---

## ✅ Benefits for Stakeholders
### For Banks:
- Improved customer experience.  
- Reduced inquiries about payment status.  
- Compliance with global payment standards.  

### For Corporates:
- Faster payments to suppliers.  
- Transparent view of costs and deductions.  
- Improved liquidity management.  

---

## 📖 Example Flow
```mermaid
sequenceDiagram
    participant Sender Bank
    participant Intermediary Bank
    participant Beneficiary Bank
    participant SWIFT gpi Tracker

    Sender Bank->>SWIFT gpi Tracker: Initiates Payment + UETR
    Sender Bank->>Intermediary Bank: Sends Funds
    Intermediary Bank->>SWIFT gpi Tracker: Updates Status
    Intermediary Bank->>Beneficiary Bank: Transfers Funds
    Beneficiary Bank->>SWIFT gpi Tracker: Confirms Credit
    SWIFT gpi Tracker->>Sender Bank: Real-Time Update
    SWIFT gpi Tracker->>Beneficiary: Confirmation Notification
```

### 🏗️ gpi System Architecture
```mermaid
flowchart LR
    A[Corporate Client] --> B[Sending Bank]
    B --> C[SWIFT Network]
    C --> D[gpi Tracker]
    C --> E[Intermediary Banks]
    E --> F[Beneficiary Bank]
    F --> G[End Customer]

    B -->|UETR Assigned| D
    E -->|Update Status| D
    F -->|Confirm Credit| D
```

### 🔄 Transaction Lifecycle
```mermaid
stateDiagram-v2
    [*] --> Initiated: Payment Instruction Sent
    Initiated --> InTransit: Passing Through Intermediary Banks
    InTransit --> Credited: Funds Reached Beneficiary Bank
    Credited --> Confirmed: Status Updated in gpi Tracker
    Confirmed --> [*]
```

### 📊 Traditional SWIFT vs SWIFT gpi

| Feature                 | Traditional SWIFT | SWIFT gpi                |
| ----------------------- | ----------------- | ------------------------ |
| **Speed**               | 2–5 days          | Same-day / near-instant  |
| **Transparency**        | Limited           | Full fee & FX visibility |
| **Traceability**        | No tracking       | End-to-end UETR tracking |
| **Certainty**           | No confirmation   | Confirmation of credit   |
| **Customer Experience** | Low               | High                     |

---


| 🌐 Real-World Use Cases | 📌 Compliance & Standards |
|-------------------------|---------------------------|
| **Corporate Treasury**: Monitoring supplier payments and ensuring funds are received on time. | **ISO 20022** messaging standards |
| **Banks**: Reducing customer inquiries about payment status. | Integrated with **SWIFTNet** for secure communication |
| **Fintechs**: Building value-added services on top of SWIFT gpi data. | Supports transparency & **AML (Anti-Money Laundering)** requirements |
| **Regulators**: Ensuring compliance, transparency, and fraud detection. | Ensures regulatory reporting & global interoperability |

---

---

## 🏦 Additional Insights on SWIFT gpi

### 🌍 Global Adoption
- More than **4,000 banks worldwide** are live with SWIFT gpi.  
- Covers **over 85% of all cross-border payments**.  
- Growing adoption in **emerging markets** to improve financial inclusion.  

### 🔗 Integration with ISO 20022
- SWIFT gpi is fully aligned with **ISO 20022**, the new global standard for financial messaging.  
- Ensures structured, richer, and more accurate payment data.  
- Enhances automation in reconciliation and compliance checks.  

### 📡 Technology & Infrastructure
- Runs on **SWIFTNet**, a secure, private global financial network.  
- **Cloud-based gpi Tracker** enables 24/7 availability and real-time updates.  
- Open APIs allow **fintechs and corporates** to integrate directly into ERP/TMS systems.  

### ⚖️ Compliance & Security
- Designed to meet stringent **AML (Anti-Money Laundering)** and **KYC (Know Your Customer)** regulations.  
- Provides an **audit trail** of every payment event across the transaction chain.  
- Increases transparency, reducing risks of fraud or delays.  

### 🚀 Future of Cross-Border Payments
- SWIFT is extending gpi to support **instant payments** by connecting with domestic real-time payment systems.  
- Moves towards **24/7/365 availability**, eliminating cut-off times.  
- Strengthens collaboration with **CBDCs (Central Bank Digital Currencies)** and digital asset initiatives.  

---

## 📖 Extended Example Flow with Transparency
```mermaid
flowchart TD
    A[Sender Initiates Payment] --> B[Sender Bank]
    B -->|Assigns UETR| C[SWIFT gpi Tracker]
    B --> D[Intermediary Bank]
    D -->|Updates Status| C
    D --> E[Beneficiary Bank]
    E -->|Confirms Credit| C
    C -->|Real-time Update| F[Sender]
    C -->|Confirmation| G[Beneficiary]
```

---

## 🔍 Deep Dive: How SWIFT gpi Works  

SWIFT gpi is not just a faster version of traditional SWIFT messaging. It’s a **paradigm shift** in global payments with these key components:  

1. **Unique End-to-End Transaction Reference (UETR)**  
   - Every payment message carries a unique identifier (UUID-based).  
   - Enables real-time tracking from the sending bank to the receiving bank.  
   - Works like a “parcel tracking number” for international payments.  

2. **SWIFT gpi Tracker**  
   - A centralized database hosted by SWIFT.  
   - All participating banks must update payment status in real time.  
   - Both senders and receivers can query the Tracker to see the payment journey, fees, FX rates, and confirmation of credit.  

3. **Service-Level Agreements (SLAs)**  
   - gpi members commit to same-day settlement for many corridors.  
   - Ensures predictable processing time and customer trust.  
   - Provides measurable accountability across the payment chain.  

4. **Integration with Back-Office Systems**  
   - APIs and ISO 20022 XML messages allow banks and corporates to plug gpi directly into ERPs and treasury systems.  
   - Improves reconciliation, liquidity forecasting, and automation.  

---

## 🌍 Industry Impact  

| Stakeholder          | Benefit from SWIFT gpi                                                                 |
|----------------------|-----------------------------------------------------------------------------------------|
| **Corporates**       | Real-time visibility, better liquidity management, reduced disputes with suppliers.     |
| **Banks**            | Lower operational costs, fewer inquiries, improved customer satisfaction.                |
| **Fintechs**         | Access to real-time payment data to build analytics, dashboards, and new services.      |
| **Regulators**       | Transparent audit trail, better compliance with AML/CTF rules, and cross-border control. |

---

## ⚙️ Technical & Governance Layers  

- **Technology Stack**  
  - Built on **SWIFTNet** with secure FIN and InterAct messaging.  
  - Fully aligned with **ISO 20022** for structured, rich data.  
  - Cloud-enabled API access for corporates and fintechs.  

- **Governance**  
  - Overseen by the SWIFT gpi **Rulebook** and participating banks.  
  - Strict SLA monitoring and performance reporting.  
  - Ensures **global standardization** across 11,000+ institutions.  

---

## 🚀 The Bigger Picture  

- SWIFT gpi is a **step toward instant cross-border payments**.  
- It directly competes with blockchain-based solutions (like Ripple, Stellar) by providing **trust, standardization, and compliance** at a global scale.  
- Adoption has been rapid:  
  - Over **60% of cross-border payments** are now sent via gpi.  
  - Covering more than **150 currencies** and **4,000 financial institutions**.  

---

✅ With SWIFT gpi, the vision of a **“truly global, transparent, and real-time payment ecosystem”** is no longer a future dream — it’s already here.  


## 🛠️ Technical Setup (High-Level)

### Membership & Connectivity
- Bank / institution must be a **SWIFT member**.  
- Needs a **SWIFTNet connection** (via Alliance Lite2, Alliance Access, or cloud connection providers).  
- Obtain **credentials + certificates** from SWIFT.  

### APIs & SDKs
- SWIFT provides **gpi Tracker APIs**.  
- Delivered via **SWIFT Developer Portal** (requires NDA & membership).  
- Exposed as **RESTful APIs** secured with **OAuth2 + PKI certificates**.  

### Integration
- Corporate treasury or bank systems integrate with **ISO 20022 MX messages**.  
- Typically via **back-office integration software** (Temenos, Finastra, FIS, SAP Treasury, etc.).  

---

## ⚙️ Simulation (Open Approach)

Since the real SWIFT gpi network is **closed**, we can **simulate** the environment for learning:

### ISO 20022 Message Simulation
- Create XML messages such as `pacs.008` (Payment Initiation) & `pacs.002` (Status Report).  
- Use **Python/Java + XML libraries** for parsing & validation.  

### Tracking Simulation
- Build a **local database** (Postgres / MySQL) to store transaction statuses.  
- Assign a **UETR (UUID v4)** for each transaction.  
- Update statuses such as `Received`, `Processing`, `Credited`.  
- Expose via **Flask/FastAPI** as a *mock SWIFT gpi Tracker API*.  

---

## 💻 Installation Guide (Mock Tracker)

### 1️⃣ Clone Repository
```bash
git clone https://github.com/kongali1720/SWIFT-GPI.git
cd SWIFT-GPI
```

### 2️⃣ Create Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```bash
pip install fastapi uvicorn pydantic sqlite-utils
```

### ▶️ Run the Mock Tracker
```bash
uvicorn mock_tracker:app --reload
```

Now open in your browser:
👉 http://127.0.0.1:8000/docs

This will give you an interactive API Explorer (Swagger UI) where you can test endpoints in real time. 🚀

### ⚡ Quick Test with cURL

Untuk cek apakah API jalan:
```bash
curl -X GET "http://127.0.0.1:8000/transactions" -H "accept: application/json"
```


---

<h3 align="center" style="color:#39ff14; font-size:1.5rem;">
💡 ☕ Traktir Kopi & Nasi Padang / Nasi Gorengnya ya cuy! 😄
</h3>

<div align="center">

<p style="color:#ffffff; font-size:1.1rem;">
Dukung terus biar semangat bikin karya edukatif lainnya...  
Keep supporting so I stay motivated to create more educational works!
</p>

<a href="https://www.paypal.com/paypalme/bungtempong99" target="_blank" style="text-decoration:none;">
  <img 
    src="https://img.shields.io/badge/Buy%20Me%20a%20Coffee-☕-FF6600?style=for-the-badge&logo=paypal&logoColor=white" 
    alt="Buy Me a Coffee" 
    style="margin-top:10px;"
  />
</a>

<p style="color:#39ff14; font-size:1rem; margin-top:8px;">
Support with ☕ so I can buy 🍜 and keep being 🧠!
</p>

</div>

---

<h2 align="center" style="color:#39ff14;">📫 Let’s Connect together</h2>

<p align="center">
  <a href="https://github.com/kongali1720" target="_blank">
    <img src="https://img.shields.io/badge/GitHub-kongali1720-39ff14?style=for-the-badge&logo=github&logoColor=white" height="35">
  </a>
  <a href="mailto:admin@kongali1720.com">
    <img src="https://img.shields.io/badge/Email-admin@kongali1720.com-DAF7A6?style=for-the-badge&logo=gmail&logoColor=white" height="35">
  </a>
  <a href="https://discord.gg/dXM88zFU" target="_blank">
    <img src="https://img.shields.io/badge/Discord-kongali1720_32854-7289DA?style=for-the-badge&logo=discord&logoColor=white" height="35">
  </a>
  <a href="https://www.instagram.com/kongali1720/" target="_blank">
    <img src="https://img.shields.io/badge/Instagram-kongali-E1306C?style=for-the-badge&logo=instagram&logoColor=white" height="35">
  </a>
</p>

<p align="center">
  <a href="https://x.com/Kongali1720" target="_blank">
    <img src="https://img.shields.io/badge/X-@KongAli50422468-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white" height="35">
  </a>
  <a href="https://younext.cloud" target="_blank">
    <img src="https://img.shields.io/badge/Web-Interactive-younext?style=for-the-badge&logo=web&logoColor=white" height="35">
  </a>
  <a href="https://kongali1720.com" target="_blank">
    <img src="https://img.shields.io/badge/Portfolio-kongali1720-FF69B4?style=for-the-badge&logo=portfolio&logoColor=white" height="35">
  </a>
  <a href="https://wa.me/447440014278" target="_blank">
    <img src="https://img.shields.io/badge/WhatsApp-+44_7440014278-25D366?style=for-the-badge&logo=whatsapp&logoColor=white" height="35">
  </a>
</p>

<h3 align="center" style="color:#ff69b4;">❤️ 💻 INITIATING HUMANITY MODE... for Down Syndrome ❤️</h3>

<div align="center">

<table style="margin: 0 auto; border-collapse: collapse; box-shadow: 0 4px 10px rgba(0,0,0,0.2); border-radius: 8px; overflow: hidden;">
  <thead style="background-color:#ff69b4; color:white;">
    <tr>
      <th style="padding: 12px 25px; font-size: 18px;">Item</th>
      <th style="padding: 12px 25px; font-size: 18px;">Keterangan / Description</th>
    </tr>
  </thead>
  <tbody style="background-color:#1a1a1a; color:#39ff14;">
    <tr>
      <td style="padding: 12px 25px;">🎯 Target</td>
      <td style="padding: 12px 25px;">Anak-anak Pejuang Down Syndrome / Kids with Down Syndrome</td>
    </tr>
    <tr>
      <td style="padding: 12px 25px;">📡 Status</td>
      <td style="padding: 12px 25px;">Butuh Dukungan / Needs Support</td>
    </tr>
    <tr>
      <td style="padding: 12px 25px;">🧠 Response</td>
      <td style="padding: 12px 25px;">Buka Hati + Klik Link = Satu Senyum Baru / Open Heart + Click Link = One New Smile</td>
    </tr>
  </tbody>
</table>

<p align="center" style="margin-top:15px; color:white; font-size:1rem;">
Mereka bukan berbeda — mereka dilahirkan untuk mengajarkan dunia tentang cinta yang murni dan kesabaran yang luar biasa.<br>
They are not different — they were born to teach the world pure love and extraordinary patience.
</p>

<p align="center" style="margin-top: 15px;">
  <a href="https://mydonation4ds.github.io/" target="_blank" style="display: inline-block; text-decoration:none;">
    <img 
      src="https://img.shields.io/badge/SUPPORT--NOW-%23FF6600?style=for-the-badge&logo=heart&logoColor=white&labelColor=FF6600&color=FF4500&logoWidth=15" 
      alt="Support Now" 
      style="height: 40px;"
    />
  </a>
</p>

---

<section align="center" style="font-family: Arial, sans-serif;">

<h2 style="margin-bottom: 15px; color: #0070f3;">💳 Dukungan Pembayaran</h2>

<table align="center" style="margin: 0 auto; border-collapse: collapse; border-radius: 8px; overflow: hidden;">
  <thead style="background-color: #0070f3; color: white;">
    <tr>
      <th style="padding: 10px 20px; font-size: 16px;">Visa</th>
      <th style="padding: 10px 20px; font-size: 16px;">Mastercard</th>
      <th style="padding: 10px 20px; font-size: 16px;">PayPal</th>
    </tr>
  </thead>
  <tbody style="background-color: #f9f9f9;">
    <tr>
      <td style="padding: 10px;">
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/41/Visa_Logo.png/120px-Visa_Logo.png" alt="Visa" width="90" />
      </td>
      <td style="padding: 10px;">
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2a/Mastercard-logo.svg/120px-Mastercard-logo.svg.png" alt="Mastercard" width="90" />
      </td>
      <td style="padding: 10px;">
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/39/PayPal_logo.svg/120px-PayPal_logo.svg.png" alt="PayPal" width="90" />
      </td>
    </tr>
  </tbody>
</table>

</section>

---

<p align="center" style="margin-top: 15px;">
  Kalau project ini bantu kamu, jangan lupa kasih bintang ⭐ dan share ke teman-teman!<br>
  Follow <a href="https://twitter.com/kongali1720" target="_blank">@kongali1720</a> untuk diskusi & update seru 🔥
</p>

<p align="center" style="margin-top: 10px;">
  <a href="https://twitter.com/kongali1720" target="_blank">
    <img src="https://img.shields.io/twitter/follow/kongali1720?style=social" alt="Twitter Follow" />
  </a>
</p>






