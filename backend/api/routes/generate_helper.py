from .utils import allacronyms

acron = allacronyms.AllAcronyms()

def generate_valid_acronyms():
    Abbs = acron.search( Keywords='YOLO', Quantity=10 )
    
    return Abbs

def generate_random_acronyms():
    print('hello')