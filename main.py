
# TODO 
## grazus zodis
#1 pakeisti produktu sarasuose esancius produktus is str() tipo i list() tipa,
# list tipo produktai turetu buti surasyti sitaip ["produkto_pavadinimas", kaina, "maistine_verte", "galiojimo_data"]
#pavizdys: buves produktas 'karpio kapotinis', dabar turi tapti ['karpio kapotinis', 6.99(kaina sugalvokit patys, svarbu kad elementas butu float tipo), "800kcal"(maistine verte sugalvokit patys svarbu str() tipas), "2023-06-16"(data sugalvokit patys, svarbu str() tipas)]

#sutvarkyti programos 1-ojo pasirinkimo meniu:
# 1 pasirinkimas daugmaz sutvarkytas, galima naudoti kaip pvz uzduociai atlikti

# prideti logikos i 2-aji programos pasirinkima
# pagal aprasyta meniu

# prideti 3-aji programos pasirinkima. 

# sutvarkyti programos estetika, taisyti tekstines klaidas

# visu produktu sarasai.

pirkiniai = []

<<<<<<< HEAD
zuvies_produktai =[['silke surime', 14.99, '500kcal', '2023-05-16'], ['karpio kapotinis', 14.99, '500kcal', '2023-05-16'],\
                   ['juros eserys', 14.99, '500kcal', '2023-05-16'], ['menkes vyniotinis', 14.99, '500kcal', '2023-05-16'],\
                   ['lydekaite', 14.99, '500kcal', '2023-05-16'], ['lasisos file', 14.99, '500kcal', '2023-05-16'],\
                   ['koldunai su karosu', 14.99, '500kcal', '2023-05-16']]
=======





zuvies_produktai =[
    ['silke surime', 11.11, 500, '2021-04-16'], ['karpio kapotinis', 1.22, 121, '1999-12-01'],\
    ['juros eserys', 23.45, 21, '2020-06-11'], ['menkes vyniotinis', 15.01, 22, '2022-01-01'],\
    ['lydekaite', 100.01, 111, '2023-12-22'], ['lasisos file', 23.89, 333, '2020-10-11'],\
    ['koldunai su karosu', 1.59, 70, '2021-05-29']
    ]
>>>>>>> ab20772673740f35a8588a96f039c7de8eab44af

pieno_produktai = [
    ['pienas', 1.20, 10, '2022-01-11'], ['surelis', 0.58, 15, '1999-04-11'], ['varske', 1.95, 45, '2020-04-01'],\
    ['jogurtas', 1.00, 55, '2023-07-05'], ['suris', 5.51, 121, '2022-09-10'], ['majonezas', 1.10, 166, '2020-12-23'],\
    ['sviestas', 5.45, 621, '2022-01-11'], ['grietine', 4.99, 91, '2022-07-07'], ['grietinele', 0.99, 15, '2023-03-11'],\
    ['kefyras', 1.10, 42, '2022-11-01']
    ]

miltiniai_produktai = [
    ['kvieciu miltai', 1.11, 220, '2030-03-30'], ['rugiu miltai', 2.23, 10, '2022-11-30'],\
    ['kukuruzu miltai', 0.87, 111, '2020-01-29'], ['ryziu miltai', 5.47, 150, '2022-10-03'],\
    ['makaronai penne', 1.49, '350kcal', '2024-01-30'], ['bociu duona', 1.49, '350kcal', '2024-01-30'], \
    ['kruasanas', 1.22, 198, '2025-05-22'], ['meduoliai', 11.87, 987, '1999-01-14'],\
    ['krekeriai' , 0.87, 12, '2021-06-10'], ['virtinukai "Dziaugsmas"', 6.87, 283, '2022-08-30'],\
    ['saldyti varskeciai', 158.60, 201, '2020-11-06']
    ]

<<<<<<< HEAD
darzoves = [['pomidorai', 3.99, '100kcal', '2023-05-16'], ['pupeles', 3.99, '500kcal', '2023-05-16'], ['bulves', 3.99, '500kcal', '2023-05-16'],\
                   ['agurkai', 3.99, '500kcal', '2023-05-16'], ['baklazanai', 3.99, '500kcal', '2023-05-16'], ['paprikos', 3.99, '500kcal', '2023-05-16'],\
                   ['pievagrybiai', 3.99, '500kcal', '2023-05-16'], ['kopustas', 3.99, '500kcal', '2023-05-16'], ['salotos', 3.99, '500kcal', '2023-05-16'],\
                   ['pipirai', 3.99, '500kcal', '2023-05-16']]
