import vision
import json
import os

data = {}

if not os.path.exists("images"):
    os.mkdir("images")

for image in os.listdir("images"):
    print(image)

    keywords = vision.look(
        image_path="images/"+image,
        prompt="Make a comma separated list of keywords that describe this image"
    ).split(", ")

    data[image] = keywords

    with open("image_data.json", "w") as f:
        json.dump(data, f, indent=4)

print("DONE!")
