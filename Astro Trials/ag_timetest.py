from sys import exit
from os.path import exists
import time

items = []
rooms_cleared = []

print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n\n\n\n")
print("                                 ASTRO TRIALS                                  \n\n\n\n ")
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
time.sleep(5)




print("""
\nintro:\nSomething has entered your ship while you were in deep hibernation.
You must reach the cockpit if you are going to survive!
But be careful creatures can be dangerous and one
false step could mean your doom!\n
""")
time.sleep(5)
print("\nTo check items just type 'items'\n")
time.sleep(2)
print("""\nFor navigation purposes the front of the ship
is North and also where the cockpit is.\n""")

def test_mode(function):
    function()
    a = input("function name?:\n>>>")
    testfunction(a)
time.sleep(5)


charactor = input("Enter Charactor name:")

def start_room():
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print(f"""
\n{charactor} awakens from a deep sleep.  There is a 'code red'
screen flashing by your sleeping pod.  Looking around {gender_he_she} sees
three doors.  One is glowing green to the west, one is glowing
yellow to the east, and one is a normal door to the north.  What do you do?\n
""")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    time.sleep(3)
    print(f"1. {charactor} enters green door.")
    print(f"2. {charactor} enters yellow door.")
    print(f"3. {charactor} enters normal door.")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    choice = input("> ")
    while True:
        if choice == "1":
            gas_room_gate()
        elif choice == "2":
            weapon_room_gate()
        elif choice == "3":
            rodent_room_gate()
        elif choice == "items":
            print(items)
            choice = choice = input('above is a list of your items.  What next?\n> ')
        else:
            print("Can you read?  Try again...")
            choice = choice = input(">  ")

def start_room_done():
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print(f"""
\nThere is a 'code red' screen flashing. Looking around {charactor} sees
three doors.  One is glowing green door on the west,
one is glowing yellow on the east, and one is a normal door to the north.
What do you do?\n
""")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    time.sleep(3)
    print(f"1.{charactor} enters green door.")
    print(f"2. {charactor} enters yellow door.")
    print(f"3. {charactor} enters normal door.")

    choice = input("> ")
    while True:
        if choice == "1":
            gas_room_gate()

        elif choice == "2":
            weapon_room_gate()

        elif choice == "3":
            rodent_room_gate()

        elif choice == "items":
            print(items)
            choice = choice = input('above is a list of your items.  What next?\n> ')
        else:
            print("Can you read?  Try again...")
            choice = choice = input(">  ")


def gas_room_gate():
    def gas_room():
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print(f"""
\n{charactor} enters the room and {gender_his_her} lungs fill
with a putrid gas.  With every step {charactor} can feel {gender_him_her}self
suffocating.  In the room {charactor} sees two chest that may have valuable
supplies.  What do you do?\n
""")
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        time.sleep(3)
        print("1. Check chest #1")
        print("2. Check chest #2")
        print("3. leave room")

        choice = input("> ")
        while True:
            if choice == "1":
                print("Inside is a peice of paper with the code '5 2 6'")
                rooms_cleared.append('gas_clear')
                gas_room_done()
            elif choice == "2":
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                print("Inside is a peice of paper with the code '5 2 6'")
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                time.sleep(3)
                rooms_cleared.append('gas_clear')
                gas_room_done()
            elif choice == "3":
                start_room_done()
            elif choice == "items":
                print(items)
                print("\n1. Check chest #1")
                print("2. Check chest #2")
                print("3. leave room\n")
                choice = choice = input('> ')
            else:
                print("Can you read?  Try again...")
                choice = choice = input(">  ")
    if 'gas_clear' in rooms_cleared:
        gas_room_done()
    else:
        gas_room()


def gas_room_done():
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print(f'''
\n{charactor} thinks  "I should remember that code." However the gas
is making it harder and harder to breath.  What do you do next?\n
''')
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    time.sleep(3)
    print("1. Check chest #1")
    print("2. Check chest #2")
    print("3. leave the room")
    choice = input('> ')
    while True:
        if choice == "1":
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            print(f"""
{charactor} reaches for the second chest gasping for air.
{gender_he_she} gets it open to read a peice of paper that says code
'5 2 6' before loosing consciousness.  {charactor} is a very greedy Gus!
""")
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            die()

        elif choice == "2":
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            print(f"""
\n{charactor} reaches for the second chest gasping for air.
{gender_he_she} reaches it and opens up to read a peice of paper that says code
'5 2 6' before loosing consciousness.  {charactor} is a very greedy Gus!\n
""")
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            die()
        elif choice == "3":
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            print(f"""
{charactor} dives out the door just as {gender_his_her} vision
starts to tunnel in.  {charactor} falls into the other room gasping for air.
""")
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            start_room_done()
        elif choice == "items":
            print(items)
            choice = choice = input('above is a list of your items.  What next?\n> ')
        else:
            print("Can you read?  Try again...")
            choice = choice = input(">  ")

def weapon_room_gate():
    def weapon_room():
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print(f"\n{charactor} walks in to see a glowing plasma gun!  What do you do?\n")
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        time.sleep(3)
        print("1. Take weapon (one charge)")
        print("2. Leave room")
        choice = input('> ')
        while True:
            if choice == "1":
                items.append('weapon')
                items.append('charge')
                return rooms_cleared.append('wep_clear')
            elif choice == "2":
                    start_room_done()
            elif choice == "items":
                print(items)
                choice = choice = input('above is a list of your items.  What next?\n> ')
            else:
                print("That is not a valid entry")
                choice = choice = input('> ')

    if 'wep_clear' in rooms_cleared:
        weapon_room_done()
    else:
        weapon_room()

def weapon_room_done():
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print("There is a door behind you and nothing more of interest in this room.")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    time.sleep(3)
    print("1. to leave room")
    choice = input('> ')
    if choice == "1":
        start_room_done()
    elif choice == "items":
        print(items)
        choice = choice = input('above is a list of your items.  What next?\n> ')
    else:
        print("That does nothing...")
        weapon_room_done()

