# useful for autotracker and in-game tracking
areaAccessPoints = {
    "Lower Mushrooms Left": {"byteIndex": 166, "bitMask": 1, "room": 0x9969, "area": "Crateria"},
    "Green Pirates Shaft Bottom Right": {"byteIndex": 166, "bitMask": 16, "room": 0x99bd, "area": "Crateria"},
    "Moat Right": {"byteIndex": 23, "bitMask": 64, "room": 0x95ff, "area": "Crateria"},
    "Keyhunter Room Bottom": {"byteIndex": 31, "bitMask": 8, "room": 0x948c, "area": "Crateria"},
    "Morph Ball Room Left": {"byteIndex": 173, "bitMask": 32, "room": 0x9e9f, "area": "Brinstar"},
    "Green Brinstar Elevator": {"byteIndex": 167, "bitMask": 128, "room": 0x9938, "area": "Crateria"},
    "Green Hill Zone Top Right": {"byteIndex": 173, "bitMask": 16, "room": 0x9e52, "area": "Brinstar"},
    "Noob Bridge Right": {"byteIndex": 59, "bitMask": 1, "room": 0x9fba, "area": "Brinstar"},
    "West Ocean Left": {"byteIndex": 23, "bitMask": 128, "room": 0x93fe, "area": "Crateria"},
    "Crab Maze Left": {"byteIndex": 41, "bitMask": 64, "room": 0x957d, "area": "Crateria"},
    "Lava Dive Right": {"byteIndex": 172, "bitMask": 4, "room": 0xaf14, "area": "Norfair"},
    "Three Muskateers Room Left": {"byteIndex": 144, "bitMask": 128, "room": 0xb656, "area": "Norfair"},
    "Warehouse Zeela Room Left": {"byteIndex": 78, "bitMask": 16, "room": 0xa471, "area": "Brinstar"},
    "Warehouse Entrance Left": {"byteIndex": 78, "bitMask": 2, "room": 0xa6a1, "area": "Brinstar"},
    "Warehouse Entrance Right": {"byteIndex": 78, "bitMask": 8, "room": 0xa6a1, "area": "Brinstar"},
    "Single Chamber Top Right": {"byteIndex": 144, "bitMask": 64, "room": 0xad5e, "area": "Norfair"},
    "Kronic Boost Room Bottom Left": {"byteIndex": 172, "bitMask": 8, "room": 0xae74, "area": "Norfair"},
    "Crocomire Speedway Bottom": {"byteIndex": 169, "bitMask": 1, "room": 0xa923, "area": "Norfair"},
    # required a fix from actual ingame position as room is not a mirror from vanilla
    "Crocomire Room Top": {"byteIndex": 173, "bitMask": 1, "room": 0xa98d, "area": "Norfair"},
    "Main Street Bottom": {"byteIndex": 198, "bitMask": 1, "room": 0xcfc9, "area": "Maridia"},
    "Crab Hole Bottom Left": {"byteIndex": 202, "bitMask": 32, "room": 0xd21c, "area": "Maridia"},
    "Red Fish Room Left": {"byteIndex": 162, "bitMask": 2, "room": 0xd104, "area": "Maridia"},
    "Crab Shaft Right": {"byteIndex": 173, "bitMask": 1, "room": 0xd1a3, "area": "Maridia"},
    "Aqueduct Top Left": {"byteIndex": 173, "bitMask": 2, "room": 0xd5a7, "area": "Maridia"},
    "Le Coude Right": {"byteIndex": 41, "bitMask": 32, "room": 0x95a8, "area": "Crateria"},
    "Red Tower Top Left": {"byteIndex": 59, "bitMask": 2, "room": 0xa253, "area": "Brinstar"},
    "Caterpillar Room Top Right": {"byteIndex": 35, "bitMask": 128, "room": 0xa322, "area": "Brinstar"},
    "Red Brinstar Elevator": {"byteIndex": 35, "bitMask": 8, "room": 0x962a, "area": "Crateria"},
    "East Tunnel Right": {"byteIndex": 206, "bitMask": 2, "room": 0xcf80, "area": "Maridia"},
    "East Tunnel Top Right": {"byteIndex": 202, "bitMask": 16, "room": 0xcf80, "area": "Maridia"},
    "Glass Tunnel Top": {"byteIndex": 202, "bitMask": 1, "room": 0xcefb, "area": "Maridia"},
    "Golden Four": {"byteIndex": 166, "bitMask": 32, "room": 0xa5ed, "area": "Crateria"}
}

