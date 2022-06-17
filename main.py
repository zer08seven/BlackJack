from getkey import getkey
import random, os, time, errno

version = "Version 2.1"
streak = 0
blackjacks = 0
wins = 0
playerCash = 75
Deck = [2,3,4,5,6,7,8,9,10,"J","Q","K","A",2,3,4,5,6,7,8,9,10,"J","Q","K","A",2,3,4,5,6,7,8,9,10,"J","Q","K","A",2,3,4,5,6,7,8,9,10,"J","Q","K","A"]
dealerHand=[]
playerHand=[]

def rgb(r,g,b):
  return f"\033[38;2;{r};{g};{b}m"
    
reset = "\033[0m"
bold = "\033[1m"
light_blue = rgb(82,180,255)
aqua = rgb(0,255,255)
light_brown = rgb(190,140,100)
brown = rgb(170,120,80)
golden = rgb(219,180,107)
red = rgb(255,0,0)

try:
    os.makedirs("./data")
    with open("data/cash.txt", "w") as file:
        file.write("20")
        
    with open("data/wins.txt", "w") as file:
        file.write("0")
        
    with open("data/winstreak.txt", "w") as file:
        file.write("0")
        
    with open("data/blackjacks.txt", "w") as file:
        file.write("0")
        
except OSError as e:
    if e.errno != errno.EEXIST:
        raise
def load():
    global playerCash, wins, streak, blackjacks
    with open("data/cash.txt", "r") as file:
        playerCash = file.read()
        
    with open("data/wins.txt", "r") as file:
        wins = file.read()
        
    with open("data/winstreak.txt", "r") as file:
        streak = file.read()
        
    with open("data/blackjacks.txt", "r") as file:
        blackjacks = file.read()
        
    startUI()

