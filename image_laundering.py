import vision
import dalle
import sys

if len(sys.argv) < 2:
    print(f"Usage: {sys.argv[0]} IMAGE_FILE")
    sys.exit(1)

image_file = sys.argv[1]

original = vision.look(image_file)
laundered = dalle.make(original)

print(laundered)
