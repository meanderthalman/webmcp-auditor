# webmcp-auditor.py
# Copyright (C) 2026 MeanderthalMan
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
#
# For commercial licensing or inquiries, contact: meanderthalman@proton.me

import os, re, json, time, datetime
from flask import Flask, render_template, request, jsonify
import httpcloak
from bs4 import BeautifulSoup
from urllib.parse import urlparse

app = Flask(__name__)

class MCPReadinessEngine:
    def __init__(self, url):
        self.url = url
        self.session = httpcloak.Session(preset="chrome-146-win11")
        self.session.headers.update({
            "User-Agent": "WebMCP-Auditor-Bot/1.0 (Open Source Agentic Audit; MeanderthalMan)"
        })
        
        self.rules = {
            "commerce": ["cart", "checkout", "buy", "product", "sku", "price", "inventory", "shop", "order"],
            "travel": ["flight", "hotel", "book", "stay", "room", "reservation", "destination", "travel", "checkin"],
            "support": ["help", "ticket", "contact", "support", "faq", "chat", "issue", "refund", "return"],
            "creative": ["edit", "design", "canvas", "layer", "addpage", "template", "export", "tool"],
            "finance": ["invoice", "payment", "billing", "statement", "transfer", "tax", "accounting", "pay"],
            "loyalty": ["club", "membership", "points", "rewards", "loyalty", "member", "signin", "login", "profile"]
        }
        self.webmcp_docs = {
            "COMMERCE": "Transaction_Execution_Service",
            "TRAVEL": "Reservation_Agent_Hook",
            "SUPPORT": "Customer_Intelligence_Bridge",
            "FINANCE": "Secure_Settlement_Gateway",
            "LOYALTY": "Member_Equity_Resolver",
            "GENERAL": "Generic_Interaction_Surface"
        }

    def _detect_cms(self, soup):
        html_str = str(soup).lower()
        cms_map = {
            "wp-content": "WordPress / WooCommerce",
            "shopify": "Shopify",
            "adobe-experience-manager": "AEM",
            "etc.clientlibs": "AEM",
            "_next/static": "Next.js / Vercel",
            "drupal": "Drupal",
            "magento": "Magento"
        }
        for key, val in cms_map.items():
            if key in html_str: return val
        return "Custom Enterprise Stack"

    def run_audit(self):
        try:
            response = self.session.get(self.url)
            soup = BeautifulSoup(response.text, 'html.parser')
            cms = self._detect_cms(soup)
            forms = soup.find_all('form')
            domain = urlparse(self.url).netloc.replace('www.', '').upper()
           
            tools = []
            for i, form in enumerate(forms):
                webmcp_name = form.get('toolname')
                inputs = [inp.get('name') or inp.get('id') for inp in form.find_all(['input', 'select', 'textarea'])]
                category = "GENERAL"
                name_attr = webmcp_name or form.get('id') or f"Surface_{i+1}"
               
                context = (str(name_attr) + " " + " ".join(inputs)).lower()
                for cat, keys in self.rules.items():
                    if any(k in context for k in keys):
                        category = cat.upper()
                        break

                is_static = not bool(re.search(r'[0-9a-f]{5,}', str(form.get('id')))) if form.get('id') else False
                has_labels = all(inp.get('aria-label') or inp.get('name') for inp in form.find_all(['input']))
                
                is_ready = webmcp_name and is_static and has_labels
                intel_status = "AGENT-VISIBLE" if is_ready else "AGENT-INVISIBLE"
               
                intel_gap = "None. Tool is natively discoverable."
                if not webmcp_name: intel_gap = f"Identity Gap. System lacks semantic toolname in {cms} layer."
                elif not is_static: intel_gap = "Persistence Gap. Dynamic IDs prevent state-machine reliability."
                elif not has_labels: intel_gap = "Instructional Gap. Field-level intent is ambiguous to LLM parsers."

                tools.append({
                    "name": webmcp_name or self.webmcp_docs[category],
                    "category": category,
                    "intel_status": intel_status,
                    "intel_gap": intel_gap,
                    "agentic_fix": f"Inject WebMCP '{self.webmcp_docs[category]}' via {cms} metadata.",
                    "readiness": (40 if webmcp_name else 0) + (30 if is_static else 0) + (30 if has_labels else 0),
                    "vitals": [
                        {"label": "Semantic Identity", "status": "PASS" if webmcp_name else "FAIL", "weight": "40%"},
                        {"label": "DOM Persistence", "status": "PASS" if is_static else "FAIL", "weight": "30%"},
                        {"label": "Input Clarity", "status": "PASS" if has_labels else "FAIL", "weight": "30%"}
                    ]
                })

            score = sum(t['readiness'] for t in tools)//len(tools) if tools else 0
            return {
                "tools": tools, "cms": cms,
                "insight": {
                    "domain": domain, "score": score,
                    "points": [
                        f"Stack: {cms} integration verified.",
                        f"Sync: {score}% WebMCP Global Protocol Alignment.",
                        f"Risk: {len([t for t in tools if t['intel_status'] == 'AGENT-INVISIBLE'])} Dead-End Surfaces."
                    ]
                }
            }
        except Exception as e: return {"error": str(e)}