def rodent_room_gate():
    def rodent_room():
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print(f"""
\n{charactor} steps into a communications room that has been
up ended with equipment broken and scattered everywhere.
There is a door on the north side of the room.  What do you do?\n
""")
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        time.sleep(3)
        print("1. Walk to the north door.")
        print("2. Go back (south door)")
        choice = input('> ')
        while True:
            if choice == "1":
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                print("""
\nA large furry rodent with green eyes jumps out from
behind some ruble.  It stands between you and the door.  What do you do?\n
""")
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                time.sleep(3)
                print("1. Knock over a shelf on top of it")
                print("2. Try to run past")
                print("3. Flee back")
                if 'weapon' and 'charge' in items:
                    print("4. Use weapon on the rodent")
                action = input('> ')
                while True:
                    if action == "1":
                        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                        print(f"""
\n{charactor} pulls hard on the shelf next to {gender_him_her}.
The shelf growns but doesnt budge as the rodent starts for {charactor}.
With a final heave {charactor} pulls down the shelf ontop of the rodent just
in time to flatten it before it could reach {gender_him_her}.\n
""")
                        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                        time.sleep(3)
                        rooms_cleared.append("rodent_clear")
                        rodent_room_done()
                    elif action == "2":
                        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                        print(f"""
\n{charactor} stares at the rodent as if daring it to attack.
Then in a sudden motion {charactor} leaps forward trying to clear the rodent
completely.  Just when {gender_he_she}thinks he has made it the rodent leaps
up and bites hard down on {gender_his_her} crotch.
With a yowl {charactor} is pulled to the ground and over the next several
hours is eaten bit by bit.\n
""")
                        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                        die()
                    elif action == "3":
                        print("Cowards do not win games.")
                        hall_a()
                    elif action == "4":
                        if "weapon" and "charge" in items:
                            print("You blast the rodent in the face and it keels over.")
                            items.remove("charge")
                            rooms_cleared.append("rodent_clear")
                            rodent_room_done()
                    elif action == "items":
                        print(items)
                        action = action = input('above is a list of your items.  What next?\n> ')

                    else:
                        print("you do not have the charges nessecary.")
                        action = action = input('> ')

            elif choice == "2":
                    hall_a()
            elif choice == "items":
                print(items)
                choice = choice = input('above is a list of your items.  What next?\n> ')
            else:
                print("That is not a valid entry")
                choice = choice = input('> ')

    if 'rodent_clear' in rooms_cleared:
        return True and rodent_room_done()
    else:
        rodent_room()

def rodent_room_done():
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print(f"""
The dead rodent lies on the ground where {charactor} killed it.
There is a door to the north and one to the south.\n
""")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print("1. go to north door.")
    print("2. Go through south door.")
    choice = input('> ')
    while True:
        if choice == "1":
            hall_a()
        elif choice == "2":
            start_room_done()
        elif choice == "items":
            print(items)
            choice = choice = input('above is a list of your items.  What next?\n> ')
        else:
            print("That is not a valid option.")
            choice = choice = input("> ")

def hall_a():
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print(f"""
{charactor} enters a long hallway with two doors at the west end,
The lights flicker leaving the end of the hallway intermittently out of sight.
There is a door to the south, and a door to the north.  What do you do?\n
""")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    time.sleep(3)
    print("1. Go to the end of the hallway.")
    print("2. Go through south door.")
    print("3. Go through the north door.")

    choice = input('> ')
    while True:
        if choice == "1":
            hall_b_gate()
        elif choice == "2":
            start_room_done()
        elif choice == "3":
            stock()
        elif choice == "items":
            print(items)
            choice = choice = input('above is a list of your items.  What next?\n> ')
        else:
            print("That is not a valid option.")
            choice = choice = input("> ")

def hall_b_gate():
    def hall_b():
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print(f"""
\nAs {charactor} starts to walk through the hallway the lights
flicker faster then go out.  Not being able to see anything you hear a
snarl from above you.  What do you do?\n
""")
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        time.sleep(3)
        print("1. Run to the end of the hall.")
        print("2. Stand still and reach for the emergency flashlight on the wall")
        print("3. run to the other end of the hall.\n")
        choice = input('> ')
        while True:
            if choice == "1":
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                print(f"""
\n{charactor} runs as fast as {gender_he_she} can twoards the end of the hall.
Just as {gender_he_she} gets a few steps in the lights come back on and
hanging in front of {gender_him_her} is a scaly creature hanging from the
ceiling its tongue so long it is touching the floor at your feet.
By the time the light comes on {charactor} has moved within inches of
the creature.  It lashes with its tongue and grabs {charactor} around
the waste before {gender_he_she} could react.  struggling is useless as the
creature swallows {charactor} whole.\n
""")
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                die()
            elif choice == "2":
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                print(f"""
You turn on the flashlight and see a scaly creature hanging
from the ceiling its mouth open and its long tongue almost touching the floor.
What do you do?
""")
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                time.sleep(3)
                print("1. Grab the tongue and pull down")
                print("2. Jump up and slap the alien in the face")
                if "weapon" and "charge" in items:
                    print("3. Shoot with weapon.")
                action = input('> ')
                while True:
                    if action == "1":
                        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                        print(f"""
{charactor} reaches out for the tongue and pulls as hard as {gender_he_she} can.
The creature loses its hold on the ceiling and comes crashing to the floor.
{charactor} stomps on its face until it doesn't move anymore.
""")
                        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                        rooms_cleared.append("hallb_clear")
                        hall_b_done()
                    elif action == "2":
                        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                        print(f"""
The tongue creature is disoriented but recovers quickly.  before {charactor}
can react its long tongue whips twoard {gender_him_her} and
wraps around {gender_his_her}waist.
Struggling is useless as the creature swallows {charactor} whole.
""")
                        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                        die()
                    elif "weapon" and "charge" in items:
                        if action == "3":
                            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                            print(f"""
{charactor} shoots the creature in the mouth and it falls off the ceiling
and lands in a heap on the ground in front of {charactor}
""")
                            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                            items.remove("charge")
                            rooms_cleared.append("hallb_clear")
                            hall_b_done()
                        else:
                            action = action = input("> ")
                    elif action == "items":
                        print(items)
                        action = action = input('above is a list of your items.  What next?\n> ')
                    else:
                        print("That is not a valid option.")
                        action = action = input("> ")
            elif choice == "3":
                hall_a()
            elif choice == "items":
                print(items)
                choice = choice = input('above is a list of your items.  What next?\n> ')
            else:
                print("That is not a valid option.")
                choice = choice = input("> ")
    if 'hallb_clear' in rooms_cleared:
        hall_b_done()
    else:
        hall_b()


