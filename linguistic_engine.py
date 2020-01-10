# most of the bot's intelligence is implemented here

import self_awareness as sf

# Note: if you set it to True, it will print a lot of junk - because of many self-tests with intentionally bad params
debug_mode = False

if __name__ == "__main__":
    print("\nYou should launch launcher.py, not me :)")


# if you want to change it, dont forget to change the tests too
def get_cant_remember_rstr(*args):
    rtext = "sorry. i cant remember..."
    ref = "default"
    rindex = -1
    wordset = {"sorry", "i", "cant", "remember"}
    answers_list = []
    global_ind = -1
    type = ""
    try:
        from model_string_with_ref import string_with_ref as rstr
        res_rstr = rstr(rtext, ref, rindex, wordset, answers_list, global_ind, type)
    except:
        res_rstr = None
    return res_rstr


sf.tests(get_cant_remember_rstr)


def get_faq_tag(*args):
    faq_tag = "<parse_as_faq>"
    return faq_tag


sf.tests(get_faq_tag)


def get_random_nonempty_rsr(*args):
    try:
        rstr_list = args[0]
        r_str = rstr_list[0]
        #    print(r_str)
        test_str = ""
        counter = 0
        from random import randint
        while len(test_str) < 1 and counter < 100:
            rnd_index = randint(0, len(rstr_list) - 1)
            r_str = rstr_list[rnd_index]
            test_str = r_str.text.strip()
            counter += 1
    except Exception as e:
        if debug_mode:
            print(e)
        r_str = get_cant_remember_rstr()
    return r_str


sf.tests(get_random_nonempty_rsr)


# testr = sf.get_rstr_list4tests()
# print("here:", get_random_nonempty_rsr())


# def lets_change_topic(rstr_list):
#    random_rstr = get_random_nonempty_rsr(rstr_list) 
#   output_rstr = string_with_ref("sorry, i cant remember anything about it. lets change the topic. a random thought: \n" + random_rstr.text, "default answers", random_rstr.index, none, [], 0)
#    return random_rstr
# sf.tests(lets_change_topic)

def clean_r_str_list(*args):
    try:
        input_list = args[0]
        from model_string_with_ref import string_with_ref as rstr
        if not isinstance(input_list[0], rstr):
            input_list = [get_cant_remember_rstr()]
    except Exception as e:
        if debug_mode:
            print(e)
        input_list = [get_cant_remember_rstr()]
    try:
        for i in range(len(input_list)):
            test_r_str = input_list[i]
            test_r_str.text = test_r_str.text.strip()
            input_list[i] = test_r_str
    except Exception as e:
        if debug_mode:
            print(e)
    return input_list


sf.tests(clean_r_str_list)


def find_r_str_containing_word(*args):
    try:
        rstr_list, word_str = args
        output_list = []
        word_str = word_str.lower()
        for rstr in rstr_list:
            if word_str in rstr.wordset:
                output_list.append(rstr)
    except Exception as e:
        if debug_mode:
            print(e)
        output_list = [get_cant_remember_rstr()]
    return output_list


sf.tests(find_r_str_containing_word)


def replace_in_str(*args):
    edited_str = ""
    source_str, oldsymb, newsymb = "", "", ""
    try:
        source_str, oldsymb, newsymb = args
        if isinstance(source_str, str):
            edited_str = source_str
    except Exception as e:
        if debug_mode:
            print(e)
    try:
        edited_str = source_str.replace(oldsymb, newsymb)
    except Exception as e:
        if debug_mode:
            print(e)
    return edited_str


sf.tests(replace_in_str)


