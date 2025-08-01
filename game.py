import random
import turtle

tr = turtle.Turtle()
tr2 = turtle.Turtle()
wn = turtle.Screen()
wn.setup(500,500)
wn.addshape('pikachu.gif')
wn.addshape('squirtle.gif')

wn.addshape('youlose.gif')
tr.shape('pikachu.gif')
tr2.shape('squirtle.gif')
tr.backward(200)
tr2.forward(200)

Fighter1 = "First Fighter"
F1Health = 100
F1Defense = 75
F1Strength = 10
F1Move1 = "Move 1"
F1M1Damage = 10
F1M1Accuracy = 95
F1Move2 = "Move 2"
F1M2Damage = 30
F1M2Accuracy = 80
F1Move3 = "Move 3"
F1M3Damage = 20
F1M3Accuracy = 87

Fighter2 = "Second Fighter"
F2Health = 100
F2Defense = 75
F2Strength = 10
F2Move1 = "Move 1"
F2M1Damage = 10
F2M1Accuracy = 95
F2Move2 = "Move 2"
F2M2Damage = 30
F2M2Accuracy = 80
F2Move3 = "Move 3"
F2M3Damage = 20
F2M3Accuracy = 87
while(F1Health > 0 and F2Health > 0):
  print("Choose move 1-3: ")
  moveChoice = input()
  moveChoice = int(moveChoice)
  if(moveChoice == 1):
    print(Fighter1 + " used " + F1Move1)
    rand = random.randint(0, 100)
    if(rand > F1M1Accuracy):
      print("The attack missed!")
    else:
     print("The attack did: " + str(F1M1Damage) + " damage! ")
     F2Health = F2Health - F1M1Damage
     print(Fighter2 + " now has " + str(F2Health) + " health remaining!")
  elif(moveChoice == 2):
    print(Fighter1 + " used " + F1Move2)
    rand = random.randint(0, 100)
    if(rand > F1M2Accuracy):
      print("The attack missed!")
    else:
      print("The attack did: " + str(F1M2Damage) + " damage! ")
      F2Health = F2Health - F1M2Damage
      print(Fighter2 + " now has " + str(F2Health) + " health remaining!")
  elif(moveChoice == 3):
    print(Fighter1 + " used " + F1Move3)
    rand = random.randint(0, 100)
    if(rand > F1M3Accuracy):
      print("The attack missed!")
    else:
      print("The attack did: " + str(F1M3Damage) + " damage! ")
      F2Health = F2Health - F1M3Damage
      print(Fighter2 + " now has " + str(F2Health) + " health remaining!")
  tr.forward(200)
  tr.backward(200)
  print("\n")
  enemymoveChoice = random.randint(1, 3)
  if(enemymoveChoice == 1):
    print(Fighter2 + " used "+ F2Move1)
    rand = random.randint(0, 100)
    if(rand > F2M1Accuracy):
      print("The attack missed!")
    else:
      print("The attack did " + str(F2M1Damage) + " damage!")
      F1Health = F1Health - F2M1Damage
      print(Fighter1 + " now has " + str(F1Health) + " health remaining!")
  
  elif(enemymoveChoice == 2):  
    print(Fighter2 + " used "+ F2Move2)
    rand = random.randint(0, 100)
    if(rand > F2M2Accuracy):
      print("The attack missed!")
    else:
      print("The attack did " + str(F2M2Damage) + " damage!")
      F1Health = F1Health - F2M2Damage
      print(Fighter1 + " now has " + str(F1Health) + " health remaining!")
  elif(enemymoveChoice == 3):
    print(Fighter2 + " used "+ F2Move3)
    rand = random.randint(0, 100)
    if(rand > F2M3Accuracy):
      print("The attack missed!")
    else:
      print("The attack did " + str(F2M3Damage) + " damage!")
      F1Health = F1Health - F2M3Damage
      print(Fighter1 + " now has " + str(F1Health) + " health remaining!")
  tr2.backward(200)
  tr2.forward(200)
  if(F1Health <= 0):
    tr.shape('youlose.gif')
    tr2.hideturtle()
    wn.update()
  elif(F2Health <= 0):
    print("YOU WIN!")
    tr.hideturtle()
    tr2.hideturtle()
    wn.update()
