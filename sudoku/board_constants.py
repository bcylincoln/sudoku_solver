GAME_SIZE = 9

BOX_0 = frozenset([0, 1, 2, 9, 10, 11, 18, 19, 20])
BOX_1 = frozenset([3, 4, 5, 12, 13, 14, 21, 22, 23])
BOX_2 = frozenset([6, 7, 8, 15, 16, 17, 24, 25, 26])
BOX_3 = frozenset([27, 28, 29, 36, 37, 38, 45, 46, 47])
BOX_4 = frozenset([30, 31, 32, 39, 40, 41, 48, 49, 50])
BOX_5 = frozenset([33, 34, 35, 42, 43, 44, 51, 52, 53])
BOX_6 = frozenset([54, 55, 56, 63, 64, 65, 72, 73, 74])
BOX_7 = frozenset([57, 58, 59, 66, 67, 68, 75, 76, 77])
BOX_8 = frozenset([60, 61, 62, 69, 70, 71, 78, 79, 80])

BOX_LIST = [
	BOX_0,
	BOX_1,
	BOX_2,
	BOX_3,
	BOX_4,
	BOX_5,
	BOX_6,
	BOX_7,
	BOX_8
]

ROW_LIST = []
COL_LIST = []

for i in range(GAME_SIZE):
	row_indices = range(9 * i, (9 * i) + 9)
	ROW_LIST.append(frozenset(row_indices))

for i in range(GAME_SIZE):
	col_indices = range(i, 81, 9)
	COL_LIST.append(frozenset(col_indices))

GRID_01 = "200080300"+\
"060070084"+\
"030500209"+\
"000105408"+\
"000000000"+\
"402706000"+\
"301007040"+\
"720040060"+\
"004010003"

GRID_49 = '000003017'+\
'015009008'+\
'060000000'+\
'100007000'+\
'009000200'+\
'000500004'+\
'000000020'+\
'500600340'+\
'340200000'