import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. HTML tag & FOUC Script
content = re.sub(
    r'<html lang="en".*?<script>.*?</script>',
    '<html lang="en" class="dark">\n<head>\n    <meta charset="UTF-8">\n    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n    <title>Batch Photo Cropper - Pro</title>',
    content,
    flags=re.DOTALL
)

# 2. Font
content = content.replace(
    '<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&display=swap" rel="stylesheet">',
    '<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&display=swap" rel="stylesheet">'
)
content = content.replace("sans: ['Outfit', 'sans-serif'],", "sans: ['Space Grotesk', 'sans-serif'],")

# 3. Tailwind config colors
tailwind_colors = """                        // Cyberpunk Deep Dark Backgrounds
                        slate: {
                            50: '#f8fafc',
                            100: '#f1f5f9',
                            200: '#e2e8f0',
                            300: '#cbd5e1',
                            400: '#94a3b8',
                            500: '#64748b',
                            600: '#475569',
                            700: '#334155',
                            800: '#0f172a',  // Very deep navy/black
                            900: '#020617',  // Pitch black
                        },
                        // Fuchsia (Primary)
                        indigo: {
                            200: '#f5d0fe',
                            300: '#f0abfc',
                            400: '#e879f9',
                            500: '#d946ef', // Main Pink
                            600: '#c026d3',
                            700: '#a21caf',
                        },
                        // Cyan (Secondary)
                        purple: {
                            400: '#22d3ee',
                            500: '#06b6d4', // Main Cyan
                            600: '#0891b2',
                        },
                        gray: {
                            300: '#cbd5e1',
                            400: '#94a3b8',
                            500: '#64748b',
                        },
                        primary: '#d946ef',
                        secondary: '#06b6d4',"""
content = re.sub(
    r'colors: \{.*?secondary: \'#[a-f0-9]+\',',
    f'colors: {{\n{tailwind_colors}',
    content,
    flags=re.DOTALL
)

# 4. CSS Variables
css_vars = """        :root {
            /* Fallbacks (mostly ignored since locked to dark mode) */
            --bg-color: #020617;
            --bg-gradient: linear-gradient(135deg, #1e1b4b 0%, #020617 100%);
            --text-color: #f8fafc;
            --glassBg: rgba(2, 6, 23, 0.85);
            --glassBorder: rgba(217, 70, 239, 0.3);
            --shadow-color: rgba(217, 70, 239, 0.2);
            --preloader-bg: #020617;
        }

        .dark {
            --bg-color: #020617;
            --bg-gradient: linear-gradient(135deg, #1e1b4b 0%, #020617 100%);
            --text-color: #f8fafc;
            --glassBg: rgba(2, 6, 23, 0.85);
            --glassBorder: rgba(217, 70, 239, 0.3); /* Neon Pink Border */
            --shadow-color: rgba(6, 182, 212, 0.2); /* Neon Cyan Shadow */
            --preloader-bg: #020617;
        }"""
content = re.sub(
    r':root \{.*\.dark \{.*?\}',
    css_vars,
    content,
    flags=re.DOTALL
)

# 5. Orb Colors and Glows
content = re.sub(
    r'\.orb-1 \{.*?\}',
    '.orb-1 { top: -10%; left: -10%; width: 50vw; height: 50vw; max-width: 600px; max-height: 600px; background: rgba(217, 70, 239, 0.25); filter: blur(120px); animation-delay: 0s; }',
    content
)
content = re.sub(
    r'\.orb-2 \{.*?\}',
    '.orb-2 { bottom: -10%; right: -10%; width: 40vw; height: 40vw; max-width: 500px; max-height: 500px; background: rgba(6, 182, 212, 0.25); filter: blur(100px); animation-delay: -5s; }',
    content
)
content = re.sub(
    r'\.dark \.orb-1 \{.*?\}',
    '.dark .orb-1 { background: rgba(217, 70, 239, 0.35); }',
    content
)
content = re.sub(
    r'\.dark \.orb-2 \{.*?\}',
    '.dark .orb-2 { background: rgba(6, 182, 212, 0.35); }',
    content
)

# 6. Loader Ring
content = re.sub(
    r'\.loader-ring \{.*?\}',
    '.loader-ring {\n            width: 80px;\n            height: 80px;\n            border: 3px solid rgba(217, 70, 239, 0.1);\n            border-top-color: #d946ef;\n            border-left-color: #06b6d4;\n            border-radius: 50%;\n            animation: spin 1s linear infinite;\n            box-shadow: 0 0 15px rgba(217, 70, 239, 0.5), inset 0 0 15px rgba(6, 182, 212, 0.5);\n        }',
    content,
    flags=re.DOTALL
)

# 7. Remove Theme Switcher HTML
content = re.sub(
    r'<button id="theme-toggle".*?</button>',
    '',
    content,
    flags=re.DOTALL
)

# 8. Remove Theme JS
content = re.sub(
    r'// Theme Toggle Logic.*?\}\);',
    '',
    content,
    flags=re.DOTALL
)

# 9. Change some specific Tailwind classes to boost the Cyberpunk feel
# Example: shadow-[0_0_20px_rgba(99,102,241,0.3)] to shadow-[0_0_20px_rgba(217,70,239,0.5)]
content = content.replace('shadow-[0_0_20px_rgba(99,102,241,0.3)]', 'shadow-[0_0_20px_rgba(217,70,239,0.5)]')
# Change emerald button (Finish/Download) to a more Cyberpunk yellow or bright cyan?
# Let's keep it emerald but maybe make it punchier, or just leave it.

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Cyberpunk update applied.")
