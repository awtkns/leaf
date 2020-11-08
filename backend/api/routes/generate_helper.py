from .utils import allacronyms
import random
from api import db

acron_finder = allacronyms.AllAcronyms()

def build_valid_pair():
    found = False

    while not found:
        acron = acron_finder.getRandom()
        if not acron:
            continue

        phrase = acron_finder.search( Keywords=acron, Quantity=1 )
        found = is_abbrev(acron, phrase)

    return {'acron': acron, 'phrases':[phrase]}

async def generate_random_acronyms(acronym: str = 'SFU', numPhrases: int = 3):
    acronym = ''.join(e for e in acronym if e.isalpha())
    phrases = [''] * numPhrases
    for c in acronym:
        words = []
        
        async for wordData in db.client.unigrams.get_collection(c.lower()).find():
            words.append(wordData['word'])
        
        for i in range(numPhrases):
            phrases[i] += random.choice(words).title() + " "

    for i in range(numPhrases):
        phrases[i] = phrases[i].strip()
    
    return phrases

def build_payload(valid_pair, random_phrases):
    valid_phrase = valid_pair['phrases'][0]
    random_phrases.append(valid_phrase)
    random.shuffle(random_phrases)
    valid_pair['phrases'] = random_phrases
    valid_pair['answer'] = valid_phrase

# reference: https://stackoverflow.com/questions/7331462/check-if-a-string-is-a-possible-abbrevation-for-a-name
def is_abbrev(abbrev, text):
    abbrev=abbrev.lower()
    text=text.lower()
    words=text.split()
    if not abbrev:
        return True
    if abbrev and not text:
        return False
    if abbrev[0]!=text[0]:
        return False
    else:
        return (is_abbrev(abbrev[1:],' '.join(words[1:])) or
                any(is_abbrev(abbrev[1:],text[i+1:])
                    for i in range(len(words[0]))))