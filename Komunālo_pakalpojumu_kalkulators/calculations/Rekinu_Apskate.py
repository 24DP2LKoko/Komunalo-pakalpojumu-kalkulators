from rekini import rekini
def RekinuApskate():
  print("ID | Veids | Summa | Datums")
  print("-----------------------------")

  for r in rekini:
    print(f"{r['id']} | {r['veids']} | {r['summa']} | {r['datums']}")
