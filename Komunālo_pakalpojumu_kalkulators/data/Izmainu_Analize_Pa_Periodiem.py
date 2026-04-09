from MaksajumuAprekins import aprekinit_pakalpojumu_maksu

def IzmainuAnalizePaPeriodiem(rekinu_saraksts):
    """
    funkcija IzmainuAnalizePaPeriodiem pieņem list tipa vērtību rekinu_saraksts un atgriež list tipa vērtību izmainu_saraksts
    """
    if not rekinu_saraksts:
        raise ValueError("Kļūda: rēķinu saraksts ir tukšs.")

    izmainu_saraksts = []
    iepriekseja_summa = None

    for rekins in rekinu_saraksts:
        periods = rekins.get("periods", "Nav norādīts")
        
        # Aprēķina kopējo summu konkrētajam periodam
        kopeja_summa = 0
        for p in rekins.get("pakalpojumi", []):
            kopeja_summa += aprekinit_pakalpojumu_maksu(p["paterins"], p["tarifs"])
        kopeja_summa = round(kopeja_summa, 2)

        # Nosaka izmaiņas pret iepriekšējo periodu (ja tas pastāv)
        if iepriekseja_summa is None:
            izmaina = None
            izmaina_procenti = None
        else:
            izmaina = round(kopeja_summa - iepriekseja_summa, 2)
            izmaina_procenti = round((izmaina / iepriekseja_summa) * 100, 2) if iepriekseja_summa != 0 else None

        izmainu_saraksts.append({
            "periods": periods,
            "summa": kopeja_summa,
            "izmaina": izmaina,
            "izmaina_%": izmaina_procenti
        })
        iepriekseja_summa = kopeja_summa

    return izmainu_saraksts