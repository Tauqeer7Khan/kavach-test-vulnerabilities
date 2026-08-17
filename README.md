# 🧪 KAVACH Test Repository

> ⚠️ **WARNING:** This repository contains **INTENTIONAL security vulnerabilities** for testing the [KAVACH](https://ai-kavach.vercel.app) AI Security Scanner.
>
> **DO NOT:**
> - Deploy this code to production
> - Use the API keys/secrets shown here (they are fake/example values)
> - Copy this code into any real project
>
> **DO:**
> - Use it to test KAVACH's vulnerability detection
> - Use it to test Auto-Fix functionality
> - Use it to test GitHub PR creation

---

## 📋 Intentional Vulnerabilities Included

This repo contains **8 known vulnerabilities** across 3 files:

### `.env` (5 vulnerabilities)
- 🔴 Hardcoded database password
- 🔴 Hardcoded Stripe live API key
- 🔴 Hardcoded AWS access key + secret
- 🔴 Weak JWT secret
- 🔴 Hardcoded OpenAI API key

### `app.py` (3 vulnerabilities)
- 🔴 SQL Injection via string concatenation
- 🟠 Command Injection via `os.system()`
- 🟡 Weak cryptography (MD5 hashing)

### `config.js` (3 vulnerabilities)
- 🔴 `eval()` on user input (code injection)
- 🟠 Path traversal via unvalidated file paths
- 🟠 Hardcoded API secret in code

---

## 🎯 Expected KAVACH Results

When you scan this repo, you should see:

| Metric | Expected Value |
|--------|----------------|
| Security Score | ~30-40 / 100 |
| Grade | D or F |
| Total Vulnerabilities | 8-12 |
| Critical | 3-5 |
| High | 3-4 |
| Medium | 1-2 |

---

## 🧪 How to Test KAVACH With This Repo

1. Go to https://ai-kavach.vercel.app
2. Click "New Scan" → "GitHub" tab
3. Paste this repo URL
4. Click "Start Scan"
5. Wait ~30-60 seconds for scan to complete
6. Review the vulnerabilities detected
7. **Pro users:** Click "Auto-Fix" to test the fixing engine
8. **Enterprise users:** Click "Create PR" to test PR creation

---

## 🛡️ About KAVACH

KAVACH is an open-source AI code security analyzer that finds vulnerabilities in AI-generated code (ChatGPT, Copilot, Cursor, Bolt.new, v0.dev).

- 🌐 Live: https://ai-kavach.vercel.app
- 💻 GitHub: https://github.com/Tauqeer7Khan/Kavach
- 📧 Built by: [Tauqeer Khan](https://www.linkedin.com/in/tauqeer7khan)

---

## ⚖️ License

MIT — This is a **test repository only**. Do not use for anything real.
