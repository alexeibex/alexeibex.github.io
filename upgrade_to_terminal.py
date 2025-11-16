import os

# --- 1. THE TERMINAL JAVASCRIPT ENGINE ---
# Handles boot sequence AND interactive commands.
TERMINAL_JS = """
document.addEventListener('DOMContentLoaded', function() {
    const terminalContent = document.getElementById('terminal-content');
    const mainGui = document.getElementById('main-gui');
    const inputLine = document.getElementById('input-line');
    const cmdInput = document.getElementById('cmd-input');
    const history = document.getElementById('history');

    // --- KNOWLEDGE BASE ---
    const db = {
        "who": "IDENTITY: Alexei Furs | Senior Privacy Engineer @ Google DeepMind | Admitted Attorney (NYS).",
        "about": "BIO: Operating at the intersection of Law & Code. Focused on AI Governance, Privacy Engineering, and Digital Rights.",
        "resume": "ACCESSING FILE... <a href='/assets/Alexei_Furs_Resume.pdf' target='_blank'>[ DOWNLOAD_RESUME.PDF ]</a>",
        "contact": "UPLINK ESTABLISHED: <a href='https://www.linkedin.com/in/alexei-furs-35587773/' target='_blank'>[ LINKEDIN_PROFILE ]</a>",
        "github": "REPO SOURCE: <a href='https://github.com/alexeibex' target='_blank'>github.com/alexeibex</a>",
        "papers": "INDEXING RESEARCH... See the <a href='#research-papers'>Research Module</a> above for full text.",
        "notes": "ACCESSING ARCHIVE... Law school notes are available in the <a href='#legal-archive'>Archive Module</a> above.",
        "help": "AVAILABLE COMMANDS: who, about, resume, contact, papers, notes, clear, exit."
    };

    // --- BOOT SEQUENCE ---
    const sequence = [
        { text: "> INITIALIZING LEGAL_OS v3.1...", delay: 300, class: "system-msg" },
        { text: "> VERIFYING ENCRYPTION KEYS...", delay: 600, class: "system-msg" },
        { text: "> ACCESS GRANTED: ALEXEI FURS [JD_GRADUATE]", delay: 1000, class: "success-msg" },
        { text: "> EXECUTE identity.py --verbose", delay: 1400, class: "command" },
        { text: "  ... Loading Professional Profile", delay: 1700, class: "output" },
        { text: "  ... Linking Google DeepMind Credentials", delay: 1900, class: "output" },
        { text: "  ... Mounting NYS Bar Admission", delay: 2100, class: "output" },
        { text: "> SYSTEM READY. WAITING FOR INPUT.", delay: 2400, class: "success-msg" }
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
        }, 10); 
    }

    function runSequence() {
        if (currentIndex < sequence.length) {
            const step = sequence[currentIndex];
            setTimeout(() => {
                typeLine(step, runSequence);
                currentIndex++;
            }, step.delay / 2);
        } else {
            // Boot complete: Reveal GUI and Enable Input
            mainGui.classList.add('visible');
            inputLine.style.display = 'flex';
            cmdInput.focus();
        }
    }

    // --- INTERACTIVE LOGIC ---
    cmdInput.addEventListener('keypress', function (e) {
        if (e.key === 'Enter') {
            const rawInput = cmdInput.value;
            const cmd = rawInput.trim().toLowerCase();
            
            // 1. Echo Command to History
            addHistory("user@legal-os:~$ " + rawInput, "command-echo");
            
            // 2. Process Command
            cmdInput.value = '';
            processCommand(cmd);
            
            // 3. Auto Scroll
            setTimeout(() => window.scrollTo(0, document.body.scrollHeight), 10);
        }
    });

    function addHistory(text, type) {
        const line = document.createElement('div');
        line.className = 'terminal-line ' + type;
        line.innerHTML = text;
        history.appendChild(line);
    }

    function processCommand(cmd) {
        if (cmd === 'clear' || cmd === 'cls') {
            history.innerHTML = '';
            return;
        }
        if (cmd === 'exit') {
            addHistory("> SESSION TERMINATED. GOODBYE.", "system-msg");
            cmdInput.disabled = true;
            return;
        }

        // Search Knowledge Base
        let response = "> ERROR: UNRECOGNIZED COMMAND. TRY 'HELP'.";
        
        if (db[cmd]) {
            response = db[cmd];
        } else {
            // Fuzzy Search
            if (cmd.includes('resume') || cmd.includes('cv')) response = db['resume'];
            else if (cmd.includes('who') || cmd.includes('name')) response = db['who'];
            else if (cmd.includes('contact') || cmd.includes('email') || cmd.includes('linkedin')) response = db['contact'];
            else if (cmd.includes('job') || cmd.includes('work') || cmd.includes('google')) response = db['who'];
            else if (cmd.includes('paper') || cmd.includes('mit')) response = db['papers'];
            else if (cmd.includes('note') || cmd.includes('law')) response = db['notes'];
        }
        
        addHistory(response, "response-msg");
    }

    // Start System
    runSequence();
    
    // Keep focus
    document.addEventListener('click', function() {
        if(inputLine.style.display !== 'none') cmdInput.focus();
    });
});
"""

