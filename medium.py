print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print(" ")
print("Clash of Clans - A Text Based Adventure")
print("Game Engine provided by Sean O'Reilly | Game Design by: Arman Haji")
print(" ")
print("This game is dynamic meaning there are multiple possibilities,")
print("and outcomes and that the gameplay is completely different each time")
print(" ")
print("The plot of the storyline is that you are stuck inside of a prison,")
print("trying to escape. If the gaurds catch you trying to escape, you")
print("have to try to fend them off. If you fail, you die. Simple.")
print("Good Luck!")
print(" ")
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print(" ")
name = input("Enter you name: ")
import sys
def dead():
      print("You died...")
      sys.exit()

def end():
      print("Game over.")
      sys.exit()
      
print("Welcome", name,"... You can choose one of these five classes.")
print("Each will enable you to do different tings.")
guardhealth = 20
guarddamage = 3
guardspeed = 3
guardhealth2 = 30
guarddamage2 = 5
guardspeed2 = 5
guardhealth3 = 40
guarddamage3 = 6
guardspeed3 = 6
inventory = []
def archer():
      print("You will start with a bow and ten arrows.")
      print("Your attributes are:")
      print("damage|--------------")
      print("Health|-------")
      print("Speed |------------") #helps when trying to flee and dodge. Make it random if you can flee an enemy depending on your speed.
archerdamage = 14
archerhealth = 7
archerspeed = 12
      

def barbarian():
      print("You will start with a sword.")
      print("Your attributes are:")
      print("damage|----------------")
      print("Health|------")
      print("Speed |---------")
barbariandamage = 16
barbarianhealth = 6
barbarianspeed = 9

def dragon():
      print("You will start with fire breath.")
      print("Your attributes are:")
      print("damage|--------------")
      print("Health|------------")
      print("Speed |-------") #helps when trying to flee and dodge and attack first. Make it random if you can flee an enemy depending on your speed.
dragondamage = 14
dragonhealth = 12
dragonspeed = 7


def goblin():
      print("You will start with a sack of gold coins.")
      print("Your attributes are:")
      print("damage|----------------")
      print("Health|------------")
      print("Speed |-----") #helps when trying to flee and dodge and attack first. Make it random if you can flee an enemy depending on your speed.
goblindamage = 16
goblinhealth = 12
goblinspeed = 5

def wizard():
      print("You will start with a wand.")
      print("Your attributes are:")
      print("damage|-------------------")
      print("Health|----")
      print("Speed |---------") 
wizarddamage = 19
wizardhealth = 4
wizardspeed = 9

rework = "no"
while rework == "no":
      print("Choose a class:")
      print("1, for an archer.")
      print("2, for a barbarian.")
      print("3, for a dragon.")
      print("4, for an goblin.")
      choicec = int(input("5, for an wizard: "))
      print(" ")
      weapons = ['bow', 'sword', 'fire breath', 'sack of gold coins', 'wand']
      if choicec == 1:
            archer()
            print(" ")
            rework = input("Are you sure you wish to be an archer? (yes/no) ")
            print(" ")
      if choicec == 2:
            barbarian()
            print(" ")
            rework = input("Are you sure you wish to be a barbarian? (yes/no) ")
            print(" ")
      if choicec == 3:
            dragon()
            print(" ")
            rework = input("Are you sure you wish to be a dragon? (yes/no) ")
            print(" ")
      if choicec == 4:
            goblin()
            print(" ")
            rework = input("Are you sure you wish to be an goblin? (yes/no) ")
            print(" ")
      if choicec == 5:
            wizard()
            print(" ")
            rework = input("Are you sure you wish to be an wizard? (yes/no) ")
            print(" ")
      if rework == "yes":
            break

print("Good choice", name)
print("You start in an underground jailcell.")
print("The only light coming from a candle being held by a guard just outside.")
print("The man fell asleep hours ago, and you see that the keys to the cell are")
print("dangling from his belt, just in reach.")
print("Moreover, the back of the room is pitch black, due to the lack of light")
print("and so you had stored your", weapons[choicec - 1], "there in the darkness")
print("What do you wish to do?")
print(" ")

