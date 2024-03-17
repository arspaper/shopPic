from engine import run


productImagePath = "imageDir/product/prod.jpg"  # e.g.: imageDir/product/prod.jpg
backgroundImagePath = "imageDir/backgrounds/waves.jpg"  # e.g.: imageDir/backgrounds/waves.jpg
warrantyImagePath = "imageDir/logos/1warranty.jpg"  # e.g.: imageDir/logos/1warranty.jpg
warrantyText = "Testing"  # e.g.: Гарантия 1 год
fontPath = "fonts/arial.ttf"  # e.g.: fonts/arial.ttf
fontColor = "white"
fontSize = 20
resultPath = "YOUR_RESULT_IMAGE_PATH"  # e.g.: result/result.jpg
show_result = True  # Do you want to see result? True/False


run(productImagePath, backgroundImagePath, warrantyImagePath, warrantyText, fontPath, resultPath, fontSize, fontColor)