def hall_b_done():
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print(f"""
{charactor} enters the hallway and see's the long tongued creature
dead on the floor.  There are two doors on the east end of the hallway,
one door to the north, and a door to the south.  What do you do?
""")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    time.sleep(3)
    print("1. Go to the east end of the hallway.")
    print("2. Go to the north door.")
    print("3. go to the south door.")
    choice = input('> ')
    while True:
        if choice == "1":
            hall_a()
        elif choice == "2":
            library_gate()
        elif choice == "3":
            case_room_gate()
        elif choice == "items":
            print(items)
            choice = choice = input('above is a list of your items.  What next?\n> ')
        else:
            print("That is not a valid option.")
            choice = choice = input("> ")

def case_room_gate():
    def case_room():
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print(f"""
In side the room you see a case with a screen on it.  It reads \n:
At night they come without being fetched,
And by day they are lost without being stolen.
What am I?
""")
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        time.sleep(3)
        answer = input('> ')
        if answer == "star" or "stars":
            items.append("charge")
            rooms_cleared.append("case_clear")
            print(f"{charactor} has gained a weapon charge!")
        elif choice == "items":
            print(items)
            choice = choice = input('above is a list of your items.  What next?\n> ')
        else:
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            print("The case locks with a red screen and cannot be opened.")
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            print("1. leave room")
            rooms_cleared.append("case_clear")
            choice = input('> ')
            while True:
                if choice == "1":
                    hall_b_gate()
                elif choice == "items":
                    print(items)
                    choice = choice = input('> ')
                else:
                    print("That is not a valid option.")
                    choice = choice = input("> ")
    if 'case_clear' in rooms_cleared:
        return True and case_room_done()
    else:
        case_room()



def case_room_done():
    if "case_clear" in rooms_cleared:
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print(f"""
{charactor}see's the case in the room but can't do
anything else with it.
""")
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print("1. Leave room out the north door.")
        choice = input('> ')
        if choice == "1":
            hall_b_gate()
        elif choice == "items":
            print(items)
            choice = choice = input('above is a list of your items.  What next?\n> ')
        else:
            print("That is not a valid option.")
            choice = choice = input("> ")
    else:
        case_room_gate()


def stock():
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print(f"""
{charactor} enter a store room where the food is kept.
At first it looks normal but then {charactor} notices small
blobs that look like cotton balls scurrying around.
There is a door to the north, and a door to the south.  What do you do?
""")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    time.sleep(3)
    print("1. Take a closer look at the cotton ball creatures.")
    print("2. Go to the north door.")
    print("3. Go to the south door.")
    print("4. Start to stomp on the cotton ball creatures.")
    choice = input('> ')
    while True:
        if choice == "1":
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            print(f'''
When {charactor} bends over to take a closer look {gender_he_she}
sees what looks like a tiny face.  It wispers to him
"Would you like to know a secret?\n"
''')
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            print("1. Yes")
            print("2. No")
            answer = input('> ')
            if answer == "1":
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                print('The cotton ball creature wispers"The code is 5 2 6"')
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                stock()
            else:
                print(f"""
leaving the creatures alone {charactor} looks around the room\n
""")
                stock()
        elif choice == "2":
            armory_gate()
        elif choice == "3":
            hall_a()
        elif choice == "items":
            print(items)
            choice = choice = input('above is a list of your items.  What next?\n> ')
        elif choice == "4":
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            print(f"""
{charactor} starts to stomp around squishing as many of the
cotton ball creatures as you can reach.  After {charactor} kills
two creatures they all start to vibrate violently.  Confused {charactor}
take a step back as the creatures start to swarm {gender_him_her}.
They climb all over {charactor} until every inch of {gender_him_her}is
covered in them.  The vibration is so intense that it {charactor}
is heated rapidly until {gender_his_her} blood starts to boil and finaly falls.
""")
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            die()
        else:
            print("That is not a valid option.")
            choice = choice = input("> ")


def library_gate():
    def library():
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print(f"""
As {charactor} enter the stale air of the library fills {gender_his_her} nose.
There is a door on the north side and a door on the south side with
a window facing west.  What do you do?
""")
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        time.sleep(3)
        print("1. Go to north door")
        print("2. Go to south door")
        print("3. Go to the window")
        choice = input('> ')
        while True:
            if choice == "1":
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                print(f"""
As {charactor} approaches {gender_he_she} feels a sudden jerking under
{gender_his_her} feet and hears a loud crash.  {charactor} looks around and
all the shelves in the library are shaking precariously and large volumes
start to fall toward {gender_him_her} from every direction.  What do you do?
""")
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                time.sleep(3)
                print("1. Dodge left")
                print("2. Dodge right")
                print("3. Hide under a desk")
                action = input('> ')
                while True:
                    if action == "1":
                        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                        print(f"""
{charactor} dodges to the left just as a large leather bound book with
iron edges hurls down from a nearbye shelf.  The corner of the book wedges
itself firmly in the skull of {charactor} knocking {gender_him_her} unconious.
The rest of the vast library burys {charactor} alive.
""")
                        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                        die()
                    elif action == "2":
                        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                        print(f"""
{charactor} dodges to the right just as a large leather bound book with
iron edges hurls down from a nearbye shelf.  The corner of the book wedges
itself firmly in the skull of {charactor} knocking {gender_him_her} unconious.
The rest of the vast library burys{charactor} alive.
""")
                        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                        die()
                    elif action == "3":
                        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                        print(f"""
{charactor} dives under a nearbye desk to wait for everything to stop
moving around {gender_him_her}.  After everything stops shaking {charactor}
takes stock of {gender_his_her} condition.  Only a small bruise or two.
What do you do now?
""")
                        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                        time.sleep(3)
                        print("1. North door")
                        print("2. South door")
                        rooms_cleared.append("library_clear")
                        action_2 = input('> ')
                        while True:
                            if action_2 == "1":
                                comanders_gate()
                            elif action_2 == "2":
                                hall_b_gate()
                            elif action_2 == "items":
                                print(items)
                                action_2 = action_2 = input('above is a list of your items.  What next?\n> ')
                            else:
                                print("That is not a valid option.")
                                action_2 = action_2 = input('> ')
                    elif action == "items":
                        print(items)
                        action = action = input('above is a list of your items.  What next?\n> ')
                    else:
                        print("That is not a valid option.")
                        action = action = input("> ")
            elif choice == "2":
                hall_b_gate()
            elif choice == "3":
                window()
            elif choice == "items":
                print(items)
                choice = choice = input('above is a list of your items.  What next?\n> ')
            else:
                print("That is not a valid option.")
                action_2 = action_2 = input('> ')

    if 'library_clear' in rooms_cleared:
        library_done()
    else:
        library()

