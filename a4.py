import sys
import time
from time import sleep

your_room = 1
living_room = 2
kitchen = 3
tv_room = 4
backyard = 5
washroom = 6
dining_room = 7
outside = 8
garage = 9
backyard = 10
bus_stop_1 = 11
garden = 12
highschool = 13
music_room = 14
cafeteria = 15
library = 16
auditorium = 17
storage_room = 18
back_of_school = 19
side_of_school = 20
bus_stop_2 = 21
crushs_street = 22
crushs_house = 23
door_to_crushs_room = 24
crushs_room = 25

def initialize_game_data():
    #in_inventory? True = Yes, False = No

    game_data = {
        "current_room": 1,
        "game_over": False,
        "score": 0,
        "note": False,
        "letter": False,
        "phone": False,
        "cash": False,
        "scissors": False,
        "keys": False,
        "knife": False,
        "chocolates": False,
        "cologne": False,
        "hammer": False,
        "flowers": False,
        "music": False,
        "necklace": False,
    }

    return game_data


def initialize_rooms():
    rooms = {
        #1-10
        "your_room": [ ("south",living_room), ("leave",living_room) ],
        "living_room": [ ("west",tv_room), ("south",backyard), ("east",kitchen), ("north",outside) ],
        "kitchen": [ ("north",dining_room), ("south",washroom) ],
        "tv_room": [ ("east",living_room), ("leave",living_room) ],
        "backyard": [ ("north",living_room), ("leave",living_room) ],
        "washroom": [ ("north",kitchen), ("leave",kitchen) ],
        "dining_room": [ ("south",kitchen), ("leave",kitchen) ],
        "outside": [ ("south",living_room), ("west",garage), ("east",backyard), ("north",bus_stop_1) ],
        "garage": [ ("north",highschool), ("east",outside) ],
        "backyard": [ ("leave",outside), ("west",outside) ],

        #11-20
        "bus_stop_1": [ ("north",highschool), ("east",garden), ("south",outside) ],
        "garden": [ ("leave",bus_stop_1), ("west",bus_stop_1) ],
        "highschool": [ ("north",music_room) ],
        "music_room": [ ("south",highschool), ("west",cafeteria), ("east",auditorium), ("north",back_of_school) ],
        "cafeteria": [ ("south",library) ],
        "library": [ ("leave",cafeteria), ("north",cafeteria) ],
        "auditorium": [ ("south",storage_room), ("west",music_room) ],
        "storage_room": [ ("leave",auditorium), ("north",auditorium) ],
        "back_of_school": [ ("south",music_room), ("north",bus_stop_2), ("east",side_of_school) ],
        "side_of_school": [ ("leave",back_of_school), ("west",back_of_school) ],

        #21-25
        "bus_stop_2": [ ("south",back_of_school), ("north",crushs_street) ],
        "crushs_street": [ ("north",crushs_house) ],
        "crushs_house": [ ("north",door_to_crushs_room) ],
        "door_to_crushs_room": [ ("north",crushs_room) ],
        "crushs_room": []
    }

    return rooms


def initialize_room_data():
    #Exists? True = Yes, False = No
    room_data = {
        #1-9
        "your_room": { "note": True,
                       "letter": True,
                       "phone": True},
        "living_room": { "cash": True,
                         "scissors": True,
                         "keys": True,
                         "mom": True,
                         "visited": False},
        "kitchen": { "knife": True,
                     "chocolates": True,
                     "visited": False},
        "tv_room": { "TV": True,
                     "dad": True,
                    "visited": False},
        "backyard": { "sister": True,
                      "visited": False},
        "washroom": { "cologne": True,
                      "visited": False},
        "dining_room": {"visited": False},
        "outside": {"visited": False},
        "garage": { "car": True,
                    "hammer": True,
                    "visited": False},

        #10-19
        "bus_stop_1": { "uber_driver": True,
                        "visited": False},
        "garden": { "flowers": True,
                     "visited": False},
        "highschool": { "TV": True,
                        "visited": False},
        "music_room": { "band_director": True,
                        "music": True,
                        "crushs_friend": True,
                        "visited": False},
        "cafeteria": { "bully": True,
                       "visited": False},
        "library": {"visited": False},
        "auditorium": { "necklace": True,
                        "visited": False},
        "storage_room": {"visited": False},
        "back_of_school": {"visited": False},
        "side_of_school": {"visited": False},

        #20-24
        "bus_stop_2": {"visited": False},
        "crushs_street": {"visited": False},
        "crushs_house": {"visited": False},
        "door_to_crushs_room": {"visited": False},
        "crushs_room": {"visited": False}
    }

    return room_data


def handle_user_input():
    user_input = input("What's next? ")
    words = user_input.upper().strip().split()

    return words


def words_to_pairs(words):

    if len(words) == 1:
        return words

    words_in_pairs = []

    for x in range (0, len(words)-1):
        pair_string =  words[x] + " " + words[x+1]
        words_in_pairs.append(pair_string)

    return words_in_pairs


def input_validity(words):
    flag = False
    if "TAKE" in words or "DROP" in words or "EXAMINE" in words or "USE" in words or "TALK" in words or "ASK" in words or "LOOK" in words or "NORTH" in words or "EAST" in words or "SOUTH" in words or "WEST" in words:
        flag = True

    return flag


def handle_room_your_room(game_data, rooms, room_data):
    print_string = """ Your room is dark except for your red LED strips in your room.
    You sit in front of your computer monitor with assignments overdue and exams rapidly approaching. 
    You haven’t gotten a notification on your phone in days.
    You’re staring at two pieces of mail your mom threw on your desk earlier.
    One of them is an advertisement from the local pizza place. The other has no obvious markings on the outside except for a date scribbled on it. It dates approximately ten years into the future.
    You tear open the envelope and read the contents.
    There's no doubt that you signed the letter. The letter describes what seems to be your perfect ideal partner.
    You slowly start to realize this can only mean one person.\n"""

    for letter in print_string:
        sleep(0.01)
        sys.stdout.write(letter)
        sys.stdout.flush()
    print("\n")

    print_string = ""
    words = handle_user_input()
    while(not input_validity(words)):
        print("Invalid input")
        words = handle_user_input()

    words_in_pairs = words_to_pairs(words)
    
    if "TAKE" in words or "DROP" in words or "EXAMINE" in words or "USE" in words:
        #User wants to do something with an object
        if "TAKE" in words:
            if "TAKE DOCTOR" in words_in_pairs or "DOCTOR NOTE" in words_in_pairs:
                for key in room_data["your_room"]:
                    if key == "note" and room_data["your_room"][key] == True:
                        game_data["note"] = True
                        room_data["your_room"][key] = False
                        print_string = """Took the doctor's note\n"""
            elif "TAKE LETTER" in words_in_pairs:
                for key in room_data["your_room"]:
                    if key == "letter" and room_data["your_room"][key] == True:
                        game_data["letter"] = True
                        room_data["your_room"][key] = False
                        print_string = """Took the letter\n"""
            elif "TAKE PHONE" in words_in_pairs:
                for key in room_data["your_room"]:
                    if key == "phone" and room_data["your_room"][key] == True:
                        game_data["phone"] = True
                        room_data["your_room"][key] = False
                        print_string = """Took your phone\n"""
            else:
                print_string = """No such item to interact with
                
                """

        elif "DROP" in words:
            did_drop = False
            for key in game_data:
                if words[1].lower() == key and game_data[key] == True:
                    game_data[key] = False
                    print_string = "Dropped the " + key + "\n"
                    did_drop = True
                    break
            if not did_drop:
                return_string = """You don't have this object to drop
                
                """

        elif "EXAMINE" in words:
            if "EXAMINE DOCTOR" in words_in_pairs or "DOCTOR NOTE" in words_in_pairs:
                print_string = """A doctor's note. After the pandemic, the value of a doctor's note on the street crashed.
                This one is legit though.
                
                """
            elif "EXAMINE LETTER" in words_in_pairs:
                print_string = """ It's a letter detailing your ideal partner. It seems to be signed by you.
                You never get mail let alone from yourself 10 years into the future. Frankly, you're not sure what to do.
                
                """
            elif "EXAMINE PHONE" in words_in_pairs:
                print_string = """It's your phone. You thought it was super cool to own one but you don't use it much except for browsing a few sites.
                You don't even really use it to play video games because you have a PC. It's essentially a thousand-dollar telephone.
                
                """
            else:
                print_string = """No such item to examine
                
                """

        elif "USE" in words:
            print_string = "You can't use that here\n\n"

    elif "TALK" in words or "ASK" in words:
        #User wants to interact with an NPC
        print_string = "There's nobody to interact with here\n\n"
    elif "LOOK" in words:
        #User wants to LOOK
        print_string = """This is your room. It's fairly cluttered but you swear that you know where everything is.
        It's pretty dark and you're too lazy to draw the curtains. It's an overall depressing place to dwell.

        """
    elif "NORTH" in words or "EAST" in words or "SOUTH" in words or "WEST" in words:
        if "SOUTH" in words:
            game_data["current_room"] = living_room
        else:
            print_string = "You can't go that way\n\n"
    
    if print_string:
        for letter in print_string:
            sleep(0.01)
            sys.stdout.write(letter)
            sys.stdout.flush()


