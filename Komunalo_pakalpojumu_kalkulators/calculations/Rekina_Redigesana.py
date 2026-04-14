from Komunalo_pakalpojumu_kalkulators.calculations.rekini import rekini
from Komunalo_pakalpojumu_kalkulators.integrity.Datu_validacija import (
    parbaudit_tuksu_lauku,
    parbaudit_skaitli,
    parbaudit_datumu,
    parbaudit_veselu_skaitli,
    izveidot_periodu_no_datuma,
)


def rediget_rekinu():
    '''
    Funkcija rediget_rekinu pieņem None tipa vērtību
    un neatgriež vērtību
    '''

    print("=== Rēķina rediģēšana ===")

    id = parbaudit_veselu_skaitli(
        input("Ievadiet rēķina ID: "),
        "Rēķina ID"
    )

    for rekins in rekini:
        if rekins["id"] == id:
            print("Atrasts rēķins:")
            print(f"ID: {rekins['id']}")
            print(f"Veids: {rekins['veids']}")
            print(f"Summa: {rekins['summa']} EUR")
            print(f"Datums: {rekins['datums']}")
            print(f"Periods: {rekins['periods']}")

            jauns_veids = parbaudit_tuksu_lauku(
                input("Jauns pakalpojuma veids: "),
                "Komunālo pakalpojumu veids"
            )

            jauna_summa = parbaudit_skaitli(
                input("Jauna summa (EUR): "),
                "Summa"
            )

            jauns_datums = parbaudit_datumu(
                input("Jauns datums (YYYY-MM-DD): "),
                "Datums"
            )

            rekins["veids"] = jauns_veids
            rekins["summa"] = round(jauna_summa, 2)
            rekins["datums"] = jauns_datums
            rekins["periods"] = izveidot_periodu_no_datuma(jauns_datums)

            print("Rēķins veiksmīgi atjaunots!\n")
            return

    print("Rēķins nav atrasts.\n")