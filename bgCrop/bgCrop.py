from PIL import Image


def bgCrop(imagePath, resultPath, show=False):
    print()
    print("======================")
    print("BG_CROP START")
    image = Image.open(imagePath)
    print(f"Image opened from {imagePath}")

    width, height = image.size

    if width > height:
        topCoord = 0
        leftCoord = (width - height) // 2
        bottomCoord = height
        rightCoord = (width + height) // 2

    elif width < height:
        topCoord = (height - width) // 2
        leftCoord = 0
        bottomCoord = (height + width) // 2
        rightCoord = width

    else:
        print("Image already has 1:1 aspect ratio")
        if show:
            image.show()
        image.save(resultPath)
        print(f"Image saved to {resultPath}")
        return 0

    image = image.crop((leftCoord, topCoord, rightCoord, bottomCoord))
    print("Image cropped")
    if show:
        image.show()
    image.save(resultPath)
    print(f"Image saved to {resultPath}")
