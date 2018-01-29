#!/usr/bin/python

# https://itemrando.supermetroid.run/randomize

import sys, struct, math, os, json, logging, argparse

# the difficulties for each technics
from parameters import Conf, Knows, Settings
from parameters import easy, medium, hard, harder, hardcore, mania

# the helper functions
from helpers import *

class Solver:
    # given a rom and parameters returns the estimated difficulty
    
    def __init__(self, type='console', rom=None, params=None, debug=False):
        if debug is True:
            logging.basicConfig(level=logging.DEBUG)
        else:
            logging.basicConfig(level=logging.INFO)
        self.log = logging.getLogger('Solver')

        if params is not None:
            for paramsFileName in params:
                self.loadParams(paramsFileName)

        # can be called from command line (console) or from web site (web)
        self.type = type

        import tournament_locations
        self.locations = tournament_locations.locations

        self.romLoaded = False
        if rom is not None:
            self.loadRom(rom)
        
        self.pickup = Pickup(Conf.majorsPickup, Conf.minorsPickup)

        Bosses.reset()

    def loadRom(self, rom):
        RomLoader.factory(rom).assignItems(self.locations)

        if self.log.getEffectiveLevel() == logging.DEBUG:
            self.log.debug("Display items at locations:")
            for location in self.locations:
                self.log.debug('{:>50}: {:>16}'.format(location["Name"], location['itemName']))

        self.romLoaded = True

    def loadParams(self, params):
        ParamsLoader.factory(params).load()

        if self.log.getEffectiveLevel() == logging.DEBUG:
            self.log.debug("loaded knows: ")
            for knows in Knows.__dict__:
                if knows[0:len('__')] != '__':
                    self.log.debug("{}: {}".format(knows, Knows.__dict__[knows]))
            self.log.debug("loaded settings:")
            for setting in Settings.__dict__:
                if setting[0:len('__')] != '__':
                    self.log.debug("{}: {}".format(setting, Settings.__dict__[setting]))
            self.log.debug("loaded conf:")
            for conf in Conf.__dict__:
                if conf[0:len('__')] != '__':
                    self.log.debug("{}: {}".format(conf, Conf.__dict__[conf]))

    def solveRom(self):
        if self.romLoaded is False:
            self.log.error("rom not loaded")
            return

        difficulty = self.computeDifficulty()

        if self.type == 'console':
            # print generated path
            if Conf.displayGeneratedPath is True:
                self.printPath("Generated path:", self.visitedLocations)
                # if we've aborted, display remaining majors
                if difficulty == -1:
                    self.printPath("Remaining major locations:", self.majorLocations)
                    self.printPath("Remaining minor locations:", self.minorLocations)

            # display difficulty scale
            self.displayDifficulty(difficulty)

        return difficulty

    def displayDifficulty(self, difficulty):
        if difficulty >= 0:
            text = DifficultyDisplayer(difficulty).scale()
            print("Estimated difficulty: {}".format(text))
        else:
            print("Aborted run, can't finish the game with the given prerequisites")

    def computeDifficulty(self):
        # loop on the available locations depending on the collected items.
        # before getting a new item, loop on all of them and get their difficulty,
        # the next collected item is the one with the smallest difficulty,
        # if equality between major and minor, take major first.

        self.majorLocations = [loc for loc in self.locations if loc["Class"] == "Major"]
        self.minorLocations = [loc for loc in self.locations if loc["Class"] == "Minor"]

        self.visitedLocations = []
        self.collectedItems = []

        # with the knowsXXX conditions some roms can be unbeatable, so we have to detect it
        previous = -1
        current = 0

        self.log.debug("{}/{}: available major: {}, available minor: {}, visited: {}".format(Conf.majorsPickup, str(Conf.minorsPickup), len(self.majorLocations), len(self.minorLocations), len(self.visitedLocations)))

        isEndPossible = False
        endDifficulty = mania
        area = 'Crateria'
        while True:
            # actual while condition
            hasEnoughItems = (self.pickup.enoughMajors(self.collectedItems, self.majorLocations)
                              and self.pickup.enoughMinors(self.collectedItems, self.minorLocations))
            canEndGame = self.canEndGame()
            (isEndPossible, endDifficulty) = (canEndGame.bool, canEndGame.difficulty)
            if isEndPossible and hasEnoughItems:
                self.log.debug("END")
                break

            #self.log.debug(str(self.collectedItems))
            self.log.debug("Current Area : " + area)

            # check if we have collected an item in the last loop
            current = len(self.collectedItems)
            if current == previous:
                # we're stuck ! abort
                self.log.debug("STUCK ALL")
                break
            previous = current

            # compute the difficulty of all the locations
            self.computeLocationsDifficulty(self.majorLocations)
            self.computeLocationsDifficulty(self.minorLocations)

            # keep only the available locations
            majorAvailable = [loc for loc in self.majorLocations if loc["difficulty"].bool == True]
            minorAvailable = [loc for loc in self.minorLocations if loc["difficulty"].bool == True]

            # check if we're stuck
            if len(majorAvailable) == 0 and len(minorAvailable) == 0:
                self.log.debug("STUCK MAJORS and MINORS")
                break

            # sort them on difficulty and proximity
            majorAvailable = self.getAvailableItemsList(majorAvailable, area, Conf.difficultyTarget)
            minorAvailable = self.getAvailableItemsList(minorAvailable, area, Conf.difficultyTarget)

            # first take major items of acceptable difficulty in the current area
            if (len(majorAvailable) > 0
                   and majorAvailable[0]['Area'] == area
                   and majorAvailable[0]['difficulty'].difficulty <= Conf.difficultyTarget):
                self.collectMajor(majorAvailable.pop(0))
                continue
            # next item decision
            if len(minorAvailable) == 0 and len(majorAvailable) > 0:
                self.log.debug('MAJOR')
                area = self.collectMajor(majorAvailable.pop(0))
            elif len(majorAvailable) == 0 and len(minorAvailable) > 0:
                self.log.debug('MINOR')
                area = self.collectMinor(minorAvailable.pop(0))
            elif len(majorAvailable) > 0 and len(minorAvailable) > 0:
                self.log.debug('BOTH|M=' + majorAvailable[0]['Name'] + ', m=' + minorAvailable[0]['Name'])
                # if both are available, decide based on area and difficulty
                nextMajDifficulty = majorAvailable[0]['difficulty'].bool
                nextMinArea = minorAvailable[0]['Area']
                nextMinDifficulty = minorAvailable[0]['difficulty'].bool
                if nextMinArea == area and nextMinDifficulty <= Conf.difficultyTarget:
                    area = self.collectMinor(minorAvailable.pop(0))
                # difficulty over area (this is a difficulty estimator,
                # not a speedrunning simulator)
                elif nextMinDifficulty < nextMajDifficulty:
                    area = self.collectMinor(minorAvailable.pop(0))
                else:
                    area = self.collectMajor(majorAvailable.pop(0))
        # main loop end
        if isEndPossible:
            self.visitedLocations.append({
                'item' : 'The End',
                'itemName' : 'The End',
                'Name' : 'The End',
                'Area' : 'The End',
                'difficulty' : SMBool(True, endDifficulty)
            })

        # compute difficulty value
        difficulty = self.computeDifficultyValue()

        self.log.debug("difficulty={}".format(difficulty))
        self.log.debug("{}/{}: remaining major: {}, remaining minor: {}, visited: {}".format(Conf.majorsPickup, Conf.minorsPickup, len(self.majorLocations), len(self.minorLocations), len(self.visitedLocations)))

        self.log.debug("remaining majors:")
        for loc in self.majorLocations:
            self.log.debug("{} ({})".format(loc['Name'], loc['itemName']))

        self.log.debug("bosses: {}".format(Bosses.golden4Dead))

        return difficulty

    def computeLocationsDifficulty(self, locations):
        for loc in locations:
            if 'PostAvailable' in loc:
                loc['difficulty'] = wand(loc['Available'](self.collectedItems),
                                         loc['PostAvailable'](self.collectedItems + [loc['itemName']]))
            else:
                loc['difficulty'] = loc['Available'](self.collectedItems)

    def computeDifficultyValue(self):
        if not self.pickup.enoughMajors(self.collectedItems, self.majorLocations) or not self.pickup.enoughMinors(self.collectedItems, self.minorLocations) or not self.canEndGame().bool:
            # we have aborted
            difficulty = -1
        else:
            # sum difficulty for all visited locations
            difficulty_max = 0
            for loc in self.visitedLocations:
                difficulty_max = max(difficulty_max, loc['difficulty'].difficulty)
            difficulty = difficulty_max

        return difficulty

    def getPath(self, locations):
        out = []
        for location in locations:
            out.append([location['Name'], location['Area'], location['itemName'], '{0:.2f}'.format(location['difficulty'].difficulty), ', '.join(location['difficulty'].knows)])

        return out

    def getKnowsUsed(self):
        knows = []
        for loc in self.visitedLocations:
            knows += loc['difficulty'].knows

        # get unique knows
        knows = list(set(knows))

        return knows

    def printPath(self, message, locations):
        print(message)
        print('{:>50} {:>13} {:>16} {:>14} {}'.format("Location Name", "Area", "Item", "Difficulty", "Knows used"))
        print('-'*106)
        for location in locations:
            print('{:>50}: {:>12} {:>16} {:>14} {}'.format(location['Name'],
                                                           location['Area'],
                                                           location['itemName'],
                                                           location['difficulty'].difficulty,
                                                           location['difficulty'].knows))

    def collectMajor(self, loc):
        self.majorLocations.remove(loc)
        self.visitedLocations.append(loc)
        area = self.collectItem(loc)
        return area

    def collectMinor(self, loc):
        self.minorLocations.remove(loc)
        self.visitedLocations.append(loc)
        area = self.collectItem(loc)
        return area

    def collectItem(self, loc):
        item = loc["itemName"]
        self.collectedItems.append(item)
        if 'Pickup' in loc:
            loc['Pickup']()

        self.log.debug("collectItem: {} at {}".format(item, loc['Name']))

        return loc['Area']

    def canEndGame(self):
        # to finish the game you must :
        # - beat golden 4 : we force pickup of the 4 items
        #   behind the bosses to ensure that
        # - defeat metroids
        # - destroy/skip the zebetites
        # - beat Mother Brain
        return wand(Bosses.allBossesDead(), enoughStuffTourian(self.collectedItems))

    def getAvailableItemsList(self, locations, area, threshold):
        around = [loc for loc in locations if loc['Area'] == area and loc['difficulty'].difficulty <= threshold and not Bosses.areaBossDead(area)]
        around.sort(key=lambda loc: loc['difficulty'].difficulty)

        outside = [loc for loc in locations if not loc in around]
        # we want to sort the outside locations by putting the ones is the same area first,
        # then we sort the remaining areas starting whith boss dead status
        outside.sort(key=lambda loc: (loc['difficulty'].difficulty, 0 if loc['Area'] == area else 1, 0 if not Bosses.areaBossDead(loc['Area']) else 1))

        return around + outside

