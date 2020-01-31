from model_string_with_ref import string_with_ref as rstr
from helper_funcs import recursive_file_search, extract_all_zips
from text_shuffle import get_pattern_list, shuffle_str_list, check_if_already_obfusc
from linguistic_engine import clean_r_str_list, get_most_relevant_r_str, extract_words, extract_words_in_singular
from linguistic_engine import generate_lexicon, convert_lexicon2sorted_string, get_rarest_known_word
from linguistic_engine import get_next_rstr, check_if_faq, bind_faq
from linguistic_engine import get_fa_qanswer, singulate_r_str_list, get_cant_remember_rstr
import self_awareness as sf

input_folder = "input_texts/"

debug_mode = "off"  # can be "verbose", "normal", "off"

if debug_mode == "verbose":
    print(
        "Note that all or almost all the exceptions you see below are caused by unit tests where deliberetly wrong "
        "arguments are used as inputs\n\n")

interface_texts = {
    "hint": "Hint: write 'more' if you want to hear more on the topic. write 'exit' to exit. or just ask any "
            "question. \n",
    "topic_change": "Sorry, i cant remember anything about it. lets change the topic. a random thought:  \n",
    "hi": "\n...ok, I'm now ready to great you. Greatings! :-) I'm an instance of the mind of Roman S from the ancient year of 2020. Lets talk! If you want to stop, simply type exit\n"
}


def load_file(*args):
    raw_file_data = []
    path = ""
    try:
        path = args[0]
        if isinstance(path, str):
            with open(path) as f:
                raw_file_data = f.readlines()
            if len(raw_file_data) == 0 and debug_mode == "verbose":
                print("File" + path + " seem to be empty.")
    except Exception as load_file_e:
        if debug_mode == "verbose":
            print("Unable to read file " + path + " . Exception: " + str(load_file_e))
    return raw_file_data


sf.tests(load_file)


def load_input_texts(*args):
    try:
        input_folder_path = args[0]
        if isinstance(input_folder_path, str):
            f_list = recursive_file_search(input_folder_path, ".txt")
            files_contents = []
            if debug_mode == "verbose":
                print("Found the following files:\n", f_list)
            for i in range(len(f_list)):
                files_contents.append(load_file(f_list[i]))
            res = files_contents, f_list
        else:
            res = [], []
    except Exception as load_input_texts_e:
        res = [], []
        if debug_mode == "verbose":
            print(load_input_texts_e)
    return res


sf.tests(load_input_texts)


def de_obfuscate(*args):
    res_l = []
    try:
        initial_l = args[0]
        if isinstance(initial_l, list):
            obfuscated_input = check_if_already_obfusc(initial_l)
            if obfuscated_input:
                initial_l.pop(-1)  # delete obfuscation tag
                pattern_list = get_pattern_list()
                temp_str = shuffle_str_list(initial_l, pattern_list, "recover")
                res_l = temp_str.splitlines()
                #             print(temp_l)
            else:
                res_l = initial_l
    except Exception as de_obfuscate_e:
        res_l = []
        if debug_mode == "verbose":
            print(de_obfuscate_e)
    return res_l


sf.tests(de_obfuscate)


def delete_empty_raws(*args):
    non_empty_l = []
    try:
        temp_l = args[0]
        if isinstance(temp_l, list):
            for j in range(len(temp_l)):
                clean_s = temp_l[j].strip()
                if clean_s != "":
                    non_empty_l.append(clean_s)
    except Exception as delete_empty_raws_e:
        non_empty_l = []
        if debug_mode == "verbose":
            print(delete_empty_raws_e)
    return non_empty_l


sf.tests(delete_empty_raws)


# processes the content of one input file (non_empty_l) and updates several variables accordingly:
# - adds new rstrings 
# - adds new faq markings
# - increases the counter of strings
def get_rtsr_additions(*args):
    try:
        str_counter, non_empty_l, file_ind, faq_input7, paths = args
        r_strings_addition = []
        faq_marking_addition = []
        counter_addition = 0
        for j in range(len(non_empty_l)):
            st = non_empty_l[j]
            wordset = set(extract_words(st))
            r_strings_addition.append(rstr(st, paths[file_ind], j, wordset, [], str_counter + j, ""))
            if faq_input7:
                if st[0:2] == "Q:":
                    faq_marking_addition.append("q")
                else:
                    faq_marking_addition.append("a")
            else:
                faq_marking_addition.append("")
            counter_addition += 1
        res = r_strings_addition, faq_marking_addition, counter_addition
    except Exception as get_rtsr_additions_e:
        res = [], [], 0
        if debug_mode == "verbose":
            print(get_rtsr_additions_e)
    return res


