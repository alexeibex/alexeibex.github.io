import os

# Force clean white-paper styling for printing
PRINT_CSS = """
/* --- FORCE PRINT STYLING (PDF) --- */
@media print {
    /* 1. HIDE CYBERPUNK UI */
    header, footer, .scanline, nav, .cursor, .export-controls, 
    #terminal-content, #input-line, #history, .sidebar, .back-button {
        display: none !important;
    }

    /* 2. RESET DOCUMENT BODY */
    body, .container, #main-gui, main {
        background-color: #ffffff !important;
        background-image: none !important;
        color: #000000 !important;
        font-family: 'Georgia', 'Times New Roman', serif !important;
        width: 100% !important;
        margin: 0 !important;
        padding: 20px !important;
        border: none !important;
        box-shadow: none !important;
        text-shadow: none !important;
        overflow: visible !important;
    }

    /* 3. TYPOGRAPHY */
    h1, h2, h3, h4 {
        color: #000000 !important;
        border-bottom: 1px solid #000 !important;
        page-break-after: avoid;
    }
    
    p, li, ul, ol {
        color: #000000 !important;
        font-size: 12pt !important;
        line-height: 1.5 !important;
    }

    /* 4. LINKS */
    a {
        color: #000000 !important;
        text-decoration: none !important;
    }
    a::after {
        content: " (" attr(href) ")";
        font-size: 0.8em;
        font-style: italic;
    }
}
"""

def main():
    print("--- INJECTING PRINT DRIVERS ---")
    css_path = 'assets/css/style.scss'
    
    if os.path.exists(css_path):
        # Read file to avoid duplicate injection
        with open(css_path, 'r') as f:
            content = f.read()
        
        if "@media print" not in content:
            with open(css_path, 'a') as f:
                f.write(PRINT_CSS)
            print(" > Print drivers installed.")
        else:
            print(" > Print drivers already present. Overwriting end of file to ensure latest version.")
            # Optional: You could choose to replace, but appending usually overrides due to CSS specificity
            with open(css_path, 'a') as f:
                f.write(PRINT_CSS)
    else:
        print(" ! ERROR: style.scss not found.")

if __name__ == "__main__":
    main()