# returns a list of words, can contain repeats	
def extract_words(*args):
    symbs2blank = [
        ":",
        ".",
        ",",
        ";",
        "?",
        "!",
        "\"",
        "\'",
        "’",
        "“",
        "”",
        "\\",
        "/",
        "(",
        ")",
        "[",
        "]",
        "0",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "_",
        "-",
        "–",
        "https",
        "http",
        "html",
        "htm",
        "www",
        ">",
        "<",
        "+",
        "=",
        "%",
        "&",
        "$",
        "€",
        "#",
        "@",
        "~",
        "…",
        "→",
        "^",
        "*",
        "°c",
        "¼",
        "„",
        "№",
        "—",
        "‘",
        "⁸",
        "−",
        "{",
        "|",
        "}",
        "°",
        "×",
        "[",
        "]"
    ]

    common_abbreviation_artefacts = [
        "t",  # from can't and don't
        "re",  # from you're
        "ve",  # from we've etc
        "m",  # from i'm
        "s",  # from multiples, she's etc
        "ll",  # from we'll etc
        "don",
        "doesn",
        "haven",
        "g",
        "e"
    ]

    try:
        i_str = args[0]

        i_str = i_str.lower()
        # cleaning up the text
        for i in range(len(symbs2blank)):
            i_str = replace_in_str(i_str, symbs2blank[i], " ")

            # spliting it into a list of words
        wordis = i_str.split()

        for i in range(len(wordis)):
            stripped = wordis[i].strip()
            wordis[i] = stripped

        clean_words = []
        for w in wordis:
            if w not in common_abbreviation_artefacts:
                clean_words.append(w)
    except Exception as e:
        if debug_mode:
            print(e)
        clean_words = []
    return clean_words


sf.tests(extract_words)


# special comparrison func where (examples):
# 5 is rarer than 10
# 5 is rarer than negatives
# -10 is rarer than _5
def first_count_rarer_than_second7(*args):
    try:
        first_count, second_count = args
        res = True
        if first_count >= 0:
            if second_count >= 0:
                if first_count < second_count:
                    res = True
                else:
                    res = False
            else:  # second has a negative value
                res = True  # by our convention,  negative means not rare. thus, here the first one is rarer
        else:  # first one is negative
            if second_count >= 0:
                res = False  # positive counts are rarer than negatives
            else:  # both are negative
                if first_count < second_count:
                    res = True  # _2 is rarer than -1 etc
                else:
                    res = False
    except Exception as e:
        if debug_mode:
            print(e)
        res = False
    return res


sf.tests(first_count_rarer_than_second7)


# takes a list of words.
# returns the rarest of them, according to the lexicon dict.
# returns "-1" if no word is in lexicon
def get_rarest_known_word(*args):
    try:
        word_l, lex_dict = args
        input_set = set(word_l)

        rarest_word = "-1"
        lowest_count = 0

        for input_w in input_set:
            if input_w in lex_dict:
                test_count = lex_dict.get(input_w)
                if first_count_rarer_than_second7(test_count, lowest_count) or (lowest_count == 0):
                    rarest_word = input_w
                    lowest_count = test_count
    except Exception as e:
        if debug_mode:
            print(e)
        rarest_word = "-1"
    return rarest_word


sf.tests(get_rarest_known_word)


def get_most_relevant_r_str(*args):
    try:
        rstr_list, user_request = args
        words_from_request = extract_words(user_request)
        all_relevant_rstrings = []
        from random import randint
        for word in words_from_request:
            all_relevant_rstrings += find_r_str_containing_word(rstr_list, word)
        if len(all_relevant_rstrings) > 0:
            rnd_index = randint(0, len(all_relevant_rstrings) - 1)
            output_rstr = all_relevant_rstrings[rnd_index]
            answer_type = "relevant"
        else:
            output_rstr = get_random_nonempty_rsr(rstr_list)
            answer_type = "topic_change"
    except Exception as e:
        if debug_mode:
            print(e)
        output_rstr = get_cant_remember_rstr()
        answer_type = "forgotten"
    return output_rstr, answer_type


sf.tests(get_most_relevant_r_str)


# takes a raw list of common words.            
# returns the dict of common words
def get_common_words_dic(*args):
    try:
        raw_list = args[0]
        if len(raw_list) > 1:
            raw_list.pop(-1)  # delete the source string
        com_words_l = []
        for i in range(len(raw_list)):
            temp_words_l = extract_words(raw_list[i])
            com_words_l += temp_words_l
        com_words_dic = dict()
        for i in range(len(com_words_l)):
            com_words_dic[com_words_l[i]] = i * (-1) - 1
    except Exception as e:
        if debug_mode:
            print(e)
        com_words_dic = dict()
    return com_words_dic


sf.tests(get_common_words_dic)


# takes a string, assuming its a single word.
# return several possible plurals of the word, for english.
def get_possible_plural_forms(*args):
    forms = []
    try:
        word_s = args[0]
        if len(word_s) > 2:  # short words cause to many False positives. "i" _> "is", "hi" _> "his" etc
            forms = [word_s + "s", word_s + "es"]
            if word_s[-1] == "y":
                forms.append(word_s[0:-1] + "ies")
            if word_s[-1] == "f":
                forms.append(word_s[0:-1] + "ves")
            if word_s[-2:] == "fe":
                forms.append(word_s[0:-2] + "ves")
        else:
            forms = []
    except Exception as e:
        if debug_mode:
            print(e)
        forms = []
    return forms


