import re
from datetime import datetime


def parbaudit_tuksu_lauku(vertiba, lauka_nosaukums):
    '''
    Funkcija parbaudit_tuksu_lauku pieņem str tipa vērtību vertiba un str tipa vērtību lauka_nosaukums
    un atgriež str tipa vērtību vertiba
    '''

    if str(vertiba).strip() == "":
        raise ValueError(f"Lauks '{lauka_nosaukums}' nedrīkst būt tukšs.")

    return str(vertiba).strip()


def parbaudit_skaitli(vertiba, lauka_nosaukums):
    '''
    Funkcija parbaudit_skaitli pieņem str tipa vērtību vertiba un str tipa vērtību lauka_nosaukums
    un atgriež float tipa vērtību vertiba
    '''

    vertiba = parbaudit_tuksu_lauku(vertiba, lauka_nosaukums)

    try:
        vertiba = float(vertiba)
    except ValueError:
        raise ValueError(f"Laukā '{lauka_nosaukums}' jāievada skaitlis.")

    if vertiba < 0:
        raise ValueError(f"Laukā '{lauka_nosaukums}' nevar būt negatīva vērtība.")

    return vertiba


def parbaudit_veselu_skaitli(vertiba, lauka_nosaukums):
    '''
    Funkcija parbaudit_veselu_skaitli pieņem str tipa vērtību vertiba un str tipa vērtību lauka_nosaukums
    un atgriež int tipa vērtību vertiba
    '''

    vertiba = parbaudit_tuksu_lauku(vertiba, lauka_nosaukums)

    try:
        if "." in vertiba:
            raise ValueError
        vertiba = int(vertiba)
    except ValueError:
        raise ValueError(f"Laukā '{lauka_nosaukums}' jāievada vesels skaitlis.")

    if vertiba < 0:
        raise ValueError(f"Laukā '{lauka_nosaukums}' nevar būt negatīva vērtība.")

    return vertiba


def parbaudit_epastu(vertiba, lauka_nosaukums):
    '''
    Funkcija parbaudit_epastu pieņem str tipa vērtību vertiba un str tipa vērtību lauka_nosaukums
    un atgriež str tipa vērtību vertiba
    '''

    vertiba = parbaudit_tuksu_lauku(vertiba, lauka_nosaukums)

    epasta_paraugs = r'^[^@\s]+@[^@\s]+\.[^@\s]+$'

    if not re.match(epasta_paraugs, vertiba):
        raise ValueError(f"Laukā '{lauka_nosaukums}' jāievada derīgs e-pasts.")

    return vertiba


def parbaudit_personas_kodu(vertiba, lauka_nosaukums):
    '''
    Funkcija parbaudit_personas_kodu pieņem str tipa vērtību vertiba un str tipa vērtību lauka_nosaukums
    un atgriež str tipa vērtību vertiba
    '''

    vertiba = parbaudit_tuksu_lauku(vertiba, lauka_nosaukums)

    personas_koda_paraugs = r'^\d{6}-\d{5}$'

    if not re.match(personas_koda_paraugs, vertiba):
        raise ValueError(f"Laukā '{lauka_nosaukums}' jāievada personas kods formātā XXXXXX-XXXXX.")

    return vertiba


def parbaudit_datumu(vertiba, lauka_nosaukums):
    '''
    Funkcija parbaudit_datumu pieņem str tipa vērtību vertiba un str tipa vērtību lauka_nosaukums
    un atgriež str tipa vērtību vertiba
    '''

    vertiba = parbaudit_tuksu_lauku(vertiba, lauka_nosaukums)

    try:
        datetime.strptime(vertiba, "%Y-%m-%d")
    except ValueError:
        raise ValueError(f"Laukā '{lauka_nosaukums}' jāievada datums formātā YYYY-MM-DD.")

    return vertiba


def izveidot_periodu_no_datuma(datums):
    '''
    Funkcija izveidot_periodu_no_datuma pieņem str tipa vērtību datums
    un atgriež str tipa vērtību periods
    '''

    datums = parbaudit_datumu(datums, "Datums")
    periods = datums[:7]
    return periods