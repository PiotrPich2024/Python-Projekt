import pygame.midi
import time


def play_harmonic(notes, player, duration):
    for note in notes:
        player.note_on(note, 127)

    time.sleep(duration)

    for note in notes:
        player.note_off(note, 127)

    time.sleep(0.5)


def play_melodic(notes, player, duration):
    for note in notes:
        player.note_on(note, 127)
        time.sleep(duration / len(notes))
        player.note_off(note, 127)

    time.sleep(0.5)


# INTERVALS
def play_interval(name, root_note, duration, interval_code, instrument, engine):
    pygame.midi.init()
    player = pygame.midi.Output(0)
    player.set_instrument(instrument)

    match name:
        case "interval_harmonic":
            play_harmonic([root_note, root_note + interval_code], player, duration)
        case "interval_melodic_up":
            play_melodic([root_note, root_note + interval_code], player, duration)
        case "interval_melodic_down":
            play_melodic([root_note + interval_code, root_note], player, duration)
        case "compound_interval_harmonic":
            play_harmonic([root_note, root_note + interval_code + 12], player, duration)
        case "compound_interval_melodic_up":
            play_melodic([root_note, root_note + interval_code + 12], player, duration)
        case "compound_interval_melodic_down":
            play_melodic([root_note + interval_code + 12, root_note], player, duration)

    player.close()
    pygame.midi.quit()
    engine.set_is_playing(False)


