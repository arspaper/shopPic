from PIL import Image, ImageDraw, ImageFont

def addText(text, position, fontPath, fontSize, font_color, show):
    print()
    print("======================")
    print("ADD TEXT START")
    image = Image.open('temp/Overlay.jpg')
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(fontPath, fontSize)
    text_position = position
    draw.text(text_position, text, font=font, fill=font_color)
    image.save('temp/Overlay.jpg')
    print("Text added")
    if show:
        image.show()

