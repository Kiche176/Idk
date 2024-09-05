import random
import time

# limit the effectiveness of certain attacks against the eye of the storm in the damage formula
# half all arts damage against the great wizard
# reduce the number of stat points awarded, i was way too generous/ this or make the enemies scale ridiculously, either exponentially or logarithmically, to the power or 1.5 ------- I've now reduced the rewards, now all thats left is to buff the enesmies

# in calculateDamage, if a thunder move is used on the eye of the storm, nerf that shit immediately. it only does a 1/5 of the damage

# give some more bosses cool intros

# -------------------------------------------------------------------------------------------------------------------------------------------
# PLAYER
# -------------------------------------------------------------------------------------------------------------------------------------------
class NewPlayer:
    # initialising stats
    def __init__(self):
        self.name = ""
        self.LVL = 1
        self.STR = 5
        self.ART = 5
        self.AGI = 5
        self.DEF = 5
        self.RES = 5
        self.staminaStat = 5
        self.manaStat = 5
        self.healthStat = 10

        self.maxStamina = self.staminaStat * 4
        self.maxMana= self.manaStat * 4
        self.maxHealth = self.healthStat * 4

        self.currentStamina = self.maxStamina  
        self.currentMana = self.maxMana
        self.currentHealth = self.maxHealth       

        self.moves = [skip, switch, meditate]
        self.skills = []
        self.spells = []
        self.status = ""
        self.job = ""
        self.currentWeapon = unarmed
        self.weapons = [unarmed]
        self.DoT = {'Name': "",
                    'Action Type': "",
                    "Multiplier": 0,
                    "Element": "",
                    "Target Type": "Single",
                    "Damage Type": "Normal",
                    "Ticks Left": 0}


    # getting a name
    def setName(self):
        while True:
            choice = input(f"What is your name, young {self.job.lower()}? ")
            if len(choice) < 1:
                print("Name is too short")
            elif len(choice) > 20:
                print("Name is too long")
            else:
                self.name = choice.title()
                break
    

    # displaying stats
    def displayStats(self):
        print("_____CURRENT STATS_____")
        print(f"Job        : {self.job} \nLevel      : {self.LVL} \nWeapon     : {self.currentWeapon['Name']} \nStrength   : {self.STR} \nArts       : {self.ART} \nAgility    : {self.AGI} \nDefense    : {self.DEF} \nResistance : {self.RES} \nStamina    : {int(self.currentStamina)}/{int(self.maxStamina)} \nMana       : {int(self.currentMana)}/{int(self.maxMana)} \nHealth     : {int(self.currentHealth)}/{int(self.maxHealth)}")
    
    def displayMoves(self):
        input("Your current moves: [PRESS ENTER] \n")
        for i in range(len(self.moves)):
            print(f"[{i + 1}] {self.moves[i]}")


    # restoring and replenishing stamina, mana and health
    def restoreStamina(self, amount):
        self.currentStamina += amount 
        if self.currentStamina > self.maxStamina:
            self.currentStamina = self.maxStamina  

    def replenishStamina(self):
        self.currentStamina = self.maxStamina   

    def restoreMana(self, amount):
        self.currentMana += amount  
        if self.currentMana > self.maxMana:
            self.currentMana = self.maxMana  

    def replenishMana(self):
        self.currentMana = self.maxMana   

    def restoreHealth(self, amount):
        self.currentHealth += amount  
        if self.currentHealth > self.maxHealth:
            self.currentHealth = self.maxHealth  

    def replenishHealth(self):
        self.currentHealth = self.maxHealth

    def replenishStats(self):
        self.replenishStamina()
        self.replenishMana()
        self.replenishHealth()  


    # adding levels to stats  
    def increaseSTR(self, points):
        self.STR += points
    
    def increaseART(self, points):
        self.ART += points
    
    def increaseAGI(self, points):
        self.AGI += points
    
    def increaseDEF(self, points):
        self.DEF += points
    
    def increaseRES(self, points):
        self.RES += points
    
    def increaseStaminaStat(self, points):
        self.staminaStat += points

        difference = self.maxStamina - self.currentStamina
        self.maxStamina += int(points * 4)
        self.currentStamina = int(self.maxStamina - difference)
    
    def increaseManaStat(self, points):
        self.manaStat += points

        difference = self.maxMana - self.currentMana
        self.maxMana += int(points * 4)
        self.currentMana = int(self.maxMana - difference)
    
    def increaseHealthStat(self, points):
        self.healthStat += points

        difference = self.maxHealth - self.currentHealth
        self.maxHealth += int(points * 4)
        self.currentHealth = int(self.maxHealth - difference)


    # gaining a new weapon
    def addWeapon(self, weapon):
        if weapon not in self.weapons:
            self.weapons.append(weapon)
    
    # equip your first weapon
    def equipWeapon(self, weapon):
        if weapon in self.weapons:
            self.currentWeapon = weapon

    # switching weapon
    def switchWeapon(self):
        statement = ("Do you wish to equip: ")
        for i in range(len(self.weapons)):
            if i == len(self.weapons) - 2:
                statement += f"[{i + 1}] {self.weapons[i]['Name']} "
            elif i == len(self.weapons) - 1:
                statement += f"or [{i + 1}] {self.weapons[i]['Name']}? "
            else:
                statement += f"[{i + 1}] {self.weapons[i]['Name']}, "
        
        while True:
            choice = input(statement).title()
            if choice.isdigit():
                choice = int(choice)
                if 0 < choice <= len(self.weapons):
                    self.currentWeapon = self.weapons[choice - 1]
                    input(f"You have equipped {self.currentWeapon['Name']}. [PRESS ENTER]")
                    break

            else:
                for weapon in self.weapons:
                    if choice == weapon['Name']:
                        self.currentWeapon == weapon
                        input(f"You have equipped {self.currentWeapon['Name']}. [PRESS ENTER]")
                    break
            input("Please enter the number or name of your desired weapon. [PRESS ENTER]")
            

    # learing a new move
    def addMove(self, move):
        if move not in self.moves:
            self.moves.append(move)

            if move['Action Type'] == "Skill":                
                    self.skills.append(move)

            elif move['Action Type'] == "Spell":
                    self.spells.append(move)

    
    def addMoves(self, moves):
        for move in moves:
            if move not in self.moves:
                self.moves.append(move)
                
                if move['Action Type'] == "Skill":                
                        self.skills.append(move)

                elif move['Action Type'] == "Spell":
                        self.spells.append(move)


    # levelling up
    def incrementLevel(self):
        self.LVL += 1

    
    # allocating new stat points after a level-up
    def allocateStats(self, points):
        stats = [
            ["Strength", self.increaseSTR],
            ["Arts", self.increaseART],
            ["Agility", self.increaseAGI],
            ["Defense", self.increaseDEF],
            ["Resistance", self.increaseRES],
            ["Stamina", self.increaseStaminaStat],
            ["Mana", self.increaseManaStat],
            ["Health", self.increaseHealthStat]
            ]
        if points == 1:
            input(f"You have 1 point to allocate [PRESS ENTER] ")
        else:
            input(f"You have {points} points to allocate [PRESS ENTER] ")

        while points > 0:
            for stat in stats:
                allocationAccepted = False
                while not allocationAccepted:
                    allocation = input(f"How many points would you like to put into the {stat[0]} stat: ")

                    if allocation == "": # an empty sting allocates 0 points
                        allocationAccepted = True

                    elif allocation.isdigit():
                        allocation = int(allocation)
                        if allocation > points:
                            print("You do not have enough points to allocate into this stat. ")
                        elif allocation < 0:
                            print("You cannot allocate a negative number of points. ")
                        else:
                            allocationAccepted = True
                            stat[1](allocation)
                            points -= allocation
                    else:
                        print("Please enter an integer. ")

                if points > 1:
                    print(f"{points} points left. ")

                elif points == 1:
                    print(f"1 point left. ")

                else:
                    break
    
    # BATTLE METHODS
    def battleIntro(self, enemies):
        input(f"You have {self.currentHealth} HP remaining. [PRESS ENTER] ")
        if len(enemies) == 1:
            input(f"There is 1 enemy. [PRESS ENTER]")
        else:
            input(f"There are {len(enemies)} enemies. [PRESS ENTER] ")

        for enemy in enemies:
            input(f"Lv.{enemy.LVL} {enemy.name.upper()} has {enemy.currentHealth} HP remaining. [PRESS ENTER] ")
    

    # battling enemies
    def battle(self, enemies):

        # --------------------------------------------------
        # The player always starts
        # --------------------------------------------------
        playerTurn = True 
        self.battleIntro(enemies)

        while (len(enemies) > 0) and (self.currentHealth > 0):


            # --------------------------------------------------
            # PLAYER'S TURN
            # --------------------------------------------------
            if playerTurn: 

                # --------------------------------------------------
                # CHECKING FOR DOT TICKS
                # --------------------------------------------------
                # enemy ticks
                for dotEnemy in enemies:
                    if dotEnemy.DoT["Ticks Left"] > 0:
                        damage = calculateDamage(self, dotEnemy, dotEnemy.DoT) # you cannot dodge DoT       

                        input(f"{dotEnemy.name.upper()} has been hit by {dotEnemy.DoT['Name'].upper()}'s damage tick. [PRESS ENTER] ")
                        input(f"You have done {damage} damage! [PRESS ENTER]")

                        if damage >= dotEnemy.currentHealth:
                            dotEnemy.currentHealth = 0
                            input(f"{dotEnemy.name.upper()} has 0 HP remaining. [PRESS ENTER] ")
                            input(f"{dotEnemy.name.upper()} has been defeated. [PRESS ENTER] ")
                            enemies.remove(dotEnemy)
                            if len(enemies) == 0: # last enemy defeated
                                input("CONGRATULATIONS! [PRESS ENTER] ")
                                continue
                        
                        else:
                            dotEnemy.currentHealth -= damage
                        input(f"{dotEnemy.name.upper()} has {dotEnemy.currentHealth} HP remaining. [PRESS ENTER] ")
                        print()
                        dotEnemy.DoT["Ticks Left"] -= 1
                
                if len(enemies) == 0:
                    continue
                
                # player ticks
                if self.DoT["Ticks Left"] > 0:
                    damage = calculateDamage(enemy, self, self.DoT) # you cannot dodge DoT       make sure it's the correct enemy in the formula

                    input(f"You have been hit by {self.DoT['Name'].upper()}'s damage tick. [PRESS ENTER] ")
                    input(f"You have done {damage} damage! [PRESS ENTER]")

                    if damage > self.currentHealth:
                        self.currentHealth = 0
                        input("You have died. ")
                        quit()
                    else:
                        input(f"{enemy.DoT['Name'].upper()} has done {damage} damage! [PRESS ENTER] ") # here too
                        self.currentHealth -= damage
                        input(f"You have {self.currentHealth} HP remaining. [PRESS ENTER] ")
                        print()

                    self.DoT["Ticks Left"] -= 1   

                # --------------------------------------------------
                # DISPLAYING STATS
                # --------------------------------------------------
                print(f"\n___Your Stats___\nStamina : {int(self.currentStamina)}/{int(self.maxStamina)} \nMana    : {int(self.currentMana)}/{int(self.maxMana)} \nHealth  : {int(self.currentHealth)}/{int(self.maxHealth)} \n")


                # --------------------------------------------------
                # SELECTING TARGET
                # --------------------------------------------------
                if len(enemies) > 1: # selecting target
                    statement = "Who will you target this turn: "
                    for i in range(len(enemies)):
                        if i == len(enemies) - 2:
                            statement += f"[{i + 1}] {enemies[i].name} "
                        elif i == len(enemies) - 1:
                            statement += f"or [{len(enemies)}] {enemies[-1].name}? "                            
                        else:
                            statement += f"[{i + 1}] {enemies[i].name}, "                    
                    
                    while True:
                        choice = input(statement)
                        choice = choice.title()
                        
                        if choice.isdigit():
                            if 0 < int(choice) <= len(enemies):
                                enemy = enemies[int(choice) - 1]
                                break
                            else:
                                input("Please enter the number or name of the enemy you wish to target. [PRESS ENTER] ")
                        else:
                            for opponent in enemies:
                                if opponent.name == choice:
                                    enemy = opponent
                                    break
                        
                        input("Please enter the number or name of the enemy you wish to target. [PRESS ENTER] ")
                

                else:
                    enemy = enemies[0]

                
                # --------------------------------------------------
                # SELECTING MOVE
                # --------------------------------------------------
                moveExists = False # selecting move
                moveRequirementsMet = False
                while not (moveExists and moveRequirementsMet):
                    moveUsed = input("Enter Move: ").title()

                    for move in self.moves:
                        if moveUsed == move['Name']:
                            moveUsed = move
                            moveExists = True

                            if (moveUsed['Name'] == "Switch") or (moveUsed['Name'] == "Skip") or (moveUsed['Name'] == "Meditate"): # these moves take no stamina/mana to perform
                                moveRequirementsMet = True

                            elif moveUsed not in self.currentWeapon["Performable Moves"]:
                                print("Your current weapon cannot use this move")

                            elif moveUsed['Action Type'] == "Skill":
                                if self.currentStamina < moveUsed["Stamina Cost"]:
                                    print("You do not have enough stamina to use this move. \n")
                                else:
                                    moveRequirementsMet = True
                                    self.currentStamina -= moveUsed["Stamina Cost"]
                            
                            elif moveUsed['Action Type'] == "Spell":
                                if self.currentMana < moveUsed["Mana Cost"]:
                                    print("You do not have enough mana to use this move. \n")
                                else:
                                    moveRequirementsMet = True
                                    self.currentMana -= moveUsed["Mana Cost"]                   
                            

                    if not moveExists:                       
                        input("You do not have this move. [PRESS ENTER] ")
                        print("\nThe moves you have access to are: ")
                        for move in self.moves:
                            print(move['Name'])
                        print()
                
                
                # --------------------------------------------------
                # IF MOVE IS UTILITY, EXECUTE
                # --------------------------------------------------
                if moveUsed['Name'] == "Switch":
                    self.switchWeapon()                               
                elif moveUsed['Name'] == "Skip":
                    self.restoreStamina(skipAmount(self))
                    input(f"You have regained {skipAmount(self)} stamina! [PRESS ENTER]")
                elif moveUsed['Name'] == "Meditate":
                    self.restoreMana(meditateAmount(self))
                    input(f"You have regained {meditateAmount(self)} mana! [PRESS ENTER]")
                elif moveUsed['Name'] == "Heal":
                    self.restoreHealth(healAmount(self))
                    input(f"You have regained {healAmount(self)} health! [PRESS ENTER]")  
                elif moveUsed['Name'] == "Great Heal":
                    self.restoreHealth(greatHealAmount(self))
                    input(f"You have regained {greatHealAmount(self)} health! [PRESS ENTER]")  
                
                # --------------------------------------------------
                # IF MOVE IS ATTACK, CALCULATE DAMAGE
                # --------------------------------------------------
                else:
                    dodged = dodgeChance(enemy, self)

                    if not dodged: # the move has hit
                        damage = calculateDamage(self, enemy, moveUsed)
                        input(f"You have done {damage} damage! [PRESS ENTER]")


                        if damage >= enemy.currentHealth:
                            enemy.currentHealth = 0
                            input(f"{enemy.name.upper()} has 0 HP remaining. [PRESS ENTER] ")
                            input(f"{enemy.name.upper()} has been defeated. [PRESS ENTER] ")
                            enemies.remove(enemy)
                            if len(enemies) == 0: # last enemy defeated
                                input("CONGRATULATIONS! [PRESS ENTER] ")
                                continue
                        
                        else:
                            enemy.currentHealth -= damage
                            input(f"{enemy.name.upper()} has {enemy.currentHealth} HP remaining. [PRESS ENTER] ") # this is the point where the DoT goes left 

                        # --------------------------------------------------
                        # APPLYING DOT TICK
                        # --------------------------------------------------
                        if moveUsed["Damage Type"] == "DoT":
                            enemy.DoT = {'Name': moveUsed['Name'],
                                         'Action Type': moveUsed['Action Type'],
                                         "Multiplier": moveUsed["Tick Info"]["Multiplier"],
                                         "Element": moveUsed["Element"],
                                         "Target Type": moveUsed["Tick Info"]["Target Type"],
                                         "Damage Type": moveUsed["Tick Info"]["Damage Type"],
                                         "Ticks Left": moveUsed["Tick Info"]["Ticks"]}
                    
                        # --------------------------------------------------
                        # CALCULATING SPLASH DAMAGE
                        # --------------------------------------------------    
                        if moveUsed["Target Type"] == "AoE": # if the move was a splash attack we calculate splash damage for all enemies
                            splashEnemies = enemies
                            if enemy in splashEnemies:
                                splashEnemies.remove(enemy)

                            for splashEnemy in splashEnemies:
                                dodged = dodgeChance(splashEnemy, self)

                                if not dodged: # the move has hit
                                    damage = calculateSplashDamage(self, splashEnemy, moveUsed)
                                    input(f"{splashEnemy.name.upper()} has also taken {damage} damage! [PRESS ENTER]")


                                    if damage >= splashEnemy.currentHealth:
                                        splashEnemy.currentHealth = 0
                                        input(f"{splashEnemy.name.upper()} has 0 HP remaining. [PRESS ENTER] ")
                                        input(f"{splashEnemy.name.upper()} has been defeated. [PRESS ENTER] ")
                                        enemies.remove(splashEnemy)
                                        if len(enemies) == 0: # last enemy defeated
                                            input("CONGRATULATIONS! [PRESS ENTER] ")
                                            continue

                                    else:
                                        splashEnemy.currentHealth -= damage
                                    input(f"{splashEnemy.name.upper()} has {splashEnemy.currentHealth} HP remaining. [PRESS ENTER] ")


                                    # --------------------------------------------------
                                    # IF THE SPLASH DAMAGE IS DOT
                                    # --------------------------------------------------
                                    if moveUsed["Damage Type"] == "DoT":
                                        splashEnemy.DoT = {'Name': moveUsed['Name'],
                                                           'Action Type': moveUsed['Action Type'],
                                                           "Multiplier": moveUsed["Tick Info"]["Multiplier"],
                                                           "Element": moveUsed["Element"],
                                                           "Target Type": moveUsed["Tick Info"]["Target Type"],
                                                           "Damage Type": moveUsed["Tick Info"]["Damage Type"],
                                                           "Ticks Left": moveUsed["Tick Info"]["Ticks"]}

                # --------------------------------------------------
                # APPLYING DOT TICK
                # --------------------------------------------------
                if (moveUsed['Name'] == "Skip") or (moveUsed['Name'] == "Meditate") or (moveUsed['Name'] == "Heal") or (moveUsed['Name'] == "Great Heal"):
                    playerTurn = False
                else:
                    playerTurn = turnChance(self, enemy)
            

        
            # --------------------------------------------------
            # ENEMY'S TURN
            # --------------------------------------------------
            else:         
                for enemy in enemies:
                    print()
                    # --------------------------------------------------
                    # CHECKING FOR DOT TICKS
                    # --------------------------------------------------
                    # enemy ticks
                    for dotEnemy in enemies:
                        if dotEnemy.DoT["Ticks Left"] > 0:
                            damage = calculateDamage(self, dotEnemy, dotEnemy.DoT) # you cannot dodge DoT       

                            input(f"{dotEnemy.name.upper()} has been hit by {dotEnemy.DoT['Name'].upper()}'s damage tick. [PRESS ENTER] ")
                            input(f"You have done {damage} damage! [PRESS ENTER]")

                            if damage >= dotEnemy.currentHealth:
                                dotEnemy.currentHealth = 0
                                input(f"{dotEnemy.name.upper()} has 0 HP remaining. [PRESS ENTER] ")
                                input(f"{dotEnemy.name.upper()} has been defeated. [PRESS ENTER] ")
                                enemies.remove(dotEnemy)
                                if len(enemies) == 0: # last enemy defeated
                                    input("CONGRATULATIONS! [PRESS ENTER] ")
                                    continue
                            
                            else:
                                dotEnemy.currentHealth -= damage
                            input(f"{dotEnemy.name.upper()} has {dotEnemy.currentHealth} HP remaining. [PRESS ENTER] ")
                            print()
                            dotEnemy.DoT["Ticks Left"] -= 1
                
                    if len(enemies) == 0:
                        continue
                    
                    # player ticks
                    if self.DoT["Ticks Left"] > 0:
                        damage = calculateDamage(enemy, self, self.DoT) # you cannot dodge DoT       

                        input(f"You have been hit by {self.DoT['Name']}'s damage tick. [PRESS ENTER] ")
                        input(f"You have done {damage} damage! [PRESS ENTER]")

                        if damage > self.currentHealth:
                            self.currentHealth = 0
                            input("You have died. ")
                            quit()
                        else:
                            input(f"{enemy.name.upper()} has done {damage} damage! [PRESS ENTER] ")
                            self.currentHealth -= damage
                            input(f"You have {self.currentHealth} HP remaining. [PRESS ENTER] ")
                            print()

                        self.DoT["Ticks Left"] -= 1   


                    moveRequirementsMet = False

                    while not moveRequirementsMet:

                        # --------------------------------------------------
                        # CHECKING THE SCRIPT
                        # --------------------------------------------------
                        if len(enemy.phasesLeft) > 0:
                            healthPercentage = enemy.currentHealth / enemy.maxHealth * 100
                            for phase in enemy.phasesLeft:
                                if phase["HP Threshold"] > healthPercentage:
                                    enemy.moves = [skip]
                                    enemy.addMoves(phase["Moveset"])
                                    enemy.phasesLeft.remove(phase) # this removes the phase from the list

                                    if phase["Scripted Move"] != None:
                                        moveUsed = phase["Scripted Move"]
                                    else:
                                        moveUsed = random.choice(enemy.moves)

                            else:
                                moveUsed = random.choice(enemy.moves)

                            if moveUsed['Action Type'] == "Skill":
                                if enemy.currentStamina < moveUsed["Stamina Cost"]:
                                    continue
                                elif moveUsed == skip:
                                    if enemy.currentStamina == enemy.maxStamina:
                                        continue
                                else:
                                    moveRequirementsMet = True
                                    if moveUsed['Name'] == "Skip":
                                        input(f"{enemy.name.upper()} has skipped a turn. [PRESS ENTER] ")
                                    else:
                                        input(f"{enemy.name.upper()} has used the skill {moveUsed['Name']}! [PRESS ENTER] ")
                                    
                            elif moveUsed['Action Type'] == "Spell":
                                if enemy.currentMana < moveUsed["Mana Cost"]:
                                    continue
                                elif moveUsed == meditate:
                                    if enemy.currentMana == enemy.maxMana:
                                        continue
                                else:
                                    moveRequirementsMet = True
                                    input(f"{enemy.name.upper()} has used the spell {moveUsed['Name']}! [PRESS ENTER] ")

                        # --------------------------------------------------
                        # IF MOVE IS UTILITY, EXECUTE
                        # --------------------------------------------------                                                 
                        if moveUsed['Name'] == "Skip":
                            enemy.restoreStamina(skipAmount(enemy))
                            input(f"{enemy.name.upper()} has regained {skipAmount(enemy)} stamina! [PRESS ENTER]")
                        elif moveUsed['Name'] == "Meditate":
                            enemy.restoreMana(meditateAmount(enemy))
                            input(f"{enemy.name.upper()} has regained {meditateAmount(enemy)} mana! [PRESS ENTER]")
                        elif moveUsed['Name'] == "Heal":
                            enemy.restoreHealth(healAmount(enemy))
                            input(f"{enemy.name.upper()} has regained {healAmount(enemy)} health! [PRESS ENTER]") 
                        elif moveUsed['Name'] == "Great Heal":
                            enemy.restoreHealth(greatHealAmount(enemy))
                            input(f"{enemy.name.upper()} has regained {greatHealAmount(enemy)} health! [PRESS ENTER]")  
                        
                        
                        # --------------------------------------------------
                        # IF MOVE IS ATTACK, CALCULATE DAMAGE
                        # --------------------------------------------------                                                                         
                        else: 
                            dodged = dodgeChance(self, enemy)
                            if not dodged: # the move has hit
                                damage = calculateDamage(enemy, self, moveUsed)

                                if damage >= self.currentHealth:
                                    self.currentHealth = 0
                                    input("You have died. ")
                                    quit()
                                else:
                                    input(f"{enemy.name.upper()} has done {damage} damage! [PRESS ENTER] ")
                                    self.currentHealth -= damage
                                    input(f"You have {self.currentHealth} HP remaining. [PRESS ENTER] ")
                                
                                
                                # --------------------------------------------------
                                # APPLYING DOT TICK
                                # --------------------------------------------------
                                if moveUsed["Damage Type"] == "DoT":
                                    self.DoT = {'Name': moveUsed['Name'],
                                                'Action Type': moveUsed['Action Type'],
                                                "Multiplier": moveUsed["Tick Info"]["Multiplier"],
                                                "Element":  moveUsed["Element"],
                                                "Target Type": moveUsed["Tick Info"]["Target Type"],
                                                "Damage Type": "Normal",
                                                "Ticks Left": moveUsed["Tick Info"]["Ticks"]}
                                    

                        # the chance that the enemy gets another turn
                        if (moveUsed['Name'] == "Skip") or (moveUsed['Name'] == "Meditate") or (moveUsed['Name'] == "Heal") or (moveUsed['Name'] == "Great Heal"):
                            enemyRepeat = False
                        else:
                            enemyRepeat = turnChance(enemy, self)
                        
                        if enemy == enemies[-1]:
                            if not enemyRepeat:
                                playerTurn = True


