from logic.smbool import SMBool
from rom.rom import snes_to_pc

# global logic identifiers for ROM patches presence
# use RomPatches.has(RomPatches.SomePatch) in logic functions to check for presence
# add a patch to ActivePatches to enable it logically
class RomPatches:
    #### Patches definitions

    ### Layout
    # blue door to access the room with etank+missile
    BlueBrinstarBlueDoor      = 10
    # missile in the first room is a major item and accessible and ceiling is a minor
    BlueBrinstarMissile       = 11
    # shot block instead of bomb blocks for spazer access
    SpazerShotBlock           = 20
    # climb back up red tower from bottom no matter what
    RedTowerLeftPassage       = 21
    # exit red tower top to crateria
    RedTowerBlueDoors         = 22
    # shot block in crumble blocks at early supers
    EarlySupersShotBlock      = 23
    # brinstar reserve area door blue
    BrinReserveBlueDoors      = 24
    # red tower top PB door to hellway
    HellwayBlueDoor           = 25
    # etecoon supers blue door
    EtecoonSupersBlueDoor     = 26
    # red tower top Super door to alpha PBs
    AlphaPowerBombBlueDoor    = 27
    # shot block to exit hi jump area
    HiJumpShotBlock           = 30
    # access main upper norfair without anything
    CathedralEntranceWallJump = 31
    # graph blue doors
    HiJumpAreaBlueDoor        = 32
    SpeedAreaBlueDoors        = 33
    # LN start
    LowerNorfairPBRoomHeatDisable = 34
    FirefleasRemoveFune       = 35
    # moat bottom block
    MoatShotBlock             = 41
    #graph+forgotten hiway anti softlock
    SpongeBathBlueDoor        = 42
    # forgotten hiway anti softlock
    EastOceanPlatforms        = 43
    # maridia
    MaridiaTubeOpened         = 51
    MamaTurtleBlueDoor        = 52
    # ws start
    WsEtankBlueDoor           = 53
    ## Area rando patches
    # remove crumble block for reverse lower norfair door access
    SingleChamberNoCrumble    = 101
    # remove green gates for reverse maridia access
    AreaRandoGatesBase        = 102
    # remove crab green gate in maridia and blue gate in green brinstar
    AreaRandoGatesOther       = 103
    # disable Green Hill Yellow, Noob Bridge Green, Coude Yellow, and Kronic Boost yellow doors
    AreaRandoBlueDoors        = 104
    # crateria key hunter yellow, green pirates shaft red
    AreaRandoMoreBlueDoors    = 105
    # croc green+grey doors
    CrocBlueDoors             = 106
    # maridia crab shaft AP door
    CrabShaftBlueDoor         = 107
    # wrap door from sand halls left to under botwoon
    MaridiaSandWarp           = 108
    # Replace PB blocks at Aqueduct entrance with bomb blocks
    AqueductBombBlocks        = 109
    # climb back up crab hole without items
    CrabHoleClimb             = 110
    ## Minimizer Patches
    NoGadoras                 = 200
    TourianSpeedup            = 201
    OpenZebetites             = 202

    ### Other
    # Gravity no longer protects from environmental damage (heat, spikes...)
    NoGravityEnvProtection  = 1000
    # Wrecked Ship etank accessible when Phantoon is alive
    WsEtankPhantoonAlive    = 1001
    # Lower Norfair chozo (vanilla access to GT/Screw Area) : disable space jump check
    LNChozoSJCheckDisabled  = 1002
    # Progressive suits patch, mutually exclusive with NoGravityEnvProtection
    ProgressiveSuits        = 1003
    # Nerfed charge beam available from the start
    NerfedCharge            = 1004
    # Nerfed rainbow beam for ultra sparse energy qty
    NerfedRainbowBeam       = 1005
    # Red doors open with one missile, and don't react to supers: part of door color rando
    RedDoorsMissileOnly     = 1006
    # Escape auto-trigger on objectives completion (no Tourian)
    NoTourian               = 1007
    # BT wakes up on its item instead of bombs
    BombTorizoWake          = 1008
    # Round-Robin Crystal Flash patch
    RoundRobinCF            = 1009

    ### Hacks
    # rotation hack
    RotationHack            = 10000

    #### Patch sets
    # total randomizer
    TotalBase = [ BlueBrinstarBlueDoor, RedTowerBlueDoors, NoGravityEnvProtection ]
    # tournament and full
    TotalLayout = [ MoatShotBlock, EarlySupersShotBlock,
                    SpazerShotBlock, RedTowerLeftPassage,
                    HiJumpShotBlock, CathedralEntranceWallJump ]

    Total = TotalBase + TotalLayout

    # casual
    TotalCasual = [ BlueBrinstarMissile ] + Total

    # area rando patch set
    AreaBaseSet = [ SingleChamberNoCrumble, AreaRandoGatesBase,
                    AreaRandoBlueDoors, AreaRandoMoreBlueDoors,
                    CrocBlueDoors, CrabShaftBlueDoor, MaridiaSandWarp ]
    AreaComfortSet = [ AreaRandoGatesOther, SpongeBathBlueDoor, EastOceanPlatforms,
                       AqueductBombBlocks, CrabHoleClimb ]
    AreaSet = AreaBaseSet + AreaComfortSet

    # VARIA specific patch set
    VariaTweaks = [ WsEtankPhantoonAlive, LNChozoSJCheckDisabled, BombTorizoWake ]

    # Tourian speedup in minimizer mode
    MinimizerTourian = [ TourianSpeedup, OpenZebetites ]

    # dessyreqt randomizer
    Dessy = []

    ### Active patches
    ActivePatches = []

    @staticmethod
    def has(patch):
        return SMBool(patch in RomPatches.ActivePatches)

    @staticmethod
    def setDefaultPatches(startLocation):
        # called by the isolver in seedless mode.
        # activate only layout patch (the most common one), red tower blue doors, startLocation's patches and balanced suits.
        from graph.graph_utils import GraphUtils
        RomPatches.ActivePatches = [RomPatches.RedTowerBlueDoors] + RomPatches.TotalLayout + GraphUtils.getGraphPatches(startLocation) + [RomPatches.NoGravityEnvProtection]

