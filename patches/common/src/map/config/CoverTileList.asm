
;---------------------------------------------------------------------------------------------------
;|x|                                    COVER TILE LIST                                          |x|
;---------------------------------------------------------------------------------------------------
{
;The tile on the list will be replaced by this tile number, if the map has been loaded but not been explored.
; (disabled in VARIA, original data provided in comment)
ORG !Freespace_CoverTiles
CoverTileList:
!b #= 0
while !b <= $ff
        db !b
        !b #= !b+1
endif
}
	;; DB $00, $01, $02, $5C, $5C, $5C, $5C, $5C, $0A, $0A, $0A, $0A, $15, $15, $0E, $0F	;tile $00 - $0F
	;; DB $10, $11, $12, $15, $15, $15, $15, $15, $1A, $1A, $1A, $52, $15, $15, $15, $1F	;tile $10 - $1F
	;; DB $20, $21, $21, $25, $25, $25, $25, $25, $25, $25, $25, $25, $25, $0A, $0A, $0A	;tile $20 - $2F
	;; DB $30, $31, $32, $33, $34, $35, $36, $37, $38, $39, $3A, $3B, $3C, $3D, $3E, $3F	;tile $30 - $3F
	;; DB $40, $41, $42, $43, $44, $45, $46, $47, $48, $49, $4A, $4B, $4C, $5C, $5C, $5C	;tile $40 - $4F
	;; DB $52, $52, $52, $52, $54, $55, $57, $57, $57, $59, $5A, $5C, $5C, $5C, $5C, $5C	;tile $50 - $5F
	;; DB $62, $62, $62, $62, $64, $65, $66, $67, $68, $69, $02, $5C, $5C, $25, $0A, $52	;tile $60 - $6F
	;; DB $72, $72, $72, $72, $74, $75, $52, $62, $02, $79, $7A, $7B, $7C, $7D, $7E, $7F	;tile $70 - $7F
	;; DB $80, $81, $82, $83, $84, $85, $86, $87, $88, $89, $8A, $8B, $8C, $8D, $8E, $8F	;tile $80 - $8F
	;; DB $0A, $0A, $0A, $93, $94, $95, $96, $97, $98, $99, $9A, $9B, $9C, $9D, $9E, $9F	;tile $90 - $9F
	;; DB $A0, $A1, $A2, $A3, $A4, $A5, $A6, $A7, $A8, $A9, $AA, $AB, $AC, $AD, $AE, $AF	;tile $A0 - $AF
	;; DB $B0, $B1, $B2, $B3, $B4, $5C, $5C, $5C, $B8, $B9, $BA, $BB, $BC, $BD, $BE, $BF	;tile $B0 - $BF
	;; DB $C0, $C1, $C2, $C3, $C4, $5C, $5C, $5C, $C8, $C9, $CA, $CB, $CC, $CD, $CE, $CF	;tile $C0 - $CF
	;; DB $D0, $D1, $D2, $D3, $D4, $D5, $D6, $D7, $D8, $D9, $DA, $DB, $DC, $DD, $DE, $DF	;tile $D0 - $DF
	;; DB $E0, $E1, $E2, $E3, $E4, $E5, $E6, $E7, $E8, $E9, $EA, $EB, $EC, $ED, $EE, $EF	;tile $E0 - $EF
	;; DB $F0, $F1, $F2, $F3, $F4, $F5, $F6, $F7, $F8, $F9, $FA, $FB, $FC, $FD, $FE, $FF	;tile $F0 - $FF