action1 = 0
b = 0
healthpot1 = 0
yourweapon = 0
while action1 != 3:
      print("1, pick up your", weapons[choicec - 1])
      print("2, look around the room")
      action1 = int(input("3, steal the guards keys and open the lock: "))
      if action1 == 1:
            print("You have added your", weapons[choicec - 1], "to your inventory.")
            inventory.append(weapons[choicec - 1])
            yourweapon = 1
            

      if action1 == 2 and b == 0:
            b = b+1
            print("You look around and see that there are no windows, and the walls")
            print("are made of crumbling brick. Then, in the corner of the room, you")
            print("spot a health potion.")
            addhealthpot1 = input("Do you wish to add it to your inventory? (yes/no) ")
            if addhealthpot1 == "yes":
                  inventory.append("Health potion")
                  print("Health potion added to your inventory")
                  healthpot1 = 1
            else:
                  print("You did not pick it up.")
      if action1 == 3:
            print("You steal the guards key and open the lock.")
            print("You quietly step out into the hallway, trying not to wake the guard.")
            break
                             

print("Suddenly the guard wakes and sees you. He shouts and draws his sword.")
print("You enter battle.")
print("The guard has 20 health, 3 damage and 3 speed.")

fight1 = 0
a = 0
while guardhealth > 0 and archerhealth > 0 and barbarianhealth > 0 and dragonhealth > 0 and goblinhealth > 0 and wizardhealth > 0:
      from random import randint
      choices = randint(1, 3)
      a = a + 1
      print("1, to attack")
      print("2, to block")
      fight1 = int(input("3, to dodge: "))
      
      if yourweapon == 0:
            print("You forgot to pick up your weapon. You are unable to defend yourself.")
            dead()
      elif archerhealth <= 0 or barbarianhealth <= 0 or dragonhealth <= 0 or goblinhealth <= 0 or wizardhealth <= 0:
            print("The guard has slain you on his previous attack.")
            dead()
      
      elif  choices == 1 and fight1 == 1:
            if choicec == 1:
                  archerhealth = archerhealth - 3
                  print("The guard attacks you. You are at", archerhealth, "health.")
                  guardhealth = guardhealth - 14
                  print("The guard is at", guardhealth, "health.")
                  
            elif choicec == 2:
                  barbarianhealth = barbarianhealth - 3
                  print("The guard attacks you. You are at", barbarianhealth, "health.")
                  guardhealth = guardhealth - 16
                  print("The guard is at", guardhealth, "health.")
                  
            elif choicec == 3:
                  dragonhealth = dragonhealth - 3
                  print("The guard attacks you. You are at", dragonhealth, "health.")
                  guardhealth = guardhealth - 14
                  print("The guard is at", guardhealth, "health.")
                  
            elif choicec == 4:
                  goblinhealth = goblinhealth - 3
                  print("The guard attacks you. You are at", goblinhealth, "health.")
                  guardhealth = guardhealth - 16
                  print("The guard is at", guardhealth, "health.")
                  
            elif choicec == 5:
                  wizardhealth = wizardhealth - 3
                  print("The guard attacks you. You are at", wizardhealth, "health.")
                  guardhealth = guardhealth - 19
                  print("The guard is at", guardhealth, "health.")
                  
      elif choices == 2 and fight1 == 1:
            if choicec == 1:
                  guardhealth = guardhealth - 11
                  print("The guard tried to block your attack and reduced its damage. He is at", guardhealth, "health.")
            elif choicec == 2:
                  guardhealth = guardhealth - 13
                  print("The guard tried to block your attack and reduced its damage. He is at", guardhealth, "health.")
            elif choicec == 3:
                  guardhealth = guardhealth - 11
                  print("The guard tried to block your attack and reduced its damage. He is at", guardhealth, "health.")
            elif choicec == 4:
                  guardhealth = guardhealth - 13
                  print("The guard tried to block your attack and reduced its damage. He is at", guardhealth, "health.")
            elif choicec == 5:
                  guardhealth = guardhealth - 16
                  print("The guard tried to block your attack and reduced its damage. He is at", guardhealth, "health.")
      elif choices == 2 and fight1 == 2:
            print("You both try to block, nothing happens...")

      elif a%2 != 0 and choices == 1 and fight1 == 2:
            
            if choicec == 1:
                  archerhealth = archerhealth - 2
                  print("The guard attacks you but you defend and it reduce its damage. You are at", archerhealth, "health.")
            elif choicec == 2:
                  barbarianhealth = barbarianhealth - 2
                  print("The guard attacks you but you defend and reduce its damage. You are at", barbarianhealth, "health.")
            elif choicec == 3:
                  dragonhealth = dragonhealth - 1
                  print("The guard attacks you but you defend it and reduce its damage. You are at", dragonhealth, "health.")
            elif choicec == 4:
                  goblinhealth = goblinhealth - 1
                  print("The guard attacks you but you defend it and reduce its damage. You are at", goblinhealth, "health.")
            elif choicec == 5:
                  wizardhealth = wizardhealth - 2
                  print("The guard attacks you but you defend it and reduce its damage. You are at", wizardhealth, "health.")
                  
      elif a%2 == 0 and choices == 1:
            print("The guard stumbles...")

      elif choices == 1 and a%2 != 0 and fight1 == 3:
            archerdodge = randint(1,10)
            barbariandodge = randint(1,10)
            dragondodge = randint(1,10)
            goblindodge = randint(1,10)
            wizarddodge = randint(1,10)
            if choicec == 1:
                  if archerdodge > 2:
                        print("You successfully dodged his attack")
                  elif archerdodge <= 2:
                        archerhealth = archerhealth - 3
                        print("You could not dodge his attack. You are at", archerhealth," health.")
            elif choicec == 2:
                  if barbariandodge > 4:
                        print("You successfully dodged his attack")
                  elif barbariandodge <= 4:
                        barbarianhealth = barbarianhealth - 3
                        print("You could not dodge his attack. You are at", barbarianhealth," health.")
            elif choicec == 3:
                  if dragondodge > 6:
                        print("You successfully dodged his attack")
                  elif dragondodge <= 6:
                        dragonhealth = dragonhealth - 3
                        print("You could not dodge his attack. You are at", dragonhealth," health.")
            elif choicec == 4:
                  if goblindodge > 8:
                        print("You successfully dodged his attack")
                  elif goblindodge <= 8:
                        goblinhealth = goblinhealth - 3
                        print("You could not dodge his attack. You are at", goblinhealth," health.")
            elif choicec == 5:
                  if wizarddodge > 4:
                        print("You successfully dodged his attack")
                  elif wizarddodge <= 4:
                        wizardhealth = wizardhealth - 3
                        print("You could not dodge his attack. You are at", wizardhealth," health.")

      elif choices == 3 and fight1 == 2:
            print("Nothing happens because you tried to block and the guard tried to dodge.")

      elif choices == 2 and fight1 == 3:
            print("Nothing happens because you tried to dodge and the guard tried to block.")

      elif choices == 3 and fight1 == 3:
            print("You both tried to dodge... Nothing happens.")

      elif choices == 3 and fight1 == 1:
            guarddodge = randint(1, 10)
            if guarddodge > 7:
                  print("The guard successfully dodged your attack.")
            elif guarddodge <= 7:
                  print("The guard tried to dodge your attack but could not.")
                  if choicec == 1:
                        guardhealth = guardhealth - 14
                        print("The guard is at", guardhealth, "health.")
                  elif choicec == 2:
                        guardhealth = guardhealth - 16
                        print("The guard is at", guardhealth, "health.")
                  elif choicec == 3:
                        guardhealth = guardhealth - 14
                        print("The guard is at", guardhealth, "health.")
                  elif choicec == 4:
                        guardhealth = guardhealth - 16
                        print("The guard is at", guardhealth, "health.")
                  elif choicec == 5:
                        guardhealth = guardhealth - 19
                        print("The guard is at", guardhealth, "health.")
