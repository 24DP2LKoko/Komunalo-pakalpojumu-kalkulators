def aprekinit_kopsummu(udens_maksa, elektribas_maksa, gazes_maksa, apkures_maksa):
    '''
    Funkcija aprekinit_kopsummu pieņem float tipa vērtību udens_maksa,
    float tipa vērtību elektribas_maksa, float tipa vērtību gazes_maksa un
    float tipa vērtību apkures_maksa un atgriež float tipa vērtību kopeja_summa
    '''

    kopeja_summa = udens_maksa + elektribas_maksa + gazes_maksa + apkures_maksa
    return round(kopeja_summa, 2)