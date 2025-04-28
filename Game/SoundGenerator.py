# import numpy as np
# import sounddevice as sd
#
# def play_note(freq, duration=0.5, sample_rate=44100):
#     t = np.linspace(0, duration, int(sample_rate * duration), False)
#     note = np.sin(freq * 2 * np.pi * t)
#     sd.play(note, samplerate=sample_rate)
#     sd.wait()
#
# # Przykład: nuta A4 (440 Hz)
#
# play_note(220)
# play_note(440)
# play_note(880)
# play_note(1760)


import pygame.midi
import time


def play_interval_harmonic(root_note, duration, interval_semitones, instrument = 0):
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


def play_interval_melodic_up(root_note, duration, interval_semitones, instrument = 0):
    pygame.midi.init()
    player = pygame.midi.Output(0)
    player.set_instrument(instrument)

    player.note_on(root_note, 127)
    time.sleep(duration / 2)
    player.note_off(root_note, 127)
    player.note_on(root_note + interval_semitones, 127)
    time.sleep(duration / 2)
    player.note_on(root_note + interval_semitones, 127)

    player.close()
    pygame.midi.quit()


def play_interval_melodic_down(root_note, duration, interval_semitones, instrument = 0):
    pygame.midi.init()
    player = pygame.midi.Output(0)
    player.set_instrument(instrument)

    player.note_on(root_note + interval_semitones, 127)
    time.sleep(duration / 2)
    player.note_on(root_note + interval_semitones, 127)
    player.note_on(root_note, 127)
    time.sleep(duration / 2)
    player.note_off(root_note, 127)

    player.close()
    pygame.midi.quit()


def play_major_root_position_harmonic(root_note, duration, instrument = 0):
    pygame.midi.init()
    player = pygame.midi.Output(0)
    player.set_instrument(instrument)

    player.note_on(root_note, 127)
    player.note_on(root_note + 4, 127)
    player.note_on(root_note + 7, 127)
    time.sleep(duration)
    player.note_off(root_note, 127)
    player.note_off(root_note + 4, 127)
    player.note_off(root_note + 7, 127)

    player.close()
    pygame.midi.quit()


def play_major_root_position_melodic_up(root_note, duration, instrument = 0):
    pygame.midi.init()
    player = pygame.midi.Output(0)
    player.set_instrument(instrument)

    player.note_on(root_note, 127)
    time.sleep(duration / 3)
    player.note_off(root_note, 127)
    player.note_on(root_note + 4, 127)
    time.sleep(duration / 3)
    player.note_off(root_note + 4, 127)
    player.note_on(root_note + 7, 127)
    time.sleep(duration / 3)
    player.note_off(root_note + 7, 127)

    player.close()
    pygame.midi.quit()


def play_major_root_position_melodic_down(root_note, duration, instrument = 0):
    pygame.midi.init()
    player = pygame.midi.Output(0)
    player.set_instrument(instrument)

    player.note_on(root_note + 7, 127)
    time.sleep(duration / 3)
    player.note_off(root_note + 7, 127)
    player.note_on(root_note + 4, 127)
    time.sleep(duration / 3)
    player.note_off(root_note + 4, 127)
    player.note_on(root_note, 127)
    time.sleep(duration / 3)
    player.note_off(root_note, 127)

    player.close()
    pygame.midi.quit()


def play_minor_root_position_harmonic(root_note, duration, instrument = 0):
    pygame.midi.init()
    player = pygame.midi.Output(0)
    player.set_instrument(instrument)

    player.note_on(root_note, 127)
    player.note_on(root_note + 3, 127)
    player.note_on(root_note + 7, 127)
    time.sleep(duration)
    player.note_off(root_note, 127)
    player.note_off(root_note + 3, 127)
    player.note_off(root_note + 7, 127)

    player.close()
    pygame.midi.quit()


