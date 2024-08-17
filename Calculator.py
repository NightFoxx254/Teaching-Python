#make a calculator that uses one input in the form of num,opperation,num



#irradical = input("what operation are you using(as a symbol?")
#won = int(input("what is the first number? "))
#too = int(input("what is the second number? "))


onek = input("what is your arithmancy problem?")

# won = int(onek[0])
# too = int(onek[2]) #You wrote position 1 not 2 


won = []
too = []





if "+" in onek: # you were checking the entirety of the input not just position one which is the operation
  threek = onek.find("+")
  for i in range(threek):
    won.append(int(onek[i]))
  for i in range(len(onek)-threek-1):
    too.append(int(onek[i+threek+1]))
  print(int(str(won))+int(str(too))) # you wrote == and you wrote == threek
elif "-" in onek:
  threek = onek.find("-")
  for i in range(threek):
    won.append(int(onek[i]))
  for i in range(len(onek)-threek-1):
    too.append(int(onek[i+threek+1]))
  print(int(str(won))+int(str(too))) # you wrote == and you wrote == threek
elif "/" in onek:
  threek = onek.find("/")
  for i in range(threek):
    won.append(int(onek[i]))
  for i in range(len(onek)-threek-1):
    too.append(int(onek[i+threek+1]))
  print(int(str(won))+int(str(too))) # you wrote == and you wrote == threek
elif "*" in onek:
  threek = onek.find("*")
  for i in range(threek):
    won.append(int(onek[i]))
  for i in range(len(onek)-threek-1):
    too.append(int(onek[i+threek+1]))
  print(int(str(won))+int(str(too))) # you wrote == and you wrote == threek
else:
  print("Sorry that didn't work")

#you can get the position of an input 
#like this  input[1] and find out what the operation and numbers are with that