def window():
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print(f"""
{charactor} sees a large piece of space junk heading towards your ship!
That kind of impact would shake everything.  What do you do?
""")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    time.sleep(3)
    print("1. run to the door to the north")
    print("2. run to the door to the south")
    print("3. Stare in awe at your doom")
    print("4. Hide under a desk")
    choice = input("> ")
    while True:
        if choice == "1":
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            print(f"""
{charactor} runs to the north door just as a large leather bound book
with iron edges hurls down from a nearbye shelf.  The corner of the
book wedges itself firmly in the skull of {charactor} knocking {gender_him_her}
unconious.  The rest of the vast library burys {charactor} alive.
""")
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            die()
        elif choice == "2":
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            print(f"""
{charactor} runs to the south door just as a large leather bound book with
iron edges hurls down from a nearbye shelf.  The corner of the book wedges
itself firmly in the skull of {charactor} knocking {gender_him_her} unconious.
The rest of the vast library burys {charactor} alive.
""")
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            die()
        elif choice == "3":
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            print(f"""
{charactor} stares out the window in awe of the distruction about to
envelope {gender_him_her}.  As the space junk gets closer and closer
{charactor} reflects on {gender_his_her} acomplishments in this life.
{gender_he_she} comes to the conclusion that {gender_he_she} is happy
with {gender_his_her} existence.{charactor} basks in the explosion as the
space junk rips into the side of {gender_his_her} ship and with a smile
gets buried under the full weight of {gender_his_her} acumulated knowledge tombs.
""")
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            die()
        elif choice == "4":
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            print(f"""
{charactor} dives under a nearbye desk to wait for everything to stop
moving around {gender_him_her}.  After everything stops shaking {charactor}
takes stock of {gender_his_her} condition.  Only a small bruise or two.
What do you do now?
""")
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            time.sleep(3)
            print("1. North door")
            print("2. South door")
            rooms_cleared.append("library_clear")
            action_2 = input('> ')
            while True:
                if action_2 == "1":
                    comanders_gate()
                elif action_2 == "2":
                    hall_b_gate()
                elif action_2 == "items":
                    print(items)
                    action_2 = action_2 = input('above is a list of your items.  What next?\n> ')
                else:
                    print("That is not a valid option.")
                    action_2 = action_2 = input('> ')
        elif choice == "items":
            print(items)
            choice = choice = input('above is a list of your items.  What next?\n> ')
        else:
            print("That is not a valid option.")
            choice = choice = input('> ')

def library_done():
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print(f"""
There are books and tomes littering the floor.
There is a door on the north and south side.
""")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    time.sleep(3)
    print("1. Go to north door")
    print("2. Go to the south door")
    choice = input('> ')
    while True:
        if choice == "1":
            comanders_gate()
        elif choice == "2":
            hall_b_gate()
        elif choice == "items":
            print(items)
            choice = choice = input('above is a list of your items.  What next?\n> ')
        else:
            print("That is not a valid option.")
            library_done()


def comanders_gate():
    def comanders():
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print(f"""
When {charactor} enters what used to be the commander's quarters
{gender_he_she} can't help but notice that all the reflective surfaces
have been covered in cloth.  Perplexed {charactor} takes a look around the room.
There is a door with a numerical pad next to it on the east side, and a door
to the north, and a door to the south..  What do you do?
""")
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        time.sleep(3)
        print("1. Go to the north door.")
        print("2. Go to the east door with number pad.")
        print("3. Go to the south door.")
        choice = input('> ')
        while True:
            if choice == "1":
                ugly_boss_gate()
            elif choice == "2":
                number_pad_door_gate_comanders()
            elif choice == "3":
                library_gate()
            elif choice == "items":
                print(items)
                choice = choice = input('above is a list of your items.  What next?\n> ')
            else:
                print("That is not a valid option.")
                choice = choice = input('> ')
    if "num_pad" in rooms_cleared:
        comanders_done()
    else:
        comanders()

def number_pad_door_gate_comanders():
    def number_pad_door():
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print(f"""
{charactor} walks up to the door with a number pad next to it.
    It needs a three digit code.  What is the code?
""")
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        tri = 0
        success = False
        while tri < 3:
            code_attempt = input("> ")
            if code_attempt == "526":
                success = True
                armory_gate()
                break
            else:
                print("wrong code try again you get 3 tries total.")
            tri += 1
        if(not success):
            print("\nto many try's you fail\n")
            rooms_cleared.append("num_pad")
            comanders_done()
        else:
            print("something broke")
            armory_gate()
    if "num_pad" in rooms_cleared:
        number_pad_door_done()
    else:
        number_pad_door()

def number_pad_door_gate_armory():
    def number_pad_door():
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print(f"""
{charactor} walks up to the door with a number pad next to it.
It needs a three digit code.  What is the code?
""")
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        tri = 0
        success = False
        while tri < 3:
            code_attempt = input("> ")
            if code_attempt == "526":
                success = True
                print("That is the correct code")
                comanders_gate()
                break
            else:
                print("wrong code try again you get 3 tries total.")
            tri += 1
        if(not success):
            print("\nto many try's you fail\n")
            rooms_cleared.append("num_pad")
            armory_done()
        else:
            print("something broke")
            armory_gate()
    if "num_pad" in rooms_cleared:
        number_pad_door_done()
    else:
        number_pad_door()