def play_minor_root_position_melodic_up(root_note, duration, instrument = 0):
    pygame.midi.init()
    player = pygame.midi.Output(0)
    player.set_instrument(instrument)

    player.note_on(root_note, 127)
    time.sleep(duration / 3)
    player.note_off(root_note, 127)
    player.note_on(root_note + 3, 127)
    time.sleep(duration / 3)
    player.note_off(root_note + 3, 127)
    player.note_on(root_note + 7, 127)
    time.sleep(duration / 3)
    player.note_off(root_note + 7, 127)

    player.close()
    pygame.midi.quit()


def play_minor_root_position_melodic_down(root_note, duration, instrument = 0):
    pygame.midi.init()
    player = pygame.midi.Output(0)
    player.set_instrument(instrument)

    player.note_on(root_note + 7, 127)
    time.sleep(duration / 3)
    player.note_off(root_note + 7, 127)
    player.note_on(root_note + 3, 127)
    time.sleep(duration / 3)
    player.note_off(root_note + 3, 127)
    player.note_on(root_note, 127)
    time.sleep(duration / 3)
    player.note_off(root_note, 127)

    player.close()
    pygame.midi.quit()


def play_major_first_inversion_harmonic(root_note, duration, instrument = 0):
    pygame.midi.init()
    player = pygame.midi.Output(0)
    player.set_instrument(instrument)

    player.note_on(root_note, 127)
    player.note_on(root_note + 3, 127)
    player.note_on(root_note + 8, 127)
    time.sleep(duration)
    player.note_off(root_note, 127)
    player.note_off(root_note + 3, 127)
    player.note_off(root_note + 8, 127)

    player.close()
    pygame.midi.quit()


def play_major_first_inversion_melodic_up(root_note, duration, instrument = 0):
    pygame.midi.init()
    player = pygame.midi.Output(0)
    player.set_instrument(instrument)

    player.note_on(root_note, 127)
    time.sleep(duration / 3)
    player.note_off(root_note, 127)
    player.note_on(root_note + 3, 127)
    time.sleep(duration / 3)
    player.note_off(root_note + 3, 127)
    player.note_on(root_note + 8, 127)
    time.sleep(duration / 3)
    player.note_off(root_note + 8, 127)

    player.close()
    pygame.midi.quit()


def play_major_first_inversion_melodic_down(root_note, duration, instrument = 0):
    pygame.midi.init()
    player = pygame.midi.Output(0)
    player.set_instrument(instrument)

    player.note_on(root_note + 8, 127)
    time.sleep(duration / 3)
    player.note_off(root_note + 8, 127)
    player.note_on(root_note + 3, 127)
    time.sleep(duration / 3)
    player.note_off(root_note + 3, 127)
    player.note_on(root_note, 127)
    time.sleep(duration / 3)
    player.note_off(root_note, 127)

    player.close()
    pygame.midi.quit()


def play_minor_first_inversion_harmonic(root_note, duration, instrument = 0):
    pygame.midi.init()
    player = pygame.midi.Output(0)
    player.set_instrument(instrument)

    player.note_on(root_note, 127)
    player.note_on(root_note + 4, 127)
    player.note_on(root_note + 9, 127)
    time.sleep(duration)
    player.note_off(root_note, 127)
    player.note_off(root_note + 4, 127)
    player.note_off(root_note + 9, 127)

    player.close()
    pygame.midi.quit()


def play_minor_first_inversion_melodic_up(root_note, duration, instrument = 0):
    pygame.midi.init()
    player = pygame.midi.Output(0)
    player.set_instrument(instrument)

    player.note_on(root_note, 127)
    time.sleep(duration / 3)
    player.note_off(root_note, 127)
    player.note_on(root_note + 4, 127)
    time.sleep(duration / 3)
    player.note_off(root_note + 4, 127)
    player.note_on(root_note + 9, 127)
    time.sleep(duration / 3)
    player.note_off(root_note + 9, 127)

    player.close()
    pygame.midi.quit()


