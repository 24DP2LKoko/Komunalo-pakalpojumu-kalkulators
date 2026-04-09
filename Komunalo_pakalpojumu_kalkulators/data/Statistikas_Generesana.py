from Komunalo_pakalpojumu_kalkulators.integrity.Videja_paterina_aprekins import aprekinit_videjo_paterinu


def StatistikasGeneresana(rekinu_saraksts):
    """
    funkcija StatistikasGeneresana pieņem list tipa vērtību rekinu_saraksts un atgriež dict tipa vērtību statistika
    """

    if not rekinu_saraksts:
        raise ValueError("Kļūda: rēķinu saraksts ir tukšs.")

    periodu_summas = {}
    pa_pakalpojumiem = {}

    for rekins in rekinu_saraksts:
        periods = rekins.get("periods", "Nav norādīts")
        veids = rekins.get("veids", "Nezināms")
        summa = round(float(rekins.get("summa", 0)), 2)

        if periods not in periodu_summas:
            periodu_summas[periods] = 0

        periodu_summas[periods] += summa
        periodu_summas[periods] = round(periodu_summas[periods], 2)

        if veids not in pa_pakalpojumiem:
            pa_pakalpojumiem[veids] = 0

        pa_pakalpojumiem[veids] += summa
        pa_pakalpojumiem[veids] = round(pa_pakalpojumiem[veids], 2)

    summas = list(periodu_summas.values())
    kopeja_summa = round(sum(summas), 2)
    videja_summa = aprekinit_videjo_paterinu(summas)

    statistika = {
        "periodu_skaits": len(summas),
        "kopeja_summa": kopeja_summa,
        "videja_summa": videja_summa,
        "min_summa": min(summas),
        "max_summa": max(summas),
        "min_periods": min(periodu_summas, key=periodu_summas.get),
        "max_periods": max(periodu_summas, key=periodu_summas.get),
        "pa_pakalpojumiem": pa_pakalpojumiem
    }

    return statistika