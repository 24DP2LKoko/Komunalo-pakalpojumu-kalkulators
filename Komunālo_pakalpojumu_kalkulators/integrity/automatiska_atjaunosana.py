from integrity.MaksajumuAprekins import aprekinit_komunalos_maksajumus

def atjaunot_aprekinu(
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
    Funkcija atjaunot_aprekinu pieņem float tipa vērtības par
    patēriņiem un tarifiem un atgriež dict tipa vērtību rezultats
    '''

    rezultats = aprekinit_komunalos_maksajumus(
        udens_paterins,
        udens_tarifs,
        elektribas_paterins,
        elektribas_tarifs,
        gazes_paterins,
        gazes_tarifs,
        apkures_paterins,
        apkures_tarifs
    )

    return rezultats