_baseIPS = [
    # common utility routines
    'utils.ips',
    # MFreak map patch, tweaked for VARIA
    'map.ips',
    # game map
    'map_data.ips',
    # game map palettes for graph areas
    'map_data_area.ips',
    # boot, save files and backup management, stats infrastructure
    'base.ips',
    # quick reset hook
    'reset.ips',
    # handles starting location and start blue doors
    'start.ips',
    # generic PLM spawner used for extra saves, blinking doors etc.
    'plm_spawn.ips',
    # needed fixes for VARIA
    'vanilla_bugfixes.ips',
    # use a byte in a unused room state header field to store area ID in the VARIA sense
    'area_ids.ips',
    # custom credits
    'credits.ips',
    # actual game hijacks to update tracking stats
    'stats.ips',
    # enemy names in menu for seed ID
    'seed_display.ips',
    # door ASM to wake zebes early in blue brinstar
    'wake_zebes.ips',
    # use any button for angle up/down
    'AimAnyButton.ips',
    # credits item% based on actual number of items in the game
    'endingtotals.ips',
    # MSU-1 patch
    'supermetroid_msu1.ips',
    # displays max ammo 
    'max_ammo_display.ips',
    # VARIA logo on startup screen
    'varia_logo.ips',
    # new nothing plm
    'nothing_item_plm.ips',
    # objectives management and display
    'objectives.ips',
    # objectives ROM options
    'objectives_options.ips',
    # display collected items percentage and RTA time in pause inventory menu
    'equipment_screen.ips',
    # always disable demos as it causes crashes in area, hud and mirrortroid
    'no_demo.ips'
]

_layoutIPS = [
    # new PLMs for indicating the color of the door on the other side
    'door_indicators_plms.ips',
    # layout patches
    'dachora.ips', 'early_super_bridge.ips', 'high_jump.ips', 'moat.ips', 'spospo_save.ips',
    'nova_boost_platform.ips', 'red_tower.ips', 'spazer.ips', 'climb_supers.ips',
    'brinstar_map_room.ips', 'kraid_save.ips', 'mission_impossible.ips'
]

