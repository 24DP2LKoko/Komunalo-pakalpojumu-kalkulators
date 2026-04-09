from integrity.Datu_validacija import parbaudit_skaitli

def aprekinit_videjo_paterinu(paterinu_saraksts):
    '''
    Funkcija aprekinit_videjo_paterinu pieņem list tipa
    vērtību paterinu_saraksts un atgriež float tipa vērtību
    videjais_paterins
    '''

    if len(paterinu_saraksts) == 0:
        raise ValueError("Kļūda: patēriņu saraksts ir tukšs.")
    
    summa = 0

    for i, vertiba in enumerate(paterinu_saraksts):
        parbaudit_vertejums = parbaudit_skaitli(vertiba, f"Patēriņš #{i + 1}")
        summa += parbaudit_vertejums
    
    videjais_paterins = summa / len(paterinu_saraksts)

    return round(videjais_paterins, 2)