# additional info for in-game tracker for "top of elevator" APs to show on a more intuitive map
areaAccessPointsInGameDisplay = {
    "Green Brinstar Elevator": {"area": "Brinstar", "coords": (54, 1)},
    "Red Brinstar Elevator": {"area": "Brinstar", "coords": (26, 4)},
    "Le Coude Right": {"area": "Maridia", "coords": (32, 1)},
    "Warehouse Entrance Left": {"area": "Norfair", "coords": (53, 1)},
    "Warehouse Entrance Right": {"area": "Norfair", "coords": (51, 1)}
}

bossAccessPoints = {
    "PhantoonRoomOut": {"byteIndex": 208, "bitMask": 8, "room": 0xcc6f, "area": "WreckedShip"},
    "PhantoonRoomIn": {"byteIndex": 208, "bitMask": 16, "room": 0xcd13, "area": "WreckedShip"},
    "RidleyRoomOut": {"byteIndex": 196, "bitMask": 2, "room": 0xb37a, "area": "Norfair"},
    "RidleyRoomIn": {"byteIndex": 196, "bitMask": 1, "room": 0xb32e, "area": "Norfair"},
    "KraidRoomOut": {"byteIndex": 81, "bitMask": 64, "room": 0xa56b, "area": "Brinstar"},
    "KraidRoomIn": {"byteIndex": 81, "bitMask": 128, "room": 0xa59f, "area": "Brinstar"},
    "DraygonRoomOut": {"byteIndex": 43, "bitMask": 64, "room": 0xd78f, "area": "Maridia"},
    "DraygonRoomIn": {"byteIndex": 43, "bitMask": 32, "room": 0xda60, "area": "Maridia"}
}

escapeAccessPoints = {
    "Tourian Escape Room 4 Top Right": {"byteIndex": 201, "bitMask": 16, "room": 0xdede, "area": "Tourian"},
    "Climb Bottom Left": {"byteIndex": 201, "bitMask": 8, "room": 0x96ba, "area": "Crateria"},
    "Green Brinstar Main Shaft Top Left": {"byteIndex": 150, "bitMask": 2, "room": 0x9ad9, "area": "Brinstar"},
    "Basement Left": {"byteIndex": 209, "bitMask": 128, "room": 0xcc6f, "area": "WreckedShip"},
    "Business Center Mid Left": {"byteIndex": 150, "bitMask": 8, "room": 0xa7de, "area": "Norfair"},
    "Crab Hole Bottom Right": {"byteIndex": 202, "bitMask": 32, "room": 0xd21c, "area": "Maridia"}
}

