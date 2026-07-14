import re

file_path = 'd:/Suresh Kumar/Auto Cropper/index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Helper function to replace a class globally inside class="..." attributes
def replace_class(html_content, old_class, new_class):
    # This regex looks for class="..." and replaces the specific token inside it
    def replacer(match):
        classes = match.group(1).split()
        if old_class in classes:
            classes = [new_class if c == old_class else c for c in classes]
        return 'class="' + ' '.join(classes) + '"'
    
    return re.sub(r'class="([^"]*)"', replacer, html_content)

# Map of old classes to new light/dark classes
replacements = {
    'text-gray-300': 'text-slate-700 dark:text-gray-300',
    'text-gray-400': 'text-slate-600 dark:text-gray-400',
    'text-gray-500': 'text-slate-500 dark:text-gray-500',
    'text-white': 'text-slate-900 dark:text-white',
    
    'bg-slate-900': 'bg-white dark:bg-slate-900',
    'bg-slate-800': 'bg-slate-50 dark:bg-slate-800',
    'bg-slate-700': 'bg-slate-200 dark:bg-slate-700',
    
    'border-slate-800': 'border-slate-200 dark:border-slate-800',
    'border-slate-700': 'border-slate-300 dark:border-slate-700',
    'border-slate-600': 'border-slate-300 dark:border-slate-600',
    
    'border-white/10': 'border-slate-200 dark:border-white/10',
    'border-white/5': 'border-slate-100 dark:border-white/5',
    'bg-white/5': 'bg-slate-100 dark:bg-white/5',
    'bg-white/10': 'bg-slate-200 dark:bg-white/10',
    
    'bg-[#0f172a]': 'bg-slate-50 dark:bg-[#0f172a]',
    'bg-black/50': 'bg-white/50 dark:bg-black/50'
}

for old, new in replacements.items():
    content = replace_class(content, old, new)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Theme refactoring complete.")
