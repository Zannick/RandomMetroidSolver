
import copy, log

from smboolmanager import SMBoolManager
from collections import Counter

def getItemListStr(items):
    return str(dict(Counter([item['Type'] for item in items])))

def getLocListStr(locs):
    return str([loc['Name'] for loc in locs])

class ItemLocContainer(object):
    def __init__(self, sm, itemPool, locations):
        self.sm = sm
        self.itemLocations = []
        self.unusedLocations = locations
        self.currentItems = []
        self.itemPool = itemPool
        self.itemPoolBackup = None
        self.log = log.get('ItemLocContainer')

    def __copy__(self):
        locs = [copy.deepcopy(loc) for loc in self.unusedLocations]
        ret = ItemLocContainer(SMBoolManager(),
                               self.itemPool[:],
                               locs)
        ret.currentItems = self.currentItems[:]
        for il in self.itemLocations:
            ilCpy = {
                'Item': il['Item'],
                'Location': copy.deepcopy(il['Location'])
            }
            ret.itemLocations.append(ilCpy)
        ret.sm.addItems([item['Type'] for item in ret.currentItems])
        return ret

    def dump(self):
        return "ItemPool: %s\nLocPool: %s\nCollected: %s" % (getItemListStr(self.itemPool), getLocListStr(self.unusedLocations), getItemListStr(self.currentItems))

    # temporarily restrict item pool to items fulfilling predicate
    def restrictItemPool(self, predicate):
        assert self.itemPoolBackup is None, "Item pool already restricted"
        self.itemPoolBackup = self.itemPool
        self.itemPool = [item for item in self.itemPoolBackup if predicate(item)]
        self.log.debug("restrictItemPool: "+getItemListStr(self.itemPool))

    # remove a placed restriction
    def unrestrictItemPool(self):
        assert self.itemPoolBackup is not None, "No pool restriction to remove"
        self.itemPool = self.itemPoolBackup
        self.itemPoolBackup = None
        self.log.debug("unrestrictItemPool: "+getItemListStr(self.itemPool))

    def extractLocs(self, locs):
        ret = []
        for loc in locs:
            ret.append(next(l for l in self.unusedLocations if l['Name'] == loc['Name']))
        return ret

    def collect(self, itemLocation, pickup=True):
        item = itemLocation['Item']
        location = itemLocation['Location']
        if pickup == True:
            self.currentItems.append(item)
            self.sm.addItem(item['Type'])
        self.unusedLocations.remove(location)
        self.itemLocations.append(itemLocation)
        itemToRemove = self.getNextItemInPool(item['Type'])
        self.itemPool.remove(itemToRemove)
        if self.itemPoolBackup is not None:
            self.itemPoolBackup.remove(itemToRemove)

    def isPoolEmpty(self):
        return len(self.itemPool) == 0
        
    def getNextItemInPool(self, t):
        return next((item for item in self.itemPool if item['Type'] == t), None)

    def hasItemTypeInPool(self, t):
        return any(item['Type'] == t for item in self.itemPool)

    def hasItemCategoryInPool(self, cat):
        return any(item['Category'] == cat for item in self.itemPool)

    def getNextItemInPoolFromCategory(self, cat):
        return next((item for item in self.itemPool if item['Category'] == cat), None)

    def getAllItemsInPoolFromCategory(self, cat):
        return [item for item in self.itemPool if item['Category'] == cat]
    
    def countItemTypeInPool(self, t):
        return len([item for item in self.itemPool if item['Type'] == t])

    def getPoolDict(self):
        poolDict = {}
        for item in self.itemPool:
            if item['Type'] not in poolDict:
                poolDict[item['Type']] = []
            poolDict[item['Type']].append(item)
        return poolDict

    def getLocs(self, predicate):
        return [loc for loc in self.unusedLocations if predicate(loc) == True]

    def getItems(self, predicate):
        return [item for item in self.itemPool if predicate(item) == True]

    def getUsedLocs(self, predicate):
        return [il['Location'] for il in self.itemLocations if predicate(il['Location']) == True]

    def getCollectedItems(self, predicate):
        return [item for item in self.currentItems if predicate(item) == True]