=======
darzoves = [
    ['pomidorai', 1.99, 200, '2023-04-28'], ['pupeles', 2.99, 350, '2023-05-01'], ['bulves', 1.49, 150, '2024-04-17'],\
    ['agurkai', 1.99, 200, '2023-05-02'], ['baklazanai', 2.99, 200, '2023-05-11'], ['paprikos', 1.99, 400, '2023-07-16'],\
    ['pievagrybiai', 2.99, 150, '2024-06-07'], ['kopustas', 150, 100, '2023-09-26'], ['salotos', 2.79, 280, '2023-05-10'],\
    ['pipirai', 1.49, 50, '2025-04-17']
    ]
>>>>>>> ab20772673740f35a8588a96f039c7de8eab44af

#Milda
{"kaina": None, "maistine_verte": None, "galiojimo_data": None}
produktu_info = {
    "zuvies_produktai": { str(zuvies_produktai[zuvies_produktas][0]):{"kaina": zuvies_produktai[zuvies_produktas][1], "maistine_verte": zuvies_produktai[zuvies_produktas][2], "galiojimo_data": zuvies_produktai[zuvies_produktas][3]} for zuvies_produktas in range(len(zuvies_produktai))},
    "pieno_produktai": { str(pieno_produktai[pieno_produktas][0]):{"kaina": pieno_produktai[pieno_produktas][1], "maistine_verte": pieno_produktai[pieno_produktas][2], "galiojimo_data": pieno_produktai[pieno_produktas][3]} for pieno_produktas in range(len(pieno_produktai))},
<<<<<<< HEAD
    "miltiniai_produktai": { str(miltiniai_produktai[miltiniai_produktai][0]):{"kaina": miltiniai_produktai[miltiniai_produktai][1], "maistine_verte": miltiniai_produktai[miltiniai_produktai][2], "galiojimo_data": miltiniai_produktai[miltiniai_produktai][3]} for miltiniai_produktai in range(len(miltiniai_produktai))},
    "darzoves": { str(darzoves[darzoves][0]):{"kaina": darzoves[darzoves][1], "maistine_verte": darzoves[darzoves][2], "galiojimo_data": darzoves[darzoves][3]} for darzoves in range(len(darzoves))}
=======
    "miltiniai_produktai": { str(miltiniai_produktai[miltinis_produktas][0]):{"kaina": miltiniai_produktai[miltinis_produktas][1], "maistine_verte": miltiniai_produktai[miltinis_produktas][2], "galiojimo_data": miltiniai_produktai[miltinis_produktas][3]} for miltinis_produktas in range(len(miltiniai_produktai))},
    "darzoves": { str(darzoves[darzove][0]):{"kaina": darzoves[darzove][1], "maistine_verte": darzoves[darzove][2], "galiojimo_data": darzoves[darzove][3]} for darzove in range(len(darzoves))}
>>>>>>> ab20772673740f35a8588a96f039c7de8eab44af
}

#meniu

while True:
    print(
        """
    Sveiki, jus naudojates programa sudaryti pirkiniu krepseliui.
    Pasirinkite funkcija:    
    1 - Pasirinkti produkta i pirkiniu krepseli
<<<<<<< HEAD
    2 - Perziureti pirkiniu krepseli
    3 - Perziureti produkto kaina
    4 - Perziureti produkto kcal
    5 - Perziureti produkto galiojimo laika
=======
    2 - apziureti pirkiniu krepseli
    
>>>>>>> ab20772673740f35a8588a96f039c7de8eab44af
    0 - Iseiti is programos

    """    
    )
    try:
        choice = int(input("Pasirinkite norima operacija (1-5 arba 0) :"))
    except:
        print("Pasirinkite norima funkcija")
        continue

    if choice == 1:
        print('Produktai:')
        print('1 - Zuvies produktai:')
        print('2 - Pieno produktai:')
        print('3 - Miltiniai produktai:')
        print('4 - Darzoves:')
        pasirinktas_produktas = int(input('Pasirinkite produkto kategorija 1, 2, 3 arba 4:'))
        
        if pasirinktas_produktas == 1:
            print('Pasirinkite produkta is saraso:')
            for i in range(len(zuvies_produktai)):
                print(f"nr: {i+1} - {zuvies_produktai[i][0]}")

            produkto_index = int(input('Pasirinkite produkta is saraso:'))
            if produkto_index - 1 in range(len(zuvies_produktai)):                         
            
                pirkiniai.append(zuvies_produktai[produkto_index - 1][0])
                print(f"Produktas {zuvies_produktai[produkto_index - 1][0]} itrauktas i pirkiniu krepseli.")
                
        
        
        elif pasirinktas_produktas == 2:
            print('Pasirinkite produkta is saraso:')
            for i in range(len(pieno_produktai)):
<<<<<<< HEAD
                print(f"{i+1} - {pieno_produktai[i]}")
                produkto_index = int(input('Pasirinkite produkto numeri:'))
                pasirinktas_produktas = pieno_produktai[produkto_index-1]
                pirkiniai.append(pasirinktas_produktas)
                print(f"Produktas {pieno_produktai[produkto_index-1]} itrauktas i pirkiniu krepseli.")
