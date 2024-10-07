#______________________________________________________________________
# IMPORTS
from CellGameFunctions import *
from theCellGameLevels import *

#______________________________________________________________________
# Main

if database_is_empty():
    db_creation()

#Main Menu
while True:
    print("The Cell Game")
    print("--------------")
    print("1. Continue")
    print("2. New Game")
    print("3. Exit")
    Selection = int(input(": "))

    match Selection:
        case 1:
            # Check if there is a save file already
            if not savefile_exists():
                new_game()
            break

        case 2:
            # Print warning and confirmation
            if not savefile_exists():
                new_game()
                break
            else:
                print("Are you sure you want to delete your save? Once deleted the data cannot be recovered.")
                if(input("Enter \"Yes\" to continue: ").strip().lower() == "yes"):
                    new_game()
                    break
                else:
                    print("New game cancelled.")
                    continue
        case 3:
            exit()
        case _:
            print("Invalid input, please try again.")

# Load Gamestate
# return array of gold, items list, and user location
user_state = load_gamestate()
user_name = user_state[0]
session_gold = user_state[1]
session_Xlocation = user_state[2]
session_Ylocation = user_state[3]

playing = True
while playing:
    # Read current encounter into variable using user location
    currentTileEncounter = get_current_tile_encounter(session_Xlocation, session_Ylocation)
    # options menu for "Enter location", "Save", and "exit game"
    print("--------------")
    print(currentTileEncounter)
    print("--------------")
    print("1. Enter Location")
    print("2. Save Game")
    print("3. Exit Game")
    Selection = int(input(": "))
    
    match Selection:
        case 1:
            print("Entering Location")
        case 2:
            save_game(user_name, session_gold, session_Xlocation, session_Ylocation)
        case 3:
            exit()
        case _:
            print("Invalid input, please try again.")

    match currentTileEncounter:
        case "Dungeon":
            DungeonTile()
        case "Camp":
            CampTile()
        case "Factory":
            FactoryTile()
        case "Ship":
            ShipTile()
        case "Town":
            TownTile()
        case "Depths":
            DepthsTile()
        case "Cultists":
            CultistsTile()
        case "Zelots":
            ZelotsTile()
        case "Vigilanties":
            VigilantiesTile()
        case "Beasts":
            BeastsTile()
        case "Depth Trawlers":
            DepthTrawlersTile()
        case "Empty":
            EmptyTile
        case _:
            break

    worldMap(session_Xlocation, session_Ylocation)
    moveTile(session_Xlocation, session_Ylocation)
    # save new coordinates for the player

#______________________________________________________________________