itemLocations = {
    "Power Bomb (Crateria surface)": {"byteIndex": 11, "bitMask": 4, "room": 0x93aa, "area": "Crateria"},
    "Missile (outside Wrecked Ship bottom)": {"byteIndex": 27, "bitMask": 128, "room": 0x93fe, "area": "Crateria"},
    "Missile (outside Wrecked Ship top)": {"byteIndex": 6, "bitMask": 1, "room": 0x93fe, "area": "Crateria"},
    "Missile (outside Wrecked Ship middle)": {"byteIndex": 15, "bitMask": 128, "room": 0x93fe, "area": "Crateria"},
    "Missile (Crateria moat)": {"byteIndex": 23, "bitMask": 32, "room": 0x95ff, "area": "Crateria"},
    "Energy Tank, Gauntlet": {"byteIndex": 141, "bitMask": 4, "room": 0x965b, "area": "Crateria"},
    "Missile (Crateria bottom)": {"byteIndex": 205, "bitMask": 32, "room": 0x975c, "area": "Crateria"},
    "Bomb": {"byteIndex": 156, "bitMask": 4, "room": 0x9804, "area": "Crateria"},
    "Energy Tank, Terminator": {"byteIndex": 158, "bitMask": 32, "room": 0x990d, "area": "Crateria"},
    "Missile (Crateria gauntlet right)": {"byteIndex": 146, "bitMask": 16, "room": 0x99bd, "area": "Crateria"},
    "Missile (Crateria gauntlet left)": {"byteIndex": 146, "bitMask": 16, "room": 0x99bd, "area": "Crateria"},
    "Super Missile (Crateria)": {"byteIndex": 168, "bitMask": 2, "room": 0x99f9, "area": "Crateria"},
    "Missile (Crateria middle)": {"byteIndex": 161, "bitMask": 2, "room": 0x9a90, "area": "Crateria"},
    "Power Bomb (green Brinstar bottom)": {"byteIndex": 162, "bitMask": 16, "room": 0x9ad9, "area": "Brinstar"},
    "Super Missile (pink Brinstar)": {"byteIndex": 168, "bitMask": 1, "room": 0x9b5b, "area": "Brinstar"},
    "Missile (green Brinstar below super missile)": {"byteIndex": 150, "bitMask": 8, "room": 0x9bc8, "area": "Brinstar"},
    "Super Missile (green Brinstar top)": {"byteIndex": 146, "bitMask": 4, "room": 0x9bc8, "area": "Brinstar"},
    "Reserve Tank, Brinstar": {"byteIndex": 150, "bitMask": 32, "room": 0x9c07, "area": "Brinstar"},
    "Missile (green Brinstar behind missile)": {"byteIndex": 150, "bitMask": 64, "room": 0x9c07, "area": "Brinstar"},
    "Missile (green Brinstar behind reserve tank)": {"byteIndex": 150, "bitMask": 64, "room": 0x9c07, "area": "Brinstar"},
    "Missile (pink Brinstar top)": {"byteIndex": 161, "bitMask": 2, "room": 0x9d19, "area": "Brinstar"},
    "Missile (pink Brinstar bottom)": {"byteIndex": 173, "bitMask": 2, "room": 0x9d19, "area": "Brinstar"},
    "Charge Beam": {"byteIndex": 177, "bitMask": 2, "room": 0x9d19, "area": "Brinstar"},
    "Power Bomb (pink Brinstar)": {"byteIndex": 166, "bitMask": 128, "room": 0x9e11, "area": "Brinstar"},
    "Missile (green Brinstar pipe)": {"byteIndex": 177, "bitMask": 64, "room": 0x9e52, "area": "Brinstar"},
    "Morphing Ball": {"byteIndex": 172, "bitMask": 2, "room": 0x9e9f, "area": "Brinstar"},
    "Power Bomb (blue Brinstar)": {"byteIndex": 173, "bitMask": 128, "room": 0x9e9f, "area": "Brinstar"},
    "Missile (blue Brinstar middle)": {"byteIndex": 47, "bitMask": 1, "room": 0x9f64, "area": "Brinstar"},
    "Energy Tank, Brinstar Ceiling": {"byteIndex": 172, "bitMask": 128, "room": 0x9f64, "area": "Brinstar"},
    "Energy Tank, Etecoons": {"byteIndex": 175, "bitMask": 64, "room": 0xa011, "area": "Brinstar"},
    "Super Missile (green Brinstar bottom)": {"byteIndex": 175, "bitMask": 32, "room": 0xa051, "area": "Brinstar"},
    "Energy Tank, Waterway": {"byteIndex": 186, "bitMask": 1, "room": 0xa0d2, "area": "Brinstar"},
    "Missile (blue Brinstar bottom)": {"byteIndex": 176, "bitMask": 16, "room": 0xa107, "area": "Brinstar"},
    "Energy Tank, Brinstar Gate": {"byteIndex": 165, "bitMask": 32, "room": 0xa15b, "area": "Brinstar"},
    "Missile (blue Brinstar top)": {"byteIndex": 164, "bitMask": 32, "room": 0xa1d8, "area": "Brinstar"},
    "Missile (blue Brinstar behind missile)": {"byteIndex": 164, "bitMask": 32, "room": 0xa1d8, "area": "Brinstar"},
    "X-Ray Scope": {"byteIndex": 193, "bitMask": 128, "room": 0xa2ce, "area": "Brinstar"},
    "Power Bomb (red Brinstar sidehopper room)": {"byteIndex": 39, "bitMask": 8, "room": 0xa37c, "area": "Brinstar"},
    "Power Bomb (red Brinstar spike room)": {"byteIndex": 51, "bitMask": 8, "room": 0xa3ae, "area": "Brinstar"},
    "Missile (red Brinstar spike room)": {"byteIndex": 51, "bitMask": 4, "room": 0xa3ae, "area": "Brinstar"},
    "Spazer": {"byteIndex": 75, "bitMask": 64, "room": 0xa447, "area": "Brinstar"},
    "Energy Tank, Kraid": {"byteIndex": 82, "bitMask": 8, "room": 0xa4b1, "area": "Brinstar"},
    "Missile (Kraid)": {"byteIndex": 78, "bitMask": 128, "room": 0xa4da, "area": "Brinstar"},
    "Varia Suit": {"byteIndex": 80, "bitMask": 2, "room": 0xa6e2, "area": "Brinstar"},
    "Missile (lava room)": {"byteIndex": 149, "bitMask": 2, "room": 0xa788, "area": "Norfair"},
    "Ice Beam": {"byteIndex": 143, "bitMask": 64, "room": 0xa890, "area": "Norfair"},
    "Missile (below Ice Beam)": {"byteIndex": 151, "bitMask": 8, "room": 0xa8f8, "area": "Norfair"},
    "Energy Tank, Crocomire": {"byteIndex": 173, "bitMask": 8, "room": 0xa98d, "area": "Norfair"},
    "Hi-Jump Boots": {"byteIndex": 158, "bitMask": 1, "room": 0xa9e5, "area": "Norfair"},
    "Missile (above Crocomire)": {"byteIndex": 158, "bitMask": 16, "room": 0xaa0e, "area": "Norfair"},
    "Missile (Hi-Jump Boots)": {"byteIndex": 154, "bitMask": 2, "room": 0xaa41, "area": "Norfair"},
    "Energy Tank (Hi-Jump Boots)": {"byteIndex": 154, "bitMask": 4, "room": 0xaa41, "area": "Norfair"},
    "Power Bomb (Crocomire)": {"byteIndex": 174, "bitMask": 2, "room": 0xaade, "area": "Norfair"},
    "Missile (below Crocomire)": {"byteIndex": 194, "bitMask": 64, "room": 0xab3b, "area": "Norfair"},
    "Missile (Grapple Beam)": {"byteIndex": 194, "bitMask": 1, "room": 0xab8f, "area": "Norfair"},
    "Grapple Beam": {"byteIndex": 199, "bitMask": 8, "room": 0xac2b, "area": "Norfair"},
    "Reserve Tank, Norfair": {"byteIndex": 141, "bitMask": 8, "room": 0xac5a, "area": "Norfair"},
    "Missile (Norfair Reserve Tank)": {"byteIndex": 141, "bitMask": 8, "room": 0xac5a, "area": "Norfair"},
    "Missile (bubble Norfair green door)": {"byteIndex": 141, "bitMask": 64, "room": 0xac83, "area": "Norfair"},
    "Missile (bubble Norfair)": {"byteIndex": 152, "bitMask": 1, "room": 0xacb3, "area": "Norfair"},
    "Missile (Speed Booster)": {"byteIndex": 15, "bitMask": 32, "room": 0xacf0, "area": "Norfair"},
    "Speed Booster": {"byteIndex": 15, "bitMask": 64, "room": 0xad1b, "area": "Norfair"},
    "Missile (Wave Beam)": {"byteIndex": 148, "bitMask": 8, "room": 0xadad, "area": "Norfair"},
    "Wave Beam": {"byteIndex": 148, "bitMask": 64, "room": 0xadde, "area": "Norfair"},
    "Missile (Gold Torizo)": {"byteIndex": 193, "bitMask": 8, "room": 0xb283, "area": "Norfair"},
    "Super Missile (Gold Torizo)": {"byteIndex": 193, "bitMask": 16, "room": 0xb283, "area": "Norfair"},
    "Missile (Mickey Mouse room)": {"byteIndex": 172, "bitMask": 32, "room": 0xb40a, "area": "Norfair"},
    "Missile (lower Norfair above fire flea room)": {"byteIndex": 27, "bitMask": 16, "room": 0xb510, "area": "Norfair"},
    "Power Bomb (lower Norfair above fire flea room)": {"byteIndex": 31, "bitMask": 64, "room": 0xb55a, "area": "Norfair"},
    "Power Bomb (Power Bombs of shame)": {"byteIndex": 63, "bitMask": 2, "room": 0xb5d5, "area": "Norfair"},
    "Missile (lower Norfair near Wave Beam)": {"byteIndex": 152, "bitMask": 64, "room": 0xb656, "area": "Norfair"},
    "Energy Tank, Ridley": {"byteIndex": 201, "bitMask": 128, "room": 0xb698, "area": "Norfair"},
    "Screw Attack": {"byteIndex": 197, "bitMask": 32, "room": 0xb6c1, "area": "Norfair"},
    "Energy Tank, Firefleas": {"byteIndex": 51, "bitMask": 64, "room": 0xb6ee, "area": "Norfair"},
    "Reserve Tank, Wrecked Ship": {"byteIndex": 176, "bitMask": 1, "room": 0xc98e, "area": "WreckedShip"},
    "Missile (Gravity Suit)": {"byteIndex": 185, "bitMask": 64, "room": 0xc98e, "area": "WreckedShip"},
    "Missile (Wrecked Ship top)": {"byteIndex": 172, "bitMask": 64, "room": 0xcaae, "area": "WreckedShip"},
    "Missile (Wrecked Ship middle)": {"byteIndex": 197, "bitMask": 32, "room": 0xcaf6, "area": "WreckedShip"},
    "Energy Tank, Wrecked Ship": {"byteIndex": 184, "bitMask": 8, "room": 0xcc27, "area": "WreckedShip"},
    "Super Missile (Wrecked Ship left)": {"byteIndex": 200, "bitMask": 1, "room": 0xcda8, "area": "WreckedShip"},
    "Right Super, Wrecked Ship": {"byteIndex": 200, "bitMask": 64, "room": 0xcdf1, "area": "WreckedShip"},
    "Gravity Suit": {"byteIndex": 185, "bitMask": 8, "room": 0xce40, "area": "WreckedShip"},
    "Missile (green Maridia shinespark)": {"byteIndex": 183, "bitMask": 128, "room": 0xcfc9, "area": "Maridia"},
    "Super Missile (green Maridia)": {"byteIndex": 178, "bitMask": 1, "room": 0xcfc9, "area": "Maridia"},
    "Energy Tank, Mama turtle": {"byteIndex": 182, "bitMask": 128, "room": 0xd055, "area": "Maridia"},
    "Missile (green Maridia tatori)": {"byteIndex": 185, "bitMask": 1, "room": 0xd055, "area": "Maridia"},
    "Super Missile (yellow Maridia)": {"byteIndex": 158, "bitMask": 2, "room": 0xd13b, "area": "Maridia"},
    "Missile (yellow Maridia super missile)": {"byteIndex": 158, "bitMask": 2, "room": 0xd13b, "area": "Maridia"},
    "Missile (yellow Maridia false wall)": {"byteIndex": 157, "bitMask": 2, "room": 0xd1dd, "area": "Maridia"},
    "Plasma Beam": {"byteIndex": 140, "bitMask": 2, "room": 0xd2aa, "area": "Maridia"},
    "Missile (left Maridia sand pit room)": {"byteIndex": 189, "bitMask": 2, "room": 0xd4ef, "area": "Maridia"},
    "Reserve Tank, Maridia": {"byteIndex": 189, "bitMask": 2, "room": 0xd4ef, "area": "Maridia"},
    "Missile (right Maridia sand pit room)": {"byteIndex": 189, "bitMask": 16, "room": 0xd51e, "area": "Maridia"},
    "Power Bomb (right Maridia sand pit room)": {"byteIndex": 193, "bitMask": 32, "room": 0xd51e, "area": "Maridia"},
    "Missile (pink Maridia)": {"byteIndex": 169, "bitMask": 32, "room": 0xd5a7, "area": "Maridia"},
    "Super Missile (pink Maridia)": {"byteIndex": 169, "bitMask": 64, "room": 0xd5a7, "area": "Maridia"},
    "Spring Ball": {"byteIndex": 196, "bitMask": 64, "room": 0xd6d0, "area": "Maridia"},
    "Missile (Draygon)": {"byteIndex": 35, "bitMask": 128, "room": 0xd78f, "area": "Maridia"},
    "Energy Tank, Botwoon": {"byteIndex": 164, "bitMask": 4, "room": 0xd7e4, "area": "Maridia"},
    "Space Jump": {"byteIndex": 47, "bitMask": 8, "room": 0xd9aa, "area": "Maridia"}
}

