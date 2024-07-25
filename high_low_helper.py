#Made by Trilo [3354210] the 25/7-24 v1
#Licens: Open Source (ofc)

#In this version user input is used and it is CLI based 
#In the future if demand i could do an application or like a scirpt which would use API or something instead.

#Rules/Good info
#Aces are the highest card, and 2s are the lowest.
#We dont care about the color of the card only that it exist 4 of each number
#We also dont care about a card other duplicates as it dosent matter if we go high or low so in the estemation it isnt taken into considoration

#Inspo https://www.torn.com/forums.php#!p=threads&f=61&t=15960774&b=0&a=0
#"You can count the cards too. It tells you when the deck is shuffled. After a shuffle if you note down all the cards you've seen 
# (2 per turn) then the choice you make can be a bit more informed. If you know you've seens all the " -  Multipass [1955315] 
#Which means that this tool is only valid when the deck have been shuffeled. So keep track when to reset and when to keep going.
#More insp https://www.torn.com/forums.php#!p=threads&f=15&t=15915634&b=0&a=0
#Torn's High Low doesn't shuffle the deck after every round in a game. It reshuffles the deck only after 16 full rounds (ie. 32 cards).

#Dont need to take probability into this determination as it can as easly be done visually with a list as done in this case.
#Just want to know how many card are lower and higher then the current card and with that information compare and return high or low'

#Not a super good programer so input as gladely acepted :)
#Im lazy so do ctrl + c to exit the game loop :=)
#Also ive not added exception so if u send in a bogus letter or number it will just fail and you have to restart. 
#Did this quick during a break so its not a solid program. Bare minimum

class Deck:
    def __init__(self):
        self.lst = [
        '2', '2', '2', '2', 
        '3', '3', '3', '3', 
        '4', '4', '4', '4', 
        '5', '5', '5', '5', 
        '6', '6', '6', '6', 
        '7', '7', '7', '7', 
        '8', '8', '8', '8', 
        '9', '9', '9', '9', 
        '10', '10', '10', '10', #TILT
        'J', 'J', 'J', 'J', 
        'Q', 'Q', 'Q', 'Q', 
        'K', 'K', 'K', 'K', 
        'A', 'A', 'A', 'A']
    
    def descision(self, curr_card):
        card = curr_card  
        high_or_low = 0 #True or false flag
        counter_higher = 0
        counter_lower = 0    

        for i in range(len(self.lst)):
            if self.lst[i] != card and not high_or_low:
                counter_lower += 1
            elif self.lst[i] != card and high_or_low:
                counter_higher += 1
            elif self.lst[i] == card:
                high_or_low = 1 #Used to determine which side of the card it is. Higher or lower part 

        if(counter_lower < counter_higher):     return "High"
        elif(counter_lower > counter_higher):   return "Low"
        else:                                   return "Draw"
        
    def mycard_remove(self, my_card):
       self.lst.remove(my_card)
       return 

def game():
    print("If the deck is shuffled typ L, so the deck can be reset")
    kortlek = Deck() #Hmmmm what country?
    while(True):
        curr_dealer_card = input("What's the dealers card? ").upper()
        print(kortlek.descision(curr_dealer_card))
        my_c = input("What card did you draw? ").upper()
        if(my_c == 'L'): #Reset flag
            kortlek = Deck() #Resets the object restoring the list
            continue
        kortlek.mycard_remove(my_c)

        
if __name__ == "__main__":
    game()