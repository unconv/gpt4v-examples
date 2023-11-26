import vision
import sys

if len(sys.argv) < 2:
    print(f"Usage: {sys.argv[0]} IMAGE_FILE")
    sys.exit(1)

sketch = sys.argv[1]

response = vision.look(
    image_path=sketch,
    prompt='Convert this sketch into a full, professional HTML and CSS template using Tailwind from a CDN (<script src="https://cdn.tailwindcss.com"></script>). Respond only with the code'
)

print(response)

code = "\n".join(response.split("```")[1].split("```")[0].split("\n")[1:-1])

with open("code.html", "w") as f:
    f.write(code)
