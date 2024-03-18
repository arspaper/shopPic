from overlay.overlayProduct import overlayProduct
from overlay.overlayWarranty import overlayWarranty
from overlay.overlayKeyboard import overlayKeyboard
from bgCrop.bgCrop import bgCrop
from bgRemove.bgRemove import bgRemove
import os, shutil
from PIL import Image

def run(productImagePath, backgroundImagePath, warrantyImagePath, warrantyText, fontPath,
        resultPath, fontSize, fontColor, keyboardPath, keyboardText, show):
    try:
        shutil.rmtree('temp', ignore_errors=True)
    except Exception:
        pass

    os.mkdir("temp")

    bgRemove(productImagePath, "temp/prod.png")
    bgRemove(warrantyImagePath, "temp/warranty.png")
    bgRemove(keyboardPath, "temp/keyboard.png")
    bgCrop(backgroundImagePath, "temp/bg.jpg")
    overlayProduct("temp/prod.png", "temp/bg.jpg")
    overlayWarranty("temp/warranty.png", "temp/Overlay.jpg", warrantyText, fontPath,
                    fontSize, fontColor)
    overlayKeyboard("temp/keyboard.png", "temp/Overlay.jpg", keyboardText, fontPath,
                    fontSize, fontColor, show)
    shutil.copy("temp/Overlay.jpg", resultPath)

    shutil.rmtree('temp', ignore_errors=True)
