#!/usr/bin/python3

import sys, os

sys.path.append(os.path.dirname(sys.path[0]))

from rom.rom_patches import _layoutIPS, _layoutAreaComfort, definitions
from rom.rom import RealROM, snes_to_pc, pc_to_snes
from rom.ips import IPS_Patch
from patches.common.patches import patches as commonPatchDict
from collections import defaultdict

variaTweaks = definitions["common"]["variaTweaks"]['ips']
vanilla = RealROM("vanilla.sfc")

used = defaultdict(list)

def getAddrAndValue(flavor, ips):
    if flavor == "common" and ips in commonPatchDict:
        patchDict = commonPatchDict[ips]
    else:
        patchPath = f"patches/{flavor}/ips/{ips}"
        if os.path.exists(patchPath):            
            patchDict = IPS_Patch.load(patchPath).toDict()
        else:
            return 0, 0
    for addr, bytez in patchDict.items():
        address = addr
        for b in bytez:
            if b != vanilla.readByte(address):
                if address in used and b in used[address]:
                    continue
                used[address].append(b)
                return address, b
            address += 1
    assert False, "Could not find addr/val for %s in flavor %s" % (ips, flavor)

def printPatchDefs(grp, patches, flavor):
    print(f"# {grp}, {flavor}")
    for ips in patches:
        addr, val = getAddrAndValue(flavor, ips)
        if addr == 0:
            continue
        print("'%s': {" % os.path.splitext(ips)[0])
        print("    'address': 0x%x, 'value': 0x%x," % (addr, val))
        print("    'desc': '',")
        print("    'ips': ['%s']," % ips)
        print("    'plms': [],")
        print("    'logic': []")
        print("}")
    print("\n")

categories = {
    'Anti-softlock layout patches': (["common", "vanilla", "mirror"], _layoutIPS),
    'Area comfort patches': (["vanilla", "mirror"], _layoutAreaComfort),
    'VARIA Tweaks': (["common"], variaTweaks)
}

for cat, entry in categories.items():
    flavors, patches = entry
    for flavor in flavors:
        printPatchDefs(cat, patches, flavor)