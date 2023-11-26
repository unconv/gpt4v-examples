import screenshot
import multivision
import json

with open("original_screenshots.json") as f:
    originals = json.load(f)

for url, original_shot in originals.items():
    new_shot = screenshot.take(url)
    response = multivision.look(
        image_paths=[original_shot, new_shot],
        prompt="Compare these two screenshots and check for errors on the second image compared to the first one. If no errors are found, respond with JSON {\"status\": \"OK\"}. Otherwise, respond with JSON {\"status\": \"ERROR\", \"details\": \"Put here the details of the error\"}",
    )

    if '"status": "OK"' not in response:
        print(response)