def play_minor_first_inversion_melodic_down(root_note, duration, instrument = 0):
    pygame.midi.init()
    player = pygame.midi.Output(0)
    player.set_instrument(instrument)

    player.note_on(root_note + 9, 127)
    time.sleep(duration / 3)
    player.note_off(root_note + 9, 127)
    player.note_on(root_note + 4, 127)
    time.sleep(duration / 3)
    player.note_off(root_note + 4, 127)
    player.note_on(root_note, 127)
    time.sleep(duration / 3)
    player.note_off(root_note, 127)

    player.close()
    pygame.midi.quit()


def play_major_second_inversion_harmonic(root_note, duration, instrument = 0):
    pygame.midi.init()
    player = pygame.midi.Output(0)
    player.set_instrument(instrument)

    player.note_on(root_note, 127)
    player.note_on(root_note + 5, 127)
    player.note_on(root_note + 9, 127)
    time.sleep(duration)
    player.note_off(root_note, 127)
    player.note_off(root_note + 5, 127)
    player.note_off(root_note + 9, 127)

    player.close()
    pygame.midi.quit()


def play_major_second_inversion_melodic_up(root_note, duration, instrument = 0):
    pygame.midi.init()
    player = pygame.midi.Output(0)
    player.set_instrument(instrument)

    player.note_on(root_note, 127)
    time.sleep(duration / 3)
    player.note_off(root_note, 127)
    player.note_on(root_note + 5, 127)
    time.sleep(duration / 3)
    player.note_off(root_note + 5, 127)
    player.note_on(root_note + 9, 127)
    time.sleep(duration / 3)
    player.note_off(root_note + 9, 127)

    player.close()
    pygame.midi.quit()


def play_major_second_inversion_melodic_down(root_note, duration, instrument = 0):
    pygame.midi.init()
    player = pygame.midi.Output(0)
    player.set_instrument(instrument)

    player.note_on(root_note + 9, 127)
    time.sleep(duration / 3)
    player.note_off(root_note + 9, 127)
    player.note_on(root_note + 5, 127)
    time.sleep(duration / 3)
    player.note_off(root_note + 5, 127)
    player.note_on(root_note, 127)
    time.sleep(duration / 3)
    player.note_off(root_note, 127)

    player.close()
    pygame.midi.quit()


def play_minor_second_inversion_harmonic(root_note, duration, instrument = 0):
    pygame.midi.init()
    player = pygame.midi.Output(0)
    player.set_instrument(instrument)

    player.note_on(root_note, 127)
    player.note_on(root_note + 5, 127)
    player.note_on(root_note + 8, 127)
    time.sleep(duration)
    player.note_off(root_note, 127)
    player.note_off(root_note + 5, 127)
    player.note_off(root_note + 8, 127)

    player.close()
    pygame.midi.quit()


def play_minor_second_inversion_melodic_up(root_note, duration, instrument = 0):
    pygame.midi.init()
    player = pygame.midi.Output(0)
    player.set_instrument(instrument)

    player.note_on(root_note, 127)
    time.sleep(duration / 3)
    player.note_off(root_note, 127)
    player.note_on(root_note + 5, 127)
    time.sleep(duration / 3)
    player.note_off(root_note + 5, 127)
    player.note_on(root_note + 8, 127)
    time.sleep(duration / 3)
    player.note_off(root_note + 8, 127)

    player.close()
    pygame.midi.quit()


def play_minor_second_inversion_melodic_down(root_note, duration, instrument = 0):
    pygame.midi.init()
    player = pygame.midi.Output(0)
    player.set_instrument(instrument)

    player.note_on(root_note + 8, 127)
    time.sleep(duration / 3)
    player.note_off(root_note + 8, 127)
    player.note_on(root_note + 5, 127)
    time.sleep(duration / 3)
    player.note_off(root_note + 5, 127)
    player.note_on(root_note, 127)
    time.sleep(duration / 3)
    player.note_off(root_note, 127)

    player.close()
    pygame.midi.quit()


