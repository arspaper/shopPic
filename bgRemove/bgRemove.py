from rembg import remove
from PIL import Image

def bgRemove(imagePath, resultPath, show=False):
    print()
    print("======================")
    print("BG_REMOVE START")
    image = Image.open(imagePath)
    print(f"Image opened from {imagePath}")
    image = remove(image)
    if show:
        image.show()
    image.save(resultPath)
    print(f"Image saved to {resultPath}")