# -------------------------------------------------------------------------------------------------------------------------------------------
# ENEMIES
# -------------------------------------------------------------------------------------------------------------------------------------------
class Enemy:

    def __init__(self, enemyName, enemyLevel):
        self.name = enemyName
        self.LVL = enemyLevel
        self.STR = 0
        self.ART = 0
        self.AGI = 0
        self.DEF = 0
        self.RES = 0
        self.staminaStat = 0
        self.manaStat = 0
        self.healthStat = 1

        self.maxStamina = self.staminaStat * 4
        self.maxMana= self.manaStat * 4
        self.maxHealth = self.healthStat * 4

        self.currentStamina = self.maxStamina  
        self.currentMana = self.maxMana
        self.currentHealth = self.maxHealth

        self.moves = [skip]
        self.skills = []
        self.spells = []
        self.status = ""
        self.job = ""
        self.currentWeapon = unarmed
        self.weapons = [unarmed]
        self.DoT = {'Name': "",
                    'Action Type': "",
                    "Multiplier": 0,
                    "Element": "",
                    "Target Type": "Single",
                    "Damage Type": "",
                    "Ticks Left": 0}
        
        self.phasesLeft = [{"HP Threshold" : -1,
                            "Moveset" : None,
                            "Scripted Move" : None}]
    
    
    # displaying stats
    def displayStats(self):
        print(f"Level : {self.LVL} \nStrength : {self.STR} \nArts : {self.ART} \nAgility : {self.AGI} \nDefense : {self.DEF} \nResistance : {self.RES} \nStamina : {self.currentStamina}/{self.maxStamina} \nMana : {self.currentMana}/{self.maxMana} \nHealth : {self.currentHealth}/{self.maxHealth}")


    # restoring and replenishing stamina, mana and health
    def restoreStamina(self, amount):
        self.currentStamina += amount  

    def replenishStamina(self):
        self.currentStamina += self.maxStamina   

    def restoreMana(self, amount):
        self.currentMana += amount  

    def replenishMana(self):
        self.currentMana += self.maxMana   

    def restoreHealth(self, amount):
        self.currentHealth += amount  

    def replenishHealth(self):
        self.currentHealth += self.maxHealth   
    
    
    # learing a new move
    def addMove(self, move):
        if move not in self.moves:
            self.moves.append(move)

            if move['Action Type'] == "Skill":                
                    self.skills.append(move)

            elif move['Action Type'] == "Spell":
                    self.spells.append(move)

    
    def addMoves(self, moves):
        for move in moves:
            if move not in self.moves:
                self.moves.append(move)
                
                if move['Action Type'] == "Skill":                
                        self.skills.append(move)

                elif move['Action Type'] == "Spell":
                        self.spells.append(move)


    # gaining a new weapon
    def addWeapon(self, weapon):
        if weapon not in self.weapons:
            self.weapons.append(weapon)
    
    # equip your first weapon
    def equipWeapon(self, weapon):
        if weapon in self.weapons:
            self.currentWeapon = weapon


class ClubOgre(Enemy):
    def __init__(self, enemyName, enemyLevel):
        super().__init__(enemyName, enemyLevel)
        self.STR = 10 + self.LVL * 5
        self.ART = 5 + self.LVL * 2
        self.AGI = 15
        self.DEF = 10 + self.LVL * 2
        self.RES = 4 + self.LVL * 1

        self.staminaStat = int(10 + self.LVL * 1.25)
        self.manaStat = int(10 + self.LVL / 4)
        self.healthStat = int(12.5 + self.LVL * 3.75)

        self.maxStamina = self.staminaStat * 4
        self.maxMana= self.manaStat * 4
        self.maxHealth = self.healthStat * 4

        self.currentStamina = self.maxStamina  
        self.currentMana = self.maxMana
        self.currentHealth = self.maxHealth

        self.job = "Club Ogre"

        self.addMoves([skillBash, skillBonk])       
        self.addWeapon(club)
        self.equipWeapon(club)


class FlameOgre(Enemy):
    def __init__(self, enemyName, enemyLevel):
        super().__init__(enemyName, enemyLevel)
        self.STR = 10 + self.LVL * 2
        self.ART = 10 + self.LVL * 5
        self.AGI = 15 + self.LVL
        self.DEF = 10 + self.LVL * 1
        self.RES = 10 + self.LVL * 2

        self.staminaStat = int(5 + self.LVL * 1.25)
        self.manaStat = int(7.5 + self.LVL * 2.5)
        self.healthStat = int(12.5 + self.LVL * 2.5)

        self.maxStamina = self.staminaStat * 4
        self.maxMana= self.manaStat * 4
        self.maxHealth = self.healthStat * 4

        self.currentStamina = self.maxStamina  
        self.currentMana = self.maxMana
        self.currentHealth = self.maxHealth

        self.job = "Flame Ogre"

        self.addMoves([skillBonk, spellEmber])  
        self.addWeapon(club)
        self.equipWeapon(club)


