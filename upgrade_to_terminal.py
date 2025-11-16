import os

# --- 1. THE TERMINAL JAVASCRIPT ENGINE ---
# Handles the "typing" effect and cursor animation.
TERMINAL_JS = """
document.addEventListener('DOMContentLoaded', function() {
    const terminalContent = document.getElementById('terminal-content');
    const sourceData = document.getElementById('source-data');
    
    // The sequence of "commands" to execute
    const sequence = [
        { text: "> INITIALIZING LEGAL_OS v3.0...", delay: 500, class: "system-msg" },
        { text: "> VERIFYING IDENTITY_TOKENS...", delay: 800, class: "system-msg" },
        { text: "> ACCESS GRANTED: ALEXEI FURS [JD_GRADUATE]", delay: 1200, class: "success-msg" },
        { text: "> EXECUTE identity.py --verbose", delay: 1500, class: "command" },
        { text: "  ... Loading Professional Profile", delay: 1800, class: "output" },
        { text: "  ... Linking Google DeepMind Credentials", delay: 2000, class: "output" },
        { text: "  ... Mounting NYS Bar Admission", delay: 2200, class: "output" },
        { text: "> DONE.", delay: 2500, class: "success-msg" }
    ];

    let currentIndex = 0;

    function typeLine(lineObj, callback) {
        const line = document.createElement('div');
        line.className = 'terminal-line ' + lineObj.class;
        terminalContent.appendChild(line);

        let charIndex = 0;
        const typeInterval = setInterval(() => {
            if (charIndex < lineObj.text.length) {
                line.textContent += lineObj.text.charAt(charIndex);
                charIndex++;
                window.scrollTo(0, document.body.scrollHeight);
            } else {
                clearInterval(typeInterval);
                if (callback) callback();
            }
        }, 30); // Speed of typing (lower is faster)
    }

    function runSequence() {
        if (currentIndex < sequence.length) {
            const step = sequence[currentIndex];
            setTimeout(() => {
                typeLine(step, runSequence);
                currentIndex++;
            }, 300);
        } else {
            // Sequence complete, reveal the main GUI
            document.getElementById('main-gui').classList.add('visible');
            document.querySelector('.cursor-line').style.display = 'block';
        }
    }

    // Start the boot sequence
    runSequence();
});
"""

# --- 2. THE TERMINAL STYLES (CSS) ---
# Monospaced, Black Background, Neon Text.
STYLE_SCSS = """---
---
/* TERMINAL AESTHETIC PROTOCOL */
@import url('https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;700&display=swap');

$bg-color: #0a0a0a;
$text-main: #00ff41; /* Classic Terminal Green */
$text-command: #00f3ff; /* Cyan for commands */
$text-system: #ff00ff; /* Pink for system alerts */
$text-dim: #666;

body {
    background-color: $bg-color;
    color: $text-main;
    font-family: 'Fira Code', monospace;
    margin: 0;
    padding: 20px;
    font-size: 14px;
    line-height: 1.5;
    overflow-x: hidden;
}

/* The Typing Container */
#terminal-content {
    margin-bottom: 20px;
}

.terminal-line {
    min-height: 20px;
    margin-bottom: 5px;
    white-space: pre-wrap;
}

.system-msg { color: $text-dim; }
.command { color: $text-command; font-weight: bold; }
.success-msg { color: $text-main; }
.output { color: #ccc; margin-left: 20px; }

/* The Main GUI (Hidden until boot finishes) */
#main-gui {
    opacity: 0;
    transition: opacity 1s ease-in;
}
#main-gui.visible {
    opacity: 1;
}

/* Links inside the terminal */
a {
    color: $text-system;
    text-decoration: none;
    border-bottom: 1px dashed $text-system;
    transition: all 0.2s;
    
    &:hover {
        background-color: $text-system;
        color: $bg-color;
        box-shadow: 0 0 10px $text-system;
    }
}

/* Grid Layout for Files */
.grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
    gap: 15px;
    margin-top: 15px;
    margin-bottom: 30px;
}

.file-card {
    border: 1px solid #333;
    padding: 10px;
    background: rgba(255,255,255,0.02);
    
    &:hover {
        border-color: $text-command;
        background: rgba(0, 243, 255, 0.05);
    }
}

.label {
    font-size: 0.7em;
    color: $text-dim;
    display: block;
    margin-bottom: 5px;
}

/* Blinking Cursor */
.cursor-block {
    display: inline-block;
    width: 10px;
    height: 18px;
    background-color: $text-main;
    animation: blink 1s step-end infinite;
    vertical-align: middle;
}

@keyframes blink {
    0%, 100% { opacity: 1; }
    50% { opacity: 0; }
}

h1, h2 {
    border-bottom: 1px solid #333;
    padding-bottom: 5px;
    color: $text-command;
    font-size: 1.2rem;
    margin-top: 40px;
}
"""