doors = {
    "LandingSiteRight": {"byteIndex": 23, "bitMask": 1, "room": 0x91f8, "area": "Crateria"},
    "LandingSiteTopRight": {"byteIndex": 11, "bitMask": 1, "room": 0x91f8, "area": "Crateria"},
    "WestOceanRight": {"byteIndex": 22, "bitMask": 64, "room": 0x93fe, "area": "Crateria"},
    "KihunterRight": {"byteIndex": 23, "bitMask": 16, "room": 0x948c, "area": "Crateria"},
    "KihunterBottom": {"byteIndex": 31, "bitMask": 8, "room": 0x948c, "area": "Crateria"},
    "LeCoudeBottom": {"byteIndex": 41, "bitMask": 32, "room": 0x95a8, "area": "Crateria"},
    "RedBrinstarElevatorTop": {"byteIndex": 35, "bitMask": 8, "room": 0x962a, "area": "Crateria"},
    "ClimbRight": {"byteIndex": 197, "bitMask": 32, "room": 0x96ba, "area": "Crateria"},
    "FlywayRight": {"byteIndex": 156, "bitMask": 2, "room": 0x9879, "area": "Crateria"},
    "GreenPiratesShaftBottomRight": {"byteIndex": 166, "bitMask": 16, "room": 0x99bd, "area": "Crateria"},
    "GreenBrinstarSaveStation": {"byteIndex": 154, "bitMask": 2, "room": 0x9ad9, "area": "Brinstar"},
    "MainShaftRight": {"byteIndex": 150, "bitMask": 2, "room": 0x9ad9, "area": "Brinstar"},
    "GreenBrinstarMissileRefill": {"byteIndex": 158, "bitMask": 2, "room": 0x9ad9, "area": "Brinstar"},
    "MainShaftBottomRight": {"byteIndex": 158, "bitMask": 2, "room": 0x9ad9, "area": "Brinstar"},
    "EarlySupersRight": {"byteIndex": 150, "bitMask": 16, "room": 0x9bc8, "area": "Brinstar"},
    "BigPinkRight": {"byteIndex": 165, "bitMask": 4, "room": 0x9d19, "area": "Brinstar"},
    "BigPinkBottomRight": {"byteIndex": 173, "bitMask": 4, "room": 0x9d19, "area": "Brinstar"},
    "BigPinkTopRight": {"byteIndex": 149, "bitMask": 4, "room": 0x9d19, "area": "Brinstar"},
    "BigPinkBottomLeft": {"byteIndex": 186, "bitMask": 128, "room": 0x9d19, "area": "Brinstar"},
    "GreenHillZoneTopRight": {"byteIndex": 173, "bitMask": 16, "room": 0x9e52, "area": "Brinstar"},
    "ConstructionZoneRight": {"byteIndex": 172, "bitMask": 32, "room": 0x9f11, "area": "Brinstar"},
    "NoobBridgeRight": {"byteIndex": 59, "bitMask": 1, "room": 0x9fba, "area": "Brinstar"},
    "EtecoonEnergyTankLeft": {"byteIndex": 175, "bitMask": 64, "room": 0xa011, "area": "Brinstar"},
    "RedBrinstarEnergyRefill": {"byteIndex": 79, "bitMask": 2, "room": 0xa253, "area": "Brinstar"},
    "RedTowerLeft": {"byteIndex": 67, "bitMask": 2, "room": 0xa253, "area": "Brinstar"},
    "RedBrinstarFirefleaLeft": {"byteIndex": 192, "bitMask": 2, "room": 0xa293, "area": "Brinstar"},
    "RedTowerElevatorTopLeft": {"byteIndex": 35, "bitMask": 32, "room": 0xa322, "area": "Brinstar"},
    "RedTowerElevatorLeft": {"byteIndex": 43, "bitMask": 32, "room": 0xa322, "area": "Brinstar"},
    "RedTowerElevatorBottomLeft": {"byteIndex": 51, "bitMask": 32, "room": 0xa322, "area": "Brinstar"},
    "BelowSpazerTopRight": {"byteIndex": 75, "bitMask": 32, "room": 0xa408, "area": "Brinstar"},
    "KraidRefillStation": {"byteIndex": 77, "bitMask": 32, "room": 0xa56b, "area": "Brinstar"},
    "CathedralRight": {"byteIndex": 149, "bitMask": 2, "room": 0xa788, "area": "Norfair"},
    "CathedralEntranceRight": {"byteIndex": 146, "bitMask": 64, "room": 0xa7b3, "area": "Norfair"},
    "BusinessCenterTopLeft": {"byteIndex": 146, "bitMask": 8, "room": 0xa7de, "area": "Norfair"},
    "BusinessCenterBottomLeft": {"byteIndex": 154, "bitMask": 8, "room": 0xa7de, "area": "Norfair"},
    "CrocomireSpeedwayBottom": {"byteIndex": 169, "bitMask": 1, "room": 0xa923, "area": "Norfair"},
    "PostCrocomireUpperLeft": {"byteIndex": 174, "bitMask": 4, "room": 0xaa82, "area": "Norfair"},
    "PostCrocomireShaftRight": {"byteIndex": 194, "bitMask": 4, "room": 0xab07, "area": "Norfair"},
    "BubbleMountainTopLeft": {"byteIndex": 141, "bitMask": 128, "room": 0xacb3, "area": "Norfair"},
    "BubbleMountainTopRight": {"byteIndex": 140, "bitMask": 1, "room": 0xacb3, "area": "Norfair"},
    "SpeedBoosterHallRight": {"byteIndex": 15, "bitMask": 32, "room": 0xacf0, "area": "Norfair"},
    "SingleChamberRight": {"byteIndex": 148, "bitMask": 2, "room": 0xad5e, "area": "Norfair"},
    "DoubleChamberRight": {"byteIndex": 148, "bitMask": 32, "room": 0xadad, "area": "Norfair"},
    "KronicBoostBottomLeft": {"byteIndex": 172, "bitMask": 8, "room": 0xae74, "area": "Norfair"},
    "RedKihunterShaftBottom": {"byteIndex": 59, "bitMask": 64, "room": 0xb585, "area": "Norfair"},
    "WastelandLeft": {"byteIndex": 71, "bitMask": 4, "room": 0xb5d5, "area": "Norfair"},
    "WreckedShipMainShaftBottom": {"byteIndex": 204, "bitMask": 2, "room": 0xcaf6, "area": "WreckedShip"},
    "ElectricDeathRoomTopLeft": {"byteIndex": 184, "bitMask": 64, "room": 0xcbd5, "area": "WreckedShip"},
    "MaridiaBottomSaveStation": {"byteIndex": 210, "bitMask": 1, "room": 0xcefb, "area": "Maridia"},
    "MainStreetBottomRight": {"byteIndex": 198, "bitMask": 1, "room": 0xcfc9, "area": "Maridia"},
    "FishTankRight": {"byteIndex": 194, "bitMask": 32, "room": 0xd017, "area": "Maridia"},
    "CrabShaftRight": {"byteIndex": 173, "bitMask": 1, "room": 0xd1a3, "area": "Maridia"},
    "ForgottenHighwaySaveStation": {"byteIndex": 148, "bitMask": 128, "room": 0xd30b, "area": "Maridia"},
    "PlasmaSparkBottom": {"byteIndex": 149, "bitMask": 8, "room": 0xd340, "area": "Maridia"},
    "OasisTop": {"byteIndex": 193, "bitMask": 8, "room": 0xd48e, "area": "Maridia"},
    "MaridiaAqueductSaveStation": {"byteIndex": 177, "bitMask": 2, "room": 0xd5a7, "area": "Maridia"},
    "DraygonSaveRefillStation": {"byteIndex": 31, "bitMask": 32, "room": 0xd72a, "area": "Maridia"},
    "ColosseumBottomRight": {"byteIndex": 35, "bitMask": 32, "room": 0xd72a, "area": "Maridia"}
}

