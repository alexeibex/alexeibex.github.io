import os
import shutil
import sys

# --- 1. CONFIGURATION PROTOCOLS ---

# Map existing folders to their new disciplined locations
# Format: 'Existing_Name': 'New_Category/New_Name'
MOVE_OPERATIONS = {
    # Law School Notes -> 'notes'
    'ConLaw Lecture Notes': 'notes/ConLaw_Lectures',
    'ConstitutionalChapters': 'notes/Constitutional_Law',
    'ContractsChapters': 'notes/Contracts',
    'FinalStudy': 'notes/Final_Study_Guides',
    'PropertyChapters': 'notes/Property_Law',
    
    # Professional Work -> 'papers'
    'Writing': 'papers/Legal_Writing_Samples',
    'Oral Arguments': 'papers/Oral_Arguments',
    'Appellate Brief.md': 'papers/Appellate_Brief.md',
    'ArgumentSection.md': 'papers/Argument_Section.md',
    'BLIP.html': 'papers/BLIP_Project.html',
    'ConstitutionalChapters|ConLawAttack.html': 'notes/Constitutional_Law/ConLawAttack.html'
}

# Ensure these directories exist
REQUIRED_DIRS = ['notes', 'papers', 'assets/css', '_layouts', '_includes']

# --- 2. THEME GENERATION (The "Cyberpunk" Look) ---

STYLE_SCSS = """---
---
/* * CYBERPUNK_LAWYER_THEME_v1.0 
 * "High Tech. Low Life. High Court."
 */

@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&family=Rajdhani:wght@600;700&display=swap');

$void-black: #050505;
$terminal-green: #00ff41;
$neon-pink: #ff00ff;
$electric-blue: #00f3ff;
$alert-red: #ff2a2a;
$grid-line: #1a1a1a;

body {
    background-color: $void-black;
    background-image: 
        linear-gradient($grid-line 1px, transparent 1px),
        linear-gradient(90deg, $grid-line 1px, transparent 1px);
    background-size: 50px 50px;
    color: $terminal-green;
    font-family: 'JetBrains Mono', monospace;
    margin: 0;
    padding: 20px;
    line-height: 1.5;
    font-size: 14px;
}

/* CRT Scanline Effect */
body::before {
    content: " ";
    display: block;
    position: fixed;
    top: 0; left: 0; bottom: 0; right: 0;
    background: linear-gradient(rgba(18, 16, 16, 0) 50%, rgba(0, 0, 0, 0.25) 50%), linear-gradient(90deg, rgba(255, 0, 0, 0.06), rgba(0, 255, 0, 0.02), rgba(0, 0, 255, 0.06));
    z-index: 2;
    background-size: 100% 2px, 3px 100%;
    pointer-events: none;
}

.container {
    max-width: 900px;
    margin: 40px auto;
    background: rgba(10, 10, 10, 0.95);
    border: 1px solid $terminal-green;
    box-shadow: 0 0 15px rgba(0, 255, 65, 0.15);
    padding: 40px;
    position: relative;
    z-index: 3;
}

/* Typography */
h1, h2, h3 {
    font-family: 'Rajdhani', sans-serif;
    text-transform: uppercase;
    letter-spacing: 2px;
    color: $electric-blue;
    text-shadow: 2px 2px 0px $neon-pink;
    margin-top: 0;
}

h1 { 
    font-size: 2.5rem; 
    border-bottom: 2px solid $terminal-green;
    padding-bottom: 10px;
    margin-bottom: 30px;
}

h2 {
    font-size: 1.5rem;
    color: $terminal-green;
    border-left: 5px solid $neon-pink;
    padding-left: 15px;
    margin-top: 40px;
}

a {
    color: $neon-pink;
    text-decoration: none;
    font-weight: bold;
    transition: all 0.3s;
    
    &:hover {
        background-color: $neon-pink;
        color: $void-black;
        box-shadow: 0 0 10px $neon-pink;
    }
}

/* File Grid System */
.grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
    gap: 20px;
    margin-top: 20px;
}

.card {
    border: 1px solid $grid-line;
    background: rgba(20, 20, 20, 0.8);
    padding: 15px;
    transition: transform 0.2s, border-color 0.2s;
    
    &:hover {
        border-color: $electric-blue;
        transform: translateY(-2px);
    }

    .label {
        display: block;
        font-size: 0.7rem;
        color: #666;
        margin-bottom: 5px;
        text-transform: uppercase;
    }
    
    .title {
        display: block;
        font-size: 1.1rem;
        color: $electric-blue;
    }
}

/* Utilities */
.blink { animation: blinker 1s linear infinite; }
@keyframes blinker { 50% { opacity: 0; } }

footer {
    margin-top: 50px;
    border-top: 1px solid #333;
    padding-top: 20px;
    font-size: 0.8rem;
    color: #555;
}
"""

