from engine import run


productImagePath = "imageDir/product/prod.jpg"
backgroundImagePath = "imageDir/backgrounds/waves.jpg"
warrantyImagePath = "imageDir/logos/1warranty.jpg"
warrantyText = "Гарантия 1 год"
fontPath = "fonts/arial.ttf"
fontColor = "white"
fontSize = 40
resultPath = "result/result.jpg"
keyboardPath = "imageDir/logos/ru.jpg"
keyboardText = "Русская раскладка"
show_result = True


run(productImagePath, backgroundImagePath, warrantyImagePath, warrantyText, fontPath, resultPath, fontSize,
    fontColor, keyboardPath, keyboardText, show_result)