class Oni(Enemy):
    def __init__(self, enemyName, enemyLevel):
        super().__init__(enemyName, enemyLevel)
        self.STR = 10 + self.LVL * 5
        self.ART = 10
        self.AGI = 10 + self.LVL * 3
        self.DEF = 10 + self.LVL * 2
        self.RES = 4 + self.LVL * 2

        self.staminaStat = int(10 + self.LVL * 1.25)
        self.manaStat = int(10 + self.LVL / 4)
        self.healthStat = int(12.5 + self.LVL * 3)

        self.maxStamina = self.staminaStat * 4
        self.maxMana= self.manaStat * 4
        self.maxHealth = self.healthStat * 4

        self.currentStamina = self.maxStamina  
        self.currentMana = self.maxMana
        self.currentHealth = self.maxHealth

        self.job = "Club Ogre"

        self.addMoves([skillSlash, skillSlice, skillStab, skillDice])       
        self.addWeapon(ironSword)
        self.equipWeapon(ironSword)


class Golem(Enemy):
    def __init__(self, enemyName, enemyLevel):
        super().__init__(enemyName, enemyLevel)
        self.STR = 10 + self.LVL * 4
        self.ART = 5 + self.LVL * 2
        self.AGI = 5
        self.DEF = 20 + self.LVL * 1.75
        self.RES = 10 + self.LVL

        self.staminaStat = int(12.5 + self.LVL * 1.25)
        self.manaStat = int(10 + self.LVL)
        self.healthStat = int(25 + self.LVL * 5)

        self.maxStamina = self.staminaStat * 4
        self.maxMana= self.manaStat * 4
        self.maxHealth = self.healthStat * 4

        self.currentStamina = self.maxStamina  
        self.currentMana = self.maxMana
        self.currentHealth = self.maxHealth
                
        self.job = "Golem"
        self.status = "rocky"

        self.addMoves([skillBash, spellStone])


class Yeti(Enemy):
    def __init__(self, enemyName, enemyLevel):
        super().__init__(enemyName, enemyLevel)
        self.STR = 15 + self.LVL * 3
        self.ART = 15 + self.LVL * 5
        self.AGI = 15 + self.LVL
        self.DEF = 10 + self.LVL * 2
        self.RES = 12 + self.LVL

        self.staminaStat = int(5 + self.LVL * 2.5)
        self.manaStat = int(7.5 + self.LVL * 2.5)
        self.healthStat = int(12.5 + self.LVL * 3)

        self.maxStamina = self.staminaStat * 4
        self.maxMana= self.manaStat * 4
        self.maxHealth = self.healthStat * 4

        self.currentStamina = self.maxStamina  
        self.currentMana = self.maxMana
        self.currentHealth = self.maxHealth

        self.job = "Yeti"
        self.status = "frosted"

        self.addMoves([skillBash, spellIcicle, spellHailstorm])
        self.currentWeapon = unarmed
        self.weapons = [unarmed]


class LavaHound(Enemy):
    def __init__(self, enemyName, enemyLevel):
        super().__init__(enemyName, enemyLevel)
        self.STR = 15 + self.LVL * 3
        self.ART = 15 + self.LVL * 5
        self.AGI = 10 + self.LVL * 2
        self.DEF = 20 + self.LVL * 2
        self.RES = 5 + self.LVL

        self.staminaStat = int(5 + self.LVL * 2.5)
        self.manaStat = int(7.5 + self.LVL * 2.5)
        self.healthStat = int(12.5 + self.LVL * 3)

        self.maxStamina = self.staminaStat * 4
        self.maxMana= self.manaStat * 4
        self.maxHealth = self.healthStat * 4

        self.currentStamina = self.maxStamina  
        self.currentMana = self.maxMana
        self.currentHealth = self.maxHealth

        self.job = "Lava Hound"
        self.status = "burning"

        self.addMoves([skillBash, spellEmber, spellEruption]) # ignite gone for now
        

class Dullahan(Enemy):
    def __init__(self, enemyName, enemyLevel):
        super().__init__(enemyName, enemyLevel)
        self.STR = 10 + self.LVL * 4
        self.ART = 25
        self.AGI = 15 + self.LVL * 3
        self.DEF = 10 + self.LVL * 2
        self.RES = 4 + self.LVL * 2

        self.staminaStat = int(10 + self.LVL * 3)
        self.manaStat = int(10 + self.LVL * 2)
        self.healthStat = int(12.5 + self.LVL * 3)

        self.maxStamina = self.staminaStat * 4
        self.maxMana= self.manaStat * 4
        self.maxHealth = self.healthStat * 4

        self.currentStamina = self.maxStamina  
        self.currentMana = self.maxMana
        self.currentHealth = self.maxHealth

        self.job = "Club Ogre"

        self.addMoves([skillSlash, skillSlice, skillStab])       
        self.addWeapon(ironSword)
        self.equipWeapon(ironSword)

        self.phasesLeft = [{"HP Threshold" : 50,
                            "Moveset" : [skillSlash, skillSlice, skillStab, skillDice, skillAnnihilation],
                            "Scripted Move" : skillAnnihilation}]


class Storm(Enemy): 
    def __init__(self, enemyName, enemyLevel):
        super().__init__(enemyName, enemyLevel)
        self.STR = 0
        self.ART = 30 + self.LVL * 3
        self.AGI = 40
        self.DEF = 20
        self.RES = 30

        self.staminaStat = 250
        self.manaStat = 250
        self.healthStat = 75

        self.maxStamina = self.staminaStat * 4
        self.maxMana= self.manaStat * 4
        self.maxHealth = self.healthStat * 4

        self.currentStamina = self.maxStamina  
        self.currentMana = self.maxMana
        self.currentHealth = self.maxHealth

        self.job = "Storm"

        self.phasesLeft = [{"HP Threshold" : 100,
                            "Moveset" : [spellGale, spellBolt],
                            "Scripted Move" : spellThunderstorm},

                            {"HP Threshold" : 50,
                            "Moveset" : [spellGale, spellBolt, spellHailstorm, spellThunderstorm, spellTornado, spellKamui, spellWindScythe],
                            "Scripted Move" : spellTornado}]


class GrandMage(Enemy): 
    def __init__(self, enemyName, enemyLevel):
        super().__init__(enemyName, enemyLevel)
        self.STR = 25
        self.ART = 50
        self.AGI = 40
        self.DEF = 20
        self.RES = 40

        self.staminaStat = 20
        self.manaStat = 50
        self.healthStat = 75

        self.maxStamina = self.staminaStat * 4
        self.maxMana= self.manaStat * 4
        self.maxHealth = self.healthStat * 4

        self.currentStamina = self.maxStamina  
        self.currentMana = self.maxMana
        self.currentHealth = self.maxHealth

        self.job = "Grand Mage"

        self.addMoves([meditate, spellBonk])
        for spell in beginnerSpells:
            self.addMove(spell)
             
        self.addWeapon(grandStaff)
        self.equipWeapon(grandStaff)

        self.phasesLeft = [{"HP Threshold" : 60,
                            "Moveset" : advancedSpells,
                            "Scripted Move" : None},
                            
                           {"HP Threshold" : 30,
                            "Moveset" : spells,
                            "Scripted Move" : spellGreatHeal}]


# -------------------------------------------------------------------------------------------------------------------------------------------
# SKILLS
# -------------------------------------------------------------------------------------------------------------------------------------------
# Utility
skip = {
    'Name': "Skip",
    'Action Type': "Skill",
    "Multiplier": 0,
    "Element": "Physical",
    "Target Type": "Single",
    "Damage Type": "",
    "Stamina Cost": 0
}

switch = {
    'Name': "Switch",
    'Action Type': "Skill",
    "Multiplier": 0,
    "Element": "Physical",
    "Target Type": "Single",
    "Damage Type": "",
    "Stamina Cost": 0
}

# Beginner Skills
skillSlash = {
    'Name': "Slash",
    'Action Type': "Skill",
    "Multiplier": 2.5,
    "Element": "Physical",
    "Target Type": "Single",
    "Damage Type": "Slash",
    "Stamina Cost": 10
}

skillStab = {
    'Name': "Stab",
    'Action Type': "Skill",
    "Multiplier": 2,
    "Element": "Physical",
    "Target Type": "Single",
    "Damage Type": "Pierce",
    "Stamina Cost": 10
}

skillBash = {
    'Name': "Bash",
    'Action Type': "Skill",
    "Multiplier": 1.5,
    "Element": "Physical",
    "Target Type": "Single",
    "Damage Type": "Blunt",
    "Stamina Cost": 5
}

skillClobber = {
    'Name': "Clobber",
    'Action Type': "Skill",
    "Multiplier": 2.5,
    "Element": "Physical",
    "Target Type": "Single",
    "Damage Type": "Blunt",
    "Stamina Cost": 7
}

skillBonk = {
    'Name': "Bonk",
    'Action Type': "Skill",
    "Multiplier": 2,
    "Element": "Physical",
    "Damage Type": "Blunt",
    "Stamina Cost": 5
}

skillPunch = {
    'Name': "Punch",
    'Action Type': "Skill",
    "Multiplier": 1,
    "Element": "Physical",
    "Target Type": "Single",
    "Damage Type": "Blunt",
    "Stamina Cost": 5
}

skillKick = {
    'Name': "Kick",
    'Action Type': "Skill",
    "Multiplier": 1,
    "Element": "Physical",
    "Target Type": "Single",
    "Damage Type": "Blunt",
    "Stamina Cost": 5
}

# Advanced Skills
skillSlice = {
    'Name': "Slice",
    'Action Type': "Skill",
    "Multiplier": 3,
    "Element": "Physical",
    "Target Type": "Single",
    "Damage Type": "Slash",
    "Stamina Cost": 20
}

skillDice = {
    'Name': "Dice",
    'Action Type': "Skill",
    "Multiplier": 2.5,
    "Element": "Physical",
    "Target Type": "Single",
    "Damage Type": "Pierce",
    "Stamina Cost": 15
}

skillDecimate = {
    'Name': "Decimate",
    'Action Type': "Skill",
    "Multiplier": 5,
    "Element": "Physical",
    "Target Type": "Single",
    "Damage Type": "AoE",
    "Stamina Cost": 35
}

skillShieldCharge = {
    'Name': "Shield Charge",
    'Action Type': "Skill",
    "Multiplier": 2.5,
    "Element": "Physical",
    "Target Type": "Single",
    "Damage Type": "Blunt",
    "Stamina Cost": 10
}

skillNeedleRain = {
    'Name': "Needle Rain",
    'Action Type': "Skill",
    "Multiplier": 4,
    "Element": "Physical",
    "Target Type": "AoE",
    "Damage Type": "Pierce",
    "Stamina Cost": 25
}

skillAnnihilation = {
    'Name': "Annihilation",
    'Action Type': "Skill",
    "Multiplier": 8,
    "Element": "Physical",
    "Target Type": "Single",
    "Damage Type": "Slash",
    "Stamina Cost": 75
}

# -------------------------------------------------------------------------------------------------------------------------------------------
# SPELLS
# -------------------------------------------------------------------------------------------------------------------------------------------
# Utility
spellHeal = {
    'Name': "Heal",
    'Action Type': "Spell",
    "Multiplier": 0,
    "Element": "",
    "Target Type": "Single",
    "Damage Type": "",
    "Mana Cost": 10
}

meditate = {
    'Name': "Meditate",
    'Action Type': "Spell",
    "Multiplier": 0,
    "Element": "",
    "Target Type": "Single",
    "Damage Type": "",
    "Mana Cost": 0
}

spellBonk = {
    'Name': "Bonk",
    'Action Type': "Spell",
    "Multiplier": 1.5,
    "Element": "Physical",
    "Damage Type": "Blunt",
    "Mana Cost": 0
}

# Beginner Spells
spellEmber = {
    'Name': "Ember",
    'Action Type': "Spell",
    "Multiplier": 1.5,
    "Element": "Fire",
    "Target Type": "Single",
    "Damage Type": "Normal",
    "Mana Cost": 10
}

spellSplash = {
    'Name': "Splash",
    'Action Type': "Spell",
    "Multiplier": 1.5,
    "Element": "Water",
    "Target Type": "Single",
    "Damage Type": "Normal",
    "Mana Cost": 10
}

spellIcicle = {
    'Name': "Icicle",
    'Action Type': "Spell",
    "Multiplier": 1,
    "Element": "Ice",
    "Target Type": "Single",
    "Damage Type": "Pierce",
    "Mana Cost": 10
}

spellStone = {
    'Name': "Stone",
    'Action Type': "Spell",
    "Multiplier": 2,
    "Element": "Earth",
    "Target Type": "Single",
    "Damage Type": "Blunt",
    "Mana Cost": 10
}

spellGale = {
    'Name': "Gale",
    'Action Type': "Spell",
    "Multiplier": 1.5,
    "Element": "Wind",
    "Target Type": "Single",
    "Damage Type": "Normal",
    "Mana Cost": 10
}

spellBolt = {
    'Name': "Bolt",
    'Action Type': "Spell",
    "Multiplier": 1.5,
    "Element": "Thunder",
    "Target Type": "Single",
    "Damage Type": "Pierce",
    "Mana Cost": 10
}

# Advanced Spells
spellEruption = {
    'Name': "Eruption",
    'Action Type': "Spell",
    "Multiplier": 2,
    "Element": "Fire",
    "Target Type": "Single",
    "Damage Type": "AoE",
    "Mana Cost": 25
}

spellIgnite = {
    'Name': "Ignite",
    'Action Type': "Spell",
    "Multiplier": 2,
    "Element": "Fire",
    "Target Type": "Single",
    "Damage Type": "DoT",
    "Mana Cost": 40,
    "Tick Info": {"Multiplier": 0.25,
                  "Target Type": "Single",
                  "Damage Type": "Normal",
                  "Ticks": 3}
}

spellTsunami = {
    'Name': "Tsunami",
    'Action Type': "Spell",
    "Multiplier": 2,
    "Element": "Water",
    "Target Type": "AoE",
    "Damage Type": "Normal",
    "Mana Cost": 25
}

spellWaterfall = {
    'Name': "Waterfall",
    'Action Type': "Spell",
    "Multiplier": 2,
    "Element": "Water",
    "Target Type": "Single",
    "Damage Type": "Normal",
    "Mana Cost": 25
}

spellHailstorm = {
    'Name': "Hailstorm",
    'Action Type': "Spell",
    "Multiplier": 2,
    "Element": "Ice",
    "Target Type": "AoE",
    "Damage Type": "Pierce",
    "Mana Cost": 20
}

spellIceLance = {
    'Name': "Ice Lance",
    'Action Type': "Spell",
    "Multiplier": 2,
    "Element": "Ice",
    "Target Type": "Single",
    "Damage Type": "Pierce",
    "Mana Cost": 20
}

