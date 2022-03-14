gold=100
start=input("you have arived at town of salem and have 100 gold , would you like to enter the tavern (y/n) ? \n").lower()
if start==("yes") or start==("y"):
  tavern=input("you have entered the tavern and found an old friend who offers you gold if you can guess the correct number betwen 1 and 10 from the first try,would you like to play (y/n) ? \n").lower()
  if tavern==("no") or tavern==("n"):
    outside=input("you went outside and found a (blacksmith) and an (alleyway) where would you like to go ? \n").lower()
    if outside==("alleyway"):
      print("you went through the alleyway and found a group of bandits where they robed and killed you")
      print("GAME OVER")
    elif outside==("blacksmith"):
      blacksmith=input("the blacksmith offers you a sword for 50 gold, would you like to buy it (y/n) ? \n").lower()
      if blacksmith==("yes") or blacksmith==("y"):
        print("you have bought the sword and left for the alleyway where you found a group of bandits that are trying to rob and kill you and you managed to defeat them")
        print("YOU WON THE GAME")
  if tavern==("yes") or tavern==("y"):
    tavern_game=int(input("What is the number betwen (1 and 10) ? \n"))
    if tavern_game==7:
      gold=gold+75
      print(f"you have won 75 gold and now have {gold} gold")
      outside=input("you went outside and found a (blacksmith) and an (alleyway) where would you like to go ? \n").lower()
      if outside==("alleyway"):
        print("you went through the alleyway and found a group of bandits where they robed and killed you")
        print("GAME OVER")
      elif outside==("blacksmith"):
        blacksmith=input("the blacksmith offers you a sword for 50 gold, would you like to buy it (y/n) ? \n").lower()
        if blacksmith==("yes") or blacksmith==("y"):
          print("you have bought the sword and left for the alleyway where you found a group of bandits that are trying to rob and kill you and you managed to defeat them")
          print("YOU HAVE WON THE GAME")
        else:
          print("you went through the alleyway and found a group of bandits where they robed and killed you")
          print("GAME OVER")
    if tavern_game <=6 or tavern_game >=8:
      outside=input("you went outside and found a (blacksmith) and an (alleyway) where would you like to go ? \n").lower()
      if outside==("alleyway"):
        print("you went through the alleyway and found a group of bandits where they robed and killed you")
        print("GAME OVER")
      elif outside==("blacksmith"):
        blacksmith=input("the blacksmith offers you a sword for 50 gold, would you like to buy it (y/n) ? \n").lower()
        if blacksmith==("yes") or blacksmith==("y"):
          print("you have bought the sword and left for the alleyway where you found a group of bandits that are trying to rob and kill you and you managed to defeat them")
          print("YOU HAVE WON THE GAME")
        else:
          print("you went through the alleyway and found a group of bandits where they robed and killed you")
          print("GAME OVER")
else:
  print("RESTART AND CHOOSE YES ( MAKEN 2LI 5LE2 KAMEL CODING LA HYDA L SECTION :) ")
