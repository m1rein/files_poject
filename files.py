import os
from pathlib import Path

def vse_fajly_iz_papki(gde_iskat=None):
    if gde_iskat is None:
        if os.path.exists('C:\\'):
            gde_iskat = 'C:\\'
        else:
            gde_iskat = 'D:\\'
    rezultat = []
    for chto in os.listdir(gde_iskat):
        if os.path.isfile(os.path.join(gde_iskat, chto)):
            rezultat.append(chto)
    rezultat.sort()
    return rezultat
def poluchit_ikonku(imya):
    return '+'
def razmer_fajla(imya):
    if os.path.exists(imya):
        razmer = os.path.getsize(imya)
        if razmer < 1024:
            return f'{razmer} Б'
        elif razmer < 1024 * 1024:
            return f'{razmer // 1024} КБ'
        elif razmer < 1024 * 1024 * 1024:
            return f'{razmer // (1024 * 1024)} МБ'
        else:
            return f'{razmer // (1024 * 1024 * 1024)} ГБ'
    return '0 B'
def sozdat_fajl(imya, tekst):
    if not imya.endswith('.txt'):
        imya = imya + '.txt'
    
    with open(imya, 'w', encoding='utf-8') as f:
        f.write(tekst)
    return imya

def udalit_fajl(imya):
    if os.path.exists(imya):
        os.remove(imya)
        return True
    return False

def pereimenovat_fajl(staroe, novoe):
    if not novoe.endswith('.txt'):
        novoe = novoe + '.txt'
    
    if os.path.exists(staroe):
        os.rename(staroe, novoe)
        return novoe
    return None

def prochitat_fajl(imya):
    if os.path.exists(imya):
        with open(imya, 'r', encoding='utf-8') as f:
            return f.read()
    return None

def sortirovat_fajly(spisok, obratno=False):
    spisok.sort(key=str.lower, reverse=obratno)
    return spisok
