def StatistikasGeneresana(rekinu_saraksts):
    """
    Pieņem list rekinu_saraksts, atgriež dict statistika.
    Satur: periodu_skaits, kopeja_summa, videja_summa, min/max summa un periods, pa_pakalpojumiem.
    """
    if not rekinu_saraksts:
        raise ValueError("Kļūda: rēķinu saraksts ir tukšs.")
    periodu_summas = {}
    pa_pakalpojumiem = {}

    for rekins in rekinu_saraksts:
        periods = rekins.get("periods", "Nav norādīts")
        periodu_summas[periods] = 0.0

        for p in rekins.get("pakalpojumi", []):
            veids = p.get("veids", "Nezināms")
            summa = round(p["paterins"] * p["tarifs"], 2)
            periodu_summas[periods] = round(periodu_summas[periods] + summa, 2)
            pa_pakalpojumiem[veids] = round(pa_pakalpojumiem.get(veids, 0) + summa, 2)

    summas = list(periodu_summas.values())
    kopeja = round(sum(summas), 2)

    return {
        "periodu_skaits":   len(summas),
        "kopeja_summa":     kopeja,
        "videja_summa":     round(kopeja / len(summas), 2),
        "min_summa":        min(summas),
        "max_summa":        max(summas),
        "min_periods":      min(periodu_summas, key=periodu_summas.get),
        "max_periods":      max(periodu_summas, key=periodu_summas.get),
        "pa_pakalpojumiem": pa_pakalpojumiem
    }
