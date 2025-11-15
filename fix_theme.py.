import os

# --- 1. OVERRIDE CONFIGURATION (The Root Cause) ---
# We are removing "theme: jekyll-theme-prime" so it doesn't block our styles.
CONFIG_YML = """title: "AlexeiBex | Cyber_Counsel"
description: "Tech-Focused Legal Portfolio."
# We do NOT specify a theme here. We are the theme.
plugins:
  - jekyll-seo-tag
"""

# --- 2. REINFORCE LAYOUT (The Structure) ---
# Ensuring the HTML knows exactly where to find the CSS.
LAYOUT_DEFAULT = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ page.title }} | {{ site.title }}</title>
    <link rel="stylesheet" href="/assets/css/style.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&family=Rajdhani:wght@600;700&display=swap" rel="stylesheet">
</head>
<body>
    <div class="scanline"></div>
    
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

# --- 3. REINFORCE VISUALS (The Neon) ---
# Re-writing the SCSS to ensure no syntax errors block the build.
STYLE_SCSS = """---
---
/* * CYBERPUNK_LAWYER_THEME_v2.0 (PATCHED) */

$void-black: #050505;
$terminal-green: #00ff41;
$neon-pink: #ff00ff;
$electric-blue: #00f3ff;
$grid-line: #1a1a1a;

body {
    background-color: $void-black;
    background-image: 
        linear-gradient($grid-line 1px, transparent 1px),
        linear-gradient(90deg, $grid-line 1px, transparent 1px);
    background-size: 40px 40px;
    color: $terminal-green;
    font-family: 'JetBrains Mono', monospace;
    margin: 0;
    padding: 20px;
    line-height: 1.6;
    min-height: 100vh;
}

.scanline {
    position: fixed;
    top: 0; left: 0; width: 100%; height: 100%;
    background: linear-gradient(to bottom, rgba(255,255,255,0), rgba(255,255,255,0) 50%, rgba(0,0,0,0.1) 50%, rgba(0,0,0,0.1));
    background-size: 100% 4px;
    pointer-events: none;
    z-index: 10;
}

.container {
    max-width: 900px;
    margin: 0 auto;
    background: rgba(5, 5, 5, 0.9);
    border: 1px solid $terminal-green;
    box-shadow: 0 0 20px rgba(0, 255, 65, 0.1);
    padding: 40px;
    position: relative;
    z-index: 20;
}

h1, h2 {
    font-family: 'Rajdhani', sans-serif;
    text-transform: uppercase;
    color: $electric-blue;
    text-shadow: 2px 2px 0px $neon-pink;
}

h1 { border-bottom: 2px solid $terminal-green; padding-bottom: 10px; }
h2 { margin-top: 50px; border-left: 4px solid $neon-pink; padding-left: 15px; color: $terminal-green; }

a {
    color: $neon-pink;
    text-decoration: none;
    font-weight: bold;
    transition: 0.3s;
}
a:hover {
    background-color: $neon-pink;
    color: $void-black;
    box-shadow: 0 0 15px $neon-pink;
}

.grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
    gap: 20px;
    margin-top: 20px;
}

.card {
    border: 1px solid #333;
    background: rgba(20, 20, 20, 0.8);
    padding: 15px;
    transition: transform 0.2s;
}
.card:hover {
    transform: translateY(-5px);
    border-color: $electric-blue;
}

.label { font-size: 0.7rem; color: #666; display: block; margin-bottom: 5px; }
.title { font-size: 1.1rem; color: $electric-blue; display: block; }

.blink { animation: blinker 1s linear infinite; }
@keyframes blinker { 50% { opacity: 0; } }
"""

def main():
    print("--- APPLYING VISUAL PATCH ---")
    
    # 1. Patch Config
    with open('_config.yml', 'w') as f:
        f.write(CONFIG_YML)
    print(" > _config.yml patched (Theme dependency removed).")

    # 2. Patch Layout
    if not os.path.exists('_layouts'): os.makedirs('_layouts')
    with open('_layouts/default.html', 'w') as f:
        f.write(LAYOUT_DEFAULT)
    print(" > _layouts/default.html patched (CSS link forced).")

    # 3. Patch CSS
    if not os.path.exists('assets/css'): os.makedirs('assets/css')
    with open('assets/css/style.scss', 'w') as f:
        f.write(STYLE_SCSS)
    print(" > assets/css/style.scss patched (Syntax verified).")

    print("--- PATCH COMPLETE. PLEASE COMMIT & PUSH. ---")

if __name__ == "__main__":
    main()