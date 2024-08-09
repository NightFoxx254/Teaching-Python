import random

#== is to check
#= is to set
#"this is a string"
#["this","is","a","List","of","strings"]
#8 ,this is a number
#False ,this is a true or false
#() these are for functions
#commas separate stuff


decision=["rock","scissors","paper","lizard","Spock"]
kingB0B = random.randint(0,4)
lalala = input("rock, paper, scissors, lizard, or Spock?")
print("the computer used",decision[kingB0B])
if decision[kingB0B]==lalala:
	print("tie")
elif decision[kingB0B] == "rock" and lalala == "scissors":
	print("you lost")
elif decision[kingB0B] == "scissors" and lalala =="paper":
	print("you lost")
elif decision[kingB0B] == "paper" and lalala == "rock":
	print("you lost")
elif decision[kingB0B] == "rock" and lalala == "lizard":
	print("you lost")
elif decision[kingB0B] == "lizard" and lalala == "Spock":
	print("you lost")
elif decision[kingB0B] == "Spock" and lalala == "scissors":
	print("you lost")
elif decision[kingB0B] == "scissors" and lalala == "lizard":
	print("you lost")
elif decision[kingB0B] == "lizard" and lalala == "paper":
	print("you lost")
elif decision[kingB0B] == "paper" and lalala == "spock":
	print("you just got disproven")
elif decision[kingB0B] == "spock" and lalala == "rock":
  print("VAPORIZED")







elif decision[kingB0B]  == "paper" and lalala == "scissors" or decision[kingB0B] == "scissors" and lalala == "rock" or decision[kingB0B] == "rock" and lalala == "paper" or decision[kingB0B] == "lizard" and lalala == "rock" or decision[kingB0B] == "Spock" and lalala == "lizard" or decision[kingB0B] == "scissors" and lalala == "Spock" or decision[kingB0B] == "lizard" and lalala == "scissors" or decision[kingB0B] == "paper" and lalala == "lizard" or decision[kingB0B] == "Spock" and lalala == "paper" or decision[kingB0B] == "rock" and lalala =="Spock":
	print("hura you one")
