def parbaudit_skaitli(vertiba, lauka_nosaukums):
    '''
    Funkcija parbaudit_skaitli pieņem str tipa vērtību
    vertiba un str tipa vērtību lauka_nosaukums un
    atgriež float tipa vērtību vertiba
    '''
    if str(vertiba).strip() == "":
        raise ValueError(f"Kļūda: lauks '{lauka_nosaukums}' nedrīkst būt tukšs.")

    try:
        vertiba = float(vertiba)
    except ValueError:
        raise ValueError(f"Kļūda: laukā '{lauka_nosaukums}' jāievada skaitlis.")
    
    if vertiba < 0:
        raise ValueError(f"Kļūda: laukā '{lauka_nosaukums}' nevar būt negatīva vērtība.")

    return vertiba