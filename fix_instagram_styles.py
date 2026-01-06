
file_path = "awards.html"

# We want to replace class="instagram-wrapper" with class="instagram-wrapper" style="..."
# to ensure the height is forced even if CSS isn't loaded.

style_string = 'style="height: 580px; width: 100%; overflow: hidden; border: 1px solid #e1e8ed; border-radius: 8px; background-color: white; display: flex; justify-content: center;"'
target_str = '<div class="instagram-wrapper">'
replace_str = f'<div class="instagram-wrapper" {style_string}>'

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

if target_str in content:
    new_content = content.replace(target_str, replace_str)
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Successfully added inline styles to Instagram wrappers.")
else:
    print("Could not find instagram-wrapper class in HTML.")
