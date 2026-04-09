from MaksajumuAprekins import aprekinit_pakalpojumu_maksu

def DatuAttelosanaGrafikos(rekinu_saraksts):
    """
    funkcija DatuAttelosanaGrafikos pieņem list tipa vērtību rekinu_saraksts un atgriež None tipa vērtību None
    """
    if not rekinu_saraksts:
        raise ValueError("Kļūda: rēķinu saraksts ir tukšs.")

    # ASCII tabulu uz ekrāna
    print(f"{'Periods':<15} | {'Kopējā summa (EUR)':<20}")
    print("-" * 38)

    for rekins in rekinu_saraksts:
        periods = rekins.get("periods", "?")
        summa = 0
        for p in rekins.get("pakalpojumi", []):
            # Integrējam funkciju no aprēķinu apakšsistēmas
            maksa = aprekinit_pakalpojumu_maksu(p["paterins"], p["tarifs"])
            summa += maksa
            
        print(f"{periods:<15} | {round(summa, 2):<20}")