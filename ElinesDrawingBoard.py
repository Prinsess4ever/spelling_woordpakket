import time
from playsound import playsound, PlaysoundException
import requests
import random
import os
woordpakket_woorden = ["aarde", "laarzen", "dezelfde", "grootste", "piekerde", "bandieten", "fietsen", "wandelden", "ergens", "kussens", "deksel", "zetel", "kriebels", "stekels", "eerder", "langer", "pikdonker", "dochters", "koffers", "meesters"]
woord = random.choice(woordpakket_woorden)
def import_een_woord(woord):
    target = woord + '.mp3'
    if not os.path.exists(target):
        lang = "Lotte"
        source = "ttsmp3"
        payload = {'msg': woord, 'lang': lang, 'source': source}
        r = requests.post("https://ttsmp3.com/makemp3_new.php", data=payload)
        URL = r.json()["URL"]
        mp3 = requests.get(URL)
        with open(target, 'wb') as file:
            file.write(mp3.content)
    playsound(target)

def import_meer_woorden():
    random.shuffle(woordpakket_woorden)
    for woord in woordpakket_woorden:
        # print(woord)
        try:
            import_een_woord(woord)
        except PlaysoundException:
            print(" --> exception!!")
            ...
        time.sleep(5.5)

import_meer_woorden()


