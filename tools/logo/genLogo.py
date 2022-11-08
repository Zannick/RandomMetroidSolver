#!/usr/bin/python3

# start with title_log_sm.bmp, 184x64 pixels, 256 colors but only 16 used (15 colors + 1 transparency (first pixel is transparent)) (with gimp, add magenta background, resize to 184x64 without interpolation, export to bmp 16 bits x1 r5 g5 b5)
# use SnesGFX to convert title_log_sm.bmp to gfx title_logo_sm.bin and palette title_logo_sm.pal
#    format: 4bpp snes, tilemap: no tilemap output, colors: 16, palette: YY-CHR Palette
# export sm_0A80D8.GFX from vanilla rom using SMILE 3.0.94 (Tileset Editor -> Special GFX -> Title 2 -> Export Graphics)
# ./genLogo.py title_logo_sm.bin sm_0A80D8.GFX title_logo_sm.pal sm.sfc
# import sm_0A80D8.GFX into sm.sfc using SMILE 3.0.94 (Tileset Editor -> Special GFX -> Title 2 -> Import Graphics)
# generate ips

# we're in directory 'tools/', update sys.path
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(sys.path[0])))

from rom.rom import RealROM

# generated by SnesGFX (title_logo_sm.bin)
variagfx = sys.argv[1]
# extracted with smile (sm_0A80D8.GFX)
vanillagfx = sys.argv[2]
# generated by SnesGFX (title_logo_sm.pal)
variapal = sys.argv[3]
# vanilla ROM
vanillarom = sys.argv[4]

# tiles to move (8x8 or 16x16 (made of 4 8x8))
tiles = [
    {'src': 5*0x20, 'dst': 0*0x20, 'size': 16},
    {'src': 7*0x20, 'dst': 2*0x20, 'size': 16},
    {'src': 9*0x20, 'dst': 4*0x20, 'size': 16},
    {'src': 11*0x20, 'dst': 6*0x20, 'size': 16},
    {'src': 13*0x20, 'dst': 8*0x20, 'size': 16},
    {'src': 15*0x20+0*0x200, 'dst': 10*0x20+0*0x200, 'size': 8},
    {'src': 0*0x20+8*0x200, 'dst': 11*0x20+0*0x200, 'size': 8},
    {'src': 15*0x20+1*0x200, 'dst': 10*0x20+1*0x200, 'size': 8},
    {'src': 0*0x20+9*0x200, 'dst': 11*0x20+1*0x200, 'size': 8},

    {'src': 2*0x20+2*0x200, 'dst': 0*0x20+2*0x200, 'size': 16},
    {'src': 4*0x20+2*0x200, 'dst': 2*0x20+2*0x200, 'size': 16},
    {'src': 6*0x20+2*0x200, 'dst': 4*0x20+2*0x200, 'size': 16},
    {'src': 8*0x20+2*0x200, 'dst': 6*0x20+2*0x200, 'size': 16},
    {'src': 10*0x20+2*0x200, 'dst': 8*0x20+2*0x200, 'size': 16},
    {'src': 12*0x20+2*0x200, 'dst': 10*0x20+2*0x200, 'size': 16},
    {'src': 14*0x20+2*0x200, 'dst': 12*0x20+2*0x200, 'size': 16},
    {'src': 0*0x20+10*0x200, 'dst': 14*0x20+2*0x200, 'size': 16},

    {'src': 1*0x20+4*0x200, 'dst': 0*0x20+4*0x200, 'size': 16},
    {'src': 3*0x20+4*0x200, 'dst': 2*0x20+4*0x200, 'size': 16},
    {'src': 5*0x20+4*0x200, 'dst': 4*0x20+4*0x200, 'size': 16},
    {'src': 7*0x20+4*0x200, 'dst': 6*0x20+4*0x200, 'size': 16},
    {'src': 9*0x20+4*0x200, 'dst': 8*0x20+4*0x200, 'size': 16},
    {'src': 11*0x20+4*0x200, 'dst': 10*0x20+4*0x200, 'size': 16},
    {'src': 13*0x20+4*0x200, 'dst': 12*0x20+4*0x200, 'size': 16},
    {'src': 15*0x20+4*0x200, 'dst': 14*0x20+4*0x200, 'size': 8},
    {'src': 0*0x20+12*0x200, 'dst': 15*0x20+4*0x200, 'size': 8},
    {'src': 15*0x20+5*0x200, 'dst': 14*0x20+5*0x200, 'size': 8},
    {'src': 0*0x20+13*0x200, 'dst': 15*0x20+5*0x200, 'size': 8},

    {'src': 0*0x20+6*0x200, 'dst': 0*0x20+6*0x200, 'size': 16},
    {'src': 2*0x20+6*0x200, 'dst': 2*0x20+6*0x200, 'size': 16},
    {'src': 4*0x20+6*0x200, 'dst': 4*0x20+6*0x200, 'size': 16},
    {'src': 6*0x20+6*0x200, 'dst': 6*0x20+6*0x200, 'size': 16},
    {'src': 8*0x20+6*0x200, 'dst': 8*0x20+6*0x200, 'size': 16},
    {'src': 10*0x20+6*0x200, 'dst': 10*0x20+6*0x200, 'size': 16},
    {'src': 12*0x20+6*0x200, 'dst': 12*0x20+6*0x200, 'size': 16},
    {'src': 14*0x20+6*0x200, 'dst': 14*0x20+6*0x200, 'size': 16},

    {'src': 1*0x20+12*0x200, 'dst': 0*0x20+8*0x200, 'size': 16},
    {'src': 3*0x20+12*0x200, 'dst': 2*0x20+8*0x200, 'size': 16},
    {'src': 5*0x20+12*0x200, 'dst': 4*0x20+8*0x200, 'size': 16},
    {'src': 0*0x20+14*0x200, 'dst': 6*0x20+8*0x200, 'size': 16},
    {'src': 2*0x20+14*0x200, 'dst': 8*0x20+8*0x200, 'size': 16},
    {'src': 4*0x20+14*0x200, 'dst': 10*0x20+8*0x200, 'size': 16},

    {'src': 6*0x20+14*0x200, 'dst': 12*0x20+8*0x200, 'size': 16},

    {'src': 2*0x20+10*0x200, 'dst': 12*0x20+0*0x200, 'size': 16},

    {'src': 4*0x20+11*0x200, 'dst': 14*0x20+1*0x200, 'size': 8},
]


