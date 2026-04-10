def IzmainuAnalizePaPeriodiem(rekinu_saraksts):
    """
    funkcija IzmainuAnalizePaPeriodiem pieņem list tipa vērtību rekinu_saraksts un atgriež list tipa vērtību izmainu_saraksts
    """

    if not rekinu_saraksts:
        raise ValueError("Kļūda: rēķinu saraksts ir tukšs.")

    periodu_summas = {}

    for rekins in rekinu_saraksts:
        periods = rekins.get("periods", "Nav norādīts")
        summa = float(rekins.get("summa", 0))

        if periods not in periodu_summas:
            periodu_summas[periods] = 0

        periodu_summas[periods] += summa

    sakartoti_periodi = sorted(periodu_summas.items())
    izmainu_saraksts = []
    iepriekseja_summa = None

    for periods, summa in sakartoti_periodi:
        summa = round(summa, 2)

        if iepriekseja_summa is None:
            izmaina = None
            izmaina_procenti = None
        else:
            izmaina = round(summa - iepriekseja_summa, 2)

            if iepriekseja_summa != 0:
                izmaina_procenti = round((izmaina / iepriekseja_summa) * 100, 2)
            else:
                izmaina_procenti = None

        izmainu_saraksts.append({
            "periods": periods,
            "summa": summa,
            "izmaina": izmaina,
            "izmaina_%": izmaina_procenti
        })

        iepriekseja_summa = summa

    return izmainu_saraksts