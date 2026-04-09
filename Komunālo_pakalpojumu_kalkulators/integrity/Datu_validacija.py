def __init__(self):
    pass

def parbaudit_skaitli(self, vertiba, lauka_nosaukums):
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

def parbaudit_tuksu_lauku(vertiba, lauka_nosaukums):
    '''
    Funkcija parbaudit_tuksu_lauku pieņem str tipa vērtību 
    vertiba un str tipa vērtību lauka_nosaukums un atgriež 
    str tipa vērtību vertiba
    '''

    if str(vertiba).strip() == "":
        raise ValueError(f"Kļūda: lauks '{lauka_nosaukums}' nedrīkst būt tukšs.")
    
    return str(vertiba).strip()

def parbaudit_epastu(vertiba, lauka_nosaukums):
    '''
    Funkcija parbaudit_epastu pieņem str tipa vērtību 
    vertiba un str tipa vērtību lauka_nosaukums un 
    atgriež str tipa vērtību vertiba
    '''

    vertiba = parbaudit_tuksu_lauku(vertiba, lauka_nosaukums)

    if "@" not in vertiba or "." not in vertiba:
        raise ValueError(f"Kļūda: laukā '{lauka_nosaukums}' jāievada derīgs e-pasts.")
    
    return vertiba