def handle_room_living_room(game_data, rooms, room_data):
    print_string = """You are temporarily blinded from the natural light coming from the living room as you step out for the first time in a week.
    Your mom doesn’t notice you as she’s busy cutting her arts and crafts for her weekly meetup with her friends.
    Sprawled across the table are various items including a pair of scissors, some car keys, her phone, and some cash."""

    for letter in print_string:
        sleep(0.01)
        sys.stdout.write(letter)
        sys.stdout.flush()
    print("\n")

    for key in room_data["living_room"]:
        if key == "visited" and room_data["living_room"][key] == False:
            room_data["living_room"][key] = True
            game_data["score"] += 10

    print_string = ""
    words = handle_user_input()
    while(not input_validity(words)):
        print("Invalid input")
        words = handle_user_input()

    words_in_pairs = words_to_pairs(words)
    
    if "TAKE" in words or "DROP" in words or "EXAMINE" in words or "USE" in words:
        #User wants to do something with an object
        if "TAKE" in words:
            if "TAKE CASH" in words_in_pairs:
                for key in room_data["living_room"]:
                    if key == "cash" and room_data["living_room"][key] == True:
                        game_data["cash"] = True
                        room_data["living_room"][key] = False
                        print_string = """Took the cash\n"""
            elif "TAKE SCISSORS" in words_in_pairs:
                for key in room_data["living_room"]:
                    if key == "scissors" and room_data["living_room"][key] == True:
                        game_data["scissors"] = True
                        room_data["living_room"][key] = False
                        print_string = """Took the scissors\n"""
            elif "TAKE CAR" in words_in_pairs or "CAR KEYS" in words_in_pairs :
                for key in room_data["living_room"]:
                    if key == "keys" and room_data["living_room"][key] == True:
                        game_data["keys"] = True
                        room_data["living_room"][key] = False
                        print_string = """Took the car keys\n"""
            elif "TAKE PHONE" in words_in_pairs :
                print_string = """You shouldn't take what isn't yours
                
                """
            else:
                print_string = """No such item to interact with
                
                """

        elif "DROP" in words:
            did_drop = False
            for key in game_data:
                if words[1].lower() == key and game_data[key] == True:
                    game_data[key] = False
                    print_string = "Dropped the " + key + "\n"
                    did_drop = True
                    break
            if not did_drop:
                return_string = """You don't have this object to drop
                
                """

        elif "EXAMINE" in words:
            if "EXAMINE CAR" in words_in_pairs or "CAR KEYS" in words_in_pairs:
                print_string = """Car keys to the Toyota Corolla out front. You wanted a Tesla but your family can't afford one.
                
                """
            elif "EXAMINE CASH" in words_in_pairs:
                print_string = """Just some loose change. Probably only enough for a one way trip somewhere close.
                
                """
            elif "EXAMINE PHONE" in words_in_pairs:
                print_string = """It's your mom's phone. She takes better care of it even though it's three generations behind yours.
                
                """
            elif "EXAMINE SCISSORS" in words_in_pairs:
                print_string = """A pair of scissors. Not sharp enough to kill, but pointy enough to do some severe damage.
                Only a lunatic would consider taking these.
                
                """
            else:
                print_string = """No such item to examine
                
                """

        elif "USE" in words:
            print_string = "You can't use that here\n\n"

    elif "TALK" in words or "ASK" in words:
        #User wants to interact with an NPC
        if "TALK MOM" in words_in_pairs or "TO MOM" in words_in_pairs or "ASK MOM" in words_in_pairs:
            print_string = """ You decide not to bother your mom. She's clearly busy and you don't want to get on her bad side.
            Perhaps another day.
            
            """
        else:
            print_string = """No such person to interact with

            """

    elif "LOOK" in words:
        #User wants to LOOK
        print_string = """It's the living room. Your mom practically lives here.
        It's very neat and tidy and frankly, it kind of pisses you off. You don't know why, but it does.

        """
    elif "NORTH" in words or "EAST" in words or "SOUTH" in words or "WEST" in words:
        if "SOUTH" in words:
            game_data["current_room"] = backyard
        elif "EAST" in words:
            game_data["current_room"] = kitchen
        elif "WEST" in words:
            game_data["current_room"] = tv_room
        elif "NORTH" in words:
            game_data["current_room"] = outside
        else:
            print_string = """You can't go that way
            
            """
    
    if print_string:
        for letter in print_string:
            sleep(0.01)
            sys.stdout.write(letter)
            sys.stdout.flush()


def handle_room_kitchen(game_data, rooms, room_data):
    print_string = """Tabletop cleaning solution fumes fill the air. Despite that, the stove looks very clean.
    A fairly cramped space if you ask me.
    There's a knife and some chocolates on the countertop.
    """

    for letter in print_string:
        sleep(0.01)
        sys.stdout.write(letter)
        sys.stdout.flush()
    print("\n")

    for key in room_data["kitchen"]:
        if key == "visited" and room_data["kitchen"][key] == False:
            room_data["kitchen"][key] = True
            game_data["score"] += 10

    print_string = ""
    words = handle_user_input()
    while(not input_validity(words)):
        print("Invalid input")
        words = handle_user_input()

    words_in_pairs = words_to_pairs(words)
    
    if "TAKE" in words or "DROP" in words or "EXAMINE" in words or "USE" in words:
        #User wants to do something with an object
        if "TAKE" in words:
            if "TAKE KNIFE" in words_in_pairs:
                for key in room_data["kitchen"]:
                    if key == "knife" and room_data["kitchen"][key] == True:
                        game_data["knife"] = True
                        room_data["kitchen"][key] = False
                        print_string = """Took the knife\n"""
            elif "TAKE CHOCOLATES" in words_in_pairs or "TAKE CHOCOLATE" in words_in_pairs:
                for key in room_data["kitchen"]:
                    if key == "chocolates" and room_data["kitchen"][key] == True:
                        game_data["chocolates"] = True
                        room_data["kitchen"][key] = False
                        print_string = """Took the chocolates\n"""
            else:
                print_string = """No such item to interact with
                
                """

        elif "DROP" in words:
            did_drop = False
            for key in game_data:
                if words[1].lower() == key and game_data[key] == True:
                    game_data[key] = False
                    print_string = "Dropped the " + key + "\n"
                    did_drop = True
                    break
            if not did_drop:
                return_string = """You don't have this object to drop
                
                """

        elif "EXAMINE" in words:
            if "EXAMINE CAR" in words_in_pairs or "CAR KEYS" in words_in_pairs:
                print_string = """Car keys to the Toyota Corolla out front. You wanted a Tesla but your family can't afford one.
                
                """
            elif "EXAMINE CASH" in words_in_pairs:
                print_string = """Just some loose change. Probably only enough for a one way trip somewhere close.
                
                """
            elif "EXAMINE PHONE" in words_in_pairs:
                print_string = """It's your mom's phone. She takes better care of it even though it's three generations behind yours.
                
                """
            elif "EXAMINE SCISSORS" in words_in_pairs:
                print_string = """A pair of scissors. Not sharp enough to kill, but pointy enough to do some severe damage.
                Only a lunatic would consider taking these.
                
                """
            else:
                print_string = """No such item to examine
                
                """

        elif "USE" in words:
            print_string = "You can't use that here\n\n"

    elif "TALK" in words or "ASK" in words:
        #User wants to interact with an NPC

        print_string = """No such person to interact with

        """

    elif "LOOK" in words:
        #User wants to LOOK
        print_string = """It's a normal kitchen. Not much to look at honestly. Very plain.

        """
    elif "NORTH" in words or "EAST" in words or "SOUTH" in words or "WEST" in words:
        if "SOUTH" in words:
            game_data["current_room"] = washroom
        elif "NORTH" in words:
            game_data["current_room"] = dining_room
        else:
            print_string = """You can't go that way
            
            """
    
    if print_string:
        for letter in print_string:
            sleep(0.01)
            sys.stdout.write(letter)
            sys.stdout.flush()


def handle_room_tv_room(game_data, rooms, room_data):
    print_string = """The TV room. Extremely messy and your dad practically lives here too.
    He never cleans up after himself and all he does is watch soap operas all day.
    He's extremely lazy too.
    """

    for letter in print_string:
        sleep(0.01)
        sys.stdout.write(letter)
        sys.stdout.flush()
    print("\n")

    for key in room_data["tv_room"]:
        if key == "visited" and room_data["tv_room"][key] == False:
            room_data["tv_room"][key] = True
            game_data["score"] += 10

    print_string = ""
    words = handle_user_input()
    while(not input_validity(words)):
        print("Invalid input")
        words = handle_user_input()

    words_in_pairs = words_to_pairs(words)
    
    if "TAKE" in words or "DROP" in words or "EXAMINE" in words or "USE" in words:
        #User wants to do something with an object
        if "TAKE" in words:
            print_string = """No such item to interact with
            
            """

        elif "DROP" in words:
            did_drop = False
            for key in game_data:
                if words[1].lower() == key and game_data[key] == True:
                    game_data[key] = False
                    print_string = "Dropped the " + key + "\n"
                    did_drop = True
                    break
            if not did_drop:
                return_string = """You don't have this object to drop
                
                """

        elif "EXAMINE" in words:
            if "EXAMINE TV" in words_in_pairs:
                print_string = """It's a pretty old television. It's a flatscreen though.
                Not that it matters since your dad just hogs it all day long anyways.
                
                """
            else:
                print_string = """No such item to examine
                
                """

        elif "USE" in words:
            print_string = "You can't use that here\n\n"

    elif "TALK" in words or "ASK" in words:
        #User wants to interact with an NPC
        if "TALK DAD" in words_in_pairs:
            print_string = """*grunt*

            ...
            """
        else:
            print_string = """No such person to interact with

            """

    elif "LOOK" in words:
        #User wants to LOOK
        print_string = """It's cluttered with objects such as newspapers, teabags, and candy wrappers.
        You often wonder to yourself if your father was a raccoon in a past life.

        """
    elif "NORTH" in words or "EAST" in words or "SOUTH" in words or "WEST" in words:
        if "EAST" in words:
            game_data["current_room"] = living_room
        else:
            print_string = """You can't go that way
            
            """
    
    if print_string:
        for letter in print_string:
            sleep(0.01)
            sys.stdout.write(letter)
            sys.stdout.flush()