spellRockslide = {
    'Name': "Rockslide",
    'Action Type': "Spell",
    "Multiplier": 2,
    "Element": "Earth",
    "Target Type": "AoE",
    "Damage Type": "Normal",
    "Mana Cost": 20
}

spellPlanetaryDevastation = {
    'Name': "Planetary Devastation",
    'Action Type': "Spell",  
    "Multiplier": 5,
    "Element": "Earth",
    "Target Type": "AoE",
    "Damage Type": "Blunt",
    "Mana Cost": 80
}

spellWindScythe = {
    'Name': "Wind Scythe",
    'Action Type': "Spell",
    "Multiplier": 2,
    "Element": "Wind",
    "Target Type": "Single",
    "Damage Type": "Normal",
    "Mana Cost": 20
}

spellTornado = {
    'Name': "Tornado",
    'Action Type': "Spell",
    "Multiplier": 2,
    "Element": "Wind",
    "Target Type": "DoT",
    "Damage Type": "Normal",
    "Mana Cost": 20
}

spellKamui = {
    'Name': "Kamui",
    'Action Type': "Spell",
    "Multiplier": 2,
    "Element": "Thunder",
    "Target Type": "Single",
    "Damage Type": "Pierce",
    "Mana Cost": 20
}

spellThunderstorm = {
    'Name': "Thunderstorm",
    'Action Type': "Spell",
    "Multiplier": 2,
    "Element": "Thunder",
    "Target Type": "AoE",
    "Damage Type": "DoT",
    "Mana Cost": 50,
    "Tick Info": {"Multiplier": 0.2,
                  "Target Type": "Single",
                  "Damage Type": "Pierce",
                  "Ticks": 3}
}

spellGreatHeal = {
    'Name': "Great Heal",
    'Action Type': "Spell",
    "Multiplier": 0,
    "Element": "",
    "Target Type": "Single",
    "Damage Type": "",
    "Mana Cost": 25
}


# -------------------------------------------------------------------------------------------------------------------------------------------
# MOVE LISTS
# -------------------------------------------------------------------------------------------------------------------------------------------
beginnerSkills = [skillSlash, skillStab, skillBash, skillClobber, skillPunch, skillKick]

advancedSkills = [skillSlice, skillDice, skillDecimate, skillShieldCharge, skillNeedleRain, skillAnnihilation]

beginnerSpells = [spellEmber, spellSplash, spellIcicle, spellStone, spellGale, spellBolt, spellHeal, spellBonk]

advancedSpells = [spellEruption, spellIgnite, spellTsunami, spellWaterfall, spellIceLance, spellHailstorm, spellRockslide, spellPlanetaryDevastation, spellWindScythe, spellTornado, spellKamui, spellThunderstorm, spellGreatHeal]


skills = [skillSlash, skillStab, skillBash, skillClobber, skillPunch, skillKick, skillSlice, skillDice, skillDecimate, skillShieldCharge, skillNeedleRain, skillAnnihilation]

spells = [spellEmber, spellSplash, spellIcicle, spellStone, spellGale, spellBolt, spellHeal, spellBonk, spellEruption, spellIgnite, spellTsunami, spellWaterfall, spellIceLance, spellHailstorm, spellRockslide, spellPlanetaryDevastation, spellWindScythe, spellTornado, spellKamui, spellThunderstorm, spellGreatHeal]


beginnerMoves = [skillSlash, skillStab, skillBash, skillClobber, skillPunch, skillKick, spellEmber, spellSplash, spellIcicle, spellStone, spellGale, spellBolt, spellHeal, spellBonk]

advancedMoves = [skillSlice, skillDice, skillDecimate, skillShieldCharge, skillNeedleRain, skillAnnihilation, spellEruption, spellIgnite, spellTsunami, spellWaterfall, spellIceLance, spellHailstorm, spellRockslide, spellPlanetaryDevastation, spellWindScythe, spellTornado, spellKamui, spellThunderstorm, spellGreatHeal]


moves = [skillSlash, skillStab, skillBash, skillClobber, skillPunch, skillKick, spellEmber, spellSplash, spellIcicle, spellStone, spellGale, spellBolt, spellHeal, spellBonk, skillSlice, skillDice, skillDecimate, skillShieldCharge, skillNeedleRain, skillAnnihilation, spellEruption, spellIgnite, spellTsunami, spellWaterfall, spellIceLance, spellHailstorm, spellRockslide, spellPlanetaryDevastation, spellWindScythe, spellTornado, spellKamui, spellThunderstorm, spellGreatHeal]


# -------------------------------------------------------------------------------------------------------------------------------------------
# WEAPONS
# -------------------------------------------------------------------------------------------------------------------------------------------
unarmed = {
    'Name': "Unarmed",
    "Additional Stat": {"Type": "", 
                        "Amount": 0},
    "Damage Affinity": "",
    "Performable Moves": [skillPunch, skillKick, skillBonk, spellBonk, spellHeal]
}
# beginner weapons
woodenSword = {
    'Name': "Wooden Sword",
    "Additional Stat": {"Type": "strength", 
                        "Amount": 3},
    "Damage Affinity": "Slash",
    "Performable Moves": [skillSlash, skillStab, skillBonk, skillKick, spellBonk, spellHeal]
}

woodenShield = {
    'Name': "Wooden Shield",
    "Additional Stat": {"Type": "defense", 
                        "Amount": 4},
    "Damage Affinity": "Blunt",
    "Performable Moves": [skillBash, skillBonk, spellBonk, skillClobber, spellHeal]
}

rustyDagger = {
    'Name': "Rusty Dagger",
    "Additional Stat": {"Type": "strength", 
                        "Amount": 2},
    "Damage Affinity": "Pierce",
    "Performable Moves": [skillSlash, skillStab, spellHeal]
}

spellbook = {
    'Name': "Spellbook",
    "Additional Stat": {"Type": "arts", 
                        "Amount": 3},
    "Damage Affinity": "",
    "Performable Moves": [spellBonk, spellEmber, spellSplash, spellIcicle, spellStone, spellGale, spellBolt, spellHeal]
}

# advanced weapons
ironSword = {
    'Name': "Iron Sword",
    "Additional Stat": {"Type": "strength", 
                        "Amount": 8},
    "Damage Affinity": "Slash",
    "Performable Moves": [skillSlash, skillStab, skillBonk, skillSlice, skillDice, skillKick, skillDecimate, skillAnnihilation, spellBonk, spellHeal]
}

ironShield = {
    'Name': "Iron Shield",
    "Additional Stat": {"Type": "defense", 
                        "Amount": 10},
    "Damage Affinity": "Blunt",
    "Performable Moves": [skillBash, skillBonk, skillClobber, skillShieldCharge, spellBonk, spellHeal]
}

needle = {
    'Name': "Needle",
    "Additional Stat": {"Type": "strength", 
                        "Amount": 7},
    "Damage Affinity": "Pierce",
    "Performable Moves": [skillSlash, skillStab, skillDice, skillNeedleRain, skillAnnihilation, spellHeal]
}

staff = {
    'Name': "Staff",
    "Additional Stat": {"Type": "arts", 
                        "Amount": 10},
    "Damage Affinity": "",
    "Performable Moves": [spellBonk, spellEmber, spellSplash, spellIcicle, spellStone, spellGale, spellBolt, spellHeal, spellEruption, spellIgnite, spellTsunami, spellWaterfall, spellIceLance, spellHailstorm, spellRockslide, spellPlanetaryDevastation, spellWindScythe, spellTornado, spellKamui, spellThunderstorm, spellGreatHeal]
}

# boss weapons

club = {
    'Name': "Club",
    "Additional Stat": {"Type": "strength", 
                        "Amount": 5},
    "Damage Affinity": "blunt",
    "Performable Moves": [skillBonk, skillBash, spellBonk, spellHeal]
}

grandStaff = {
    'Name': "Grand Staff",
    "Additional Stat": {"Type": "arts", 
                        "Amount": 15},
    "Damage Affinity": "",
    "Performable Moves": [spellBonk, spellEmber, spellSplash, spellIcicle, spellStone, spellGale, spellBolt, spellHeal, spellEruption, spellIgnite, spellTsunami, spellWaterfall, spellIceLance, spellHailstorm, spellRockslide, spellPlanetaryDevastation, spellWindScythe, spellTornado, spellKamui, spellThunderstorm, spellGreatHeal]
}

beginnerWeapons = [woodenSword, woodenShield, rustyDagger, spellbook]

advancedWeapons = [ironSword, ironShield, needle, staff]


# -------------------------------------------------------------------------------------------------------------------------------------------
# SELECTIONS
# -------------------------------------------------------------------------------------------------------------------------------------------
def classSelection():

    while player.job == "":        
        choice = input("What is your desired job? [TYPE swordsman, assassin, tank or mage] ").lower()
        if choice == "swordsman":
            player.job = "Swordsman"
            player.increaseSTR(20)
            player.increaseART(0)
            player.increaseAGI(10)
            player.increaseDEF(10)
            player.increaseRES(5)
            player.increaseStaminaStat(7.5)
            player.increaseManaStat(2.5)
            player.increaseHealthStat(4)

            player.addMove(skillSlash)
            input("You have learned the skill SLASH. \nWhen in battle, type SLASH to use the skill. [PRESS ENTER] ")
            player.addWeapon(woodenSword)
            player.currentWeapon = woodenSword            
            input("You have picked up a wooden sword. [PRESS ENTER]")


        elif choice == "assassin":
            player.job = "Assassin"
            player.increaseSTR(15)
            player.increaseART(5)
            player.increaseAGI(30)
            player.increaseDEF(5)
            player.increaseRES(5)
            player.increaseStaminaStat(6.25)
            player.increaseManaStat(2.5)
            player.increaseHealthStat(1.5)

            player.addMove(skillStab)
            input("You have learned the skill STAB. \nWhen in battle, type STAB to use the skill. [PRESS ENTER] ")
            player.addWeapon(rustyDagger)
            player.currentWeapon = rustyDagger            
            input("You have picked up a rusty dagger. [PRESS ENTER]")

        elif choice == "tank":
            player.job = "Tank"
            player.increaseSTR(15)
            player.increaseART(0)
            player.increaseAGI(5)
            player.increaseDEF(15)
            player.increaseRES(15)
            player.increaseStaminaStat(5)
            player.increaseManaStat(1.25)
            player.increaseHealthStat(10)

            player.addMove(skillBash)
            input("You have learned the skill BASH. \nWhen in battle, type BASH to use the skill. [PRESS ENTER] ")
            player.addWeapon(woodenShield)
            player.currentWeapon = woodenShield          
            input("You have picked up a wooden shield. [PRESS ENTER]")

        elif choice == "mage":
            player.job = "Mage"
            player.increaseSTR(5)
            player.increaseART(25)
            player.increaseAGI(10)
            player.increaseDEF(5)
            player.increaseRES(15)
            player.increaseStaminaStat(2.5)
            player.increaseManaStat(7.5)
            player.increaseHealthStat(0)

            while len(player.spells) < 1:
                choice = input("Which element would you like to specialise in? [TYPE fire, water, ice, earth, wind or thunder] ")
                choice = choice.lower()

                if choice == "fire":
                    player.addMove(spellEmber)
                
                elif choice == "water":
                    player.addMove(spellSplash)
                
                elif choice == "ice":
                    player.addMove(spellIcicle)
                
                elif choice == "earth":
                    player.addMove(spellStone)
                
                elif choice == "wind":
                    player.addMove(spellGale)
                
                elif choice == "thunder":
                    player.addMove(spellBolt)
                
                else:
                    print("Please type one of the elements in the square brackets. [PRESS ENTER] ")
            
            input(f"You have learned the spell {player.spells[0]['Name'].upper()}. \nWhen in battle, type {player.spells[0]['Name'].upper()} to use the spell. [PRESS ENTER] ")

            player.addWeapon(spellbook)
            player.currentWeapon = spellbook
            input("You have picked up a spellbook. [PRESS ENTER] ")
            player.addMove(spellBonk)
            input("You have also learned the skill BONK. \nWhen in battle, type BONK to use the skill. [PRESS ENTER] ")
            input("This will be useful when you run out of mana. [PRESS ENTER] ")

        else:
            print("Please type one of the jobs in the square brackets ")
    
    input("You may also type SKIP to skip a turn to recover stamina, or MEDITATE to recover mana. [PRESS ENTER] ")
    
    player.replenishStats()


def advanceSpell(spell):
    if spell == spellEmber:
        while True:
            choice = input("Do you wish to learn: [1] Eruption or [2] Ignite? ").title()
            if choice == "1":
                player.addMove(spellEruption)
                break
            elif choice == "2":
                player.addMove(spellIgnite)
                break
            input("Please enter the number of the spell you wish to learn. [PRESS ENTER] ")
    
    elif spell == spellSplash:
        while True:
            choice = input("Do you wish to learn: [1] Tsunami or [2] Waterfall? ").title()
            if choice == "1":
                player.addMove(spellTsunami)
                break
            elif choice == "2": 
                player.addMove(spellWaterfall)
                break
            input("Please enter the number of the spell you wish to learn. [PRESS ENTER] ")
    
    elif spell == spellIcicle:
        while True:
            choice = input("Do you wish to learn: [1] Hailstorm or [2] Ice Lance? ").title()
            if choice == "1":
                player.addMove(spellHailstorm)
                break
            elif choice =="2":
                player.addMove(spellIceLance)
                break
            input("Please enter the number of the spell you wish to learn. [PRESS ENTER] ")
    
    elif spell == spellStone:
        while True:
            choice = input("Do you wish to learn: [1] Rock Slide or [2] Planetary Devastation? ").title()
            if choice == "1": 
                player.addMove(spellRockslide)
                break
            elif choice == "2":
                player.addMove(spellPlanetaryDevastation)
                break
            input("Please enter the number of the spell you wish to learn. [PRESS ENTER] ")
    
    elif spell == spellGale:
        while True:
            choice = input("Do you wish to learn: [1] Wind Scythe or [2] Tornado? ").title()
            if choice == "1":
                player.addMove(spellWindScythe)
                break
            elif choice == "2":
                player.addMove(spellTornado)
                break
            input("Please enter the number of the spell you wish to learn. [PRESS ENTER] ")

    elif spell == spellBolt:
        while True:
            choice = input("Do you wish to learn: [1] Kamui or [2] Thunderstorm? ").title()
            if choice == "1":
                player.addMove(spellKamui)
                break
            elif choice == "2": 
                player.addMove(spellThunderstorm)
                break
            input("Please enter the number of the spell you wish to learn. [PRESS ENTER] ")
    
    elif spell == spellHeal:           
        player.addMove(spellGreatHeal)

    
    input(f"You have learned the spell {player.spells[-1]['Name']}")
    