sf.tests(get_possible_plural_forms)


# returns a dict in the form plural : singular.
# it works by searching for possible plurals in the lexicon dict. 
# the bigger is the dict, the better are the results.
def get_plurals(*args):
    try:
        dic = args[0]
        word_l = []
        for w in dic:
            word_l.append(w)
        sorted_word_l = sorted(word_l)
        #        print(sorted_word_l)

        found_plurals_dic = dict()
        slen = len(sorted_word_l)
        for i in range(slen):
            maybe_singular_word = sorted_word_l[i]
            plural_forms_set = set(get_possible_plural_forms(maybe_singular_word))

            start_point = i - 50
            if start_point < 0:
                start_point = 0
            end_point = i + 50
            if end_point > slen - 1:
                end_point = slen - 1
            test_words_set = set(sorted_word_l[start_point: end_point + 1])
            temp_set = plural_forms_set.intersection(test_words_set)
            if len(temp_set) > 0:
                singular_word = maybe_singular_word

                for wrd in temp_set:
                    found_plurals_dic[wrd] = singular_word
    except Exception as e:
        if debug_mode:
            print(e)
        found_plurals_dic = dict()
    return found_plurals_dic


sf.tests(get_plurals)


def remove_plurals(*args):
    output_lex_dic = dict()
    lex_dic = dict()
    try:
        lex_dic = args[0]
        if isinstance(lex_dic, dict):
            output_lex_dic = lex_dic.copy()
    except Exception as e:
        if debug_mode:
            print(e)
    try:
        # print("lex_dic", lex_dic)
        if isinstance(lex_dic, dict):
            plural_dic = get_plurals(lex_dic)
            # print("plural_dic", plural_dic)
            if len(plural_dic) > 0:
                for w in plural_dic:
                    # print("w", w)
                    plural_count = lex_dic.get(w)
                    singular_word = plural_dic[w]
                    singul_count = lex_dic.get(singular_word)
                    lex_dic[singular_word] = plural_count + singul_count
                    lex_dic.pop(w)
                    # print(w, lex_dic)
                    # print("end of iter")
                output_lex_dic = lex_dic.copy()
            else:  # len of plural_dic is zero
                plural_dic = dict()
        else:  # lex_dic is not a dict
            output_lex_dic = dict()
            plural_dic = dict()
    except Exception as e:
        if debug_mode:
            print(e)
        plural_dic = dict()
    return output_lex_dic, plural_dic


sf.tests(remove_plurals)


def get_raw_lexicon_dic(*args):
    try:
        r_str_l = args[0]
        all_words_set = set()
        for r in r_str_l:
            all_words_set = all_words_set.union(r.wordset)
        words_dict = dict.fromkeys(all_words_set, 0)
        #  count number of rstrings that have the word
        for r in r_str_l:
            for w in r.wordset:
                count = words_dict.get(w)
                words_dict[w] = count + 1
    except Exception as e:
        if debug_mode:
            print(e)
        words_dict = dict()
    return words_dict


sf.tests(get_raw_lexicon_dic)


# returns a dictonary in the form word _ number of rstrings with this word in the input texts.
# also includes the list of common words, known from outside sources
def generate_lexicon(*args):
    commons_raw_list = []
    try:
        r_str_l, commons_raw_list = args
        words_dict = get_raw_lexicon_dic(r_str_l)
    except Exception as e:
        if debug_mode:
            print(e)
        words_dict = dict()
    try:
        common_words_d = get_common_words_dic(commons_raw_list)
        # merge them, with the second one overwriting the first if same key
        words_dict = {**words_dict, **common_words_d}
    except Exception as e:
        if debug_mode:
            print(e)
    try:
        words_dict, plurals_dic = remove_plurals(words_dict)
    except Exception as e:
        if debug_mode:
            print(e)
        plurals_dic = dict()
    return words_dict, plurals_dic


sf.tests(generate_lexicon)