def game():
    global playerCash, wins, streak, blackjacks
    
    dealerHand=[]
    playerHand=[]

    os.system("clear")
    globalDeck = Deck

    def bet():
        global playerCash
        global betCash
        global Deck
        global globalDeck
        globalDeck = Deck
        ammount = input(f"""{bold}{light_blue}Simple Blackjack {reset}         {version}        {red}        Play safe +18\n{reset}
♦ ────────────────────────────────────────────────────────────── ♠\n\nYour cash: ${playerCash}\n \_> [🤵] Dealer: Enter your bet sir: $""")

        try:
            bet = int(ammount)
        except: 
            print(f"\n\n {red}ERROR: The bet must be an integer number!")
            time.sleep(3)
            game()

        if int(playerCash) < 1:
            exit(f"\n\n{red}[🤵] Dealer: You are broke!\n\_>You lost all your cash, there is no way to get your cash back")
            time.sleep(4)
        elif bet > int(playerCash):
            betCash = int(playerCash)
        elif bet < 1:
            betCash = 1
        else:
            betCash = bet
        playerCash = int(playerCash) - betCash
    
    def backjack():
        global playerCash, betCash, wins, streak, blackjacks
        get = betCash * 3
        playerCash = int(playerCash) + betCash + get
        blackjacks = int(blackjacks) + 1
        wins = int(wins) + 1
        streak = int(streak) + 1

    def win():
        global playerCash, betCash, wins, streak, blackjacks
        playerCash = int(playerCash) + betCash + betCash
        streak = int(streak) + 1
        wins = int(wins) + 1

    def winDouble():
        global playerCash, betCash, wins, streak, blackjacks
        playerCash = int(playerCash) + betCash + betCash + betCash
        streak = int(streak) + 1
        wins = int(wins) + 1

    def draw():
        global playerCash, betCash, wins, streak, blackjacks
        playerCash = int(playerCash) + betCash
        streak = 0

    def save():
        global playerCash, wins, streak, blackjacks
        
        with open("data/cash.txt", "w") as file:
            file.write(str(playerCash))
        
        with open("data/wins.txt", "w") as file:
            file.write(str(wins))
        
        with open("data/winstreak.txt", "w") as file:
            file.write(str(streak))

        with open("data/blackjacks.txt", "w") as file:
            file.write(str(blackjacks))
        startUI()
        pass

    def end():
        global globalDeck, Deck
        globalDeck = Deck
        print("""\n♣ ────────────────────────────────────────────────────────────── ♥
                        Made with ❤  By github.com/zer08seven """)
        print("\n[🤵] Dealer: The game is over, sir!\n\n                  Save [S]       Menu [A]     \n\n")
        
        key = getkey()
        if key == "s":
            save()
        else: startUI()

        
    def checkDealerValues():
         for i in dealerHand:
            global dealerHandValue
            dealerHandValue = 0
            try:
                for i in dealerHand:
                    if i == 2:
                        dealerHandValue = dealerHandValue + i
                    elif i == 3:
                        dealerHandValue = dealerHandValue + i
                    elif i == 4:
                        dealerHandValue = dealerHandValue + i
                    elif i == 5:
                        dealerHandValue = dealerHandValue + i
                    elif i == 6:
                        dealerHandValue = dealerHandValue + i
                    elif i == 7:
                        dealerHandValue = dealerHandValue + i
                    elif i == 8:
                        dealerHandValue = dealerHandValue + i
                    elif i == 9:
                        dealerHandValue = dealerHandValue + i
                    elif i == 10:
                        dealerHandValue = dealerHandValue + i       
                for i in dealerHand:
                    if i == "Q":
                        dealerHandValue = dealerHandValue + 10
                    elif i == "K":
                        dealerHandValue = dealerHandValue + 10
                    elif i == "J":
                        dealerHandValue = dealerHandValue + 10
                    elif i == "A":
                        if dealerHandValue < 11:
                            dealerHandValue = dealerHandValue + 11
                        elif dealerHandValue > 10:
                            dealerHandValue = dealerHandValue + 1     
            except: pass
            return dealerHandValue
             
    def checkPlayerValues():
         for i in playerHand:
            global playerHandValue
            playerHandValue = 0
            try:
                for i in playerHand:
                    if i == 2:
                        playerHandValue = playerHandValue + i
                    elif i == 3:
                        playerHandValue = playerHandValue + i
                    elif i == 4:
                        playerHandValue = playerHandValue + i
                    elif i == 5:
                        playerHandValue = playerHandValue + i
                    elif i == 6:
                        playerHandValue = playerHandValue + i
                    elif i == 7:
                        playerHandValue = playerHandValue + i
                    elif i == 8:
                        playerHandValue = playerHandValue + i
                    elif i == 9:
                        playerHandValue = playerHandValue + i
                    elif i == 10:
                        playerHandValue = playerHandValue + i
                for i in playerHand:
                    if i == "Q":
                        playerHandValue = playerHandValue + 10
                    elif i == "K":
                        playerHandValue = playerHandValue + 10
                    elif i == "J":
                        playerHandValue = playerHandValue + 10
                    elif i == "A":
                        if playerHandValue < 11:
                            playerHandValue = playerHandValue + 11
                        elif playerHandValue > 10:
                            playerHandValue = playerHandValue + 1      
            except: pass
            return playerHandValue
           
    def shuffleDealer():
        dealerCard = random.choice(globalDeck)
        dealerHand.append(dealerCard)
        globalDeck.remove(dealerCard)     
        
    def shufflePlayer():
        playerCard = random.choice(globalDeck)
        playerHand.append(playerCard)
        globalDeck.remove(playerCard)

    def stand():
        global playerCash, wins, streak, blackjacks
        
        checkDealerValues()
        checkPlayerValues()
        print(f"Dealer Hand: {dealerHand[0:90]} for a total of {dealerHandValue}")
        if dealerHandValue > playerHandValue:
            print("\nDealer Wins")
            streak = 0
            end()
        else:    
            while dealerHandValue < 17:
                time.sleep(1.2)
                time.sleep(1.2)
                shuffleDealer()
                checkDealerValues()
                print(f"\nDealer new card: {dealerHand[0:90]} for a total of {dealerHandValue}")
        
            if dealerHandValue > 21:
                print("\nplayer wins")
                win()
                end()
            elif dealerHandValue < playerHandValue:
                print("\nplayer wins")
                win()
                end()
            elif dealerHandValue > playerHandValue:
                print("\ndealer wins")
                streak = 0
                end()
            elif dealerHandValue == playerHandValue:
                print("\nDraw!")
                streak = 0
                draw()
                end()

    def standDouble():
        global playerCash, wins, streak, blackjacks
        checkDealerValues()
        checkPlayerValues()
        print(f"Dealer Hand: {dealerHand[0:90]} for a total of {dealerHandValue}")
        if dealerHandValue > playerHandValue:
            print("\nDealer Wins")
            streak = 0
            end()
        else:    
            while dealerHandValue < 17:
                time.sleep(1.2)
                time.sleep(1.2)
                shuffleDealer()
                checkDealerValues()
                print(f"\nDealer new card: {dealerHand[0:90]} for a total of {dealerHandValue}")
        
            if dealerHandValue > 21:
                print("\nplayer wins")
                winDouble()
                end()
            elif dealerHandValue < playerHandValue:
                print("\nplayer wins")
                winDouble()
                end()
            elif dealerHandValue > playerHandValue:
                print("\ndealer wins")
                streak = 0
                end()
            elif dealerHandValue == playerHandValue:
                print("\nDraw!")
                streak = 0
                draw()
                end()
                
    def hit():
        global playerCash, wins, streak, blackjacks
        shufflePlayer()
        checkPlayerValues()
        print(f"\nPlayer new card: {playerHand[0:9]} for a total of: {playerHandValue}")
        if playerHandValue < 21: 
            secondMenu()
        elif playerHandValue > 21:
            print("\nDealer wins")
            streak = 0
            end()
        elif playerHandValue == 21:
            stand()
            
    def double():
        global playerCash, wins, streak, blackjacks, betCash
        if playerCash <  betCash:
            hit()
        else: 
            playerCash = playerCash - betCash
            shufflePlayer()
            checkPlayerValues()
            print(f"\nPlayer new card: {playerHand[0:9]} for a total of: {playerHandValue}")
            if playerHandValue == 21:
                print("\nPlayer wins")
                winDouble()
                end()
            if playerHandValue > 21:
                print("\nDealer wins")
                streak = 0
                end()
            elif playerHandValue < 21: 
                standDouble()

    def menu():
        print("\nWhat do you want to do?:\n\n             Hit [a]       Stand [s]    Double [d]\n\n")
        key = getkey() 
        if key == "s":
            stand()
        if key == "a":
            hit()
        if key == "d":
            double()
        else: stand()

    def secondMenu():
        print("\nWhat do you want to do?:\n\n                  Hit [a]       Stand [s]     \n\n")
        key = getkey() 
        if key == "s":
            stand()
        elif key == "a":
            hit()   
            
    bet()
    shuffleDealer()
    shufflePlayer()
    shuffleDealer()
    shufflePlayer()
    checkDealerValues()
    checkPlayerValues()

    time.sleep(1)
    print(f"\n\nDealer Hand: [{dealerHand[0]}, ?]")
    time.sleep(1)
    print(f"\nPlayer Hand: {playerHand[0:9]} for a total of: {playerHandValue}")
    if playerHandValue == 21:
         print("\nPlayer Wins by BLACKJACK!")
         backjack()
         end()
    elif dealerHandValue == 21:
          print(f"\nDealer Has: {dealerHand[0:9]}, Dealer Wins by BLACKJACK!")
          streak = 0
          end()
    else:
          menu()
    
