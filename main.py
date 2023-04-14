


while True:
    print("""
    1 - kaskokia operacija
    2 - kaskokia operacija
    3 - exit, iseiti is ciklo
    """
    )
    try:
        choice = int(input("pasirinkite norima operacija (1-2-3) :"))
    except:
        print("NaN - Not a Number!")
        continue


    if choice == 1:
        pass
    
    elif choice == 2:
        pass
    


    elif choice == 3:
        break
    else:
        if choice > 3 or choice < 1:
            print("invalid choice")
            continue