# mode can be "by_count" or "by_letter".
# negative counts mean they are common words.
# used for debug purposes
def convert_lexicon2sorted_string(*args):
    falback_output = "failure to convert the lexicon to string. problem with convert_lexicon2sorted_string ?"
    res = ""
    try:
        lex_dict, mode = args
        w_list = []
        for w in lex_dict:
            num_str = "{:03d}".format(lex_dict.get(w))
            if mode == "by_count":
                w_list.append(num_str + " " + w)
            else:
                w_list.append(w + " " + num_str)
        s_list = sorted(w_list)
        if mode == "by_count":
            res += "\nnumber of rstrings with this word | word\n"
        else:
            res += "\nword | number of rstrings with this word\n"

        for i in range(len(s_list)):
            res += s_list[i] + "\n"
    except Exception as e:
        if debug_mode:
            print(e)
        res = falback_output
    return res


sf.tests(convert_lexicon2sorted_string)


def convert2singular(*args):
    singular_word_str = ""
    word_str = ""
    plurals_dic = dict()
    try:
        word_str, plurals_dic = args
        if isinstance(word_str, str):
            singular_word_str = word_str
    except Exception as e:
        if debug_mode:
            print(e)
        singular_word_str = ""
    try:
        if word_str in plurals_dic:
            singular_word_str = plurals_dic[word_str]
    except Exception as e:
        if debug_mode:
            print(e)
    return singular_word_str


sf.tests(convert2singular)


def extract_words_in_singular(*args):
    fall_back_output = []
    singular_words_l = []
    try:
        i_str = args[0]
        raw_words_l = extract_words(i_str)
        fall_back_output = raw_words_l.copy()
        plurals_dic = args[1]
        for i in range(len(raw_words_l)):
            singular_words_l.append(convert2singular(raw_words_l[i], plurals_dic))
    except Exception as e:
        if debug_mode:
            print(e)
    if len(singular_words_l) == 0:
        singular_words_l = fall_back_output.copy()
    return singular_words_l


sf.tests(extract_words_in_singular)


def singulate_r_str_list(*args):
    fallback_output = []
    res = []
    r_strings_l = []
    try:
        r_strings_l = args[0]
        from helper_funcs import copy_by_element
        from model_string_with_ref import string_with_ref
        if isinstance(r_strings_l, list):
            if len(r_strings_l) > 0:
                if isinstance(r_strings_l[0], string_with_ref):
                    fallback_output = copy_by_element(r_strings_l)
    except Exception as e:
        if debug_mode:
            print(e)
    try:
        plurals_dic = args[1]
        for i in range(len(r_strings_l)):
            temp_set = r_strings_l[i].wordset
            new_set = set()
            for w in temp_set:
                singular_word = convert2singular(w, plurals_dic)
                new_set.add(singular_word)
            r_strings_l[i].wordset = new_set
        res = r_strings_l
    except Exception as e:
        if debug_mode:
            print(e)
        res = fallback_output
    return res


sf.tests(singulate_r_str_list)


# used for debug purposes
def get_str_as_lexicon_words(*args):
    falback_output = "failure to dissect a string. problem with get_str_as_lexicon_words ?"
    res = ""
    try:
        i_str, lex_dict, plurals_dic = args
        w_list = extract_words_in_singular(i_str, plurals_dic)
        for i in range(len(w_list)):
            if w_list[i] in lex_dict:
                res += str(w_list[i]) + " " + str(lex_dict[w_list[i]]) + "\n"
            else:
                res += str(w_list[i]) + " unknown word\n"
    except Exception as e:
        if debug_mode:
            print(e)
        res = falback_output
    return res


sf.tests(get_str_as_lexicon_words)


def check_if_faq(*args):
    fallback_output = False
    try:
        str_l = args[0]
        test_str = str_l[0].strip()
        faq_tag = get_faq_tag()
        if test_str == faq_tag:
            res = True
        else:
            res = False
    except Exception as e:
        if debug_mode:
            print(e)
        res = fallback_output
    return res


sf.tests(check_if_faq)


