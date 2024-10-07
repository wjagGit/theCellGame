#______________________________________________________________________
# Static Data For database creation

# Structure(Name, Class, Ability, Alignment, Quality)
characters = (
    ("Asema", "Magic", "Phase", "Chaos", "Legendary"),
    ("Valentine", "Rogue", "Illusion", "Chaos", "Legendary"),
    ("Bran The Brave", "Fighter", "Resolve", "Balance", "Legendary"),
    ("Nip Legbeard", "Rogue", "Leap", "Balance", "Legendary"),
    ("Stout", "Magic", "Repair", "Order", "Legendary"),
    ("Elissa", "Music", "Piercing Note", "Order", "Legendary"),
    ("Thorme", "Fighter", "Smash", "Chaos", "Epic"),
    ("Lucy", "Music", "Lullaby", "Chaos", "Common"),
    ("Terin", "Music", "Rally", "Balance", "Epic"),
    ("Erin", "Magic", "Heal", "Balance", "Common"),
    ("Felix", "Fighter", "Petrify", "Order", "Common"),
    ("Bu", "Rogue", "Cut", "Order", "Epic")
)

# Structure(Item Name, Item Description)
items = (
    ("Cell Key", "Unlocks cell door"),
    ("Valve handle", "Repairs valve in factory")
)

# Structure(Enounter Name, Gold Reward)
encounters = (
    ("Dungeon", 75),
    ("Camp", 150),
    ("Factory", 225),
    ("Ship", 350),
    ("Town", 0),
    ("Depths", 1000),
    ("Cultists", 50),
    ("Zelots", 50),
    ("Vigilanties", 50),
    ("Beasts", 25),
    ("Depth Trawlers", 200),
    ("Empty", 0)
)

worldmap = (
    (1,1,11, 'x'), (1,2,0, 'x'), (1,3,11, 'x'), (1,4,11, 'x'), (1,5,11, 'x'),
    (2,1,6, 'x'), (2,2,11, 'x'), (2,3,11, 'x'), (2,4,7, 'x'), (2,5,2, 'x'),
    (3,1,11, 'x'), (3,2,11, 'x'), (3,3,1, 'x'), (3,4,8, 'x'), (3,5,11, 'x'),
    (4,1,9, 'x'), (4,2,9, 'x'), (4,3,11, 'x'), (4,4,11, 'x'), (4,5,11, 'x'),
    (5,1,3, 'x'), (5,2,11, 'x'), (5,3,11, 'x'), (5,4,11, 'x'), (5,5,11, 'x'),
    (6,1,4, 'x'), (6,2,11, 'x'), (6,3,11, 'x'),
    (7,1,10, 'x'), (7,2,11, 'x'),
    (8,1,5, 'x'),
)