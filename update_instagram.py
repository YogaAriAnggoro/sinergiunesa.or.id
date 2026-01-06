
links = [
    "https://www.instagram.com/reel/DPYiLxjD63U/?igsh=cHE1a3V0MGozd2to",
    "https://www.instagram.com/reel/DR38mo5D_Dw/?igsh=aG94bnRraHZ6c3Vp",
    "https://www.instagram.com/reel/DOs6FSDDyMQ/?igsh=eTBuamptem91dnQ5",
    "https://www.instagram.com/p/DLpcTAOv02N/?igsh=MTdxYzNzdGFxY2hsZg==",
    "https://www.instagram.com/p/DStYmGTExfy/?igsh=MWd6aW8zdTVia25lMQ==",
    "https://www.instagram.com/p/DSbdKCxj7AW/?igsh=OTV4amUzdGUyZnRm",
    "https://www.instagram.com/p/DRJmwG9D1dn/?igsh=MWI0cHVqcm1nc3Y4aQ==",
    "https://www.instagram.com/p/DQtvCBhjwi3/?igsh=aHBpOTRjcmoya2M2"
]

# Minimal blockquote content is sufficient as JS renders the actual post
def create_embed_html(link):
    clean_link = link.split('?')[0] # Remove query params for cleaner embed URL usually, but keeping them is fine too.
    # Actually Instagram permalinks usually need to be clean or specific.
    # The provided links have ?igsh=...
    # It's safer to pass the full link provided by user to data-instgrm-permalink
    
    return f"""            <div class="col-md-3 mb-3 p-1">
              <div class="instagram-wrapper">
                <blockquote class="instagram-media" data-instgrm-captioned data-instgrm-permalink="{link}" data-instgrm-version="14" style=" background:#FFF; border:0; border-radius:3px; box-shadow:none; margin: 0; padding:0; width:100%;">
                  <div style="padding:16px;">
                    <a href="{link}" style=" background:#FFFFFF; line-height:0; padding:0 0; text-align:center; text-decoration:none; width:100%;" target="_blank">
                      View this post on Instagram
                    </a>
                  </div>
                </blockquote>
              </div>
            </div>"""

html_content = '          <div class="row justify-content-center">\n'
for link in links:
    html_content += create_embed_html(link) + "\n"
html_content += '          </div>\n          <script async src="//www.instagram.com/embed.js"></script>'

file_path = "awards.html"

