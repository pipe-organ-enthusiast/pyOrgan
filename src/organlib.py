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
    "BACHFLÖTE",  # FLUTE / STRING HYBRID
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
    "BOKFLÖTE",  # FLUTE / STRING HYBRID
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
    "COPEL",  # FLUTE / MIXTURE
    "COPL",  # FLUTE / MIXTURE
    "COPPEL",  # FLUTE / MIXTURE
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
    "DECEM",  # FOUNDATION
    "DECEMBASS",  # FOUNDATION
    "DECIMA",  # FOUNDATION
    "DECIMA NONA",  # FOUNDATION
    "DECIMA QUINTA",  # FOUNDATION
    "DECIMA SETTIMA",  # FOUNDATION
    "DECUPLA",  # FOUNDATION
    "DESSUS DE FLÛTE",  # FLUTE
    "DESSUS DE FLÛTE ALLEMANDE",  # FLUTE
    "DETZEHM",  # FOUNDATION
    "DETZEMBASS",  # FOUNDATION
    "DEUTSCHE FLÖTE",  # FLUTE
    "DEVANTURE", # FOUNDATION
    "DIAOCTON",  # FOUNDATION
    "DIAPASON",  # FOUNDATION
    "DIAPASON CONIQUE",  # FOUNDATION
    "DIAPASON MAGNA",  # FOUNDATION
    "DIAPASON PHONON",  # FOUNDATION
    "DIAPASON SONORA",  # FOUNDATION
    "DIAPENTE",  # FOUNDATION
    "DIAPENTE PILEATA",  # FLUTE
    #"DIAPHONE",  # CAN TAKE ON SOUNDS OF ALL FAMILIES
    "DIAPHONE PROFUNDO",  # REED?
    "DIAPHONIC BASSOON",  # REED
    "DIAPHONIC DIAPASON",  # FOUNDATION
    "DIAPHONIC HORN",  # REED
    "DIAPHONIC VIOLONE",  # STRING
    "DIATONUS",  # FOUNDATION
    "DIEZ",  # FLUTE
    "DIEZ Y NOVENA",  # FLUTE
    "DIEZMONOVENA",  # FLUTE
    "DISCANTPRINCIPAL",  # FOUNDATION
    "DISDIAPASON",  # FOUNDATION
    "DISDIAPENTE",  # FOUNDATION
    "DISDISDIAPASON",  # FOUNDATION
    "DISKANTPRINZIPAL", # FOUNDATION
    "DISKANTSCHWIEGEL",  # FLUTE
    "DIATONUS",  # FOUNDATION
    "DIVINARE",  # FLUTE
    "DOCENA",  # FOUNDATION
    "DOEF",  # FOUNDATION
    "DÖEFF",  # FOUNDATION
    "DÖFF",  # FOUNDATION
    "DOIF",  # FOUNDATION
    "DOIFLÖT",  # FLUTE
    "DOIFLÖTE",  # FLUTE
    "DOLCAN",  # FLUTE
    "DOLCAN CÉLESTE",  # FLUTE
    "DOLCAN MIXTURE",  # MIXTURE - FLUTE
    "DOLCE",  # FLUTE
    "DOLCE CÉLESTE",  # FLUTE
    "DOLCE CORNET",  # MIXTURE
    "DOLCE FLUTE",  # FLUTE
    "DOLCE FLUTE CÉLESTE",  # FLUTE
    "DOLCE GRAND CORNET",  # MIXTURE
    "DOLCE MIXTURE",  # MIXTURE
    "DOLCE SUONO",  # REED
    "DOLCEAAN",  # REED
    "DOLCEAN",  # FOUNDATION
    "DOLCETTE",  # FLUTE
    "DOLCETTE FLUTE",  # FLUTE
    "DOLCIAN",  # REED
    "DOLCIANA",  # REED
    "DOLCIANE",  # FOUNDATION
    "DOLCIANO",  # FLUTE / REED
    "DOLCIANO PROFUNDO",  # FOUNDATION
    "DOLCISSIMO",  # FLUTE / FOUNDATION
    "DOLCISSIMO CÉLESTE",  # FLUTE
    "DOLKAN",  # FOUNDATION
    "DOLZFLÖTE",  # FLUTE
    "DOLZIANA",  # REED
    #"DONNER",  # SPECIAL EFFECT
    "DOOF",  # FOUNDATION
    "DOPPELFLÖTE",  # FLUTE
    "DOPPELFLÖTENBASS",  # FLUTE
    "DOPPELGEDACKT",  # FLUTE
    "DOPPELGEDECKT",  # FLUTE
    "DOPPELKEGELREGAL",  # REED
    "DOPPELPRINCIPAL",  # FOUNDATION
    "DOPPELROHRBORDUN",  # FLUTE
    "DOPPELROHRFLÖTE",  # FLUTE
    "DOPPELROHRGEDECKT",  # FLUTE
    "DOPPELSPITZFLÖTE",  # FLUTE
    "DOPPLT UNTERBASS",  # FLUTE
    "DORIS",  # FLUTE
    "DOTZENA NAZARDA",  # FONDATION
    "DOUBLE BASS",  # STRING
    "DOUBLE BASSET HORN",  # REED
    "DOUBLE BASSOON",  # REED
    "DOUBLE CLARIBEL FLUTE",  # FLUTE
    "DOUBLE CLARINET",  # REED
    "DOUBLE DIAPASON",  # FOUNDATION
    "DOUBLE DULCIANA",  # FOUNDATION
    "DOUBLE ENGLISH HORN",  # REED
    "DOUBLE FLUTE",  # FLUTE
    "DOUBLE GEMSHORN",  # FOUNDATION
    "DOUBLE HAUTBOY",  # REED
    "DOUBLE MELODIA",  # FLUTE
    "DOUBLE OBOE",  # REED
    "DOUBLE OBOE HORN",  # REED
    "DOUBLE OPEN DIAPASON",  # FOUNDATION
    "DOUBLE OPEN WOOD",  # FLUTE
    "DOUBLE OPHICLEIDE",  # REED
    "DOUBLE PRINCIPAL",  # FOUNDATION
    "DOUBLE QUINT",  # FOUNDATION
    "DOUBLE SALICIONAL",  # STRING
    "DOUBLE STOPPED BASS",  # FLUTE
    "DOUBLE STRING",  # STRING
    "DOUBLE TIERCE",  # FLUTE
    "DOUBLE TROMBONE",  # REED
    "DOUBLE TRUMPET",  # REED
    "DOUBLE TUBA",  # REED
    "DOUBLE TWELFTH",  # FOUNDATION
    "DOUBLE VOX HUMANA",  # REED
    "DOUBLETTE",  # MIXTURE / FOUNDATION
    "DOUCAINE",  # REED
    "DOUCE",  # FLUTE / FOUNDATION
    "DOUSEYNEN",  # REED
    #"DRUM PEDAL",  # PERCUSSION
    #"DRUMS",  # PERCUSSION
    #"DUCTUS INUTILIS",  # DUMMY STOP
    "DUDELSACK",  # REED
    "DUIFLÖT",  # FLUTE
    "DUIFLÖTE",  # FLUTE
    "DULCAN",  # FLUTE
    "DULCAYNA",  # REED
    "DULCEFLÖT",  # FLUTE
    "DULCEON",  # FLUNDATION
    "DULCET",  # FLUTE / FOUNDATION
    "DULCET PRINCIPAL",  # FLUTE / FOUNDATION
    "DULCETINA",  # FOUNDATION
    "DULCIAAN",  # REED
    "DULCIAN",  # REED
    "DULCIANA",  # FOUNDATION
    "DULCIANA CÉLESTE",  # FOUNDATION
    "DULCIANA CORNET",  # MIXTURE - FOUNDATION
    "DULCIANA FLUTE",  # FLUTE
    "DULCIANA FLUTE CÉLESTE",  # FLUTE
    "DULCIANA MIXTURE",  # MIXTURE - FOUNDATION
    "DULCIANA OCTAVE",  # FOUNDATION
    "DULCIANA PRINCIPAL",  # FOUNDATION
    "DULCIANE",  # FOUNDATION
    "DULCIANFLÖTE",  # FLUTE
    "DULCIMER",  # STRING
    "DULCINUS",  # REED
    #"DULCIS",  # MEANS SWEET. NO KNOWN EXAMPLES. MEANTIONED ONLY BY GROVE
    "DULCISSIMA",  # FLUTE / FOUNDATION
    "DULTZEN",  # REED
    "DULZAEN",  # FLUTE / FOUNDATION
    "DULZAIN",  # FLUTE / FOUNDATION
    "DULZAINA",  # REED
    "DULZAYNA",  # REED
    "DULZET",  # FOUNDATION
    "DULZFOIT",  # FLUTE
    "DULZFLÖTE",  # FLUTE
    "DULZGEDACKT",  # FLUTE
    "DULZIAN",  # REED
    "DULZIANA",  # FOUNDATION
    "DULZIANO",  # REED
    "DULZIANREGAL",  # REED
    "DULZINO",  # FOUNDATION
    #"DUNECKEN",  # GERMAN, MENTIONED BY PRAETORIUS, UNSURE OF FAMILY
    "DUODECIMA",  # FOUNDATION
    "DUOPHONE",  # COMPOUND (STRING / FLUTE?)
    "DUYTSCHE FLUYT",  # FLUTE
    "DUYTSCHE HOOREN",  # REED?
    "DWARSFLUIT",  # FLUTE
    "EARLY ENGLISH DIAPASON",  # FOUNDATION
    "ECHO AEOLINE",  # STRING
    "ECHO BASS",  #  FLUTE
    "ECHO BOURDON",  # FLUTE
    "ECHO CELLO",  # STRING
    "ECHO CLARABELLA",  # FLUTE
    "ECHO CLARION",  # REED
    "ECHO CORNET",  # MIXTURE - FOUNDATION
    "ECHO CORNETT",  # MIXTURE - FOUNDATION
    "ECHO CYMBAL",  # MIXTURE
    "ECHO DIAPASON",  # FOUNDATION
    "ECHO DOLCAN",  # FLUTE / FOUNDATION
    "ECHO DOLCE",  # FLUTE
    "ECHO DULCIANA",  # FOUNDATION
    "ECHO DULCIANA CÉLESTE",  # FOUNDATION
    "ECHO DULCIANA MIXTURE",  # MIXTURE - FOUNDATION
    "ECHO ERZÄHLER",  # STRING
    "ECHO FAGOTTO",  # REED
    "ECHO FIFTEENTH",  # FOUNDATION
    "ECHO FLUTE",  # FLUTE
    "ECHO GAMBA",  # STRING
    "ECHO GEDECKT",  # FLUTE
    "ECHO GEIGEN",  # FOUNDATION
    "ECHO GEIGEN DIAPASON",  # FOUNDATION
    "ECHO GEIGEN PRINCIPAL",  # FOUNDATION
    "ECHO GEMSHORN",  # FOUNDATION
    "ECHO HARMONICS",  # MIXTURE
    "ECHO HORN",  # REED
    "ECHO LIEBLICH",  # FLUTE
    "ECHO MELODIA",  # FLUTE
    "ECHO MIXTURE",  # MIXTURE
    "ECHO NACHTHORN",  # FLUTE / MIXTURE
    "ECHO OBOE",  # REED
    "ECHO OCTAVE",  # FOUNDATION
    "ECHO OPEN FLUTE",  # FLUTE
    "ECHO PRINCIPAL",  # FOUNDATION
    "ECHO SALICIONAL",  # STRING
    "ECHO STOPPED FLUTE",  # FLUTE
    "ECHO TIBIA",  # FLUTE
    "ECHO TIBIA CLAUSA",  # FLUTE
    "ECHO TROMBA",  # REED
    "ECHO TROMPETE",  # REED
    "ECHO TRUMPET",  # REED
    "ECHO TWELFTH",  # FOUNDATION
    "ECHO VIOL",  # STRING
    "ECHO VIOL MIXTURE",  # MIXTURE - STRING
    "ECHO VIOLA",  # STRING
    "ECHO VIOLA DA GAMBA",  # STRING
    "ECHO VIOLE CÉLESTE",  # STRING
    "ECHO VIOLIN",  # STRING
    "ECHO VOX HUMANA",  # REED
    "ECHOBORDUN",  # FLUTE
    "ECHOFLÖTE",  # FLUTE
    #"EFFETS D'ORAGE",  # EFFECT
    "EGYPTIAN HORN",  # REED
    "EIGHTEENTH",  # FOUNDATION
    "ELEVENTH",  # FOUNDATION
    "ENGELSTIMME",  # REED
    "ENGLISCH HORN",  # REED
    "ENGLISCH PRINZIPAL",  # FOUNDATION
    "ENGLISCH FLÖTE",  # FLUTE
    "ENGLISH DIAPASON",  # FOUNDATION
    "ENGLISH HORN",  # REED
    "ENGLISH POST HORN",  # REED
    "ENGPRINCIPAL",  # FOUNDATION
    "ENGPRINZIPAL",  # FOUNDATION
    "EOLINA",  # STRING
    "ÊOLINE",  # STRING
    "ERZÄHLER",  # STRING
    "ERZÄHLER CÉLESTE",  # STRING
    "ESPIGUETA",  # FLUTE
    "ETHEREAL VIOLIN",  # STRING
    "ETHEREAL VIOLIN CÉLESTE",  # STRING
    #"ÉTOILE SONORE",  # TOY
    "EUPHON",  # REED
    "EUPHÔNE",  # REED
    "EUPHONIUM",  # REED
    #"EXAUDIRE",  # DUMMY STOP
    "EYPHONE",  # REED
    "FABERTON",  # MIXTURE
    "FABERTONE",  # MIXTURE
    "FAGOT",  # REED
    "FAGOT OBOE",  # REED
    "FAGOT Y OBOE",  # REED
    "FAGOTT",  # REED
    "FAGOTT-DISKANT",  # REED
    "FAGOTTBASS",  # REED
    "FAGOTTE",  # REED
    "FAGOTTO",  # REED
    "FAGOTTONE",  # REED
    "FAN TRUMPET",  # REED
    "FAN TUBA",  # REED
    "FANFARE TRUMPET",  # REED
    "FELDFLÖT",  # FLUTE
    "FELDFLÖTE",  # FLUTE
    "FELDHORN",  # REED
    "FELDPFEIFE",  # FLUTE
    "FELDPIPE",  # FLUTE
    "FELDTROMMET",  # REED
    "FELDTROMPETE",  # REED
    "FERN FLUTE",  # FLUTE
    "FERNFLÖTE",  # FLUTE
    "FERNHORN",  # REED
    "FESTIVAL TRUMPET",  # REED
    "FIEDEL",  # STRING
    "FIELD TRUMPET",  # REED
    "FIFE",  # FLUTE
    "FIFFARO",  # FLUTE
    "FIFRE",  # FLUTE
    "FIFTEENTH",  # FOUNDATION
    "FIFTH",  # FOUNDATION
    "FILOMELA",  # FLUTE
    "FISTULA LARGIOR",  # FLUTE
    "FISTULA MILITARIS",  # FLUTE
    "FISTULA MINIMA",  # FLUTE
    "FISTULA RURESTRIS",  # FLUTE
    "FISTULA SALICIS",  # STRING
    "FLACH FLUTE",  # FLUTE
    "FLACHFLOIT",  # FLUTE
    "FLACHFLOJTE",  # FLUTE
    "FLACHFLÖTE",  # FLUTE
    "FLACHPFEIFE",  # FLUTE
    "FLAGEOLET",  # FLUTE
    "FLAGEOLET ECHO",  # FLUTE
    "FLAGEOLET HARMONIQUE",  # FLUTE
    "FLAGEOLETT",  # FLUTE
    "FLAGEOLETTA",  # FLUTE
    "FLAGEOLETTE",  # FLUTE
    "FLAT SEPTIME",  # FOUNDATION
    "FLAT SEVENTH",  # FOUNDATION
    "FLAT TWENTY-FIRST",  # FOUNDATION
    "FLAUT-À-BECQ",  # FLUTE
    "FLAUT ALLEMANDE",  # FLUTE
    "FLAUT DOUCE-BASS",  # FLUTE
    "FLAUT HEMIOL",  # FLUTE
    "FLAUT TRAVERS",  # FLUTE
    "FLAUTA ARMÓNICA",  # FLUTE
    "FLAUTA CUSPIDA",  # FLUTE
    "FLAUTA EUSKERIA",  # FLUTE
    "FLAUTA TAPADA",  # FLUTE
    "FLAUTA TRAVESIERA",  # FLUTE
    "FLAUTADA",  # FLUTE
    "FLAUTADITO",  # FLUTE
    "FLAUTADO",  # FOUNDATION
    "FLAUTADO DE VIOLÓN",  # FLUTE
    "FLAUTAT PRINCIPAL",  # MIXTURE - FOUNDATION
    "FLAUTIM",  # FLUTE
    "FLAUTINA",  # FLUTE
    "FLAUTINA DOLCE",  # FLUTE
    "FLAUTINO",  # FLUTE
    "FLAUTO",  # FLUTE
    "FLAUTO A CAMINO",  # FLUTE
    "FLAUTO ALLEMANO",  # FLUTE
    "FLAUTO AMABILE",  # FLUTE
    "FLAUTO AMOROSO",  # FLUTE
    "FLAUTO ANGELICO",  # FLUTE
    "FLAUTO APERTO",  # FLUTE
    "FLAUTO CAMINO",  # FLUTE
    "FLAUTO COPERTO",  # FLUTE
    "FLAUTO CUSPIDO",  # FLUTE
    "FLAUTO D'AMORE",  # FLUTE
    "FLAUTO DI PAN",  # FLUTE
    "FLAUTO DOLCE",  # FLUTE
    "FLAUTO DOLCISSIMO",  # FLUTE
    "FLAUTO DOLCISSIMO CÉLESTE",  # FLUTE
    "FLAUTO DORIS",  # FLUTE
    "FLAUTO DULCIO",  # FLUTE
    "FLAUTO DULCIS",  # FLUTE
    "FLAUTO GRAVE",  # FLUTE
    "FLAUTO HARMONICISSIMO",  # FLUTE
    "FLAUTO ITALICO",  # FLUTE
    "FLAUTO MAGGIORE",  # FLUTE
    "FLAUTO MAJOR",  # FLUTE
    "FLAUTO MINOR",  # FLUTE
    "FLAUTO MINORE",  # FLUTE
    "FLAUTO MIRABILIS",  # FLUTE
    "FLAUTO PICCOLO",  # FLUTE
    "FLAUTO PRIMO",  # FLUTE
    "FLAUTO REALE",  # FLUTE
    "FLAUTO STACCATO",  # FLUTE
    "FLAUTO TEDESCA",  # FLUTE
    "FLAUTO TEDESCO",  # FLUTE
    "FLAUTO TRAVERSO",  # FLUTE
    "FLAUTO TRAVESIERA",  # FLUTE
    "FLAUTO UNISONE",  # FLUTE
    "FLAUTONE",  # FLUTE
    "FLAUTONNE",  # FLUTE
    "FLAUTT IN 6TA",  # MIXTURE - FOUNDATION
    "FLET",  # FLUTE
    "FLETNA",  # FLUTE
    "FLEUT",  # FLUTE
    "FLÖT",  # FLUTE
    "FLÖTE",  # FLUTE
    "FLÖTE DUPLA",  # FLUTE
    "FLÖTE HARMONICA",  # FLUTE
    "FLÖTE MAJOR",  # FLUTE
    "FLÖTE MINOR",  # FLUTE
    "FLÖTE TRAVERSA",  # FLUTE
    "FLÖTEDOUCE",  # FLUTE
    "FLÖTEDOUCEBASS",  # FLUTE
    "FLÖTENBASS",  # FLUTE
    "FLÖTENPRINCIPAL",  # FLUTE
    "FLUE CLARINET",  # FLUTE
    "FLUE COR ANGLAIS",  # FLUTE
    "FLUE EUPHONE",  # MIXTURE - FLUTE/STRING
    "FLUE OBOE",  # MIXTURE - FLUTE/STRING
    "FLUEGELHORN",  # REED
    "FLÜGELHORN",  # REED
    "FLUIT",  # FLUTE
    "FLUSTE",  # FLUTE
    "FLUTA",  # FLUTE
    "FLÛTE",  # FLUTE
    "FLÛTE À BEC",  # FLUTE
    "FLÛTE À BECQ",  # FLUTE
    "FLÛTE À BIBERON",  # FLUTE
    "FLÛTE À BOUCHE RONDE",  # FLUTE
    "FLÛTE À CHEMINÉE",  # FLUTE
    "FLÛTE À FUSEAU",  # FLUTE
    "FLÛTE À FUSÉE",  # FLUTE
    "FLÛTE À NEUF TROUS",  # FLUTE
    "FLÛTE À PAVILLON",  # FLUTE
    "FLÛTE À POINTE",  # FLUTE
    "FLÛTE À PYRAMIDE",  # FLUTE
    "FLUTE ALEMAND",  # FLUTE
    "FLÛTE ALLEMANDE",  # FLUTE
    "FLÛTE ANGÉLIQUE",  # FLUTE
    "FLÛTE BASS",  # FLUTE
    "FLÛTE BOUCHÉE",  # FLUTE
    "FLÛTE BOUCHÉE HARMONIQUE",  # FLUTE
    "FLUTE CÉLESTE",  # FLUTE
    "FLÛTE CHAMP",  # FLUTE
    "FLÛTE COELESTIS",  # FLUTE
    "FLÛTE CONIQUE",  # FLUTE
    "FLÛTE COURTE",  # FLUTE
    "FLÛTE COUVERTE",  # FLUTE
    "FLÛTE CREUSE",  # FLUTE
    "FLÛTE D'ALEMAGNE",  # FLUTE
    "FLÛTE D'ALLEMAGNE",  # FLUTE
    "FLÛTE D'AMOUR",  # FLUTE
    "FLÛTE D'AMOUR CÉLESTE",  # FLUTE
    "FLÛTE D'ORCHESTRE",  # FLUTE
    "FLÛTE DE BOIS",  # FLUTE
    "FLÛTE DE PÉDALE",  # FLUTE
    "FLÛTE DES BOIS",  # FLUTE
    "FLUTE DOLCE",  # FLUTE
    "FLUTE DOUBLE",  # FLUTE
    "FLÛTE DOUCE",  # FLUTE
    "FLÛTE DUPLA",  # FLUTE
    "FLÛTE EN FUSÉE",  # FLUTE
    "FLÛTE FONDAMENTALE",  # FLUTE
    "FLÛTE HARMONIQUE",  # FLUTE
    "FLÛTE MAGIQUE",  # FLUTE
    "FLÛTE MAJEUR",  # FLUTE
    "FLÛTE NASARD",  # FLUTE
    "FLÛTE OCTAVIANTE",  # FLUTE
    "FLÛTE OCTAVIANTE HARMONIQUE",  # FLUTE
    "FLÛTE OCTAVIENTE HARMONIQUE",  # FLUTE
    "FLÛTE OCTAVIN HARMONIQUE",  # FLUTE
    "FLÛTE ORCHESTRALE",  # FLUTE
    "FLÛTE OUVERTE",  # FLUTE
    "FLÛTE POINTUE",  # FLUTE
    "FLUTE PRINCIPAL",  # FLUTE
    "FLÛTE PYRAMIDALE",  # FLUTE
    "FLUTE QUINT",  # FLUTE
    "FLUTE TRAVERSA",  # FLUTE
    "FLUTE TRAVERSE",  # FLUTE
    "FLÛTE TRAVERSIÈRE",  # FLUTE
    "FLÛTE TRIANGULAIRE",  # FLUTE
    "FLUTE TRIANGULAR",  # FLUTE
    "FLUTE BASS",  # FLUTE
    "FLÛTON",  # FLUTE
    #"FLUTTUAN",  # FLUTE? UNCOMMON STOP
    "FOREST FLUTE",  # FLUTE
    "FORNITURA",  # MIXTURE
    "FORNITURE",  # MIXTURE
    "FOURNITURE CYMBALISÉE",  # MIXTURE
    "FOURNITURE HARMONIQUE",  # MIXTURE
    "FOURTEENTH",  # FOUNDATION
    "FRANZÖSISCHE POSAUNE",  # REED
    "FRENCH HORN",  # REED
    "FRENCH TRUMPET",  # REED
    "FRONTISPICIUM",  # FOUNDATION
    #"FUCHSSCHWANK",  # JOKE STOP
    #"FUCHSSCHWANZ",  # JOKE STOP
    "FUGARA",  # STRING
    "FULL FLUTE",  # FLUTE
    "FULL MIXTURE",  # MIXTURE
    "FULLFLÖTE",  # FLUTE
    "FÜLLQUINTE",  # FOUNDATION
    "FUNDAMENTALIS",  # FOUNDATION
    "FURNITURE",  # MIXTURE
    "GAITAS",  # REED
    "GALONBEL",  # MIXTURE
    "GALOUBET",  # FLUTE
    "GALOUBETH",  # FLUTE
    "GAMBA",  # STRING
    "GAMBA CELESTE",  # STRING
    "GAMBA DIAPASON",  # STRING
    "GAMBE",  # STRING
    "GAMBENBASS",  # STRING
    "GAMBETTE",  # STRING
    "GAMBETTE CELESTE",  # STRING
    "GEDACKT",  # FLUTE
    "GEDACKT-BOMMER",  # FLUTE
    "GEDACKT LIEBLICH",  # FLUTE
    "GEDACKT POMMER",  # FLUTE
    "GEDACKTE ITALIENISCHE QUINTE",  # FLUTE
    "GEDACKTE QUINTE",  # FLUTE
    "GEDACKTE QUINTFLÖTE",  # FLUTE
    "GEDACKTFLÖTE",  # FLUTE
    "GEDACKTFLÖTOKTAVE",  # FLUTE
    "GEDACKTQUINTE",  # FLUTE
    "GEDACT",  # FLUTE
    "GEDACT POMMER",  # FLUTE
    "GEDACT QUINT",  # FLUTE
    "GEDAKT",  # FLUTE
    "GEDAKTFLÖT CHORMASS",  # FLUTE
    "GEDAKTFLÖT UNTER CHORMASS",  # FLUTE
    "GEDAKTPOMMER",  # FLUTE
    "GEDÄMPFTREGAL",  # REED
    "GEDECKT",  # FLUTE
    "GEDECKT QUINTE",  # FLUTE
    "GEDECKT TIERCE",  # FLUTE
    "GEDECKT TWELFTH",  # FLUTE
    "GEDECKTBASS",  # FLUTE
    "GEDECKTBOMMER",  # FLUTE
    "GEDECKTFLÖTE",  # FLUTE
    "GEDECKTPOMMER",  # FLUTE
    "GEDECKTQUINTE",  # FLUTE
    "GEDECKTREGAL",  # REED?
    "GEDEMPFTREGAL",  # REED
    "GEIGEN",  # FOUNDATION / STRING HYBRID
    "GEIGEN DIAPASON",  # FOUNDATION / STRING HYBRID
    "GEIGEN FIFTEENTH",  # FOUNDATION / STRING HYBRID
    "GEIGEN OCTAVE",  # FOUNDATION / STRING HYBRID
    "GEIGEN PRINCIPAL"  # FOUNDATION / STRING HYBRID
    "GEIGEN REGAL",  # REED
    "GEIGEN SUPER OCTAVE",  # FOUNDATION / STRING HYBRID
    "GEIGEN TWELFTH",  # FOUNDATION / STRING HYBRID
    "GEIGENBASS",  # FOUNDATION
    "GEIGENDREGAL",  # REED
    "GEIGENDREGÄLCHEN",  # REED
    "GEIGENOCTAV",  # FOUNDATION / STRING HYBRID
    "GEIGENPRINCIPAL",  # FOUNDATION / STRING HYBRID
    "GEIGENPRINZIPAL",  # FOUNDATION / STRING HYBRID
    "GEIGENREGAL",  # REED
    "GELINDGEDECKT",  # FLUTE
    "GEMSHOORN",  # FLUTE / STRING HYBRID
    "GEMSHORN",  # FLUTE / STRING HYBRID
    "GEMSHORN BAARPIJP",  # FLUTE
    "GEMSHORN CELESTE",  # FLUTE / STRING HYBRID
    "GEMSHORN CORNET",  # MIXTURE - FLUTE / STRING HYBRID
    "GEMSHORN DIAPASON",  # FOUNDATION
    "GEMAHORN FIFTEENTH",  # FLUTE / STRING HYBRID
    "GEMSHORN GAMBA",  # STRING
    "GEMSHORN MIXTURE",  # MIXTURE
    "GEMSHORN OCTAVE",  # FLUTE / STRING HYBRID
    "GEMSHORN QUINT",  # FLUTE / STRING HYBRID
    "GEMSHORN SUPER OCTAVE",  # FLUTE / STRING HYBRID
    "GEMSHORN TWELFTH",  # FLUTE / STRING HYBRID
    "GEMSHORN VIOLIN",  # STRING
    "GEMSHORNBASS",  # FLUTE / STRING HYBRID
    "GEMSHORNQUINT",  # FLUTE / STRING HYBRID
    "GEMSHORNQUINTE",  # FLUTE / STRING HYBRID
    "GEMSQUINTE",  # FLUTE / STRING HYBRID
    "GEMSROHRFLÖTE",  # FLUTE
    "GEMSTER",  # FLUTE / STRING HYBRID
    "GERMAN FLUTE",  # FLUTE
    "GERMAN GAMBA",  # STRING
    "GESANG REGAL",  # REED
    "GINGRINA",  # REED
    "GLOCKENFLÖTE",  # FLUTE
    "GLOCKENGAMBA",  # STRING
    #"GLOCKENREGISTER",  # PERCUSSION
    #"GLOCKENSPIEL",  # PERCUSSION
    "GLÖCKENTON",  # FLUTE
    "GLOCKENZIMBEL",  # MIXTURE
    "GLOCKENZYMBEL",  # MIXTURE
    "GLÖCKLEIN",  # FLUTE
    "GLÖCKLEINTON",  # FLUTE
    #"GONGS",  # PERCUSSION
    "GOTTFRIED TRUMPET",  # REED
    "GRAND CHORUS",  # MIXTURE
    "GRAND CORNET",  # MIXTURE
    "GRAND DIAPASON",  # FOUNDATION
    "GRAND FLUTE",  # FLUTE
    "GRAND FOURNITURE",  # MIXTURE
    "GRAND MUTATION",  # MIXTURE
    "GRAND OCTAVE",  # FOUNDATION
    "GRAND OPEN DIAPASON",  # FOUNDATION
    "GRAND OPEN PEDAL",  # FOUNDATION
    "GRAND PRINCIPAL",  # FOUNDATION
    "GRAND QUINTE",  # FOUNDATION
    "GRAND QUINTATEN",  # FLUTE
    "GRAND VIOL",  # STRING
    "GRANDE FOURNITURE",  # MIXTURE
    "GRAVE",  # MIXTURE
    "GRAVE MIXTURE",  # MIXTURE
    "GRAVISSIMA",  # MIXTURE - FOUNDATION
    "GRAVITONE",  # MIXTURE - FOUNDATION
    "GREAT BASS",  # FOUNDATION
    "GREAT TIERCE",  # FOUNDATION ?
    #"GRÊLE",  # EFFECT
    "GROẞ GEDACKT",  # FLUTE
    "GROẞCYMBEL",  # MIXTURE
    "GROẞEMIXTUR UNTERCHORMASS",  # MIXTURE
    "GROẞEN PRINCIPAL",  # FOUNDATION
    "GROẞER POSAUNEN-UNTERSATZ",  # REED
    "GROẞMIXTURE",  # MIXTURE
    "GROẞPOSAUNE",  # REED
    "GROẞREGAL",  # REED
    "GROS BOURDON",  # FLUTE
    "GROS NASARD",  # FLUTE
    "GROSS CORNET",  # MIXTURE
    "GROSS FLUTE",  # FLUTE
    "GROSS FLÛTE DOUCE",  # FLUTE
    "GROSS GAMBA",  # STRING
    "GROSS GEDACKT",  # FLUTE
    "GROSS GEIGEN",  # FOUNDATION
    "GROSS MIXTURE",  # MIXTURE
    "GROSS NASARD",  # FLUTE
    "GROSS QUINT",  # FLUTE
    "GROSS RANKET",  # REED
    "GROSS SESQUIALTERA",  # MIXTURE
    "GROSS SPITZFLÖTE",  # FLUTE
    "GROSS TIERCE",  # FOUNDATION
    "GROSSDOPPELGEDECKT",  # FLUTE
    "GROSSE CYMBALE",  # MIXTURE
    "GROSSE FLÖTE",  # FLUTE
    "GROSSE FLÛTE",  # FLUTE
    "GROSSE FOURNITURE",  # MIXTURE
    "GROSSE QUINTE",  # FLUTE
    "GROSSE SEQUIALTERA",  # MIXTURE
    "GROSSE SPITZFLÖTE",  # FLUTE
    "GROSSE TIERCE",  # FOUNDATION
    "GROSSFLACHFLÖTE",  # FLUTE
    "GROSSFLÖTE",  # FLUTE
    "GROSSGAMBA",  # STRING
    "GROSSGEDECKT",  # FLUTE
    "GROSSGEMSHORN", # FOUNDATION
    "GROSSGEMSHORNBASS",  # FOUNDATION / FLUTE
    "GROSSHOHLFLÖTE",  # FLUTE
    "GROSSHOTZFLÖT",  # FLUTE
    "GROSSKOPPEL",  # FLUTE
    "GROSSNASAT",  # FLUTE
    "GROSSNASSAT",  # FLUTE
    "GROSSOCTAV",  # FOUNDATION
    "GROSSOCTAVBASS",  # FOUNDATION
    "GROSSOKTAV",  # FOUNDATION
    "GROSSPOSAUNE",  # REED
    "GROSSPRASTANT",  # FOUNDATION
    "GROSSPRINCIPALBASS",  # FOUNDATION
    "GROSSPRINZIPAL",  # FOUNDATION
    "GROSSPRINZIPALBASS",  # FOUNDATION
    "GROSSQUERFLÖTE",  # FLUTE
    "GORSSQUINTENBASS",  # FLUTE
    "GROSSRAUSCHQUINTE",  # FOUNDATION
    "GROSSREGAL",  # REED
    "GROSSROHRFLÖTE",  # FLUTE
    "GROSSROHRFLÖTENBASS",  # FLUTE
    "GROSSSUBBASS",  # FLUTE
    "GROSSTERZ",  # FOUNDATION
    "GROSSUNTERBASS",  # FLUTE
    "GROSSUNTERSATZ",  # FLUTE
    #"GUCKGUCK",  # TOY STOP
    #"GUKUK",  # TOY STOP
    "HAEMIOL",  # FLUTE
    #"HAHN",  # IMITATIVE ROOSTER CALL
    #"HAIL",  # EFFECT
    "HALBER CORNET",  # MIXTURE
    "HALPRINCIPAL",  # FOUNDATION
    #"HARFA",  # HARP
    #"HARFE",  # HARP
    "HARFENPRINCIPAL",  # FOUNDATION / STRING
    "HARFENPRINZIPAL",  # FOUNDATION / STRING
    "HARFENREGAL",  # REED
    "HARFPFEIFE",  # STRING
    "HARMONIA AETHERA",  # MIXTURE - STRING
    "HARMONIA AETHEREA",  # MIXTURE - STRING
    "HARMONIA AETHERIA",  # MIXTURE - STRING
    "HARMONIC BASS",  # MIXTURE - PRINCIPAL
    "HARMONIC CLARIBEL",  # FLUTE
    "HARMONIC CLARION",  # REED
    "HARMONIC CORNET",  # MIXTURE
    "HARMONIC CYMBAL",  # MIXTURE
    "HARMONIC DIAPASON",  # FOUNDATION
    "HARMONIC FLUTE",  # FLUTE
    "HARMONIC GEDECKT",  # FLUTE
    "HARMONIC GEMSHORN",  # FLUTE / STRING
    "HARMONIC MIXTURE",  # MIXTURE
    "HARMONIC OCTAVE",  # FOUNDATION
    "HARMONIC PICCOLO",  # FLUTE
    "HARMONIC PLEIN JEU",  # MIXTURE
    "HARMONIC STOPPED TWELFTH",  # FLUTE
    "HARMONIC TIERCE",  # FOUNDATION
    "HARMONIC TRUMPET",  # REED
    "HARMONIC TUBA",  # REED
    "HARMONIC TUBA CLARION",  # REED
    "HARMONIC TWELFTH",  # FLUTE
    "HARMONICA",  # FLUTE / STRING
    "HARMONICABASS",  # FLUTE / STRING
    "HARMONICS",  # MIXTURE
    "HARMONIEFLÖTE",  # FLUTE
    "HARMONIETROMPETE",
    "HARMONIKA",
    "HARMONIKA CELESTE",
    "HARMONIKABASS",
    "HARMONIQUE PICCOLO",
    "HARMONIUM",
    #"HARP",
    "HARP AEOLIAN",
    "HARP AEOLINE",
    "HARP AEOLONE",
    "HAUTBOIS",
    "HAUTBOIS D'AMOUR",
    "HAUTBOIS D'ORCHESTRE",
    "HAUTBOY",
    "HAUTBOY & BASSOON",
    "HAUTBOY CLARION",
    "HAUTBOY CORNET",
    "HECKELPHONE",
    #"HEDEIAPHONE",
    #"HEERTRUMMEL",
    "HELLEZIMBEL",
    "HELLFLÖTE",
    "HELLPFEIFE",
    "HEMIOL",
    "HEMIOLFLÖTE",
    "HINTERSATZ",
    "HOBOE",
    "HOHL FLUTE",
    "HOHLFLÖTE",
    "HOHLFLÖTENBASS",
    "HOHLPFEIFE",
    "HOHLQUINTA",
    "HOHLQUINTE",
    "HOHLSCHELLE",
    "HOHPFEIFE",
    "HOL FLUTE",
    "HOLE FLUTE",
    "HOLFLÖTE",
    "HOLFLUIT",
    "HOLPFEIFE",
    "HOLPIJP",
    "HOLPIPE",
    "HOLQUINTE",
    "HOLSCHELLE",
    "HOLTZBASS",
    "HOLTZFLÖTE",
    "HOLTZGEDACKT",
    "HOLZDULZIAN",
    #"HÖLZERNES GELÄCHTER",
    "HÖLZERNPRINCIPAL",
    "HOLZFLÖTE",
    "HOLZGEDACKT",
    "HOLZGEDECKT",
    "HOLZHARMONICA",
    "HOLZKRUMMHORN",
    "HOLZPFEIFE",
    "HOLZPOSAUNE",
    "HOLZPRINZIPAL",
    "HOLZRANKETT",
    "HOLZREGAL",
    "HOORN",
    "HORIZONTAL TRUMPET",
    "HORIZONTAL TUBA",
    "HORN",
    "HORN DIAPASON",
    "HORN GAMBA",
    "HORNBÄSSLEIN",
    "HORNLE"
    "HÖRNLEIN",
    "HÖRNLI",
    #"HÜLTZE GLECHTER",
    "HUMANGEDACKT",
    "HUMANGEDECKT",
    #"HUMMEL",
    #"HUMMELCHEN",
    #"HUNDPFEIFE",
    "HUNTING HORN",
    #"IMITACION DE TEMPESTAD",
    "INFRA BASS",
    "ITALIAN PRINCIPAL",
    "IULA",
    "JAUCHZENDPFEIFE",
    "JEU DE CLOCHETTE",
    "JEU EN MONTRE",
    "JEU ÉRARD",
    "JUBAL",
    "JUBAL FLUTE",
    "JUBALFLÖTE",
    "JUBALHORN",
    "JULA",
    "JULAQUINTE",
    "JUNFERNREGAL",
    "JUNGFERNREGAL",
    "JUNGFERNREGALBASS",
    "JUNGFERNSTIME",
    "JUNGFERNSTIMME",
    "JUNGFERSTIMME",
    "JUNGFRAUENREGAL",
    "JUNGFRAUENREGALBASS",
    "KÄLBERREGAL",
    "KALLIOPE",
    "KAMMERFLÖTE",
    "KAMMERGEDECKT",
    "KAMMERTON GEDACKT",
    "KEEN STRINGS",
    "KEGEL",
    "KERAULOPHON",
    "KERAULOPHONE",
    #"KETTLEDRUMS",
    "KEWZIALFLÖTE",
    "KINURA",
    "KLARIN",
    "KLARINETTE",
    "KLARINETTBASS",
    "KLAROEN",
    "KLAVÄOLINE",
    "KLAXON HORN",
    "KLEIN ERZÄHLER",
    "KLEIN ERZÄHLER CELESTE",
    "KLEIN FLÖTENBASS",
    "KLEIN GEDACKT",
    "KLEIN OCTAVENGEMSHORN",
    "KLEIN PRINCIPAL",
    "KLEIN RANKET",
    "KLEIN VIOLN",
    "KLEIN OCTAVE",
    "KLEINCIMBEL",
    "KLEINE ERZÄHLER",
    "KLEINE ERZÄHLER CELESTE"
    "KLEINE FLÖTE",
    "KLEINE HOHLFLÖTE",
    "KLEINE MIXTUR",
    "KLEINE MIXTUR CHORMASS",
    "KLEINE MIXTURE",
    "KLEINE ZIMBEL",
    "KLEINER CYMBEL",
    "KLEINER ERZÄHLER",
    "KLEINER ERZÄHLER CELESTE",
    "KLEINERZÄHLER",
    "KLEINFLACHFLÖT",
    "KLEINFLÖTE",
    "KLEINFLÖTENBASS",
    "KLEINGEDECKT",
    "KLEINGEMSHORN",
    "KLEINHOHLFLÖTE",
    "KLEINMIXTUR",
    "KLEINOKTAVE",
    "KLEINPRINZIPAL",
    "KLEINQUERFLÖTE",
    "KLEINREGAL",
    "KLEINREGALBASS",
    "KLEINSCHREIER",
    "KLEINSCHREYER",
    "KLEINTERZ",
    "KLINGENDE CYMBEL",
    "KLINGENDER CYMBEL",
    "KLINGENDZIMBEL",
    "KNIEGEIGE",
    "KNOPFREGAL",
    "KONTRA BASS",
    "KÖPFLINREGAL",
    "KOPFREGAL",
    "KOPFTROMPETE",
    "KOPPEL",
    "KOPPEL FLUTE",
    "KOPPEL OCTAVE",
    "KOPPELDONE",
    "KOPPELDOOF",
    "KOPPELDOUS",
    "KOPPELFLÖTE",
    "KOPPELGEDACKT",
    "KOPPELGEDECKT",
    "KOPPELOKTAVE",
    "KORNETT",
    "KROMHOORN",
    "KRUMET",
    "KRUMET HORN",
    "KRUMHORN",
    "KRUMMHORN",
    "KRUMMHORNREGAL",
    "KRYTHER",
    #"KUCKUCK",
    "KEURLOFON",
    "KUPFERFLÖTE",
    "KURZEFLÖTE",
    "KURZFLÖTE",
    "KÜTZIALFLÖTE",
    "KUZIALFLÖTE",
    "LA FORCE",
    "LABIAL CLARINET",
    "LABIAL COR ANGLAIS",
    "LABIAL EUPHONE",
    "LABIAL KLARINETTE",
    "LABIAL OBOE",
    "LARGIOR",
    "LARGO",
    "LARIGOT",
    "LARIGOT MIXTURE",
    "LIEBESGEIGE",
    "LIEBLICH BOURDON",
    "LIEBLICH FLUTE",
    "LIEBLICH GEDACKT",
    "LIEBLICH GEDACT",
    "LIEBLICH GEMSQUINTE",
    "LIEBLICH QUINT",
    "LIEBLICHBORDUN",
    "LIEBLICHFLÖTE",
    "LIEBLICHGEDECKT",
    "LIEBLICHGESCHALLT",
    "LIEBLICHNASAT",
    "LIEBLICHPFEIF",
    "LIEBLICHQUINTE",
    "LITICE",
    "LITURGICAL TRUMPET",
    "LITUUS",
    "LLENO",
    "LOCATIE",
    "LOCATIO",
    "LOCATION",
    "LOCHGEDACKT",
    "LOCHGEDECKT",
    "LOKATIO",
    "LUDWIGTONE",
    #"LUTE",
    "MAGNATON",
    "MAJOR BASS",
    "MAJOR CLARINET",
    "MAJOR DIAPASON",
    "MAJOR FLUTE",
    "MAJOR MIXTUR",
    "MAJOR MIXTURE",
    "MAJOR OCTAVE",
    "MAJOR OPEN FLUTE",
    "MAJOR PRINCIPAL",
    "MAJOR QUINTE",
    "MAJOR SAXOPHONE",
    "MAJOR TWELFTH",
    "MAJOR VOX HUMANA",
    "MAJORBASS",
    "MAJORFLÖTE",
    "MANUALUNTERSATZ",
    #"MANUM DE TABULA",
    #"MARIMBA",
    #"MARIMBA HARP",
    "MEERFLÖTE",
    "MEGALOPENTE",
    "MEGALOPHONE",
    "MELLOPHONE",
    "MELODIA",
    "MELODICA"
    "MÉLODIE",
    "MELOPHONE",
    "MELOTONE",
    "MENSCHENSTIMME",
    #"MERULA",
    "MESSINGREGAL",
    "MESSINGREGAL SINGEND",
    "METALGEDACKT",
    "METALGEDECKT",
    "METALLIC FLUTE",
    "METRONOMUS",
    "MICXTUERE",
    "MILITARY TRUMPET",
    "MINERICI",
    "MINOR CLARINET",
    "MINOR DIAPASON",
    "MINOR OCTAVE",
    "MINOR OPEN FLUTE",
    "MINOR PRINCIPAL",
    "MINOR VOX HUMANA",
    "MINORFLÖTE",
    "MITTELGEDACKT",
    "MITTELGEDECKT",
    "MIXTUER",
    "MIXTUR",
    "MIXTUR CHORMASS",
    "MIXTUR MAJOR",
    "MIXTURA",
    "MIXTURA MAJOR",
    "MIXTURE",
    "MIXTUUR",
    "MOLLTERS",
    "MOLLTERZ",
    "MONSTER",
    "MONTRE",
    "MONTRE ECHO",
    "MOSTRA",
    "MOUNTED CORNET",
    "MUNDFLÖTE",
    "MUSETTE",
    "MUSICIRGEDECKT",
    "MUSIKGEDACKT",
    "MUSIZIERGEDACKT",
    "MUTED CELLO",
    "MUTED CORNET",
    "MUTED DIAPASON",
    "MUTED GAMBA",
    "MUTED HORN",
    #"MUTED SNARE DRUM",
    "MUTED STRINGS",
    "MUTED TRUMPET",
    "MUTED VIOL",
    "MUTED VIOL MIXTURE",
    "MUTED VIOLA",
    "MUTED VIOLE",
    "MUTED VIOLIN",
    "MUTED VIOLIN CÉLESTE",
    "NACHSATZ",
    "NACHTHOORN",
    "NACHTHORN",
    "NACHTHORNBASS",
    "NACHTHÖRNCHEN",
    "NACHTHORNGEDACKT",
    #"NACHTIGALL",
    "NACHTSCHALL",
    "NASAD",
    "NASARD",
    "NASARD À FUSEAU",
    "NASARD EN CHEMINÉE",
    "NASARD FLÛTE",
    "NASARD GAMBA",
    "NASARD HARMONIQUE",
    "NASARD OUVERT",
    "NASARDE",
    "NASARDO",
    "NASARDOS",
    "NASAT",
    "NASATFLÖTE",
    "NASATH",
    "NASATQUINTE",
    "NASAZ",
    "NASHORN",
    "NASON",
    "NASON FLUTE",
    "NASON GEDACKT",
    "NASON GEDECKT",
    "NASONFLÖTE",
    "NASSART",
    "NASSAT",
    "NASSATQUINT",
    "NASSATT",
    "NAZAR",
    "NAZARD",
    "NAZARD HARMONIQUE",
    "NAZARDO",
    "NAZAT",
    "NETE",
    "NEUVIÈME",
    "NIGHT HORN",
    #"NIGHTINGALE",
    #"NIHIL",
    "NINETEENTH",
    "NINTH",
    "NITSUA",
    #"NOLI ME TANGERE",
    "NONE",
    "NONENKORNETT",
    "OBERTON",
    "OBOE",
    "OBOE & FAGOTTO",
    "OBOE CLARION",
    "OBOE D'AMORE",
    "OBOE D'AMOUR",
    "OBOE ECHO",
    "OBOE FLUTE",
    "OBOE GAMBA",
    "OBOE HORN",
    "OBOE SHALMEI",
    "OBTUSA",
    "OBTUSIOR",
    "OCARINA",
    "OCTAAF",
    "OCTAV",
    "OCTAVA",
    "OCTAVA COMPOSITA",
    "OCTAVA DE ECOS",
    "OCTAVA DE NASARDOS",
    "OCTAVA TAPADA",
    "OCTAVBASS",
    "OCTAVE",
    "OCTAVE BASS",
    "OCTAVE BASSET HORN",
    "OCTAVE CELESTE",
    "OCTAVE CLARABELLA",
    "OCTAVE CLARION",
    "OCTAVE DIAPASON",
    "OCTAVE DOLCE",
    "OCTAVE DULCIANA",
    "OCTAVE FIFTEENTH",
    "OCTAVE FLUTE",
    "OCTAVE GAMBA",
    "OCTAVE GEIGEN",
    "OCTAVE GEMSHORN",
    "OCTAVE HAUTBOY",
    "OCTAVE HORN",
    "OCTAVE MIXTURE",
    "OCTAVE OBOE",
    "OCTAVE PRINCIPAL",
    "OCTAVE QUINT",
    "OCTAVE STOPPED DIAPASON",
    "OCTAVE TIERCE",
    "OCTAVE TROMBA",
    "OCTAVE TUBA",
    "OCTAVE TWELFTH",
    "OCTAVE VIOL",
    "OCTAVE VIOLA",
    "OCTAVE VIOLE",
    "OCTAVE VIOLIN",
    "OCTAVE WOOD",
    "OCTAVENBASS",
    "OCTAVIN",
    "OCTAVIN HARMONIQUE",
    "OCTAVINA HARMONIQUE",
    "OFFENBASS",
    "OFFENFLÖT",
    "OFFENFLÖTE",
    "OFFENFLÖTENQUINTE",
    "OFFENQUINTFLÖTE",
    "OFFICLEIDE",
    #"OISEAU",
    "OKTAVA",
    "OKTAVCYMBEL",
    "OKTAVENBASS",
    "OKTAVENGEMSHORN",
    "OKTAVENPRINCIPAL",
    "OKTAVZIMBEL",
    "ONDA MARIS",
    "OPEN DIAPASON",
    "OPEN DIAPASON BASS",
    "OPEN TWELFTH",
    "OPEN WOOD",
    "OPHICLEÏD",
    "OPHICLÉIDE",
    #"ORAGE",
    "ORCHESTRAL BASSOON",
    #"ORCHESTRAL BELLS",
    "ORCHESTRAL CLARINET",
    "ORCHESTRAL CORNET",
    "ORCHESTRAL FAGOTTO",
    "ORCHESTRAL FLUTE",
    "ORCHESTRAL HAUTBOY",
    "ORCHESTRAL HORN",
    "ORCHESTRAL OBOE",
    "ORCHESTRAL PICCOLO",
    "ORCHESTRAL SAXOPHONE",
    "ORCHESTRAL STRINGS",
    "ORCHESTRAL TRUMPET",
    "ORCHESTRAL TUBA",
    "ORCHESTRAL VIOLIN",
    "ORCHESTRAL VIOLONCELLO",
    "ORLO",
    "ORLOS",
    "OTTAVA",
    "OTTAVINA",
    "OTTAVINO",
    "PÄANSHORN",
    #"PÁJAROS",
    "PAMMERT",
    "PAN FLUTE",
    "PANDEAN FLUTE",
    "PANFLÖTE",
    "PARADE",
    #"PARADE DRUM",
    "PARFORCE",
    #"PASSARINHOS",
    "PASSUNEN",
    "PASTORITA",
    "PAUERFLÖTE",
    "PAUKE",
    #"PAUKEN",
    #"PAUKERENGEL",
    "PÄURLIN",
    "PEDAL OPEN WOOD",
    "PEDAL PIPES",
    "PEDAL STRING MIXTURE",
    "PEDAL TROMBA",
    "PENTE",
    "PERDUNA",
    #"PERSIAN CYMBAL",
    "PETIT",
    "PETIT BOURDON",
    "PETIT CORNET",
    "PETIT NASARD",
    "PETITE NASARD",
    "PETITE TIERCE",
    "PETITE TROMPETTE",
    "PFEIFE",
    "PFEIFERFLÖTE",
    "PHILOMELA",
    "PHISHARMONIKA",
    "PHOCINX",
    "PHONEUMA",
    "PHYSHARMONICA",
    "PHYSHARMONIKA",
    #"PIANO",
    "PICCOLO",
    "PICCOLO D'AMORE",
    "PICCOLO HARMONIQUE",
    "PIFANO",
    "PIFFARA",
    "PIFFARO",
    "PIFFERO",
    "PILEATA",
    "PILEATA DIAPENTE",
    "PILEATA MAGNA",
    "PILEATA MAJOR",
    "PILEATA MAXIMA",
    "PILEATA MINIMA",
    "PILEATA MINOR",
    "PILGERCHOR",
    "PLEIN JEU",
    "PLEIN JEU HARMONIQUE",
    "PLOCHFLÖT",
    "PLOCHFLÖTE",
    "PLOCKPFEIFE",
    "POMART",
    "POMBARDA",
    "POMBART",
    "POMMER",
    "POMMER GEDACKT",
    "PONTIFICAL TRUMPET",
    "PORTUNAL",
    "PORTUNAL FLUTE",
    "PORTUNALFLÖTE",
    "PORTUNEN",
    "POSAUNBASS",
    "POSAUNE",
    "POSAUNENBASS",
    "POSAUNENBASS CHORMASS",
    "POSAUNENBASS UNTERCHORMASS",
    "POSAUNENCHORMASSBASS",
    "POSAUNENUNTERCHORBASS",
    "POSITIE",
    "POSITIEN",
    "POSITION",
    "POST HORN",
    "PRAESTANT",
    "PRÄSTANT",
    "PRESSIOR",
    "PRESTANT",
    "PRIMARIA",
    "PRIMARIA REGULA",
    "PRINCIPAAL",
    "PRINCIPAL",
    "PRINCIPAL AMABILE",
    "PRINCIPAL BASSE",
    "PRINCIPAL FLUTE",
    "PRINCIPAL MIXTURE",
    "PRINCIPAL OCTAVE",
    "PRINCIPALBASS",
    "PRINCIPALDISCANT",
    "PRINCIPALE",
    "PRINCIPALE BASSO",
    "PRINCIPALE DOPPIO",
    "PRINCIPALFLÖTE",
    "PRINCIPALINO",
    "PRINZIPAL",
    "PRINZIPALBASS",
    "PRINZIPALDISKANT",
    "PRINZIPALFLÖTE",
    #"PRO FORMA",
    "PROGRESSIO",
    "PROGRESSIO HARMONICA",
    "PUSAUN",
    "PYRAMID DIAPASON",
    "PYRAMID FLUTE",
    "PYRAMIDAL FLUTE",
    "PYRAMIDFLÖTE",
    "PYRAMIDON",
    "QUADRAGESIMA",
    "QUADRAGESIMA TERZA",
    "QUARTA",
    "QUARTA DECIMA",
    "QUARTAIN",
    "QUARTANE",
    "QUARTE",
    "QUARTE DE NASARD",
    "QUARTE DE NAZARD",
    "QUERFLOIT",
    "QUERFLÖTE",
    "QUERFLÖTENBASS",
    "QUERPFEIFE",
    "QUERPIPE",
    "QUIET GEDACKT",
    "QUINCENA",
    "QUINDECIMA",
    "QUINT",
    "QUINT BASS",
    "QUINT DE TONO",
    "QUINT DIAPASON",
    "QUINT FLUTE",
    "QUINT MIXTURE",
    "QUINT TROMBONE",
    "QUINT TRUMPET",
    "QUINT VIOLA",
    "QUINTA",
    "QUINTA AD UNA",
    "QUINTADE",
    "QUINTADECIMA",
    "QUINTADEEN",
    "QUINTADEENS",
    "QUINTADEHN",
    "QUINTADEMA",
    "QUINTADEN",
    "QUINTADENA",
    "QUINTADENA CELESTE",
    "QUINTADENE",
    "QUINTADINER",
    "QUINTADON",
    "QUINTALOPHON",
    "QUINTANUS",
    "QUINTAPHON",
    "QUINTAPHONE",
    "QUINTATEN",
    "QUINTATHÖN",
    "QUINTATON",
    "QUINTATÖNBASS",
    "QUINTATÖNSUBBASS",
    "QUINTBASS",
    "QUINTE",
    "QUINTE BOMBARDE",
    "QUINTE FLUTE",
    "QUINTE OUVERTE",
    "QUINTE VIOLA",
    "QUINTENBASS",
    "QUINTENOR",
    "QUINTET BASS",
    "QUINTFLÖTE",
    "QUINTFLUIT",
    "QUINTFLUTE",
    "QUINTGEMSHORN",
    "QUINTGETÖN",
    "QUINTIDEN",
    "QUINTITEN",
    "QUINTITENENS",
    "QUINTNASAT",
    "QUINTSPITZ",
    "QUINTVIOLE",
    "QUINZIÈME",
    "RACKET",
    "RACKETT",
    #"RAIN",
    "RANKET",
    "RANKETT",
    "RANQUET",
    "RANQUETTE",
    "RAUSCHCIMBEL",
    "RAUSCHENDE ZIMBEL",
    "RAUSCHFLÖTE",
    "RAUSCHMIXTUR",
    "RAUSCHPFEIFE",
    "RAUSCHPFEIFFE",
    "RAUSCHQUARTE",
    "RAUSCHQUINTE",
    "RAUSCHWERK",
    "RAUSCHZIMBEL",
    #"RECHTE HEERTRUMMEL",
    "RECORDER",
    "RECORDOR",
    "REGAAL",
    "REGAL",
    "REGALE",
    "REGALIAS",
    "REGULA",
    "REGULA MINIMA",
    "REGULA MINOR",
    "REGULA MIXTA",
    "REGULA PRIMARIA",
    "REIM",
    "REINFORZA A LIGNE",
    "RELIQUA",
    "REPETIRENDER CYMBEL",
    "RESIMBALA",
    #"REST",
    "RESULTANT",
    "RESULTANT BASS",
    "RINFORZO A LINGUE",
    "RIPIENFLÖTE",
    "RIPIENO",
    "RIPIENO DI CINQUE",
    "ROERFLUIT",
    "ROERQUINT",
    "ROHR FLUTE",
    "ROHR NASAT",
    "ROHR SCHALMEI",
    "ROHR SCHALMEY",
    "ROHRBORDUN",
    "ROHRBOURDON",
    "ROHRFLÖTE",
    "ROHRFLÖTENBASS",
    "ROHRFLÖTENQUINTE",
    "ROHRFLÖTQUINT",
    "ROHRGEDACKT",
    "ROHRGEDECKT",
    "ROHRGEDECKTPOMMER",
    "ROHRNASAT",
    "ROHRPFEIFE",
    "ROHRPOMMER",
    "ROHRQUINTE",
    "ROHRQUINTADEN",
    "ROHRQUINTADENA",
    "ROHRQUINTATON",
    "ROHRQUINTE",
    "ROHRSCHALMEI",
    "ROHRSCHELLE",
    "RORFLOJTE",
    "ROSIGNOLO",
    "ROSSIGNOL",
    "RUSSZIMBEL"
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
