from PIL import Image, ImageFont, ImageDraw
import datetime
import os

#Configuracao
#Voce vera a nova imagem na proxima reunião
#Para atualizar todo dia configure seu SO para rodar esse script na inicializacao

#Precisa ver qual a pasta e qual o nome de arquivo que o seu zoom usou para salvar o seu background em uso
arquivo_fundo_zoom = "C:\\Users\\99771546\\AppData\\Roaming\\Zoom\\data\\VirtualBkgnd_Custom\\{FFCB4691-A4F1-4031-AD05-C62BA8B7510D}"

#Dias para copa
date_copa = datetime.date(day=20, month=11, year=2022)
date_today = datetime.date.today()
gap_copa = (date_copa-date_today).days

#Montando Imagem
title_text = "Faltam "+ str(gap_copa) +" dias para a copa"

my_image = Image.open("FundoZeCopa.png")
title_font = ImageFont.truetype('GaroaHackerClubeBold.otf', 100)
image_editable = ImageDraw.Draw(my_image)
image_editable.text((300,20), title_text, (0, 0, 0), font=title_font)
my_image.save("FundoZeCopaResult.jpg")

#Mudando no Zoom
os.replace("FundoZeCopaResult.jpg", arquivo_fundo_zoom)

