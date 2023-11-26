from PIL import Image
import os

def split(input_image_path, output_folder, piece_height, offset=0):
    if not os.path.exists(output_folder):
        os.mkdir(output_folder)

    # Open the input image
    original_image = Image.open(input_image_path)

    # Get the width and height of the original image
    width, height = original_image.size

    # Initialize pieces and fist piece size
    pieces = []
    upper = 0
    lower = piece_height

    # Loop to split the image vertically
    while lower <= height:
        left = 0
        right = width

        # Crop the piece from the original image
        piece = original_image.crop((left, upper, right, lower))

        # Move the crop area down
        upper += piece_height - offset
        lower += piece_height - offset

        # Save the piece to the output folder with a unique name
        piece_file = f"{output_folder}/piece_{len(pieces)}.jpg"
        piece.save(piece_file)

        # Add piece filename to return value
        pieces.append(piece_file)

    return pieces
