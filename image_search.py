import json

with open("image_data.json") as f:
    image_data = json.load(f)

search_words = input("Search: ").strip().split(" ")

for image, keywords in image_data.items():
    found = False
    for keyword in keywords:
        for word in search_words:
            if word in keyword:
                found = True
                break
        if found:
            print("images/"+image)
            break
