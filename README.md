# Torn-HIGH-LOW-Helper
Made by Trilo [3354210] on 25/7/24 v1
License: Open Source (of course)

In this version, user input is used, and it is CLI-based.
In the future, if there is demand, I could create an application or a script that would use an API or something similar.

Rules/Good Information
Aces are the highest card, and 2s are the lowest.
We don't care about the suit of the card, only that there are four of each number.
We also don't care about card duplicates, as it doesn't matter if we go high or low. Therefore, duplicates are not considered in the estimation.

Inspiration: https://www.torn.com/forums.php#!p=threads&f=61&t=15960774&b=0&a=0
"You can count the cards too. It tells you when the deck is shuffled. After a shuffle, if you note down all the cards you've seen 
(2 per turn), then the choice you make can be a bit more informed. If you know you've seen all the..." - Multipass [1955315]
This means that this tool is only valid when the deck has been shuffled. Keep track of when to reset and when to keep going.
More inspiration: https://www.torn.com/forums.php#!p=threads&f=15&t=15915634&b=0&a=0
Torn's High Low doesn't shuffle the deck after every round in a game. It reshuffles the deck only after 16 full rounds (i.e., 32 cards).

You don't need to consider probability in this determination, as it can be done visually with a list, as shown in this case.
The goal is to know how many cards are lower and higher than the current card and, with that information, compare and return high or low.

I'm not a super good programmer, so input is gladly accepted :)
I'm lazy, so do Ctrl + C to exit the game loop :)
Also, I've not added exceptions, so if you enter an invalid letter or number, it will just fail, and you will have to restart. 
I did this quickly during a break, so it's not a solid program—bare minimum.



#  HOW TO USE IT WILL COME SOON
