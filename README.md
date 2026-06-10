# 🔐 Security Log Analyzer

A Python-based cybersecurity project designed to analyze authentication logs, detect failed login attempts, identify potential brute-force attacks, and generate security reports.

---

## 📌 Features

- Detect failed login attempts from authentication logs
- Extract IP addresses involved in failed logins
- Identify possible brute-force attacks based on repeated failed attempts
- Generate automated TXT security reports
- Generate CSV reports for further analysis

---

## 🛠 Technologies Used

- Python
- Regular Expressions (Regex)
- File Handling
- CSV Module
- Git & GitHub

---

## 📂 Project Structure

```text
Security-Log-Analyzer/
│
├── analyzer.py
├── README.md
├── requirements.txt
│
├── logs/
│   └── auth.log
│
├── reports/
│   ├── report.txt
│   └── report.csv
│
└── screenshots/
```

---

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/ishuwari2004/Security-Log-Analyzer.git
```

### 2. Navigate to the project directory

```bash
cd Security-Log-Analyzer
```

### 3. Run the analyzer

```bash
python analyzer.py
```

---

## 📊 Sample Output

```text
Failed Login Summary
----------------------
192.168.1.10 : 3 failed attempts
ALERT! Possible brute-force attack from 192.168.1.10

192.168.1.20 : 1 failed attempts

Report generated successfully!
Location: reports/report.txt

CSV report generated successfully!
Location: reports/report.csv
```

---

## 🛡 Cybersecurity Concepts Demonstrated

- Log Analysis
- Threat Detection
- Failed Login Monitoring
- Brute-force Attack Detection
- Basic SIEM Concepts
- Security Reporting

---

## 🎯 Skills Demonstrated

- Python Programming
- Cybersecurity Fundamentals
- Security Monitoring
- Regex Pattern Matching
- Report Generation
- Git Version Control

---

## 👩‍💻 Author

**Ishuwari**

GitHub: https://github.com/ishuwari2004