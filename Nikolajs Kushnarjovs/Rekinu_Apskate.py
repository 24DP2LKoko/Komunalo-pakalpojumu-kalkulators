from Rekina_Pievienosana import pievienot_rekinu

def RekinuApskate():
  print("ID | Veids | Summa | Datums")
  print("-----------------------------")

  for i in rekini:
    print(f"{r['id']} | {r['veids']} | {r['summa']} | {r['datums']}")