class Items:
    itemsClasses = {
        'ETank': 'Major',
        'Missile': 'Minor',
        'Super': 'Minor',
        'PowerBomb': 'Minor',
        'Bomb': 'Major',
        'Charge': 'Major',
        'Ice': 'Major',
        'HiJump': 'Major',
        'SpeedBooster': 'Major',
        'Wave': 'Major',
        'Spazer': 'Major',
        'SpringBall': 'Major',
        'Varia': 'Major',
        'Plasma': 'Major',
        'Grapple': 'Major',
        'Morph': 'Major',
        'Reserve': 'Major',
        'Gravity': 'Major',
        'XRayScope': 'Major',
        'SpaceJump': 'Major',
        'ScrewAttack': 'Major',
        'Nothing': 'Nothing'
    }

    @staticmethod
    def getItemClass(item):
        return Items.itemsClasses[item]

class RomReader:
    # read the items in the rom
    items = {
        # vanilla
        '0xeed7': {'name': 'ETank'},
        '0xeedb': {'name': 'Missile'},
        '0xeedf': {'name': 'Super'},
        '0xeee3': {'name': 'PowerBomb'},
        '0xeee7': {'name': 'Bomb'},
        '0xeeeb': {'name': 'Charge'},
        '0xeeef': {'name': 'Ice'},
        '0xeef3': {'name': 'HiJump'},
        '0xeef7': {'name': 'SpeedBooster'},
        '0xeefb': {'name': 'Wave'},
        '0xeeff': {'name': 'Spazer'},
        '0xef03': {'name': 'SpringBall'},
        '0xef07': {'name': 'Varia'},
        '0xef13': {'name': 'Plasma'},
        '0xef17': {'name': 'Grapple'},
        '0xef23': {'name': 'Morph'},
        '0xef27': {'name': 'Reserve'},
        '0xef0b': {'name': 'Gravity'},
        '0xef0f': {'name': 'XRayScope'},
        '0xef1b': {'name': 'SpaceJump'},
        '0xef1f': {'name': 'ScrewAttack'},
        # old rando "chozo" items
        '0xef2b': {'name': 'ETank'},
        '0xef2f': {'name': 'Missile'},
        '0xef33': {'name': 'Super'},
        '0xef37': {'name': 'PowerBomb'},
        '0xef3b': {'name': 'Bomb'},
        '0xef3f': {'name': 'Charge'},
        '0xef43': {'name': 'Ice'},
        '0xef47': {'name': 'HiJump'},
        '0xef4b': {'name': 'SpeedBooster'},
        '0xef4f': {'name': 'Wave'},
        '0xef53': {'name': 'Spazer'},
        '0xef57': {'name': 'SpringBall'},
        '0xef5b': {'name': 'Varia'},
        '0xef5f': {'name': 'Gravity'},
        '0xef63': {'name': 'XRayScope'},
        '0xef67': {'name': 'Plasma'},
        '0xef6b': {'name': 'Grapple'},
        '0xef6f': {'name': 'SpaceJump'},
        '0xef73': {'name': 'ScrewAttack'},
        '0xef77': {'name': 'Morph'},
        '0xef7b': {'name': 'Reserve'},
        # old rando "hidden" items
        '0xef7f': {'name': 'ETank'},
        '0xef83': {'name': 'Missile'},
        '0xef87': {'name': 'Super'},
        '0xef8b': {'name': 'PowerBomb'},
        '0xef8f': {'name': 'Bomb'},
        '0xef93': {'name': 'Charge'},
        '0xef97': {'name': 'Ice'},
        '0xef9b': {'name': 'HiJump'},
        '0xef9f': {'name': 'SpeedBooster'},
        '0xefa3': {'name': 'Wave'},
        '0xefa7': {'name': 'Spazer'},
        '0xefab': {'name': 'SpringBall'},
        '0xefaf': {'name': 'Varia'},
        '0xefb3': {'name': 'Gravity'},
        '0xefb7': {'name': 'XRayScope'},
        '0xefbb': {'name': 'Plasma'},
        '0xefbf': {'name': 'Grapple'},
        '0xefc3': {'name': 'SpaceJump'},
        '0xefc7': {'name': 'ScrewAttack'},
        '0xefcb': {'name': 'Morph'},
        '0xefcf': {'name': 'Reserve'},
        '0x0': {'name': 'Nothing'}
    }

    def __init__(self, romFileName=None):
        if romFileName is not None:
            self.romFileName = romFileName

    def getItemFromFakeRom(self, fakeRom, address, visibility):
        value1 = fakeRom[address]
        value2 = fakeRom[address+1]
        value3 = fakeRom[address+4]

        if (value3 == int('0x1a', 16)
            and value2*256+value1 == int('0xeedb', 16)
            and address != int('0x786DE', 16)):
            return hex(0)

        if visibility == 'Visible':
            return hex(value2*256+(value1-0))
        elif visibility == 'Chozo':
            return hex(value2*256+(value1-84))
        elif visibility == 'Hidden':
            return hex(value2*256+(value1-168))
        else:
            # crash !
            manger.du(cul)

    def getItem(self, romFile, address, visibility):
        # return the hex code of the object at the given address

        romFile.seek(address, 0)
        # value is in two bytes
        value1 = struct.unpack("B", romFile.read(1))
        value2 = struct.unpack("B", romFile.read(1))

        # dessyreqt randomizer make some missiles non existant, detect it
        # 0x1a is to say that the item is a morphball
        # 0xeedb is missile item
        # 0x786de is Morphing Ball location
        romFile.seek(address+4, 0)
        value3 = struct.unpack("B", romFile.read(1))
        if (value3[0] == int('0x1a', 16)
            and value2[0]*256+(value1[0]) == int('0xeedb', 16)
            and address != int('0x786DE', 16)):
            return hex(0)

        # match itemVisibility with
        # | Visible -> 0
        # | Chozo -> 0x54 (84)
        # | Hidden -> 0xA8 (168)
        if visibility == 'Visible':
            return hex(value2[0]*256+(value1[0]-0))
        elif visibility == 'Chozo':
            return hex(value2[0]*256+(value1[0]-84))
        elif visibility == 'Hidden':
            return hex(value2[0]*256+(value1[0]-168))
        else:
            # crash !
            manger.du(cul)

    def loadItemsFromFakeRom(self, fakeRom, locations):
        for loc in locations:
            item = self.getItemFromFakeRom(fakeRom, loc["Address"], loc["Visibility"])
            loc["itemName"] = self.items[item]["name"]

    def loadItems(self, locations):
        with open(self.romFileName, "rb") as romFile:
            for loc in locations:
                item = self.getItem(romFile, loc["Address"], loc["Visibility"])
                loc["itemName"] = self.items[item]["name"]
                #print("{}: {} => {}".format(loc["Name"], loc["Class"], loc["itemName"]))

