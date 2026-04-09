from rekini import rekini

def RekinaDzesana():
  print("=== Rēķina dzēšana ===")

  id = int(input("Ievadiet rēķinu ID: "))
  for rekinis in rekini:
    if rekini[rekinis]["id"] == id:
      del rekini[rekinis]
      print("Dzēst!")
      return
  
  print("Nav atrasts!")
