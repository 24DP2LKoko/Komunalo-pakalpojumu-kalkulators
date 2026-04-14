from Komunalo_pakalpojumu_kalkulators.calculations.rekini import rekini
from Komunalo_pakalpojumu_kalkulators.integrity.Datu_validacija import (
    parbaudit_tuksu_lauku,
    parbaudit_skaitli,
    parbaudit_datumu,
)


def filtre_rekinus():
    '''
    Funkcija filtre_rekinus pieņem None tipa vērtību
    un neatgriež vērtību
    '''

    print("=== Filtrēšana ===")

    veids = input("Veids (Enter = izlaist): ").strip()
    summa = input("Maksimālā summa (EUR) (Enter = izlaist): ").strip()
    datums = input("Datums (YYYY-MM-DD) (Enter = izlaist): ").strip()

    if veids != "":
        veids = parbaudit_tuksu_lauku(veids, "Veids")

    if summa != "":
        summa = parbaudit_skaitli(summa, "Maksimālā summa")

    if datums != "":
        datums = parbaudit_datumu(datums, "Datums")

    rezultati = []

    for r in rekini:
        if veids and r["veids"].lower() != veids.lower():
            continue

        if summa != "" and r["summa"] > summa:
            continue

        if datums and r["datums"] != datums:
            continue

        rezultati.append(r)

    if rezultati:
        print("\n=== ATRASTIE RĒĶINI ===")
        print("-" * 72)
        print(f"{'ID':<5} {'Veids':<20} {'Summa (EUR)':<15} {'Datums':<12} {'Periods':<10}")
        print("-" * 72)

        for r in rezultati:
            print(f"{r['id']:<5} {r['veids']:<20} {r['summa']:<15} {r['datums']:<12} {r['periods']:<10}")

        print("-" * 72)
    else:
        print("Nav atrasti rēķini.")