# CHORDS
def play_chord(name, root_note, duration, instrument, engine):
    pygame.midi.init()
    player = pygame.midi.Output(0)
    player.set_instrument(instrument)

    match name:
        case "major_root_position_harmonic":
            play_harmonic([root_note, root_note + 4, root_note + 7], player, duration)
        case "major_root_position_melodic_up":
            play_melodic([root_note, root_note + 4, root_note + 7], player, duration)
        case "major_root_position_melodic_down":
            play_melodic([root_note + 7, root_note + 4, root_note], player, duration)
        case "minor_root_position_harmonic":
            play_harmonic([root_note, root_note + 3, root_note + 7], player, duration)
        case "minor_root_position_melodic_up":
            play_melodic([root_note, root_note + 3, root_note + 7], player, duration)
        case "minor_root_position_melodic_down":
            play_melodic([root_note + 7, root_note + 3, root_note], player, duration)
        case "major_first_inversion_harmonic":
            play_harmonic([root_note, root_note + 3, root_note + 8], player, duration)
        case "major_first_inversion_melodic_up":
            play_melodic([root_note, root_note + 3, root_note + 8], player, duration)
        case "major_first_inversion_melodic_down":
            play_melodic([root_note + 8, root_note + 3, root_note], player, duration)
        case "minor_first_inversion_harmonic":
            play_harmonic([root_note, root_note + 4, root_note + 9], player, duration)
        case "minor_first_inversion_melodic_up":
            play_melodic([root_note, root_note + 4, root_note + 9], player, duration)
        case "minor_first_inversion_melodic_down":
            play_melodic([root_note + 9, root_note + 4, root_note], player, duration)
        case "major_second_inversion_harmonic":
            play_harmonic([root_note, root_note + 5, root_note + 9], player, duration)
        case "major_second_inversion_melodic_up":
            play_melodic([root_note, root_note + 5, root_note + 9], player, duration)
        case "major_second_inversion_melodic_down":
            play_melodic([root_note + 9, root_note + 5, root_note], player, duration)
        case "minor_second_inversion_harmonic":
            play_harmonic([root_note, root_note + 5, root_note + 8], player, duration)
        case "minor_second_inversion_melodic_up":
            play_melodic([root_note, root_note + 5, root_note + 8], player, duration)
        case "minor_second_inversion_melodic_down":
            play_melodic([root_note + 8, root_note + 5, root_note], player, duration)
        case "augmented_harmonic":
            play_harmonic([root_note, root_note + 4, root_note + 8], player, duration)
        case "augmented_melodic_up":
            play_melodic([root_note, root_note + 4, root_note + 8], player, duration)
        case "augmented_melodic_down":
            play_melodic([root_note + 8, root_note + 4, root_note], player, duration)
        case "diminished_root_position_harmonic":
            play_harmonic([root_note, root_note + 3, root_note + 6], player, duration)
        case "diminished_root_position_melodic_up":
            play_melodic([root_note, root_note + 3, root_note + 6], player, duration)
        case "diminished_root_position_melodic_down":
            play_melodic([root_note + 6, root_note + 3, root_note], player, duration)
        case "diminished_first_inversion_harmonic":
            play_harmonic([root_note, root_note + 3, root_note + 9], player, duration)
        case "diminished_first_inversion_melodic_up":
            play_melodic([root_note, root_note + 3, root_note + 9], player, duration)
        case "diminished_first_inversion_melodic_down":
            play_melodic([root_note + 9, root_note + 3, root_note], player, duration)
        case "diminished_second_inversion_harmonic":
            play_harmonic([root_note, root_note + 6, root_note + 9], player, duration)
        case "diminished_second_inversion_melodic_up":
            play_melodic([root_note, root_note + 6, root_note + 9], player, duration)
        case "diminished_second_inversion_melodic_down":
            play_melodic([root_note + 9, root_note + 6, root_note], player, duration)
        case "d7_root_position_harmonic":
            play_harmonic([root_note, root_note + 4, root_note + 7, root_note + 10], player, duration)
        case "d7_root_position_melodic_up":
            play_melodic([root_note, root_note + 4, root_note + 7, root_note + 10], player, duration)
        case "d7_root_position_melodic_down":
            play_melodic([root_note + 10, root_note + 7, root_note + 4, root_note], player, duration)
        case "d7_first_inversion_harmonic":
            play_harmonic([root_note, root_note + 3, root_note + 6, root_note + 8], player, duration)
        case "d7_first_inversion_melodic_up":
            play_melodic([root_note, root_note + 3, root_note + 6, root_note + 8], player, duration)
        case "d7_first_inversion_melodic_down":
            play_melodic([root_note + 8, root_note + 6, root_note + 3, root_note], player, duration)
        case "d7_second_inversion_harmonic":
            play_harmonic([root_note, root_note + 3, root_note + 5, root_note + 9], player, duration)
        case "d7_second_inversion_melodic_up":
            play_melodic([root_note, root_note + 3, root_note + 5, root_note + 9], player, duration)
        case "d7_second_inversion_melodic_down":
            play_melodic([root_note + 9, root_note + 5, root_note + 3, root_note], player, duration)
        case "d7_third_inversion_harmonic":
            play_harmonic([root_note, root_note + 2, root_note + 6, root_note + 9], player, duration)
        case "d7_third_inversion_melodic_up":
            play_melodic([root_note, root_note + 2, root_note + 6, root_note + 9], player, duration)
        case "d7_third_inversion_melodic_down":
            play_melodic([root_note + 9, root_note + 6, root_note + 2, root_note], player, duration)
        case "d9_with_major_second_harmonic":
            play_harmonic([root_note, root_note + 4, root_note + 7, root_note + 10, root_note + 14], player, duration)
        case "d9_with_major_second_melodic_up":
            play_melodic([root_note, root_note + 4, root_note + 7, root_note + 10, root_note + 14], player, duration)
        case "d9_with_major_second_melodic_down":
            play_melodic([root_note + 14, root_note + 10, root_note + 7, root_note + 4, root_note], player, duration)
        case "d9_with_minor_second_harmonic":
            play_harmonic([root_note, root_note + 4, root_note + 7, root_note + 10, root_note + 13], player, duration)
        case "d9_with_minor_second_melodic_up":
            play_melodic([root_note, root_note + 4, root_note + 7, root_note + 10, root_note + 13], player, duration)
        case "d9_with_minor_second_melodic_down":
            play_melodic([root_note + 13, root_note + 10, root_note + 7, root_note + 4, root_note], player, duration)

    player.close()
    pygame.midi.quit()
    engine.set_is_playing(False)