def startUI():
    global playerCash, wins, streak, blackjacks

    def stats():
        os.system("clear")
        print(f"""{bold}{light_blue}Simple Blackjack {reset}         {version}        {red}        Play safe +18\n{reset}
♦ ────────────────────────────────────────────────────────────── ♠

    ❮ Start [A]           │ 🏆 Wins: {wins}               
                          │ 💰 Cash: ${playerCash}              
                          │ 📈 Streak: {streak}
                          │ 🃏 Blackjacks: {blackjacks}
              
♣ ────────────────────────────────────────────────────────────── ♥
                         Made with ❤  By github.com/zer08seven """)
        key = getkey()
        if key == "a":
            startUI()
        else: startUI()
            
    def main():
        os.system("clear")
        print(f"""{bold}{light_blue}Simple Blackjack {reset}         {version}        {red}        Play safe +18\n{reset}
♦ ────────────────────────────────────────────────────────────── ♠
              
                          🤠 Start [A]
                          📊 Stats [S]
                          📩 Load  [D]
                          ❌ Quit  [Q]
              
♣ ────────────────────────────────────────────────────────────── ♥
                         Made with ❤  By github.com/zer08seven """)
    main()
    key = getkey()
    if key == "s":
        stats()
    elif key == "d":
        load()
    elif key == "q":
        exit("Player left the game")
    else: game()   
        
startUI()