def number_pad_door_done():
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print(f"""
{charactor} walks up to the door with a number pad next to it.
{charactor} had {gender_his_her} chance and messed it up.
""")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print("1. Go to the armory")
    print("2. Go to the comanders quarters")
    choice = input("> ")
    while True:
        if choice == "1":
            armory_gate()
        elif choice == "2":
            comanders_gate()
        elif choice == "items":
            print(items)
            choice = choice = input('above is a list of your items.  What next?\n> ')
        else:
            print("That is not a valid option.")
            choice = choice = input("> ")

def comanders_done():
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print(f"""
When {charactor} enters what used to be the commander's quarters
{gender_he_she} can't help but notice that all the reflective surfaces
have been covered in cloth.  Perplexed {charactor} takes a look around the room.
There is a door to the north, a door to the south, and a door with a number pad
that is security locked.  What do you do?
""")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    time.sleep(3)
    print("1. Go to the north door.")
    print("2. Go to the south door.")
    choice = input('> ')
    while True:
        if choice == "1":
            ugly_boss_gate()
        elif choice == "2":
            library_gate()
        elif choice == "items":
            print(items)
            choice = choice = input('above is a list of your items.  What next?\n> ')
        else:
            print("That is not a valid option.")
            choice = choice = input('> ')

def armory_gate():
    def armory():
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print(f"""
{charactor} walks into to find a makeshift bed in the middle of what
used to be an armory.  There are pieces of paper with writing strewn
about in a language {gender_he_she} does not understand.  One you see has a
circular shape cut in half with one side black and the other white.  There is
a door to the north, a door on the west with a numerical pad next to it,
and a door to the south.  What do you do?
""")
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        time.sleep(3)
        print("1. Go to the north door")
        print("2. Go to the west door with the number pad")
        print("3. Go to the south door")
        choice = input("> ")
        while True:
            if choice == "1":
                gray_boss_gate()
            elif choice == "2":
                number_pad_door_gate_armory()
            elif choice == "3":
                stock()
            elif choice == "items":
                print(items)
                choice = choice = input('above is a list of your items.  What next?\n> ')
            else:
                print("That is not a valid option.")
                choice = choice = input('> ')

    if "num_pad" in rooms_cleared:
        armory_done()
    else:
        armory()

def armory_done():
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print(f"""
{charactor} walks into to find a makeshift bed in the middle of
what used to be an armory.  There are pieces of paper with writing strewn
about in a language {gender_he_she} does not understand.  One you see has
a circular shape cut in half with one side black and the other white.
There is a door to the north and a door to the south.  What do you do?
""")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    time.sleep(3)
    print("1. Go to the north door")
    print("2. Go to the south door")
    choice = input("> ")
    while True:
        if choice == "1":
            gray_boss_gate()
        elif choice == "2":
            stock()
        elif choice == "items":
            print(items)
            choice = choice = input('above is a list of your items.  What next?\n> ')
        else:
            print("That is not a valid option.")
            choice = choice = input('> ')

def gray_boss_gate():
    def gray_boss():
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print(f"""
{charactor} enters the room to see a smallish creature covered with
gray hair.  The creature looks at {gender_him_her} and says
“Is it worthy to be in my presence?  Does it have the mental capacity
to challenge the old one?”   What do you do?
""")
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        time.sleep(3)
        print("1. Proclaim you are smart enough")
        print("2. Try to run past the creature to the cockpit room")
        if "weapon" and "charge" in items:
            print("3. Shoot with weapon")
        choice = input('> ')
        if choice == "1":
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            print("""
“Then I will test you with my favorite puzzle.”
“Answer this and I shall let you pass:
Always old, sometimes new.
Never sad, sometimes blue.
Never empty, sometimes full.
Never pushes, always pulls.  “What am I?”
""")
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            answer = input("> ")
            if answer == "Moon" or "moon":
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                print('''
The creature looks pleased.  "You are smarter then you look!"
And steps aside to let you pass
''')
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                if ("ugly_clear" or "ugly_clear_wep") in rooms_cleared:
                    print("\nBoth doors to the cockpit have been unlocked.\n")
                print("1. Go to the north door cockpit")
                print("2. Go to the south door")
                rooms_cleared.append("gray_clear")
                action = input('> ')

                while True:
                    if action == "1":
                        if ("gray_clear_wep" or "gray_clear") and ("ugly_clear" or "ugly_clear_wep") in rooms_cleared:
                            last_boss()
                        else:
                            print(f"You must unlock both doors before {charactor} can go to the cockpit.")
                            action = action = input('> ')

                    elif action == "2":
                        armory_gate()
                    elif action == "items":
                        print(items)
                        action = action = input('above is a list of your items.  What next?\n> ')
                    else:
                        print("That is not a valid option.")
                        action = action = input('> ')
            elif answer == "items":
                print(items)
                answer = answer = input('above is a list of your items.  What next?\n> ')
            else:
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                print(f'''
The gray creature frowns after {charactor} says {gender_his_her}
answer obviously displeased.  "You had good potential but it seems you are
as slow-witted as everyone else" the creature says.  "Ah well begone then"
and with that {charactor} is lifted into mid air and slowly compressed into
a smaller and smaller invisible cube.  Gasping for breath {charactor} tries
to break free but it is useless by the time it is done {charactor} is
pressed into a 2 ft by 2 ft cube on the ground.  The gray creature strolls
over, picks up the cube, and stores it in the closet next to a dozen others.
''')
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                die()
        if choice == "2":
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            print(f'''
{charactor} is frozen in place by an unknown force.  “You will proceed
if you are worthy.  Answer this my favorite puzzle” the creature said.
"Get it correct and you shall pass":
Always old, sometimes new.
Never sad, sometimes blue.
Never empty, sometimes full.
Never pushes, always pulls.  “What am I?”
''')
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            time.sleep(3)
            answer = input("> ")
            if answer == "Moon" or "moon":
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                print('''
The creature looks pleased.  "You are smarter then you look!"
And steps aside to let you pass
''')
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                print("1. Go to the north door cockpit")
                print("2. Go to the south door")
                rooms_cleared.append("gray_clear")
                action = input('> ')
                while True:
                    if action == "1":
                        if ("gray_clear_wep" or "gray_clear") and ("ugly_clear" or "ugly_clear_wep") in rooms_cleared:
                            last_boss()
                        else:
                            print("Both doors to the cockpit need to be unlocked.")
                            action = action = input("> ")
                    elif action == "2":
                        armory_gate()
                    elif action == "items":
                        print(items)
                        action = action = input('above is a list of your items.  What next?\n> ')
                    else:
                        print("That is not a valid option.")
                        action = action = input('> ')
            elif answer == "items":
                print(items)
                answer = answer = input('above is a list of your items.  What next?\n> ')
            else:
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                print(f'''
The gray creature frowns after {charactor} says {gender_his_her} answer
obviously displeased.  "You had good potential but it seems you are as
slow-witted as everyone else" the creature says.  "Ah well begone then" and
with that {charactor} is lifted into mid air and slowly compressed into
a smaller and smaller invisible cube.  Gasping for breath {charactor} tries
to break free but it is useless by the time it is done {charactor} is
pressed into a 2 ft by 2 ft cube on the ground.  The gray creature strolls
over picks up the cube and stores it in the closet next to a dozen others.
''')
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                die()

        if choice == "3":
            if "weapon" and "charge" in items:
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                print(f"""
{charactor} reaches for {gender_his_her} plasma gun and takes a shot.  The creature
staggers but stays conscious.  It will take two shots to bring this one down.
""")
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                time.sleep(3)
                items.remove("charge")
                if "weapon" and "charge" in items:
                    print("1. take another shot")
                    print("2. save shot")
                    action = input('> ')
                    if action == "1":
                        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                        print("""
The second shot hits the gray creature in the face and he falls back dead.
One of two lights next to the north door turns green.
""")
                        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                        rooms_cleared.append("gray_clear_wep")
                        if ("ugly_clear" or "ugly_clear_wep") in rooms_cleared:
                            rooms_cleared.append("last_boss_unlocked")
                            print("Both rooms doors have unlocked and the cockpit is accessable.")
                            gray_boss_done_gate()
                    elif action == "2":
                        gray_boss_gate()
                    elif action == "items":
                        print(items)
                        action = action = input('above is a list of your items.  What next?\n> ')
                    else:
                        print("That is not a valid option.")
                        action = action = input('> ')
                else:
                    gray_boss_gate()
        elif choice == "items":
            print(items)
            choice = choice = input('above is a list of your items.  What next?\n> ')
        else:
            print("That is not a valid option.")
            choice = choice = input('> ')
    if "gray_clear" in rooms_cleared:
        gray_boss_done_gate()
    elif "gray_clear_wep" in rooms_cleared:
        gray_boss_done_gate()
    else:
        gray_boss()