def isString(string):
    if sys.version[0] == '2':
        return type(string) == str or type(string) == unicode
    else:
        return type(string) == str

class RomLoader:
    @staticmethod
    def factory(rom):
        # can be a real rom. can be a json or a dict with the locations - items association
        # unicode only exists in python2
        if isString(rom):
            ext = os.path.splitext(rom)
            if ext[1].lower() == '.sfc' or ext[1].lower() == '.smc':
                return RomLoaderSfc(rom)
            elif ext[1].lower() == '.json':
                return RomLoaderJson(rom)
            else:
                print("wrong rom file type: {}".format(ext[1]))
                sys.exit(-1)
        elif type(rom) is dict:
            return RomLoaderDict(rom)

    def assignItems(self, locations):
        # update the itemName and Class of the locations
        for loc in locations:
            loc['itemName'] = self.locsItems[loc['Name']]
            loc["Class"] = self.getLocClass(loc["Name"], Items.getItemClass(loc['itemName']))

    def dump(self, fileName):
        with open(fileName, 'w') as jsonFile:
            json.dump(self.locsItems, jsonFile)

    def getLocClass(self, locName, itemClass):
        # always keep bosses locs as major
        if locName in ["Energy Tank, Ridley", "Right Super, Wrecked Ship",
                       "Space Jump", "Varia Suit"]:
            return "Major"
        else:
            return itemClass

