import random


playersNotLost = []
chips = []
onek = int(input("how many players"))
for i in range(onek):
	chips.append(15)
	playersNotLost.append(True)

cards = []
for i in range(onek):
	cards.append([random.randint(1,11),random.randint(1,11)])

#ask each player how much they want to bet and by adressing them by player # and store all of that information in another list
#loop until the players cards either add up to other 21 or they enter the word STAY

bets= []

for i in range(onek):
	print("you have",chips[i],"chips")
	tooksido = int(input("how many chips would you like to bet?"))
	print(tooksido)
	#append the betts of tooxsido bets = []
	bets.append(tooksido)


for i in range(onek):
	print("hi player", i+1)
	beep = True
	while beep == True:
		#ask if the player says stay for no more cards and set beep to False
		print(cards[i])
		threek = input("would you like to stay or hit?")
		if threek == "stay":
		   beep = False	
		elif threek == "hit":
			cards[i].append(random.randint(1,11))
			if sum(cards[i]) > 21:
				print("BUST with a", cards[i][len(cards)-1]
				beep = False
				playersNotLost[i] = False
				chips[i] -= bets[i]
		#if the player says hit for more cards generate them a new card, show them the card, and check if they went over 21 if so print BUSTTTTTTTTTTTTATTTTTTTSSTSTSTSTTTTTTTT
  
#make list called hand, give it 2 cards
hand = [random.randint(1,11),random.randint(1,11)]
#check if the sum of the hand < 16 if it is hit and if not don't
while sum(hand) < 16:
	hand.append(random.randint(1,11))
	if sum(hand) > 21:
		print("computer busted")

#loop through all of the players
#check if they haven't already lost
#check if the sum of their hand is larger than the sum of the computers hand
for i in range(onek):
	if playersNotLost[i]:
		if sum(hand) < sum(cards[i]):
			print("you beat the computer!!")
			chips[i] += bets[i]
		else:
			
			print("computer had", sum(hand))			
			print("you LOST!!")
			chips[i] -= bets[i]


	
