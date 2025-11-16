import os

# --- 1. THE NEURAL ENGINE (JAVASCRIPT) ---
TERMINAL_JS = """
document.addEventListener('DOMContentLoaded', function() {
    const terminalContent = document.getElementById('terminal-content');
    const mainGui = document.getElementById('main-gui');
    const inputLine = document.getElementById('input-line');
    const cmdInput = document.getElementById('cmd-input');
    const history = document.getElementById('history');
    const promptText = document.querySelector('.prompt');

    // --- CONFIGURATION ---
    const API_KEY = "AIzaSyCQz68Pa_FSesxzCxYJMjMgj7dnHHwijwc"; 
    const OWNER_EMAIL = "alexeifurs92@gmail.com";
    
    const SYSTEM_PROMPT = `You are Legal_OS v7.0, a cyberpunk portfolio assistant for Alexei Furs. 
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
    4. If asked for legal advice, state that you are a portfolio bot and cannot provide legal counsel.`;

    // --- STATE MANAGEMENT ---
    let currentMode = 'BOOT'; // BOOT, INTERROGATION, ACCESS_GRANTED
    let interrogationStep = 0;
    
    const visitorLog = {
        name: "",
        purpose: "",
        metAlexei: "",
        wantsMeeting: "N/A",
        timestamp: new Date().toISOString()
    };

    const interrogationSequence = [
        { text: "IDENTIFY YOURSELF.", field: "name" },
        { text: "STATE YOUR PURPOSE.", field: "purpose" },
        { text: "RELATIONSHIP STATUS: HAVE YOU ENCOUNTERED TARGET [ALEXEI] IN PHYSICAL REALITY? (Y/N)", field: "metAlexei" },
        // Optional step inserted dynamically if answer is N
        { text: "DO YOU SEEK A MEETING? (Y/N)", field: "wantsMeeting" }, 
        { text: "TRANSMIT IDENTIFICATION LOGS TO SECURE SERVER? (Y/N)", field: "transmit" }
    ];

    // --- KNOWLEDGE BASE ---
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

    // --- BOOT SEQUENCE ---
    const bootSequence = [
        { text: "> INITIALIZING SECURITY PROTOCOL...", delay: 200, class: "system-msg" },
        { text: "> SCANNING BIOMETRICS...", delay: 400, class: "system-msg" },
        { text: "> UNIDENTIFIED USER DETECTED.", delay: 600, class: "error-msg" },
        { text: "> HALT. SECURITY CLEARANCE REQUIRED.", delay: 1000, class: "error-msg" }
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
                window.scrollTo(0, document.body.scrollHeight);
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
            // Boot done, start interrogation
            currentMode = 'INTERROGATION';
            promptText.innerText = "UNKNOWN_USER@GATEKEEPER:~$";
            promptText.style.color = "#ff2a2a"; // Red for danger
            cmdInput.style.color = "#ff2a2a";
            inputLine.style.display = 'flex';
            inputLine.style.borderColor = "#ff2a2a";
            
            // Print first question
            askNextQuestion();
        }
    }

    function askNextQuestion() {
        // Skip conditional logic for array mapping, handle logic here
        let q = interrogationSequence[interrogationStep];
        
        // Logic for skipping "Meeting" question if they HAVE met Alexei
        if (q.field === "wantsMeeting" && (visitorLog.metAlexei.toLowerCase().startsWith('y'))) {
            interrogationStep++;
            askNextQuestion();
            return;
        }

        const line = document.createElement('div');
        line.className = 'terminal-line question-msg';
        line.innerText = "> " + q.text;
        history.appendChild(line);
        
        cmdInput.value = "";
        cmdInput.focus();
        window.scrollTo(0, document.body.scrollHeight);
    }

    function grantAccess() {
        currentMode = 'ACCESS_GRANTED';
        
        const grantMsg = [
            { text: "> IDENTITY VERIFIED.", delay: 500, class: "success-msg" },
            { text: "> UNLOCKING GEMINI 2.5 NEURAL NET...", delay: 800, class: "success-msg" },
            { text: "> ACCESS GRANTED: WELCOME TO LEGAL_OS.", delay: 1200, class: "success-msg" }
        ];

        let i = 0;
        function showGrant() {
            if (i < grantMsg.length) {
                typeLine(grantMsg[i], history, () => {
                    setTimeout(() => { i++; showGrant(); }, 300);
                });
            } else {
                // Switch UI to Safe Mode
                promptText.innerText = "user@legal-os:~$";
                promptText.style.color = "#00f3ff"; 
                cmdInput.style.color = "#00ff41";
                inputLine.style.borderColor = "#333";
                mainGui.classList.add('visible');
                cmdInput.placeholder = "Ask me anything (e.g. 'Who is the president?', 'Draft an NDA')";
                cmdInput.focus();
            }
        }
        showGrant();
    }

    function handleInterrogationInput(input) {
        const currentQ = interrogationSequence[interrogationStep];
        
        // Store Answer
        visitorLog[currentQ.field] = input;
        
        // Echo Answer
        const echo = document.createElement('div');
        echo.className = 'terminal-line command-echo';
        echo.style.color = "#ff2a2a"; // Keep it red
        echo.innerText = input;
        history.appendChild(echo);

        // Handle Special Logic
        if (currentQ.field === "transmit") {
            if (input.toLowerCase().startsWith('y')) {
                const subject = `LEGAL_OS VISITOR LOG: ${visitorLog.name}`;
                const body = `VISITOR LOG CAPTURED:\n\nNAME: ${visitorLog.name}\nPURPOSE: ${visitorLog.purpose}\nMET ALEXEI: ${visitorLog.metAlexei}\nWANTS MEETING: ${visitorLog.wantsMeeting}\n\nTIMESTAMP: ${visitorLog.timestamp}`;
                window.open(`mailto:${OWNER_EMAIL}?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`);
                
                const sent = document.createElement('div');
                sent.className = 'terminal-line system-msg';
                sent.innerText = "> LOGS TRANSMITTED TO SECURE SERVER.";
                history.appendChild(sent);
            } else {
                const skip = document.createElement('div');
                skip.className = 'terminal-line system-msg';
                skip.innerText = "> TRANSMISSION ABORTED. LOCAL LOGS PURGED.";
                history.appendChild(skip);
            }
            
            // End Interrogation
            setTimeout(grantAccess, 1000);
            return;
        }

        interrogationStep++;
        if (interrogationStep < interrogationSequence.length) {
            setTimeout(askNextQuestion, 500);
        } else {
            // Should be caught by transmit logic, but failsafe
            grantAccess();
        }
    }

    // --- AI LOGIC: GEMINI 2.5 API CALL ---
    async function callGemini(prompt) {
        if (API_KEY.includes("PUT_YOUR")) return "> ERROR: API KEY NOT CONFIGURED.";
        const url = `https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key=${API_KEY}`;
        try {
            const response = await fetch(url, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ contents: [{ parts: [{ text: SYSTEM_PROMPT + "\\n\\nUSER QUERY: " + prompt }] }] })
            });
            const data = await response.json();
            if (data.error) return `> API ERROR: ${data.error.message}`;
            if (data.candidates && data.candidates.length > 0) return data.candidates[0].content.parts[0].text.replace(/\\n/g, "<br>");
            return "> API ERROR: No response.";
        } catch (error) { return "> CONNECTION FAILURE."; }
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
                setTimeout(() => { line.remove(); callback(); }, 200);
            }
        }, 30);
    }

    // --- INPUT HANDLER ---
    cmdInput.addEventListener('keypress', function (e) {
        if (e.key === 'Enter') {
            const rawInput = cmdInput.value.trim();
            if (!rawInput) return;

            if (currentMode === 'INTERROGATION') {
                handleInterrogationInput(rawInput);
                return;
            }

            // ACCESS GRANTED MODE
            const echo = document.createElement('div');
            echo.className = 'terminal-line command-echo';
            echo.innerText = `user@legal-os:~$ ${rawInput}`;
            history.appendChild(echo);
            
            cmdInput.value = '';
            cmdInput.disabled = true;

            let localResponse = null;
            const lowerInput = rawInput.toLowerCase();
            
            if (lowerInput === 'clear') {
                history.innerHTML = '';
                cmdInput.disabled = false;
                cmdInput.focus();
                return;
            }
            
            // Check Knowledge Base
            for (const [intent, keywords] of Object.entries({
                "experience": ["work", "job", "history", "career"],
                "education": ["school", "college", "degree", "law"],
                "skills": ["skill", "tech", "python", "sql"],
                "contact": ["email", "phone", "linkedin", "contact"],
                "bar": ["bar", "lawyer", "attorney", "admitted"],
                "projects": ["project", "paper", "mit", "blip"]
            })) {
                if (keywords.some(k => lowerInput.includes(k)) && knowledge[intent]) {
                    localResponse = knowledge[intent];
                    break;
                }
            }

            if (localResponse) {
                const respDiv = document.createElement('div');
                respDiv.className = 'terminal-line response-msg';
                respDiv.innerHTML = localResponse;
                history.appendChild(respDiv);
                cmdInput.disabled = false;
                cmdInput.focus();
            } else {
                simulateThinking(async () => {
                    const aiResponse = await callGemini(rawInput);
                    const respDiv = document.createElement('div');
                    respDiv.className = 'terminal-line response-msg';
                    respDiv.style.borderLeftColor = "#00f3ff"; 
                    respDiv.innerHTML = aiResponse;
                    history.appendChild(respDiv);
                    cmdInput.disabled = false;
                    cmdInput.focus();
                });
            }
        }
    });

    runBoot();
    
    document.addEventListener('click', () => {
        if(inputLine.style.display !== 'none' && !cmdInput.disabled) cmdInput.focus();
    });
});
"""

