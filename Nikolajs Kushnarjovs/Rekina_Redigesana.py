from rekini import rekini

def rediget_rekinu():
  print("=== Rēķina rediģēšana ===")

  id = int(input("Ievadiet rēķina ID: "))

  for rekins in rekini:
    if rekins["id"] == id:
      print("Atrasts rēķins:", rekins)
      rekins["veids"] = input("Jauns veids: ")
      rekins["summa"] = float(input("Jauna summa: "))
      rekins["datums"] = input("Jauns datums: ")
      
      print("Rēķins veiksmīgi atjaunots!\n")
      return

  print("Rēķins nav atrasts!\n")