def play_augmented_harmonic(root_note, duration, instrument = 0):
    pygame.midi.init()
    player = pygame.midi.Output(0)
    player.set_instrument(instrument)

    player.note_on(root_note, 127)
    player.note_on(root_note + 4, 127)
    player.note_on(root_note + 8, 127)
    time.sleep(duration)
    player.note_off(root_note, 127)
    player.note_off(root_note + 4, 127)
    player.note_off(root_note + 8, 127)

    player.close()
    pygame.midi.quit()


def play_augmented_melodic_up(root_note, duration, instrument = 0):
    pygame.midi.init()
    player = pygame.midi.Output(0)
    player.set_instrument(instrument)

    player.note_on(root_note, 127)
    time.sleep(duration / 3)
    player.note_off(root_note, 127)
    player.note_on(root_note + 4, 127)
    time.sleep(duration / 3)
    player.note_off(root_note + 4, 127)
    player.note_on(root_note + 8, 127)
    time.sleep(duration / 3)
    player.note_off(root_note + 8, 127)

    player.close()
    pygame.midi.quit()


def play_augmented_melodic_down(root_note, duration, instrument = 0):
    pygame.midi.init()
    player = pygame.midi.Output(0)
    player.set_instrument(instrument)

    player.note_on(root_note + 8, 127)
    time.sleep(duration / 3)
    player.note_off(root_note + 8, 127)
    player.note_on(root_note + 4, 127)
    time.sleep(duration / 3)
    player.note_off(root_note + 4, 127)
    player.note_on(root_note, 127)
    time.sleep(duration / 3)
    player.note_off(root_note, 127)

    player.close()
    pygame.midi.quit()


def play_diminished_root_position_harmonic(root_note, duration, instrument=0):
    pygame.midi.init()
    player = pygame.midi.Output(0)
    player.set_instrument(instrument)

    player.note_on(root_note, 127)
    player.note_on(root_note + 3, 127)
    player.note_on(root_note + 6, 127)
    time.sleep(duration)
    player.note_off(root_note, 127)
    player.note_off(root_note + 3, 127)
    player.note_off(root_note + 6, 127)

    player.close()
    pygame.midi.quit()


def play_diminished_root_position_melodic_up(root_note, duration, instrument=0):
    pygame.midi.init()
    player = pygame.midi.Output(0)
    player.set_instrument(instrument)

    player.note_on(root_note, 127)
    time.sleep(duration / 3)
    player.note_off(root_note, 127)
    player.note_on(root_note + 3, 127)
    time.sleep(duration / 3)
    player.note_off(root_note + 3, 127)
    player.note_on(root_note + 6, 127)
    time.sleep(duration / 3)
    player.note_off(root_note + 6, 127)

    player.close()
    pygame.midi.quit()


def play_diminished_root_position_melodic_down(root_note, duration, instrument=0):
    pygame.midi.init()
    player = pygame.midi.Output(0)
    player.set_instrument(instrument)

    player.note_on(root_note + 6, 127)
    time.sleep(duration / 3)
    player.note_off(root_note + 6, 127)
    player.note_on(root_note + 3, 127)
    time.sleep(duration / 3)
    player.note_off(root_note + 3, 127)
    player.note_on(root_note, 127)
    time.sleep(duration / 3)
    player.note_off(root_note, 127)

    player.close()
    pygame.midi.quit()


def play_diminished_first_inversion_harmonic(root_note, duration, instrument=0):
    pygame.midi.init()
    player = pygame.midi.Output(0)
    player.set_instrument(instrument)

    player.note_on(root_note, 127)
    player.note_on(root_note + 3, 127)
    player.note_on(root_note + 9, 127)
    time.sleep(duration)
    player.note_off(root_note, 127)
    player.note_off(root_note + 3, 127)
    player.note_off(root_note + 9, 127)

    player.close()
    pygame.midi.quit()


