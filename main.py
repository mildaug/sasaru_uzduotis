
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

zuvies_produktai =[['silke surime', 14.99, '500kcal', '2023-05-16'], ['karpio kapotinis', 14.99, '500kcal', '2023-05-16'],\
                   ['juros eserys', 14.99, '500kcal', '2023-05-16'], ['menkes vyniotinis', 14.99, '500kcal', '2023-05-16'],\
                   ['lydekaite', 14.99, '500kcal', '2023-05-16'], ['lasisos file', 14.99, '500kcal', '2023-05-16'],\
                   ['koldunai su karosu', 14.99, '500kcal', '2023-05-16']]

pieno_produktai = [['pienas', 3.99, '500kcal', '2023-05-16'], ['surelis', 3.99, '500kcal', '2023-05-16'], ['varske', 3.99, '500kcal', '2023-05-16'],\
                   ['jogurtas', 3.99, '500kcal', '2023-05-16'], ['suris', 3.99, '500kcal', '2023-05-16'], ['majonezas', 3.99, '500kcal', '2023-05-16'],\
                   ['sviestas', 3.99, '500kcal', '2023-05-16'], ['grietine', 3.99, '500kcal', '2023-05-16'], ['grietinele', 3.99, '500kcal', '2023-05-16'],\
                   ['kefyras', 3.99, '500kcal', '2023-05-16']]

miltiniai_produktai = [['kvieciu miltai', 1.49, '350kcal', '2024-01-30'], ['rugiu miltai', 1.49, '200kcal', '2024-01-30'],\
                        ['kukuruzu miltai', 1.49, '200kcal', '2024-01-30'], ['ryziu miltai', 1.49, '350kcal', '2024-01-30'],\
                        ['makaronai penne', 1.49, '350kcal', '2024-01-30'], ['bociu duona', 1.49, '350kcal', '2024-01-30'], \
                        ['kruasanas', 1.49, '350kcal', '2024-01-30'], ['meduoliai', 1.49, '350kcal', '2024-01-30'],\
                        ['krekeriai' , 1.49, '350kcal', '2024-01-30'], ['virtinukai "Dziaugsmas"', 1.49, '350kcal', '2024-01-30'],\
                        ['saldyti varskeciai', 1.49, '350kcal', '2024-01-30']]

darzoves = [['pomidorai', 3.99, '100kcal', '2023-05-16'], ['pupeles', 3.99, '500kcal', '2023-05-16'], ['bulves', 3.99, '500kcal', '2023-05-16'],\
                   ['agurkai', 3.99, '500kcal', '2023-05-16'], ['baklazanai', 3.99, '500kcal', '2023-05-16'], ['paprikos', 3.99, '500kcal', '2023-05-16'],\
                   ['pievagrybiai', 3.99, '500kcal', '2023-05-16'], ['kopustas', 3.99, '500kcal', '2023-05-16'], ['salotos', 3.99, '500kcal', '2023-05-16'],\
                   ['pipirai', 3.99, '500kcal', '2023-05-16']]

#Milda
{"kaina": None, "maistine_verte": None, "galiojimo_data": None}
produktu_info = {
    "zuvies_produktai": { str(zuvies_produktai[zuvies_produktas][0]):{"kaina": zuvies_produktai[zuvies_produktas][1], "maistine_verte": zuvies_produktai[zuvies_produktas][2], "galiojimo_data": zuvies_produktai[zuvies_produktas][3]} for zuvies_produktas in range(len(zuvies_produktai))},
    "pieno_produktai": { str(pieno_produktai[pieno_produktas][0]):{"kaina": pieno_produktai[pieno_produktas][1], "maistine_verte": pieno_produktai[pieno_produktas][2], "galiojimo_data": pieno_produktai[pieno_produktas][3]} for pieno_produktas in range(len(pieno_produktai))},
    "miltiniai_produktai": { str(miltiniai_produktai[miltiniai_produktai][0]):{"kaina": miltiniai_produktai[miltiniai_produktai][1], "maistine_verte": miltiniai_produktai[miltiniai_produktai][2], "galiojimo_data": miltiniai_produktai[miltiniai_produktai][3]} for miltiniai_produktai in range(len(miltiniai_produktai))},
    "darzoves": { str(darzoves[darzoves][0]):{"kaina": darzoves[darzoves][1], "maistine_verte": darzoves[darzoves][2], "galiojimo_data": darzoves[darzoves][3]} for darzoves in range(len(darzoves))}
}

#meniu

while True:
    print(
        """
    Sveiki, jus naudojates programa sudaryti pirkiniu krepseliui.
    Pasirinkite funkcija:    
    1 - Pasirinkti produkta i pirkiniu krepseli
    2 - Perziureti pirkiniu krepseli
    3 - Perziureti produkto kaina
    4 - Perziureti produkto kcal
    5 - Perziureti produkto galiojimo laika
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
                print(f"{i+1} - {pieno_produktai[i]}")
                produkto_index = int(input('Pasirinkite produkto numeri:'))
                pasirinktas_produktas = pieno_produktai[produkto_index-1]
                pirkiniai.append(pasirinktas_produktas)
                print(f"Produktas {pieno_produktai[produkto_index-1]} itrauktas i pirkiniu krepseli.")

        
        
        elif pasirinktas_produktas == 3:
            print('Pasirinkite produkta is saraso:')
            for i in range(len(miltiniai_produktai)):
                print(f"{i+1} - {miltiniai_produktai[i]}")
                produkto_index = int(input('Pasirinkite produkto numeri:'))
                pasirinktas_produktas = miltiniai_produktai[produkto_index-1]
                pirkiniai.append(pasirinktas_produktas)
                print(f"Produktas {miltiniai_produktai[produkto_index-1]} itrauktas i pirkiniu krepseli.")
    
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
            # pirkiniai.pop(produkto_pavadinimas)
            pass
 #Milda       
        elif choice == 2:
            for pirkinys in pirkiniai:
                for pirkinio_tipas in produktu_info.values():
                    if pirkinys in pirkinio_tipas:
                        print(f"{pirkinys} - Kaina: {pirkinio_tipas.get(pirkinys).get('kaina')},\
 Maistine verte: {pirkinio_tipas.get(pirkinys).get('maistine_verte')},\
 Galiojimo data: {pirkinio_tipas.get(pirkinys).get('galiojimo_data')}") # logika gauti pirkinio value
                galutine_krepselio_suma = 0
                for pirkinys in galutine_krepselio_suma(0, len(pirkiniai)):
                    suma = suma + pirkiniai[pirkinys]

        
        elif choice <= 0 or choice > 2:
            continue
    


    elif choice == 0:
        break
    else:
        if choice > 3 or choice < 0:
            print("invalid choice")
            continue
