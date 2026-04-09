from Komunalo_pakalpojumu_kalkulators.calculations.rekini import rekini
def rekinu_apskate():
  print("ID | Veids | Summa | Datums")
  print("-----------------------------")

  for r in rekini:
    print(f"{r['id']} | {r['veids']} | {r['summa']} | {r['datums']}")