if archerhealth <= 0 or barbarianhealth <= 0 or dragonhealth <= 0 or goblinhealth <= 0 or wizardhealth <= 0:
      dead()
print(" ")
print("You have successfully slain the guard.")
print(" ")
while healthpot1 == 1:
      print(" ")
      if choicec == 1:
            print("You are currently at", archerhealth,"health and you started with 7 health.")
            deletehppot = input("Would you like to use it and be retored to full health? (yes/no) ")
            if deletehppot == "yes":
                  healthpot1 = 0
                  archerhealth = 7
                  print("You have been restored to", archerhealth," health.")
            elif deletehppot == "no":
                  print("You are still at", archerhealth," health.")
                  break
      elif choicec == 2:
            print("You are currently at", barbarianhealth,"health and you started with 6 health.")
            deletehppot = input("Would you like to use it and be retored to full health? (yes/no) ")
            if deletehppot == "yes":
                  healthpot1 = 0
                  barbarianhealth = 6
                  print("You have been restored to", barbarianhealth," health.")
            elif deletehppot == "no":
                  print("You are still at", barbarianhealth," health.")
                  break
      elif choicec == 3:
            print("You are currently at", dragonhealth,"health and you started with 12 health.")
            deletehppot = input("Would you like to use it and be retored to full health? (yes/no) ")
            if deletehppot == "yes":
                  healthpot1 = 0
                  dragonhealth = 12
                  print("You have been restored to", dragonhealth," health.")
            elif deletehppot == "no":
                  print("You are still at", dragonhealth," health.")
                  break
      elif choicec == 4:
            print("You are currently at", goblinhealth,"health and you started with 12 health.")
            deletehppot = input("Would you like to use it and be retored to full health? (yes/no) ")
            if deletehppot == "yes":
                  healthpot1 = 0
                  goblinhealth = 12
                  print("You have been restored to", goblinhealth," health.")
            elif deletehppot == "no":
                  print("You are still at", goblinhealth," health.")
                  break
      elif choicec == 5:
            print("You are currently at", wizardhealth,"health and you started with 4 health.")
            deletehppot = input("Would you like to use it and be retored to full health? (yes/no) ")
            if deletehppot == "yes":
                  healthpot1 = 0
                  wizardhealth = 4
                  print("You have been restored to", wizardhealth," health.")
            elif deletehppot == "no":
                  print("You are still at", wizardhealth," health.")
                  break
