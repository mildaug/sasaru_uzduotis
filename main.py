
# TODO 

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






zuvies_produktai =[['silke surime', 14.99, '500kcal', '2023-05-16'], 'karpio kapotinis', 'juros eserys', 'menkes vyniotinis', 'lydekaite',\
                    'lasisos file', 'koldunai su karosu']
pieno_produktai = ['pienas', 'surelis', 'varske', 'jogurtas', 'suris', 'majonezas', 'sviestas', 'grietine', 'grietinele', 'kefyras']

miltiniai_produktai = ["kvieciu miltai", "rugiu miltai" , "kukuruzu miltai", "ryziu miltai", 'makaronai penne', 'bociu duona', 'kruasanas', 'meduoliai', 'krekeriai' \
                        'virtinukai "Dziaugsmas"', 'saldyti varskeciai']

Miltai = {"kvieciu", "rugiu", "miežiu", "kukuruzu", "ryziu"}
Tešlos =  {"makaronai", "duonos gaminiai", "blynai", "koldūnai"}
Kepiniai = {"pyragai", "tortai", "sausainiai", "misiniai"}
Padažai_prieskoniai = {"miltiniai padažai", "prieskoniai"}
Gerimai = {"alus", "viskis", "romas"}
Pusgaminiai = {"traskuciai", "krekeriai", "duonos trupiniai"}
Kitos_iltinių_produktų_rūšys = {"dribsniai", "grūdėtų miltų produktai", "miltų mišiniai"}

produktu_info = {
    "zuvies_produktai": {'silke surime': {"kaina": None, "maistine_verte": None, "galiojimo_data": None},
                                      'karpio kapotinis': {"kaina": None, "maistine_verte": None, "galiojimo_data": None},
                                      'juros eserys': {"kaina": None, "maistine_verte": None, "galiojimo_data": None},
                                      'menkes vyniotinis': {"kaina": None, "maistine_verte": None, "galiojimo_data": None},
                                      'lydekaite': {"kaina": None, "maistine_verte": None, "galiojimo_data": None},
                                      'lasisos file': {"kaina": None, "maistine_verte": None, "galiojimo_data": None},
                                      'koldunai su karosu': {"kaina": None, "maistine_verte": None, "galiojimo_data": None}
                                      },
    "pieno_produktai": { str(pieno_produktai[pieno_produktas][0]):{"kaina": pieno_produktai[pieno_produktas][1], "maistine_verte": pieno_produktai[pieno_produktas][2], "galiojimo_data": pieno_produktai[pieno_produktas][3]} for pieno_produktas in range(len(pieno_produktai))},
    "miltiniai_produktai": { str(miltinis_produktas):{"kaina": None, "maistine_verte": None, "galiojimo_data": None} for miltinis_produktas in miltiniai_produktai}
}







for i in range(len(zuvies_produktai)):
    print(f"{i+1} - {zuvies_produktai[i]}")
#meniu

while True:
    print(
        """
    Sveiki, jus naudojates programa sudaryti pirkiniu krepseliui.
    Pasirinkite programos funkcija:    
    1 - Pasirinkti produkta i pirkiniu krepseli
    2 - apziureti pirkiniu krepseli
    2 - Produkto kaina
    3 - Produkto kcal
    4 - Produkto galiojimo laikas
    0 - Iseiti is programos

    """    
    )
    try:
        choice = int(input("pasirinkite norima operacija (0-2-) :"))
    except:
        print("NaN - Not a Number!")
        continue


    if choice == 1:
        print('Produktai:')
        print('1 Zuvies:')
        print('2 Pieno:')
        print('3 Miltiniai:')
        pasirinktas_produktas = int(input('Pasirinkite produkto kategorija 1, 2 arba 3:'))
        
        if pasirinktas_produktas == 1:
            print('Pasirinkite produkta is saraso:')
            for i in range(len(zuvies_produktai)):
                print(f"nr: {i+1} - {zuvies_produktai[i]}")

            produkto_index = int(input('Iveskite produkto numeri:'))
            if produkto_index - 1 in range(len(zuvies_produktai)):                         
                
                pirkiniai.append(zuvies_produktai[produkto_index - 1])
                print(f"Produktas {zuvies_produktai[produkto_index - 1]} itrauktas i pirkiniu krepseli.")
                
        
        
        elif pasirinktas_produktas == 2:
            print('Pasirinkite produkta is saraso:')
            for i in range(len(pieno_produktai)):
                print(f"{i+1} - {pieno_produktai[i]}")
                produkto_index = int(input('Iveskite produkto numeri:'))
                pasirinktas_produktas = pieno_produktai[produkto_index-1]
                pirkiniai.append(pasirinktas_produktas)
                print(f"Produktas {pieno_produktai[produkto_index-1]} itrauktas i pirkiniu krepseli.")

        
        
        elif pasirinktas_produktas == 3:
            print('Pasirinkite produkta is saraso:')
            for i in range(len(miltiniai_produktai)):
                print(f"{i+1} - {miltiniai_produktai[i]}")
                produkto_index = int(input('Iveskite produkto numeri:'))
                pasirinktas_produktas = miltiniai_produktai[produkto_index-1]
                pirkiniai.append(pasirinktas_produktas)
                print(f"Produktas {miltiniai_produktai[produkto_index-1]} itrauktas i pirkiniu krepseli.")
    
    elif choice == 2:
        for pirkinys in pirkiniai:
            print(f"nr: {pirkiniai.index(pirkinys) +1} - {pirkinys}")
        print("""
        Ka norite daryti su pirkiniu krepseliu ?
        0 - iseiti i meniu
        1 - isimti produkta if krepselio
        2 - parodyti info apie produkta
        
        """)
        choice = int(input('jusu pasirinkimas: '))
        if choice == 1:
            pass
        
        elif choice == 2:
            pass
        
        elif choice <= 0 or choice > 2:
            continue
    


    elif choice == 0:
        break
    else:
        if choice > 3 or choice < 0:
            print("invalid choice")
            continue