def gray_boss_done_gate():
    if "gray_clear_wep" in rooms_cleared:
        gray_boss_done_wep()
    elif "gray_clear" in rooms_cleared:
        gray_boss_done_reg()

def gray_boss_done_reg():
    print(f"""
{charactor} see's the gray creature in the corner meditating.
it opens one eye and gives a small nod.  There is a door to the north and
a door to the south.
""")
    time.sleep(3)
    print("1. Go to north door")
    print("2. Go to south door")
    choice = input("> ")
    while True:
        if choice == "1":
            if "last_boss_unlocked" in rooms_cleared:
                last_boss()
            else:
                print(f"{charactor} must unlock both doors before gaining access to the cockpit.")
                choice = choice = input("> ")
        elif choice == "2":
            armory_gate()
        elif choice == "items":
            print(items)
            choice = choice = input('above is a list of your items.  What next?\n> ')
        else:
            print("That is not a valid option.")
            choice = choice = input('> ')

def gray_boss_done_wep():
    print(f"""
{charactor} see's the gray creature in the corner with a large hole in
its head.  There is a door to the north and a door to the south.
""")
    print("1. Go to north door")
    print("2. Go to south door")
    choice = input("> ")
    while True:
        if choice == "1":
            if "last_boss_unlocked" in rooms_cleared:
                last_boss()
            else:
                print(f"{charactor} must unlock both doors before gaining access to the cockpit.")
                choice = choice = input("> ")
        elif choice == "2":
            armory_gate()
        elif choice == "items":
            print(items)
            choice = choice = input('above is a list of your items.  What next?\n> ')
        else:
            print("That is not a valid option.")
            choice = choice = input('> ')

def ugly_boss_gate():
    def ugly_boss():
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print(f'''
{charactor} enters the room to see a disgusting being with gnarled skin and
multiple warts on its face.  It turns to {charactor} and growls
“What are you doing here?  I will rip you apart!”  The being starts towards
{charactor} when {gender_he_she} looks around the room and notice the
same cloth is on all surfaces.  What do you do?
''')
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        time.sleep(3)
        print("1. Take the cloth off a nearby table")
        print("2. Take the cloth off what looks like a mirror")
        if "weapon" and "charge" in items:
            print("3. Shoot with weapon")
        choice = input("> ")
        while True:
            if choice == "1":
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                print(f"""
{charactor} pulls on the cloth that is covering the table.
Nothing happens and the ugly being reaches {charactor} who has a confused
look on {gender_his_her} face.  {charactor} stands there like a dope while
the ugly creature rips {gender_his_her} limbs off one by one.
""")
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                die()
            elif choice == "2":
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                print(f'''
As {charactor} uncovers the mirror the being sees its reflection and stops
in its tracks.  “I am hidious!!! Look at me!!” The being colapses in a heap
on the floor convulsing with sobs.  One of the two lights next to the north
door light up green.  There is the north door and the south door.
What do you do?
''')
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                time.sleep(3)
                if ("gray_clear" or "gray_clear_wep") in rooms_cleared:
                    print("\nBoth doors to the cockpit have been unlocked.\n")
                rooms_cleared.append("ugly_clear")
                print("1. Go to the north door")
                print("2. Go to the south door")
                action = input("> ")
                while True:
                    if action == "1":
                        if ("gray_clear" or "gray_clear_wep") in rooms_cleared:
                            last_boss()
                        else:
                            print("Both doors to the cockpit need to be unlocked.")
                            action = action = input("> ")
                    elif action == "2":
                        comanders_gate()
                    elif action == "items":
                        print(items)
                        action = action = input('above is a list of your items.  What next?\n> ')
                    else:
                        print("That is not a valid entry")
                        action = action = input("> ")
            elif choice == "3":
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                if "weapon" and "charge" in items:
                    print(f"""
{charactor} reaches for {gender_his_her} plasma gun and takes a shot.
The creature takes a hit on the side but is not completely stopped.
It will take two shots to bring this one down.
""")
                    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                    time.sleep(3)
                    items.remove("charge")
                    if "weapon" and "charge" in items:
                        print("1. take another shot")
                        print("2. save shot")
                        action = input('> ')
                        if action == "1":
                            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                            print(f"""
The second shot hits it square in the thigh and the being falls to the ground.
ground writhing in pain.  Taking the oppurtunity {charactor} springs
forward and proceeds to stomp on the ugly beings head until it no longer moved.
One of two lights next to the north door turns green.
""")
                            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                            time.sleep(3)
                            rooms_cleared.append("ugly_clear_wep")
                            if ("gray_clear_wep" or "gray_clear") in rooms_cleared:
                                rooms_cleared.append("last_boss_unlocked")
                                print("Both rooms doors have unlocked and the cockpit is accessable.")
                            ugly_boss_done_gate()

                        elif action == "2":
                            ugly_boss_gate()
                        elif action == "items":
                            print(items)
                            action = action = input('above is a list of your items.  What next?\n> ')
                        else:
                            print("That is not a valid option.")
                            action = action = input('> ')
            elif choice == "items":
                print(items)
                choice = choice = input('above is a list of your items.  What next?\n> ')

            else:
                print("That is not a valid option.")
                choice = choice = input('> ')
    if "ugly_clear" in rooms_cleared:
        ugly_boss_done_gate()
    elif "ugly_clear_wep" in rooms_cleared:
        ugly_boss_done_gate()
    else:
        ugly_boss()