with open(file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

start_index = -1
end_index = -1

for i, line in enumerate(lines):
    if 'h4 class="judul">Instagram Sinergi' in line:
        start_index = i + 1 
    if '<!-- Akhir Konten Awards -->' in line:
         # Identifying the end of the section.
         # Structure:
         # <div class="col-md-12"> (contains H4 and Row)
         #   <h4>...</h4>
         #   <div class="row">...</div> (This is what we want to replace)
         # </div> 
         # ...
         # </div> (Closing container)
         # <!-- Akhir Konten Awards -->
         
         # The current file likely has:
         # <div class="col-md-12">
         #   <h4 ...>Instagram Sinergi</h4>
         #   <div class="row">
         #     ...
         #   </div>
         # </div>
         pass

# Scanning more carefully
# We want to replace the DIV class="row" immediately following "Instagram Sinergi"
# and its content, up to the closing div of that row.

tok_start_marker = 'h4 class="judul">Instagram Sinergi'
# The row starts after this.

found_start = False
row_start_idx = -1
row_end_idx = -1

for i, line in enumerate(lines):
    if tok_start_marker in line:
        found_start = True
        continue
    
    if found_start:
        if '<div class="row' in line:
            row_start_idx = i
            break

# Now find the matching closing div for this row.
# Since formatting is well-indented, we can look for the closing div with same indentation?
# Or just look for the next "col-md-12" closing or "container" closing.
# Actually, in the previous `view_file`, the Instagram section was the last part of "Konten Awards".
# It looked like:
# ...
# <div class="col-md-12">
#   <h4>Instagram</h4>
#   <div class="row">...</div>
# </div>
# </div> (row all)
# </div> (container)
# </div> (konten)
# <!-- Akhir Konten Awards -->

# So we can look for the closing div of the `row` we found.
# The row contains `col-md-3` divs.
# We can just search for the line containing `<!-- Akhir Konten Awards -->` and go back a few lines.
# But simpler: replace everything from `row_start_idx` until we see a line that is `        </div>` (indentation 8 spaces) followed by `      </div>` (indentation 6 spaces).
# Let's try to just find the `row` start, and then find the line index of `<script async src="//www.instagram.com/embed.js"></script>`
# The script tag is usually at the end of the embeds.
# In the OLD file, there was a script tag inside EACH column? No, let's check view_file.
# Line 193: <script async src="//www.instagram.com/embed.js"></script>
# Line 287: <script async src="//www.instagram.com/embed.js"></script>
# It seems there was a script tag in every column or multiple.

# Strategy: 
# 1. Find line with "Instagram Sinergi".
# 2. Find the FIRST `<div class="row` after that. This is our Start Replace.
# 3. Find `<!-- Akhir Konten Awards -->`.
# 4. Walk backwards from Akhir Konten Awards to find the closing div of the `col-md-12` wrapping Instagram.
#    The structure is:
#    <div class="col-md-12">  <-- Parent
#       <h4>Instagram</h4>
#       <div class="row">...</div> <-- We want to replace this fully
#    </div>

# So we search for `<!-- Akhir Konten Awards -->`
# The lines immediately before it are closing divs.
# ...
#       </div>  (Closing col-md-12 containing Instagram?) No, let's check indent again.

# HTML Snippet from previous turn:
# 477:           </div> (Closing row of Instagram?)
# 478:         </div> (Closing col-md-12 of Instagram)
# 479:       </div> (Closing row all)
# 480:     </div> (Closing container)
# 481:   </div> (Closing konten)
# 482:   <!-- Akhir Konten Awards -->

# So if we find `<!-- Akhir Konten Awards -->`, we go back:
# - 1 line: </div> (line 481)
# - 2 lines: </div> (line 480)
# - 3 lines: </div> (line 479)
# - 4 lines: </div> (line 478) -- This closes the col-md-12 of Instagram
# - 5 lines: </div> (line 477) -- This closes the ROW of Instagram.

# So the ROW ends at line index of (Akhir - 5).
# Let's verify this logic with search.

akhir_idx = -1
for i, line in enumerate(lines):
    if '<!-- Akhir Konten Awards -->' in line:
        akhir_idx = i
        break

if row_start_idx != -1 and akhir_idx != -1:
    # We want to replace from row_start_idx to (akhir_idx - 4) roughly.
    # To be safe, let's look at the lines around akhir_idx - 4.
    # It should be a </div>.
    
    # Actually, simpler: 
    # The Instagram section is the LAST thing in that container.
    # So valid range is row_start_idx ... up to the line before `</div> <!-- col-md-12 closing -->`
    
    # We can perform the write now.
    
    # Double check indentation of the closing row.
    # The new content closes with `</div>` (for the row) and `<script>`.
    # The original file has closing `</div>` for row at line ~477.
    # We will replace everything from row_start_idx to that closing div.
    
    # Let's count matching divs is hard.
    # Let's use the limit of "end of file" logic relative to that section.
    
    # We replace from `row_start_idx` (inclusive)
    # The end point is the line before the 3rd-to-last </div> before Akhir.
    
    # Let's just grab everything before row_start_idx
    pre = lines[:row_start_idx]
    
    # And everything after the Instagram row.
    # The Instagram row ends just before the closing of col-md-12.
    # col-md-12 closes at roughly akhir_idx - 4.
    
    post_start_idx = -1
    # Scanning backwards from akhir_idx
    # 481: </div>
    # 480: </div>
    # 479: </div>
    # 478: </div> <- col-md-12 closing
    # 477: </div> <- row closing.
    
    # We want to keep 478 onwards.
    # So post_start_idx should be the index where lines[i] is the col-md-12 closing div.
    # Let's verify indentation or count.
    
    # Let's assume standard formatting as seen in ViewFile.
    # We can scan backwards from Akhir looking for 4th </div>?
    
    count_divs = 0
    for j in range(akhir_idx - 1, 0, -1):
        if "</div>" in lines[j]:
            count_divs += 1
            if count_divs == 4: # Found the col-md-12 closing
                post_start_idx = j
                break
                
    if post_start_idx != -1:
        post = lines[post_start_idx:]
        
        with open(file_path, "w", encoding="utf-8") as f:
            f.writelines(pre)
            f.write(html_content + "\n")
            f.writelines(post)
        print("Successfully updated Instagram section.")
    else:
        print("Could not locate end of Instagram section.")
else:
    print("Could not locate start of Instagram section.")
