from PIL import Image
from imageResize.imageResize import imageResize


def overlayProduct(prodPath, bgPath, show=False):
    print()
    print("======================")
    print("OVERLAY_PRODUCT START")
    prodImage = Image.open(prodPath)
    bgImage = Image.open(bgPath)
    print(f"Image opened from {prodPath}")
    print(f"Image opened from {bgPath}")
    bgWidth, bgHeight = bgImage.size
    prodWidth, prodHeight = prodImage.size
    prodSizeMax = max(prodWidth, prodHeight)

    if prodSizeMax > bgWidth:
        ratio = bgWidth * 0.8 / prodSizeMax
    else:
        ratio = prodSizeMax / bgWidth * 0.8

    imageResize(prodPath, ratio, "temp/resizedImg.png")
    prodImageNew = Image.open("temp/resizedImg.png")
    prodWidthNew, prodHeightNew = prodImageNew.size
    position = ((bgWidth - prodWidthNew), (bgHeight - prodHeightNew) // 2)
    bgImage.paste(prodImageNew, position, prodImageNew)
    print("Image overlayed")
    if show:
        bgImage.show()
    bgImage.save("temp/Overlay.jpg")
    print("Image saved to temp/Overlay.jpg")
