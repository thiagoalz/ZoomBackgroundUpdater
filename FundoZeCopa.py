from PIL import Image, ImageFont, ImageDraw
import datetime
import os
import shutil

#=====Configuracoes=====
#Voce vera a nova imagem na proxima reunião iniciada
#Para atualizar todo dia configure seu SO para rodar esse script na inicializacao

#Imagem original
original_image_path = "FundoZeCopa.png"
#Fonte
font_path = 'GaroaHackerClubeBold.otf'
#tamanho
font_size = 100

#Precisa descobrir qual a pasta e qual o nome de arquivo que o seu zoom usou para salvar o seu background em uso
#Vc pode fazer isso adicionando um background novo e verificando a data dos arquivos 
arquivo_fundo_zoom = "C:\\Users\\99771546\\AppData\\Roaming\\Zoom\\data\\VirtualBkgnd_Custom\\{FFCB4691-A4F1-4031-AD05-C62BA8B7510D}"

arquivo_fundo_teams = "C:\\Users\\99771546\\AppData\\Roaming\\Microsoft\\Teams\\Backgrounds\\Uploads\\FundoZeCopa.png"

#Data final
countdown_date = datetime.date(day=20, month=11, year=2022)

#Frase na imagem
title_text = "Faltam {:02d} dias para a copa"

#Posicao do texto
#lelft, right, center or number of pixels
width_text_pos = "center"

#top, botton, center or number of pixels
height_text_pos = "30"
#======================

def get_center_width(image):
	text_box = image.textbbox((0,0), title_text, font=title_font, align='center', stroke_width=2)
	return((image.im.size[0]/2)-text_box[2]/2)
	
def get_center_height(image):
	text_box = image.textbbox((0,0), title_text, font=title_font, align='center', stroke_width=2)
	return((image.im.size[1]/2)-text_box[3]/2)

def get_right_width(image):
	text_box = image.textbbox((0,0), title_text, font=title_font, align='center', stroke_width=2)
	return((image.im.size[0])-text_box[2])

def get_botton_height(image):
	text_box = image.textbbox((0,0), title_text, font=title_font, align='center', stroke_width=2)
	return((image.im.size[1])-text_box[3])
	
def text_position(image):
	width_return = 0
	match width_text_pos:
		case "center":
			 width_return = get_center_width(image)
		case "left":
			 width_return = 0
		case "right":
			 width_return = get_right_width(image)
		case _:
			try:
				width_return = int(width_text_pos)
			except:
				print("Parametro width_text_pos invalido")		

	height_return = 0
	match height_text_pos:
		case "center":
			 height_return = get_center_height(image)
		case "top":
			 height_return = 0
		case "botton":
			 height_return = get_botton_height(image)
		case _:
			try:
				height_return = int(height_text_pos)
			except:
				print("Parametro height_text_pos invalido")
			
	return (width_return,height_return)
	
#Dias para data final
date_today = datetime.date.today()
gap_countdown = (countdown_date-date_today).days
title_text = title_text.format(gap_countdown)

#Montando Imagem
my_image = Image.open(original_image_path)
title_font = ImageFont.truetype(font_path, font_size)
image_editable = ImageDraw.Draw(my_image)

text_pos = text_position(image_editable)

image_editable.multiline_text(text_pos, title_text, "black", font=title_font, align='center', stroke_width=2, stroke_fill="white")
my_image.save("FundoZeCopaResult.jpg")

#Mudando no Zoom
shutil.copyfile("FundoZeCopaResult.jpg", arquivo_fundo_zoom)

#Mudando no Teams
shutil.copyfile("FundoZeCopaResult.jpg", arquivo_fundo_teams)

os.remove("FundoZeCopaResult.jpg")
	