# --- 2. THE TERMINAL STYLES (CSS) ---
STYLE_SCSS = """---
---
/* TERMINAL AESTHETIC PROTOCOL v7.0 */
@import url('https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;700&display=swap');

$bg-color: #0a0a0a;
$text-main: #00ff41; 
$text-command: #00f3ff; 
$text-system: #ff00ff; 
$text-dim: #666;
$text-danger: #ff2a2a;

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
.error-msg { color: $text-danger; font-weight: bold; }
.question-msg { color: $text-danger; border-left: 3px solid $text-danger; padding-left: 10px; margin-top: 20px; }

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
    <title>alexei@gatekeeper:~</title>
    <link rel="stylesheet" href="/assets/css/style.css">
    <script src="/assets/js/terminal.js"></script>
</head>
<body>

    <div id="terminal-content"></div>

    <div id="history" style="margin-top: 20px; margin-bottom: 20px;"></div>

    <div id="input-line">
        <span class="prompt">user@legal-os:~$</span>
        <input type="text" id="cmd-input" autocomplete="off" spellcheck="false" placeholder="">
    </div>

    <div id="main-gui">
        
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
    print("--- INSTALLING LEGAL_OS v7.0 (GATEKEEPER PROTOCOL) ---")
    
    # Ensure directories exist
    os.makedirs('assets/js', exist_ok=True)
    os.makedirs('assets/css', exist_ok=True)
    
    # Write JS
    with open('assets/js/terminal.js', 'w') as f:
        f.write(TERMINAL_JS)
    print(" > Neural Engine (Gatekeeper Logic) Updated.")

    # Write CSS
    with open('assets/css/style.scss', 'w') as f:
        f.write(STYLE_SCSS)
    print(" > Visual Protocol Updated.")

    # Write HTML
    with open('index.html', 'w') as f:
        f.write(INDEX_HTML)
    print(" > Interface Updated.")
    
    print("--- UPGRADE COMPLETE. REMEMBER TO ADD YOUR API KEY AND EMAIL! ---")

if __name__ == "__main__":
    main()