from enum import Enum

class Intervals(Enum):
    PERFECT_UNISON = 0
    MINOR_SECOND = 1
    MAJOR_SECOND = 2
    MINOR_THIRD = 3
    MAJOR_THIRD = 4
    PERFECT_FOURTH = 5
    TRITONE = 6
    PERFECT_FIFTH = 7
    MINOR_SIXTH = 8
    MAJOR_SIXTH = 9
    MINOR_SEVENTH = 10
    MAJOR_SEVENTH = 11
    PERFECT_OCTAVE = 12
    MINOR_NINTH = 13
    MAJOR_NINTH = 14
    MINOR_TENTH = 15
    MAJOR_TENTH = 16
    PERFECT_ELEVENTH = 17
    AUGMENTED_ELEVENTH = 18
    PERFECT_TWELFTH = 19
    MINOR_THIRTEENTH = 20
    MAJOR_THIRTEENTH = 21
    MINOR_FOURTEENTH = 22
    MAJOR_FOURTEENTH = 23
    PERFECT_FIFTEENTH = 24

def get_interval_name(self):
    match self.value:
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
        case 13:
            return "Minor ninth"
        case 14:
            return "Major ninth"
        case 15:
            return "Minor tenth"
        case 16:
            return "Major tenth"
        case 17:
            return "Perfect eleventh"
        case 18:
            return "Augmented eleventh / Diminished twelfth"
        case 19:
            return "Perfect twelfth"
        case 20:
            return "Minor thirteenth"
        case 21:
            return "Major thirteenth"
        case 22:
            return "Minor fourteenth"
        case 23:
            return "Major fourteenth"
        case 24:
            return "Perfect fifteenth"
        case _:
            return "Unknown interval"
