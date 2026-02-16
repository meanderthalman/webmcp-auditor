```markdown
# 🤖 webmcp-auditor

**The Global Benchmark for Agentic Web Readiness.** [![License: AGPL v3](https://img.shields.io/badge/License-AGPL_v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Platform: Render](https://img.shields.io/badge/Platform-Render-green.svg)](https://render.com)

`webmcp-auditor` is an open-source diagnostic tool designed to measure how "AI-agent-friendly" a website is. As the web shifts from human-centric browsing to agentic execution, this tool helps developers identify technical gaps that prevent autonomous agents from successfully navigating and interacting with their site.

---

## 🌐 Live Demo
**Try the tool now:** [https://webmcp-auditor.onrender.com](https://webmcp-auditor.onrender.com)  
*(Note: As this is hosted on a free tier, it may take 30-60 seconds to "wake up" on the first load.)*

---

## 🎯 Why This Matters
Traditional SEO and accessibility (ARIA) are no longer enough. AI Agents require **Semantic Identity** and **DOM Persistence** to function without losing context. This tool audits your site against the **WebMCP (Web Machine Learning Protocol)** standards to ensure your business logic is discoverable by autonomous agents.

## 🚀 Key Features
* **Strategic Readiness Index:** A quantitative score (0-100) based on agentic interoperability.
* **Semantic Identity Audit:** Detects missing `toolname` attributes required for agentic discovery.
* **DOM Persistence Check:** Flags dynamic/hashed IDs (CSS-in-JS) that break agentic state-machines.
* **Heuristic Industry Analysis:** Categorizes surfaces into Commerce, Travel, Finance, and more.
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

```

Open your browser to `http://127.0.0.1:5000`.

## 📊 Methodology

The auditor evaluates surfaces based on three technical pillars:

| Pillar | Weight | Description |
| --- | --- | --- |
| **Semantic Identity** | 40% | Is the surface explicitly named for an AI Agent via `toolname`? |
| **DOM Persistence** | 30% | Are IDs static and reliable for multi-step agentic workflows? |
| **Input Clarity** | 30% | Is the intent of every input field unambiguous to an LLM parser? |

## 📜 License & Commercial Inquiries

This project is licensed under the **GNU Affero General Public License v3 (AGPL-3.0)**.

**Commercial Licensing:** If you wish to use this software under terms other than the AGPL v3 (e.g., to incorporate it into a proprietary product without disclosing your source code), please contact me for a commercial license at: **meanderthalman@proton.me**.

---

### 🔗 Official Links

* **Protocol:** [WebMCP.dev](https://webmcp.dev/)
* **Spec:** [W3C WebMCP Documentation](https://webmachinelearning.github.io/webmcp/)

Made with ❤️ by **MeanderthalMan**
