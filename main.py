
#meniu

while True:
    print(
        """
    Sveiki, jus naudojates programa sudaryti pirkiniu krepseliui.
    Pasirinkite programos funkcija:    
    1 - Pasirinkti produkta i pirkiniu krepseli
    2 - Produkto kaina
    3 - Produkto kcal
    4 - Produkto galiojimo laikas
    0 - Iseiti is programos

    """    
    )
    try:
        choice = int(input("Pasirinkite norima operacija (1-4 arba 0) :"))
    except:
        print("Pasirinkite teisinga funkcija")
        continue

    if choice == 1:
        pass
    
    elif choice == 2:
        pass
    


    elif choice == 0:
        break
    else:
        if choice > 3 or choice < 0:
            print("invalid choice")
            continue