from graph.vanilla.map_tiles import objectives as vanillaObjectives
import copy

objectives = copy.copy(vanillaObjectives)

# brinstar
objectives["Kraid"]["map_coords_px"] = (60, 156)
objectives["SporeSpawn"]["map_coords_px"] = (328, 24)
objectives["Etecoons"]["map_coords_px"] = (416, 96)
objectives["Dachora"]["map_coords_px"] = (424, 104)
# wrecked ship
objectives["Phantoon"]["map_coords_px"] = (280, 160)
objectives["WreckedShipChozo"]["map_coords_px"] = (320, 104)
# draygon
objectives["Draygon"]["map_coords_px"] = (212, 84)
objectives["Botwoon"]["map_coords_px"] = (336, 72)
objectives["RedFish"]["map_coords_px"] = (416, 72)
objectives["Shaktool"]["map_coords_px"] = (304, 128)
# crateria
objectives["OrangeGeemer"]["map_coords_px"] = (152, 24)
objectives["BombTorizo"]["map_coords_px"] = (296, 56)
# norfair
objectives["Ridley"]["map_coords_px"] = (312, 140)
objectives["Crocomire"]["map_coords_px"] = (364, 88)
objectives["GoldenTorizo"]["map_coords_px"] = (344, 132)
objectives["LowerNorfairChozo"]["map_coords_px"] = (376, 112)
objectives["KingCacatac"]["map_coords_px"] = (324, 24)