@app.route('/')
def index():
    return '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>WebMCP Auditor | Global Agentic Standard</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800&display=swap');
        body { background-color: #f8fafc; font-family: 'Plus Jakarta Sans', sans-serif; color: #0f172a; min-height: 100vh; display: flex; flex-direction: column; }
        .executive-card { position: relative; border: 1px solid #e2e8f0; border-radius: 2rem; background: #fff; transition: all 0.3s; height: 100%; display: flex; flex-direction: column; }
        .executive-card:hover { border-color: #3b82f6; transform: translateY(-2px); box-shadow: 0 10px 30px -10px rgba(0,0,0,0.05); }
        .status-badge { font-size: 8px; font-weight: 900; padding: 4px 12px; border-radius: 100px; text-transform: uppercase; }
        .badge-invisible { background: #fef2f2; color: #dc2626; border: 1px solid #fecaca; }
        .badge-visible { background: #f0fdf4; color: #16a34a; border: 1px solid #bbf7d0; }
        .vitals-overlay { position: absolute; top: 0; left: 0; right: 0; bottom: 0; background: rgba(15, 23, 42, 0.98); border-radius: 2rem; color: white; opacity: 0; pointer-events: none; transition: opacity 0.3s; padding: 2.5rem; z-index: 20; display: flex; flex-direction: column; justify-content: center; }
        .executive-card:hover .vitals-overlay { opacity: 1; pointer-events: auto; }
        .method-box { background: white; border: 1px solid #e2e8f0; border-radius: 2.5rem; padding: 3rem; }
    </style>
</head>
<body class="p-8 lg:p-16">
    <div class="max-w-[1450px] mx-auto flex-grow">
        <header class="flex justify-between items-center mb-16 border-b pb-10 border-slate-200">
            <div>
                <h1 class="text-3xl font-extrabold tracking-tighter text-slate-900 uppercase">WebMCP Auditor</h1>
                <p class="text-slate-400 font-bold text-[10px] uppercase tracking-[0.4em] mt-2">The Global Standard for Agentic Web Interoperability</p>
            </div>
            <div class="flex gap-4">
                <button onclick="location.reload()" class="bg-white border border-slate-200 text-slate-500 px-8 py-3 rounded-full text-[10px] font-bold uppercase tracking-widest hover:bg-slate-50 transition-all">Reset Auditor</button>
            </div>
        </header>

        <div class="max-w-3xl mx-auto mb-20">
            <div class="flex gap-3 p-2 bg-white rounded-2xl border border-slate-200 shadow-xl">
                <input type="text" id="urlInput" placeholder="Enter target URL (e.g. https://example.com)" class="flex-1 px-6 py-2 text-sm font-semibold outline-none text-slate-900 placeholder-slate-300">
                <button onclick="runAudit()" id="scanBtn" class="bg-blue-600 text-white px-10 py-4 rounded-xl text-[10px] font-bold uppercase tracking-widest hover:bg-blue-700 transition-all shadow-lg shadow-blue-200">Execute Scan</button>
            </div>
        </div>

        <div id="results" style="display:none;" class="space-y-12">
            <div class="grid grid-cols-12 gap-8 items-stretch">
                <div class="col-span-12 lg:col-span-8 bg-white border border-slate-200 p-12 rounded-[3rem] flex justify-between items-center">
                    <div class="space-y-6">
                        <p class="text-blue-600 font-bold uppercase tracking-[0.3em] text-[10px]">Strategic Readiness Index</p>
                        <h2 class="text-5xl font-black text-slate-900 uppercase" id="domainTitle">DOMAIN</h2>
                        <div id="insightList" class="space-y-4"></div>
                    </div>
                    <div class="bg-slate-900 h-40 w-40 rounded-full flex flex-col items-center justify-center border-[8px] border-slate-50 shadow-2xl">
                        <span id="scoreVal" class="text-5xl font-black text-white">0</span>
                        <span class="text-[8px] font-bold uppercase tracking-widest text-slate-400 mt-1">Score</span>
                    </div>
                </div>
                <div class="col-span-12 lg:col-span-4 bg-red-50 border border-red-100 p-10 rounded-[3rem]">
                    <h3 class="text-[10px] font-black uppercase tracking-[0.3em] text-red-600 mb-6">Agentic Blind-Spot Analysis</h3>
                    <div class="space-y-4 text-xs font-bold text-red-800 leading-relaxed">
                        <p>• <b>Discovery Failure:</b> Elements without 'toolname' are ignored by Agent registries.</p>
                        <p>• <b>State Fragmentation:</b> Dynamic IDs cause Agents to lose context during multi-step flows.</p>
                        <p>• <b>Decision Latency:</b> Missing ARIA/Metadata forces Agents into costly "Trial & Error" cycles.</p>
                    </div>
                </div>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8" id="toolGrid"></div>
        </div>
    </div>

    <footer class="mt-20 border-t border-slate-200 pt-10 flex flex-col md:flex-row justify-between items-center text-[10px] font-bold uppercase tracking-widest text-slate-400 gap-6">
        <div class="flex items-center gap-4">
            <span>Made with ❤️ by MeanderthalMan | <a href="mailto:meanderthalman@proton.me" class="hover:text-blue-600 transition-colors">Commercial Contact</a></span>
        </div>
        <div class="flex gap-8">
            <a href="https://webmachinelearning.github.io/webmcp/" target="_blank" class="hover:text-blue-600 transition-colors">Documentation</a>
            <a href="https://webmcp.dev/" target="_blank" class="hover:text-blue-600 transition-colors">WebMCP Protocol</a>
            <a href="https://github.com/meanderthalman/webmcp-auditor" target="_blank" class="text-blue-600 underline">Open Source (AGPL v3)</a>
        </div>
    </footer>

    <script>
        async function runAudit() {
            const btn = document.getElementById('scanBtn');
            const urlInput = document.getElementById('urlInput').value;
            if(!urlInput) return alert("Please enter a valid URL.");
            btn.innerText = "ANALYZING...";
            btn.disabled = true;
            try {
                const res = await fetch('/api/audit', { 
                    method: 'POST', 
                    headers: {'Content-Type': 'application/json'}, 
                    body: JSON.stringify({url: urlInput}) 
                });
                const data = await res.json();
                if(data.error) throw new Error(data.error);
                document.getElementById('results').style.display = "block";
                document.getElementById('domainTitle').innerText = data.insight.domain;
                document.getElementById('scoreVal').innerText = data.insight.score;
                document.getElementById('insightList').innerHTML = data.insight.points.map(p => `<p class="text-xl font-bold text-slate-600">▶ ${p}</p>`).join('');
                document.getElementById('toolGrid').innerHTML = data.tools.map(t => `
                    <div class="executive-card p-10">
                        <div class="vitals-overlay">
                            <h5 class="text-[10px] font-black uppercase tracking-widest text-blue-400 mb-8 border-b border-white/10 pb-4">WebMCP Core Vitals</h5>
                            <div class="space-y-5">
                                ${t.vitals.map(v => `
                                    <div class="flex justify-between items-center">
                                        <span class="text-xs font-bold uppercase tracking-tight">${v.label}</span>
                                        <span class="text-[10px] font-black ${v.status === 'PASS' ? 'text-green-400' : 'text-red-400'}">${v.status} (${v.weight})</span>
                                    </div>
                                `).join('')}
                            </div>
                        </div>
                        <div class="flex justify-between items-start mb-8">
                            <span class="text-[9px] font-black text-slate-400 tracking-widest uppercase">${t.category}</span>
                            <span class="status-badge ${t.intel_status === 'AGENT-VISIBLE' ? 'badge-visible' : 'badge-invisible'}">${t.intel_status}</span>
                        </div>
                        <h4 class="text-sm font-black text-slate-900 mb-4 uppercase tracking-tight">${t.name}</h4>
                        <div class="space-y-4">
                            <p class="text-[10px] font-bold text-slate-400 uppercase tracking-widest border-b pb-2">Intelligence Gap</p>
                            <p class="text-[11px] font-bold text-slate-600 leading-relaxed">${t.intel_gap}</p>
                        </div>
                    </div>
                `).join('');
            } catch (err) { alert("Audit failed: " + err.message); }
            finally { btn.innerText = "EXECUTE SCAN"; btn.disabled = false; }
        }
    </script>
</body>
</html>
'''

@app.route('/api/audit', methods=['POST'])
def api_audit():
    return jsonify(MCPReadinessEngine(request.json['url']).run_audit())

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
