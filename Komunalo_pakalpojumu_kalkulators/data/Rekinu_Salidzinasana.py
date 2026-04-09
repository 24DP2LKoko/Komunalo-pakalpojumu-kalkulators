def RekinuSalidzinasana(rekinu_saraksts):
    """
    funkcija RekinuSalidzinasana pieņem list tipa vērtību rekinu_saraksts un atgriež dict tipa vērtību salidzinajums
    """

    if len(rekinu_saraksts) < 2:
        raise ValueError("Kļūda: nepieciešami vismaz 2 rēķini.")

    salidzinajums = {}

    for i, rekins in enumerate(rekinu_saraksts):
        periods = rekins.get("periods", f"Periods {i + 1}")
        summa = round(float(rekins.get("summa", 0)), 2)

        if periods not in salidzinajums:
            salidzinajums[periods] = 0

        salidzinajums[periods] += summa
        salidzinajums[periods] = round(salidzinajums[periods], 2)

    return salidzinajums