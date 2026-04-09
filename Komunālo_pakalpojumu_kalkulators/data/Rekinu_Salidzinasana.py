from Datu_validacija import parbaudit_skaitli
from MaksajumuAprekins import aprekinit_pakalpojumu_maksu

def RekinuSalidzinasana(rekinu_saraksts):
    """
    funkcija RekinuSalidzinasana pieņem list tipa vērtību rekinu_saraksts un atgriež dict tipa vērtību salidzinajums
    """
    if len(rekinu_saraksts) < 2:
        raise ValueError("Kļūda: nepieciešami vismaz 2 rēķini.")

    salidzinajums = {}
    for i, rekins in enumerate(rekinu_saraksts):
        periods = rekins.get("periods", f"Periods {i + 1}")
        summa = 0
        
        for p in rekins.get("pakalpojumi", []):
            # Datu validācija pirms tālākā aprēķina
            paterins = parbaudit_skaitli(p["paterins"], "Patēriņš")
            tarifs = parbaudit_skaitli(p["tarifs"], "Tarifs")
            summa += aprekinit_pakalpojumu_maksu(paterins, tarifs)
            
        salidzinajums[periods] = round(summa, 2)

    return salidzinajums