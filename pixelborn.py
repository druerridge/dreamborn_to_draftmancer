import create_template
import base64
from datetime import datetime
import lcc_error

def id_to_pixelborn_name(id):
    return id

# def name_to_pixelborn_name(name):
#     return name

def load_id_to_pixelborn_name():
    id_to_pixelborn_name = {}
    with open('inputs/pixelborn_all_cards.txt', 'r') as file:
        for line in file:
            pixelborn_name = line.strip()
            id = create_template.to_id(pixelborn_name)
            id_to_pixelborn_name[id] = pixelborn_name
    return id_to_pixelborn_name

def generate_pixelborn_deck(id_to_count):
    id_to_pixelborn_name = load_id_to_pixelborn_name()
    pixelborn_deck_decoded = ""
    for id, count in id_to_count.items():
        try:
            pixelborn_deck_decoded += f"{id_to_pixelborn_name[id]}${count}|"            
        except KeyError:
            raise lcc_error.UnidentifiedCardError(f"Unable to identify card with id {id} ")
    print("pixelborn_deck_decoded")
    print(pixelborn_deck_decoded)
    pixelborn_deck_encoded = base64.b64encode(pixelborn_deck_decoded.encode('utf-8')).decode('utf-8')
    return pixelborn_deck_encoded

def inktable_import_link(pixelborn_deck_encoded):
    current_time = datetime.now().isoformat()
    return f"https://www.inktable.net/lor/import?svc=dreamborn&name={current_time}&id={pixelborn_deck_encoded}"

# def initialize():
#     global id_to_pixelborn_name
#     id_to_pixelborn_name = load_id_to_pixelborn_name()