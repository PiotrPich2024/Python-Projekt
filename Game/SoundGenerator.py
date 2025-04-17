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

def play_interval_harmonic(root_note, instrument, duration, interval_semitones):
    pygame.midi.init()
    player = pygame.midi.Output(0)
    instrument = 0
    player.set_instrument(instrument)

    player.note_on(root_note, 127)
    player.note_on(root_note + interval_semitones, 127)
    time.sleep(duration)
    player.note_off(root_note, 127)
    player.note_on(root_note + interval_semitones, 127)

    player.close()
    pygame.midi.quit()

def play_interval_melodic(root_note, instrument, duration, interval_semitones):
    pygame.midi.init()
    player = pygame.midi.Output(0)
    instrument = 0
    player.set_instrument(instrument)

    player.note_on(root_note, 127)
    time.sleep(duration / 2)
    player.note_off(root_note, 127)
    player.note_on(root_note + interval_semitones, 127)
    time.sleep(duration / 2)
    player.note_on(root_note + interval_semitones, 127)

    player.close()
    pygame.midi.quit()


def play_major_root_position_harmonic(root_note, instrument, duration):
    pygame.midi.init()
    player = pygame.midi.Output(0)
    instrument = 0
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


def play_minor_root_position_harmonic(root_note, instrument, duration):
    pygame.midi.init()
    player = pygame.midi.Output(0)
    instrument = 0
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


def play_major_first_inversion_harmonic(root_note, instrument, duration):
    pygame.midi.init()
    player = pygame.midi.Output(0)
    instrument = 0
    player.set_instrument(instrument)

    player.note_on(root_note, 127)
    player.note_on(root_note + 3, 127)
    player.note_on(root_note + 5, 127)
    time.sleep(duration)
    player.note_off(root_note, 127)
    player.note_off(root_note + 3, 127)
    player.note_off(root_note + 5, 127)

    player.close()
    pygame.midi.quit()


def play_minor_first_inversion_harmonic(root_note, instrument, duration):
    pygame.midi.init()
    player = pygame.midi.Output(0)
    instrument = 0
    player.set_instrument(instrument)

    player.note_on(root_note, 127)
    player.note_on(root_note + 4, 127)
    player.note_on(root_note + 5, 127)
    time.sleep(duration)
    player.note_off(root_note, 127)
    player.note_off(root_note + 4, 127)
    player.note_off(root_note + 5, 127)

    player.close()
    pygame.midi.quit()


def play_major_second_inversion_harmonic(root_note, instrument, duration):
    pygame.midi.init()
    player = pygame.midi.Output(0)
    instrument = 0
    player.set_instrument(instrument)

    player.note_on(root_note, 127)
    player.note_on(root_note + 5, 127)
    player.note_on(root_note + 4, 127)
    time.sleep(duration)
    player.note_off(root_note, 127)
    player.note_off(root_note + 5, 127)
    player.note_off(root_note + 4, 127)

    player.close()
    pygame.midi.quit()


def play_minor_second_inversion_harmonic(root_note, instrument, duration):
    pygame.midi.init()
    player = pygame.midi.Output(0)
    instrument = 0
    player.set_instrument(instrument)

    player.note_on(root_note, 127)
    player.note_on(root_note + 5, 127)
    player.note_on(root_note + 3, 127)
    time.sleep(duration)
    player.note_off(root_note, 127)
    player.note_off(root_note + 5, 127)
    player.note_off(root_note + 3, 127)

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


# play_major_root_position_harmonic(50, 0, 7.0)
# play_minor_root_position_harmonic(50, 0, 7.0)
# play_major_first_inversion_harmonic(50, 0, 7.0)
# play_minor_first_inversion_harmonic(50, 0, 7.0)
# play_major_second_inversion_harmonic(50, 0, 7.0)
# play_minor_second_inversion_harmonic(50, 0, 7.0)

for i in range(13):
    play_interval_harmonic(50, 0, 3.0, i)

for i in range(13):
    play_interval_melodic(50, 0, 3.0, i)