class RomLoaderSfc(RomLoader):
    # standard usage
    def __init__(self, romFileName):
        self.romFileName = romFileName
        self.romReader = RomReader(romFileName)

    def assignItems(self, locations):
        # update the itemName of the locations
        self.romReader.loadItems(locations)

        self.locsItems = {}
        for loc in locations:
            self.locsItems[loc['Name']] = loc['itemName']
            loc["Class"] = self.getLocClass(loc["Name"], Items.getItemClass(loc['itemName']))

class RomLoaderJson(RomLoader):
    # when called from the test suite
    def __init__(self, jsonFileName):
        with open(jsonFileName) as jsonFile:
            self.locsItems = json.load(jsonFile)

class RomLoaderDict(RomLoader):
    # when called from the website
    def __init__(self, fakeRom):
        self.fakeRom = fakeRom

    def assignItems(self, locations):
        # update the itemName of the locations
        RomReader().loadItemsFromFakeRom(self.fakeRom, locations)

        self.locsItems = {}
        for loc in locations:
            self.locsItems[loc['Name']] = loc['itemName']
            loc["Class"] = self.getLocClass(loc["Name"], Items.getItemClass(loc['itemName']))

class ParamsLoader:
    @staticmethod
    def factory(params):
        # can be a json, a python file or a dict with the parameters
        if type(params) is str:
            ext = os.path.splitext(params)
            if ext[1].lower() == '.json':
                return ParamsLoaderJson(params)
            elif ext[1].lower() == '.py':
                return ParamsLoaderPy(ext[0])
            else:
                print("wrong parameters file type: {}".format(ext[1]))
                sys.exit(-1)
        elif type(params) is dict:
            return ParamsLoaderDict(params)
        elif params is None:
            return ParamsLoaderMem()

    def load(self):
        # update the parameters in the parameters classes: Conf, Knows, Settings
        # Conf
        for param in self.params['Conf']:
            if param[0:len('__')] != '__':
                setattr(Conf, param, self.params['Conf'][param])

        # Knows
        for param in self.params['Knows']:
            if param[0:len('__')] != '__':
                setattr(Knows, param, SMBool(self.params['Knows'][param][0],
                                             self.params['Knows'][param][1],
                                             ['{}'.format(param)]))

        # Settings
        for param in self.params['Settings']:
            if param[0:len('__')] != '__':
                setattr(Settings, param, self.params['Settings'][param])

    def dump(self, fileName):
        with open(fileName, 'w') as jsonFile:
            json.dump(self.params, jsonFile)

    def printToScreen(self):
        print("self.params: {}".format(self.params))

        print("loaded knows: ")
        for knows in Knows.__dict__:
            if knows[0:len('__')] != '__':
                print("{}: {}".format(knows, Knows.__dict__[knows]))
        print("loaded settings:")
        for setting in Settings.__dict__:
            if setting[0:len('__')] != '__':
                print("{}: {}".format(setting, Settings.__dict__[setting]))
        print("loaded conf:")
        for conf in Conf.__dict__:
            if conf[0:len('__')] != '__':
                print("{}: {}".format(conf, Conf.__dict__[conf]))