print(" ")
print("You look down the hallway and see a staircase up to the surface.")
print("What would you like to do?")
print(" ")
action1 = 0
b = 0
healthpot1 = 0
yourweapon = 0
while action1 != 3:
      print("1, Follow the staircase")
      print("2, Go through a hallway beside you instead of the staircase to the surface")
      action1 = int(input("3, Use the guards radio to call for help: "))
      if action1 == 1:
            print(" ")
            print("You follow the staircase, but the iron door to the surface is sealed")
            print("shut, and there's no way you're going to be able to open it.")
            print(" ")

      if action1 == 2:
            print(" ")
            print("You look around the wall and see that there is nobody in sight.")
            print("You proceed into the hallway. Suddenly, you start to hear a gaurds footsteps approcahing. The gaurd sees you.")
            print(" ")
            break

      if action1 == 3:
            print(" ")
            print("You aproach the guards radio and press the dispatch button to radio for help. Unfortunately, there isn't and radio signal underground.")
            print("You return back to the bottom of the staircase and the hallway..")
            print(" ")


guard2health = 40
guard2damage = 4
guard2speed = 5
guard2health2 = 30
guard2damage2 = 5
guard2speed2 = 5
guard2health3 = 40
guard2damage3 = 6
guard2speed3 = 6

print("You enter battle.")
print("The guard has 40 health, 4 damage and 5 speed.")
print(" ")