def play_diminished_first_inversion_melodic_up(root_note, duration, instrument=0):
    pygame.midi.init()
    player = pygame.midi.Output(0)
    player.set_instrument(instrument)

    player.note_on(root_note, 127)
    time.sleep(duration / 3)
    player.note_off(root_note, 127)
    player.note_on(root_note + 3, 127)
    time.sleep(duration / 3)
    player.note_off(root_note + 3, 127)
    player.note_on(root_note + 9, 127)
    time.sleep(duration / 3)
    player.note_off(root_note + 9, 127)

    player.close()
    pygame.midi.quit()


def play_diminished_first_inversion_melodic_down(root_note, duration, instrument=0):
    pygame.midi.init()
    player = pygame.midi.Output(0)
    player.set_instrument(instrument)

    player.note_on(root_note + 9, 127)
    time.sleep(duration / 3)
    player.note_off(root_note + 9, 127)
    player.note_on(root_note + 3, 127)
    time.sleep(duration / 3)
    player.note_off(root_note + 3, 127)
    player.note_on(root_note, 127)
    time.sleep(duration / 3)
    player.note_off(root_note, 127)

    player.close()
    pygame.midi.quit()


def play_diminished_second_inversion_harmonic(root_note, duration, instrument=0):
    pygame.midi.init()
    player = pygame.midi.Output(0)
    player.set_instrument(instrument)

    player.note_on(root_note, 127)
    player.note_on(root_note + 6, 127)
    player.note_on(root_note + 9, 127)
    time.sleep(duration)
    player.note_off(root_note, 127)
    player.note_off(root_note + 6, 127)
    player.note_off(root_note + 9, 127)

    player.close()
    pygame.midi.quit()


def play_diminished_second_inversion_melodic_up(root_note, duration, instrument=0):
    pygame.midi.init()
    player = pygame.midi.Output(0)
    player.set_instrument(instrument)

    player.note_on(root_note, 127)
    time.sleep(duration / 3)
    player.note_off(root_note, 127)
    player.note_on(root_note + 6, 127)
    time.sleep(duration / 3)
    player.note_off(root_note + 6, 127)
    player.note_on(root_note + 9, 127)
    time.sleep(duration / 3)
    player.note_off(root_note + 9, 127)

    player.close()
    pygame.midi.quit()


def play_diminished_second_inversion_melodic_down(root_note, duration, instrument=0):
    pygame.midi.init()
    player = pygame.midi.Output(0)
    player.set_instrument(instrument)

    player.note_on(root_note + 9, 127)
    time.sleep(duration / 3)
    player.note_off(root_note + 9, 127)
    player.note_on(root_note + 6, 127)
    time.sleep(duration / 3)
    player.note_off(root_note + 6, 127)
    player.note_on(root_note, 127)
    time.sleep(duration / 3)
    player.note_off(root_note, 127)

    player.close()
    pygame.midi.quit()


def play_d7_root_position_harmonic(root_note, duration, instrument = 0):
    pygame.midi.init()
    player = pygame.midi.Output(0)
    player.set_instrument(instrument)

    player.note_on(root_note, 127)
    player.note_on(root_note + 4, 127)
    player.note_on(root_note + 7, 127)
    player.note_on(root_note + 10, 127)
    time.sleep(duration)
    player.note_off(root_note, 127)
    player.note_off(root_note + 4, 127)
    player.note_off(root_note + 7, 127)
    player.note_off(root_note + 10, 127)

    player.close()
    pygame.midi.quit()


