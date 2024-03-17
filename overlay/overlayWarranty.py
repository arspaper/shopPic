from PIL import Image, ImageFont
from imageResize.imageResize import imageResize
from overlay.addText import addText


def overlayWarranty(logoPath, bgPath, warrantyText, fontPath, fontSize, fontColor, show=False):
    print()
    print("======================")
    print("OVERLAY_WARRANTY START")
    prodImage = Image.open(logoPath)
    bgImage = Image.open(bgPath)
    print(f"Image opened from {logoPath}")
    print(f"Image opened from {bgPath}")
    bgWidth, bgHeight = bgImage.size
    prodWidth, prodHeight = prodImage.size
    prodSizeMax = max(prodWidth, prodHeight)

    if prodSizeMax > bgWidth:
        ratio = bgWidth * 0.36 / prodSizeMax
    else:
        ratio = prodSizeMax / bgWidth * 0.35

    imageResize(logoPath, ratio, "temp/resizedImg.png")
    prodImageNew = Image.open("temp/resizedImg.png")
    prodWidthNew, prodHeightNew = prodImageNew.size
    position = (int(prodWidthNew * 0.03), int(bgHeight - prodHeightNew * 1.03))
    bgImage.paste(prodImageNew, position, prodImageNew)
    print("Image overlayed")
    bgImage.save("temp/Overlay.jpg")
    textPosition = (position[0], int(position[1] - 0.25 * prodHeightNew))
    addText(warrantyText, textPosition, fontPath, fontSize, fontColor)
    print("Image saved to temp/Overlay.jpg")
    if show:
        bgImage.show()
