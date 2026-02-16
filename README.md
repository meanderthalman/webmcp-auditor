# 🤖 webmcp-auditor

**The Global Benchmark for Agentic Web Readiness.** [![License: AGPL v3](https://img.shields.io/badge/License-AGPL_v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)



## 🌐 Live Demo
**Try the tool now:** [https://webmcp-auditor.onrender.com](https://webmcp-auditor.onrender.com)  
*(Note: As this is hosted on a free tier, it may take 30-60 seconds to "wake up" on the first load.)*

---

## 🎯 Why This Matters
Traditional SEO and accessibility (ARIA) are no longer enough. AI Agents require **Semantic Identity** and **DOM Persistence** to function without losing context. This tool audits your site against the **WebMCP (Web Machine Learning Protocol)** standards to ensure your business logic is discoverable by autonomous agents.

## 🚀 Key Features
* **Strategic Readiness Index:** A quantitative score (0-100) based on agentic interoperability.
* **Semantic Identity Audit:** Detects missing `toolname` attributes required for agent discovery.
* **DOM Persistence Check:** Flags dynamic/hashed IDs (CSS-in-JS) that break agentic state-machines.
* **One-Click Recommendations:** Provides specific "Agentic Fixes" tailored to your CMS (WordPress, Shopify, Next.js, etc.).

## 🛠️ Installation & Local Run
If you prefer to run the auditor locally:

```bash
# Clone the repo
git clone [https://github.com/meanderthalman/webmcp-auditor.git](https://github.com/meanderthalman/webmcp-auditor.git)
cd webmcp-auditor

# Install dependencies
pip install -r requirements.txt

# Run the app
python webmcp-auditor.py
