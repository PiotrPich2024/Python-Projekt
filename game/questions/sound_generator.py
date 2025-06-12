import pygame.midi
import time


# INTERVALS
def play_interval_harmonic(root_note, duration, interval_semitones, instrument, engine):
    pygame.midi.init()
    player = pygame.midi.Output(0)
    player.set_instrument(instrument)

    player.note_on(root_note, 127)
    player.note_on(root_note + interval_semitones, 127)
    time.sleep(duration)
    player.note_off(root_note, 127)
    player.note_on(root_note + interval_semitones, 127)

    player.close()
    pygame.midi.quit()
    engine.set_is_playing(False)


def play_interval_melodic_up(root_note, duration, interval_semitones, instrument, engine):
    pygame.midi.init()
    player = pygame.midi.Output(0)
    player.set_instrument(instrument)

    player.note_on(root_note, 127)
    time.sleep(duration / 2)
    player.note_off(root_note, 127)
    player.note_on(root_note + interval_semitones, 127)
    time.sleep(duration / 2)
    player.note_off(root_note + interval_semitones, 127)

    player.close()
    pygame.midi.quit()
    engine.set_is_playing(False)


def play_interval_melodic_down(root_note, duration, interval_semitones, instrument, engine):
    pygame.midi.init()
    player = pygame.midi.Output(0)
    player.set_instrument(instrument)

    player.note_on(root_note + interval_semitones, 127)
    time.sleep(duration / 2)
    player.note_off(root_note + interval_semitones, 127)
    player.note_on(root_note, 127)
    time.sleep(duration / 2)
    player.note_off(root_note, 127)

    player.close()
    pygame.midi.quit()
    engine.set_is_playing(False)


def play_compound_interval_harmonic(root_note, duration, interval_semitones, instrument, engine):
    pygame.midi.init()
    player = pygame.midi.Output(0)
    player.set_instrument(instrument)

    player.note_on(root_note, 127)
    player.note_on(root_note + interval_semitones + 12, 127)
    time.sleep(duration)
    player.note_off(root_note, 127)
    player.note_on(root_note + interval_semitones + 12, 127)

    player.close()
    pygame.midi.quit()
    engine.set_is_playing(False)


def play_compound_interval_melodic_up(root_note, duration, interval_semitones, instrument, engine):
    pygame.midi.init()
    player = pygame.midi.Output(0)
    player.set_instrument(instrument)

    player.note_on(root_note, 127)
    time.sleep(duration / 2)
    player.note_off(root_note, 127)
    player.note_on(root_note + interval_semitones + 12, 127)
    time.sleep(duration / 2)
    player.note_off(root_note + interval_semitones + 12, 127)

    player.close()
    pygame.midi.quit()
    engine.set_is_playing(False)


def play_compound_interval_melodic_down(root_note, duration, interval_semitones, instrument, engine):
    pygame.midi.init()
    player = pygame.midi.Output(0)
    player.set_instrument(instrument)

    player.note_on(root_note + interval_semitones + 12, 127)
    time.sleep(duration / 2)
    player.note_off(root_note + interval_semitones + 12, 127)
    player.note_on(root_note, 127)
    time.sleep(duration / 2)
    player.note_off(root_note, 127)

    player.close()
    pygame.midi.quit()
    engine.set_is_playing(False)


# CHORDS
def play_harmonic(notes, player, duration):
    for note in notes:
        player.note_on(note, 127)

    time.sleep(duration)

    for note in notes:
        player.note_off(note, 127)


def play_melodic(notes, player, duration):
    for note in notes:
        player.note_on(note, 127)
        time.sleep(duration / len(notes))
        player.note_off(note, 127)


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


def play_death():
    pygame.midi.init()
    player = pygame.midi.Output(0)
    instrument = 50
    player.set_instrument(instrument)

    player.note_on(60, 127)
    player.note_on(61, 127)
    player.note_on(62, 127)
    time.sleep(3.0)
    player.note_off(60, 127)
    player.note_off(61, 127)
    player.note_off(62, 127)

    player.close()
    pygame.midi.quit()
