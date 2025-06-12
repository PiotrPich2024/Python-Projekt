import random
import threading
import Game.questions.sound_generator as sound_generator
import Game.questions.names as names


def play_interval_question(mode, root_note, duration, interval_semitones, instrument, engine):

    interval_functions = {
        0: sound_generator.play_interval_harmonic,      # interwał harmoniczny
        1: sound_generator.play_interval_melodic_up,    # interwał melodyczny w górę
        2: sound_generator.play_interval_melodic_down,  # interwał melodyczny w dół
    }

    interval_functions[mode](root_note, duration, interval_semitones, instrument, engine)


def play_triad_question(mode, root_note, duration, triad_code, instrument, engine):

    triad_names = {
        0: ["major_root_position_harmonic", "major_root_position_melodic_up", "major_root_position_melodic_down"],
        1: ["minor_root_position_harmonic", "minor_root_position_melodic_up", "minor_root_position_melodic_down"],
        2: ["major_first_inversion_harmonic", "major_first_inversion_melodic_up", "major_first_inversion_melodic_down"],
        3: ["minor_first_inversion_harmonic", "minor_first_inversion_melodic_up", "minor_first_inversion_melodic_down"],
        4: ["major_second_inversion_harmonic", "major_second_inversion_melodic_up", "major_second_inversion_melodic_down"],
        5: ["minor_second_inversion_harmonic", "minor_second_inversion_melodic_up", "minor_second_inversion_melodic_down"],
        6: ["diminished_root_position_harmonic", "diminished_root_position_melodic_up", "diminished_root_position_melodic_down"],
        7: ["diminished_first_inversion_harmonic", "diminished_first_inversion_melodic_up", "diminished_first_inversion_melodic_down"],
        8: ["diminished_second_inversion_harmonic", "diminished_second_inversion_melodic_up", "diminished_second_inversion_melodic_down"],
        9: ["augmented_harmonic", "augmented_melodic_up", "augmented_melodic_down"],
    }

    sound_generator.play_chord(triad_names[triad_code][mode], root_note, duration, instrument, engine)


def play_d7_question(mode, root_note, duration, d7_code, instrument, engine):

    d7_names = {
        0: ["d7_root_position_harmonic", "d7_root_position_melodic_up", "d7_root_position_melodic_down"],
        1: ["d7_first_inversion_harmonic", "d7_first_inversion_melodic_up", "d7_first_inversion_melodic_down"],
        2: ["d7_second_inversion_harmonic", "d7_second_inversion_melodic_up", "d7_second_inversion_melodic_down"],
        3: ["d7_third_inversion_harmonic", "d7_third_inversion_melodic_up", "d7_third_inversion_melodic_down"],

    }

    sound_generator.play_chord(d7_names[d7_code][mode], root_note, duration, instrument, engine)


def play_d9_question(mode, root_note, duration, d9_code, instrument, engine):
    d9_names = {
        0: ["d9_with_major_second_harmonic", "d9_with_major_second_melodic_up", "d9_with_major_second_melodic_down"],
        1: ["d9_with_minor_second_harmonic", "d9_with_minor_second_melodic_up", "d9_with_minor_second_melodic_down"],
    }

    sound_generator.play_chord(d9_names[d9_code][mode], root_note, duration, instrument, engine)


def play_compound_interval_question(mode, root_note, duration, interval_semitones, instrument, engine):

    compound_interval_functions = {
        0: sound_generator.play_compound_interval_harmonic,      # interwał harmoniczny
        1: sound_generator.play_compound_interval_melodic_up,    # interwał melodyczny w górę
        2: sound_generator.play_compound_interval_melodic_down,  # interwał melodyczny w dół
    }

    compound_interval_functions[mode](root_note, duration, interval_semitones, instrument, engine)


def generate_question(answer_no, max_answer_no, instrument, duration, lowest_root_note, highest_root_note, question_type):
    # maksymalna liczba odpowiedzi zależna od tego ile mamy możliwości
    if answer_no > max_answer_no:
        answer_no = max_answer_no

    # generowanie poprawnej oraz złych odpowiedzi
    root_note = random.randrange(lowest_root_note, highest_root_note)
    code = random.randrange(max_answer_no)  # kod interwału lub akordu
    mode = random.randrange(3)  # harmoniczny, melodyczny w góre, melodyczny w dół
    answer_index = random.randrange(answer_no)
    answers = []
    for i in range(answer_no):
        if i == answer_index:
            answers.append(code)
        else:
            fake_code = random.randrange(max_answer_no)
            unsuccessful_attempts = 0
            while unsuccessful_attempts < 10 and (fake_code == code or fake_code in answers):
                unsuccessful_attempts += 1
                fake_code = random.randrange(max_answer_no)
            while fake_code == code or fake_code in answers:
                fake_code += 1
                if fake_code >= max_answer_no:
                    fake_code = 0
            answers.append(fake_code)

    # # zagranie pytania
    # play_thread = threading.Thread(target=question_type, args=(mode, root_note, duration, code, instrument))
    # play_thread.start()

    # zwracamy odpowiedzi, parametry do ponownego odtworzenia pytania oraz wskazanie na funkcję wypisującą odpowiedzi
    target = question_type
    args = (mode, root_note, duration, code, instrument)
    readers = {  # przypisujemy każdej funkcji grającej pytanie, funkcję, która wypisze odpowiedzi
        play_interval_question: names.get_interval_name,
        play_compound_interval_question: names.get_compound_interval_name,
        play_triad_question: names.get_triad_name,
        play_d7_question: names.get_d7_name,
        play_d9_question: names.get_d9_name,
    }
    return answers, answer_index, target, args, readers[question_type]


def choose_question(answer_no, difficulty_level=0, instrument=0, duration=3, lowest_root_note=48, highest_root_note=71):

    questions = {
        0: generate_question(answer_no, 13, instrument, duration, lowest_root_note, highest_root_note, play_interval_question),
        1: generate_question(answer_no, 10, instrument, duration + 1, lowest_root_note, highest_root_note, play_triad_question),
        2: generate_question(answer_no, 4, instrument, duration + 2, lowest_root_note, highest_root_note, play_d7_question),
        3: generate_question(answer_no, 2, instrument, duration + 2, lowest_root_note, highest_root_note, play_d9_question),
        4: generate_question(answer_no, 12, instrument, duration, lowest_root_note, highest_root_note, play_compound_interval_question),
    }

    match difficulty_level:
        case 0:
            return questions[0]
        case 1:
            return questions[random.randrange(2)]
        case 2:
            return questions[random.randrange(3)]
        case 3:
            return questions[random.randrange(4)]
        case 4:
            return questions[random.randrange(5)]
        case _:
            return questions[random.randrange(5)]
