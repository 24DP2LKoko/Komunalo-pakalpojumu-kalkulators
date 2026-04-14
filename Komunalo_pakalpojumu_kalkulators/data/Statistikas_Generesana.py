from Komunalo_pakalpojumu_kalkulators.integrity.Videja_paterina_aprekins import aprekinit_videjo_paterinu


def StatistikasGeneresana(rekinu_saraksts):
    """
    funkcija StatistikasGeneresana pieņem list tipa vērtību rekinu_saraksts
    un atgriež dict tipa vērtību statistika
    """

    if not rekinu_saraksts:
        raise ValueError("Rēķinu saraksts ir tukšs.")

    periodu_summas = {}
    izdevumi_pa_pakalpojumu_veidiem = {}

    for rekins in rekinu_saraksts:
        periods = rekins.get("periods", "Nav norādīts")
        veids = rekins.get("veids", "Nezināms")
        summa = round(float(rekins.get("summa", 0)), 2)

        if periods not in periodu_summas:
            periodu_summas[periods] = 0

        periodu_summas[periods] += summa
        periodu_summas[periods] = round(periodu_summas[periods], 2)

        if veids not in izdevumi_pa_pakalpojumu_veidiem:
            izdevumi_pa_pakalpojumu_veidiem[veids] = 0

        izdevumi_pa_pakalpojumu_veidiem[veids] += summa
        izdevumi_pa_pakalpojumu_veidiem[veids] = round(izdevumi_pa_pakalpojumu_veidiem[veids], 2)

    summas = list(periodu_summas.values())

    kopeja_summa = round(sum(summas), 2)
    videja_summa = round(aprekinit_videjo_paterinu(summas), 2)
    minimala_summa = round(min(summas), 2)
    maksimala_summa = round(max(summas), 2)

    periods_ar_mazako_summu = min(periodu_summas, key=periodu_summas.get)
    periods_ar_lielako_summu = max(periodu_summas, key=periodu_summas.get)

    statistika = {
        "Periodu skaits": len(summas),
        "Kopējā summa": kopeja_summa,
        "Vidējā summa": videja_summa,
        "Mazākā summa": minimala_summa,
        "Lielākā summa": maksimala_summa,
        "Periods ar mazāko summu": periods_ar_mazako_summu,
        "Periods ar lielāko summu": periods_ar_lielako_summu,
        "Izdevumi pa pakalpojumu veidiem": izdevumi_pa_pakalpojumu_veidiem
    }

    return statistika