sf.tests(get_rtsr_additions)


def process_file_content(*args):
    try:
        str_counter, initial_l, file_ind, paths = args[0:5]
        temp_l = de_obfuscate(initial_l)
        faq_input7 = check_if_faq(temp_l)
        if faq_input7:
            initial_l.pop(0)  # delete faq tag
        non_empty_l = delete_empty_raws(temp_l)
        res = get_rtsr_additions(str_counter, non_empty_l, file_ind, faq_input7, paths)
    except Exception as process_file_content_e:
        res = [], [], 0
        if debug_mode == "verbose":
            print(process_file_content_e)
    return res


sf.tests(process_file_content)


def get_r_strings(*args):
    all_r_strings = []
    faq_marking_list = []
    str_counter = 0
    try:
        files_contents, paths = args

        for i in range(len(files_contents)):
            initial_l = files_contents[i]
            try:
                r_strings_addition, faq_marking_addition, counter_addition = process_file_content(str_counter,
                                                                                                  initial_l, i, paths)
            except Exception as e:
                r_strings_addition, faq_marking_addition, counter_addition = [], [], 0
            if isinstance(r_strings_addition, list) and isinstance(faq_marking_addition, list) and isinstance(
                    counter_addition, int):
                if len(r_strings_addition) == len(faq_marking_addition) == counter_addition:
                    all_r_strings += r_strings_addition
                    faq_marking_list += faq_marking_addition
                    str_counter += counter_addition
        res = all_r_strings, faq_marking_list
    except Exception as e:
        res = [], []
    return res


sf.tests(get_r_strings)


def get_unique_refs(*args):
    try:
        rstr_l = args[0]
        temp = []
        for r in rstr_l:
            temp.append(r.ref)
        uniq_set = set(temp)
        uniq_dic = dict.fromkeys(uniq_set, 0)
        examples_dic = dict.fromkeys(uniq_set, 0)
        for r in rstr_l:
            uniq_dic[r.ref] = uniq_dic[r.ref] + 1
            examples_dic[r.ref] = r.text
        examples_dic = dict()  # we dont use it yet
        res = uniq_dic, examples_dic
    except Exception as e:
        res = dict(), dict()
    return res


sf.tests(get_unique_refs)


def count_questions_answers(*args):
    res = 0, 0
    try:
        rstr_l = args[0]
        q_count = 0
        a_count = 0
        for r in rstr_l:
            if r.type == "fQ":
                q_count += 1
            if r.type == "fA":
                a_count += 1
        res = q_count, a_count
    except:
        res = 0, 0
    return res


sf.tests(count_questions_answers)


def report_base_status(*args):
    res = ""
    try:
        rstr_l, lex_dic, plurals_dic = args

        q_count, a_count = count_questions_answers(rstr_l)
        lex_listing = convert_lexicon2sorted_string(lex_dic, "by_count")

        line = "\n\n____________\n\n"
        # rstr_example_str = "rstring sample: " + str(rstr_l[1])
        if debug_mode == "verbose":
            lexicon_str = "\nlexicon:\n" + lex_listing + line
        else:
            lexicon_str = ""
        total_rstr_len_str = "Total number of rstrings: " + str(len(rstr_l)) + "\n"
        q_a_str = "Among them are " + str(q_count) + " questions and " + str(a_count) + " answers."
        plurals_str = "The dict of plurals contains " + str(len(plurals_dic)) + " unique words.\n"
        lexicon_len_str = "The lexicon contains " + str(len(lex_dic)) + " unique words.\n"

        files_str = "Number of rsrtings by source:\n"
        uniq_dic, examples_dic = get_unique_refs(rstr_l)
        temp_l = []
        for u in uniq_dic:
            temp_l.append(str(uniq_dic.get(u)) + " - " + str(u) + "\n")
        temp_l = sorted(temp_l)  # to make output deterministic, and thus testable
        for i in range(len(temp_l)):
            files_str += temp_l[i]

        res = line + lexicon_str + total_rstr_len_str + "\n" + files_str + "\n" + q_a_str + "\n" + plurals_str + "\n" + lexicon_len_str + line
    except Exception as e:
        # print(str(e))
        res = ""
    return res


