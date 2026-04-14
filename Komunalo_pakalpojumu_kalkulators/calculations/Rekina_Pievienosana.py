from Komunalo_pakalpojumu_kalkulators.calculations.rekini import rekini
from Komunalo_pakalpojumu_kalkulators.integrity.Datu_validacija import (
    parbaudit_tuksu_lauku,
    parbaudit_skaitli,
    parbaudit_datumu,
    izveidot_periodu_no_datuma,
)


def pievienot_rekinu():
    '''
    Funkcija pievienot_rekinu pieņem None tipa vērtību
    un neatgriež vērtību
    '''

    id = len(rekini) + 1
    print("=== Jauna rēķina pievienošana ===")

    veids = parbaudit_tuksu_lauku(
        input("Ievadiet pakalpojuma veidu: "),
        "Komunālo pakalpojumu veids"
    )

    summa = parbaudit_skaitli(
        input("Ievadiet summu (EUR): "),
        "Summa"
    )

    datums = parbaudit_datumu(
        input("Ievadiet datumu (YYYY-MM-DD): "),
        "Datums"
    )

    periods = izveidot_periodu_no_datuma(datums)

    rekins = {
        "id": id,
        "veids": veids,
        "summa": round(summa, 2),
        "datums": datums,
        "periods": periods
    }

    rekini.append(rekins)

    print(f"Rēķins veiksmīgi pievienots. Rēķina ID: {id}\n")