def play_d7_root_position_melodic_up(root_note, duration, instrument = 0):
    pygame.midi.init()
    player = pygame.midi.Output(0)
    player.set_instrument(instrument)

    player.note_on(root_note, 127)
    time.sleep(duration / 4)
    player.note_off(root_note, 127)
    player.note_on(root_note + 4, 127)
    time.sleep(duration / 4)
    player.note_off(root_note + 4, 127)
    player.note_on(root_note + 7, 127)
    time.sleep(duration / 4)
    player.note_off(root_note + 7, 127)
    player.note_on(root_note + 10, 127)
    time.sleep(duration / 4)
    player.note_off(root_note + 10, 127)

    player.close()
    pygame.midi.quit()


def play_d7_root_position_melodic_down(root_note, duration, instrument = 0):
    pygame.midi.init()
    player = pygame.midi.Output(0)
    player.set_instrument(instrument)

    player.note_on(root_note + 10, 127)
    time.sleep(duration / 4)
    player.note_off(root_note + 10, 127)
    player.note_on(root_note + 7, 127)
    time.sleep(duration / 4)
    player.note_off(root_note + 7, 127)
    player.note_on(root_note + 4, 127)
    time.sleep(duration / 4)
    player.note_off(root_note + 4, 127)
    player.note_on(root_note, 127)
    time.sleep(duration / 4)
    player.note_off(root_note, 127)

    player.close()
    pygame.midi.quit()


def play_d7_first_inversion_harmonic(root_note, duration, instrument = 0):
    pygame.midi.init()
    player = pygame.midi.Output(0)
    player.set_instrument(instrument)

    player.note_on(root_note, 127)
    player.note_on(root_note + 3, 127)
    player.note_on(root_note + 6, 127)
    player.note_on(root_note + 8, 127)
    time.sleep(duration)
    player.note_off(root_note, 127)
    player.note_off(root_note + 3, 127)
    player.note_off(root_note + 6, 127)
    player.note_off(root_note + 8, 127)

    player.close()
    pygame.midi.quit()


def play_d7_first_inversion_melodic_up(root_note, duration, instrument = 0):
    pygame.midi.init()
    player = pygame.midi.Output(0)
    player.set_instrument(instrument)

    player.note_on(root_note, 127)
    time.sleep(duration / 4)
    player.note_off(root_note, 127)
    player.note_on(root_note + 3, 127)
    time.sleep(duration / 4)
    player.note_off(root_note + 3, 127)
    player.note_on(root_note + 6, 127)
    time.sleep(duration / 4)
    player.note_off(root_note + 6, 127)
    player.note_on(root_note + 8, 127)
    time.sleep(duration / 4)
    player.note_off(root_note + 8, 127)

    player.close()
    pygame.midi.quit()


def play_d7_first_inversion_melodic_down(root_note, duration, instrument = 0):
    pygame.midi.init()
    player = pygame.midi.Output(0)
    player.set_instrument(instrument)

    player.note_on(root_note + 8, 127)
    time.sleep(duration / 4)
    player.note_off(root_note + 8, 127)
    player.note_on(root_note + 6, 127)
    time.sleep(duration / 4)
    player.note_off(root_note + 6, 127)
    player.note_on(root_note + 3, 127)
    time.sleep(duration / 4)
    player.note_off(root_note + 3, 127)
    player.note_on(root_note, 127)
    time.sleep(duration / 4)
    player.note_off(root_note, 127)

    player.close()
    pygame.midi.quit()


def play_d7_second_inversion_harmonic(root_note, duration, instrument = 0):
    pygame.midi.init()
    player = pygame.midi.Output(0)
    player.set_instrument(instrument)

    player.note_on(root_note, 127)
    player.note_on(root_note + 3, 127)
    player.note_on(root_note + 5, 127)
    player.note_on(root_note + 9, 127)
    time.sleep(duration)
    player.note_off(root_note, 127)
    player.note_off(root_note + 3, 127)
    player.note_off(root_note + 5, 127)
    player.note_off(root_note + 9, 127)

    player.close()
    pygame.midi.quit()