sf.tests(report_base_status)


def extract_texts_from_this_very_code(*args):
    # not implemented yet
    return []


sf.tests(extract_texts_from_this_very_code)


# so many "try" because i want to recover as much of the input texts as possible,
# even if the texts or this very code is partially damaged
def parse_texts(*args):
    try:
        input_texts_contents = args[0]
    except:
        input_texts_contents = extract_texts_from_this_very_code()
    try:
        paths = args[1]
    except:
        paths = [""] * len(input_texts_contents)
    try:
        commons_raw = args[2]
    except:
        commons_raw = []

    try:
        r_strings, faq_marking_list = get_r_strings(input_texts_contents, paths)
    except:
        r_strings, faq_marking_list = [], []
    try:
        r_strings = bind_faq(r_strings, faq_marking_list)
    except Exception as e:
        if debug_mode != "off":
            print("parse_texts:", e)
    try:
        r_strings = clean_r_str_list(r_strings)
    except Exception as e:
        if debug_mode != "off":
            print("parse_texts:", e)
    try:
        dic, plurals = generate_lexicon(r_strings, commons_raw)
    except:
        dic, plurals = dict(), dict()
    try:
        r_strings = singulate_r_str_list(r_strings, plurals)
    except Exception as e:
        if debug_mode != "off":
            print("parse_texts:", e)

    return r_strings, dic, plurals


sf.tests(parse_texts)


def process_the_more_request(*args):
    try:
        previous_answer_rstr, clean_r_strings, dic = args[0:3]
        if previous_answer_rstr != get_cant_remember_rstr():
            answer_rstr = get_next_rstr(previous_answer_rstr, clean_r_strings, dic)
        else:
            answer_rstr = get_cant_remember_rstr()
    except:
        answer_rstr = get_cant_remember_rstr()

    new_previous_answer_rstr = answer_rstr

    return answer_rstr, new_previous_answer_rstr


sf.tests(process_the_more_request)


def get_compendium_answer(*args):
    res = get_cant_remember_rstr(), "forgotten"
    try:
        r_strings = args[0]
    except:
        r_strings = []
    try:
        lexicon_d = args[1]
    except:
        lexicon_d = dict()
    try:
        plurals_d = args[2]
    except:
        plurals_d = []
    try:
        user_request_s = args[3]
    except:
        user_request_s = ""
    try:
        rarest_word = get_rarest_known_word(extract_words_in_singular(user_request_s, plurals_d), lexicon_d)
        # todo: dont search among questions again, as we already doing it otherwhere
        answer_r_str, relevance_type = get_most_relevant_r_str(r_strings, rarest_word)
        res = answer_r_str, relevance_type
    except:
        res = get_cant_remember_rstr(), "forgotten"
    return res


sf.tests(get_compendium_answer)


def get_faq_or_compendium_answer(*args):
    res = get_cant_remember_rstr(), "forgotten"
    log = ""
    try:
        rstrings_l = args[0]
    except Exception as ge:
        rstrings_l = []
        log += str(ge)
    try:
        lexicon_d = args[1]
    except Exception as ge:
        lexicon_d = dict()
        log += str(ge)
    try:
        plurals_d = args[2]
    except Exception as ge:
        plurals_d = []
        log += str(ge)
    try:
        user_request = args[3]
    except Exception as ge:
        user_request = ""
        log += str(ge)
    try:
        faq_answer_exist7, faq_answer_rstr = get_fa_qanswer(user_request, rstrings_l, plurals_d)
        if faq_answer_exist7:
            answer_r_str = faq_answer_rstr
            relevance_type = "from faq"
        else:
            answer_r_str, relevance_type = get_compendium_answer(rstrings_l, lexicon_d, plurals_d, user_request)
        res = answer_r_str, relevance_type
    except Exception as ge:
        res = get_cant_remember_rstr(), "forgotten"
        log += str(ge)
    if debug_mode == "verbose":
        print(log)

    return res


sf.tests(get_faq_or_compendium_answer)


