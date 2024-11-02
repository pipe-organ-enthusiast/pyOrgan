# A4 Frequency:
FREQUENCY_A4: float = 440.0

###############################################################################
# Musical Notes
###############################################################################
NOTES: tuple[str] = (
    "C2", 
    "C#2", 
    "D2", 
    "D#2", 
    "E2", 
    "F2", 
    "F#2", 
    "G2", 
    "G#2", 
    "A2", 
    "A#2",
    "B2", 
    "C3", 
    "C#3", 
    "D3", 
    "D#3", 
    "E3", 
    "F3", 
    "F#3", 
    "G3", 
    "G#3", 
    "A3",
    "A#3", 
    "B3", 
    "C4", 
    "C#4", 
    "D4", 
    "D#4", 
    "E4", 
    "F4", 
    "F#4", 
    "G4", 
    "G#4",
    "A4", 
    "A#4", 
    "B4", 
    "C5", 
    "C#5", 
    "D5", 
    "D#5", 
    "E5", 
    "F5", 
    "F#5", 
    "G5",
    "G#5", 
    "A5", 
    "A#5", 
    "B5", 
    "C6", 
    "C#6", 
    "D6", 
    "D#6", 
    "E6", 
    "F6", 
    "F#6",
    "G6", 
    "G#6", 
    "A6", 
    "A#6", 
    "B6", 
    "C7"
)

NOTE_TO_MIDI: dict = {
    "C2": 36, 
    "C#2": 37, 
    "D2": 38, 
    "D#2": 39, 
    "E2": 40, 
    "F2": 41, 
    "F#2": 42,
    "G2": 43, 
    "G#2": 44, 
    "A2": 45, 
    "A#2": 46, 
    "B2": 47, 
    "C3": 48, 
    "C#3": 49,
    "D3": 50, 
    "D#3": 51, 
    "E3": 52, 
    "F3": 53, 
    "F#3": 54, 
    "G3": 55, 
    "G#3": 56,
    "A3": 57, 
    "A#3": 58, 
    "B3": 59, 
    "C4": 60, 
    "C#4": 61, 
    "D4": 62, 
    "D#4": 63,
    "E4": 64, 
    "F4": 65, 
    "F#4": 66, 
    "G4": 67, 
    "G#4": 68, 
    "A4": 69, 
    "A#4": 70,
    "B4": 71, 
    "C5": 72, 
    "C#5": 73, 
    "D5": 74, 
    "D#5": 75, 
    "E5": 76, 
    "F5": 77,
    "F#5": 78, 
    "G5": 79, 
    "G#5": 80, 
    "A5": 81, 
    "A#5": 82, 
    "B5": 83, 
    "C6": 84,
    "C#6": 85, 
    "D6": 86, 
    "D#6": 87, 
    "E6": 88, 
    "F6": 89, 
    "F#6": 90, 
    "G6": 91,
    "G#6": 92, 
    "A6": 93, 
    "A#6": 94, 
    "B6": 95, 
    "C7": 96
}

MIDI_TO_NOTE: dict = {
    36: "C2", 
    37: "C#2", 
    38: "D2", 
    39: "D#2", 
    40: "E2", 
    41: "F2", 
    42: "F#2",
    43: "G2", 
    44: "G#2", 
    45: "A2", 
    46: "A#2", 
    47: "B2", 
    48: "C3", 
    49: "C#3",
    50: "D3", 
    51: "D#3", 
    52: "E3", 
    53: "F3", 
    54: "F#3", 
    55: "G3", 
    56: "G#3",
    57: "A3", 
    58: "A#3", 
    59: "B3", 
    60: "C4", 
    61: "C#4", 
    62: "D4", 
    63: "D#4",
    64: "E4", 
    65: "F4", 
    66: "F#4", 
    67: "G4", 
    68: "G#4", 
    69: "A4", 
    70: "A#4",
    71: "B4", 
    72: "C5", 
    73: "C#5", 
    74: "D5", 
    75: "D#5", 
    76: "E5", 
    77: "F5",
    78: "F#5", 
    79: "G5", 
    80: "G#5", 
    81: "A5", 
    82: "A#5", 
    83: "B5", 
    84: "C6",
    85: "C#6", 
    86: "D6", 
    87: "D#6", 
    88: "E6", 
    89: "F6", 
    90: "F#6", 
    91: "G6",
    92: "G#6", 
    93: "A6", 
    94: "A#6", 
    95: "B6", 
    96: "C7"
}

###############################################################################
# Pipe Construction
###############################################################################
PIPE_TYPES: tuple[str] = (
    "OPEN",
    "CLOSED"
)