def upgradeSpell():
    upgradableSpells = []
    for spell in player.spells:
        if spell in beginnerSpells:
            upgradableSpells.append(spell)
    
    if spellBonk in upgradableSpells:
        upgradableSpells.remove(spellBonk)


    if len(upgradableSpells) == 0:
        input(f"You have no spells to upgrade. [PRESS ENTER] ")
    
    elif len(upgradableSpells) == 1:
        input(f"The only spell you can upgrade is {upgradableSpells[0]['Name']}. [PRESS ENTER] ")
        spellToUpgrade = upgradableSpells[0]
        advanceSpell(spellToUpgrade)
    
    else:
        statement = ("The spells you may enhance are: ")

        for i in range(len(upgradableSpells)):
            if i == len(upgradableSpells) - 2:
                statement += f"[{i + 1}] {upgradableSpells[i]['Name']} "
            elif i == len(upgradableSpells) - 1:
                statement += f"or [{i + 1}] {upgradableSpells[i]['Name']} [PRESS ENTER] "
            else:
                statement += f"[{i + 1}] {upgradableSpells[i]['Name']}, "


        spellFound = False
        spellToUpgrade = ""
        while not spellFound:
            input(statement)
            choice = input("Please enter desired spell: ").title()
                
            for spell in upgradableSpells:
                if choice == spell['Name']:
                    spellFound = True
                    spellToUpgrade = spell
                    break

                elif choice.isdigit():
                    if 0 < int(choice) <= len(upgradableSpells):
                        spellFound = True
                        spellToUpgrade = upgradableSpells[int(choice) - 1]
                        break
                
            if spellFound:
                break
            else:
                input("Please enter the name or number of the spell you wish to upgrade. [PRESS ENTER] ")
        
        advanceSpell(spellToUpgrade)


def newMoveSelection(moveList):
    options = []
    while len(options) < 3:
        move = random.choice(moveList)
        if move in options:
            continue
        elif move in player.moves:
            continue
        else:
            options.append(move)

    input(f"You will have a choice of three random {options[0]['Action Type'].lower()}s. [PRESS ENTER] ")
    while True:      
        choice = input(f"Would you like to learn: [1] {options[0]['Name'].upper()}, [2] {options[1]['Name'].upper()} or [3] {options[2]['Name'].upper()}? ")
        choice = choice.title()
        if choice == "1":
            addition = options[0]
            input(f"Type {options[0]['Name'].upper()} to use this {options[0]['Action Type'].lower()}. [PRESS ENTER] ")
            break
        elif choice == "2":
            addition = options[1]
            input(f"Type {options[1]['Name'].upper()} to use this {options[1]['Action Type'].lower()}. [PRESS ENTER] ")
            break
        elif choice == "3":
            addition = options[2]
            input(f"Type {options[2]['Name'].upper()} to use this {options[2]['Action Type'].lower()}. [PRESS ENTER] ")
            break
        else:
            input("Please type 1, 2 or 3. [PRESS ENTER] ")
       
    player.addMove(addition)


def newWeaponSelection(weaponList):
    options = []
    while len(options) < 3:
        weapon = random.choice(weaponList)
        if weapon in options:
            continue
        elif weapon in player.weapons:
            continue
        else:
            options.append(weapon)

    input(f"You will have a choice of three random weapons. [PRESS ENTER] ")
    while True:      
        choice = input(f"Would you like to obtain: [1] {options[0]['Name'].upper()}, [2] {options[1]['Name'].upper()} or [3] {options[2]['Name'].upper()}? ")
        choice = choice.title()
        if choice == "1":
            input(f"You have obtained the {options[0]['Name'].upper()}. [PRESS ENTER] ")
            player.addWeapon(options[0])
            break
        elif choice == "2":
            input(f"You have obtained the {options[1]['Name'].upper()}. [PRESS ENTER] ")
            player.addWeapon(options[1])
            break
        elif choice == "3":
            input(f"You have obtained the {options[2]['Name'].upper()}. [PRESS ENTER] ")
            player.addWeapon(options[2])
            break
        else:
            input("Please type 1, 2 or 3. [PRESS ENTER] ")
       
    
# -------------------------------------------------------------------------------------------------------------------------------------------
# DAMAGE FORMULAS
# -------------------------------------------------------------------------------------------------------------------------------------------
def calculateDamage(attacker, defender, move):
    # return array in the form of [damage, agility debuff]
    element = move["Element"]


    # -------------------------------------------------------------------------------------------------------------------------------------------
    # PHYSICAL DAMAGE
    # -------------------------------------------------------------------------------------------------------------------------------------------
    if element == "Physical":
        damage = physDamage(attacker, defender, move)
        if defender.status == "frozen":
            print(f"{(defender.name).upper()} has been shattered ")
            damage *= shatteredMultiplier
            defender.status = "" # reset the status


    # -------------------------------------------------------------------------------------------------------------------------------------------
    # AGAINST NEUTRAL ENEMIES
    # -------------------------------------------------------------------------------------------------------------------------------------------
    else:
        if defender.status == "": # neutral enemies
            if element == "Fire":
                damage = artsDamage(attacker, defender, move)
                defender.status = "hot"

            elif element == "Water":
                damage = artsDamage(attacker, defender, move)
                defender.status = "wet"

            elif element == "Ice":
                damage = artsDamage(attacker, defender, move)
                defender.status = "cold"

            elif element == "Earth":
                damage = artsDamage(attacker, defender, move)
                defender.status = "rocky"

            elif element == "Wind":
                damage = artsDamage(attacker, defender, move)

            elif element == "Thunder":
                damage = artsDamage(attacker, defender, move)
                defender.status = "charged"


        # -------------------------------------------------------------------------------------------------------------------------------------------
        # BASIC REACTIONS
        # -------------------------------------------------------------------------------------------------------------------------------------------
        elif defender.status == "hot": # hot enemies
            if element == "Fire":
                damage = artsDamage(attacker, defender, move)
                damage *= burnedMultiplier
                defender.status = "burned"
                print(f"{(defender.name).upper()} is burning. ")

            elif element == "Water":
                damage = artsDamage(attacker, defender, move)
                damage *= vaporizedMultiplier
                defender.status = ""
                print(f"{(defender.name).upper()} has been vaporised. ")

            elif element == "Ice":
                damage = artsDamage(attacker, defender, move)
                damage *= (1 / meltedMultiplier)
                defender.status = ""
                print(f"{(defender.name).upper()} has resisted. ")

            elif element == "Earth":
                damage = artsDamage(attacker, defender, move)
                defender.status = ""

            elif element == "Wind":
                damage = artsDamage(attacker, defender, move)
                damage * swirlMultiplier
                print(f"{(defender.name).upper()} has been swirled. ")

            elif element == "Thunder":
                damage = artsDamage(attacker, defender, move)
                defender.status = ""


        elif defender.status == "wet": # wet enemies
            if element == "Fire":
                damage = artsDamage(attacker, defender, move)
                damage *= (1 / vaporizedMultiplier)
                defender.status = ""
                print(f"{(defender.name).upper()} has resisted. ")

            elif element == "Water":
                damage = artsDamage(attacker, defender, move)
                damage *= drownedMultiplier
                defender.status = "drowned"
                print(f"{(defender.name).upper()} is drowning. ")

            elif element == "Ice":
                damage = artsDamage(attacker, defender, move)
                damage *= frozenMultiplier
                defender.status = "frozen"
                print(f"{(defender.name).upper()} has been partially frozen. ")

            elif element == "Earth":
                damage = artsDamage(attacker, defender, move)
                damage *= swampedMultiplier
                defender.status = ""
                print(f"{(defender.name).upper()} has been swamped in mud. ")

            elif element == "Wind":
                damage = artsDamage(attacker, defender, move)
                damage * swirlMultiplier
                print(f"{(defender.name).upper()} has been swirled. ")

            elif element == "Thunder":
                damage = artsDamage(attacker, defender, move)
                damage *= electrifiedMultiplier
                print(f"{(defender.name).upper()} has been electrified. ")
                defender.status = ""
        

        elif defender.status == "cold": # cold enemies
            if element == "Fire":
                damage = artsDamage(attacker, defender, move)
                damage *= meltedMultiplier
                defender.status = ""
                print(f"{(defender.name).upper()} has been melted. ")

            elif element == "Water":
                damage = artsDamage(attacker, defender, move)
                damage *= frozenMultiplier
                defender.status = "frozen"
                print(f"{(defender.name).upper()} has been partially frozen. ")

            elif element == "Ice":
                damage = artsDamage(attacker, defender, move)
                damage *= frostedMultiplier
                defender.status = "frosted"
                print(f"{(defender.name).upper()} has been frosted. ")

            elif element == "Earth":
                damage = artsDamage(attacker, defender, move)
                defender.status = ""

            elif element == "Wind":
                damage = artsDamage(attacker, defender, move)
                damage * swirlMultiplier
                print(f"{(defender.name).upper()} has been swirled. ")

            elif element == "Thunder":
                damage = artsDamage(attacker, defender, move)
                defender.status = ""
            

        elif defender.status == "rocky": # rocky enemies
            if element == "Fire":
                damage = artsDamage(attacker, defender, move)
                defender.status = ""

            elif element == "Water":
                damage = artsDamage(attacker, defender, move)
                damage *= swampedMultiplier
                defender.status = "swamped"
                print(f"{(defender.name).upper()} has been swamped in mud. ")

            elif element == "Ice":
                damage = artsDamage(attacker, defender, move)
                defender.status = ""

            elif element == "Earth":
                damage = artsDamage(attacker, defender, move)

            elif element == "Wind":
                damage = artsDamage(attacker, defender, move)

            elif element == "Thunder":
                damage = artsDamage(attacker, defender, move)
                damage *= (1 / groundedMultiplier)
                defender.status = ""
                print(f"{(defender.name).upper()} has resisted. ")
                

        elif defender.status == "charged": # charged enemies
            if element == "Fire":
                damage = artsDamage(attacker, defender, move)
                defender.status = ""

            elif element == "Water":
                damage = artsDamage(attacker, defender, move)
                damage *= electrifiedMultiplier
                defender.status = ""
                print(f"{(defender.name).upper()} has been electrified. ")

            elif element == "Ice":
                damage = artsDamage(attacker, defender, move)
                defender.status = ""

            elif element == "Earth":
                damage = artsDamage(attacker, defender, move)
                damage *= groundedMultiplier
                defender.status = ""
                print(f"{(defender.name).upper()} has been grounded. ")

            elif element == "Wind":
                damage = artsDamage(attacker, defender, move)
                damage * swirlMultiplier
                print(f"{(defender.name).upper()} has been swirled. ")

            elif element == "Thunder":
                damage = artsDamage(attacker, defender, move)
                damage *= stunnedMultiplier
                defender.status = "stunned"
                print(f"{(defender.name).upper()} has been stunned. ")
                            
        # -------------------------------------------------------------------------------------------------------------------------------------------
        # DOUBLE REACTIONS and EXTRA REACTOINS
        # -------------------------------------------------------------------------------------------------------------------------------------------
        elif defender.status == "burned": # burned enemies
            if element == "Fire":
                damage = artsDamage(attacker, defender, move)
                damage *= burnedMultiplier
                print(f"{(defender.name).upper()} is burning. ")

            elif element == "Water":
                damage = artsDamage(attacker, defender, move)
                damage *= (vaporizedMultiplier + enhancedMultiplier)
                defender.status = ""
                print(f"{(defender.name).upper()} has been vaporised. ")

            elif element == "Ice":
                damage = artsDamage(attacker, defender, move)
                damage *= (1 / (meltedMultiplier + enhancedMultiplier))
                defender.status = ""
                print(f"{(defender.name).upper()} has resisted. ")

            elif element == "Earth":
                damage = artsDamage(attacker, defender, move)
                defender.status = ""

            elif element == "Wind":
                damage = artsDamage(attacker, defender, move)
                damage * (swirlMultiplier + enhancedMultiplier)
                print(f"{(defender.name).upper()} has been swirled. ")

            elif element == "Thunder":
                damage = artsDamage(attacker, defender, move)
                defender.status = ""
            
        
        elif defender.status == "drowned": # drowned enemies
            if element == "Fire":
                damage = artsDamage(attacker, defender, move)
                damage *= (1 / (vaporizedMultiplier + enhancedMultiplier))
                defender.status = ""
                print(f"{(defender.name).upper()} has resisted. ")

            elif element == "Water":
                damage = artsDamage(attacker, defender, move)
                damage *= drownedMultiplier
                print(f"{(defender.name).upper()} is drowning. ")

            elif element == "Ice":
                damage = artsDamage(attacker, defender, move)
                damage *= (frozenMultiplier + enhancedMultiplier)
                defender.status = "frozen"
                print(f"{(defender.name).upper()} has been partially frozen. ")

            elif element == "Earth":
                damage = artsDamage(attacker, defender, move)
                damage *= swampedMultiplier
                defender.status = ""
                print(f"{(defender.name).upper()} has been swamped in mud. ") # no enhanced reaction for this one

            elif element == "Wind":
                damage = artsDamage(attacker, defender, move)
                damage * (swirlMultiplier + enhancedMultiplier)
                print(f"{(defender.name).upper()} has been swirled. ")

            elif element == "Thunder":
                damage = artsDamage(attacker, defender, move)
                damage *= (electrifiedMultiplier + enhancedMultiplier)
                print(f"{(defender.name).upper()} has been electrified. ")
                defender.status = ""
        

        elif defender.status == "frosted" or "frozen": # frosted or frozen enemies
            if element == "Fire":
                damage = artsDamage(attacker, defender, move)
                damage *= (meltedMultiplier + enhancedMultiplier)
                defender.status = ""
                print(f"{(defender.name).upper()} has been melted. ")

            elif element == "Water":
                damage = artsDamage(attacker, defender, move)
                damage *= (frozenMultiplier + enhancedMultiplier)
                defender.status = "frozen"
                print(f"{(defender.name).upper()} has been partially frozen. ")

            elif element == "Ice":
                damage = artsDamage(attacker, defender, move)
                damage *= frostedMultiplier
                print(f"{(defender.name).upper()} has been frosted. ")

            elif element == "Earth":
                damage = artsDamage(attacker, defender, move)
                if defender.status == "frozen":
                    damage *= shatteredMultiplier
                defender.status = ""

            elif element == "Wind":
                damage = artsDamage(attacker, defender, move)
                damage * (swirlMultiplier + enhancedMultiplier)
                print(f"{(defender.name).upper()} has been swirled. ")

            elif element == "Thunder":
                damage = artsDamage(attacker, defender, move)
                defender.status = ""
                            

        elif defender.status == "stunned" or "electrified": # stunned or electrified enemies
            if element == "Fire":
                damage = artsDamage(attacker, defender, move)
                defender.status = ""

            elif element == "Water":
                damage = artsDamage(attacker, defender, move)
                damage *= (electrifiedMultiplier + enhancedMultiplier)
                defender.status = ""
                print(f"{(defender.name).upper()} has been electrified. ")

            elif element == "Ice":
                damage = artsDamage(attacker, defender, move)
                defender.status = ""

            elif element == "Earth":
                damage = artsDamage(attacker, defender, move)
                damage *= (groundedMultiplier + enhancedMultiplier)
                defender.status = ""
                print(f"{(defender.name).upper()} has been grounded. ")

            elif element == "Wind":
                damage = artsDamage(attacker, defender, move)
                damage * (swirlMultiplier + enhancedMultiplier)
                print(f"{(defender.name).upper()} has been swirled. ")

            elif element == "Thunder":
                damage = artsDamage(attacker, defender, move)
                damage *= stunnedMultiplier
                print(f"{(defender.name).upper()} has been stunned. ")

    return int(damage)