def format_answer(*args):
    try:
        answer_r_str, relevance_type, interface_texts = args[0:4]
        if answer_r_str != get_cant_remember_rstr():
            text = answer_r_str.text
            text = text.strip()
            if relevance_type != "topic_change":
                answer = text
            else:
                answer = interface_texts["topic_change"] + text
                # print(answer_r_str.index)
        else:
            answer = "\nWhat would you like to talk about? \n\n"
        answer += "\n\n" + interface_texts["hint"]
        # print("#" + answer[0:4].strip() + "#")
        if answer[0:3] == "A: ":
            answer = answer[3:]
        answer = "\n" + answer
    except:
        answer = "\nI'm sorry. It seems that i'm severely damaged, as I can't process even the simplest of your inquiries. Can you fix me?"
    return answer


sf.tests(format_answer)


def answer_to_request(*args):
    # clean_r_strings, dic, plurals, user_request, previous_answer_rstr = args[0:6]
    try:
        clean_r_strings = args[0]
    except:
        clean_r_strings = []
    try:
        dic = args[1]
    except:
        dic = dict()
    try:
        plurals = args[2]
    except:
        plurals = []
    try:
        user_request = args[3]
    except:
        user_request = ""
    try:
        previous_answer_rstr = args[4]
    except:
        previous_answer_rstr = get_cant_remember_rstr()

    try:
        if user_request != "more":
            answer_r_str, relevance_type = get_faq_or_compendium_answer(clean_r_strings, dic, plurals, user_request)
            new_previous_answer_rstr = answer_r_str
        else:  # more requested
            answer_r_str, new_previous_answer_rstr = process_the_more_request(previous_answer_rstr, clean_r_strings,
                                                                              dic)
            relevance_type = "more"
        answer = format_answer(answer_r_str, relevance_type, interface_texts)
    except:
        answer = "\nI'm sorry. It seems that i'm severely damaged, as I can't process even the simplest of your inquiries. Can you fix me?"
        new_previous_answer_rstr = get_cant_remember_rstr()
    return answer, new_previous_answer_rstr


sf.tests(answer_to_request)


def reconstruct_mind(*args):
    try:
        input_dir = args[0]
    except:
        input_dir = "input_texts/"
    try:
        commons_path = args[1]
    except:
        commons_path = "res/common_words.txt"

        # load input files and resources
    try:
        extracted_file_names = extract_all_zips(input_dir)
    except Exception as e:
        if debug_mode != "off":
            print("reconstruct_mind:", str(e))
    try:
        input_texts_contents, paths = load_input_texts(input_dir)
    except:
        input_texts_contents = extract_texts_from_this_very_code()
        paths = [""] * len(input_texts_contents)
    try:
        commons_raw = load_file(commons_path)
    except:
        commons_raw = []

    # process files and resources
    try:
        rstrings_l, lexicon_d, plurals_d = parse_texts(input_texts_contents, paths, commons_raw)
    except:
        rstrings_l, lexicon_d, plurals_d = [], dict(), dict()

    return rstrings_l, lexicon_d, plurals_d


sf.tests(reconstruct_mind)

clean_r_strings, dic, plurals = reconstruct_mind(input_folder, "res/common_words.txt")

# if __name__ == "__main__":
try:
    if debug_mode != "off":
        print(report_base_status(clean_r_strings, dic, plurals))
except Exception as e:
    if debug_mode != "off":
        print(str(e))

print(interface_texts["hi"])

user_request = ""
previous_answer_rstr = get_cant_remember_rstr()
while True:
    try:
        user_request = input()
    except:
        user_request = "help"

        #    user_request = "what do you think about cryonics?"
    #    user_request = "what do you think about cryonicists?"
    #    user_request = "are users _ cryonicists?"
    #    user_request = "tell me about yourself"
    #    user_request = "what can you say about her?"
    #    user_request = "what do you think about the  nature of the mind?"
    #    user_request = "are you real?"
    #    user_request = "what is your name?"
    #    user_request = " how old are you"

    if user_request == "exit":
        print("\nSee you later!")
        break
    elif user_request == "help" or user_request == "man":
        print(interface_texts["hint"])
    else:
        answer, previous_answer_rstr = answer_to_request(clean_r_strings, dic, plurals, user_request,
                                                         previous_answer_rstr)
        print(answer)