def play_d7_second_inversion_melodic_up(root_note, duration, instrument = 0):
    pygame.midi.init()
    player = pygame.midi.Output(0)
    player.set_instrument(instrument)

    player.note_on(root_note, 127)
    time.sleep(duration / 4)
    player.note_off(root_note, 127)
    player.note_on(root_note + 3, 127)
    time.sleep(duration / 4)
    player.note_off(root_note + 3, 127)
    player.note_on(root_note + 5, 127)
    time.sleep(duration / 4)
    player.note_off(root_note + 5, 127)
    player.note_on(root_note + 9, 127)
    time.sleep(duration / 4)
    player.note_off(root_note + 9, 127)

    player.close()
    pygame.midi.quit()


def play_d7_second_inversion_melodic_down(root_note, duration, instrument = 0):
    pygame.midi.init()
    player = pygame.midi.Output(0)
    player.set_instrument(instrument)

    player.note_on(root_note + 9, 127)
    time.sleep(duration / 4)
    player.note_off(root_note + 9, 127)
    player.note_on(root_note + 5, 127)
    time.sleep(duration / 4)
    player.note_off(root_note + 5, 127)
    player.note_on(root_note + 3, 127)
    time.sleep(duration / 4)
    player.note_off(root_note + 3, 127)
    player.note_on(root_note, 127)
    time.sleep(duration / 4)
    player.note_off(root_note, 127)

    player.close()
    pygame.midi.quit()


def play_d7_third_inversion_harmonic(root_note, duration, instrument = 0):
    pygame.midi.init()
    player = pygame.midi.Output(0)
    player.set_instrument(instrument)

    player.note_on(root_note, 127)
    player.note_on(root_note + 2, 127)
    player.note_on(root_note + 6, 127)
    player.note_on(root_note + 9, 127)
    time.sleep(duration)
    player.note_off(root_note, 127)
    player.note_off(root_note + 2, 127)
    player.note_off(root_note + 6, 127)
    player.note_off(root_note + 9, 127)

    player.close()
    pygame.midi.quit()


def play_d7_third_inversion_melodic_up(root_note, duration, instrument = 0):
    pygame.midi.init()
    player = pygame.midi.Output(0)
    player.set_instrument(instrument)

    player.note_on(root_note, 127)
    time.sleep(duration / 4)
    player.note_off(root_note, 127)
    player.note_on(root_note + 2, 127)
    time.sleep(duration / 4)
    player.note_off(root_note + 2, 127)
    player.note_on(root_note + 6, 127)
    time.sleep(duration / 4)
    player.note_off(root_note + 6, 127)
    player.note_on(root_note + 9, 127)
    time.sleep(duration / 4)
    player.note_off(root_note + 9, 127)

    player.close()
    pygame.midi.quit()


def play_d7_third_inversion_melodic_down(root_note, duration, instrument = 0):
    pygame.midi.init()
    player = pygame.midi.Output(0)
    player.set_instrument(instrument)

    player.note_on(root_note + 9, 127)
    time.sleep(duration / 4)
    player.note_off(root_note + 9, 127)
    player.note_on(root_note + 6, 127)
    time.sleep(duration / 4)
    player.note_off(root_note + 6, 127)
    player.note_on(root_note + 2, 127)
    time.sleep(duration / 4)
    player.note_off(root_note + 2, 127)
    player.note_on(root_note, 127)
    time.sleep(duration / 4)
    player.note_off(root_note, 127)

    player.close()
    pygame.midi.quit()


def play_d9_with_major_second_harmonic(root_note, duration, instrument = 0):
    pygame.midi.init()
    player = pygame.midi.Output(0)
    player.set_instrument(instrument)

    player.note_on(root_note, 127)
    player.note_on(root_note + 4, 127)
    player.note_on(root_note + 7, 127)
    player.note_on(root_note + 10, 127)
    player.note_on(root_note + 14, 127)
    time.sleep(duration)
    player.note_off(root_note, 127)
    player.note_off(root_note + 4, 127)
    player.note_off(root_note + 7, 127)
    player.note_off(root_note + 10, 127)
    player.note_on(root_note + 14, 127)

    player.close()
    pygame.midi.quit()


