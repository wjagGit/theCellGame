from CellGameDBConnect import cursor, conn
from CellGameData import characters, items, encounters, worldmap


# GENERAL FUNCTIONS
# ======================================================================================
def ValidInput(input):
    if input == "" or not input.isalnum() or len(input) <4 or len(input) >16:
        return False
    else:
        return True
    
# GAME FUNCTIONS
#=======================================================================================

def load_gamestate():
    cursor.execute("SELECT Name, Gold, Xlocation, Ylocation FROM User")
    return cursor.fetchone()

def reset_savefile():
    cursor.execute("DELETE FROM Users")

    conn.commit()

def savefile_exists():
    cursor.execute("SELECT COUNT(*) FROM User")
    row_count = cursor.fetchone()[0]
    if row_count == 0:
        return False
    else:
        return True

def new_game():

    cursor.execute("SELECT COUNT(*) FROM User")
    row_count = cursor.fetchone()[0]
    if savefile_exists():
        reset_savefile()

    characterName = ""
    while not ValidInput(characterName):
        characterName = input("Please enter a valid character name: ")

    cursor.execute('''
        INSERT INTO User (Name, Gold, Xlocation, Ylocation) 
        VALUES (?, 10, 3, 3)
        ''', (characterName,))
    
    conn.commit()

def user_has_item(itemToCheck):
    cursor.execute("SELECT * FROM Items WHERE ItemName = ? AND UserOwns = 1", itemToCheck)
    result = cursor.fetchone()
    if result is None:
        return False
    else:
        return True
    
def get_current_tile_encounter(xlocation, ylocation):
    cursor.execute('''
    SELECT * FROM MapTiles WHERE xlocation = ? AND ylocation = ?
    ''', (xlocation, ylocation)
    )

    encounterID = cursor.fetchone()[2]

    cursor.execute("SELECT EncounterName FROM Encounters WHERE EncounterID = ?", (encounterID,))

    return cursor.fetchone()[0]

def save_game(user_name, session_gold, session_Xlocation, session_Ylocation):
    cursor.execute('''
        Update User
        SET Gold = ?, Xlocation = ?, Ylocation = ? 
        WHERE Name = ?
        ''', (session_gold, session_Xlocation, session_Ylocation, user_name))
    
    conn.commit()

# DISPLAY GRID OF ICONS INDICATING WORLDMAP WITH flashing to indicate current location
def worldMap(session_Xlocation, session_Ylocation):

    # CREATING DYNAMIC LINES
    mapLines = [
        "	2  |  ",
        "   	3  |    ",
        "   	4  |  ",
        "   	5  |  ",
        "   	6  |    ",
        "   	7  |     ",
        "   	8  |    ",
        "   	9  |      "
    ]

    for i in range(8):
        cursor.execute("SELECT * FROM MAPTILES WHERE XLOCATION = ?", (i + 1,))
        holder = cursor.fetchall()

        for r in range(len(holder)):
            if holder[r][0] == session_Xlocation and holder[r][1] == session_Ylocation:
                mapLines[i] += "O "
            if holder[r][3] == 0:
                mapLines[i] += holder[r][4] + " "
            else:
                mapLines[i] += "? "

    # ADDING HEADING CONTENT
    mapLines[0] += "   |"
    mapLines[1] += " |  1. Left"
    mapLines[2] += " |  2. Right"
    mapLines[3] += "   |  3. Up"
    mapLines[4] += " |  4. Down"
    mapLines[5] += "    |"
    mapLines[6] += (f"       | Current Location {session_Xlocation}, {session_Ylocation}")
    mapLines[7] += "       |"

    #PRINTING CONTENT
    # Static Head
    print("""
                CRAKKITA MAP

            A B C D E F G H
            _______________
        1  |               |  Choose a direction of travel
    """, end= "")

    # Dynamic Middle
    for line in mapLines:
        print(line)

    # Static Footer
    print("	10 |_______________|")

def moveTile(session_Xlocation, session_Ylocation):
    print("TODO")


# DATABASE FUNCTIONS
#=======================================================================================

def create_theCellGame_tables():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS User (
        UserID INTEGER PRIMARY KEY AUTOINCREMENT,
        Name TEXT NOT NULL UNIQUE,
        Gold INTEGER NOT NULL,
        Xlocation INTEGER NOT NULL,
        Ylocation INTEGER NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Characters (
        CharacterID INTEGER PRIMARY KEY AUTOINCREMENT,
        CharacterName TEXT NOT NULL UNIQUE,
        CharacterClass TEXT NOT NULL,
        CharacterAbility TEXT NOT NULL,
        CharacterFaction TEXT NOT NULL,
        CharacterRarity TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Items (
        ItemID INTEGER PRIMARY KEY AUTOINCREMENT,
        ItemName TEXT NOT NULL UNIQUE,
        ItemEffect TEXT NOT NULL,
        UserOwns INTEGER DEFAULT 0 NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Backpack (
        PackSpaceID INTEGER PRIMARY KEY AUTOINCREMENT,
        BackpackItemID INTEGER NOT NULL,
        FOREIGN KEY (BackpackItemID) REFERENCES Items(ItemID)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Encounters (
        EncounterID INTEGER PRIMARY KEY AUTOINCREMENT,
        EncounterName TEXT NOT NULL UNIQUE,
        EncounterReward INTEGER NOT NULL
        )
    ''')


    cursor.execute('''
        CREATE TABLE IF NOT EXISTS MapTiles (
        xlocation INTEGER NOT NULL,
        ylocation INTEGER NOT NULL,
        MapEncounterID INTEGER NOT NULL,
        tileVisited INTEGER DEFAULT 0,
        tileCharacter char NOT NULL,
        PRIMARY KEY (xlocation, ylocation),
        FOREIGN KEY (MapEncounterID) REFERENCES Encounters(EncounterID)
        )
    ''')

    conn.commit()

def insert_static_database_values():
    cursor.executemany('''
        INSERT OR IGNORE INTO Characters (CharacterName, CharacterClass, CharacterAbility, CharacterFaction, CharacterRarity)
        VALUES (?,?,?,?,?)
    ''', characters)

    cursor.executemany('''
        INSERT OR IGNORE INTO Items (ItemName, ItemEffect)
        VALUES (?, ?)
    ''', items)

    cursor.executemany('''
        INSERT OR IGNORE INTO Encounters (EncounterName, EncounterReward)
        VALUES (?, ?)
    ''', encounters)

    cursor.executemany('''
        INSERT OR IGNORE INTO MapTiles (xlocation, ylocation, MapEncounterID, tileCharacter)
        VALUES (?, ?, ?, ?)
    ''', worldmap)

    conn.commit()

def database_is_empty():
    cursor.execute('''
        SELECT count(name) FROM sqlite_master WHERE type='table' AND name='Users'
    ''')
    if cursor.fetchone()[0] == 0:
        return True
    return False

def db_creation():
    create_theCellGame_tables()
    insert_static_database_values()
    conn.commit()