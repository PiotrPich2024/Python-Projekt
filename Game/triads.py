from enum import Enum

class Triads(Enum):
    MAJOR_ROOT_POSITION = 0
    MAJOR_FIRST_INVERSION = 1
    MAJOR_SECOND_INVERSION = 2
    MINOR_ROOT_POSITION = 3
    MINOR_FIRST_INVERSION = 4
    MINOR_SECOND_INVERSION = 5
    DIMINISHED_ROOT_POSITION = 6
    DIMINISHED_FIRST_INVERSION = 7
    DIMINISHED_SECOND_INVERSION = 8
    AUGMENTED = 9


def get_triad_name(self):
    match self.value:
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