# --- 2. THE TERMINAL STYLES (CSS) ---
STYLE_SCSS = """---
---
/* TERMINAL AESTHETIC PROTOCOL v3.1 */
@import url('https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;700&display=swap');

$bg-color: #0a0a0a;
$text-main: #00ff41; 
$text-command: #00f3ff; 
$text-system: #ff00ff; 
$text-dim: #666;

body {
    background-color: $bg-color;
    color: $text-main;
    font-family: 'Fira Code', monospace;
    margin: 0;
    padding: 20px;
    font-size: 14px;
    line-height: 1.6;
    overflow-x: hidden;
    padding-bottom: 100px; /* Space for scrolling */
}

/* Typography & Links */
h1, h2 {
    border-bottom: 1px solid #333;
    padding-bottom: 5px;
    color: $text-command;
    font-size: 1.2rem;
    margin-top: 40px;
    text-transform: uppercase;
}

a {
    color: $text-system;
    text-decoration: none;
    border-bottom: 1px dashed $text-system;
    transition: all 0.2s;
    &:hover { background-color: $text-system; color: $bg-color; }
}

/* Terminal Elements */
.terminal-line { margin-bottom: 5px; white-space: pre-wrap; }
.system-msg { color: $text-dim; }
.command { color: $text-command; font-weight: bold; }
.success-msg { color: $text-main; }
.output { color: #ccc; margin-left: 20px; }
.response-msg { color: #fff; margin-bottom: 15px; display: block; }
.command-echo { color: $text-command; margin-top: 10px; }

/* Interactive Input */
#input-line {
    display: none; /* Hidden until boot finishes */
    align-items: center;
    margin-top: 10px;
}

.prompt {
    color: $text-command;
    margin-right: 10px;
}

#cmd-input {
    background: transparent;
    border: none;
    color: $text-main;
    font-family: 'Fira Code', monospace;
    font-size: 14px;
    outline: none;
    flex-grow: 1;
    width: 100%;
}

/* Main GUI Transition */
#main-gui { opacity: 0; transition: opacity 1s ease-in; }
#main-gui.visible { opacity: 1; }

/* Grid System */
.grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
    gap: 15px;
    margin-top: 15px;
}

.file-card {
    border: 1px solid #333;
    padding: 10px;
    background: rgba(255,255,255,0.02);
    &:hover { border-color: $text-command; background: rgba(0, 243, 255, 0.05); }
}

.label { font-size: 0.7em; color: $text-dim; display: block; margin-bottom: 5px; }
"""

# --- 3. THE HTML STRUCTURE ---
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

    <div id="main-gui">
        
        <div id="history"></div>
        <div id="input-line">
            <span class="prompt">user@legal-os:~$</span>
            <input type="text" id="cmd-input" autocomplete="off" spellcheck="false">
        </div>
        <br>

        <div class="output-block">
            <p>> CURRENT_STATUS: <span style="color: #ff00ff;">ONLINE</span></p>
            <p>
                I am a <strong>Senior Privacy Engineer</strong> at <strong>Google DeepMind</strong> and an <strong>Admitted Attorney (NYS)</strong>.<br>
                My work ensures that AI Agents and Large Language Models adhere to privacy laws and ethical standards.
            </p>
            <p>
                > <a href="/assets/Alexei_Furs_Resume.pdf" target="_blank">[ DOWNLOAD_RESUME.PDF ]</a><br>
                > <a href="https://www.linkedin.com/in/alexei-furs-35587773/" target="_blank">[ CONNECT_LINKEDIN_RELAY ]</a>
            </p>
        </div>

        <h2 id="research-papers">// DIR: /RESEARCH_PAPERS/</h2>
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

        <h2 id="legal-archive">// DIR: /LEGAL_ARCHIVE/ (NOTES)</h2>
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

    </div>

</body>
</html>
"""

def main():
    print("--- INSTALLING INTERACTIVE TERMINAL V3.1 ---")
    
    # Ensure directories exist
    os.makedirs('assets/js', exist_ok=True)
    os.makedirs('assets/css', exist_ok=True)
    
    # Write JS
    with open('assets/js/terminal.js', 'w') as f:
        f.write(TERMINAL_JS)
    print(" > Terminal Engine (JS) Updated.")

    # Write CSS
    with open('assets/css/style.scss', 'w') as f:
        f.write(STYLE_SCSS)
    print(" > Visual Protocol (SCSS) Updated.")

    # Write HTML
    with open('index.html', 'w') as f:
        f.write(INDEX_HTML)
    print(" > Interface (HTML) Rewritten with Input Layer.")
    
    print("--- UPGRADE COMPLETE. RUN GIT COMMANDS TO DEPLOY. ---")

if __name__ == "__main__":
    main()