class ParamsLoaderJson(ParamsLoader):
    # when called from the test suite
    def __init__(self, jsonFileName):
        with open(jsonFileName) as jsonFile:
            self.params = json.load(jsonFile)

class ParamsLoaderPy(ParamsLoader):
    # for testing purpose
    def __init__(self, pyFileName):
        import importlib
        mod = importlib.import_module(pyFileName)
        conf = getattr(mod, 'Conf')
        knows = getattr(mod, 'Knows')
        settings = getattr(mod, 'Settings')
        self.params = {'Conf': {k: v for k, v in conf.__dict__.items() if k[0:len('__')] != '__'},
                       'Knows': {k: v for k, v in knows.__dict__.items() if k[0:len('__')] != '__'},
                       'Settings': {k: v for k, v in settings.__dict__.items() if k[0:len('__')] != '__'}}

class ParamsLoaderDict(ParamsLoader):
    # when called from the website
    def __init__(self, params):
        self.params = params

class ParamsLoaderMem(ParamsLoader):
    # to load the current classes from memory
    def __init__(self):
        self.params = {'Conf': {k: v for k, v in Conf.__dict__.items() if k[0:len('__')] != '__'},
                       'Knows': {k: v for k, v in Knows.__dict__.items() if k[0:len('__')] != '__'},
                       'Settings': {k: v for k, v in Settings.__dict__.items() if k[0:len('__')] != '__'}}