def handle_room_backyard(game_data, rooms, room_data):
    print_string = """The backyard is full of weeds and overgrown plants you don't know the name of.
    It looks like rural Australia. Your sister is busy hanging up the laundry.

    """

    for letter in print_string:
        sleep(0.01)
        sys.stdout.write(letter)
        sys.stdout.flush()
    print("\n")

    for key in room_data["backyard"]:
        if key == "visited" and room_data["backyard"][key] == False:
            room_data["backyard"][key] = True
            game_data["score"] += 10

    print_string = ""
    words = handle_user_input()
    while(not input_validity(words)):
        print("Invalid input")
        words = handle_user_input()

    words_in_pairs = words_to_pairs(words)
    
    if "TAKE" in words or "DROP" in words or "EXAMINE" in words or "USE" in words:
        #User wants to do something with an object
        if "TAKE" in words:
            print_string = """No such item to interact with
            
            """

        elif "DROP" in words:
            did_drop = False
            for key in game_data:
                if words[1].lower() == key and game_data[key] == True:
                    game_data[key] = False
                    print_string = "Dropped the " + key + "\n"
                    did_drop = True
                    break
            if not did_drop:
                return_string = """You don't have this object to drop
                
                """

        elif "EXAMINE" in words:
            print_string = """No such item to examine
            
            """

        elif "USE" in words:
            print_string = "You can't use that here\n\n"

    elif "TALK" in words or "ASK" in words:
        #User wants to interact with an NPC
        if "TALK SISTER" in words_in_pairs:
            print_string = """ "Leave me alone you nerd."

            How hostile.

            """
        else:
            print_string = """No such person to interact with

            """

    elif "LOOK" in words:
        #User wants to LOOK
        print_string = """The lawn hasn't been mowed since last summer. The grass is knee high and the weeds have started to scale the house.
        You're lucky your neighbors haven't called by-law on you.

        """
    elif "NORTH" in words or "EAST" in words or "SOUTH" in words or "WEST" in words:
        if "NORTH" in words:
            game_data["current_room"] = living_room
        else:
            print_string = """You can't go that way
            
            """
    
    if print_string:
        for letter in print_string:
            sleep(0.01)
            sys.stdout.write(letter)
            sys.stdout.flush()


def handle_room_washroom(game_data, rooms, room_data):
    print_string = """The backyard is full of weeds and overgrown plants you don't know the name of.
    It looks like rural Australia. Your sister is busy hanging up the laundry.

    """

    for letter in print_string:
        sleep(0.01)
        sys.stdout.write(letter)
        sys.stdout.flush()
    print("\n")

    for key in room_data["washroom"]:
        if key == "visited" and room_data["washroom"][key] == False:
            room_data["washroom"][key] = True
            game_data["score"] += 10

    print_string = ""
    words = handle_user_input()
    while(not input_validity(words)):
        print("Invalid input")
        words = handle_user_input()

    words_in_pairs = words_to_pairs(words)
    
    if "TAKE" in words or "DROP" in words or "EXAMINE" in words or "USE" in words:
        #User wants to do something with an object
        if "TAKE COLOGNE" in words_in_pairs:
                for key in room_data["washroom"]:
                    if key == "cologne" and room_data["washroom"][key] == True:
                        game_data["cologne"] = True
                        room_data["washroom"][key] = False
                        print_string = """Took the cologne\n"""
        else:
            print_string = """No such item to interact with
            
            """

        if "DROP" in words:
            did_drop = False
            for key in game_data:
                if words[1].lower() == key and game_data[key] == True:
                    game_data[key] = False
                    print_string = "Dropped the " + key + "\n"
                    did_drop = True
                    break
            if not did_drop:
                return_string = """You don't have this object to drop
                
                """

        elif "EXAMINE" in words:
            if "EXAMINE COLOGNE" in words_in_pairs:
                print_string = """It's a cheap cologne but nobody can really tell. Probably purchased it from a dollar store.
                
                """
            else:
                print_string = """No such item to examine
                
                """

        elif "USE" in words:
            if "USE COLOGNE" in words_in_pairs and game_data["cologne"] == True:
                game_data["cologne"] = False
                print_string = """You used the cologne. You smell a bit better now.
                
                """
            else:
                print_string = """No such item to use
                
                """

    elif "TALK" in words or "ASK" in words:
        #User wants to interact with an NPC

        print_string = """No such person to interact with

        """

    elif "LOOK" in words:
        #User wants to LOOK
        print_string = """It's a normal washroom. There's no soap left though. The toilet seat is also up.

        """
    elif "NORTH" in words or "EAST" in words or "SOUTH" in words or "WEST" in words:
        if "NORTH" in words:
            game_data["current_room"] = kitchen
        else:
            print_string = """You can't go that way
            
            """
    
    if print_string:
        for letter in print_string:
            sleep(0.01)
            sys.stdout.write(letter)
            sys.stdout.flush()


def handle_room_dining_room(game_data, rooms, room_data):
    print_string = """The backyard is full of weeds and overgrown plants you don't know the name of.
    It looks like rural Australia. Your sister is busy hanging up the laundry.

    """

    for letter in print_string:
        sleep(0.01)
        sys.stdout.write(letter)
        sys.stdout.flush()
    print("\n")

    for key in room_data["dining_room"]:
        if key == "visited" and room_data["dining_room"][key] == False:
            room_data["dining_room"][key] = True
            game_data["score"] += 10

    print_string = ""
    words = handle_user_input()
    while(not input_validity(words)):
        print("Invalid input")
        words = handle_user_input()

    words_in_pairs = words_to_pairs(words)
    
    if "TAKE" in words or "DROP" in words or "EXAMINE" in words or "USE" in words:
        #User wants to do something with an object
        if "TAKE" in words:

            print_string = """No such item to interact with
            
            """

        elif "DROP" in words:
            did_drop = False
            for key in game_data:
                if words[1].lower() == key and game_data[key] == True:
                    game_data[key] = False
                    print_string = "Dropped the " + key + "\n"
                    did_drop = True
                    break
            if not did_drop:
                return_string = """You don't have this object to drop
                
                """

        elif "EXAMINE" in words:

            print_string = """No such item to examine
            
            """

        elif "USE" in words:
            if "USE COLOGNE" in words_in_pairs and game_data["cologne"] == True:
                game_data["cologne"] = False
                print_string = """You used the cologne. You smell a bit better now.
                
                """
            else:
                print_string = """No such item to use
                
                """

    elif "TALK" in words or "ASK" in words:
        #User wants to interact with an NPC

        print_string = """No such person to interact with

        """

    elif "LOOK" in words:
        #User wants to LOOK
        print_string = """It's not a bad looking dining room for your family's standards, however nobody has eaten on it for years.
        You can't remember the last time you had guests over.

        """
    elif "NORTH" in words or "EAST" in words or "SOUTH" in words or "WEST" in words:
        if "SOUTH" in words:
            game_data["current_room"] = kitchen
        else:
            print_string = """You can't go that way
            
            """
    
    if print_string:
        for letter in print_string:
            sleep(0.01)
            sys.stdout.write(letter)
            sys.stdout.flush()