###############################################################################
# Rank Sizes
###############################################################################
RANK_SIZES: tuple[str] = (
    "64'", 
    "32'", 
    "21 1/3'", 
    "16'", 
    "12 4/5'", 
    "10 2/3'", 
    "9 1/7'", 
    "8'", 
    "7 1/9'", 
    "6 2/5'", 
    "5 9/11'", 
    "5 1/3'", 
    "4 12/13'", 
    "4 4/7'", 
    "4 4/15'",
    "4'", 
    "3 13/17'", 
    "3 5/9'", 
    "3 7/19'", 
    "3 1/5'", 
    "2 10/11'", 
    "2 18/23'",
    "2 2/3'", 
    "2 14/25'", 
    "2 6/13'", 
    "2 2/7'", 
    "2 2/15'", 
    "2'", 
    "1 15/17'",
    "1 7/9'", 
    "1 13/19'", 
    "1 3/5'", 
    "1 5/11'", 
    "1 9/23'", 
    "1 1/3'", 
    "1 7/25'",
    "1 3/13'", 
    "1 1/7'", 
    "1 1/15'", 
    "1'", 
    "16/17'", 
    "8/9'", 
    "16/19'", 
    "4/5'",
    "8/11'", 
    "16/23'", 
    "2/3'", 
    "16/25'", 
    "8/13'", 
    "4/7'", 
    "8/15'", 
    "1/2'",
    "8/17'", 
    "4/9'", 
    "8/19'", 
    "2/5'", 
    "4/11'", 
    "8/23'", 
    "1/3'", 
    "8/25'",
    "4/13'", 
    "2/7'", 
    "4/15'", 
    "1/4'", 
    "4/17'", 
    "2/9'", 
    "4/19'", 
    "1/5'",
    "2/11'", 
    "4/23'", 
    "1/6'", 
    "4/25'", 
    "2/13'", 
    "1/7'", 
    "2/15'", 
    "1/8'",
    "1/12'", 
    "1/16'"
)

RANK_SERIES_64: tuple[str] = (
    "64'", 
    "32'", 
    "21 1/3'", 
    "16'", 
    "12 4/5'", 
    "10 2/3'", 
    "9 1/7'", 
    "8'",
    "7 1/9'", 
    "6 2/5'", 
    "5 9/11'", 
    "5 1/3'", 
    "4 12/13'", 
    "4 4/7'", 
    "4 4/15'",
    "4'", 
    "3 13/17'", 
    "3 5/9'", 
    "3 7/19", 
    "3 1/5'", 
    "2 10/11'", 
    "2 18/23'",
    "2 2/3'", 
    "2 14/25'", 
    "2 6/13'", 
    "2 2/7'", 
    "2 2/15'", 
    "2'", 
    "1 1/3'", 
    "1'"
)

RANK_SERIES_32: tuple[str] = (
    "32'", 
    "16'", 
    "10 2/3'", 
    "8'", 
    "6 2/5'", 
    "5 1/3'", 
    "4 4/7'", 
    "4'",
    "3 5/9'", 
    "3 1/5'", 
    "2 10/11'", 
    "2 2/3'", 
    "2 6/13'", 
    "2 2/7'", 
    "2 2/15'",
    "2'", 
    "1 15/17'", 
    "1 7/9'", 
    "1 13/19'", 
    "1 3/5'", 
    "1 5/11'", 
    "1 9/23'",
    "1 1/3'", 
    "1 7/25'", 
    "1 3/13'", 
    "1 1/7'", 
    "1 1/15'", 
    "1'", 
    "2/3'", 
    "1/2'"
)

RANK_SERIES_16: tuple[str] = (
    "16'", 
    "8'", 
    "5 1/3'", 
    "4'", 
    "3 1/5'", 
    "2 2/3'", 
    "2 2/7'", 
    "2'", 
    "1 7/9'",
    "1 3/5'", 
    "1 5/11'", 
    "1 1/3'", 
    "1 3/13'", 
    "1 1/7'", 
    "1 1/15'", 
    "1'",
    "16/17'", 
    "8/9'", 
    "16/19'", 
    "4/5'", 
    "8/11'", 
    "16/23'", 
    "2/3'", 
    "16/25'",
    "8/13'", 
    "4/7'", 
    "8/15'", 
    "1/2'", 
    "1/3'", 
    "1/4'" 
)

RANK_SERIES_8: tuple[str] = (
    "8'", 
    "4'", 
    "2 2/3'", 
    "2'", 
    "1 3/5'", 
    "1 1/3'", 
    "1 1/7'", 
    "1'", 
    "8/9'",
    "4/5'", 
    "8/11'", 
    "2/3'", 
    "8/13'", 
    "4/7'", 
    "8/15'", 
    "1/2'", 
    "8/17'", 
    "4/9'",
    "8/19'", 
    "2/5'", 
    "4/11'", 
    "8/23'", 
    "1/3'", 
    "8/25'", 
    "4/13'", 
    "2/7'",
    "4/15'", 
    "1/4'", 
    "1/6'", 
    "1/8'"
)