=======
                print(f"nr: {i+1} - {pieno_produktai[i][0]}")
            produkto_index = int(input('Iveskite produkto numeri:'))
            if produkto_index - 1 in range(len(pieno_produktai)):

                # pasirinktas_produktas = pieno_produktai[produkto_index-1]
                pirkiniai.append(pieno_produktai[produkto_index - 1][0])
                print(f"Produktas {pieno_produktai[produkto_index - 1][0]} itrauktas i pirkiniu krepseli.")
>>>>>>> ab20772673740f35a8588a96f039c7de8eab44af

        
        
        elif pasirinktas_produktas == 3:
            print('Pasirinkite produkta is saraso:')
            for i in range(len(miltiniai_produktai)):
<<<<<<< HEAD
                print(f"{i+1} - {miltiniai_produktai[i]}")
                produkto_index = int(input('Pasirinkite produkto numeri:'))
                pasirinktas_produktas = miltiniai_produktai[produkto_index-1]
                pirkiniai.append(pasirinktas_produktas)
                print(f"Produktas {miltiniai_produktai[produkto_index-1]} itrauktas i pirkiniu krepseli.")
=======
                print(f"nr: {i+1} - {miltiniai_produktai[i][0]}")
            produkto_index = int(input('Iveskite produkto numeri:'))
            if produkto_index - 1 in range(len(miltiniai_produktai)):

                # pasirinktas_produktas = pieno_produktai[produkto_index-1]
                pirkiniai.append(miltiniai_produktai[produkto_index - 1][0])
                print(f"Produktas {miltiniai_produktai[produkto_index - 1][0]} itrauktas i pirkiniu krepseli.")
        
        elif pasirinktas_produktas == 4:
            print('Pasirinkite produkta is saraso:')
            for i in range(len(darzoves)):
                print(f"nr: {i+1} - {darzoves[i][0]}")
            produkto_index = int(input('Iveskite produkto numeri:'))

            if produkto_index - 1 in range(len(darzoves)):

                pirkiniai.append(darzoves[produkto_index - 1][0])
                print(f"Produktas {darzoves[produkto_index - 1][0]} itrauktas i pirkiniu krepseli.")
>>>>>>> ab20772673740f35a8588a96f039c7de8eab44af
    
    elif choice == 2:
        for pirkinys in pirkiniai:
            print(f"nr: {pirkiniai.index(pirkinys) +1} - {pirkinys}")
        print("""
        Ka norite daryti su pirkiniu krepseliu ?
        1 - Pasalinti produkta is krepselio
        2 - Parodyti produkto info
        0 - Grizti i meniu
        
        """)
        choice = int(input('Jusu pasirinkimas: '))
        if choice == 1:
<<<<<<< HEAD
            # pirkiniai.pop(produkto_pavadinimas)
            pass
 #Milda       
=======
            for i in range(len(pirkiniai)):
                print(f"nr: {i+1} - {pirkiniai[i]}")
            pirkiniu_krepselis = int(input('Iveskite produkto numeri produkto kuri norite istrinti:'))
            pirkiniai.pop(pirkiniu_krepselis - 1)
        
>>>>>>> ab20772673740f35a8588a96f039c7de8eab44af
        elif choice == 2:
            visa_maist_verte = 0
            visa_kaina = 0
            for pirkinys in pirkiniai:
                for pirkinio_tipas in produktu_info.values():
                    if pirkinys in pirkinio_tipas:
                        print(f"{pirkinys} - Kaina: {pirkinio_tipas.get(pirkinys).get('kaina')},\
<<<<<<< HEAD
 Maistine verte: {pirkinio_tipas.get(pirkinys).get('maistine_verte')},\
 Galiojimo data: {pirkinio_tipas.get(pirkinys).get('galiojimo_data')}") # logika gauti pirkinio value
                galutine_krepselio_suma = 0
                for pirkinys in galutine_krepselio_suma(0, len(pirkiniai)):
                    suma = suma + pirkiniai[pirkinys]

=======
 Maistine Verte: {pirkinio_tipas.get(pirkinys).get('maistine_verte')},\
 Galiojimo data: {pirkinio_tipas.get(pirkinys).get('galiojimo_data')}")
                        visa_kaina += pirkinio_tipas.get(pirkinys).get('kaina')
                        visa_maist_verte += pirkinio_tipas.get(pirkinys).get('maistine_verte')
            print(f"Visa kaina: {visa_kaina}, Visa maistine verte: {visa_maist_verte}")# logika gauti pirkinio value
>>>>>>> ab20772673740f35a8588a96f039c7de8eab44af
        
        elif choice <= 0 or choice > 2:
            continue
    


    elif choice == 0:
        break
    else:
        if choice > 3 or choice < 0:
            print("invalid choice")
            continue