def handle_room_outside(game_data, rooms, room_data):
    print_string = """The great outdoors. The birds are chirping. The sun is shining. The cicadas are screeching.

    """

    for letter in print_string:
        sleep(0.01)
        sys.stdout.write(letter)
        sys.stdout.flush()
    print("\n")

    for key in room_data["outside"]:
        if key == "visited" and room_data["outside"][key] == False:
            room_data["outside"][key] = True
            game_data["score"] += 10

    print_string = ""
    words = handle_user_input()
    while(not input_validity(words)):
        print("Invalid input")
        words = handle_user_input()

    words_in_pairs = words_to_pairs(words)
    
    if "TAKE" in words or "DROP" in words or "EXAMINE" in words or "USE" in words:
        #User wants to do something with an object
        if "TAKE" in words:

            print_string = """No such item to interact with
            
            """

        elif "DROP" in words:
            did_drop = False
            for key in game_data:
                if words[1].lower() == key and game_data[key] == True:
                    game_data[key] = False
                    print_string = "Dropped the " + key + "\n"
                    did_drop = True
                    break
            if not did_drop:
                return_string = """You don't have this object to drop
                
                """

        elif "EXAMINE" in words:

            print_string = """No such item to examine
            
            """

        elif "USE" in words:
            if "USE COLOGNE" in words_in_pairs and game_data["cologne"] == True:
                game_data["cologne"] = False
                print_string = """You used the cologne. You smell a bit better now.
                
                """
            else:
                print_string = """No such item to use
                
                """

    elif "TALK" in words or "ASK" in words:
        #User wants to interact with an NPC

        print_string = """No such person to interact with

        """

    elif "LOOK" in words:
        #User wants to LOOK
        print_string = """It's 20 degrees with a breeze. It's a beautiful day for any outdoor activity.
        You're honestly surprised at how nice it is today. You haven't been outside in a long, long time.
        The sudden Vitamin D intake is refreshing.

        """
    elif "NORTH" in words or "EAST" in words or "SOUTH" in words or "WEST" in words:
        if "NORTH" in words:
            game_data["current_room"] = bus_stop_1
        elif "SOUTH" in words:
            game_data["current_room"] = living_room
        elif "EAST" in words:
            game_data["current_room"] = backyard
        elif "WEST" in words:
            game_data["current_room"] = garage
        else:
            print_string = """You can't go that way
            
            """
    
    if print_string:
        for letter in print_string:
            sleep(0.01)
            sys.stdout.write(letter)
            sys.stdout.flush()


def handle_room_garage(game_data, rooms, room_data):
    print_string = """Your unfinished garage reeks of mold and chalk, not to mention the smell of gasoline.
    It's extremely hot inside as it's essentially become a greenhouse in the hot summer days.
    Theres a hammer and a car here.

    """

    for letter in print_string:
        sleep(0.01)
        sys.stdout.write(letter)
        sys.stdout.flush()
    print("\n")

    for key in room_data["garage"]:
        if key == "visited" and room_data["garage"][key] == False:
            room_data["garage"][key] = True
            game_data["score"] += 10

    print_string = ""
    words = handle_user_input()
    while(not input_validity(words)):
        print("Invalid input")
        words = handle_user_input()

    words_in_pairs = words_to_pairs(words)
    
    if "TAKE" in words or "DROP" in words or "EXAMINE" in words or "USE" in words:
        #User wants to do something with an object
        if "TAKE" in words:
            if "TAKE HAMMER" in words_in_pairs:
                for key in room_data["garage"]:
                    if key == "hammer" and room_data["garage"][key] == True:
                        game_data["hammer"] = True
                        room_data["garage"][key] = False
                        print_string = """Took the hammer\n"""
            elif "TAKE CAR" in words_in_pairs:
                for key in room_data["garage"]:
                    if key == "phone" and room_data["garage"][key] == True:
                        if game_data["keys"] == True:
                            game_data["phone"] = True
                            room_data["garage"][key] = False
                            print_string = """Took the car to school\n"""
                            game_data["current_room"] = highschool
                            break
                        else:
                            print_string = """You don't have the keys to this car...\n"""

            else:
                print_string = """No such item to interact with"""

        elif "DROP" in words:
            did_drop = False
            for key in game_data:
                if words[1].lower() == key and game_data[key] == True:
                    game_data[key] = False
                    print_string = "Dropped the " + key + "\n"
                    did_drop = True
                    break
            if not did_drop:
                return_string = """You don't have this object to drop
                
                """

        elif "EXAMINE" in words:
            if "EXAMINE HAMMER" in words_in_pairs:
                print_string = """Yep. This is a hammer all right. You could probably nail someone's head in with this.
                
                """
            elif "EXAMINE CAR" in words_in_pairs:
                print_string = """It's the family car. You don't drive it much since its the only car your family has and your dad needs it for work.
                
                """
            else:
                print_string = """No such item to examine
                
                """

        elif "USE" in words:
            if "USE COLOGNE" in words_in_pairs and game_data["cologne"] == True:
                game_data["cologne"] = False
                print_string = """You used the cologne. You smell a bit better now.
                
                """
            else:
                print_string = """No such item to use
                
                """

    elif "TALK" in words or "ASK" in words:
        #User wants to interact with an NPC

        print_string = """No such person to interact with

        """

    elif "LOOK" in words:
        #User wants to LOOK
        print_string = """The hammer looks to be a nice weapon to defend yourself with. The car also looks enticing but you need keys first to avoid setting off the alarm.

        """
    elif "NORTH" in words or "EAST" in words or "SOUTH" in words or "WEST" in words:
        if "EAST" in words:
            game_data["current_room"] = outside
        else:
            print_string = """You can't go that way
            
            """
    
    if print_string:
        for letter in print_string:
            sleep(0.01)
            sys.stdout.write(letter)
            sys.stdout.flush()


def handle_room_backyard(game_data, rooms, room_data):
    pass


def handle_room_bus_stop_1(game_data, rooms, room_data):
    print_string = """The public transit bus stop. You're lucky they put one so close to your house.
    It's only a 2 minute walk from your house. For some odd reason, there's an Uber Driver near the stop.

    """

    for letter in print_string:
        sleep(0.01)
        sys.stdout.write(letter)
        sys.stdout.flush()
    print("\n")

    for key in room_data["bus_stop_1"]:
        if key == "visited" and room_data["bus_stop_1"][key] == False:
            room_data["bus_stop_1"][key] = True
            game_data["score"] += 10

    print_string = ""
    words = handle_user_input()
    while(not input_validity(words)):
        print("Invalid input")
        words = handle_user_input()

    words_in_pairs = words_to_pairs(words)
    
    if "TAKE" in words or "DROP" in words or "EXAMINE" in words or "USE" in words:
        #User wants to do something with an object
        if "TAKE" in words:
            if "TAKE UBER" in words_in_pairs or "TAKE TAXI" in words_in_pairs:
                for key in room_data["bus_stop_1"]:
                    if key == "uber_driver" and room_data["bus_stop_1"][key] == True:
                        if game_data["cash"] == True:
                            print_string = """Took an Uber to school\n"""
                            game_data["current_room"] = highschool
                            break
                        else:
                            print_string = """You don't have the cash for this ride...\n"""

            else:
                print_string = """No such item to interact with"""

        elif "DROP" in words:
            did_drop = False
            for key in game_data:
                if words[1].lower() == key and game_data[key] == True:
                    game_data[key] = False
                    print_string = "Dropped the " + key + "\n"
                    did_drop = True
                    break
            if not did_drop:
                return_string = """You don't have this object to drop
                
                """

        elif "EXAMINE" in words:

            print_string = """No such item to examine
            
            """

        elif "USE" in words:
            if "USE COLOGNE" in words_in_pairs and game_data["cologne"] == True:
                game_data["cologne"] = False
                print_string = """You used the cologne. You smell a bit better now.
                
                """

            elif "USE CASH" in words_in_pairs and game_data["cash"] == True:
                game_data["cash"] = False
                print_string = """Took an Uber to school\n"""
                game_data["current_room"] = highschool
                
            else:
                print_string = """No such item to use
                
                """

    elif "TALK" in words or "ASK" in words:
        #User wants to interact with an NPC
        if "TALK UBER" in words_in_pairs or "TO UBER" in words_in_pairs or "ASK UBER" in words_in_pairs:
            print_string = """ "This ain't a charity kid. You need to get somewhere I need money. Capitalism buddy."
            
            """
        else:
            print_string = """No such person to interact with

            """

    elif "LOOK" in words:
        #User wants to LOOK
        print_string = """You have no idea what time the bus is going to arrive and you probably should waste time waiting.
        Your once in a lifetime opportunity may pass you up. It's probably best to take that Uber.

        """
    elif "NORTH" in words or "EAST" in words or "SOUTH" in words or "WEST" in words:
        if "EAST" in words:
            game_data["current_room"] = garden
        else:
            print_string = """You can't go that way
            
            """
    
    if print_string:
        for letter in print_string:
            sleep(0.01)
            sys.stdout.write(letter)
            sys.stdout.flush()


