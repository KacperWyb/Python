def main():
    #print("Mam w pamięci pewną liczbę, spróbuj ją zgadnąć!") # ta funkcja wypisuje napis
    import Calculator, Game

    print("Wybierz tryb:")
    print("1. Kalkulator")
    print("2. Gra")
    choose = input();

    if(choose == "1"):
        Calculator.Calculator.calculator()
    elif(choose == "2"):
        Game.Game.guessNumberGame()
    else:
        print("Wybierz poprawny tryb.")
        main()

    print("Czy chcesz zagrać jeszcze raz? y/n")
    decision = input()
    if(decision == "y"):
        main()


if __name__ == "__main__":
    main()