def calculateSplashDamage(attacker, defender, move):
    # return array in the form of [damage, agility debuff]
    element = move["Element"]


    # -------------------------------------------------------------------------------------------------------------------------------------------
    # PHYSICAL DAMAGE
    # -------------------------------------------------------------------------------------------------------------------------------------------
    if element == "Physical":
        damage = physSplashDamage(attacker, defender, move)
        if defender.status == "frozen":
            print(f"{(defender.name).upper()} has been shattered ")
            damage *= shatteredMultiplier
            defender.status = "" # reset the status


    # -------------------------------------------------------------------------------------------------------------------------------------------
    # AGAINST NEUTRAL ENEMIES
    # -------------------------------------------------------------------------------------------------------------------------------------------
    else:
        if defender.status == "": # neutral enemies
            if element == "Fire":
                damage = artsSplashDamage(attacker, defender, move)
                defender.status = "hot"

            elif element == "Water":
                damage = artsSplashDamage(attacker, defender, move)
                defender.status = "wet"

            elif element == "Ice":
                damage = artsSplashDamage(attacker, defender, move)
                defender.status = "cold"

            elif element == "Earth":
                damage = artsSplashDamage(attacker, defender, move)
                defender.status = "rocky"

            elif element == "Wind":
                damage = artsSplashDamage(attacker, defender, move)

            elif element == "Thunder":
                damage = artsSplashDamage(attacker, defender, move)
                defender.status = "charged"


        # -------------------------------------------------------------------------------------------------------------------------------------------
        # BASIC REACTIONS
        # -------------------------------------------------------------------------------------------------------------------------------------------
        elif defender.status == "hot": # hot enemies
            if element == "Fire":
                damage = artsSplashDamage(attacker, defender, move)
                damage *= burnedMultiplier
                defender.status = "burned"
                print(f"{(defender.name).upper()} is burning. ")

            elif element == "Water":
                damage = artsSplashDamage(attacker, defender, move)
                damage *= vaporizedMultiplier
                defender.status = ""
                print(f"{(defender.name).upper()} has been vaporised. ")

            elif element == "Ice":
                damage = artsSplashDamage(attacker, defender, move)
                damage *= (1 / meltedMultiplier)
                defender.status = ""
                print(f"{(defender.name).upper()} has resisted. ")

            elif element == "Earth":
                damage = artsSplashDamage(attacker, defender, move)
                defender.status = ""

            elif element == "Wind":
                damage = artsSplashDamage(attacker, defender, move)
                damage * swirlMultiplier
                print(f"{(defender.name).upper()} has been swirled. ")

            elif element == "Thunder":
                damage = artsSplashDamage(attacker, defender, move)
                defender.status = ""


        elif defender.status == "wet": # wet enemies
            if element == "Fire":
                damage = artsSplashDamage(attacker, defender, move)
                damage *= (1 / vaporizedMultiplier)
                defender.status = ""
                print(f"{(defender.name).upper()} has resisted. ")

            elif element == "Water":
                damage = artsSplashDamage(attacker, defender, move)
                damage *= drownedMultiplier
                defender.status = "drowned"
                print(f"{(defender.name).upper()} is drowning. ")

            elif element == "Ice":
                damage = artsSplashDamage(attacker, defender, move)
                damage *= frozenMultiplier
                defender.status = "frozen"
                print(f"{(defender.name).upper()} has been partially frozen. ")

            elif element == "Earth":
                damage = artsSplashDamage(attacker, defender, move)
                damage *= swampedMultiplier
                defender.status = ""
                print(f"{(defender.name).upper()} has been swamped in mud. ")

            elif element == "Wind":
                damage = artsSplashDamage(attacker, defender, move)
                damage * swirlMultiplier
                print(f"{(defender.name).upper()} has been swirled. ")

            elif element == "Thunder":
                damage = artsSplashDamage(attacker, defender, move)
                damage *= electrifiedMultiplier
                print(f"{(defender.name).upper()} has been electrified. ")
                defender.status = ""
        

        elif defender.status == "cold": # cold enemies
            if element == "Fire":
                damage = artsSplashDamage(attacker, defender, move)
                damage *= meltedMultiplier
                defender.status = ""
                print(f"{(defender.name).upper()} has been melted. ")

            elif element == "Water":
                damage = artsSplashDamage(attacker, defender, move)
                damage *= frozenMultiplier
                defender.status = "frozen"
                print(f"{(defender.name).upper()} has been partially frozen. ")

            elif element == "Ice":
                damage = artsSplashDamage(attacker, defender, move)
                damage *= frostedMultiplier
                defender.status = "frosted"
                print(f"{(defender.name).upper()} has been frosted. ")

            elif element == "Earth":
                damage = artsSplashDamage(attacker, defender, move)
                defender.status = ""

            elif element == "Wind":
                damage = artsSplashDamage(attacker, defender, move)
                damage * swirlMultiplier
                print(f"{(defender.name).upper()} has been swirled. ")

            elif element == "Thunder":
                damage = artsSplashDamage(attacker, defender, move)
                defender.status = ""
            

        elif defender.status == "rocky": # rocky enemies
            if element == "Fire":
                damage = artsSplashDamage(attacker, defender, move)
                defender.status = ""

            elif element == "Water":
                damage = artsSplashDamage(attacker, defender, move)
                damage *= swampedMultiplier
                defender.status = "swamped"
                print(f"{(defender.name).upper()} has been swamped in mud. ")

            elif element == "Ice":
                damage = artsSplashDamage(attacker, defender, move)
                defender.status = ""

            elif element == "Earth":
                damage = artsSplashDamage(attacker, defender, move)

            elif element == "Wind":
                damage = artsSplashDamage(attacker, defender, move)

            elif element == "Thunder":
                damage = artsSplashDamage(attacker, defender, move)
                damage *= (1 / groundedMultiplier)
                defender.status = ""
                print(f"{(defender.name).upper()} has resisted. ")
                

        elif defender.status == "charged": # charged enemies
            if element == "Fire":
                damage = artsSplashDamage(attacker, defender, move)
                defender.status = ""

            elif element == "Water":
                damage = artsSplashDamage(attacker, defender, move)
                damage *= electrifiedMultiplier
                defender.status = ""
                print(f"{(defender.name).upper()} has been electrified. ")

            elif element == "Ice":
                damage = artsSplashDamage(attacker, defender, move)
                defender.status = ""

            elif element == "Earth":
                damage = artsSplashDamage(attacker, defender, move)
                damage *= groundedMultiplier
                defender.status = ""
                print(f"{(defender.name).upper()} has been grounded. ")

            elif element == "Wind":
                damage = artsSplashDamage(attacker, defender, move)
                damage * swirlMultiplier
                print(f"{(defender.name).upper()} has been swirled. ")

            elif element == "Thunder":
                damage = artsSplashDamage(attacker, defender, move)
                damage *= stunnedMultiplier
                defender.status = "stunned"
                print(f"{(defender.name).upper()} has been stunned. ")
                            
        # -------------------------------------------------------------------------------------------------------------------------------------------
        # DOUBLE REACTIONS and EXTRA REACTOINS
        # -------------------------------------------------------------------------------------------------------------------------------------------
        elif defender.status == "burned": # burned enemies
            if element == "Fire":
                damage = artsSplashDamage(attacker, defender, move)
                damage *= burnedMultiplier
                print(f"{(defender.name).upper()} is burning. ")

            elif element == "Water":
                damage = artsSplashDamage(attacker, defender, move)
                damage *= (vaporizedMultiplier + enhancedMultiplier)
                defender.status = ""
                print(f"{(defender.name).upper()} has been vaporised. ")

            elif element == "Ice":
                damage = artsSplashDamage(attacker, defender, move)
                damage *= (1 / (meltedMultiplier + enhancedMultiplier))
                defender.status = ""
                print(f"{(defender.name).upper()} has resisted. ")

            elif element == "Earth":
                damage = artsSplashDamage(attacker, defender, move)
                defender.status = ""

            elif element == "Wind":
                damage = artsSplashDamage(attacker, defender, move)
                damage * (swirlMultiplier + enhancedMultiplier)
                print(f"{(defender.name).upper()} has been swirled. ")

            elif element == "Thunder":
                damage = artsSplashDamage(attacker, defender, move)
                defender.status = ""
            
        
        elif defender.status == "drowned": # drowned enemies
            if element == "Fire":
                damage = artsSplashDamage(attacker, defender, move)
                damage *= (1 / (vaporizedMultiplier + enhancedMultiplier))
                defender.status = ""
                print(f"{(defender.name).upper()} has resisted. ")

            elif element == "Water":
                damage = artsSplashDamage(attacker, defender, move)
                damage *= drownedMultiplier
                print(f"{(defender.name).upper()} is drowning. ")

            elif element == "Ice":
                damage = artsSplashDamage(attacker, defender, move)
                damage *= (frozenMultiplier + enhancedMultiplier)
                defender.status = "frozen"
                print(f"{(defender.name).upper()} has been partially frozen. ")

            elif element == "Earth":
                damage = artsSplashDamage(attacker, defender, move)
                damage *= swampedMultiplier
                defender.status = ""
                print(f"{(defender.name).upper()} has been swamped in mud. ") # no enhanced reaction for this one

            elif element == "Wind":
                damage = artsSplashDamage(attacker, defender, move)
                damage * (swirlMultiplier + enhancedMultiplier)
                print(f"{(defender.name).upper()} has been swirled. ")

            elif element == "Thunder":
                damage = artsSplashDamage(attacker, defender, move)
                damage *= (electrifiedMultiplier + enhancedMultiplier)
                print(f"{(defender.name).upper()} has been electrified. ")
                defender.status = ""
        

        elif defender.status == "frosted" or "frozen": # frosted or frozen enemies
            if element == "Fire":
                damage = artsSplashDamage(attacker, defender, move)
                damage *= (meltedMultiplier + enhancedMultiplier)
                defender.status = ""
                print(f"{(defender.name).upper()} has been melted. ")

            elif element == "Water":
                damage = artsSplashDamage(attacker, defender, move)
                damage *= (frozenMultiplier + enhancedMultiplier)
                defender.status = "frozen"
                print(f"{(defender.name).upper()} has been partially frozen. ")

            elif element == "Ice":
                damage = artsSplashDamage(attacker, defender, move)
                damage *= frostedMultiplier
                print(f"{(defender.name).upper()} has been frosted. ")

            elif element == "Earth":
                damage = artsSplashDamage(attacker, defender, move)
                if defender.status == "frozen":
                    damage *= shatteredMultiplier
                defender.status = ""

            elif element == "Wind":
                damage = artsSplashDamage(attacker, defender, move)
                damage * (swirlMultiplier + enhancedMultiplier)
                print(f"{(defender.name).upper()} has been swirled. ")

            elif element == "Thunder":
                damage = artsSplashDamage(attacker, defender, move)
                defender.status = ""
                            

        elif defender.status == "stunned" or "electrified": # stunned or electrified enemies
            if element == "Fire":
                damage = artsSplashDamage(attacker, defender, move)
                defender.status = ""

            elif element == "Water":
                damage = artsSplashDamage(attacker, defender, move)
                damage *= (electrifiedMultiplier + enhancedMultiplier)
                defender.status = ""
                print(f"{(defender.name).upper()} has been electrified. ")

            elif element == "Ice":
                damage = artsSplashDamage(attacker, defender, move)
                defender.status = ""

            elif element == "Earth":
                damage = artsSplashDamage(attacker, defender, move)
                damage *= (groundedMultiplier + enhancedMultiplier)
                defender.status = ""
                print(f"{(defender.name).upper()} has been grounded. ")

            elif element == "Wind":
                damage = artsSplashDamage(attacker, defender, move)
                damage * (swirlMultiplier + enhancedMultiplier)
                print(f"{(defender.name).upper()} has been swirled. ")

            elif element == "Thunder":
                damage = artsSplashDamage(attacker, defender, move)
                damage *= stunnedMultiplier
                print(f"{(defender.name).upper()} has been stunned. ")

    return int(damage)