def handle_room_garden(game_data, rooms, room_data):
    print_string = """It's the garden beside the bus stop. It's pretty beautiful and you can smell the pollen in the air.
    It's probably kept by the city so that explains the tidyness of it.
    The flowers are especially pretty.

    """

    for letter in print_string:
        sleep(0.01)
        sys.stdout.write(letter)
        sys.stdout.flush()
    print("\n")

    for key in room_data["garden"]:
        if key == "visited" and room_data["garden"][key] == False:
            room_data["garden"][key] = True
            game_data["score"] += 10

    print_string = ""
    words = handle_user_input()
    while(not input_validity(words)):
        print("Invalid input")
        words = handle_user_input()

    words_in_pairs = words_to_pairs(words)
    
    if "TAKE" in words or "DROP" in words or "EXAMINE" in words or "USE" in words:
        #User wants to do something with an object
        if "TAKE" in words:
            if "TAKE FLOWERS" in words_in_pairs or "TAKE FLOWER" in words_in_pairs:
                for key in room_data["garden"]:
                    if key == "flowers" and room_data["garden"][key] == True:
                        game_data["flowers"] = True
                        room_data["garden"][key] = False
                        print_string = """Picked some flowers\n"""

            else:
                print_string = """No such item to interact with"""

        elif "DROP" in words:
            did_drop = False
            for key in game_data:
                if words[1].lower() == key and game_data[key] == True:
                    game_data[key] = False
                    print_string = "Dropped the " + key + "\n"
                    did_drop = True
                    break
            if not did_drop:
                return_string = """You don't have this object to drop
                
                """

        elif "EXAMINE" in words:
            if "EXAMINE FLOWERS" in words_in_pairs or "EXAMINE FLOWER" in words_in_pairs:
                print_string = """There are many beautiful flowers such as lilacs, dandelions, even sunflowers.
                The most practical species here to pick seems to be the buttercups.
                
                """

            else:
                print_string = """No such item to examine
                
                """

        elif "USE" in words:
            if "USE COLOGNE" in words_in_pairs and game_data["cologne"] == True:
                game_data["cologne"] = False
                print_string = """You used the cologne. You smell a bit better now.
                
                """
            else:
                print_string = """No such item to use
                
                """

    elif "TALK" in words or "ASK" in words:
        #User wants to interact with an NPC

        print_string = """No such person to interact with

        """

    elif "LOOK" in words:
        #User wants to LOOK
        print_string = """There are so many beautiful flowers here, it's easy to get lost flower-gazing.
        You nearly start to fall into a trance until you catch yourself. You see some pretty yellow flowers.
        You contemplate picking them.

        """
    elif "NORTH" in words or "EAST" in words or "SOUTH" in words or "WEST" in words:
        if "WEST" in words:
            game_data["current_room"] = bus_stop_1
        else:
            print_string = """You can't go that way
            
            """
    
    if print_string:
        for letter in print_string:
            sleep(0.01)
            sys.stdout.write(letter)
            sys.stdout.flush()


def handle_room_highschool(game_data, rooms, room_data):
    print_string = """It's the highschool you currently attend. You hate it here. It's pushed you to the brink of suicide.
    You wonder what the point of education even is. Where will you ever need to use the equation of a tangent line?
    You're pissed off just thinking about it. But you're here today for one reason.

    """

    for letter in print_string:
        sleep(0.01)
        sys.stdout.write(letter)
        sys.stdout.flush()
    print("\n")

    for key in room_data["highschool"]:
        if key == "visited" and room_data["highschool"][key] == False:
            room_data["highschool"][key] = True
            game_data["score"] += 10

    print_string = ""
    words = handle_user_input()
    while(not input_validity(words)):
        print("Invalid input")
        words = handle_user_input()

    words_in_pairs = words_to_pairs(words)
    
    if "TAKE" in words or "DROP" in words or "EXAMINE" in words or "USE" in words:
        #User wants to do something with an object
        if "TAKE" in words:
        
            print_string = """No such item to interact with"""

        elif "DROP" in words:
            did_drop = False
            for key in game_data:
                if words[1].lower() == key and game_data[key] == True:
                    game_data[key] = False
                    print_string = "Dropped the " + key + "\n"
                    did_drop = True
                    break
            if not did_drop:
                return_string = """You don't have this object to drop
                
                """

        elif "EXAMINE" in words:
            
            print_string = """No such item to examine
            
            """

        elif "USE" in words:
            if "USE COLOGNE" in words_in_pairs and game_data["cologne"] == True:
                game_data["cologne"] = False
                print_string = """You used the cologne. You smell a bit better now.
                
                """
            else:
                print_string = """No such item to use
                
                """

    elif "TALK" in words or "ASK" in words:
        #User wants to interact with an NPC

        print_string = """No such person to interact with

        """

    elif "LOOK" in words:
        #User wants to LOOK
        print_string = """It's just a giant building made of bricks. You long to see it demolished.
        There's nothing of interest outside the school.

        """
    elif "NORTH" in words or "EAST" in words or "SOUTH" in words or "WEST" in words:
        if "NORTH" in words:
            game_data["current_room"] = music_room
        else:
            print_string = """You can't go that way
            
            """
    
    if print_string:
        for letter in print_string:
            sleep(0.01)
            sys.stdout.write(letter)
            sys.stdout.flush()


def handle_room_music_room(game_data, rooms, room_data):
    print_string = """It's the music room. You used to actually be a part of the school band before you quit.
    It's a theory lecture today and people are doing a quiz. Your crush is a part of the band too but you don't see her right now. 
    The director looks pissed off. You see your crush's friend and she's holding your crush's sheet music.

    """

    for letter in print_string:
        sleep(0.01)
        sys.stdout.write(letter)
        sys.stdout.flush()
    print("\n")

    for key in room_data["music_room"]:
        if key == "visited" and room_data["music_room"][key] == False:
            room_data["music_room"][key] = True
            game_data["score"] += 10

    print_string = ""
    words = handle_user_input()
    while(not input_validity(words)):
        print("Invalid input")
        words = handle_user_input()

    words_in_pairs = words_to_pairs(words)
    
    if "TAKE" in words or "DROP" in words or "EXAMINE" in words or "USE" in words:
        #User wants to do something with an object
        if "TAKE" in words:
            if "TAKE SHEET" in words_in_pairs or "SHEET MUSIC" in words_in_pairs:
                for key in room_data["music_room"]:
                    if key == "music" and room_data["music_room"][key] == True:
                        game_data["music"] = True
                        room_data["music_room"][key] = False
                        print_string = """ "Oh hey, could you please return this sheet music back to her?
                        I think she left it here by accident"
                        
                        Took the sheet music\n
                        
                        """
            else:
                print_string = """No such item to interact with
                
                """

        elif "DROP" in words:
            did_drop = False
            for key in game_data:
                if words[1].lower() == key and game_data[key] == True:
                    game_data[key] = False
                    print_string = "Dropped the " + key + "\n"
                    did_drop = True
                    break
            if not did_drop:
                return_string = """You don't have this object to drop
                
                """

        elif "EXAMINE" in words:
            if "EXAMINE SHEET" in words_in_pairs or "SHEET MUSIC" in words_in_pairs or "EXAMINE MUSIC" in words_in_pairs:
                print_string = """It's your crush's sheet music. Maybe you can use it to try and talk to her.
                
                """
            else:
                print_string = """No such item to examine
                
                """

        elif "USE" in words:
            if "USE COLOGNE" in words_in_pairs and game_data["cologne"] == True:
                game_data["cologne"] = False
                print_string = """You used the cologne. You smell a bit better now.
                
                """
            elif "USE FLOWERS" in words_in_pairs and game_data["flowers"] == True:
                print_string = """Why are you giving me this? You should keep it.
                
                """
            elif "USE CHOCOLATES" in words_in_pairs and game_data["chocolates"] == True:
                print_string = """Why are you giving me this? You should keep it.
                
                """
            elif "USE DOCTOR" in words_in_pairs or "USE NOTE" in words_in_pairs and game_data["note"] == True:
                game_data["note"] = False
                print_string = """Oh she was absent today with a good reason? Ok.
                Thanks for letting me know kid.
                
                """
            
            else:
                print_string = """No such item to use
                
                """

    elif "TALK" in words or "ASK" in words:
        #User wants to interact with an NPC
        if "TALK FRIEND" in words_in_pairs or "TO CRUSH" in words_in_pairs or "CRUSH'S FRIEND" in words_in_pairs or "ASK FRIEND" in words_in_pairs:
            print_string = """ ...\n...\n...\n...\nAwkward.
            
            """
        else:
            print_string = """No such person to interact with

            """

    elif "LOOK" in words:
        #User wants to LOOK
        print_string = """It's a decent sized music room. Everyone is scribbling at their quiz.
        The band director is miffed. It's probably because of your crush ditching class. You might be able to bail her out.
        Her friend still has her sheet music.

        """
    elif "NORTH" in words or "EAST" in words or "SOUTH" in words or "WEST" in words:
        if "NORTH" in words:
            game_data["current_room"] = back_of_school
        elif "EAST" in words:
            game_data["current_room"] = auditorium
        elif "SOUTH" in words:
            game_data["current_room"] = highschool
        elif "WEST" in words:
            game_data["current_room"] = cafeteria
        else:
            print_string = """You can't go that way
            
            """
    
    if print_string:
        for letter in print_string:
            sleep(0.01)
            sys.stdout.write(letter)
            sys.stdout.flush()