RANK_SERIES_4: tuple[str] = (
    "4'", 
    "2'", 
    "1 1/3'", 
    "1'", 
    "4/5'", 
    "2/3'", 
    "4/7'", 
    "1/2'", 
    "4/9'", 
    "2/5'",
    "4/11'", 
    "1/3'", 
    "4/13'", 
    "2/7'", 
    "4/15'", 
    "1/4'", 
    "4/17'", 
    "2/9'",
    "4/19'", 
    "1/5'", 
    "2/11'", 
    "4/23'", 
    "1/6'", 
    "4/25'", 
    "2/13'", 
    "1/7'",
    "2/15'", 
    "1/8'", 
    "1/12'", 
    "1/16'"
)

RANK_TO_NOTE: dict = {
    "64'": "C-1", 
    "32'": "C0", 
    "21 1/3'": "G0", 
    "16'": "C1", 
    "12 4/5'": "E1",
    "10 2/3'": "G1", 
    "9 1/7'": "A#1", 
    "8'": "C2", 
    "7 1/9'": "D2",
    "6 2/5'": "E2", 
    "5 9/11'": "F2", 
    "5 1/3'": "G2", 
    "4 12/13'": "A2",
    "4 4/7'": "A#2", 
    "4 4/15'": "B2", 
    "4'": "C3", 
    "3 13/17'": "C#3",
    "3 5/9'": "D3", 
    "3 7/19'": "D#3", 
    "3 1/5'": "E3", 
    "2 10/11'": "F3",
    "2 18/23'": "F#3", 
    "2 2/3'": "G3", 
    "2 14/25'": "G#3", 
    "2 6/13'": "A3",
    "2 2/7'": "A#3", 
    "2 2/15'": "B3", 
    "2'": "C4", 
    "1 15/17'": "C#4",
    "1 7/9'": "D4", 
    "1 13/19'": "D#4", 
    "1 3/5'": "E4", 
    "1 5/11'": "F4",
    "1 9/23'": "F#4", 
    "1 1/3'": "G4", 
    "1 7/25'": "G#4", 
    "1 3/13'": "A4",
    "1 1/7'": "A#4", 
    "1 1/15'": "B4", 
    "1'": "C5", 
    "16/17'": "C#5",
    "8/9'": "D5", 
    "16/19'": "D#5", 
    "4/5'": "E5", "8/11'": "F5",
    "16/23'": "F#5", 
    "2/3'": "G5", 
    "16/25'": "G#5", 
    "8/13'": "A5",
    "4/7'": "A#5", 
    "8/15'": "B5", 
    "1/2'": "C6", 
    "8/17'": "C#6", 
    "4/9'": "D6",
    "8/19'": "D#6", 
    "2/5'": "E6", 
    "4/11'": "F6", 
    "8/23'": "F#6", 
    "1/3'": "G6",
    "8/25'": "G#6", 
    "4/13'": "A6", 
    "2/7'": "A#6", 
    "4/15'": "B6", 
    "1/4'": "C7",
    "4/17'": "C#7", 
    "2/9'": "D7", 
    "4/19'": "D#7", 
    "1/5'": "E7", 
    "2/11'": "F7",
    "4/23'": "F#7", 
    "1/6'": "G7", 
    "4/25'": "G#7", 
    "2/13'": "A7", 
    "1/7'": "A#7",
    "2/15'": "B7", 
    "1/8'": "C8", 
    "1/12'": "G8", 
    "1/16'": "C9"
}

RANK_MIDI_OFFSET: dict = {
    "64'": -36,
    "32'": -24,
    "21 1/3'": -17,
    "16'": -12,
    "12 4/5'": -8,
    "10 2/3'": -5,
    "9 1/7'": -2,
    "8'": 0,
    "7 1/9'": 2,
    "6 2/5'": 4,
    "5 9/11'": 5,
    "5 1/3'": 7,
    "4 12/13'": 9,
    "4 4/7'": 10,
    "4 4/15'": 11,
    "4'": 12,
    "3 13/17'": 13,
    "3 5/9'": 14,
    "3 7/19'": 15,
    "3 1/5'": 16,
    "2 10/11'": 17,
    "2 18/23'": 18,
    "2 2/3'": 19,
    "2 14/25'": 20,
    "2 6/13'": 21,
    "2 2/7'": 22,
    "2 2/15'": 23,
    "2'": 24,
    "1 15/17'": 25,
    "1 7/9'": 26,
    "1 13/19'": 27,
    "1 3/5'": 28,
    "1 5/11'": 29,
    "1 9/23'": 30,
    "1 1/3'": 31,
    "1 7/25'": 32,
    "1 3/13'": 33,
    "1 1/7'": 34,
    "1 1/15'": 35,
    "1'": 36,
    "16/17'": 37,
    "8/9'": 38,
    "16/19'": 39,
    "4/5'": 40,
    "8/11'": 41,
    "16/23'": 42,
    "2/3'": 43,
    "16/25'": 44,
    "8/13'": 45,
    "4/7'": 46,
    "8/15'": 47,
    "1/2'": 48,
    "8/17'": 49,
    "4/9'": 50,
    "8/19'": 51,
    "2/5'": 52,
    "4/11'": 53,
    "8/23'": 54,
    "1/3'": 55,
    "8/25'": 56,
    "4/13'": 57,
    "2/7'": 58,
    "4/15'": 59,
    "1/4'": 60,
    "4/17'": 61,
    "2/9'": 62,
    "4/19'": 63,
    "1/5'": 64,
    "2/11'": 65,
    "4/23'": 66,
    "1/6'": 67,
    "4/25'": 68,
    "2/13'": 69,
    "1/7'": 70,
    "2/15'": 71,
    "1/8'": 72,
    "1/12'": 79,
    "1/16'": 84
}

