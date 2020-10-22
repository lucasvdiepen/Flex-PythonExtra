from PIL import Image, ImageFont, ImageDraw

file = open("meme_tekst.txt")

memeCounter = 0

for text in file:
    memeCounter += 1
    text = text.strip()
    afbeelding = Image.open("meme.jpg")

    breedte = afbeelding.width
    hoogte = afbeelding.height

    lettertype = ImageFont.truetype("impact.ttf", 40)
    
    tekengebied = ImageDraw.Draw(afbeelding)
    tekst_breedte, tekst_hoogte = tekengebied.textsize(text, font=lettertype)

    tekst_x = (breedte - tekst_breedte) / 2
    tekst_y = 10

    tekengebied.multiline_text((tekst_x, tekst_y), text, font=lettertype, fill=(0,0,0))
    tekengebied.multiline_text((tekst_x-2, tekst_y-2), text, font=lettertype, fill=(255,255,255))

    afbeelding.save("meme" + str(memeCounter) + ".jpg")

print(str(memeCounter) + " memes gemaakt")