def handle_room_cafeteria(game_data, rooms, room_data):
    print_string = """It's the cafeteria. Full of overpriced and expensive items, not to mention greasy.
    The lunchladys also exploit child labour laws in exchange for volunteer hours.
    Nobody really comes here to eat their lunch.

    """

    for letter in print_string:
        sleep(0.01)
        sys.stdout.write(letter)
        sys.stdout.flush()
    print("\n")

    for key in room_data["cafeteria"]:
        if key == "visited" and room_data["cafeteria"][key] == False:
            room_data["cafeteria"][key] = True
            game_data["score"] += 10

    print_string = ""
    words = handle_user_input()
    while(not input_validity(words)):
        print("Invalid input")
        words = handle_user_input()

    words_in_pairs = words_to_pairs(words)
    
    if "TAKE" in words or "DROP" in words or "EXAMINE" in words or "USE" in words:
        #User wants to do something with an object
        if "TAKE" in words:
            
            print_string = """No such item to interact with
            
            """

        elif "DROP" in words:
            did_drop = False
            for key in game_data:
                if words[1].lower() == key and game_data[key] == True:
                    game_data[key] = False
                    print_string = "Dropped the " + key + "\n"
                    did_drop = True
                    break
            if not did_drop:
                return_string = """You don't have this object to drop
                
                """

        elif "EXAMINE" in words:
            if "EXAMINE BULLY" in words_in_pairs:
                print_string = """It's the kid that beats up nerds for their lunch money.
                Despicable but at least he doesn't target you.
                
                """
            else:
                print_string = """No such item to examine
                
                """

        elif "USE" in words:
            if "USE COLOGNE" in words_in_pairs and game_data["cologne"] == True:
                game_data["cologne"] = False
                print_string = """You used the cologne. You smell a bit better now.
                
                """
            elif "USE FLOWERS" in words_in_pairs and game_data["flowers"] == True:
                print_string = """I don't think the bully would care for this.
                
                """
            elif "USE CHOCOLATES" in words_in_pairs and game_data["chocolates"] == True:
                print_string = """I don't think the bully would care for this.
                
                """
            
            else:
                print_string = """No such item to use
                
                """

    elif "TALK" in words or "ASK" in words:
        #User wants to interact with an NPC
        if "TALK BULLY" in words_in_pairs:
            print_string = """ Beat it nerd.
            
            """
        else:
            print_string = """No such person to interact with

            """

    elif "LOOK" in words:
        #User wants to LOOK
        print_string = """It's a pretty large cafeteria with large pane windows letting in the natural sunlight.
        You would be pretty psyched if the place itself was not packed with little kids and losers.

        """
    elif "NORTH" in words or "EAST" in words or "SOUTH" in words or "WEST" in words:
        if "EAST" in words:
            game_data["current_room"] = music_room
        elif "SOUTH" in words:
            game_data["current_room"] = library
        else:
            print_string = """You can't go that way
            
            """
    
    if print_string:
        for letter in print_string:
            sleep(0.01)
            sys.stdout.write(letter)
            sys.stdout.flush()


def handle_room_library(game_data, rooms, room_data):
    print_string = """The library. One of your favourite spots to hang out... not for studying, but for the free Wi-Fi.
    It's an extremely relaxing place and one of the only places you can go to without getting sidetracked.
    God Bless noise laws.

    """

    for letter in print_string:
        sleep(0.01)
        sys.stdout.write(letter)
        sys.stdout.flush()
    print("\n")

    for key in room_data["library"]:
        if key == "visited" and room_data["library"][key] == False:
            room_data["library"][key] = True
            game_data["score"] += 10

    print_string = ""
    words = handle_user_input()
    while(not input_validity(words)):
        print("Invalid input")
        words = handle_user_input()

    words_in_pairs = words_to_pairs(words)
    
    if "TAKE" in words or "DROP" in words or "EXAMINE" in words or "USE" in words:
        #User wants to do something with an object
        if "TAKE" in words:
            
            print_string = """No such item to interact with
            
            """

        elif "DROP" in words:
            did_drop = False
            for key in game_data:
                if words[1].lower() == key and game_data[key] == True:
                    game_data[key] = False
                    print_string = "Dropped the " + key + "\n"
                    did_drop = True
                    break
            if not did_drop:
                return_string = """You don't have this object to drop
                
                """

        elif "EXAMINE" in words:
            
            print_string = """No such item to examine
            
            """

        elif "USE" in words:
            if "USE COLOGNE" in words_in_pairs and game_data["cologne"] == True:
                game_data["cologne"] = False
                print_string = """You used the cologne. You smell a bit better now.
                
                """
            
            else:
                print_string = """No such item to use
                
                """

    elif "TALK" in words or "ASK" in words:
        #User wants to interact with an NPC
        
        print_string = """No such person to interact with

        """

    elif "LOOK" in words:
        #User wants to LOOK
        print_string = """This is the library that she always goes to after school.
        It's drumming up some bittersweet memories and you heart starts to strain.

        """
    elif "NORTH" in words or "EAST" in words or "SOUTH" in words or "WEST" in words:
        if "NORTH" in words:
            game_data["current_room"] = cafeteria
        else:
            print_string = """You can't go that way
            
            """
    
    if print_string:
        for letter in print_string:
            sleep(0.01)
            sys.stdout.write(letter)
            sys.stdout.flush()


def handle_room_auditorium(game_data, rooms, room_data):
    print_string = """The auditorium. One of the places your school is actually known for.
    From the school band, to the musicals performed by the drama class.

    """

    for letter in print_string:
        sleep(0.01)
        sys.stdout.write(letter)
        sys.stdout.flush()
    print("\n")

    for key in room_data["auditorium"]:
        if key == "visited" and room_data["auditorium"][key] == False:
            room_data["auditorium"][key] = True
            game_data["score"] += 10

    print_string = ""
    words = handle_user_input()
    while(not input_validity(words)):
        print("Invalid input")
        words = handle_user_input()

    words_in_pairs = words_to_pairs(words)
    
    if "TAKE" in words or "DROP" in words or "EXAMINE" in words or "USE" in words:
        #User wants to do something with an object
        if "TAKE" in words:
            if "TAKE NECKLACE" in words_in_pairs:
                for key in room_data["auditorium"]:
                    if key == "necklace" and room_data["auditorium"][key] == True:
                        game_data["necklace"] = True
                        room_data["auditorium"][key] = False
                        print_string = """Took the necklace\n
                        
                        """

        elif "DROP" in words:
            did_drop = False
            for key in game_data:
                if words[1].lower() == key and game_data[key] == True:
                    game_data[key] = False
                    print_string = "Dropped the " + key + "\n"
                    did_drop = True
                    break
            if not did_drop:
                return_string = """You don't have this object to drop
                
                """

        elif "EXAMINE" in words:
            if "EXAMINE NECKLACE" in words_in_pairs:
                print_string = """It's a pretty beautiful necklace but you aren't sure if the diamonds are real or not.
                But hey, a free necklace is a free necklace.
                
                """
            else:
                print_string = """No such item to examine
                
                """

        elif "USE" in words:
            if "USE COLOGNE" in words_in_pairs and game_data["cologne"] == True:
                game_data["cologne"] = False
                print_string = """You used the cologne. You smell a bit better now.
                
                """
            
            else:
                print_string = """No such item to use
                
                """

    elif "TALK" in words or "ASK" in words:
        #User wants to interact with an NPC

        print_string = """No such person to interact with

        """

    elif "LOOK" in words:
        #User wants to LOOK
        print_string = """A nice auditorium. Spacious yet cozy. You see a sparkle from the corner of your eye on one of the seats.
        It seems to be some kind of necklace.

        """
    elif "NORTH" in words or "EAST" in words or "SOUTH" in words or "WEST" in words:
        if "WEST" in words:
            game_data["current_room"] = music_room
        elif "SOUTH" in words:
            game_data["current_room"] = storage_room
        else:
            print_string = """You can't go that way
            
            """
    
    if print_string:
        for letter in print_string:
            sleep(0.01)
            sys.stdout.write(letter)
            sys.stdout.flush()


def handle_room_storage_room(game_data, rooms, room_data):
    print_string = """It's the storage room for the school bands and the drama club. You've only been inside on a few occasions.
    The entrance into the room itself is very narrow and can only fit one person at a time.
    It's pretty creepy with nobody else to talk to in here...

    """

    for letter in print_string:
        sleep(0.01)
        sys.stdout.write(letter)
        sys.stdout.flush()
    print("\n")

    for key in room_data["storage_room"]:
        if key == "visited" and room_data["storage_room"][key] == False:
            room_data["storage_room"][key] = True
            game_data["score"] += 10

    print_string = ""
    words = handle_user_input()
    while(not input_validity(words)):
        print("Invalid input")
        words = handle_user_input()

    words_in_pairs = words_to_pairs(words)
    
    if "TAKE" in words or "DROP" in words or "EXAMINE" in words or "USE" in words:
        #User wants to do something with an object
        if "TAKE" in words:
           
            print_string = """No such item to interact with
            
            """

        elif "DROP" in words:
            did_drop = False
            for key in game_data:
                if words[1].lower() == key and game_data[key] == True:
                    game_data[key] = False
                    print_string = "Dropped the " + key + "\n"
                    did_drop = True
                    break
            if not did_drop:
                return_string = """You don't have this object to drop
                
                """

        elif "EXAMINE" in words:
            
            print_string = """No such item to examine
            
            """

        elif "USE" in words:
            if "USE COLOGNE" in words_in_pairs and game_data["cologne"] == True:
                game_data["cologne"] = False
                print_string = """You used the cologne. You smell a bit better now.
                
                """

            else:
                print_string = """No such item to use
                
                """

    elif "TALK" in words or "ASK" in words:
        #User wants to interact with an NPC

        print_string = """No such person to interact with

        """

    elif "LOOK" in words:
        #User wants to LOOK
        print_string = """There's nothing in here but keyboards, pianos, and old percussion instruments.
        There's also some weird looking costumes that the drama club probably uses for props.
        Overall, not a good vibe...

        """
    elif "NORTH" in words or "EAST" in words or "SOUTH" in words or "WEST" in words:
        if "NORTH" in words:
            game_data["current_room"] = auditorium
        else:
            print_string = """You can't go that way
            
            """
    
    if print_string:
        for letter in print_string:
            sleep(0.01)
            sys.stdout.write(letter)
            sys.stdout.flush()