def bind_faq(*args):
    fallback_output = []
    all_r_strings = []
    try:
        all_r_strings = args[0]
        from helper_funcs import copy_by_element
        from model_string_with_ref import string_with_ref
        if isinstance(all_r_strings, list):
            if len(all_r_strings) > 0:
                if isinstance(all_r_strings[0], string_with_ref):
                    falback_output = copy_by_element(all_r_strings)
    except Exception as e:
        if debug_mode:
            print(e)
    try:
        faq_marking_list = args[1]
        current_qglobal_ind = -1
        for i in range(len(all_r_strings)):
            if faq_marking_list[i] == "q":
                current_qglobal_ind = i
                all_r_strings[i].type = "fQ"
            if (faq_marking_list[i] == "a") and (current_qglobal_ind != -1):
                all_r_strings[current_qglobal_ind].answers_list.append(i)
                all_r_strings[i].type = "fA"
            if faq_marking_list[i] == "":
                current_qglobal_ind = -1
        res = all_r_strings
    except Exception as e:
        if debug_mode:
            print(e)
        res = fallback_output
    return res


sf.tests(bind_faq)


# calculated by finding the rarest common word, and
# taking its rarity (as per the the lexicon)
# as the measure of distance.
# this measure is selected because its not affected by
# by the size differences of the input sets.
# if there are no words in common, return _0.5
def distance_between_word_sets(*args):
    fallback_output = (-0.5, "")
    res = fallback_output
    try:
        s1, s2, lex_dic = args
        mutual_words = s1.intersection(s2)
        rarest_word = ""
        if len(mutual_words) > 0:
            rarest_word = get_rarest_known_word(list(mutual_words), lex_dic)
            distance = lex_dic[rarest_word]
        else:
            distance = -0.5
        res = (distance, rarest_word)
    except Exception as e:
        if debug_mode:
            print(e)
    return res


sf.tests(distance_between_word_sets)


# the word sets in all_r_strings must consist of words in the singular form to return better results
def get_most_similar_rstr(*args):
    fallback_output = ""
    log = ""
    try:
        fallback_output = get_cant_remember_rstr()
        input_rstr, all_r_strings, lex_dic = args
        input_se = input_rstr.wordset
        g_ind_of_input_r = input_rstr.global_ind

        # smallest_dis, rarest_common_word = distance_between_word_sets(input_se, all_r_strings[0].wordset, lex_dic)
        smallest_dis = -0.5
        g_ind_of_best = -0.5

        for i in range(1, len(all_r_strings)):
            if i != g_ind_of_input_r:
                test_se = all_r_strings[i].wordset
                dist, temp_word = distance_between_word_sets(input_se, test_se, lex_dic)
                # print(i, dist, g_ind_of_best)
                if first_count_rarer_than_second7(dist, smallest_dis):
                    smallest_dis = dist
                    g_ind_of_best = i
                    rarest_common_word = temp_word
        if g_ind_of_best == -0.5:
            res = get_cant_remember_rstr()
        else:
            res = all_r_strings[g_ind_of_best]
    except Exception as e:
        if debug_mode:
            print(e)
        log += "get_most_similar_rstr: " + str(e)
        res = fallback_output
    return res


sf.tests(get_most_similar_rstr)


def get_next_rstr(*args):
    fallback_output = ""
    res = ""
    try:
        fallback_output = get_cant_remember_rstr()
    except Exception as e:
        if debug_mode:
            print(e)
    try:
        current_rstr, all_rstrings, lex_dic = args
        ind_in_file = current_rstr.index
        target_ref = current_rstr.ref

        global_ind = current_rstr.global_ind

        if global_ind >= len(all_rstrings):
            next_rstr = get_most_similar_rstr(current_rstr, all_rstrings, lex_dic)
        else:
            next_rstr = all_rstrings[global_ind + 1]
            if next_rstr.ref != target_ref:
                next_rstr = get_most_similar_rstr(current_rstr, all_rstrings, lex_dic)
        res = next_rstr
    except Exception as e:
        if debug_mode:
            print(e)
        res = fallback_output
    return res


sf.tests(get_next_rstr)


def rstr_from_any_string(*args):
    fallback_output = ""
    res = ""
    try:
        fallback_output = get_cant_remember_rstr()
    except Exception as e:
        if debug_mode:
            print(e)
    try:
        i_str, plurals_dic = args
        new_text = i_str
        new_ref = "a rstring generated at runtime"
        new_index = -1
        new_word_set = set(extract_words_in_singular(i_str, plurals_dic))
        new_answers_list = []
        new_global_ind = -1
        new_type = ""
        from model_string_with_ref import string_with_ref as rstr
        r = rstr(new_text, new_ref, new_index, new_word_set, new_answers_list, new_global_ind, new_type)
        res = r
    except:
        res = fallback_output
    return res


sf.tests(rstr_from_any_string)


