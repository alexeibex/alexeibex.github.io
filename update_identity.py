import os

# --- THE NEW HOMEPAGE CONTENT ---
# Updated with "J.D. Graduate" status and LinkedIn integration.

INDEX_HTML = """---
layout: default
title: Home
---

<section id="identity">
    <div style="border-left: 4px solid #00ff41; padding-left: 20px;">
        <h1 style="border: none; margin-bottom: 0;">ALEXEI FURS</h1>
        <p style="margin-top: 0; color: #00f3ff; font-family: 'Rajdhani', sans-serif; font-size: 1.2rem; letter-spacing: 1px;">
            J.D. GRADUATE // LEGAL TECHNOLOGIST // CYBER_COUNSEL
        </p>
    </div>

    <p class="intro">
        <strong>> STATUS:</strong> <span style="color: #ff00ff;">BAR_ADMISSION_PENDING (Or J.D. CONFERRED)</span><br>
        <strong>> ALMA MATER:</strong> Brooklyn Law School<br>
        <strong>> BACKGROUND:</strong> Former President, <a href="https://blslegalhackers.github.io/">BLS Legal Hackers</a>.
    </p>

    <p>
        I operate at the edge of <strong>Digital Rights</strong>, <strong>Blockchain Policy</strong>, and <strong>Algorithmic Accountability</strong>. 
        My work bridges the gap between rigid statutes and fluid code.
    </p>

    <div style="margin: 30px 0; border: 1px solid #ff00ff; padding: 15px; background: rgba(255, 0, 255, 0.05);">
        <h3 style="margin-top: 0; color: #ff00ff;">// PROFESSIONAL_UPLINK</h3>
        <p>
            Connect with my professional network for legal consultation and tech collaboration.
        </p>
        <a href="https://www.linkedin.com/in/alexei-furs-35587773/" target="_blank" style="font-size: 1.2rem;">
            [ ACCESS LINKEDIN PROFILE > ]
        </a>
    </div>
</section>

<section id="future-tech">
    <h2>// SECTOR_01: FUTURE_OF_LAW_RESEARCH</h2>
    <p>Published works and analysis on the decentralized web.</p>
    
    <div class="card" style="border-color: #00f3ff; margin-bottom: 20px;">
        <span class="label" style="color: #00f3ff;">MIT COMPUTATIONAL LAW REPORT</span>
        <a href="https://law.mit.edu/" target="_blank" class="title">Trust in a Trustless System (Co-Author)</a>
        <span class="label" style="margin-top: 5px;">> Analysis of Decentralized Identity & Financial Security</span>
    </div>

    <div class="grid">
        {% for file in site.static_files %}
            {% if file.path contains 'papers/Future_Law_Tech' %}
             <div class="card">
                <span class="label">INTERNAL_DOC</span>
                <a href="{{ file.path }}" class="title">{{ file.name | replace: '.md', '' | replace: '_', ' ' }}</a>
            </div>
            {% endif %}
        {% endfor %}
    </div>
</section>

<section id="core-kernel">
    <h2>// SECTOR_02: THE_LEGAL_ARCHIVE (NOTES)</h2>
    <p>Comprehensive data logs from my J.D. curriculum.</p>
    
    <div class="grid">
        {% if site.data.curriculum.1L_Core_Kernel %}
            {% for item in site.data.curriculum.1L_Core_Kernel %}
            <div class="card">
                <span class="label">KERNEL: FOUNDATION</span>
                <a href="/notes/{{ item[0] }}/" class="title">{{ item[0] | replace: '_', ' ' }}</a>
            </div>
            {% endfor %}
        {% endif %}

        {% if site.data.curriculum.Advanced_Protocols %}
            {% for item in site.data.curriculum.Advanced_Protocols %}
            <div class="card" style="border-color: #666;">
                <span class="label">MODULE: ADVANCED</span>
                <a href="/notes/{{ item[0] }}/" class="title">{{ item[0] | replace: '_', ' ' }}</a>
            </div>
            {% endfor %}
        {% endif %}
    </div>
</section>

<section id="contact">
    <h2>// ENCRYPTED_COMMS</h2>
    <p>
        > <a href="https://github.com/alexeibex">GITHUB_REPO</a><br>
        > <a href="https://www.linkedin.com/in/alexei-furs-35587773/">LINKEDIN_RELAY</a>
    </p>
</section>
"""

def main():
    print("--- INITIATING IDENTITY UPGRADE ---")
    
    # Overwrite the index.html with the new professional data
    with open('index.html', 'w') as f:
        f.write(INDEX_HTML)
        
    print(" > Identity Module Updated: J.D. Status Confirmed.")
    print(" > LinkedIn Uplink Established.")
    print(" > MIT Publication Added to Portfolio.")
    print("--- UPGRADE COMPLETE. COMMIT TO DEPLOY. ---")

if __name__ == "__main__":
    main()