fight = 0
a = 0
while guard2health > 0 and archerhealth > 0 and barbarianhealth > 0 and dragonhealth > 0 and goblinhealth > 0 and wizardhealth > 0:
      from random import randint
      choices = randint(1, 3)
      a = a + 1
      print("1, to attack")
      print("2, to block")
      fight1 = int(input("3, to dodge: "))
      
      if archerhealth <= 0 or barbarianhealth <= 0 or dragonhealth <= 0 or goblinhealth <= 0 or wizardhealth <= 0:
            print("The guard has slain you on his previous attack.")
            dead()
      
      elif  choices == 1 and fight1 == 1:
            if choicec == 1:
                  archerhealth = archerhealth - 3
                  print("The guard attacks you. You are at", archerhealth, "health.")
                  guard2health = guard2health - 14
                  print("The guard is at", guard2health, "health.")
                  
            elif choicec == 2:
                  barbarianhealth = barbarianhealth - 3
                  print("The guard attacks you. You are at", barbarianhealth, "health.")
                  guard2health = guard2health - 16
                  print("The guard is at", guard2health, "health.")
                  
            elif choicec == 3:
                  dragonhealth = dragonhealth - 3
                  print("The guard attacks you. You are at", dragonhealth, "health.")
                  guard2health = guard2health - 14
                  print("The guard is at", guard2health, "health.")
                  
            elif choicec == 4:
                  goblinhealth = goblinhealth - 3
                  print("The guard attacks you. You are at", goblinhealth, "health.")
                  guard2health = guard2health - 16
                  print("The guard is at", guard2health, "health.")
                  
            elif choicec == 5:
                  wizardhealth = wizardhealth - 3
                  print("The guard attacks you. You are at", wizardhealth, "health.")
                  guard2health = guard2health - 19
                  print("The guard is at", guard2health, "health.")
                  
      elif choices == 2 and fight1 == 1:
            if choicec == 1:
                  guard2health = guard2health - 11
                  print("The guard tried to block your attack and reduced its damage. He is at", guard2health, "health.")
            elif choicec == 2:
                  guard2health = guard2health - 13
                  print("The guard tried to block your attack and reduced its damage. He is at", guard2health, "health.")
            elif choicec == 3:
                  guard2health = guard2health - 11
                  print("The guard tried to block your attack and reduced its damage. He is at", guard2health, "health.")
            elif choicec == 4:
                  guard2health = guard2health - 13
                  print("The guard tried to block your attack and reduced its damage. He is at", guard2health, "health.")
            elif choicec == 5:
                  guard2health = guard2health - 16
                  print("The guard tried to block your attack and reduced its damage. He is at", guard2health, "health.")
      elif choices == 2 and fight1 == 2:
            print("You both try to block, nothing happens...")

      elif a%2 != 0 and choices == 1 and fight1 == 2:
            
            if choicec == 1:
                  archerhealth = archerhealth - 2
                  print("The guard attacks you but you defend and it reduce its damage. You are at", archerhealth, "health.")
            elif choicec == 2:
                  barbarianhealth = barbarianhealth - 2
                  print("The guard attacks you but you defend and reduce its damage. You are at", barbarianhealth, "health.")
            elif choicec == 3:
                  dragonhealth = dragonhealth - 1
                  print("The guard attacks you but you defend it and reduce its damage. You are at", dragonhealth, "health.")
            elif choicec == 4:
                  goblinhealth = goblinhealth - 1
                  print("The guard attacks you but you defend it and reduce its damage. You are at", goblinhealth, "health.")
            elif choicec == 5:
                  wizardhealth = wizardhealth - 2
                  print("The guard attacks you but you defend it and reduce its damage. You are at", wizardhealth, "health.")
                  
      elif a%2 == 0 and choices == 1:
            print("The guard stumbles...")

      elif choices == 1 and a%2 != 0 and fight1 == 3:
            archerdodge = randint(1,10)
            barbariandodge = randint(1,10)
            dragondodge = randint(1,10)
            goblindodge = randint(1,10)
            wizarddodge = randint(1,10)
            if choicec == 1:
                  if archerdodge > 2:
                        print("You successfully dodged his attack")
                  elif archerdodge <= 2:
                        archerhealth = archerhealth - 3
                        print("You could not dodge his attack. You are at", archerhealth," health.")
            elif choicec == 2:
                  if barbariandodge > 4:
                        print("You successfully dodged his attack")
                  elif barbariandodge <= 4:
                        barbarianhealth = barbarianhealth - 3
                        print("You could not dodge his attack. You are at", barbarianhealth," health.")
            elif choicec == 3:
                  if dragondodge > 6:
                        print("You successfully dodged his attack")
                  elif dragondodge <= 6:
                        dragonhealth = dragonhealth - 3
                        print("You could not dodge his attack. You are at", dragonhealth," health.")
            elif choicec == 4:
                  if goblindodge > 8:
                        print("You successfully dodged his attack")
                  elif goblindodge <= 8:
                        goblinhealth = goblinhealth - 3
                        print("You could not dodge his attack. You are at", goblinhealth," health.")
            elif choicec == 5:
                  if wizarddodge > 4:
                        print("You successfully dodged his attack")
                  elif wizarddodge <= 4:
                        wizardhealth = wizardhealth - 3
                        print("You could not dodge his attack. You are at", wizardhealth," health.")

      elif choices == 3 and fight1 == 2:
            print("Nothing happens because you tried to block and the guard tried to dodge.")

      elif choices == 2 and fight1 == 3:
            print("Nothing happens because you tried to dodge and the guard tried to block.")

      elif choices == 3 and fight1 == 3:
            print("You both tried to dodge... Nothing happens.")

      elif choices == 3 and fight1 == 1:
            guarddodge = randint(1, 10)
            if guarddodge > 7:
                  print("The guard successfully dodged your attack.")
            elif guarddodge <= 7:
                  print("The guard tried to dodge your attack but could not.")
                  if choicec == 1:
                        guard2health = guard2health - 14
                        print("The guard is at", guard2health, "health.")
                  elif choicec == 2:
                        guard2health = guard2health - 16
                        print("The guard is at", guard2health, "health.")
                  elif choicec == 3:
                        guard2health = guard2health - 14
                        print("The guard is at", guard2health, "health.")
                  elif choicec == 4:
                        guard2health = guard2health - 16
                        print("The guard is at", guard2health, "health.")
                  elif choicec == 5:
                        guard2health = guard2health - 19
                        print("The guard is at", guard2health, "health.")
