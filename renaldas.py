krepselis = []


# Produktu menu
mesos_gaminiai = {"jautiena", "kiauliena", "vistiena"}
darzoves = {"brokolis", "morkos", "pomidorai"}
pieno = {"jogurtas", "pienas", "sūris"}

# Produktu aprasymas
jautiena = {"produktas" : "jautiena", "Kaina": 15.99, "Kcal": 250, "Galiojimo laikas": "2023-04-30"}
kiauliena = {"produktas" : "vistiena", "Kaina": 10.99, "Kcal": 200, "Galiojimo laikas": "2023-04-25"}
vistiena = {"produktas" : "kiauliena", "Kaina": 12.99, "Kcal": 220, "Galiojimo laikas": "2023-04-27"}

brokolis = {"produktas" : "morkos", "Kaina": 2.99, "Kcal": 50, "Galiojimo laikas": "2023-04-26"}
morkos = {"produktas" : "brokolis", "Kaina": 3.99, "Kcal": 70, "Galiojimo laikas": "2023-04-28"}
pomidorai = {"produktas" : "pomidorai", "Kaina": 1.99, "Kcal": 30, "Galiojimo laikas": "2023-04-23"}

jogurtas = {"produktas" : "pienas", "Kaina": 1.99, "Kcal": 120, "Galiojimo laikas": "2023-04-25"}
pienas = {"produktas" : "sūris", "Kaina": 3.99, "Kcal": 150, "Galiojimo laikas": "2023-04-28"}
sūris = {"produktas" : "jogurtas", "Kaina": 2.99, "Kcal": 100, "Galiojimo laikas": "2023-05-01"}

# Produktu list'as
produktai = [jautiena, vistiena, kiauliena, morkos, brokolis, pomidorai, pienas, sūris, jogurtas]

while True:
    print("Pasirinkite gaminį:")
    print("1 - Mesos gaminiai")
    print("2 - Daržovės")
    print("3 - Pieno gaminiai")
    print("4 - Rodyti krepseli")
    print("0 - Baigti")
    
    pasirinkimas = input("Įveskite pasirinkimo numerį: ")
    
    if pasirinkimas == "1":
        print(f"Tu pasirinkai mesos gaminius: {mesos_gaminiai}")
        antras_pasirinkimas = input("Pasirinkite (1-3) arba 0, jei nenorite nieko pasirinkti: ")
        
        if antras_pasirinkimas == "0":
            break
        elif antras_pasirinkimas == "4":
            print(f"Tavo krepselis: {krepselis}")
           

        elif antras_pasirinkimas in {"1", "2", "3"}:
            print(f"Tu pasirinkai: {list(mesos_gaminiai)[int(antras_pasirinkimas) - 1]}")
            trecias_pasirinkimas = input("1 - ideti i krepseli, 2 - isimti is krepselio: ")
            if trecias_pasirinkimas == "1":
                krepselis.append(vistiena)
                print(f"Tavo krepselyje yra {krepselis} produktai.")

            else:
                 print("Neteisingas pasirinkimo numeris. Bandykite dar kartą.")

                 




