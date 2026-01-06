import os
import glob

# The files to update
files = [
    "KSM.html",
    "arsipberita.html",
    "arsipberita2.html",
    "awards.html",
    "capacitybuilding.html",
    "capacitybuilding2025.html",
    "famgath.html",
    "famgath2025.html",
    "index.html",
    "isiberita.html",
    "organisasi.html",
    "profil.html",
    "raker.html",
    "raker2025.html",
    "struktur organisasi.html"
]

# The closing part of the address might be split across lines in source HTML, 
# but usually we can find the start and end of the block.
# Let's search for the block signature.

new_footer_content = """            <h6 style="font-weight: bold;">UNIVERSITAS NEGERI SURABAYA</h6>
            <p style="margin-bottom: 6px;">Sekretariat BEM U, Lt.1, UKM Center, Unesa, Jl. Ketintang No.8, Ketintang, Kec. Gayungan, Surabaya, Jawa Timur 60231</p>
            <p style="margin-bottom: 6px;">+62 858-5425-4727 (Umi Nur Hidayah)</p>
            <p style="margin-bottom: 6px;">Instagram: @Sinergiunesa</p>
            <p style="margin-bottom: 6px;">TikTok: @Sinergiunesa</p>
            <p style="margin-bottom: 6px;">YouTube: Sinergi Vlog</p>
            <p style="margin-bottom: 6px;">Email: sinergiunesa@gmail.com</p>
            <p style="margin-bottom: 0;">Website: sinergiunesa.or.id</p>"""

def update_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # We need to find the specific block. Since whitespace/newlines might vary slightly, 
    # we can try to locate the start of the block and the end.
    
    start_marker = '<h6 style="font-weight: bold;">UNIVERSITAS NEGERI SURABAYA</h6>'
    end_marker = 'Email: sinergiunesa@gmail.com</p>'
    
    start_idx = content.find(start_marker)
    if start_idx == -1:
        print(f"Skipping {filepath}: Start marker not found")
        return

    # Find the end of the paragraph containing the email
    email_idx = content.find(end_marker, start_idx)
    if email_idx == -1:
        print(f"Skipping {filepath}: End marker not found")
        return
    
    # Calculate end_idx: it should include the closing </p> which is part of end_marker
    end_idx = email_idx + len(end_marker)
    
    # We want to check content between start and end to make sure it's the right block
    # It is safe enough since that specific H6 is unique to footer.
    
    # indentation detection
    # find the newline before start_marker
    last_newline = content.rfind('\n', 0, start_idx)
    indentation = ""
    if last_newline != -1:
        indentation = content[last_newline+1:start_idx]
    
    # Prepare new block with correct indentation
    # new_footer_content lines serve as template.
    # We should adjust indentation of new_footer_content to match target file if needed, 
    # but using the common indentation from my variable might be enough if files are consistent.
    # The variable `new_footer_content` already has spaces. Let's trust it aligns reasonably well 
    # or just use the replace.
    
    # Construct new content
    new_content = content[:start_idx] + new_footer_content.strip() + content[end_idx:]
    
    # Check if we need to fix indentation for the first line of the new block? 
    # The strip() removes leading spaces from first line, 
    # but content[:start_idx] keeps the indentation of the original first line.
    
    # However, subsequent lines in `new_footer_content` have hardcoded spaces.
    # Ideally they should match the file's indentation.
    # But files might use tabs or different spaces.
    # Let's simple use the string replacement method, assuming consistent formatting related to `awards.html` style.
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Updated {filepath}")

for filename in files:
    try:
        update_file(filename)
    except Exception as e:
        print(f"Error processing {filename}: {e}")
