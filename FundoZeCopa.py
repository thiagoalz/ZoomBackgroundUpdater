from PIL import Image, ImageFont, ImageDraw
from datetime import datetime, date
import os
import shutil

#=====Configuracoes=====
#Voce vera a nova imagem na proxima reunião iniciada
#Para atualizar todo dia configure seu SO para rodar esse script na inicializacao

#Imagem original
original_image_path = "FundoZeCopa.png"

#Precisa descobrir qual a pasta e qual o nome de arquivo que o seu zoom usou para salvar o seu background em uso
#Vc pode fazer isso adicionando um background novo e verificando a data dos arquivos
#Padrao Windows: C:\\Users\\Username\\AppData\\Roaming\\Zoom\\data\\VirtualBkgnd_Custom\\{FFCB4691-A4F1-4031-AD05-C62BA8B7510D}
#Padrão macOS: /Users/Username/Library/Application Support/zoom.us/data/VirtualBkgnd_Custom/63327A14-224B-49B1-8E66-30AF4686089A

arquivo_fundo_zoom = "/Users/zeuser/Library/Application Support/zoom.us/data/VirtualBkgnd_Custom/63327A14-224B-49B1-8E66-30AF4686089A"

#Padrao windows: C:\\Users\\99771546\\AppData\\Roaming\\Microsoft\\Teams\\Backgrounds\\Uploads\\FundoZeCopa.png
arquivo_fundo_teams = ""

#Frase na imagem
title_text = "Faltam {:02d} dias para a copa"

#Data final
countdown_date_text = "2022-11-20"
countdown_date = datetime.strptime(countdown_date_text, "%Y-%m-%d").date()
gap_countdown = (countdown_date-date.today()).days
title_text = title_text.format(gap_countdown)

#Fonte
font_path = 'GaroaHackerClubeBold.otf'
font_size = 100
text_color = "black" #you can use "black" or (0,0,0)
text_stroke_color = "white" #you can use "black" or (0,0,0)
text_stroke_width = 0

#Posicao do texto
#left, right, center or number of pixels
width_text_pos = "center"
#top, bottom, center or number of pixels
height_text_pos = "25"
#======================

def get_center_width(image):
	text_box = image.textbbox((0,0), title_text, font=title_font, align='center', stroke_width=text_stroke_width)
	return((image.im.size[0]/2)-text_box[2]/2)
	
def get_center_height(image):
	text_box = image.textbbox((0,0), title_text, font=title_font, align='center', stroke_width=text_stroke_width)
	return((image.im.size[1]/2)-text_box[3]/2)

def get_right_width(image):
	text_box = image.textbbox((0,0), title_text, font=title_font, align='center', stroke_width=text_stroke_width)
	return((image.im.size[0])-text_box[2])

def get_bottom_height(image):
        text_box = image.textbbox((0,0), title_text, font=title_font, align='center', stroke_width=text_stroke_width)
        return((image.im.size[1])-text_box[3])
	
def text_position(image):
	width_return = 0
	if width_text_pos == "center": width_return = get_center_width(image)
	elif width_text_pos == "left": width_return = 0
	elif width_text_pos == "right": width_return = get_right_width(image)
	else:
		try:
			width_return = int(width_text_pos)
		except:
			print("Parametro width_text_pos invalido")		

	height_return = 0
	if height_text_pos == "center": height_return = get_center_height(image)
	elif height_text_pos == "top": height_return = 0
        elif height_text_pos == "bottom": height_return = get_bottom_height(image)
	else:
		try:
			height_return = int(height_text_pos)
		except:
			print("Parametro height_text_pos invalido")
			
	return (width_return,height_return)
	

#Montando Imagem
my_image = Image.open(original_image_path)
title_font = ImageFont.truetype(font_path, font_size)
image_editable = ImageDraw.Draw(my_image)

text_pos = text_position(image_editable)

image_editable.multiline_text(text_pos, title_text, text_color, font=title_font, align='center', stroke_width=text_stroke_width, stroke_fill=text_stroke_color)
my_image.save("FundoZeCopaResult.jpg")

#Mudando no Zoom
if arquivo_fundo_zoom: shutil.copyfile("FundoZeCopaResult.jpg", arquivo_fundo_zoom)

#Mudando no Teams
if arquivo_fundo_teams: shutil.copyfile("FundoZeCopaResult.jpg", arquivo_fundo_teams)

os.remove("FundoZeCopaResult.jpg")

