from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


for i in range(2010):

    img = Image.new('RGB', (50, 50))
    d = ImageDraw.Draw(img)
    font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeMono.ttf", 20)
    d.text((0, 20), f'{i}', fill=(255, 0, 0), font=font)

    img.save(f'./{i}.png')
