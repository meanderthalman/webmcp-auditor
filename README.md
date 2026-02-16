# 🤖 webmcp-auditor

**The Global Benchmark for Agentic Web Readiness.** `webmcp-auditor` is an open-source diagnostic tool designed to measure how "AI-agent-friendly" a website is. As the web shifts from human-centric browsing to agentic execution, this tool helps developers identify technical gaps that prevent autonomous agents (like Claude Operator or OpenAI Operator) from successfully navigating and interacting with their site.



## 🎯 Why This Matters
Traditional SEO and accessibility (ARIA) are no longer enough. AI Agents require **Semantic Identity** and **DOM Persistence** to function without "hallucinating" or losing context. This tool audits your site against the **WebMCP (Web Machine Learning Protocol)** standards to ensure your business logic is discoverable by the next generation of agents.

## 🚀 Key Features
* **Strategic Readiness Index:** A quantitative score (0-100) based on agentic interoperability.
* **Semantic Identity Audit:** Detects missing `toolname` attributes required for agentic discovery.
* **DOM Persistence Check:** Flags dynamic/hashed IDs (CSS-in-JS) that break agentic state-machines.
* **Heuristic Industry Analysis:** Categorizes surfaces into Commerce, Travel, Finance, and more.
* **One-Click Recommendations:** Provides specific "Agentic Fixes" tailored to your CMS (WordPress, Shopify, Next.js, etc.).

## 🛠️ Quick Start

### 1. Installation
Ensure you are in your Python virtual environment:
```bash
pip install flask httpcloak beautifulsoup4
