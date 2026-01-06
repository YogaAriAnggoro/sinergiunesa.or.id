import glob

files = [
    "KSM.html",
    "arsipberita.html",
    "arsipberita2.html",
    "capacitybuilding.html",
    "capacitybuilding2025.html",
    "famgath.html",
    "famgath2025.html",
    "isiberita.html",
    "raker.html",
    "raker2025.html"
]

target_str = r"img/sinergi\ news.png"
# Also try without backslash just in case
target_str_2 = "img/sinergi news.png"

replacement_str = "img/SINERGILITERASI.png"

for filepath in files:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        new_content = content
        if target_str in new_content:
            new_content = new_content.replace(target_str, replacement_str)
        
        if target_str_2 in new_content:
             new_content = new_content.replace(target_str_2, replacement_str)

        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {filepath}")
        else:
            print(f"No changes in {filepath}")
            
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
