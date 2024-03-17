from PIL import Image, ImageDraw, ImageFont

def addText(text, position, fontPath, fontSize, font_color):
    print()
    print("======================")
    print("ADD TEXT START")
    image = Image.open('temp/Overlay.jpg')
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(f"{fontPath}", fontSize)
    text_position = (10, 10)
    draw.text(text_position, text, font=font, fill=font_color)
    image.save('temp/Overlay.jpg')
    print("Text added")