CONFIG_YML = """title: "AlexeiBex | Cyber_Counsel"
description: "Tech-Focused Legal Portfolio. Organizing the chaos of code and law."
theme: jekyll-theme-prime
plugins:
  - jekyll-seo-tag
"""

INDEX_HTML = """---
layout: default
title: Home
---

<section id="identity">
    <p>
        <span style="color: #666;">> SYSTEM_USER:</span> <strong>AlexeiBex</strong><br>
        <span style="color: #666;">> ROLE:</span> <strong>Tech-Focused Legal Counsel</strong><br>
        <span style="color: #666;">> STATUS:</span> <span style="color: #00ff41;" class="blink">ONLINE</span>
    </p>
    <p class="intro">
        Operating at the intersection of <strong>Cyber Rights</strong>, <strong>IP Law</strong>, and <strong>Future Tech</strong>. 
        This repository serves as a digital vault for my legal arguments, academic papers, and raw data logs.
    </p>
</section>

<section id="papers">
    <h2>// LEGAL_WRITING_MODULES</h2>
    <p>Polished arguments and published works.</p>
    <div class="grid">
        {% for file in site.static_files %}
            {% if file.path contains 'papers/' %}
            <div class="card">
                <span class="label">DOC_TYPE: PAPER</span>
                <a href="{{ file.path }}" class="title">{{ file.name }}</a>
            </div>
            {% endif %}
        {% endfor %}
    </div>
</section>

<section id="notes">
    <h2>// RAW_DATA_LOGS (NOTES)</h2>
    <p>Unfiltered output from legal training and research.</p>
    <div class="grid">
        {% for file in site.static_files %}
            {% if file.path contains 'notes/' %}
                {% unless file.path contains '.DS_Store' %}
                <div class="card">
                    <span class="label">DIR: /NOTES/</span>
                    <a href="{{ file.path }}" class="title">{{ file.name }}</a>
                </div>
                {% endunless %}
            {% endif %}
        {% endfor %}
    </div>
</section>

<section id="contact">
    <h2>// ESTABLISH_UPLINK</h2>
    <p>
        > <a href="https://github.com/alexeibex">GITHUB_PROFILE</a><br>
        > <a href="mailto:your.email@example.com">ENCRYPTED_MAIL_RELAY</a>
    </p>
</section>
"""

LAYOUT_DEFAULT = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ page.title }} | {{ site.title }}</title>
    <link rel="stylesheet" href="/assets/css/style.css">
</head>
<body>
    <div class="container">
        <header>
            <h1>{{ site.title }} <span class="blink">_</span></h1>
        </header>
        <main>
            {{ content }}
        </main>
        <footer>
            <p>> END OF LINE. © 2025 ALEXEIBEX.</p>
        </footer>
    </div>
</body>
</html>
"""

# --- 3. EXECUTION LOGIC ---

def log(msg):
    print(f" [SYSTEM] {msg}")

def main():
    log("INITIATING CYBERPUNK TRANSFORMATION PROTOCOL...")

    # Step 1: Create Directory Structure
    for d in REQUIRED_DIRS:
        if not os.path.exists(d):
            os.makedirs(d)
            log(f"Created directory: {d}")

    # Step 2: Move Files (The Cleanup)
    log("ORGANIZING ARTIFACTS...")
    for src, dest in MOVE_OPERATIONS.items():
        if os.path.exists(src):
            # Check if dest is a directory or file path
            if '.' in os.path.basename(dest): # Treat as file rename
                dest_dir = os.path.dirname(dest)
                if dest_dir and not os.path.exists(dest_dir):
                    os.makedirs(dest_dir)
                shutil.move(src, dest)
                log(f"Moved File: {src} -> {dest}")
            else: # Treat as directory move
                if not os.path.exists(dest):
                    shutil.move(src, dest)
                    log(f"Moved Folder: {src} -> {dest}")
                else:
                    log(f"Skipping {src}: Destination {dest} already exists.")
        else:
            log(f"Target Missing: {src} (Skipping)")

    # Step 3: Generate System Files
    log("WRITING SYSTEM FILES...")
    
    with open('_config.yml', 'w') as f: 
        f.write(CONFIG_YML)
    
    with open('assets/css/style.scss', 'w') as f: 
        f.write(STYLE_SCSS)
        
    with open('_layouts/default.html', 'w') as f: 
        f.write(LAYOUT_DEFAULT)
        
    with open('index.html', 'w') as f: 
        f.write(INDEX_HTML)

    log("PROTOCOL COMPLETE. COMMIT CHANGES TO DEPLOY.")

if __name__ == "__main__":
    main()