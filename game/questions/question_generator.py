
import random
import threading


class SoundGenerator:
    pass


def play_interval_question(mode ,root_note, duration, interval_semitones, instrument):

    interval_functions = {
        0: [SoundGenerator.play_interval_harmonic],
        1: [SoundGenerator.play_interval_melodic_up],
        2: [SoundGenerator.play_interval_melodic_down],
    }

    random.choice(interval_functions[mode])(root_note, duration, interval_semitones, instrument)

def generate_interval_question(answer_no):
    if answer_no > 12:
        answer_no = 12
    root_note = random.randrange(41, 81)
    interval_semitones = random.randrange(13)
    instrument = 0
    duration = 3
    answer_index = random.randrange(answer_no)
    answers = []
    for i in range (answer_no):
        if i == answer_index:
            answers.append(interval_semitones)
        else:
            fake_semitones = random.randrange(13)
            while fake_semitones == interval_semitones or fake_semitones in answers:
                fake_semitones += 1
                if fake_semitones > 12:
                    fake_semitones = 0
            answers.append(fake_semitones)

    mode = random.randrange(3)
    play_thread = threading.Thread(target=play_interval_question, args=(mode, root_note, duration, interval_semitones, instrument))
    play_thread.start()

    # text = TextFont(12,16,1)
    # text.render_string("sdfsdf", surf, pos)

    return answers, answer_index

def generate_triad_question(answer_no):
    if answer_no > 10:
        answer_no = 10
    root_note = random.randrange(41, 81)
    triad_code = random.randrange(10)
    instrument = 0
    duration = 3
    answer_index = random.randrange(answer_no)
    answers = []
    for i in range (answer_no):
        if i == answer_index:
            answers.append(triad_code)
        else:
            fake_triad_code = random.randrange(10)
            while fake_triad_code == triad_code or fake_triad_code in answers:
                fake_triad_code += 1
                if fake_triad_code > 9:
                    fake_triad_code = 0
            answers.append(fake_triad_code)

    match random.randrange(10):
        case 0:
            match random.randrange(3):
                case 0:
                    SoundGenerator.play_major_root_position_harmonic(root_note, duration, instrument)
                case 1:
                    SoundGenerator.play_major_root_position_melodic_up(root_note, duration, instrument)
                case 2:
                    SoundGenerator.play_major_root_position_melodic_down(root_note, duration, instrument)
        case 1:
            match random.randrange(3):
                case 0:
                    SoundGenerator.play_major_first_inversion_harmonic(root_note, duration, instrument)
                case 1:
                    SoundGenerator.play_major_first_inversion_melodic_up(root_note, duration, instrument)
                case 2:
                    SoundGenerator.play_major_first_inversion_melodic_down(root_note, duration, instrument)
        case 2:
            match random.randrange(3):
                case 0:
                    SoundGenerator.play_major_second_inversion_harmonic(root_note, duration, instrument)
                case 1:
                    SoundGenerator.play_major_second_inversion_melodic_up(root_note, duration, instrument)
                case 2:
                    SoundGenerator.play_major_second_inversion_melodic_down(root_note, duration, instrument)
        case 3:
            match random.randrange(3):
                case 0:
                    SoundGenerator.play_minor_root_position_harmonic(root_note, duration, instrument)
                case 1:
                    SoundGenerator.play_minor_root_position_melodic_up(root_note, duration, instrument)
                case 2:
                    SoundGenerator.play_minor_root_position_melodic_down(root_note, duration, instrument)
        case 4:
            match random.randrange(3):
                case 0:
                    SoundGenerator.play_minor_first_inversion_harmonic(root_note, duration, instrument)
                case 1:
                    SoundGenerator.play_minor_first_inversion_melodic_up(root_note, duration, instrument)
                case 2:
                    SoundGenerator.play_minor_first_inversion_melodic_down(root_note, duration, instrument)
        case 5:
            match random.randrange(3):
                case 0:
                    SoundGenerator.play_minor_second_inversion_harmonic(root_note, duration, instrument)
                case 1:
                    SoundGenerator.play_minor_second_inversion_melodic_up(root_note, duration, instrument)
                case 2:
                    SoundGenerator.play_minor_second_inversion_melodic_down(root_note, duration, instrument)
        case 6:
            match random.randrange(3):
                case 0:
                    SoundGenerator.play_diminished_root_position_harmonic(root_note, duration, instrument)
                case 1:
                    SoundGenerator.play_diminished_root_position_melodic_up(root_note, duration, instrument)
                case 2:
                    SoundGenerator.play_diminished_root_position_melodic_down(root_note, duration, instrument)
        case 7:
            match random.randrange(3):
                case 0:
                    SoundGenerator.play_diminished_first_inversion_harmonic(root_note, duration, instrument)
                case 1:
                    SoundGenerator.play_diminished_first_inversion_melodic_up(root_note, duration, instrument)
                case 2:
                    SoundGenerator.play_diminished_first_inversion_melodic_down(root_note, duration, instrument)
        case 8:
            match random.randrange(3):
                case 0:
                    SoundGenerator.play_diminished_second_inversion_harmonic(root_note, duration, instrument)
                case 1:
                    SoundGenerator.play_diminished_second_inversion_melodic_up(root_note, duration, instrument)
                case 2:
                    SoundGenerator.play_diminished_second_inversion_melodic_down(root_note, duration, instrument)
        case 9:
            match random.randrange(3):
                case 0:
                    SoundGenerator.play_augmented_harmonic(root_note, duration, instrument)
                case 1:
                    SoundGenerator.play_augmented_melodic_up(root_note, duration, instrument)
                case 2:
                    SoundGenerator.play_augmented_melodic_down(root_note, duration, instrument)

    return answers

def generate_dominant_question(answer_no):
    pass

def generate_question(answer_no, difficulty):
    match difficulty:
        case 0:
            return generate_interval_question(answer_no)
        case 1:
            return generate_triad_question(answer_no)
        case 2:
            return generate_dominant_question(answer_no)
        case _:
            return generate_interval_question(answer_no)