class DifficultyDisplayer:
    difficulties = {
        0 : 'baby',
        easy : 'easy',
        medium : 'medium',
        hard : 'hard',
        harder : 'very hard',
        hardcore : 'hardcore',
        mania : 'mania',
        mania*2 : 'god',
        mania*4 : 'samus'
    }

    def __init__(self, difficulty):
        self.difficulty = difficulty

    def text(self):
        if self.difficulty >= easy and self.difficulty < medium:
            difficultyText = self.difficulties[easy]
        elif self.difficulty >= medium and self.difficulty < hard:
            difficultyText = self.difficulties[medium]
        elif self.difficulty >= hard and self.difficulty < harder:
            difficultyText = self.difficulties[hard]
        elif self.difficulty >= harder and self.difficulty < hardcore:
            difficultyText = self.difficulties[harder]
        elif self.difficulty >= hardcore and self.difficulty < mania:
            difficultyText = self.difficulties[hardcore]
        else:
            difficultyText = self.difficulties[mania]

        return difficultyText

    def scale(self):
        previous = 0
        for d in sorted(self.difficulties):
            if self.difficulty >= d:
                previous = d
            else:
                displayString = self.difficulties[previous]
                displayString += ' '
                scale = d - previous
                pos = int(self.difficulty - previous)
                displayString += '-' * pos
                displayString += '^'
                displayString += '-' * (scale - pos)
                displayString += ' '
                displayString += self.difficulties[d]
                break

        return displayString

    def normalize(self):
        if self.difficulty == -1:
            return (None, None)

        previous = 0
        for d in sorted(self.difficulties):
            if self.difficulty >= d:
                previous = d
            else:
                baseDiff = self.difficulties[previous]
                normalized = int(5*float(self.difficulty - previous)/float(d - previous))
                break

        return (baseDiff, normalized)

    def percent(self):
        # return the difficulty as a percent
        if self.difficulty == -1:
            return -1
        elif self.difficulty in [0, easy]:
            return 0

        difficultiesPercent = {
            easy: 0,
            medium: 20,
            hard: 40,
            harder: 60,
            hardcore: 80,
            mania: 100,
            mania*2: 100,
            mania*4: 100
        }

        difficulty = self.difficulty if self.difficulty < mania else mania

        lower = 0
        for upper in sorted(self.difficulties):
            if self.difficulty >= upper:
                lower = upper
            else:
                lowerPercent = difficultiesPercent[lower]
                upperPercent = difficultiesPercent[upper]

                a = (upperPercent-lowerPercent)/float(upper-lower)
                b = lowerPercent - a * lower

                percent = int(difficulty * a + b)
                break

        return percent

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Random Metroid Solver")
    parser.add_argument('romFileName', help="the input rom")
    parser.add_argument('--param', '-p', help="the input parameters", nargs='+', default=None, dest='paramsFileName')

    parser.add_argument('--debug', '-d', help="activate debug logging", dest='debug', action='store_true')
    parser.add_argument('--difficultyTarget', '-t', help="the difficulty target that the solver will aim for", dest='difficultyTarget', nargs='?', default=None, type=int)
    parser.add_argument('--displayGeneratedPath', '-g', help="display the generated path (spoilers!)", dest='displayGeneratedPath', action='store_true')

    args = parser.parse_args()

    solver = Solver(rom=args.romFileName, params=args.paramsFileName, debug=args.debug)

    if args.difficultyTarget is not None:
        Conf.difficultyTarget = args.difficultyTarget

    Conf.displayGeneratedPath = args.displayGeneratedPath

    #solver.solveRom()
    diff = solver.solveRom()
    knowsUsed = solver.getKnowsUsed()
    print("{} : diff : {}".format(diff, args.romFileName))
    print("{} : knows Used : {}".format(len(knowsUsed), args.romFileName))
