import importlib.util
import pathlib
from unittest.mock import patch
from PIL import Image, ImageDraw, ImageFont

MODULE_PATH = pathlib.Path(__file__).resolve().parents[1] / 'FundoZeCopa.py'


def load_module():
    spec = importlib.util.spec_from_file_location('fundo', MODULE_PATH)
    module = importlib.util.module_from_spec(spec)
    with patch('shutil.copyfile'), patch('os.remove'):
        spec.loader.exec_module(module)
    return module


def test_text_position_center():
    fundo = load_module()
    fundo.width_text_pos = 'center'
    fundo.height_text_pos = 'center'
    fundo.title_text = 'Test'
    fundo.title_font = ImageFont.load_default()
    fundo.text_stroke_width = 0

    img = Image.new('RGB', (100, 50), 'white')
    draw = ImageDraw.Draw(img)

    x, y = fundo.text_position(draw)
    bbox = draw.textbbox((0, 0), fundo.title_text, font=fundo.title_font,
                          align='center', stroke_width=fundo.text_stroke_width)
    expected_x = (img.size[0] - bbox[2]) / 2
    expected_y = (img.size[1] - bbox[3]) / 2
    assert (x, y) == (expected_x, expected_y)


def test_text_position_left_top():
    fundo = load_module()
    fundo.width_text_pos = 'left'
    fundo.height_text_pos = 'top'
    fundo.title_text = 'Test'
    fundo.title_font = ImageFont.load_default()
    fundo.text_stroke_width = 0

    img = Image.new('RGB', (100, 50), 'white')
    draw = ImageDraw.Draw(img)

    x, y = fundo.text_position(draw)
    assert (x, y) == (0, 0)


def test_text_position_right_bottom():
    fundo = load_module()
    fundo.width_text_pos = 'right'
    fundo.height_text_pos = 'bottom'
    fundo.title_text = 'Test'
    fundo.title_font = ImageFont.load_default()
    fundo.text_stroke_width = 0

    img = Image.new('RGB', (100, 50), 'white')
    draw = ImageDraw.Draw(img)

    x, y = fundo.text_position(draw)
    bbox = draw.textbbox((0, 0), fundo.title_text, font=fundo.title_font,
                          align='center', stroke_width=fundo.text_stroke_width)
    expected_x = img.size[0] - bbox[2]
    expected_y = img.size[1] - bbox[3]
    assert (x, y) == (expected_x, expected_y)


def test_text_position_numeric():
    fundo = load_module()
    fundo.width_text_pos = '10'
    fundo.height_text_pos = '20'
    fundo.title_text = 'Test'
    fundo.title_font = ImageFont.load_default()
    fundo.text_stroke_width = 0

    img = Image.new('RGB', (100, 50), 'white')
    draw = ImageDraw.Draw(img)

    x, y = fundo.text_position(draw)
    assert (x, y) == (10, 20)