def ugly_boss_done_gate():
    if "ugly_clear" in rooms_cleared:
        ugly_boss_done_reg()
    elif "ugly_clear_wep" in rooms_cleared:
        ugly_boss_done_wep()
    else:
        print("something broke in ugly_boss_done_gate")

def ugly_boss_done_reg():
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print(f"""
{charactor} sees the ugly being on the floor in the corner sobbing
uncontrolably.  There is a feeling of guilt in {gender_his_her} gut but
then {gender_he_she} remembers that the creature want to kill {gender_him_her}.
There is a door to the Northand a door to the south.
""")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    time.sleep(3)
    print("1. Go to the north door.")
    print("2. Go to the south door.")
    choice = input("> ")
    while True:
        if choice == "1":
            if "last_boss_unlocked" in rooms_cleared:
                last_boss()
            else:
                print("Both doors to the cockpit must be unlocked to gain access.")
                choice = choice = input("> ")
        elif choice == "2":
            comanders_gate()
        elif choice == "items":
            print(items)
            choice = choice = input('above is a list of your items.  What next?\n> ')
        else:
            print("That is not a valid option.")
            choice = choice = input('> ')

def ugly_boss_done_wep():
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print(f"""
{charactor} sees the ugly being on the floor with two large holes in its body.
There is a door to the North and a door to the south.
    """)
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    time.sleep(3)
    print("1. Go to the north door.")
    print("2. Go to the south door.")
    choice = input("> ")
    while True:
        if choice == "1":
            if "last_boss_unlocked" in rooms_cleared:
                last_boss()
            else:
                print("Both doors to the cockpit must be unlocked to gain access.")
                choice = choice = input("> ")
        elif choice == "2":
            comanders_gate()
        elif choice == "items":
            print(items)
            choice = choice = input('above is a list of your items.  What next?\n> ')
        else:
            print("That is not a valid option.")
            choice = choice = input('> ')

def last_boss():
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print(f'''
When {charactor} enters the cockpit {gender_he_she} sees an imposing
humanoid figure in a commander's uniform sitting in the captain's
chair and staring at {gender_him_her}.  “Did you have fun with my pets?”
The commander said.
''')
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    time.sleep(3)
    print("1. Yes, they are all dead now")
    print("2. No, why do you keep such creatures here")
    print("3. why are you here?")
    choice = input("> ")
    while True:
        if choice == "1":
            last_boss_why()
        elif choice == "2":
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            print(f'''
“They are my side project to keep me entertained while roaming the galaxy.
You have been but an experiment for me.  I wanted to see if you could
best them all and you have not disappointed me."
''')
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            time.sleep(3)
            print("1. Why are you here?")
            action = action = input("> ")
            while True:
                if action == "1":
                    last_boss_why()
                else:
                    print("That is not a valid option.")
                    action = action = input("> ")
        elif choice == "3":
            last_boss_why()

        else:
            print("That is not a valid option.")
            choice = choice = input("> ")

def last_boss_why():
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print(f'''
“I roam the galaxy finding intelligent life to test against other forms I
have collected.  I have been watching your progress and am pleased to say
you have exceeded my expectations.  Now you will travel with me forever to
test against all other forms throughout deep space.”  What do you do?
''')
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    time.sleep(3)
    print("1. Look around the room")
    print("2. Charge the commander")
    if "weapon" and "charge" in items:
        print("3. Use weapon")
    choice = input("> ")
    while True:
        if choice == "1":
            last_boss_look()
        elif choice == "2":
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            print(f"""
{charactor} charges at the commander meaning to knock him off his feet and
whipe the smug smile off his face.  Just before {charactor} reaches him
however the commander fast as lightning whips a longish staff in the
direction of {charactor}'s face.  The staff catches {charactor} in the
temple with a force that is far beyond human strength.  {charactor} falls
to the floor completely unresponsive.  The commander looks disappointed
then casually grabs a sphere from inside his pocket pushes a button and
tosses it on the ground.  {charactor}.  The sphere sucks {charactor} inside
itself traping {gender_him_her} for later use in any trials the
commander sees fit.
""")
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            die()
        elif choice == "3":
            if ("weapon" and "charge") in items:
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                print(f'''
{charactor} pulls out {gender_his_her} plasma gun and takes a shot.
The commander easily dodges the shot and laughs at {charactor}.
"That will not work on me I am afraid but I admire your curage."
''')
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                time.sleep(3)
                items.remove("charge")
                choice = choice = input("Make another choice\n> ")
            else:
                print(f"{charactor} does not have any charges")
                choice = choice = input("Make another choice\n> ")
        elif choice == "items":
            print(items)
            choice = choice = input('above is a list of your items.  What next?\n> ')
        else:
            print("That is not a valid entry.")
            choice = choice = input("Make another choice\n> ")


