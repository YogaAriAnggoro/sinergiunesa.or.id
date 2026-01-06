import urllib.request

links = [
    "https://vt.tiktok.com/ZS5JagDaX/",
    "https://vt.tiktok.com/ZS5JmFVQH/",
    "https://vt.tiktok.com/ZS5JmNfEb/",
    "https://vt.tiktok.com/ZS5JmLADo/",
    "https://vt.tiktok.com/ZS5JmGmc1/"
]

for link in links:
    try:
        req = urllib.request.Request(link, method='HEAD')
        with urllib.request.urlopen(req) as response:
            print(f"{link} -> {response.geturl()}")
    except Exception as e:
        print(f"{link} -> Error: {e}")