_layoutArea = [
    "WS_Main_Open_Grey", "WS_Save_Active",
    # make incompatible door transitions work
    'door_transition.ips',
    # east maridia looping doors (common)
    'area_rando_doors.ips',
    # remove maridia red fish exit green gate (move plm in room A322: Caterpillar Room - flavor)
    'area_rando_gate_caterpillar.ips',
    # remove maridia tube exit green gate (move plm in room CF80: East Tunnel - common)
    'area_rando_gate_east_tunnel.ips',
    # remove lower norfair exit crumble blocks (change layout in room AD5E: Single Chamber - flavor)
    'area_layout_ln_exit.ips',
    # additionnal save at crab shaft (change layout in room D1A3: Crab Shaft - flavor)
    'crab_shaft.ips',
    'Save_Crab_Shaft',
    # additionnal save at main street
    'Save_Main_Street',
    # change door connection in bank 83 (room D461: West Sand Hall - flavor)
    'area_door_west_sand_hall.ips',
    # change layout (room D6FD: Sand falls sand pit - flavor)
    'area_rando_warp_door.ips'
]

_layoutAreaComfort = [
    # remove crab geen gate in maridia (move plm in room D08A: Crab Tunnel - common)
    'area_rando_gate_crab_tunnel.ips',
    # update ceiling on top on the gate (change layout in room D08A: Crab Tunnel - flavor)
    'area_layout_crabe_tunnel.ips',
    # remove blue gate in green hill zone (move plm in room 9E52: Green Hill Zone - flavor)
    'area_rando_gate_greenhillzone.ips',
    # access transition door in green hill zone (change layout in room 9E52: Green Hill Zone - flavor)
    'area_layout_greenhillzone.ips',
    # set sponge bath door to blue in wreckedship
    'Sponge_Bath_Blinking_Door',
    # add platforms to traverse forgotten hiway both ways (change layout in room 94FD: east ocean - flavor)
    'east_ocean.ips',
    # aqueduct entrance pb blocks changed to bomb blocks (change layout in room D5A7: aqueduct - flavor)
    'aqueduct_bomb_blocks.ips',
    # reveal opening to portal (change layout in room CF80: east tunnel - flavor)
    'area_layout_east_tunnel.ips',
    # reveal opening to portal (change layout in room A322: Caterpillar Room - flavor)
    'area_layout_caterpillar.ips',
    # reveal opening to portal (change layout in room AD5E: Single Chamber - flavor)
    # to be applied on top of patch area_layout_ln_exit.ips
    'area_layout_single_chamber.ips',
    # make it possible to climb back up crab hole with no items
    'area_layout_crab_hole_lvl.ips',
    'area_layout_crab_hole_plms_enemies.ips'
]

