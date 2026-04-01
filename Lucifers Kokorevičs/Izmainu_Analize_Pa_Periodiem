def IzmainuAnalizePaPeriodiem(rekinu_saraksts):
    """
    Funkcija IzmainuAnalizePaPeriodiem pieņem list tipa vērtību rekinu_saraksts
    un atgriež list tipa vērtību izmain_saraksts.

    Katrs elements sarakstā ir dict ar atslēgām:
        "periods"     - teksts, piemēram "2024-01"
        "pakalpojumi" - list ar dict elementiem, kur katram ir:
                        "veids", "paterins", "tarifs"

    Atgriežamais saraksts satur dict elementus ar:
        "periods"   - pašreizējais periods
        "summa"     - kopējā summa šajā periodā
        "izmaina"   - starpība salīdzinot ar iepriekšējo periodu (None pirmajam)
        "izmaina_%" - procentuālā izmaiņa (None pirmajam periodam)
    """
    if not rekinu_saraksts:
        raise ValueError("Kļūda: rēķinu saraksts ir tukšs.")

    izmain_saraksts = []
    iepriekšeja_summa = None

    for rekins in rekinu_saraksts:
        periods = rekins.get("periods", "Nav norādīts")

        # Aprēķina kopējo summu periodam
        kopeja_summa = round(
            sum(p["paterins"] * p["tarifs"] for p in rekins.get("pakalpojumi", [])),
            2
        )

        # Aprēķina izmaiņu salīdzinot ar iepriekšējo periodu
        if iepriekšeja_summa is None:
            izmaina = None
            izmaina_procenti = None
        else:
            izmaina = round(kopeja_summa - iepriekšeja_summa, 2)
            # Izvairās dalīt ar nulli
            if iepriekšeja_summa != 0:
                izmaina_procenti = round((izmaina / iepriekšeja_summa) * 100, 2)
            else:
                izmaina_procenti = None

        izmain_saraksts.append({
            "periods": periods,
            "summa": kopeja_summa,
            "izmaina": izmaina,
            "izmaina_%": izmaina_procenti
        })

        iepriekšeja_summa = kopeja_summa

    return izmain_saraksts