###############################################################################
# Stops
###############################################################################
STOP_FAMILIES: tuple[str] = (
    "FOUNDATION",
    "FLUTE",
    "STRING",
    "REED",
    #"PERCUSSION",
    "MIXTURE"
)

STOP_NAMES: tuple[str] = (
    "ACOUSTIC BASS",  # MIXTURE | FOUNDATION
    "ACUTA",  # MIXTURE
    "AELODICON",  # REED
    "AEOLIAN",  # STRING
    "AEOLINA",  # STRING
    "AEOLINE",  # STRING
    "AEOLINE CÉLESTE",  # STRING
    "AEOLINE REED",  # REED
    "AEOLODICON",  # REED
    "AEQUAL",  # FOUNDATION
    "AEQUAL-GEMSHORN",  # FOUNDATION
    "AEQUALE",  # FOUNDATION
    "AEQUALPRINZIPAL",  # FOUNDATION
    #"AKKORDGLOCKEN",  # NOT A TRADITIONAL STOP - MAINLY FOUND ON OLDER ORGANS 
    "AKUTA",  # MIXTURE
    "ALODICON",  # REED
    "AMOROSA",  # FLUTE
    "AMOROSO",  # FLUTE
    "ANGELICA",  # REED
    "ANGENEHMGEDECKT",  # FLUTE
    "ANGLE HORN",  # REED
    "ANTHROPOGLOSSA",  # REED
    "ÄOLINE",  # REED
    "APFELREGAL",  # REED
    "ÄQUAL",  # FOUNDATION
    "AQUAL GEMSHORN",  # FOUNDATION
    "ASSAT",  # FLUTE
    #"AVICINIUM",  # NOT A TRADITIONAL STOP - SIMILAR TO BIRD WHISTLE
    "BAARPFEIFE",  # REED
    "BAARPIJP",  # FLUTE
    "BAARPYP",  # REED
    "BACHFLÖTE",  # FLUTE
    "BÄHRPFEIFE",  # REED
    "BAIXO",  # REED
    "BAIXONILHO",  # REED
    "BAJETE",  # REED
    "BAJON",  # REED
    "BAJONCILLO",  # REED
    "BAJONCILLO Y CLARÍN",  # REED 
    "BALLAD HORN",  # REED
    "BÄRBOMMER",  # REED
    "BARDONE",  # FLUTE
    "BARDUEN",  # FLUTE
    "BAREM",  # FLUTE
    "BARITONE",  # REED
    "BARITONO",  # REED
    "BÄRPFEIFE",  # REED
    "BÄRPIPE",  # REED
    "BARYPHON", # REED
    "BARYPHONE",  # REED
    "BARYTON",  # REED
    "BARYTONE",  # REED
    "BASS",  # FOUNDATION
    "BASS-BOMMER",  # REED
    "BASS CLARINET",  # REED
    "BASS CLARIONET",  # REED
    #"BASS DRUM",  # PERCUSSION
    "BASS FLUTE",  # FLUTE
    "BASS HORN",  # REED
    "BASS-POMMER",  # REED
    "BASS SAXOPHONE",  # REED
    "BASS SOLO STRING",  # STRING
    "BASS STRING",  # STRING
    "BASS TROMBONE",  # REED
    "BASS TUBA",  # REED
    "BASS VIOL",  # STRING
    "BASS VIOLIN",  # STRING
    "BASSANELLI",  # REED
    "BASSANELLO",  # REED
    "BASSBRUMMER",  # FLUTE
    "BASSE ACOUSTIQUE",  # FOUNDATION
    "BASS CONTRE",  # STRING
    "BASSE DE CHORMORNE",  # REED
    #"BASSE DE CROMHORNE",  # NAME OF REGISTRATION
    "BASSE DE VIOLE",  # STRING
    "BASSET",  # FLUTE
    "BASSET HORN",  # REED
    "BASSETHORN",  # REED
    "BASSETTHORN",  # REED
    "BASSETTO",  # FLUTE
    "BASSFLÖTE",  # FLUTE
    "BASSKORNETT",  # REED
    "BASSO PROFUNDO",  # FOUNDATION
    "BASSON",  # REED
    "BASSON-HAUTBOIS",  # REED 
    "BASSONELL",  # REED
    "BASSOON",  # REED
    "BASSOON REGAL",  # REED
    "BASSPOSAUNE",  # REED
    "BASSTUBA",  # REED
    "BASSZINK",  # MIXTURE
    "BASUN",  # REED
    "BAUERFLÖT",  # FLUTE
    "BAUERFLÖTBASS",  # FLUTE
    "BAUERFLÖTE",  # FLUTE
    "BAUERFLÖTENBASS",  # FLUTE
    "BAUERLEIN",  # FLUTE
    "BAUERLIN",  # FLUTE
    "BAUERNFLÖTE",  # FLUTE
    "BAUERNFLÖTENBASS",  # FLUTE
    "BAUERNPFEIFE",  # FLUTE
    "BAUERNROHRFLÖTE",  # FLUTE
    "BAUERPFEIFE",  # FLUTE
    "BAURPFEIFE",  # FLUTE
    "BAXONCILLO",  # REED
    "BAZUIN",  # REED
    "BEARDED GAMBA",  # STRING
    "BEERPFEIFE",  # REED
    "BEERPIPE",  # REED
    "BEHRPFEIFE", # REED
    "BELL CLARINET",  # REED
    "BELL DIAPASON",  # FLUTE
    "BELL FLUTE",  # FLUTE
    "BELL GAMBA",  # STRING
    #"BELLS",  # PERCUSSION
    "BIBELREGAL",  # REED
    "BIBLE-REGAL",  # REED
    "BIFARA",  # MIXTURE
    "BIFFARO",  # MIXTURE
    "BIFFRA",  # MIXTURE
    "BIFFURA",  # MIXTURE
    "BIFRA",  # MIXTURE
    #"BIRD WHISTLE",  # NOT A TRADITIONAL STOP
    "BLOCK FLUTE",  # FLUTE 
    "BLOCKFLÖT",  # FLUTE
    "BLOCKFLÖTE",  # FLUTE
    "BLOCKFLÖTENBASS",  # FLUTE
    "BLOCKPFEIFE",  # FLUTE
    "BLOCKPIPE",  # FLUTE
    "BLOKFLØJTE",  # FLUTE
    "BLOCKFLUIT",  # FLUTE
    "BOCKFLÖTE",  # FLUTE
    "BOEHM FLUTE",  # FLUTE
    "BOEHMFLÖTE",  # FLUTE
    "BOEHMISCHEFLÖTE",  # FLUTE
    "BOIS CELESTE",  # FLUTE
    "BOKFLÖTE",  # FLUTE
    "BOMBARD",  # REED
    "BOMBARD QUINT",  # REED
    "BOMBARDA",  # REED
    "BOMBARDE",  # REED
    "BOMBARDE EN CHAMADE",  # REED
    "BOMBARDE QUINTE",  # REED
    "BOMBARDO",  # REED
    "BOMBARDON",  # REED
    "BOMBARDONE",  # REED
    "BOMBART",  # REED
    "BOMHARD",  # REED
    "BOMMER",  # REED
    "BORDÓN",  # FLUTE
    "BORDONCINO",  # FLUTE
    "BORDONE",  # FLUTE
    "BORDONECHO",  # FLUTE
    "BORDUN",  # FLUTE
    "BORDUN-SUBBASS",  # FLUTE
    "BORDUNA",  # FLUTE
    "BORDUNAL",  # FLUTE
    "BORDUNALFLÖTE",  # FLUTE
    "BÖTZE",  # REED
    "BOURDON",  # FLUTE
    "BOURDON À CHEMINÉE",  # FLUTE 
    "BOURDON DOUX",  # FLUTE
    "BOURDONALFLÖTE",  # FLUTE
    "BOURDONECHO",  # FLUTE
    "BRASS REGAL",  # REED
    "BRASS SAXOPHONE",  # REED
    "BRASS TRUMPET",  # REED
    "BRATSCHE",  # STRING
    "BRUMHORN",  # REED
    "BRUMMBASS",  # FLUTE
    "BRUMMHORN",  # REED
    "BUCCINA",  # REED
    "BUCCINE",  # REED
    "BURDO",  # FLUTE
    "BUZAIN",  # REED
    "CAMPANA",  # FLUTE
    "CAMPANELLA",  # FLUTE
    "CAMPANELLI",  # FLUTE
    "CAMPANELLO",  # FLUTE
    #"CAMPANETTA",  # PERCUSSION
    "CAMPANETTE",  # FLUTE
    "CAMPANILLA",  # FLUTE
    #"CANARY",  # TOY
    "CANTUS FLUTE", # FLUTE
    "CARILLON",  # PRINCIPAL
    "CART",  # FLUTE
    #"CASTANETS",  # PERCUSSION
    "CEDIRNE",  # STRING
    #"CELESTA",  # PERCUSSION
    "CELESTIANA",  # FLUTE
    "CELESTINA",  # FLUTE
    "CELESTINA CÉLESTE",  # FLUTE
    "CELESTINA VIOL",  # STRING
    "CELLO",  # STRING
    "CELLO CELESTE",  # STRING
    "CELLO DIAPASON",  # STRING
    "CELLO DOLCE",  # STRING
    "CELLO POMPOSA",  # STRING
    "CELLO VIOLIN",  # STRING
    "CEMBALO",  # MIXTURE
    "CEMBALOREGAL",  # REED
    "CHALEMIE",  # REED
    "CHALEMOY",  # REED
    "CHALMEAUX",  # REED
    "CHALMOUII",  # REED
    "CHALUMEAU",  # REED
    "CHEIO",  # MIXTURE
    #"CHIMES"  # PERCUSSION
    "CHIMNEY FLUTE",  # FLUTE
    #"CHINESE BLOCK",  # PERCUSSION
    #"CHINESE GONG",  # PERCUSSION
    "CHIRIMÍA",  # REED
    "CHORAL",  # MIXTURE
    "CHORALBASS",  # FOUNDATION
    "CHORALBASSET",  # FOUNDATION
    "CHORALFLÖTE",  # FLUTE
    "CHORALMIXTUR",  # MIXTURE
    "CHORALPRÄSTANT",  # FOUNDATION
    "CHORALPRINCIPAL",  # FOUNDATION
    "CHORALPRINZIPAL",  # FOUNDATION
    "CHORMASSPRINCIPAL",  # FOUNDATION
    "CHORMORNE",  # REED
    "CHORUS DIAPASON",  # FOUNDATION
    #"CHRYSOGLOTT",  # PERCUSSION
    "CILINDERQUINT",  # FOUNDATION
    "CÍMBALA",  # MIXTURE
    "CIMBALE",  # MIXTURE
    "CIMBALL",  # MIXTURE
    "CIMBALO",  # MIXTURE
    "CIMBEL",  # MIXTURE
    #"CIMBELSTERN"  # TOY
    "CINK",  # REED
    "CINQ",  # REED
    "CLAIRON",  # REED
    "CLAIRON DOUBLETTE",  # REED
    "CLAIRON EN CHAMADE",  # REED
    "CLAIRON HARMONIQUE",  # REED
    "CLARABEL FLUTE",  # FLUTE
    "CLARABELLA",  # FLUTE
    "CLARIANA",  # STRING
    "CLARIBEL",  # FLUTE
    "CLARIBEL FLUTE",  # FLUTE
    "CLARIBELLA",  # FLUTE
    "CLARÍN",  # REED
    "CLARIN CLARO",  # REED
    "CLARIN DE BAJOS",  # REED
    "CLARÍN DE BATALLA",  # REED
    "CLARÍN DE CAMPAÑA",  # REED
    "CLARÍN DE COMPAÑA",  # REED
    "CLARÍN DE ECOS",  # REED
    "CLARÍN DE MAR",  # REED
    "CLARÍN FUERTE",  # REED
    "CLARIN PARDO",  # REED
    "CLARÍN REAL",  # REED
    "CLARIN SORDINO",  # REED
    "CLARÍN SUAVE",  # REED
    "CLARINA",  # REED
    "CLARINES",  # REED
    "CLARINES EN QUINCENA",  # REED
    "CLARINET",  # REED
    "CLARINET À PAVILLON",  # REED
    "CLARINET FLUTE",  # FLUTE
    "CLARINETE",  # REED
    "CLARINETTE",  # REED
    "CLARINETTE-AIGUE",  # REED
    "CLARINETTE-BASSE",  # REED
    "CLARINETTO",  # REED
    "CLARINO",  # REED
    "CLARION",  # REED
    "CLARION HARMONIC",  # REED
    "CLARION HORN",  # REED
    "CLARION MIRABILIS",  # REED
    "CLARION MIXTURE",  # MIXTURE
    "CLARIONA",  # STRING
    "CLARIONET",  # REED
    "CLARIONET FLUTE",  # FLUTE
    "CLARON",  # REED
    "CLARONE",  # REED
    "CLAVAEOLINA",  # STRING
    "CLAVAEOLINE",  # REED
    "CLAVÄOLINE",  # REED
    "CLAVEOLINE",  # REED
    "CLEAR FLUTE",  # FLUTE
    "CLEAR MIXTURE",  # MIXTURE
    #"CLOCHES",  # PERCUSSION
    "CLOCHETTE",  # MIXTURE
    #"CLOCHETTES",  # TOY
    "CLOSED HORN",  # REED
    "COELESTINA",  # FLUTE
    "COMPENSATING MIXTURE",  # MIXTURE
    "COMPENSATION MIXTURE",  # MIXTURE
    "COMPENSATIONSMIXTUR",  # MIXTURE
    "COMPUESTAS",  # MIXTURE
    "COMPUESTAS DE LLENO",  # MIXTURE
    "CONCERT FLUTE",  # FLUTE
    "CONCERT VIOLIN",  # STRING
    "CONCERT VIOLIN CELESTE",  # STRING
    "CONCERTFLÖTE",  # FLUTE
    "CONE DIAPASON",  # FOUNDATION
    "CONE FLUTE",  # FLUTE
    "CONE GAMBA",  # STRING
    "CONE GAMBA CÉLESTE",  # STRING
    "CONE GEDACKT",  # FLUTE
    "CONE GEDECKT",  # FLUTE
    "CONE LIEBLICH GEDACT",  # FLUTE
    "CONI",  # FLUTE
    "CONICAL FLUTE",  # FLUTE
    "CONOCLYTE",  # REED
    "CONTRA BASSOON",  # REED
    "CONTRA BOMBARDE",  # REED
    "CONTRA BOMBARDON",  # REED
    "CONTRA BOURDON",  # FLUTE
    "CONTRA CORNO DI BASSETTO",  # REED
    "CONTRA DIAPHONE",  # FOUNDATION
    "CONTRA DULCIAN",  # REED
    "CONTRA DULCIANA",  # REED
    "CONTRA GAMBA",  # STRING
    "CONTRA HAUTBOY",  # REED
    "CONTRA OBOE",  # REED
    "CONTRA OPHICLEIDE",  # REED
    "CONTRA POSAUNE",  # REED
    "CONTRA PRINCIPAL",  # FOUNDATION
    "CONTRA SALICIONAL",  # STRING
    "CONTRA SAXOPHONE",  # REED
    "CONTRA SPITZFLÖTE",  # FLUTE
    "CONTRA TROMBA",  # REED
    "CONTRA TROMBONE",  # REED
    "CONTRA TRUMPET",  # REED
    "CONTRA TUBA",  # REED
    "CONTRA VIOL",  # STRING
    "CONTRA VIOLA",  # STRING
    "CONTRA VIOLA DA GAMBA",  # STRING
    "CONTRA VIOLE",  # STRING
    "CONTRA-VIOLIN",  # STRING
    "CONTRA-VIOLON",  # STRING
    "CONTRA VIOLONE", # STRING
    "CONTRABASS",  # STRING
    "CONTRABASSO",  # STRING
    "CONTRAFAGOTT",  # REED
    "CONTRAFAGOTTO",  # REED
    "CONTRAPOSAUNE",  # REED
    "CONTRAPRINZIPAL",  # FOUNDATION
    "CONTRAS",  # FOUNDATION
    "CONTRAS DE BOMBARDA",  # REED
    "CONTRAS EN BOMBARDAS",  # REED
    "CONTRAS PROFUNDAS",  # FLUTE
    "CONTRE-BASSE",  # STRING
    "CONTRE BOMBARDE",  # REED
    "CONTRE GAMBE",  # STRING
    "CONTRE TROMPETTE",  # REED
    "CONTRE VIOLE",  # STRING
    "CONUS",  # FLUTE
    "COPEL",  # MIXTURE
    "COPL",  # MIXTURE
    "COPPEL",  # FLUTE
    "COPPELDOEF",  # FLUTE
    "COPPELDONE",  # FOUNDATION
    "COPPELFLÖTE",  # FLUTE
    "COPPELFLUIT",  # FLUTE
    "COPPELOKTAVE",  # FOUNDATION
    "COPULA",  # MIXTURE
    "COPULA MAIOR",  # MIXTURE
    "COPULA MAJOR",  # MIXTURE
    "COPULA MINOR",  # MIXTURE,
    "COR ANGLAIS",  # REED
    "COR D'AMOUR",  # REED
    "COR D'HARMONIE",  # REED
    "COR D'ORCHESTRE",  # REED
    "COR DE BASSET",  # REED
    "COR DE CHAMOIS",  # FOUNDATION
    "COR DE NUIT",  # FLUTE
    "COR DE NUIT CELESTE",  # FLUTE
    "COR GLORIEUX",  # REED
    "COR-OBOE",  # REED
    "COR DE CHASSE",  # REED
    "CORDEDAIN",  # FLUTE
    "CORDELAIN",  # FLUTE
    "CORMORNE",  # REED
    #"CORNAMUSA",  # TOY
    "CORNE PARFORCE",  # REED
    "CORNE SYLVESTRE",  # REED
    "CORNEHORNE",  # REED
    #"CORNEMEUSE",  # TOY
    #"CORNEMUSE",  # TOY
    "CORNET",  # MIXTURE
    "CORNET À BOUCQUIN",  # MIXTURE
    "CORNET À PAVILLON",  # REED?
    "CORNET À PISTON",  # REED
    "CORNET D'ALLEMAGNE"  # MIXTURE
    "CORNET DE RÉCIT",  # MIXTURE
    "CORNET DES VIOLES",  # MIXTURE
    "CORNET DES BOMBARDES",  # MIXTURE
    "CORNET A TOLOSANA",  # MIXTURE
    "CORNETA",  # MIXTURE
    "CORNETA CLARA",  # MIXTURE
    "CORNETA REALE",  # MIXTURE
    "CORNETIN",  # MIXTURE
    "CORNETT",  # MIXTURE
    "CORNETTE DE CACCIA",  # REED
    "CORNETTI",  # MIXTURE
    "CORNETTIN",  # MIXTURE
    "CORNETTINO",  # MIXTURE
    "CORNETTO",  # MIXTURE
    "CORNETTO DA CACCIA",  # REED
    "CORNETTO DI CACCIA",  # REED
    "CORNETTO MUTO",  # MIXTURE
    "CORNETTO PRIMO",  # MIXTURE
    "CORNETTO SECONDO", # MIXTURE
    "CORNETTO TERZO",  # MIXTURE
    "CORNETTO TORTO",  # MIXTURE
    "CORNETZ À BOUCQUIN",  # MIXTURE
    "CORNO",  # REED
    "CORNO BASSO",  # REED
    "CORNO CAMOSCIO",  # FLUTE
    "CORNO CLARION",  # REED
    "CORNO D'AMORE",  # REED
    "CORNO DA CACCIA",  # REED
    "CORNO DI BASSETTO",  # REED
    "CORNO DI CACCIA",  # REED
    "CORNO DI CAMOSCIO",  # FLUTE
    "CORNO DOLCE",  # FLUTE
    "CORNO FLUTE",  # FLUTE, REED
    "CORNO INGLESE",  # REED
    "CORNO TROMBA",  # REED
    "CORNON",  # MIXTURE
    "CORNOPEAN",  # REED
    "CORNU",  # MIXTURE
    "CORNU SYLVESTRE",  # REED
    "CORROBORATING MIXTURE",  # MIXTURE
    "COUPLER",  # MIXTURE
    "COUPLING-FLUTE",  # MIXTURE
    "COURCELLINA",  # FLUTE
    "COURTAL",  # REED
    "COURTAND",  # REED
    "COURTEL",  # REED
    #"CRASH CYMBAL",  # PERCUSSION
    "CREMONA",  # REED
    "CREMORNE",  # REED
    "CRO ORLO",  # REED
    "CROMHORNE",  # REED
    "CROMMEHORNE",  # REED
    "CROMORNE",  # REED
    "CRUMHORN",  # REED
    #"CUCKGUCK",  # TOY
    #"CUCKOO",  # TOY
    #"CUCULUS",  # TOY
    #"CUKUK", # TOY
    "CURTAL",  # REED
    "CUSPIDA",  # FLUTE
    "CYLINDER-QUINTE",  # FOUNDATION
    "CYLINDERQUINT",  # FOUNDATION
    "CYMBAL",  # MIXTURE
    "CYMBALE",  # MIXTURE
    "CYMBALE HARMONIQUE",  # MIXTURE
    #"CYMBALSTERN",  # TOY
    "CYMBEL",  # MIXTURE
    "CYMBELBASS",  # MIXTURE
    #"CYMBELGLÖCKLEIN",  # TOY
    "CYMBELOKTAVE",  # FOUNDATION
    "CYMBELREGAL",  # MIXTURE
    "CYMBELSHARF",  # MIXTURE
    #"CYMBELSTERN",  # TOY
    "CYVELET",  # FLUTE
    "CZAKANFLÖTE",  # FLUTE
)

###############################################################################
# Functions
###############################################################################
def calc_frequency_equal_temperment(note: str, rank: str) -> float:
    midi_note: int = NOTE_TO_MIDI[note]
    midi_adjust: int = RANK_MIDI_OFFSET[rank]
    midi_num: int = midi_note + midi_adjust - NOTE_TO_MIDI["A4"]
    return FREQUENCY_A4 * pow(2, (midi_num/12))


if __name__ == "__main__":
    frequency: float = calc_frequency_equal_temperment("A4", "16'")
    print(frequency)
