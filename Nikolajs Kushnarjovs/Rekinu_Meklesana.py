from rekini import rekini

def RekinuMeklesana():
  print("=== Meklēšana ===")
  
  atsl = input("Ievadiet meklējamo vārdu (veids vai datums): ").lower()
  
  atrasti = False
  
  for r in rekini:
      if atsl in r["veids"].lower() or atsl in r["datums"]:
          print(f"{r['id']} | {r['veids']} | {r['summa']} | {r['datums']}")
          atrasti = True
  
  if not atrasti:
      print("Nekas netika atrasts.\n")