def handle_room_back_of_school(game_data, rooms, room_data):
    print_string = """It's the back of the school. You used to watch her as you pretended to talk to your friends.
    You start getting nostalgic feelings and start getting choked up.

    """

    for letter in print_string:
        sleep(0.01)
        sys.stdout.write(letter)
        sys.stdout.flush()
    print("\n")

    for key in room_data["back_of_school"]:
        if key == "visited" and room_data["back_of_school"][key] == False:
            room_data["back_of_school"][key] = True
            game_data["score"] += 10

    print_string = ""
    words = handle_user_input()
    while(not input_validity(words)):
        print("Invalid input")
        words = handle_user_input()

    words_in_pairs = words_to_pairs(words)
    
    if "TAKE" in words or "DROP" in words or "EXAMINE" in words or "USE" in words:
        #User wants to do something with an object
        if "TAKE" in words:
            
            print_string = """No such item to interact with
            
            """

        elif "DROP" in words:
            did_drop = False
            for key in game_data:
                if words[1].lower() == key and game_data[key] == True:
                    game_data[key] = False
                    print_string = "Dropped the " + key + "\n"
                    did_drop = True
                    break
            if not did_drop:
                return_string = """You don't have this object to drop
                
                """

        elif "EXAMINE" in words:

            print_string = """No such item to examine
            
            """

        elif "USE" in words:
            if "USE COLOGNE" in words_in_pairs and game_data["cologne"] == True:
                game_data["cologne"] = False
                print_string = """You used the cologne. You smell a bit better now.
                
                """
            
            else:
                print_string = """No such item to use
                
                """

    elif "TALK" in words or "ASK" in words:
        #User wants to interact with an NPC
        
        print_string = """No such person to interact with

        """

    elif "LOOK" in words:
        #User wants to LOOK
        print_string = """All you want to do is go forward as fast as possible to see her.

        """
    elif "NORTH" in words or "EAST" in words or "SOUTH" in words or "WEST" in words:
        if "NORTH" in words:
            game_data["current_room"] = bus_stop_2
        else:
            print_string = """You can't go that way
            
            """
    
    if print_string:
        for letter in print_string:
            sleep(0.01)
            sys.stdout.write(letter)
            sys.stdout.flush()


def handle_room_side_of_school(game_data, rooms, room_data):
    print_string = """The side of the school. She always waits for her bus with her friends here.
    Once again, it's stirring up slightly bittersweet memories of her so you try not to think about it.
    But it's nearly impossible.

    """

    for letter in print_string:
        sleep(0.01)
        sys.stdout.write(letter)
        sys.stdout.flush()
    print("\n")

    for key in room_data["side_of_school"]:
        if key == "visited" and room_data["side_of_school"][key] == False:
            room_data["side_of_school"][key] = True
            game_data["score"] += 10

    print_string = ""
    words = handle_user_input()
    while(not input_validity(words)):
        print("Invalid input")
        words = handle_user_input()

    words_in_pairs = words_to_pairs(words)
    
    if "TAKE" in words or "DROP" in words or "EXAMINE" in words or "USE" in words:
        #User wants to do something with an object
        if "TAKE" in words:
           
            print_string = """No such item to interact with
            
            """

        elif "DROP" in words:
            did_drop = False
            for key in game_data:
                if words[1].lower() == key and game_data[key] == True:
                    game_data[key] = False
                    print_string = "Dropped the " + key + "\n"
                    did_drop = True
                    break
            if not did_drop:
                return_string = """You don't have this object to drop
                
                """

        elif "EXAMINE" in words:
            
            print_string = """No such item to examine
            
            """

        elif "USE" in words:
            if "USE COLOGNE" in words_in_pairs and game_data["cologne"] == True:
                game_data["cologne"] = False
                print_string = """You used the cologne. You smell a bit better now.
                
                """
           
            else:
                print_string = """No such item to use
                
                """

    elif "TALK" in words or "ASK" in words:
        #User wants to interact with an NPC
        
        print_string = """No such person to interact with

        """

    elif "LOOK" in words:
        #User wants to LOOK
        print_string = """There's moss growing up the wall of the school. It's a sight for sore eyes.
        Not much to look at here except for the gravel pavement.
        You start to question the differences between a school and federal prison.

        """
    elif "NORTH" in words or "EAST" in words or "SOUTH" in words or "WEST" in words:
        if "WEST" in words:
            game_data["current_room"] = back_of_school
        else:
            print_string = """You can't go that way
            
            """
    
    if print_string:
        for letter in print_string:
            sleep(0.01)
            sys.stdout.write(letter)
            sys.stdout.flush()


def handle_room_bus_stop_2(game_data, rooms, room_data):
    print_string = """It's the bus stop for every student on their way home. The lot is empty right now.
    Kind of like your heart.

    """

    for letter in print_string:
        sleep(0.01)
        sys.stdout.write(letter)
        sys.stdout.flush()
    print("\n")

    for key in room_data["bus_stop_2"]:
        if key == "visited" and room_data["bus_stop_2"][key] == False:
            room_data["bus_stop_2"][key] = True
            game_data["score"] += 10

    print_string = ""
    words = handle_user_input()
    while(not input_validity(words)):
        print("Invalid input")
        words = handle_user_input()

    words_in_pairs = words_to_pairs(words)
    
    if "TAKE" in words or "DROP" in words or "EXAMINE" in words or "USE" in words:
        #User wants to do something with an object
        if "TAKE" in words:
            
            print_string = """No such item to interact with
            
            """

        elif "DROP" in words:
            did_drop = False
            for key in game_data:
                if words[1].lower() == key and game_data[key] == True:
                    game_data[key] = False
                    print_string = "Dropped the " + key + "\n"
                    did_drop = True
                    break
            if not did_drop:
                return_string = """You don't have this object to drop
                
                """

        elif "EXAMINE" in words:

            print_string = """No such item to examine
            
            """

        elif "USE" in words:
            if "USE COLOGNE" in words_in_pairs and game_data["cologne"] == True:
                game_data["cologne"] = False
                print_string = """You used the cologne. You smell a bit better now.
                
                """
            
            else:
                print_string = """No such item to use
                
                """

    elif "TALK" in words or "ASK" in words:
        #User wants to interact with an NPC
        
        print_string = """No such person to interact with

        """

    elif "LOOK" in words:
        #User wants to LOOK
        print_string = """There's no busses right now. You just have to keep trudging forward.

        """
    elif "NORTH" in words or "EAST" in words or "SOUTH" in words or "WEST" in words:
        if "NORTH" in words:
            game_data["current_room"] = crushs_street
        else:
            print_string = """You can't go that way
            
            """
    
    if print_string:
        for letter in print_string:
            sleep(0.01)
            sys.stdout.write(letter)
            sys.stdout.flush()


def handle_room_crushs_street(game_data, rooms, room_data):
    print_string = """It's her street.

    """

    for letter in print_string:
        sleep(0.01)
        sys.stdout.write(letter)
        sys.stdout.flush()
    print("\n")

    for key in room_data["crushs_street"]:
        if key == "visited" and room_data["crushs_street"][key] == False:
            room_data["crushs_street"][key] = True
            game_data["score"] += 10

    print_string = ""
    words = handle_user_input()
    while(not input_validity(words)):
        print("Invalid input")
        words = handle_user_input()

    words_in_pairs = words_to_pairs(words)
    
    if "TAKE" in words or "DROP" in words or "EXAMINE" in words or "USE" in words:
        #User wants to do something with an object
        if "TAKE" in words:
            
            print_string = """No such item to interact with
            
            """

        elif "DROP" in words:
            did_drop = False
            for key in game_data:
                if words[1].lower() == key and game_data[key] == True:
                    game_data[key] = False
                    print_string = "Dropped the " + key + "\n"
                    did_drop = True
                    break
            if not did_drop:
                return_string = """You don't have this object to drop
                
                """

        elif "EXAMINE" in words:

            print_string = """No such item to examine
            
            """

        elif "USE" in words:
            if "USE COLOGNE" in words_in_pairs and game_data["cologne"] == True:
                game_data["cologne"] = False
                print_string = """You used the cologne. You smell a bit better now.
                
                """
            
            else:
                print_string = """No such item to use
                
                """

    elif "TALK" in words or "ASK" in words:
        #User wants to interact with an NPC
        
        print_string = """No such person to interact with

        """

    elif "LOOK" in words:
        #User wants to LOOK
        print_string = """You don't want to do anything except see her, but you feel your legs locking up.

        """
    elif "NORTH" in words or "EAST" in words or "SOUTH" in words or "WEST" in words:
        if "NORTH" in words:
            game_data["current_room"] = crushs_house
        else:
            print_string = """You can't go that way
            
            """
    
    if print_string:
        for letter in print_string:
            sleep(0.01)
            sys.stdout.write(letter)
            sys.stdout.flush()


