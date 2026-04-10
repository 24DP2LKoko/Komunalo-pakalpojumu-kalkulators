# Komunalo-pakalpojumu-kalkulators

## Projekta apraksts

Šī sistēma ir komunālo pakalpojumu kalkulators, kas ļauj lietotājiem aprēķināt un pārvaldīt savus rēķinus. Sistēma nodrošina iespēju ievadīt patēriņu, aprēķināt maksājumus, kā arī saglabāt un apskatīt aprēķinu vēsturi.

## Funkcionalitāte

Sistēmā ir realizētas šādas funkcijas:

- Lietotāja reģistrācija (iedzīvotājs vai saimnieks)
- Lietotāja panelis ar galveno izvēlni
- Rēķina pievienošana
- Rēķina dzēšana
- Rēķinu apskate
- Rēķinu filtrēšana
- Rēķinu meklēšana
- Komunālo maksājumu aprēķins
- Kopsummas aprēķins
- Vidējā patēriņa aprēķins
- Automātiska aprēķinu atjaunošana
- Aprēķinu saglabāšana datubāzē

## Izmantotas tehnoloģijas

- Programmēšanas valoda: Python
- Izstrādes vide: Visual Studio Code
- Datu bāze: MySQL
- Versiju kontrole: GitHub
- Darba organizēšana: Trello

## Datu bāze

Sistēma izmanto MySQL datubāzi, kurā tiek glabāti:
- lietotāju dati
- rēķini
- aprēķinu vēsture

## Nepieciešamības

Pirms projektu var palaist ir jāparbauda vai visi no šiem punktiem ir izpildīti:
1. Instalēt jaunāko python versiju uz sava datora
2. Nodrošināties, ka kopā ar python ir arī instalēta pip sistēma izmantojot komandu `pip help`, ja komanda izvada kļūdu instalēt pip uz sava datora izmantojot `python3 get-pip.py` ja lietotājs izmanto Windows vai MacOS, `$ sudo apt install python3-pip` ja lietotājs izmanto linux operētājsistmēmu
3. Instalēt MySql konektoru, PDF un xlsx novertētājus izmantojot komandu `$ pip install mysql-connector-python openyxl fpdf`

## Kā palaist projektu

1. Lejuplādēt projektu no GitHub 
2. Izvilkt saspiestos failus
4. Palaist galveno failu Main.py no izvilktās mapes:
```bash
python Main.py
```

