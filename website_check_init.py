import screenshot
import json
import os

urls = [
    "http://localhost:8043/",
    "http://localhost:8043/?p=75",
]

data = {}

if not os.path.exists("screenshots"):
    os.mkdir("screenshots")

for i, url in enumerate(urls):
    shot = screenshot.take(url, f"screenshots/{i}.jpg")

    data[url] = shot

with open("original_screenshots.json", "w") as f:
    json.dump(data, f)
