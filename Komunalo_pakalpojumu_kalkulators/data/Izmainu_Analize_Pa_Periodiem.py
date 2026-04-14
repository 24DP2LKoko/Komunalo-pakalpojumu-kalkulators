def IzmainuAnalizePaPeriodiem(rekinu_saraksts):
    """
    funkcija IzmainuAnalizePaPeriodiem pieņem list tipa vērtību rekinu_saraksts
    un atgriež list tipa vērtību izmainu_saraksts
    """

    if not rekinu_saraksts:
        raise ValueError("Rēķinu saraksts ir tukšs.")

    periodu_summas = {}

    for rekins in rekinu_saraksts:
        periods = rekins.get("periods", "Nav norādīts")
        summa = round(float(rekins.get("summa", 0)), 2)

        if periods not in periodu_summas:
            periodu_summas[periods] = 0

        periodu_summas[periods] += summa
        periodu_summas[periods] = round(periodu_summas[periods], 2)

    sakartoti_periodi = sorted(periodu_summas.items())
    izmainu_saraksts = []
    iepriekseja_summa = None

    for periods, summa in sakartoti_periodi:
        if iepriekseja_summa is None:
            izmaina = "Nav salīdzinājuma"
            izmaina_procenti = "Nav salīdzinājuma"
        else:
            starpiba = round(summa - iepriekseja_summa, 2)

            if iepriekseja_summa != 0:
                procenti = round((starpiba / iepriekseja_summa) * 100, 2)
                izmaina_procenti = f"{procenti}%"
            else:
                izmaina_procenti = "Nav iespējams aprēķināt"

            if starpiba > 0:
                izmaina = f"+{starpiba}"
            elif starpiba < 0:
                izmaina = f"{starpiba}"
            else:
                izmaina = "0.0"

        izmainu_saraksts.append({
            "Periods": periods,
            "Kopējā summa": round(summa, 2),
            "Izmaiņa": izmaina,
            "Izmaiņa procentos": izmaina_procenti
        })

        iepriekseja_summa = summa

    return izmainu_saraksts