def last_boss_look():
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print(f"""
{charactor} sees a small sphere with a button on it placed on the table
to the left.  On the right is the emergency fire alarm/extinguisher.
Straight ahead is the commander sitting in front of the ship controls.
What do you do?
""")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    time.sleep(3)
    print("1. Leap for the ship controls")
    print("2. Go for the extinguisher")
    print("3. Go for the sphere on the table")
    if "weapon" and "charge" in items:
        print("4. Use weapon")
    choice = input("> ")
    while True:
        if choice == "1":
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            print(f"""
{charactor} charges at the commander meaning to knock him off his feet
and whipe the smug smile off his face.  Just before {charactor} reaches him
however the commander fast as lightning whips a longish staff in the
direction of {charactor}'s face.  The staff catches {charactor} in the
temple with a force that is far beyond human strength.  {charactor} falls
to the floor completely unresponsive.  The commander looks disappointed then
casually grabs a sphere from inside his pocket pushes a button and tosses
it on the ground.  The sphere sucks {charactor} inside itself traping
{gender_him_her} for later use in any trials the commander sees fit.
""")
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            die()
        elif choice == "2":
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            print(f"""
You jump to pull the extinguisher lever and the whole room fills with
a white smokey substance.  What do you do next?
""")
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            time.sleep(3)
            print("1. Go for the ship controls")
            print("2. Grab the sphere")
            action = input("> ")
            while True:
                if action == "1":
                    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                    print(f"""
{charactor} feels {gender_his_her} surroundings and makes {gender_his_her}
way to the ship controls.  Once {gender_he_she} gets there {gender_he_she}
initiates ships internal security measures.  A laser comes down from the
ceiling and shoots the commander dead.
""")
                    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                    win()
                elif action == "2":
                    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                    print(f"""
{charactor} fumbles around to try and find the sphere on the table.
{gender_he_she} trips over a box on the ground you didn't see because of
the smoke.  In that instance the commander grabs the sphere and uses it
to cage you inside.  You spend the rest of your life in the service of the
commander in the trials he puts on.
""")
                    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                    die()
                elif action == "items":
                    print(items)
                    action = action = input('above is a list of your items.  What next?\n> ')
                else:
                    print("That is not a valid entry.")
                    action = action = input("Make another choice\n> ")
        elif choice == "3":
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            print(f"""
{charactor} grabs the sphere pushes the button and throws it at the commander.
With a scream the commander is thrown inside the sphere with a loud crack.
You can now do what you wish with the caged commander.
""")
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            win()
        elif choice == "4":
            if ("weapon" and "charge") in items:
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                print(f'''
{charactor} pulls out {gender_his_her} plasma gun and takes a shot.
The commander easily dodges the shot and laughs at {charactor}.
"That will not work on me I am afraid but I admire your curage."
''')
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                time.sleep(3)
            else:
                print(f"{charactor} does not have enough charges for that")
                choice = choice = input("Make another choice\n>  ")
        elif choice == "items":
            print(items)
            choice = choice = input('above is a list of your items.  What next?\n> ')
        else:
            print("That is not a valid entry.")
            choice = choice = input('> ')

def win():
    time.sleep(5)
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print(f"""
{charactor} has taken back {gender_his_her} ship and survived many trials.
The commander is gone and {charactor} may do as {gender_he_she} wishes.
Will {gender_he_she} go find more adventures throughout the galaxy or
decide to retire after this ordeal.  Even {gender_he_she} doesnt know.
""")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    time.sleep(3)
    print("Thank you for playing!")
    print("if you would like to play again type 'play'")
    print("if you would like to exit type 'exit'")
    choice = input("> ")
    items.clear()
    rooms_cleared.clear()
    if choice == "play":
        start_room()
    if choice == "exit":
        exit()
    else:
        print("That is not a valid input")
        choice = choice = input('> ')


def die():
    time.sleep(5)
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    time.sleep(1)
    print("{}           {}")
    print("  \  _---_  /")
    time.sleep(1)
    print("   \/     \/")
    print("    |() ()|")
    print("     \ + /")
    time.sleep(1)
    print("    / HHH  \ ")
    print("   /  \_/   \ ")
    print(" {}          {}")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    items.clear()
    rooms_cleared.clear()
    time.sleep(3)
    print(f"\n\n{charactor} is super dead!  Would you like to try again?\n")
    print("press 'Y' to start over")
    print("type exit to quit")

    choice = input("> ")
    while True:
        if choice == "Y":
            start_room()
        elif choice == "y":
            start_room()
        elif choice == "exit":
            exit(0)
        else:
            print("That doesnt do anything.")
            choice = choice = input('> ')


while True:
    gender = input("\nWhat is your gender? (male or female)")
    if gender == "male":
        print("You have chosen male")
        gender_him_her = "him"
        gender_his_her = "his"
        gender_he_she = "he"
        start_room()
        break
    elif gender == "Male":
        print("you have chosen male")
        gender_him_her = "him"
        gender_his_her = "his"
        gender_he_she = "he"
        start_room()
        break
    elif gender == "female":
        print("you have chosen female")
        gender_him_her = "her"
        gender_his_her = "her"
        gender_he_she = "she"
        start_room()
        break
    elif gender == "Female":
        print("you have chosen female")
        gender_him_her = "her"
        gender_his_her = "her"
        gender_he_she = "she"
        start_room()
        break
    else:
        print(f"\n'{gender}'is not a real gender!  I know I am not PC :P")


if charactor == "test.mode":
    module = input('Enter the name of a function:\n>>> ')
    while True:
        if module == "weps":
            print("weapon and charges added to items")
            items.append("weapon")
            items.append("charge")
            items.append("charge")
            module = module = input('Enter the name of a function:\n>>> ')

        elif module == "weps1":
            print("weapon and charges added to items")
            items.append("weapon")
            items.append("charge")
            module = module = input('Enter the name of a function:\n>>> ')

        elif module == "items":
            print(items)
            module = module = input('Enter the name of a function:\n>>> ')

        elif callable(globals()[module]):
            test_mode(globals()[module])

        else:
            print("that is not a function")
            module = module = input('Enter the name of a function:\n>>> ')
