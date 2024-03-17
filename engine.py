from overlay.overlayProduct import overlayProduct
from overlay.overlayWarranty import overlayWarranty
from bgCrop.bgCrop import bgCrop
from bgRemove.bgRemove import bgRemove
import os, shutil
def run(productImagePath, backgroundImagePath, warrantyImagePath, warrantyText, fontPath,
        resultPath, fontSize, fontColor):
    try:
        shutil.rmtree('temp', ignore_errors=True)
    except Exception:
        pass

    os.mkdir("temp")

    bgRemove(productImagePath, "temp/prod.png")
    bgRemove(warrantyImagePath, "temp/warranty.png")
    bgCrop(backgroundImagePath, "temp/bg.jpg")
    overlayProduct("temp/prod.png", "temp/bg.jpg")
    overlayWarranty("temp/warranty.png", "temp/Overlay.jpg", warrantyText, fontPath,
                    fontSize, fontColor, 1)

    shutil.rmtree('temp', ignore_errors=True)
