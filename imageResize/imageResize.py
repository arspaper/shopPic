from PIL import Image


def imageResize(imagePath, ratio, resultPath, show=False):
    print()
    print("======================")
    print("IMAGE_RESIZE START")
    image = Image.open(imagePath)
    print(f"Image opened from {imagePath}")
    width, height = image.size
    image = image.resize((int(width * ratio), int(height * ratio)), Image.Resampling.LANCZOS)
    print("Image resized")
    if show:
        image.show()
    image.save(resultPath)
    print(f"Image saved to {resultPath}")