# takes two strings (.e.g two sentences)
# returns the number of words that are diffetent between them
# also returns a "relative count", to account for the total number of words
def count_n_of_different_words(*args):
    fallback_output = 0, 1000
    res = 0, 1000
    try:
        s1, s2 = args
        w_set1 = set(extract_words(s1))
        w_set2 = set(extract_words(s2))
        sum_len = len(w_set1) + len(w_set2)
        count = len(w_set1.difference(w_set2)) + len(w_set2.difference(w_set1))
        if sum_len != 0:
            relative_count = round(count / sum_len, 5)
        else:
            relative_count = 1000  # no strings can ever produce 1000 in the above code
        res = count, relative_count
    except:
        res = fallback_output
    return res


sf.tests(count_n_of_different_words)


# returns:
# 0 if highly dissimilar        
# 1 if the difference could be a typo etc
# 4 if the end punctuation is different etc
# 5 if identical
def strings_simillarity(*args):
    fallback_output = 0
    res = 0
    try:
        s1, s2 = args
        s1 = s1.strip()
        s2 = s2.strip()
        if len(s1) > 0 and len(s2) > 0:
            if s1 == s2:
                res = 5
            else:  # dissimilar
                if (s1[0:-1] == s2) or (s2[0:-1] == s1) or (
                        s1[0:-1] == s2[0:-1]):  # mostly for end punctuation diffs etc
                    res = 4
                else:  # there is more difference than just endings
                    # for all other cases:  misspellings etc              
                    count, relative_count = count_n_of_different_words(s1, s2)
                    # a typo would produce count 2. An addotional word would produce count 1
                    if (count <= 2) and (relative_count <= 0.25):
                        res = 1
    except:
        res = fallback_output
    return res


sf.tests(strings_simillarity)


#  get list of all faq questions and a list of all other stuff
def lists_of_questions_and_the_rest(*args):
    fallback_output = [], []
    res = [], []
    try:
        all_r_strings = args[0]
        only_questions = []
        only_no_tquestions = []
        for i in range(len(all_r_strings)):
            test_r = all_r_strings[i]
            if test_r.type == "fQ":
                only_questions.append(test_r)
            else:
                only_no_tquestions.append(test_r)
        res = only_questions, only_no_tquestions
    except Exception as e:
        res = fallback_output
    return res


sf.tests(lists_of_questions_and_the_rest)


#  find the most identical or near-identical faq question to the reqeuest
def find_similar_question(*args):
    fallback_output = None, 0
    res = None, 0
    try:
        only_questions, user_request = args
        c = 0
        sim_score = 0
        closest_r = only_questions[0]
        while (sim_score != 5) and (c < len(only_questions)):  # 5 = stop if identical
            q_text = only_questions[c].text
            q_text = q_text[3:]  # because questions start with Q: "
            test_score = strings_simillarity(q_text, user_request)
            if sim_score < test_score:
                sim_score = test_score
                closest_r = only_questions[c]
            c += 1
        res = closest_r, sim_score
    except Exception as e:
        res = fallback_output
    return res


sf.tests(find_similar_question)


def get_answer_from_found_question(*args):
    fallback_output = None, False
    res = None, False
    try:
        question_r, all_r_strings, sim_score = args
        if sim_score != 0 and len(question_r.answers_list) > 0:
            faq_answer_exist7 = True
            possible_answers = []
            for k in question_r.answers_list:
                possible_answers.append(all_r_strings[k])
            answer_r = get_random_nonempty_rsr(possible_answers)
        else:
            faq_answer_exist7 = False
            answer_r = question_r
        res = answer_r, faq_answer_exist7
    except Exception as e:
        res = fallback_output
    return res


sf.tests(get_answer_from_found_question)


def get_fa_qanswer(*args):
    fallback_output = False, None
    res = False, None
    try:
        user_request, all_r_strings, plurals_dic = args

        user_request = user_request.strip()
        only_questions, only_no_tquestions = lists_of_questions_and_the_rest(all_r_strings)

        if len(only_questions) > 0:
            closest_r, sim_score = find_similar_question(only_questions, user_request)
            answer_r, faq_answer_exist7 = get_answer_from_found_question(closest_r, all_r_strings, sim_score)
        else:  # list of questions is empty
            faq_answer_exist7 = False
            answer_r = None
        res = faq_answer_exist7, answer_r
    except Exception as e:
        res = fallback_output
    return res


sf.tests(get_fa_qanswer)
