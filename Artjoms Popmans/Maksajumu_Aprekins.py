from Kopsummas_Aprekins import aprekinit_kopsummu
from Datu_Validacija import parbaudit_skaitli

def aprekinit_pakalpojumu_maksu(paterins, tarifs):
    '''
    Funkcija aprekinit_pakalpojumu_maksu pieņem float 
    tipa vērtību paterins un float tipa vērtību tarifs
    '''

    maksa = paterins * tarifs
    return maksa

def aprekinit_komunalos_maksajumus(
    udens_paterins,
    udens_tarifs,
    elektribas_paterins,
    elektribas_tarifs,
    gazes_paterins,
    gazes_tarifs,
    apkures_paterins,
    apkures_tarifs
):
    '''
    Funkcija aprekinit_komunalos_maksajumus pieņem float
    tipa vērtības par patēriņiem un tarifiem un atgriež
    dict tipa vērtību rezultats
    '''

    udens_paterins = parbaudit_skaitli(udens_paterins, "Ūdens patēriņš")
    udens_tarifs = parbaudit_skaitli(udens_tarifs, "Ūdens tarifs")

    elektribas_paterins = parbaudit_skaitli(elektribas_paterins, "Elektrības patēriņš")
    elektribas_tarifs = parbaudit_skaitli(elektribas_tarifs, "Elektrības tarifs")

    gazes_paterins = parbaudit_skaitli(gazes_paterins, "Gāzes patēriņš")
    gazes_tarifs = parbaudit_skaitli(gazes_tarifs, "Gāzes tarifs")

    apkures_paterins = parbaudit_skaitli(apkures_paterins, "Apkures patēriņš")
    apkures_tarifs = parbaudit_skaitli(apkures_tarifs, "Apkures tarifs")

    udens_maksa = aprekinit_pakalpojumu_maksu(udens_paterins, udens_tarifs)
    elektribas_maksa = aprekinit_pakalpojumu_maksu(elektribas_paterins, elektribas_tarifs)
    gazes_maksa = aprekinit_pakalpojumu_maksu(gazes_paterins, gazes_tarifs)
    apkures_maksa = aprekinit_pakalpojumu_maksu(apkures_paterins, apkures_tarifs)

    kopa = aprekinit_kopsummu(
        udens_maksa,
        elektribas_maksa,
        gazes_maksa,
        apkures_maksa
    )

    rezultats = {
        "udens_maksa": round(udens_maksa, 2),
        "elektribas_maksa": round(elektribas_maksa, 2),
        "gazes_maksa": round(gazes_maksa, 2),
        "apkures_maksa": round(apkures_maksa, 2),
        "kopeja_summa": kopa
    }

    return rezultats