# Patches definition tables: 'common' + a table for each flavor
# each table has patch names associated to entries as follows:
# 'desc': patch description
# 'address'/'value': detection byte
# 'ips': (optional) ROM patch list to apply
# 'logic': (optional) logic patch list to apply
definitions = {
    'common': {
        'startCeres': {
            'address': snes_to_pc(0x80ff1f), 'value': 0xB6,
            'desc': "Blue Brinstar and Red Tower blue doors",
            'logic': [RomPatches.BlueBrinstarBlueDoor,
                      RomPatches.RedTowerBlueDoors]
        },
        'startLS': {
            'address': snes_to_pc(0x80ff17), 'value': 0xB6,
            'desc': "Blue Brinstar and Red Tower blue doors",
            'logic': [RomPatches.BlueBrinstarBlueDoor,
                      RomPatches.RedTowerBlueDoors]
        },
        'casual': {
            'address': snes_to_pc(0xc5e87a), 'value': 0x9F,
            'desc': "Switch Blue Brinstar Etank and missile",
            'logic': [RomPatches.BlueBrinstarMissile]
        },
        'gravityNoHeatProtection': {
            'address': snes_to_pc(0x90e9dd), 'value': 0x01,
            'desc': "Gravity suit heat protection removed",
            'ips': ["Removes_Gravity_Suit_heat_protection"],
            'logic': [RomPatches.NoGravityEnvProtection]
        },
        'progressiveSuits': {
            'address': snes_to_pc(0x90e9df), 'value': 0xF0,
            'desc': "Progressive suits",
            'ips': ['progressive_suits.ips'],
            'logic': [RomPatches.ProgressiveSuits]
        },
        # nerfed charge taken in vanilla ROM space value works for both DASH and VARIA variants
        'nerfedCharge': {
            'address': snes_to_pc(0x90b821), 'value': 0x80,
            'desc': "Nerfed charge beam from the start of the game",
            'ips': ['nerfed_charge.ips'],
            'logic': [RomPatches.NerfedCharge]
        },
        'variaTweaks': {
            'address': snes_to_pc(0x8fcc4d), 'value': 0x37,
            'desc': "VARIA tweaks",
            'ips': ['WS_Etank', 'LN_Chozo_SpaceJump_Check_Disable',
                    'ln_chozo_platform.ips', 'bomb_torizo.ips'],
            'logic': RomPatches.VariaTweaks
        },
        'boss': {
            # TODO? addr/value?
            'desc': "Bosses randomization",
            'ips': [
                'door_transition.ips',
                'Phantoon_Eye_Door',
                "WS_Main_Open_Grey",
                "WS_Save_Active"
            ]
        },
        'areaEscape': {
            'address': snes_to_pc(0x848c91), 'value': 0x4C,
            'desc': "Area escape randomization",
            'ips': ['rando_escape_common.ips', 'rando_escape.ips',
                    'rando_escape_ws_fix.ips', 'door_transition.ips']
        },
        'base': {
            'address': snes_to_pc(0x82801d), 'value': 0x22,
            'desc': "VARIA base patches",
            'ips': _baseIPS,
            'logic': [RomPatches.RedTowerBlueDoors]
        },
        'nerfedRainbowBeam': {
            'address': snes_to_pc(0xa9ba2e), 'value': 0x13,
            'desc': 'nerfed rainbow beam',
            'ips': ["nerfed_rainbow_beam.ips"],
            'logic': [RomPatches.NerfedRainbowBeam]
        },
        'minimizer_bosses': {
            'address': snes_to_pc(0xa7afad), 'value': 0x5C,
            'desc': "Minimizer",
            'ips': ['minimizer_bosses.ips'],
            'logic': [RomPatches.NoGadoras]
        },
        'fast_tourian': {
            'address': snes_to_pc(0xa9b90e), 'value': 0xCF,
            'desc': "Fast Tourian",
            'ips': ['minimizer_tourian_common.ips', 'minimizer_tourian.ips', 'open_zebetites.ips'],
            'logic': [RomPatches.TourianSpeedup, RomPatches.OpenZebetites]
        },
        'doorsColorsRando': {
            'address': snes_to_pc(0x84a6e5), 'value': 0x0D,
            'desc': "Door color rando",
            'ips': ['beam_doors_plms.ips', 'beam_doors_gfx.ips', 'red_doors.ips'],
            'logic': [RomPatches.RedDoorsMissileOnly]
        },
        'objectives': {
            'address': snes_to_pc(0x82a822), 'value': 0x08,
            'desc': "Objectives displayed in pause",
            'ips': ['objectives.ips', 'objectives_options.ips']
        },
        'round_robin_cf': {
            'address': snes_to_pc(0x90d5d6), 'value': 0x0,
            'desc': "Round robin Crystal Flash",
            'ips': ['relaxed_round_robin_cf.ips'],
            'logic': [RomPatches.RoundRobinCF]
        },
        'revealMap': {
            'address': snes_to_pc(0x8FE893), 'value': 0x20,
            'desc': "Map revealed from the start",
            'ips': ['reveal_map.ips', 'reveal_map_data.ips']
        },
        'hud': {
            'address': snes_to_pc(0x809B8B), 'value': 0x20,
            'desc': "VARIA HUD",
            'ips': ['varia_hud.ips']
        },
        'debug': {
            'address': snes_to_pc(0xb5ffed), 'value': 0x0,
            'desc': "Debug Hack",
            'ips': ['Debug_Full.ips']
        }
    },
    'vanilla': {
        'logic': {
            'ips': []
        },
        'layout': {
            'address': snes_to_pc(0xc3bd80), 'value': 0xD5,
            'desc': "Anti soft lock layout modifications",
            'ips': _layoutIPS,
            'logic': RomPatches.TotalLayout
        },
        'area': {
            'address': snes_to_pc(0x8f88a0), 'value': 0x2B,
            'desc': "Area layout modifications",
            'ips': _layoutArea,
            'logic': RomPatches.AreaBaseSet
        },
        'areaLayout': {
            'address': snes_to_pc(0xcaafa7), 'value': 0xF8,
            'desc': "Area layout additional modifications",
            'ips': _layoutAreaComfort,
            'logic': RomPatches.AreaComfortSet
        },
        'traverseWreckedShip': {
            'address': snes_to_pc(0xc39dbf), 'value': 0xFB,
            'desc': "Area layout additional access to east Wrecked Ship"
        },
        'aqueductBombBlocks': {
            'address': snes_to_pc(0xcc82d6), 'value': 0x44,
            'desc': "Aqueduct entrance bomb blocks instead of power bombs"
        },
        'open_zebetites': {
            'address': snes_to_pc(0xcddf22), 'value': 0xc3,
            'desc': "Zebetites without morph"
        }
    },
    'mirror': {
        'logic': {
            'address': snes_to_pc(0x84d650), 'value': 0x29,
            'desc': "MirrorTroid hack",
            'ips': ['mirrortroid.ips', 'bank_8f.ips', 'bank_83.ips', 'map_icon_data.ips',
                    'baby_room.ips', 'baby_remove_blocks.ips', 'escape_animals.ips',
                    'snails.ips', 'boulders.ips', 'rinkas.ips', 'etecoons.ips', 'crab_main_street.ips',
                    'crab_mt_everest.ips', 'mother_brain.ips', 'kraid.ips', 'torizos.ips', 'botwoon.ips',
                    'crocomire.ips', 'ridley.ips', 'ws_treadmill.ips']
        },
        'layout': {
            'address': snes_to_pc(0xc3bd80),
            'value': 0x32, 'desc': "Anti soft lock layout modifications",
            'ips': _layoutIPS,
            'logic': RomPatches.TotalLayout
        },
        'area': {
            'address': snes_to_pc(0x8f88a0), 'value': 0x04,
            'desc': "Area layout modifications",
            'ips': _layoutArea,
            'logic': RomPatches.AreaBaseSet
        },
        'areaLayout': {
            'address': snes_to_pc(0xcaafa7),
            'value': 0x03,
            'desc': "Area layout additional modifications",
            'ips': _layoutAreaComfort,
            'logic': RomPatches.AreaComfortSet
        },
        'traverseWreckedShip': {
            'address': snes_to_pc(0xc39df6), 'value': 0x84,
            'desc': "Area layout additional access to east Wrecked Ship"
        },
        'aqueductBombBlocks': {
            'address': snes_to_pc(0xcc82d6), 'value': 0x6c,
            'desc': "Aqueduct entrance bomb blocks instead of power bombs"
        },
        'open_zebetites': {
            'address': snes_to_pc(0xcddf22), 'value': 0x48,
            'desc': "Zebetites without morph"
        }
    }
}