def handle_room_crushs_house(game_data, rooms, room_data):
    print_string = """You're at the steps of her house now.

    """

    for letter in print_string:
        sleep(0.01)
        sys.stdout.write(letter)
        sys.stdout.flush()
    print("\n")

    for key in room_data["crushs_house"]:
        if key == "visited" and room_data["crushs_house"][key] == False:
            room_data["crushs_house"][key] = True
            game_data["score"] += 10

    print_string = ""
    words = handle_user_input()
    while(not input_validity(words)):
        print("Invalid input")
        words = handle_user_input()

    words_in_pairs = words_to_pairs(words)
    
    if "TAKE" in words or "DROP" in words or "EXAMINE" in words or "USE" in words:
        #User wants to do something with an object
        if "TAKE" in words:
            
            print_string = """No such item to interact with
            
            """

        elif "DROP" in words:
            did_drop = False
            for key in game_data:
                if words[1].lower() == key and game_data[key] == True:
                    game_data[key] = False
                    print_string = "Dropped the " + key + "\n"
                    did_drop = True
                    break
            if not did_drop:
                return_string = """You don't have this object to drop
                
                """

        elif "EXAMINE" in words:

            print_string = """No such item to examine
            
            """

        elif "USE" in words:
            if "USE COLOGNE" in words_in_pairs and game_data["cologne"] == True:
                game_data["cologne"] = False
                print_string = """You used the cologne. You smell a bit better now.
                
                """
            
            else:
                print_string = """No such item to use
                
                """

    elif "TALK" in words or "ASK" in words:
        #User wants to interact with an NPC
        
        print_string = """No such person to interact with

        """

    elif "LOOK" in words:
        #User wants to LOOK
        print_string = """ *gulp*

        """
    elif "NORTH" in words or "EAST" in words or "SOUTH" in words or "WEST" in words:
        if "NORTH" in words:
            game_data["current_room"] = door_to_crushs_room
        else:
            print_string = """You can't go that way
            
            """
    
    if print_string:
        for letter in print_string:
            sleep(0.01)
            sys.stdout.write(letter)
            sys.stdout.flush()


def handle_room_door_to_crushs_room(game_data, rooms, room_data):
    print_string = """You are literally in front of her room door now.

    """

    for letter in print_string:
        sleep(0.01)
        sys.stdout.write(letter)
        sys.stdout.flush()
    print("\n")

    for key in room_data["door_to_crushs_room"]:
        if key == "visited" and room_data["door_to_crushs_room"][key] == False:
            room_data["door_to_crushs_room"][key] = True
            game_data["score"] += 10

    print_string = ""
    words = handle_user_input()
    while(not input_validity(words)):
        print("Invalid input")
        words = handle_user_input()

    words_in_pairs = words_to_pairs(words)
    
    if "TAKE" in words or "DROP" in words or "EXAMINE" in words or "USE" in words:
        #User wants to do something with an object
        if "TAKE" in words:
            
            print_string = """No such item to interact with
            
            """

        elif "DROP" in words:
            did_drop = False
            for key in game_data:
                if words[1].lower() == key and game_data[key] == True:
                    game_data[key] = False
                    print_string = "Dropped the " + key + "\n"
                    did_drop = True
                    break
            if not did_drop:
                return_string = """You don't have this object to drop
                
                """

        elif "EXAMINE" in words:

            print_string = """No such item to examine
            
            """

        elif "USE" in words:
            if "USE COLOGNE" in words_in_pairs and game_data["cologne"] == True:
                game_data["cologne"] = False
                print_string = """You used the cologne. You smell a bit better now.
                
                """
            
            else:
                print_string = """No such item to use
                
                """

    elif "TALK" in words or "ASK" in words:
        #User wants to interact with an NPC
        
        print_string = """No such person to interact with

        """

    elif "LOOK" in words:
        #User wants to LOOK
        print_string = """You're scared to see what's on the other side but you know you must.

        """
    elif "NORTH" in words or "EAST" in words or "SOUTH" in words or "WEST" in words:
        if "NORTH" in words:
            game_data["current_room"] = crushs_room
        else:
            print_string = """You can't go that way
            
            """
    
    if print_string:
        for letter in print_string:
            sleep(0.01)
            sys.stdout.write(letter)
            sys.stdout.flush()


def handle_room_crushs_room(game_data, rooms, room_data):
    print_string = """You can't believe your eyes. You want to die.
    She's with another guy. You weren't quick enough. You drop to your knees in tears.
    
    It's over now.

    """

    
    if print_string:
        for letter in print_string:
            sleep(0.01)
            sys.stdout.write(letter)
            sys.stdout.flush()

    sys.exit()


def handle_room(game_data, rooms, room_data):

    #1-10
    if game_data["current_room"] == your_room :
        handle_room_your_room(game_data, rooms, room_data)

    elif game_data["current_room"] == living_room :
        handle_room_living_room(game_data, rooms, room_data)

    elif game_data["current_room"] == kitchen :
        handle_room_kitchen(game_data, rooms, room_data)

    elif game_data["current_room"] == tv_room :
        handle_room_tv_room(game_data, rooms, room_data)

    elif game_data["current_room"] == backyard :
        handle_room_backyard(game_data, rooms, room_data)

    elif game_data["current_room"] == washroom :
        handle_room_washroom(game_data, rooms, room_data)

    elif game_data["current_room"] == dining_room :
        handle_room_dining_room(game_data, rooms, room_data)

    elif game_data["current_room"] == outside :
        handle_room_outside(game_data, rooms, room_data)

    elif game_data["current_room"] == garage :
        handle_room_garage(game_data, rooms, room_data)

    elif game_data["current_room"] == backyard :
        handle_room_backyard(game_data, rooms, room_data)


    #11-20
    elif game_data["current_room"] == bus_stop_1 :
        handle_room_bus_stop_1(game_data, rooms, room_data)

    elif game_data["current_room"] == garden :
        handle_room_garden(game_data, rooms, room_data)

    elif game_data["current_room"] == highschool :
        handle_room_highschool(game_data, rooms, room_data)

    elif game_data["current_room"] == music_room :
        handle_room_music_room(game_data, rooms, room_data)

    elif game_data["current_room"] == cafeteria :
        handle_room_cafeteria(game_data, rooms, room_data)

    elif game_data["current_room"] == library :
        handle_room_library(game_data, rooms, room_data)

    elif game_data["current_room"] == auditorium :
        handle_room_auditorium(game_data, rooms, room_data)

    elif game_data["current_room"] == storage_room :
        handle_room_storage_room(game_data, rooms, room_data)

    elif game_data["current_room"] == back_of_school :
        handle_room_back_of_school(game_data, rooms, room_data)

    elif game_data["current_room"] == side_of_school :
        handle_room_side_of_school(game_data, rooms, room_data)


    #21-25
    elif game_data["current_room"] == bus_stop_2 :
        handle_room_bus_stop_2(game_data, rooms, room_data)

    elif game_data["current_room"] == crushs_street :
        handle_room_crushs_street(game_data, rooms, room_data)

    elif game_data["current_room"] == crushs_house :
        handle_room_crushs_house(game_data, rooms, room_data)

    elif game_data["current_room"] == door_to_crushs_room :
        handle_room_door_to_crushs_room(game_data, rooms, room_data)
        
    elif game_data["current_room"] == crushs_room :
        handle_room_crushs_room(game_data, rooms, room_data)

    return


def display_intro_text():
    print_string = """ Welcome to this Text Adventure Game.\n\tDevelopment by Henry Zhangxiao.
    To play the game, type short commands into the command line.
    Typing \"take\", \"drop\", and \"examine\" allows you to interact with objects.
    You can also \"look\" at any time to learn more about the environment and setting you're currently in.
    You can use items by typing "use" followed by the item name in the command line (provided you can actually use it).
    There are non-player characters which you can interact with using \"talk\" and "ask".
    You will move around using the commands \"north\", \"east\", \"south\", \"west\"."""

    for letter in print_string:
        sleep(0.01)
        sys.stdout.write(letter)
        sys.stdout.flush()


def output_score(game_data):
    print_string = "Current Score: " + str(game_data["score"]) + "\n"

    for letter in print_string:
        sleep(0.01)
        sys.stdout.write(letter)
        sys.stdout.flush()


def main():
    ''' Main function of script - calls all central functions above via a Game Loop code structure.
    Input: None
    Output: None
    '''
    # Initialize Data
    game_data = initialize_game_data()
    rooms = initialize_rooms()
    room_data = initialize_room_data()
    display_intro_text()
    print("\n")
    ready_to_play = input("If you're ready, type \"yes\": ")
    ready_to_play = ready_to_play.upper().strip().split()
    while("YES" not in ready_to_play):
        ready_to_play = input("If you're ready, type \"yes\": ")
        ready_to_play = ready_to_play.upper().strip().split()

    # Begin Central Game Loop
    while not game_data["game_over"]:
        output_score(game_data)
        handle_room(game_data, rooms, room_data)
        
        #update(game_data)
        #render(game_data)
        
    # Exit Pygame and Python
    sys.exit()


if __name__ == "__main__":
    main()