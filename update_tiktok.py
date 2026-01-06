import time

new_content = """          <div class=\"row justify-content-center\">\n            <div class=\"col-md-4 mb-4\">\n              <div class=\"placeholder\" style=\"width: 325px; height: 605px; background-color: #f0f0f0; display: flex; align-items: center; justify-content: center;\">\n                <span>Loading TikTok...</span>\n              </div>\n              <blockquote class=\"tiktok-embed lazyload\" cite=\"https://www.tiktok.com/@sinergiunesa/video/7566190932693945618\" data-video-id=\"7566190932693945618\" style=\"max-width: 605px;min-width: 325px; display: none;\"> <section> <a target=\"_blank\" href=\"https://www.tiktok.com/@sinergiunesa/video/7566190932693945618\">@sinergiunesa</a> </section> </blockquote>\n            </div>\n            <div class=\"col-md-4 mb-4\">\n              <div class=\"placeholder\" style=\"width: 325px; height: 605px; background-color: #f0f0f0; display: flex; align-items: center; justify-content: center;\">\n                <span>Loading TikTok...</span>\n              </div>\n              <blockquote class=\"tiktok-embed lazyload\" cite=\"https://www.tiktok.com/@sinergiunesa/video/7573947011267874056\" data-video-id=\"7573947011267874056\" style=\"max-width: 605px;min-width: 325px; display: none;\"> <section> <a target=\"_blank\" href=\"https://www.tiktok.com/@sinergiunesa/video/7573947011267874056\">@sinergiunesa</a> </section> </blockquote>\n            </div>\n            <div class=\"col-md-4 mb-4\">\n              <div class=\"placeholder\" style=\"width: 325px; height: 605px; background-color: #f0f0f0; display: flex; align-items: center; justify-content: center;\">\n                <span>Loading TikTok...</span>\n              </div>\n              <blockquote class=\"tiktok-embed lazyload\" cite=\"https://www.tiktok.com/@sinergiunesa/video/7565391950103268628\" data-video-id=\"7565391950103268628\" style=\"max-width: 605px;min-width: 325px; display: none;\"> <section> <a target=\"_blank\" href=\"https://www.tiktok.com/@sinergiunesa/video/7565391950103268628\">@sinergiunesa</a> </section> </blockquote>\n            </div>\n          </div>\n          <script async src=\"https://www.tiktok.com/embed.js\"></script>\n          <script>\n            document.addEventListener('DOMContentLoaded', function() {\n              const lazyBlocks = document.querySelectorAll('.tiktok-embed.lazyload');\n              const placeholders = document.querySelectorAll('.placeholder');\n              const observer = new IntersectionObserver((entries, observer) => {\n                entries.forEach(entry => {\n                  if (entry.isIntersecting) {\n                    const block = entry.target;\n                    const placeholder = block.previousElementSibling;\n                    placeholder.style.display = 'none';\n                    block.style.display = 'block';\n                    block.classList.remove('lazyload');\n                    observer.unobserve(block);\n                  }\n                });\n              });\n              lazyBlocks.forEach(block => observer.observe(block));\n            });\n          </script>\n"""

file_path = "awards.html"

with open(file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

start_index = -1
end_index = -1

for i, line in enumerate(lines):
    if 'h4 class="judul">TikTok Sinergi' in line:
        start_index = i + 1 # The line after the header is where we want to start replacing (the row)
    if 'h4 class="judul">Instagram Sinergi' in line:
        end_index = i - 1 # The line before the next header's container start (approx)
        break

if start_index != -1 and end_index != -1:
    lines[start_index:end_index] = [new_content]

with open(file_path, "w", encoding="utf-8") as f:
    f.writelines(lines)
