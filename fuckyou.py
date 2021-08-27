from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

img = Image.new('RGB', (50, 50))
d = ImageDraw.Draw(img)
font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeMono.ttf", 28)
d.text((0, 20), '1999', fill=(255, 0, 0), font=font)

img.save('./0.png')