# --- 3. THE HTML STRUCTURE ---
# Formatted as a command-line interface.
INDEX_HTML = """---
layout: null
---
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>alexei@legal-system:~</title>
    <link rel="stylesheet" href="/assets/css/style.css">
    <script src="/assets/js/terminal.js"></script>
</head>
<body>

    <div id="terminal-content"></div>

    <div class="cursor-line" style="display:none;">
        <span style="color: #00f3ff;">alexei@legal-system:~$</span>
        <span class="cursor-block"></span>
    </div>

    <div id="main-gui">
        
        <div class="output-block">
            <p>> CURRENT_STATUS: <span style="color: #ff00ff;">ONLINE</span></p>
            <p>
                I am a <strong>Senior Privacy Engineer</strong> at <strong>Google DeepMind</strong> and an <strong>Admitted Attorney (NYS)</strong>.<br>
                My work ensures that AI Agents and Large Language Models adhere to privacy laws and ethical standards.<br>
                Previously: Google (Search/Assistant), Twitter, BetterCloud.
            </p>
            <p>
                > <a href="/assets/Alexei_Furs_Resume.pdf" target="_blank">[ DOWNLOAD_RESUME.PDF ]</a><br>
                > <a href="https://www.linkedin.com/in/alexei-furs-35587773/" target="_blank">[ CONNECT_LINKEDIN_RELAY ]</a>
            </p>
        </div>

        <h2>// DIR: /RESEARCH_PAPERS/</h2>
        <div class="grid">
            <div class="file-card">
                <span class="label">r--r--r-- MIT_CLR.pdf</span>
                <a href="https://law.mit.edu/pub/trustinatrustlesssystem" target="_blank">Trust in a Trustless System</a>
            </div>
            {% for file in site.static_files %}
                {% if file.path contains 'papers/Future_Law_Tech' %}
                <div class="file-card">
                    <span class="label">r--r--r-- LOCAL_FILE</span>
                    <a href="{{ file.path }}">{{ file.name }}</a>
                </div>
                {% endif %}
            {% endfor %}
        </div>

        <h2>// DIR: /LEGAL_ARCHIVE/ (NOTES)</h2>
        <div class="grid">
            {% if site.data.curriculum.1L_Core_Kernel %}
                {% for item in site.data.curriculum.1L_Core_Kernel %}
                <div class="file-card">
                    <span class="label">d--x--x-- MODULE</span>
                    <a href="/notes/{{ item[0] }}/">{{ item[0] }}</a>
                </div>
                {% endfor %}
            {% endif %}

            {% if site.data.curriculum.Advanced_Protocols %}
                {% for item in site.data.curriculum.Advanced_Protocols %}
                <div class="file-card">
                    <span class="label">d--x--x-- MODULE</span>
                    <a href="/notes/{{ item[0] }}/">{{ item[0] }}</a>
                </div>
                {% endfor %}
            {% endif %}
        </div>

        <footer>
            <br>
            <p style="color: #444;">> SYSTEM_IDLE. WAITING FOR INPUT...</p>
        </footer>
    </div>

</body>
</html>
"""

def main():
    print("--- INSTALLING TERMINAL UI V3.0 ---")
    
    # Ensure directories exist
    os.makedirs('assets/js', exist_ok=True)
    os.makedirs('assets/css', exist_ok=True)
    
    # Write JS
    with open('assets/js/terminal.js', 'w') as f:
        f.write(TERMINAL_JS)
    print(" > Terminal Engine (JS) Installed.")

    # Write CSS
    with open('assets/css/style.scss', 'w') as f:
        f.write(STYLE_SCSS)
    print(" > Visual Protocol (SCSS) Updated.")

    # Write HTML
    with open('index.html', 'w') as f:
        f.write(INDEX_HTML)
    print(" > Interface (HTML) Rewritten.")
    
    print("--- UPGRADE COMPLETE. DEPLOY TO GO LIVE. ---")

if __name__ == "__main__":
    main()