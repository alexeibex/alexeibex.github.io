import os

# --- 1. THE NEURAL ENGINE (JAVASCRIPT) ---
# Now includes REAL Gemini API calls.
TERMINAL_JS = """
document.addEventListener('DOMContentLoaded', function() {
    const terminalContent = document.getElementById('terminal-content');
    const mainGui = document.getElementById('main-gui');
    const inputLine = document.getElementById('input-line');
    const cmdInput = document.getElementById('cmd-input');
    const history = document.getElementById('history');

    // --- CONFIGURATION ---
    // REPLACE THIS WITH YOUR ACTUAL API KEY FROM GOOGLE AI STUDIO
    const API_KEY = "AIzaSyAkWiLWRhGEFPJy7U4nh1PVYw69FUMbRh8"; 
    
    const SYSTEM_PROMPT = `You are Legal_OS v6.0, a cyberpunk portfolio assistant for Alexei Furs. 
    Alexei is a Senior Privacy Engineer at Google DeepMind and an Admitted Attorney (NYS). 
    Key Bio:
    - Current: Google DeepMind (Privacy for Gemini/AI Agents).
    - Previous: Google (Search/Assistant), Twitter, BetterCloud.
    - Education: Brooklyn Law (JD), Georgetown (BA).
    - Tech: Python, SQL, Privacy Engineering.
    - Projects: MIT Computational Law Report co-author.
    
    INSTRUCTIONS:
    1. Answer the user's question briefly (under 3 sentences).
    2. Use a cool, professional, cyberpunk tone (e.g., "Affirmative," "Data retrieved").
    3. If asked about general facts (math, history), answer correctly but briefly.
    4. If asked for legal advice, state that you are a portfolio bot and cannot provide legal counsel.
    5. Do NOT make up facts about Alexei. Refuse if unsure.`;

    // --- 1. LOCAL KNOWLEDGE BASE (FAST PATH) ---
    const knowledge = {
        "experience": `WORK HISTORY:
        <br>> <strong>Google DeepMind</strong> (2025-Present): Senior Privacy Engineer (AI Agents, Gemini).
        <br>> <strong>Google</strong> (2021-2025): Senior Privacy Engineer (Search & Assistant, Devices).
        <br>> <strong>BetterCloud</strong> (2019-2021): Legal Intern (Commercial Transactions).
        <br>> <strong>Twitter</strong> (2019): Legal Intern (Product Counsel, IP, Policy).
        <br>> <strong>Optimatic</strong> (2014-2018): Lead Product Manager (AdTech).`,
        
        "education": `ACADEMIC RECORD:
        <br>> <strong>Brooklyn Law School</strong> (J.D. 2021): Certificate in IP, Media & Info Law.
        <br>> <strong>Georgetown University</strong> (B.A. 2014): Government.`,
        
        "skills": `SKILLSET MATRIX:
        <br>> <strong>LEGAL:</strong> Privacy Law (GDPR/CCPA/DMA), IP Licensing, Commercial Contracts.
        <br>> <strong>TECH:</strong> Python, SQL, HTML/CSS, GitHub, Distributed Systems.
        <br>> <strong>CORE:</strong> Privacy by Design, AI Governance, Product Management.`,
        
        "bar": "STATUS: <strong>Admitted Attorney</strong> - NYS Appellate Division, 2nd Dept (Feb 2023).",
        
        "projects": `KEY PROJECTS:
        <br>> <strong>MIT Computational Law Report:</strong> Co-Author, "Trust in a Trustless System".
        <br>> <strong>BLIP:</strong> Contributor to Blockchain Law for Information Privacy.`,
        
        "contact": "UPLINK ESTABLISHED: <a href='https://www.linkedin.com/in/alexei-furs-35587773/' target='_blank'>[ LINKEDIN_PROFILE ]</a>",
        
        "resume": "ACCESSING FILE... <a href='/assets/Alexei_Furs_Resume.pdf' target='_blank'>[ DOWNLOAD_RESUME.PDF ]</a>"
    };

    // --- 2. INTENT MAPPING (FAST PATH) ---
    const intentMap = {
        "experience": ["work", "job", "history", "career", "google", "deepmind", "twitter", "optimatic", "experience", "resume", "background"],
        "education": ["school", "college", "university", "degree", "law", "brooklyn", "georgetown", "education", "study", "academic"],
        "skills": ["skill", "tech", "python", "sql", "coding", "program", "language", "tool", "stack", "technology"],
        "contact": ["email", "phone", "linkedin", "reach", "contact", "message", "connect", "hire"],
        "bar": ["bar", "lawyer", "attorney", "admitted", "court", "license", "esq"],
        "projects": ["project", "paper", "research", "mit", "blip", "writing", "publication"]
    };

    // --- 3. BOOT SEQUENCE ---
    const bootSequence = [
        { text: "> INITIALIZING LEGAL_OS v6.0 (GEMINI INTEGRATED)...", delay: 200, class: "system-msg" },
        { text: "> ESTABLISHING NEURAL UPLINK...", delay: 400, class: "system-msg" },
        { text: "> ACCESS GRANTED: ALEXEI FURS [JD_GRADUATE]", delay: 1000, class: "success-msg" },
        { text: "> SYSTEM READY. WAITING FOR INPUT.", delay: 1200, class: "success-msg" }
    ];

    function typeLine(lineObj, container, callback) {
        const line = document.createElement('div');
        line.className = 'terminal-line ' + (lineObj.class || '');
        container.appendChild(line);

        let charIndex = 0;
        const typeInterval = setInterval(() => {
            if (charIndex < lineObj.text.length) {
                line.innerHTML += lineObj.text.charAt(charIndex);
                charIndex++;
            } else {
                clearInterval(typeInterval);
                if (callback) callback();
            }
        }, 5);
    }

    function runBoot(index = 0) {
        if (index < bootSequence.length) {
            typeLine(bootSequence[index], terminalContent, () => {
                setTimeout(() => runBoot(index + 1), bootSequence[index].delay / 2);
            });
        } else {
            mainGui.classList.add('visible');
            inputLine.style.display = 'flex';
            cmdInput.focus();
        }
    }

    // --- AI LOGIC: GEMINI API CALL ---
    async function callGemini(prompt) {
        if (API_KEY === "PUT_YOUR_GEMINI_API_KEY_HERE") {
            return "> ERROR: API KEY NOT CONFIGURED. PLEASE UPDATE terminal.js.";
        }

        const url = `https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=${API_KEY}`;
        
        try {
            const response = await fetch(url, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({
                    contents: [{
                        parts: [{ text: SYSTEM_PROMPT + "\\n\\nUSER QUERY: " + prompt }]
                    }]
                })
            });

            const data = await response.json();
            
            if (data.error) {
                return `> API ERROR: ${data.error.message}`;
            }

            // Extract text
            const text = data.candidates[0].content.parts[0].text;
            // Simple formatting: replace newlines with breaks for HTML
            return text.replace(/\\n/g, "<br>");

        } catch (error) {
            return "> CONNECTION FAILURE: UNABLE TO REACH NEURAL NET.";
        }
    }

    function simulateThinking(callback) {
        const id = 'proc-' + Date.now();
        const line = document.createElement('div');
        line.id = id;
        line.className = 'terminal-line system-msg';
        line.innerText = "> NEURAL_NET_PROCESSING: [                    ] 0%";
        history.appendChild(line);

        let progress = 0;
        const interval = setInterval(() => {
            progress += Math.floor(Math.random() * 15) + 5;
            if (progress > 100) progress = 100;
            
            const bars = "|".repeat(Math.floor(progress / 5));
            const spaces = " ".repeat(20 - Math.floor(progress / 5));
            line.innerText = `> NEURAL_NET_PROCESSING: [${bars}${spaces}] ${progress}%`;

            if (progress === 100) {
                clearInterval(interval);
                setTimeout(() => {
                    line.remove(); 
                    callback();
                }, 200);
            }
        }, 50);
    }

    // --- INPUT HANDLER ---
    cmdInput.addEventListener('keypress', function (e) {
        if (e.key === 'Enter') {
            const rawInput = cmdInput.value.trim();
            if (!rawInput) return;

            // Echo Input
            const echo = document.createElement('div');
            echo.className = 'terminal-line command-echo';
            echo.innerText = `user@legal-os:~$ ${rawInput}`;
            history.appendChild(echo);
            
            cmdInput.value = '';
            cmdInput.disabled = true;

            // Check Local Intents First (Fast Path)
            let localResponse = null;
            const lowerInput = rawInput.toLowerCase();
            
            // Check hardcoded commands
            if (lowerInput === 'clear' || lowerInput === 'cls') {
                history.innerHTML = '';
                cmdInput.disabled = false;
                cmdInput.focus();
                return;
            }
            if (lowerInput === 'help') {
                localResponse = "AVAILABLE COMMANDS: experience, education, skills, bar, projects, contact, resume.<br>OR ASK ANYTHING: 'Who is the president?', 'Draft an NDA'.";
            } else {
                // Check Intent Map
                for (const [intent, keywords] of Object.entries(intentMap)) {
                    if (keywords.some(k => lowerInput.includes(k)) && knowledge[intent]) {
                        localResponse = knowledge[intent];
                        break;
                    }
                }
            }

            if (localResponse) {
                // Instant Response for Local Knowledge
                const respDiv = document.createElement('div');
                respDiv.className = 'terminal-line response-msg';
                respDiv.innerHTML = localResponse;
                history.appendChild(respDiv);
                cmdInput.disabled = false;
                cmdInput.focus();
            } else {
                // API Call for Everything Else
                simulateThinking(async () => {
                    const aiResponse = await callGemini(rawInput);
                    
                    const respDiv = document.createElement('div');
                    respDiv.className = 'terminal-line response-msg';
                    // Add a subtle style to show it came from AI
                    respDiv.style.borderLeftColor = "#00f3ff"; 
                    respDiv.innerHTML = aiResponse;
                    history.appendChild(respDiv);
                    
                    cmdInput.disabled = false;
                    cmdInput.focus();
                });
            }
        }
    });

    // Init
    runBoot();
    
    document.addEventListener('click', () => {
        if(inputLine.style.display !== 'none' && !cmdInput.disabled) cmdInput.focus();
    });
});
"""

