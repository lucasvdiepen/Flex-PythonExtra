from PIL import Image, ImageFont, ImageDraw

afbeelding = Image.open("bunny.jpg")

breedte = afbeelding.width
hoogte = afbeelding.height

lettertype = ImageFont.truetype("impact", 40)

tekengebied = ImageDraw.Draw(afbeelding)

tekst = "Coding in Python\nNo problemo!"
tekengebied.multiline_text((10,10), tekst, font=lettertype, fill=(0,0,0))

afbeelding.show()
afbeelding.save("meme_met_tekst.jpg")
