from PIL import Image, ImageFont, ImageDraw
import datetime
import os
import shutil

#=====Configuracao=====
#Voce vera a nova imagem na proxima reunião iniciada
#Para atualizar todo dia configure seu SO para rodar esse script na inicializacao

#Precisa descobrir qual a pasta e qual o nome de arquivo que o seu zoom usou para salvar o seu background em uso
#Vc pode fazer isso adicionando um background novo e verificando a data dos arquivos 
arquivo_fundo_zoom = "C:\\Users\\99771546\\AppData\\Roaming\\Zoom\\data\\VirtualBkgnd_Custom\\{FFCB4691-A4F1-4031-AD05-C62BA8B7510D}"

arquivo_fundo_teams = "C:\\Users\\99771546\\AppData\\Roaming\\Microsoft\\Teams\\Backgrounds\\Uploads\\FundoZeCopa.png"

#Data final
countdown_date = datetime.date(day=20, month=11, year=2022)

#Frase na imagem
title_text = "Faltam {:02d} dias para a copa"
#======================

#Dias para data final
date_today = datetime.date.today()
gap_countdown = (countdown_date-date_today).days

#Montando Imagem
title_text = title_text.format(gap_countdown)

my_image = Image.open("FundoZeCopa.png")
title_font = ImageFont.truetype('GaroaHackerClubeBold.otf', 100)
image_editable = ImageDraw.Draw(my_image)
image_editable.multiline_text((300,20), title_text, "black", font=title_font, align='center', stroke_width=2, stroke_fill="white")
my_image.save("FundoZeCopaResult.jpg")

#Mudando no Zoom
shutil.copyfile("FundoZeCopaResult.jpg", arquivo_fundo_zoom)

#Mudando no Teams
shutil.copyfile("FundoZeCopaResult.jpg", arquivo_fundo_teams)

os.remove("FundoZeCopaResult.jpg")