# --- 2. THE TERMINAL STYLES (CSS) ---
# Reusing the proven v5 styles
STYLE_SCSS = """---
---
/* TERMINAL AESTHETIC PROTOCOL v6.0 */
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
    padding-bottom: 100px;
}

a {
    color: $text-system;
    text-decoration: none;
    border-bottom: 1px dashed $text-system;
    transition: 0.2s;
    &:hover { background-color: $text-system; color: $bg-color; }
}

h1, h2 {
    border-bottom: 1px solid #333;
    padding-bottom: 5px;
    color: $text-command;
    font-size: 1.2rem;
    margin-top: 40px;
    text-transform: uppercase;
}

.terminal-line { margin-bottom: 5px; white-space: pre-wrap; }
.system-msg { color: $text-dim; }
.command { color: $text-command; font-weight: bold; }
.success-msg { color: $text-main; }
.output { color: #ccc; margin-left: 20px; }
.response-msg { color: #fff; margin-bottom: 20px; display: block; border-left: 3px solid $text-system; padding-left: 15px; }
.command-echo { color: $text-command; margin-top: 15px; font-weight: bold; }

#input-line {
    display: none;
    align-items: center;
    margin-top: 10px;
    background: rgba(255,255,255,0.05);
    padding: 10px;
    border-radius: 4px;
    border: 1px solid #333;
}

.prompt { color: $text-command; margin-right: 10px; }

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

#main-gui { opacity: 0; transition: opacity 1s ease-in; }
#main-gui.visible { opacity: 1; }

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
    transition: 0.2s;
    &:hover { border-color: $text-command; background: rgba(0, 243, 255, 0.05); transform: translateY(-2px); }
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
    <title>alexei@legal-os:~</title>
    <link rel="stylesheet" href="/assets/css/style.css">
    <script src="/assets/js/terminal.js"></script>
</head>
<body>

    <div id="terminal-content"></div>

    <div id="main-gui">
        
        <div id="input-line">
            <span class="prompt">user@legal-os:~$</span>
            <input type="text" id="cmd-input" autocomplete="off" spellcheck="false" placeholder="Ask me anything (e.g. 'What is 1+1?', 'Who is the president?')">
        </div>
        
        <div id="history" style="margin-top: 20px; margin-bottom: 40px;"></div>

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
    print("--- INSTALLING LEGAL_OS v6.0 (GEMINI API INTEGRATION) ---")
    
    # Ensure directories exist
    os.makedirs('assets/js', exist_ok=True)
    os.makedirs('assets/css', exist_ok=True)
    
    # Write JS
    with open('assets/js/terminal.js', 'w') as f:
        f.write(TERMINAL_JS)
    print(" > Neural Engine (Gemini API) Installed.")

    # Write CSS
    with open('assets/css/style.scss', 'w') as f:
        f.write(STYLE_SCSS)
    print(" > Visual Protocol Updated.")

    # Write HTML
    with open('index.html', 'w') as f:
        f.write(INDEX_HTML)
    print(" > Interface Updated.")
    
    print("--- UPGRADE COMPLETE. REMEMBER TO ADD YOUR API KEY BEFORE DEPLOYING! ---")

if __name__ == "__main__":
    main()