def play_d9_with_minor_second_harmonic(root_note, duration, instrument = 0):
    pygame.midi.init()
    player = pygame.midi.Output(0)
    player.set_instrument(instrument)

    player.note_on(root_note, 127)
    player.note_on(root_note + 4, 127)
    player.note_on(root_note + 7, 127)
    player.note_on(root_note + 10, 127)
    player.note_on(root_note + 13, 127)
    time.sleep(duration)
    player.note_off(root_note, 127)
    player.note_off(root_note + 4, 127)
    player.note_off(root_note + 7, 127)
    player.note_off(root_note + 10, 127)
    player.note_on(root_note + 13, 127)

    player.close()
    pygame.midi.quit()


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


# play_major_root_position_harmonic(50, 4.0)
# play_major_root_position_melodic_up(50, 4.0)
# play_major_root_position_melodic_down(50, 4.0)
#
# play_minor_root_position_harmonic(50, 4.0)
# play_minor_root_position_melodic_up(50, 4.0)
# play_minor_root_position_melodic_down(50, 4.0)
#
# play_major_first_inversion_harmonic(46, 4.0)
# play_major_first_inversion_melodic_up(46, 4.0)
# play_major_first_inversion_melodic_down(46, 4.0)
#
# play_minor_first_inversion_harmonic(46, 4.0)
# play_minor_first_inversion_melodic_up(46, 4.0)
# play_minor_first_inversion_melodic_down(46, 4.0)
#
# play_major_second_inversion_harmonic(43, 4.0)
# play_major_second_inversion_melodic_up(43, 4.0)
# play_major_second_inversion_melodic_down(43, 4.0)
#
# play_minor_second_inversion_harmonic(43, 4.0)
# play_minor_second_inversion_melodic_up(43, 4.0)
# play_minor_second_inversion_melodic_down(43, 4.0)

# play_augmented_harmonic(50, 4.0)
# play_augmented_melodic_up(50, 4.0)
# play_augmented_melodic_down(50, 4.0)
#
# play_diminished_root_position_harmonic(50, 4.0)
# play_diminished_root_position_melodic_up(50, 4.0)
# play_diminished_root_position_melodic_down(50, 4.0)
#
# play_diminished_first_inversion_harmonic(50, 4.0)
# play_diminished_first_inversion_melodic_up(50, 4.0)
# play_diminished_first_inversion_melodic_down(50, 4.0)
#
# play_diminished_second_inversion_harmonic(50, 4.0)
# play_diminished_second_inversion_melodic_up(50, 4.0)
# play_diminished_second_inversion_melodic_down(50, 4.0)

# for i in range(13):
#     play_interval_harmonic(50, 3.0, i)

# for i in range(13):
#     play_interval_melodic(50, 3.0, i)

# play_death()

# play_d7_root_position_harmonic(55, 3.0)
# play_d7_root_position_melodic_up(55, 3.0)
# play_d7_root_position_melodic_down(55, 3.0)
#
# play_d7_first_inversion_harmonic(55, 3.0)
# play_d7_first_inversion_melodic_up(55, 3.0)
# play_d7_first_inversion_melodic_down(55, 3.0)
#
# play_d7_second_inversion_harmonic(55, 3.0)
# play_d7_second_inversion_melodic_up(55, 3.0)
# play_d7_second_inversion_melodic_down(55, 3.0)
#
# play_d7_third_inversion_harmonic(55, 3.0)
# play_d7_third_inversion_melodic_up(55, 3.0)
# play_d7_third_inversion_melodic_down(55, 3.0)

# play_d9_with_major_second_harmonic(55, 3.0)
# play_d9_with_minor_second_harmonic(55, 3.0)