if archerhealth <= 0 or barbarianhealth <= 0 or dragonhealth <= 0 or goblinhealth <= 0 or wizardhealth <= 0:
      dead()
print(" ")
print("You have successfully slain the guard.")
print(" ")
print("A health potion falls out of the gaurds pocket. Would you like to add it to your inventory?")
addhealthpot1 = input("Do you wish to add it to your inventory? (yes/no) ")
if addhealthpot1 == "yes":
                inventory.append("Health potion")
                print("Health potion added to your inventory")
                healthpot1 = 1
else:
                print("You did not pick it up.")

while healthpot1 == 1:
      print(" ")
      if choicec == 1:
            print("You are currently at", archerhealth,"health and you started with 7 health.")
            deletehppot = input("Would you like to use it and be retored to full health? (yes/no) ")
            if deletehppot == "yes":
                  healthpot1 = 0
                  archerhealth = 7
                  print("You have been restored to", archerhealth," health.")
            elif deletehppot == "no":
                  print("You are still at", archerhealth," health.")
                  break
      elif choicec == 2:
            print("You are currently at", barbarianhealth,"health and you started with 6 health.")
            deletehppot = input("Would you like to use it and be retored to full health? (yes/no) ")
            if deletehppot == "yes":
                  healthpot1 = 0
                  barbarianhealth = 6
                  print("You have been restored to", barbarianhealth," health.")
            elif deletehppot == "no":
                  print("You are still at", barbarianhealth," health.")
                  break
      elif choicec == 3:
            print("You are currently at", dragonhealth,"health and you started with 12 health.")
            deletehppot = input("Would you like to use it and be retored to full health? (yes/no) ")
            if deletehppot == "yes":
                  healthpot1 = 0
                  dragonhealth = 12
                  print("You have been restored to", dragonhealth," health.")
            elif deletehppot == "no":
                  print("You are still at", dragonhealth," health.")
                  break
      elif choicec == 4:
            print("You are currently at", goblinhealth,"health and you started with 12 health.")
            deletehppot = input("Would you like to use it and be retored to full health? (yes/no) ")
            if deletehppot == "yes":
                  healthpot1 = 0
                  goblinhealth = 12
                  print("You have been restored to", goblinhealth," health.")
            elif deletehppot == "no":
                  print("You are still at", goblinhealth," health.")
                  break
      elif choicec == 5:
            print("You are currently at", wizardhealth,"health and you started with 4 health.")
            deletehppot = input("Would you like to use it and be retored to full health? (yes/no) ")
            if deletehppot == "yes":
                  healthpot1 = 0
                  wizardhealth = 4
                  print("You have been restored to", wizardhealth," health.")
            elif deletehppot == "no":
                  print("You are still at", wizardhealth," health.")
                  break