def getPatchSet(setName, flavor=None):
    if setName in definitions['common']:
        patchSet = definitions['common'][setName]
    elif flavor is not None and setName in definitions[flavor]:
        patchSet = definitions[flavor][setName]
    else:
        raise ValueError(f"Invalid patch set {setName}")
    return patchSet

def getPatchSetsFromPatcherSettings(patcherSettings):
    patchSets = ["logic", "base"]
    boolSettings = [
        "layout",
        "nerfedCharge",
        "nerfedRainbowBeam",
        "variaTweaks",
        "area",
        "areaLayout",
        "boss",
        "doorsColorsRando",
        "hud",
        "revealMap",
        "round_robin_cf",
        "debug"
    ]
    patchSets += [k for k in boolSettings if patcherSettings.get(k) == True]
    if patcherSettings["suitsMode"] == "Balanced":
        patchSets.append("gravityNoHeatProtection")
    elif patcherSettings["suitsMode" ] == "Progressive":
        patchSets.append("progressiveSuits")
    if patcherSettings["escapeAttr"] is not None:
        patchSets.append("areaEscape")
    if patcherSettings["minimizerN"] is not None:
        patchSets.append("minimizer_bosses")
    if patcherSettings["tourian"] == "Fast":
        patchSets.append("fast_tourian")
    return patchSets
