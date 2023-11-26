from openai import OpenAI
import base64

model = OpenAI()

def make(prompt="Something cool", output_file="creation.webp"):
    response = model.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1024",
        quality="standard",
        response_format="b64_json",
        n=1,
    )

    image_b64 = response.data[0].b64_json

    with open(output_file, "wb") as f:
        f.write(base64.b64decode(image_b64))

    return output_file
