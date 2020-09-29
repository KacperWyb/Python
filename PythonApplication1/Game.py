class Game(object):
    """description of class"""       

    def guessNumberGame():
        import Random

        rand = Random.Random.giveRandom()
        tryCounter = 0

        #print(rand)
        print("Mam w pamięci pewną liczbę, zgadnij ją!")
        
        while True:
            try:
                userNumber = int(input())
                tryCounter = tryCounter + 1

                if(userNumber < rand):
                    print("Twoja liczba jest za mała.")
                elif(userNumber > rand):
                    print("Twoja liczba jest za duża.")
                else:
                    print("Brawo, zgadłeś moją liczbę za " + str(tryCounter) + " razem!")
                    break
            except:
                print("Mówiłem podaj liczbę! Losuję nową oszuście!")
                Game.guessNumberGame()
                