def move8tile(srcGfx, dstGfx, srcAddr, dstAddr):
    bytes = srcGfx.readBytes(0x20, srcAddr)
    dstGfx.writeBytes(bytes, 0x20, dstAddr)

def move16tile(srcGfx, dstGfx, srcAddr, dstAddr):
    move8tile(srcGfx, dstGfx, srcAddr, dstAddr)
    move8tile(srcGfx, dstGfx, srcAddr+0x20, dstAddr+0x20)
    move8tile(srcGfx, dstGfx, srcAddr+0x200, dstAddr+0x200)
    move8tile(srcGfx, dstGfx, srcAddr+0x200+0x20, dstAddr+0x200+0x20)


variagfx = RealROM(variagfx)
vanillagfx = RealROM(vanillagfx)

# move tiles to match vanilla layout
for tile in tiles:
    if tile['size'] == 16:
        move16tile(variagfx, vanillagfx, tile['src'], tile['dst'])
    else:
        move8tile(variagfx, vanillagfx, tile['src'], tile['dst'])

variagfx.close()
vanillagfx.close()

# update palette
variapal = RealROM(variapal)
vanillarom = RealROM(vanillarom)
palAddr = 0x661e9 + 10*0x20

def RGB_24_to_15(color_tuple):
    R_adj = int(color_tuple[0])//8
    G_adj = int(color_tuple[1])//8
    B_adj = int(color_tuple[2])//8

    c = B_adj * 1024 + G_adj * 32 + R_adj
    return (c)

def RGB_15_to_24(SNESColor):
    R = ((SNESColor      ) % 32) * 8
    G = ((SNESColor//32  ) % 32) * 8
    B = ((SNESColor//1024) % 32) * 8

    return (R,G,B)

variapal.seek(0x00)
vanillarom.seek(palAddr)
final = []
for i in range(16):
    r = variapal.readByte()
    g = variapal.readByte()
    b = variapal.readByte()
    final.append([r,g,b])
    color = RGB_24_to_15((r, g, b))
    vanillarom.writeWord(color)

# update logo fadein palettes
final.pop(0) # first color is not updated by the fadein
fadeinPaletteAddr = 0x6C6BE
for i in range(15):
    steps = [int(final[i][0]/8)+1, int(final[i][1]/8)+1, int(final[i][2]/8)+1]
    cur = [0, 0, 0]
    inc = [0, 0, 0]
    for s in range(6):
        for c in range(3):
            inc[c] += steps[c]
            if inc[c] >= 0x8:
                cur[c] += inc[c]
                inc[c] = 0
        color = RGB_24_to_15(cur)
        addr = fadeinPaletteAddr + i * 2 + s * 34
        vanillarom.writeWord(color, addr)

vanillarom.seek(0x6c78a)
for c in final:
    color = RGB_24_to_15(c)
    vanillarom.writeWord(color)

variapal.close()

# update oam for lower right sprite, update its size and y pos
oamAddr = 0x6079D+0x2
oam1 = vanillarom.readWord(oamAddr)
oam2 = vanillarom.readByte()
oam3 = vanillarom.readWord()

# replace size from 8x8 to 16x16
oam1 = 0xC200 + (oam1 & 0x00FF)
vanillarom.writeWord(oam1, oamAddr)

# set y to 16 like the other tiles on that row
oam2 = 16
vanillarom.writeByte(oam2, oamAddr+2)

# decrement tile number by 16, to have the tile start one line before
tileNumber = 140
oam3 = (oam3 & 0xFE00) + (tileNumber)
vanillarom.writeWord(oam3, oamAddr+3)


vanillarom.close()