# only tanks can fully negate damage, otherwise 5 percent minimum damage
def physDamage(attacker, defender, move):
    if attacker.currentWeapon["Additional Stat"]["Type"] == "strength":
        damage = (((attacker.STR + attacker.currentWeapon["Additional Stat"]["Amount"]) * move["Multiplier"]) * (1 + (attacker.LVL / 5))) / 2
    else:
        damage = ((attacker.STR * move["Multiplier"]) * (1 + (attacker.LVL / 5))) / 2
    

    if move["Damage Type"] == attacker.currentWeapon["Damage Affinity"]:
        damage *= 1.25


    if defender.currentWeapon["Additional Stat"]["Type"] == "defense":
        if move["Damage Type"] == "Pierce":      
            finalDamage = damage - ((defender.DEF + defender.currentWeapon["Additional Stat"]["Amount"]) * (1 + (defender.LVL / 5)) / 2)
        else:
            finalDamage = damage - (2 * (defender.DEF + defender.currentWeapon["Additional Stat"]["Amount"]) * (1 + (defender.LVL / 5)))
    else:
        if move["Damage Type"] == "Pierce":
            finalDamage = damage - (defender.DEF * (1 + (defender.LVL / 5)) / 2)
        else:
            finalDamage = damage - (2 * defender.DEF * (1 + (defender.LVL / 5)))


    if finalDamage < 0:
        finalDamage = 0

    if defender.job == "tank": # minimum damage doesn't apply to tanks
        return int(finalDamage)
    else:
        if finalDamage < (attacker.STR // 5): # minimum damage rule
            return int(attacker.STR // 5)
        else:
            return int(finalDamage)

def artsDamage(attacker, defender, move):
    if attacker.currentWeapon["Additional Stat"]["Type"] == "arts":
        damage = (((attacker.ART + attacker.currentWeapon["Additional Stat"]["Amount"]) * move["Multiplier"]) * (1 + (attacker.LVL / 5))) / 2
    else:
        damage = ((attacker.ART * move["Multiplier"]) * (1 + (attacker.LVL / 5))) / 2
    
    
    if move["Damage Type"] == attacker.currentWeapon["Damage Affinity"]:
        damage *= 1.25


    if defender.currentWeapon["Additional Stat"]["Type"] == "resistance":
        if move["Damage Type"] == "Pierce":      
            finalDamage = damage - ((defender.RES + defender.currentWeapon["Additional Stat"]["Amount"]) / 2)
        else:
            finalDamage = damage - (2 * (defender.RES + defender.currentWeapon["Additional Stat"]["Amount"]))
    else:
        if move["Damage Type"] == "Pierce":
            finalDamage = damage - (defender.RES * (1 + (defender.LVL / 5)) / 2)
        else:
            finalDamage = damage - (2 * defender.RES* (1 + (defender.LVL / 5)))
    
    # additional defense negation
    if defender.currentWeapon["Additional Stat"]["Type"] == "defense":
        if move["Damage Type"] == "Pierce":      
            finalDamage = damage - ((defender.DEF + defender.currentWeapon["Additional Stat"]["Amount"]) * (1 + (defender.LVL / 5)) / 8)
        else:
            finalDamage = damage - ((defender.DEF + defender.currentWeapon["Additional Stat"]["Amount"]) * (1 + (defender.LVL / 5)) / 4)
    else:
        if move["Damage Type"] == "Pierce":
            finalDamage = damage - (defender.DEF * (1 + (defender.LVL / 5)) / 8)
        else:
            finalDamage = damage - (defender.DEF * (1 + (defender.LVL / 5)) / 4)


    if defender.job == "tank": # minimum damage doesn't apply to tanks
        return int(finalDamage)
    else:
        if finalDamage < (attacker.ART // 5): # minimum damage rule
            return int(attacker.ART // 5)
        else:
            return int(finalDamage)

def physSplashDamage(attacker, defender, move):
    if attacker.currentWeapon["Additional Stat"]["Type"] == "strength":
        damage = (((attacker.STR + attacker.currentWeapon["Additional Stat"]["Amount"]) * move["Multiplier"]) * (1 + (attacker.LVL / 5))) / 5
    else:
        damage = ((attacker.STR * move["Multiplier"]) * (1 + (attacker.LVL / 5))) / 5
    

    if move["Damage Type"] == attacker.currentWeapon["Damage Affinity"]:
        damage *= 1.25


    if defender.currentWeapon["Additional Stat"]["Type"] == "defense":
        if move["Damage Type"] == "Pierce":      
            finalDamage = damage - ((defender.DEF + defender.currentWeapon["Additional Stat"]["Amount"]) * (1 + (defender.LVL / 5)) / 2)
        else:
            finalDamage = damage - (2 * (defender.DEF + defender.currentWeapon["Additional Stat"]["Amount"]) * (1 + (defender.LVL / 5)))
    else:
        if move["Damage Type"] == "Pierce":
            finalDamage = damage - (defender.DEF * (1 + (defender.LVL / 5)) / 2)
        else:
            finalDamage = damage - (2 * defender.DEF * (1 + (defender.LVL / 5)))


    if finalDamage < 0:
        finalDamage = 0

    if defender.job == "tank": # minimum damage doesn't apply to tanks
        return int(finalDamage)
    else:
        if finalDamage < (attacker.STR // 5): # minimum damage rule
            return int(attacker.STR // 5)
        else:
            return int(finalDamage)

def artsSplashDamage(attacker, defender, move):
    if attacker.currentWeapon["Additional Stat"]["Type"] == "arts":
        damage = (((attacker.ART + attacker.currentWeapon["Additional Stat"]["Amount"]) * move["Multiplier"]) * (1 + (attacker.LVL / 5))) / 5
    else:
        damage = ((attacker.ART * move["Multiplier"]) * (1 + (attacker.LVL / 5))) / 5
    
    
    if move["Damage Type"] == attacker.currentWeapon["Damage Affinity"]:
        damage *= 1.25


    if defender.currentWeapon["Additional Stat"]["Type"] == "resistance":
        if move["Damage Type"] == "Pierce":      
            finalDamage = damage - ((defender.RES + defender.currentWeapon["Additional Stat"]["Amount"]) / 2)
        else:
            finalDamage = damage - (2 * (defender.RES + defender.currentWeapon["Additional Stat"]["Amount"]))
    else:
        if move["Damage Type"] == "Pierce":
            finalDamage = damage - (defender.RES * (1 + (defender.LVL / 5)) / 2)
        else:
            finalDamage = damage - (2 * defender.RES* (1 + (defender.LVL / 5)))
    
    # additional defense negation
    if defender.currentWeapon["Additional Stat"]["Type"] == "defense":
        if move["Damage Type"] == "Pierce":      
            finalDamage = damage - ((defender.DEF + defender.currentWeapon["Additional Stat"]["Amount"]) * (1 + (defender.LVL / 5)) / 8)
        else:
            finalDamage = damage - ((defender.DEF + defender.currentWeapon["Additional Stat"]["Amount"]) * (1 + (defender.LVL / 5)) / 4)
    else:
        if move["Damage Type"] == "Pierce":
            finalDamage = damage - (defender.DEF * (1 + (defender.LVL / 5)) / 8)
        else:
            finalDamage = damage - (defender.DEF * (1 + (defender.LVL / 5)) / 4)


    if defender.job == "tank": # minimum damage doesn't apply to tanks
        return int(finalDamage)
    else:
        if finalDamage < (attacker.ART // 5): # minimum damage rule
            return int(attacker.ART // 5)
        else:
            return int(finalDamage)

def turnChance(attacker, defender):
    number = random.randint(1, 100) # pick a random number from 1-100
    chance = 10 + (attacker.AGI * statusToDebuff(attacker.status)) - (defender.AGI * statusToDebuff(defender.status))
    chance = int(chance) # our percentage chance is represented by the chance that number is lower thaan chance. The bigger the chance stat is , the bigger the chance number is in that pool
            
    if chance < 0:
        return False
    elif number < chance:
        if attacker == player:
            print("Your agility has allowed you to take another turn! ")
        else:
            print(f"{attacker.name.upper()}'s agility has allowed it to take another turn! ")
        return True           
    else:
        return False

def dodgeChance(defender, attacker):
    number = random.randint(1, 100) # pick a random number from 1-100
    chance = 10 + (defender.AGI * statusToDebuff(defender.status)) - (attacker.AGI * statusToDebuff(attacker.status))
    chance = int(chance) # our percentage chance is represented by the chance that number is lower thaan chance. The bigger the chance stat is , the bigger the chance number is in that pool
            
    if chance < 0:
        return False
    elif number < chance:
        if defender == player:
            print(f"Your agility has allowed you to dodge {attacker.name.upper()}'s attack! ")
        else:
            print(f"{defender.name.upper()} has dodged your attack! ")
        return True           
    else:
        return False

def skipAmount(character):
    if character.STR > character.AGI:
        return int((character.maxStamina / 10) * (1 + character.STR / 50))
    else:
        return int((character.maxStamina / 10) * (1 + character.AGI / 50))

def meditateAmount(character):
    return int((character.maxMana / 10) * (1 + character.ART / 50))

def healAmount(character):
    return int((character.maxHealth / 10) * (1 + character.ART / 25))

def greatHealAmount(character):
    return int((character.maxHealth / 5) * (1 + character.ART / 25))

# -------------------------------------------------------------------------------------------------------------------------------------------
# DAMAGE MULTIPLIERS
# -------------------------------------------------------------------------------------------------------------------------------------------
# basic statuses are hot, wet, cold, rocky, charged
# double statuses are burned, drowned, frosted and stunned
# additional statuses are frosted, frozen, swamped, electrified, and stunned
# when an attack of an element hits an enemy with an elemental status and there is no reatction, the 2 elements cancel out and the status returns to normal
# wind has no reactions, however its base damage is higher and when it attacks, the status is not removed

# basic reactions
meltedMultiplier = 1.5 # when fire meets ice
vaporizedMultiplier = 1.5 # when water meets fire
shatteredMultiplier = 1.6 # when physical meets a frozen enemy
frozenMultiplier = 1 # when ice meets water
swampedMultiplier = 1 # when water meets earth
electrifiedMultiplier = 1.3 # when thunder meets water
groundedMultiplier = 1.3 # when earth meets thunder
swirlMultiplier = 1.2 # when wind meets anything

# double reactions
burnedMultiplier = 1.25
drownedMultiplier = 1.1
frostedMultiplier = 1.1
stunnedMultiplier = 1.2

# enhanced reactions multiplier
enhancedMultiplier = 0.5


# -------------------------------------------------------------------------------------------------------------------------------------------
# AGILITY DEBUFFS
# -------------------------------------------------------------------------------------------------------------------------------------------
frostedDebuff = 0.9 # when ice meetes ice
frozenDebuff = 0.5 # when ice meets water
swampedDebuff = 0.7 # when water meets earth
electrifiedDebuff = 0.8 # when thunder meets thunder
stunnedDebuff = 0.6 # when thunder meets water

def statusToDebuff(status):
    if status == "frosted":
        return frostedDebuff
    elif status == "frozen":
        return frozenDebuff
    elif status == "swamped":
        return swampedDebuff
    elif status == "electrified":
        return electrifiedDebuff
    elif status == "stunned":
        return stunnedDebuff
    else:
        return 1
        

# -------------------------------------------------------------------------------------------------------------------------------------------
# Start of Story and Job selection
# -------------------------------------------------------------------------------------------------------------------------------------------
input("WELCOME TO THE TOWER! [PRESS ENTER] ")
input("\nYou awake after a long slumber; you have lost all of your memories and power. [PRESS ENTER] ")
input("Yet you have a faint feeling, that what you are seeking can be found at the summit. [PRESS ENTER] ")

player = NewPlayer() # creates a lv 1 player
classSelection()
player.setName()

input(f"???: Well then {player.name}, I wish you luck on your tower ascension. [PRESS ENTER] ")
input("???: May we meet again at the top. [PRESS ENTER] ")

print(f"You step forward through the double doors, into the first room of the tower. ")
time.sleep(2)
input("[PRESS ENTER TO BEGIN YOUR ASCENSION] ")


# -------------------------------------------------------------------------------------------------------------------------------------------
# FLOOR 1 - ogre
# -------------------------------------------------------------------------------------------------------------------------------------------
print("\n*** FLOOR 1 ***\n")
time.sleep(2)

# Battle
input("* AN OGRE HAS ENTERED * [PRESS ENTER] ")
ogre = ClubOgre("Ogre", 1)
print()
player.battle([ogre])

input("\nYou have completed the FLOOR 1 trial. [PRESS ENTER] ")

# Stat Recovery
input("Just this once, your stamina, mana and health have all been recovered. [PRESS ENTER] ")
player.replenishStats()

# Level Up
input("YOU HAVE LEVELLED UP! [PRESS ENTER] ")
player.incrementLevel()
print()

player.displayStats()
print()
player.allocateStats(5)
input("\nYour final stats: [PRESS ENTER] ")
player.displayStats()
print()
player.displayMoves()
print()

# Floor Rewards
while True:
    choice = input("Do you wish to: [1] gain 5 stat points to allocate [2] learn a new skill or [3] learn a new spell? ")
    if choice == "1":
        player.allocateStats(5)
        break
    elif choice == "2":
        newMoveSelection(beginnerSkills)
        break  
    elif choice == "3":      
        newMoveSelection(beginnerSpells)
        break
    else:
        input("Please type 1, 2 or 3. [PRESS ENTER] ")


input("You have advanced to the 2nd floor of the tower: [PRESS ENTER] ")


# -------------------------------------------------------------------------------------------------------------------------------------------
# FLOOR 2 - dual ogres
# -------------------------------------------------------------------------------------------------------------------------------------------
print("\n*** FLOOR 2 ***\n")
time.sleep(2)

# Battle
input("* 2 OGRES HAVE ENTERED * [PRESS ENTER] ")
ogreClub = ClubOgre("Club Ogre", 2)
ogreFlame = FlameOgre("Flame Ogre", 2)
print()
player.battle([ogreClub, ogreFlame])

input("\nYou have completed the FLOOR 2 trial! [PRESS ENTER] ")

# Boss Drops
input("The Club Ogre has dropped his club. [PRESS ENTER] ")
player.addWeapon(club)

while True:
    choice = input("You pick it up, do you wish to equip it? [Y/N] ").upper()
    if choice == "Y":       
        player.equipWeapon(club)
        input("You have equipped the CLUB. [PRESS ENTER] ")
        break
    elif choice == "N": 
        input("You have stored the CLUB in your inventory. [PRESS ENTER] ")
        break
    else:
        input("Please type Y or N. [PRESS ENTER] ")

# Stat Recovery
input("You have recovered 30 Stamina. [PRESS ENTER] ")
player.restoreStamina(30)

input("You have recovered 30 MP. [PRESS ENTER] ")
player.restoreMana(30)

input("You have recovered 30 HP. [PRESS ENTER] ")
player.restoreHealth(30)

input("Your maximum health and stamina have increased by 10. [PRESS ENTER] ")
player.increaseHealthStat(2.5)
player.increaseStaminaStat(2.5)
input("Your maximum mana has increased by 5. [PRESS ENTER] ")
player.increaseHealthStat(1.25)

# Level Up
input("YOU HAVE LEVELLED UP!. [PRESS ENTER] ")
player.incrementLevel()
print()

player.displayStats()
print()
player.allocateStats(10)
input("\nYour final stats: [PRESS ENTER] ")
player.displayStats()
print()
player.displayMoves()
print()

# Floor Rewards
input("You may choose a new skill or spell to learn. ")
while True:
    choice = input("Do you either wish to [1] learn a new skill or [2] learn a new spell? ")
    if choice == "1":       
        newMoveSelection(beginnerSkills)
        break
    elif choice == "2": 
        newMoveSelection(beginnerSpells)
        break
    else:
        input("Please type 1 or 2. [PRESS ENTER] ")


input("Extra reward: [PRESS ENTER] ")
while True:
    choice = input("Do you either wish to [1] restore your health, [2] restore your stamina and mana or [3] gain 5 stat points to allocate? ")
    if choice == "1":
        player.replenishHealth()
        input("Your health has been restored [PRESS ENTER] ")
        break
    elif choice == "2":
        player.replenishStamina()
        player.replenishMana()
        input("Your stamina and mana have been restored [PRESS ENTER] ")
        break
    elif choice == "3":
        player.allocateStats(5)
        break
    else:
        input("Please type 1, 2 or 3. [PRESS ENTER] ")


input("You have advanced to the 3rd floor of the tower: [PRESS ENTER] ")


# -------------------------------------------------------------------------------------------------------------------------------------------
# FLOOR 3 - dual golems
# -------------------------------------------------------------------------------------------------------------------------------------------
print("\n*** FLOOR 3 ***\n")
time.sleep(2)

# Battle
input("* 2 GOLEMS HAVE ENTERED * [PRESS ENTER] ")
golem1 = Golem("Golem 1", 3)
golem2 = Golem("Golem 2", 3)
print()
player.battle([golem1, golem2])

input("\nYou have completed the FLOOR 3 trial! [PRESS ENTER] ")

# Stat Recovery
input("You have recovered 30 Stamina. [PRESS ENTER] ")
player.restoreStamina(30)

input("You have recovered 30 MP. [PRESS ENTER] ")
player.restoreMana(30)

input("You have recovered 30 HP. [PRESS ENTER] ")
player.restoreHealth(30)

# Level Up
input("YOU HAVE LEVELLED UP!. [PRESS ENTER] ")
player.incrementLevel()
print()

player.displayStats()
print()
player.allocateStats(10)
input("\nYour final stats: [PRESS ENTER] ")
player.displayStats()
print()
player.displayMoves()
print()

# Floor Rewards
input("You may choose a new skill or spell to learn. ")
while True:
    choice = input("Do you wish to [1] learn a new skill or [2] learn a new spell? ")
    if choice == "1":
        newMoveSelection(beginnerSkills)
        break 
    elif choice == "2":
        newMoveSelection(beginnerSpells)
        break
    else:
        input("Please type 1 or 2. [PRESS ENTER] ")


input("You have advanced to the 4th floor of the tower: [PRESS ENTER] ")


# -------------------------------------------------------------------------------------------------------------------------------------------
# FLOOR 4 - oni
# -------------------------------------------------------------------------------------------------------------------------------------------
print("\n*** FLOOR 4 ***\n")
time.sleep(2)

# Battle
input("* AN ONI RUSHES TOWARDS YOU, CLUTCHING IT'S SWORD * [PRESS ENTER] ")
swordOni = Oni("Sword Oni", 4)
print()
player.battle([swordOni])

input("\nYou have completed the FLOOR 4 trial! [PRESS ENTER] ")

# Stat Recovery
input("You have recovered 35 Stamina. [PRESS ENTER] ")
player.restoreStamina(30)

input("You have recovered 35 MP. [PRESS ENTER] ")
player.restoreMana(30)

input("You have recovered 35 HP. [PRESS ENTER] ")
player.restoreHealth(30)

# Level Up
input("YOU HAVE LEVELLED UP!. [PRESS ENTER] ")
player.incrementLevel()
print()

player.displayStats()
print()
player.allocateStats(10)
input("\nYour final stats: [PRESS ENTER] ")
player.displayStats()
print()
player.displayMoves()
print()

# Floor Rewards
newWeaponSelection(advancedWeapons)
while True:
    choice = input("You pick it up, do you wish to equip it? [Y/N] ").upper()
    if choice == "Y":       
        player.equipWeapon(player.weapons[-1])
        input(f"You have equipped the {player.weapons[-1]['Name'].upper()}. [PRESS ENTER] ")
        break
    elif choice == "N": 
        input(f"You have stored the {player.weapons[-1]['Name'].upper()} in your inventory. [PRESS ENTER] ")
        break
    else:
        input("Please type Y or N. [PRESS ENTER] ")


input("Extra reward: [PRESS ENTER] ")
while True:
    choice = input("Do you either wish to [1] restore your health, [2] restore your stamina and mana or [3] gain 10 stat points to allocate? ")
    if choice == "1":
        player.replenishHealth()
        input("Your health has been restored [PRESS ENTER] ")
        break
    elif choice == "2":
        player.replenishStamina()
        player.replenishMana()
        input("Your stamina and mana have been restored [PRESS ENTER] ")
        break
    elif choice == "3":
        player.allocateStats(10)
        break
    else:
        input("Please type 1, 2 or 3. [PRESS ENTER] ")


input("You have advanced to the 5th floor of the tower: [PRESS ENTER] ")


# -------------------------------------------------------------------------------------------------------------------------------------------
# FLOOR 5 - yeti, lava hound
# -------------------------------------------------------------------------------------------------------------------------------------------
print("\n*** FLOOR 5 ***\n")
time.sleep(2)

# Battle
input("* A YETI HAS ENTERED * [PRESS ENTER] ")
yeti = Yeti("Yeti", 5)
hound = LavaHound("Lava Hound", 5)
print()
player.battle([yeti, hound])

input("\nYou have completed the FLOOR 5 trial! [PRESS ENTER] ")

# Stat Recovery
input("You have recovered 40 Stamina. [PRESS ENTER] ")
player.restoreStamina(40)

input("You have recovered 40 MP. [PRESS ENTER] ")
player.restoreMana(40)

input("You have recovered 40 HP. [PRESS ENTER] ")
player.restoreHealth(40)

input("Your maximum health and stamina and mana have increased by 15. [PRESS ENTER] ")
player.increaseStaminaStat(3.75)
player.increaseManaStat(3.75)
player.increaseHealthStat(3.75)
input("Your elemental resistance and physical defense have also increased by 15. [PRESS ENTER] ")
player.increaseRES(15)
player.increaseDEF(15)

# Level Up
input("YOU HAVE LEVELLED UP!. [PRESS ENTER] ")
player.incrementLevel()
print()

player.displayStats()
print()
player.allocateStats(15)
input("\nYour final stats: [PRESS ENTER] ")
player.displayStats()
print()
player.displayMoves()
print()

# Upgrading a Move
while True:
    choice = input("Do you wish to [1] learn an advanced skill or [2] upgrade a spell? ")
    if choice == "1":
        newMoveSelection(advancedSkills)
        break    
    elif choice == "2":
        upgradeSpell()
        break
    else:
        input("Please type 1 or 2. [PRESS ENTER] ")

input("Extra reward: [PRESS ENTER] ")
# Floor Rewards
while True:
    choice = input("Do you either wish to [1] restore your health or [2] restore your stamina and mana? ")
    if choice == "1":
        player.replenishHealth()
        break
    elif choice == "2":
        player.replenishStamina()
        player.replenishMana()
        break
    else:
        input("Please type 1 or 2. [PRESS ENTER] ")


input("You have advanced to the 6th floor of the tower: [PRESS ENTER] ")


# -------------------------------------------------------------------------------------------------------------------------------------------
# FLOOR 6 - THREE MAN STEP
# -------------------------------------------------------------------------------------------------------------------------------------------
print("\n*** FLOOR 6 ***\n")
time.sleep(2)

# Battle
input("* A DEVIOUS TRIO HAS ENTERED * [PRESS ENTER] ")
ogre = FlameOgre("Devious Ogre", 6)
golem = Golem("Devious Golem", 6)
yeti = Yeti("Devious Yeti", 6)
print()
player.battle([ogre, golem, yeti])

input("\nYou have completed the FLOOR 6 trial! [PRESS ENTER] ")

# Stat Recovery
input("The trio drops a full recovery potion. [PRESS ENTER] ")
input("You drink the potion and recover all health, stamina and mana. [PRESS ENTER] ")
player.replenishStats()

# Level Up
input("YOU HAVE LEVELLED UP!. [PRESS ENTER] ")
player.incrementLevel()
print()

player.displayStats()
print()
player.allocateStats(10)
input("\nYour final stats: [PRESS ENTER] ")
player.displayStats()
print()
player.displayMoves()
print()

# Floor Rewards
while True:
    choice = input("Do you wish to: [1] gain 5 stat points to allocate [2] learn a new skill or [3] learn a new spell? ")
    if choice == "1":
        player.allocateStats(5)
        break
    elif choice == "2":
        newMoveSelection(skills)
        break 
    elif choice == "3":       
        newMoveSelection(beginnerSpells)
        break
    else:
        input("Please type 1, 2 or 3. [PRESS ENTER] ")
        

input("You have advanced to the 7th floor of the tower: [PRESS ENTER] ")


# -------------------------------------------------------------------------------------------------------------------------------------------
# FLOOR 7 - Dullahan
# -------------------------------------------------------------------------------------------------------------------------------------------
print("\n*** FLOOR 7 ***\n")
time.sleep(2)

# Battle
input("* A DULLAHAN HAS ENTERED * [PRESS ENTER] ")
dullahan = Dullahan("Death Knight", 7)
print()
player.battle([dullahan])

input("\nYou have completed the FLOOR 7 trial! [PRESS ENTER] ")

# Stat Recovery
input("You have recovered 40 Stamina. [PRESS ENTER] ")
player.restoreStamina(40)

input("You have recovered 40 MP. [PRESS ENTER] ")
player.restoreMana(40)

input("You have recovered 40 HP. [PRESS ENTER] ")
player.restoreHealth(40)

input("Your maximum health has increased by 30. [PRESS ENTER] ")
player.increaseHealthStat(7.5)
input("Your maximum stamina and mana have increased by 20. [PRESS ENTER] ")
player.increaseStaminaStat(5)
player.increaseManaStat(5)

# Level Up
input("YOU HAVE LEVELLED UP!. [PRESS ENTER] ")
player.incrementLevel()
print()

player.displayStats()
print()
player.allocateStats(15)
input("\nYour final stats: [PRESS ENTER] ")
player.displayStats()
print()
player.displayMoves()
print()

# Floor Rewards
while True:
    choice = input("Do you wish to [1] gain 5 stat points to allocate, [2] learn an advanced skill or [3] upgrade a spell? ")
    if choice == "1":
        player.allocateStats(5)
        break    
    if choice == "2":
        newMoveSelection(advancedSkills)
        break    
    elif choice == "3":
        upgradeSpell()
        break
        

input("You have advanced to the 8th floor of the tower: [PRESS ENTER] ")


# -------------------------------------------------------------------------------------------------------------------------------------------
# FLOOR 8 - The Storm (wind and thunder and water) (skills rain, hurricane, thunderstrike)
# -------------------------------------------------------------------------------------------------------------------------------------------
print("\n*** FLOOR 8 ***\n")
time.sleep(2)

# Intro
input("You walk into the massive chamber that is the 8th floor. [PRESS ENTER] ")
input("Immediately, a gentle breeze strokes your cheek. [PRESS ENTER] ")

input("You have sustained 15 damage! [PRESS ENTER] ")
player.currentHealth -= 15
if player.currentHealth <= 0:
    input("You have died. ")
    quit()

input("All of a sudden, the wind intensifies and cuts your cheek. [PRESS ENTER] ")
input("As the wind currents grow and converge, you start to notice the rain... [PRESS ENTER] ")
input("... And the laughter from above. [PRESS ENTER] ")
input("???: Huahahahaha! [PRESS ENTER] ")

input("Out of nowhere, a bolt of lightning flashes approaching your direction. [PRESS ENTER] ")
if player.AGI > 40:
    input("However, this time you are able to dodge. [PRESS ENTER] ")
else:
    input("You are struck, and are dealt 20 damage. [PRESS ENTER] ")
    player.currentHealth -= 20
    if player.currentHealth <= 0:
        input("You have died. ")
        quit()

input("You look up again, towards the direction of the laughter, pissed off. [PRESS ENTER] ")
input("And this time you notice a sort of orb in the eye of the storm. [PRESS ENTER] ")
input("This is what you must target, but only certain attacks can reach it. [PRESS ENTER] ")

# Battle
eye = Storm("Eye of the Storm", 8)
print()
player.battle([eye])

input("\nYou have completed the FLOOR 8 trial! [PRESS ENTER] ")

# Stat Recovery
input("You have recovered 50 Stamina. [PRESS ENTER] ")
player.restoreStamina(50)

input("You have recovered 50 MP. [PRESS ENTER] ")
player.restoreMana(50)

input("You have recovered 50 HP. [PRESS ENTER] ")
player.restoreHealth(50)

input("Your maximum health has increased by 20. [PRESS ENTER] ")
player.increaseHealthStat(5)
input("Your maximum stamina and mana have increased by 10. [PRESS ENTER] ")
player.increaseStaminaStat(2.5)
player.increaseManaStat(2.5)
input("Your elemental resistance and physical defense have also increased by 15. [PRESS ENTER] ")
player.increaseRES(15)
player.increaseDEF(15)

# Level Up
input("YOU HAVE LEVELLED UP!. [PRESS ENTER] ")
player.incrementLevel()
print()

player.displayStats()
print()
player.allocateStats(15)
input("\nYour final stats: [PRESS ENTER] ")
player.displayStats()
print()
player.displayMoves()
print()

# Floor Rewards
while True:
    choice = input("Do you either wish to [1] restore your health, [2] restore your stamina and mana or [3] gain 10 stat points to allocate? ")
    if choice == "1":
        player.replenishHealth()
        input("Your health has been restored [PRESS ENTER] ")
        break
    elif choice == "2":
        player.replenishStamina()
        player.replenishMana()
        input("Your stamina and mana have been restored [PRESS ENTER] ")
        break
    elif choice == "3":
        player.allocateStats(10)
        break
    else:
        input("Please type 1, 2 or 3. [PRESS ENTER] ")
        

input("You have advanced to the 9th floor of the tower: [PRESS ENTER] ")


# -------------------------------------------------------------------------------------------------------------------------------------------
# FLOOR 9 - Master Wizard (every element + heal and meditate)
# -------------------------------------------------------------------------------------------------------------------------------------------
print("\n*** FLOOR 9 ***\n")
time.sleep(2)

# Intro
input("Upon opening the doors of the ninth floor, you see an old man with his back turned to you, clutching his cane. [PRESS ENTER] ")
input("???: Oh? So You've made it? [PRESS ENTER] ")
input("???: He told me you'd be coming, but I never expected you to make it, you know? [PRESS ENTER] ")
input("???: You can call me Angus. [PRESS ENTER] ")
input("ANGUS: The all-knowing, master of all magic. [PRESS ENTER] ")
input("Angus turns around slowly. [PRESS ENTER] ")
input("He lifts up his cane, which you now recognise to be a magic staff. [PRESS ENTER] ")
input("ANGUS: But don't think that an old fossil like me can't still teach a lesson to a young fool like you! [PRESS ENTER] ")

# Battle
angus = GrandMage("Angus, the Master of All Magic", 10)
print()
player.battle([angus])

input("\nYou have completed the FLOOR 9 trial! [PRESS ENTER] ")

# Boss Drops
input("\nAngus falls over, letting go of his staff. [PRESS ENTER] ")
player.addWeapon(grandStaff)

while True:
    choice = input("You pick it up, do you wish to equip it? [Y/N] ").upper()
    if choice == "Y":       
        player.equipWeapon(grandStaff)
        input("You have equipped the club. [PRESS ENTER] ")
        break
    elif choice == "N": 
        input("You have stored the club in your inventory. [PRESS ENTER] ")
        break
    else:
        input("Please type Y or N. [PRESS ENTER] ")

# Stat Recovery
input("The trio drops a full recovery potion. [PRESS ENTER] ")
input("You drink the potion and recover all health, stamina and mana. [PRESS ENTER] ")
player.replenishStats()

# Level Up
input("YOU HAVE LEVELLED UP!. [PRESS ENTER] ")
player.incrementLevel()
print()

player.displayStats()
print()
player.allocateStats(10)
input("\nYour final stats: [PRESS ENTER] ")
player.displayStats()
print()
player.displayMoves()
print()

# Floor Rewards

input("You have advanced to the 10th and final floor of the tower: [PRESS ENTER] ")


# -------------------------------------------------------------------------------------------------------------------------------------------
# FLOOR 10 - Dragon
# -------------------------------------------------------------------------------------------------------------------------------------------


# -------------------------------------------------------------------------------------------------------------------------------------------
# SURPRISE FLOOR
# -------------------------------------------------------------------------------------------------------------------------------------------
input(f"WELL DONE {player.name}! You have conquered the tower! [PRESS ENTER] ")
input("???: Wow, I didn't expect you to make it all the way up here, especially at your low power level when we first met. [PRESS ENTER] ")
input("???: Unfortunately though, your luck has run out. [PRESS ENTER] ")
input("??? has done 50 damage! [PRESS ENTER] ")
player.currentHealth -= 50
if player.currentHealth <= 0:
    input("You have died. ")
    quit()

input(f"You have {player.currentHealth} HP remaining. [PRESS ENTER] ")

input("???: BECAUSE I AM YOUR FINAL OPPONENT. [PRESS ENTER] ")
input("???: AS FOR MY NAME? [PRESS ENTER] ")
input("???: CALL ME HEADEN, KING OF THE TOWER! [PRESS ENTER] ")
