
def get_interval_name(value):
    match value:
        case 0:
            return "Perfect unison"
        case 1:
            return "Minor second"
        case 2:
            return "Major second"
        case 3:
            return "Minor third"
        case 4:
            return "Major third"
        case 5:
            return "Perfect fourth"
        case 6:
            return "Tritone"
        case 7:
            return "Perfect fifth"
        case 8:
            return "Minor sixth"
        case 9:
            return "Major sixth"
        case 10:
            return "Minor seventh"
        case 11:
            return "Major seventh"
        case 12:
            return "Perfect octave"
        case _:
            return "Unknown interval"


def get_compound_interval_name(value):
    match value:
        case 0:
            return "Minor ninth"
        case 1:
            return "Major ninth"
        case 2:
            return "Minor tenth"
        case 3:
            return "Major tenth"
        case 4:
            return "Perfect eleventh"
        case 5:
            return "Augmented eleventh / Diminished twelfth"
        case 6:
            return "Perfect twelfth"
        case 7:
            return "Minor thirteenth"
        case 8:
            return "Major thirteenth"
        case 9:
            return "Minor fourteenth"
        case 10:
            return "Major fourteenth"
        case 11:
            return "Perfect fifteenth"
        case 12:
            return "Double octave"
        case _:
            return "Unknown interval"


def get_triad_name(value):
    match value:
        case 0:
            return "Major triad root position"
        case 1:
            return "Major triad first inversion"
        case 2:
            return "Major triad second inversion"
        case 3:
            return "Minor triad root position"
        case 4:
            return "Minor triad first inversion"
        case 5:
            return "Minor triad second inversion"
        case 6:
            return "Diminished triad root position"
        case 7:
            return "Diminished triad first inversion"
        case 8:
            return "Diminished triad second inversion"
        case 9:
            return "Augmented triad"
        case _:
            return "Unknown triad"


def get_d7_name(value):
    match value:
        case 0:
            return "D7 root position"
        case 1:
            return "D7 first inversion"
        case 2:
            return "D7 second inversion"
        case 3:
            return "D7 third inversion"
        case _:
            return "Unknown chord"


def get_d9_name(value):
    match value:
        case 0:
            return "D9 with major second"
        case 1:
            return "D9 with minor second"
        case _:
            return "Unknown chord"
