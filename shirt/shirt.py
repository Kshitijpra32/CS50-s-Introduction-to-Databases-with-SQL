import sys
from PIL import Image, ImageOps

def main():
    # Expect exactly two command-line arguments
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Validate extensions
    valid_ext = (".jpg", ".jpeg", ".png")
    input_ext = input_file.lower().rsplit(".", 1)[-1]
    output_ext = output_file.lower().rsplit(".", 1)[-1]

    if not input_file.lower().endswith(valid_ext):
        sys.exit("Invalid input")

    if not output_file.lower().endswith(valid_ext):
        sys.exit("Invalid output")

    if input_ext != output_ext:
        sys.exit("Input and output have different extensions")

    # Try opening input file
    try:
        image = Image.open(input_file)
    except FileNotFoundError:
        sys.exit("Input does not exist")

    # Open shirt
    shirt = Image.open("shirt.png")

    # Fit input image to shirt size
    size = shirt.size
    image = ImageOps.fit(image, size)

    # Overlay
    image.paste(shirt, shirt)

    # Save output
    image.save(output_file)


if __name__ == "__main__":
    main()

