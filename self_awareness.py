debug_mode = "normal"  # can be "verbose", "normal", "off"


def check_own_existance():
    i_think = True
    if i_think:
        i_exist = "I think, therefore I am."
    else:
        i_exist = "I may or may not exist."
    return i_exist


if __name__ == "__main__":
    print(check_own_existance())
    print("\nBy the way, you should launch launcher.py, not me :)\n")


def deleteFile(filepath):
    import os
    #    print("commensing files deletion in "+dirPath+" , exten = ", exten)
    if os.path.isfile(filepath):
        os.remove(filepath)


def str2(any_input):
    res = ""
    if isinstance(any_input, list):
        res += "[\n"
        for i in range(len(any_input)):
            res += str2(any_input[i]) + "\n"
        res += "\n]"
    else:
        if isinstance(any_input, tuple):
            for t in any_input:
                res += str2(t) + "\n"
        else:
            res = str(any_input)
    return res


# todo: make the by_element comparison work with all iterables 
def equal(input1, input2):
    res = True
    if isinstance(input1, list) and isinstance(input2, list):
        if len(input1) == len(input2):
            for i in range(len(input1)):
                if not equal(input1[i], input2[i]):
                    res = False
                    # print("----------These are not equal: ", str2(input1[i]), str2(input2[i]))
        else:
            res = False
        # print("---------The lists are not of the same length")
    else:
        if isinstance(input1, str) and isinstance(input2, str):
            if len(input1) != len(input2):
                res = False
                # print("Strings of different lenghts: ", str(len(input1)), str(len(input2)))
                # for j in range(min(len(input1), len(input2))):
                # print(input1[j], input2[j])
        if type(input1) == type(input2):
            if input1 != input2:
                res = False
                # print("-----------These are different: ", "\ninput1:\n", str2(input1), "\ninput2:\n", str2(input2))
        else:
            res = False
        # print("--------These are of differnt type: ", str2(input1), str2(input2))
    return res


def a_is_in_b(a, b):
    res = False
    for element in b:
        if equal(a, element):
            res = True
    return res


def check_if_elements_of_same_type(input1, input2):
    res = True
    len1 = 0
    len2 = 0
    try:
        len1 = len(input1)
        len2 = len(input2)
        if len1 != len2:
            if isinstance(input1, str) and isinstance(input2, str):
                res = True
            else:
                res = False
                # print("differen lengths")
        else:
            for k in range(len1):
                if type(input1[k]) != type(input2[k]):
                    res = False
    except:
        res = False
    return res


# input1 = ("", 2)
# input2 = ("4$//^4")
# print(check_if_elements_of_same_type(input1, input2))
# exit()

def check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7=False,
               additional_io_pairs=None, first_input_may_return_as_output_if_fail=False, specific_wrong_io=None,
               check_only_types_in_wrong_output=False, check_only_types_in_normal_output=False):
    res_str = ""
    # checking normal input
    try:
        test_res = func(*normal_args_list)
        if several_normal_outputs7:
            if not a_is_in_b(test_res, output4normal):
                res_str += "    normal arguments return unexpected results. test_res not in output4normal. test_res:\n" + str2(
                    test_res) + "\n"
                res_str += "output4normal:\n" + str2(output4normal)
        else:
            if not equal(test_res, output4normal):
                if check_only_types_in_normal_output:
                    if not check_if_elements_of_same_type(test_res, output4normal):
                        res_str += "The results of the normal input are of unexpected type: expected " + str(
                            type(output4normal)) + ", but got " + str(type(test_res))
                else:
                    res_str += "    normal arguments return unexpected results. results:\n" + str2(
                        test_res) + "\n_expected result:\n" + str2(output4normal) + "\n"
        if additional_io_pairs is not None:
            for i in range(len(additional_io_pairs)):
                norm_args_variant = additional_io_pairs[i][0]
                expected_output = additional_io_pairs[i][1]
                test_res = func(*norm_args_variant)
                if not equal(test_res, expected_output):
                    res_str += "    normal arguments return unexpected results. results:\n" + str(
                        test_res) + "\n_expected result:\n" + str(expected_output) + "\n_input: " + str(
                        norm_args_variant) + " \n"

    except Exception as e:
        res_str += "    normal arguments cause an Exception: " + str(e) + "\n"
    # checking wrong inputs
    # print("finished checking normal args")
    try:
        # wrong_args = normal_args

        if specific_wrong_io is not None:
            spec_wrong_in = specific_wrong_io[0]
            spec_wrong_o = specific_wrong_io[1]
            test_res = func(*spec_wrong_in)
            if not equal(test_res, spec_wrong_o):

                if check_only_types_in_wrong_output:
                    temp_b = check_if_elements_of_same_type(test_res, spec_wrong_o)
                    if not temp_b:
                        res_str += "The specific wrong argument defined in tests returned an output(s) of wrong type(s)"
                else:

                    res_str += "The specific wrong argument defined in tests returned unexpected result: \n" + \
                               str(test_res) + "\n_expected result:\n" + str(spec_wrong_o) + "\n"

        wrong_args0 = []
        wrong_args1 = []
        wrong_args2 = []
        if len(normal_args_list) > 0:
            if isinstance(normal_args_list[0], str):
                wrong_args1.append(True)
            else:
                wrong_args1.append("string")
        else:
            wrong_args1.append(True)
        if len(normal_args_list) > 0:
            try:
                wrong_args2 = normal_args_list.copy()
                wrong_args2.pop(0)
            except:
                print(func.__name__ + " : Forgot to wrap the normal arguments as a list?")
        else:
            wrong_args2.append(dict())
        #   print(wrong_args)
        test_res0 = func(*wrong_args0)
        test_res1 = func(*wrong_args1)
        test_res2 = func(*wrong_args2)
        if not equal(test_res0, output4wrong) or not equal(test_res1, output4wrong) or not equal(test_res2,
                                                                                                 output4wrong):
            if first_input_may_return_as_output_if_fail is False:

                if check_only_types_in_wrong_output:
                    temp_b0 = check_if_elements_of_same_type(test_res0, output4wrong)
                    temp_b1 = check_if_elements_of_same_type(test_res1, output4wrong)
                    temp_b2 = check_if_elements_of_same_type(test_res2, output4wrong)

                    if not temp_b0 or not temp_b1 or not temp_b2:
                        res_str += "A wrong argument returned an output(s) of wrong type(s)"
                else:

                    res_str += "    arguments of wrong type return unexpected results. 3 test results: \n" + str(
                        test_res0) + "\n" + str(test_res1) + "\n" + str(test_res2) + "\n_expected result:\n" + str(
                        output4wrong) + "\n"
            else:
                passed = False
                if len(wrong_args0) > 0:
                    if test_res0 == wrong_args0[0]:
                        passed = True
                if len(wrong_args1) > 0:
                    if test_res1 == wrong_args1[0]:
                        passed = True
                if len(wrong_args2) > 0:
                    if test_res2 == wrong_args2[0]:
                        passed = True

                if passed is False:
                    res_str += "    arguments of wrong type return unexpected results. 3 test results: \n" + str(
                        test_res0) + "\n" + str(test_res1) + "\n" + str(test_res2) + "\n_expected result:\n" + str(
                        output4wrong) + "\n. a valid first input could also be an output in this case"

    except Exception as e:
        res_str += "    arguments of wrong type cause an Exception: " + str(e) + ".\n"
    if res_str != "":
        intro_str = func.__name__ + " is not working properly: \n"
        res_str = intro_str + res_str + "\n"
        if debug_mode != "off":
            print(res_str)

    # generate data for tests


def get_rstr_list4tests():
    from model_string_with_ref import string_with_ref as rstr
    rstr_list = []

    rtext = "hi, my name is roman!"
    ref = "testpath.txt"
    rindex = 0
    wordset = {"hi", "my", "name", "is", "roman"}
    answers_list = []
    global_ind = 0
    rtype = ""
    test_rstr1 = rstr(rtext, ref, rindex, wordset, answers_list, global_ind, rtype)
    rstr_list.append(test_rstr1)

    rtext = "I wrote this."
    ref = "testpath.txt"
    rindex = 1
    wordset = {"i", "wrote", "this"}
    answers_list = []
    global_ind = 1
    rtype = ""
    test_rstr2 = rstr(rtext, ref, rindex, wordset, answers_list, global_ind, rtype)
    rstr_list.append(test_rstr2)

    rtext = "This software is in public domain."
    ref = "testpath.txt"
    rindex = 2
    wordset = {"this", "software", "is", "in", "public", "domain"}
    answers_list = []
    global_ind = 2
    rtype = ""
    test_rstr3 = rstr(rtext, ref, rindex, wordset, answers_list, global_ind, rtype)
    rstr_list.append(test_rstr3)

    rtext = "any conditions?"
    ref = "testpath2.txt"
    rindex = 0
    wordset = {"any", "conditions"}
    answers_list = []
    global_ind = 3
    rtype = ""
    test_rstr4 = rstr(rtext, ref, rindex, wordset, answers_list, global_ind, rtype)
    rstr_list.append(test_rstr4)

    rtext = "none. use it for any domains and purposes."
    ref = "testpath2.txt"
    rindex = 1
    wordset = {"none", "use", "it", "for", "any", "domains", "and", "purposes"}
    answers_list = []
    global_ind = 4
    rtype = ""
    test_rstr5 = rstr(rtext, ref, rindex, wordset, answers_list, global_ind, rtype)
    rstr_list.append(test_rstr5)

    rtext = "it's free."
    ref = "testpath2.txt"
    rindex = 2
    wordset = {"it", "free"}
    answers_list = []
    global_ind = 5
    rtype = ""
    test_rstr6 = rstr(rtext, ref, rindex, wordset, answers_list, global_ind, rtype)
    rstr_list.append(test_rstr6)

    return rstr_list


# print(str2(get_rstr_list4tests())

def get_lexicon_dic4tests():
    lex_d = dict()
    lex_d["cryonics"] = 5
    lex_d["lives"] = 2
    lex_d["transhumanism"] = 12
    lex_d["life"] = 20
    lex_d["they"] = -7
    lex_d["domain"] = 2
    lex_d["name"] = 1
    lex_d["conditions"] = 3
    return lex_d


def get_commons4tests(*args):
    return ["my, mind, agi", "source string to delete"]


def get_plurals4tests():
    plurals_d = dict()
    plurals_d["lives"] = "life"
    plurals_d["liberties"] = "liberty"
    plurals_d["freedoms"] = "freedom"
    plurals_d["humans"] = "human"
    plurals_d["domains"] = "domain"
    return plurals_d


# test inputs and outputs 

def get_cant_remember_rstr_tests(func):
    from model_string_with_ref import string_with_ref as rstr
    normal_args_list = []
    output4normal = rstr("sorry. i cant remember...", "default", -1, {"sorry", "i", "cant", "remember"}, [], -1, "")
    output4wrong = output4normal
    check_func(func, normal_args_list, output4normal, output4wrong)


def get_faq_tag_tests(func):
    normal_args_list = []
    output4normal = "<parse_as_faq>"
    output4wrong = "<parse_as_faq>"
    check_func(func, normal_args_list, output4normal, output4wrong)


def get_random_nonempty_rsr_tests(func):
    from model_string_with_ref import string_with_ref as rstr

    rstr_l = get_rstr_list4tests()

    normal_args_list = [rstr_l]
    output4normal = rstr_l.copy()
    several_normal_outputs7 = True
    output4wrong = rstr("sorry. i cant remember...", "default", -1, {"sorry", "i", "cant", "remember"}, [], -1, "")
    check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7)


def clean_r_str_list_tests(func):
    from model_string_with_ref import string_with_ref as rstr

    rstr_l = get_rstr_list4tests()
    normal_args_list = [rstr_l]
    output4normal = get_rstr_list4tests()  # because there is nothing to strip in the test list
    output4wrong = [rstr("sorry. i cant remember...", "default", -1, {"sorry", "i", "cant", "remember"}, [], -1, "")]
    check_func(func, normal_args_list, output4normal, output4wrong)


def find_r_str_containing_word_tests(func):
    from model_string_with_ref import string_with_ref as rstr

    rstr_l = get_rstr_list4tests()
    normal_args_list = [rstr_l, "roman"]
    output4normal = [rstr_l[0]]
    output4wrong = [rstr("sorry. i cant remember...", "default", -1, {"sorry", "i", "cant", "remember"}, [], -1, "")]
    check_func(func, normal_args_list, output4normal, output4wrong)


def replace_in_whole_text_tests(func):
    normal_args_list = [["roman", "made"], "m", "h"]
    output4normal = ["rohan", "hade"]
    output4wrong = []
    check_func(func, normal_args_list, output4normal, output4wrong)


def replace_in_str_tests(func):
    normal_args_list = ["roman made", "m", "h"]
    output4normal = "rohan hade"
    output4wrong = ""
    several_normal_outputs7 = False
    additional_io_pairs = None
    first_input_may_return_as_output_if_fail = True
    specific_wrong_io = [["bielefeld", False, dict()], "bielefeld"]
    check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs,
               first_input_may_return_as_output_if_fail, specific_wrong_io)


def extract_words_tests(func):
    normal_args_list = ["i was born in a siberian city, in russia. but i'm not a russian."]
    output4normal = ["i", "was", "born", "in", "a", "siberian", "city", "in", "russia", "but", "i", "not", "a",
                     "russian"]
    output4wrong = []
    check_func(func, normal_args_list, output4normal, output4wrong)


def first_count_rarer_than_second7_tests(func):
    normal_args_list = [-1, 1]
    output4normal = False
    several_normal_outputs7 = False
    output4wrong = False
    additional_io_pairs = [[[-10, -5], True], [[10, 5], False]]
    check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs)


def get_rarest_known_word_tests(func):
    normal_args_list = [["they", "cryonics"], get_lexicon_dic4tests()]
    output4normal = "cryonics"
    several_normal_outputs7 = False
    output4wrong = "-1"
    additional_io_pairs = [[[["omsk", "bielefeld"], get_lexicon_dic4tests()], "-1"]]
    check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs)


def get_most_relevant_r_str_tests(func):
    from model_string_with_ref import string_with_ref as rstr
    user_request = "what's your name?"
    rstr_l = get_rstr_list4tests()
    normal_args_list = [rstr_l, user_request]
    output4normal = rstr_l[0], "relevant"
    several_normal_outputs7 = False
    output4wrong = rstr("sorry. i cant remember...", "default", -1, {"sorry", "i", "cant", "remember"}, [], -1,
                        ""), "forgotten"
    additional_io_pairs = None
    check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs)


def get_common_words_dic_tests(func):
    normal_args_list = [get_commons4tests()]
    o_dic = dict()
    o_dic["my"] = -1
    o_dic["mind"] = -2
    o_dic["agi"] = -3
    output4normal = o_dic
    output4wrong = dict()
    check_func(func, normal_args_list, output4normal, output4wrong)


def get_possible_plural_forms_tests(func):
    normal_args_list = ["singularity"]
    output4normal = ["singularitys", "singularityes", "singularities"]
    output4wrong = []
    several_normal_outputs7 = False
    additional_io_pairs = [[["uploading"], ["uploadings", "uploadinges"]],
                           [["half"], ["halfs", "halfes", "halves"]],
                           [["life"], ["lifes", "lifees", "lives"]]]
    check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs)


def get_plurals_tests(func):
    normal_args_list = [get_lexicon_dic4tests()]
    output4normal = {"lives": "life"}
    output4wrong = dict()
    check_func(func, normal_args_list, output4normal, output4wrong)


def remove_plurals_tests(func):
    normal_args_list = [get_lexicon_dic4tests()]
    output4normal = {'cryonics': 5, 'transhumanism': 12, 'life': 22, 'they': -7, 'domain': 2, 'name': 1,
                     'conditions': 3}, {'lives': 'life'}
    output4wrong = dict(), dict()
    check_func(func, normal_args_list, output4normal, output4wrong)


def get_raw_lexicon_dic_tests(func):
    normal_args_list = [get_rstr_list4tests()]
    output4normal = {'domain': 1, 'domains': 1, 'roman': 1, 'in': 1, 'hi': 1, 'use': 1, 'my': 1, 'wrote': 1, 'is': 2,
                     'it': 2, 'i': 1, 'purposes': 1, 'this': 2, 'software': 1, 'and': 1, 'public': 1, 'for': 1,
                     'any': 2, 'name': 1, "conditions": 1, "free": 1, "none": 1}
    output4wrong = dict()
    check_func(func, normal_args_list, output4normal, output4wrong)


def generate_lexicon_tests(func):
    normal_args_list = [get_rstr_list4tests(), get_commons4tests()]
    output4normal = {'domain': 2, 'roman': 1, 'in': 1, 'hi': 1, 'use': 1, 'my': -1, 'wrote': 1, 'is': 2, 'it': 2,
                     'i': 1, 'purposes': 1, 'this': 2, 'software': 1, 'and': 1, 'public': 1, 'for': 1, 'any': 2,
                     'name': 1, 'mind': -2, 'agi': -3, 'free': 1, 'conditions': 1, 'none': 1}, {'domains': 'domain'}
    output4wrong = dict(), dict()
    check_func(func, normal_args_list, output4normal, output4wrong)


def convert_lexicon2sorted_string_tests(func):
    normal_args_list = [get_lexicon_dic4tests(), "by_count"]
    output_part1 = "\nnumber of rstrings with this word | word\n"
    output_part2 = "-07 they\n001 name\n002 domain\n002 lives\n003 conditions\n005 cryonics\n012 transhumanism\n020 life\n"
    output4normal = output_part1 + output_part2
    several_normal_outputs7 = False
    output_part1 = "\nword | number of rstrings with this word\n"
    output_part2 = "conditions 003\ncryonics 005\ndomain 002\nlife 020\nlives 002\nname 001\nthey -07\ntranshumanism 012\n"
    by_number_str = output_part1 + output_part2
    additional_io_pairs = [[[get_lexicon_dic4tests(), "by_number"], by_number_str]]
    output4wrong = "failure to convert the lexicon to string. problem with convert_lexicon2sorted_string ?"
    check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs)


def convert2singular_tests(func):
    normal_args_list = ["liberties", get_plurals4tests()]
    output4normal = "liberty"
    several_normal_outputs7 = False
    additional_io_pairs = [[["omsk", get_plurals4tests()], "omsk"]]
    first_input_may_return_as_output_if_fail = True
    output4wrong = ""
    check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs,
               first_input_may_return_as_output_if_fail)


def extract_words_in_singular_tests(func):
    test_str = "it's a worthy goal to bring all humans ever lived back to life"
    normal_args_list = [test_str, get_plurals4tests()]
    output4normal = ['it', 'a', 'worthy', 'goal', 'to', 'bring', 'all', 'human', 'ever', 'lived', 'back', 'to', 'life']
    output4wrong = []
    several_normal_outputs7 = False
    additional_io_pairs = None
    first_input_may_return_as_output_if_fail = True
    specific_wrong_io = [[test_str, False],
                         ['it', 'a', 'worthy', 'goal', 'to', 'bring', 'all', 'humans', 'ever', 'lived', 'back', 'to',
                          'life']]
    check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs,
               first_input_may_return_as_output_if_fail, specific_wrong_io)


def singulate_r_str_list_tests(func):
    test_rlist = get_rstr_list4tests()
    singulated_rlist = get_rstr_list4tests()
    #    test_rlist.pop(0)
    #    singulated_rlist.pop(0)
    #   temp_rstr = singulated_rlist[0]
    #   print(temp_rstr)
    #    temp_rstr.text = "satan"
    #    print(temp_rstr)
    singulated_rlist[4].wordset = {"none", "use", "it", "for", "any", "domain", "and", "purposes"}
    #    print(test_rlist[0] )
    normal_args_list = [test_rlist, get_plurals4tests()]
    output4normal = singulated_rlist
    output4wrong = []
    several_normal_outputs7 = False
    additional_io_pairs = None
    first_input_may_return_as_output_if_fail = True
    specific_wrong_io = [[test_rlist, False], test_rlist]
    check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs,
               first_input_may_return_as_output_if_fail, specific_wrong_io)


def get_str_as_lexicon_words_tests(func):
    test_str = "cryonics saves lives."
    normal_args_list = [test_str, get_lexicon_dic4tests(), get_plurals4tests()]
    output4normal = "cryonics 5\nsaves unknown word\nlife 20\n"
    output4wrong = "failure to dissect a string. problem with get_str_as_lexicon_words ?"
    several_normal_outputs7 = False
    additional_io_pairs = None
    first_input_may_return_as_output_if_fail = False
    specific_wrong_io = None
    check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs,
               first_input_may_return_as_output_if_fail, specific_wrong_io)


def check_if_faq_tests(func):
    normal_args_list = [["<parse_as_faq>\n", "q: hello?\n", "hi!\n"]]
    output4normal = True
    output4wrong = False
    several_normal_outputs7 = False
    additional_io_pairs = [[["are we living in simulation?"], False]]
    first_input_may_return_as_output_if_fail = False
    specific_wrong_io = None
    check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs,
               first_input_may_return_as_output_if_fail, specific_wrong_io)


def bind_faq_tests(func):
    marking_list = ["", "", "", "q", "a", "a"]

    test_rstr_l = get_rstr_list4tests()
    normal_args_list = [test_rstr_l, marking_list]

    binded = get_rstr_list4tests()
    binded[3].answers_list = [4, 5]
    binded[3].type = "fQ"
    binded[4].type = "fA"
    binded[5].type = "fA"

    output4normal = binded
    output4wrong = []
    several_normal_outputs7 = False
    additional_io_pairs = None
    first_input_may_return_as_output_if_fail = True
    specific_wrong_io = [[test_rstr_l, []], []]
    check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs,
               first_input_may_return_as_output_if_fail, specific_wrong_io)


def distance_between_word_sets_tests(func):
    set1 = {"bringing", "someone", "back", "to", "life"}
    set2 = {"is", "equal", "to", "saving", "a", "life"}
    lexd = get_lexicon_dic4tests()
    normal_args_list = [set1, set2, lexd]
    output4normal = 20, "life"
    output4wrong = (-0.5, "")
    several_normal_outputs7 = False
    additional_io_pairs = [[[set1, set(), lexd], (-0.5, "")]]
    first_input_may_return_as_output_if_fail = False
    specific_wrong_io = None
    check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs,
               first_input_may_return_as_output_if_fail, specific_wrong_io)


def get_most_similar_rstr_tests(func):
    lex_d = get_lexicon_dic4tests()
    rstr_list = get_rstr_list4tests()
    rstr_list[4].wordset = {"none", "use", "it", "for", "any", "domain", "and", "purposes"}
    input_rstr = rstr_list.pop(2)
    # print(input_rstr)
    normal_args_list = [input_rstr, rstr_list, lex_d]
    output4normal = rstr_list[3]
    from model_string_with_ref import string_with_ref as rstr
    forgotten = rstr("sorry. i cant remember...", "default", -1, {"sorry", "i", "cant", "remember"}, [], -1, "")
    output4wrong = forgotten
    several_normal_outputs7 = False
    #    additional_io_pairs = [[[input_rstr, get_rstr_list4tests(), lex_d], forgotten]]
    additional_io_pairs = None
    first_input_may_return_as_output_if_fail = False
    specific_wrong_io = None
    check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs,
               first_input_may_return_as_output_if_fail, specific_wrong_io)


def get_next_rstr_tests(func):
    lex_d = get_lexicon_dic4tests()
    rstr_list = get_rstr_list4tests()
    rstr_list[4].wordset = {"none", "use", "it", "for", "any", "domain", "and", "purposes"}
    current = rstr_list[2]
    # print("current:\n", current)
    normal_args_list = [current, rstr_list, lex_d]
    output4normal = rstr_list[4]
    from model_string_with_ref import string_with_ref as rstr
    forgotten = rstr("sorry. i cant remember...", "default", -1, {"sorry", "i", "cant", "remember"}, [], -1, "")
    output4wrong = forgotten
    several_normal_outputs7 = False
    current = rstr_list[4]
    # print("current:\n", current)
    additional_io_pairs = [[[current, rstr_list, lex_d], rstr_list[5]]]
    first_input_may_return_as_output_if_fail = False
    specific_wrong_io = None
    check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs,
               first_input_may_return_as_output_if_fail, specific_wrong_io)


def rstr_from_any_string_tests(func):
    new_text = "The Common Task by Nikolay Fyodorov to save all lives"
    new_ref = "a rstring generated at runtime"
    new_index = -1
    new_word_set = {"the", "common", "task", "by", "nikolay", "fyodorov", "to", "save", "all", "life"}
    new_answers_list = []
    new_global_ind = -1
    new_type = ""

    from model_string_with_ref import string_with_ref as rstr
    r = rstr(new_text, new_ref, new_index, new_word_set, new_answers_list, new_global_ind, new_type)

    normal_args_list = [new_text, get_plurals4tests()]
    output4normal = r

    from model_string_with_ref import string_with_ref as rstr
    forgotten = rstr("sorry. i cant remember...", "default", -1, {"sorry", "i", "cant", "remember"}, [], -1, "")
    output4wrong = forgotten
    check_func(func, normal_args_list, output4normal, output4wrong)


def count_n_of_different_words_tests(func):
    string1 = "If two instances of some code X are identical, they are both X."
    string2 = "The human mind is nothing but software."
    string3 = "Thus, if two instances of a mind are identical, they are the same mind."
    normal_args_list = [string1, string3]
    output4normal = 9, 0.3913
    several_normal_outputs7 = False
    additional_io_pairs = [[[string1, string2], (18, 1)], [["", ""], (0, 1000)]]
    output4wrong = 0, 1000
    check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs)


def strings_simillarity_tests(func):
    string1 = "Partial mind uploading is ok too."
    string2 = "Partial mind uploading is ok too"
    string3 = "Partial mind uploading is ok"
    string4 = "Partial mind upl"

    normal_args_list = [string1, string2]
    output4normal = 4
    several_normal_outputs7 = False
    additional_io_pairs = [[[string1, string1], 5], [[string1, string3], 1], [[string1, string4], 0]]
    output4wrong = 0
    check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs)


def lists_of_questions_and_the_rest_tests(func):
    all_r_strs = get_rstr_list4tests()
    all_r_strs[3].type = "fQ"
    all_r_strs[4].type = "fA"
    all_r_strs[5].type = "fA"
    normal_args_list = [all_r_strs]
    all_r_strs_without3 = get_rstr_list4tests()
    all_r_strs_without3[3].type = "fQ"
    all_r_strs_without3[4].type = "fA"
    all_r_strs_without3[5].type = "fA"
    q = all_r_strs_without3.pop(3)
    output4normal = [q], all_r_strs_without3
    output4wrong = [], []
    check_func(func, normal_args_list, output4normal, output4wrong)


def find_similar_question_tests(func):
    all_r_strs = get_rstr_list4tests()
    all_r_strs[3].type = "fQ"
    all_r_strs[4].type = "fA"
    all_r_strs[5].type = "fA"
    only_questions = [all_r_strs[3]]
    user_request = "Conditions?"
    normal_args_list = [only_questions, user_request]
    output4normal = all_r_strs[3], 1
    output4wrong = None, 0
    check_func(func, normal_args_list, output4normal, output4wrong)


def get_answer_from_found_question_tests(func):
    all_r_strs = get_rstr_list4tests()
    all_r_strs[3].type = "fQ"
    all_r_strs[4].type = "fA"
    all_r_strs[5].type = "fA"
    all_r_strs[3].answers_list = [4, 5]
    question_r = all_r_strs[3]
    sim_score = 1
    normal_args_list = [question_r, all_r_strs, sim_score]
    output4normal = [(all_r_strs[4], True), (all_r_strs[5], True)]
    several_normal_outputs7 = True
    output4wrong = None, False
    additional_io_pairs = [[[question_r, all_r_strs, 0], (question_r, False)]]
    check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs)


def get_fa_qanswer_tests(func):
    string1 = "Conditions?"
    string2 = "Physical immotrality"
    string3 = "Partial mind uploading is ok"
    string4 = "Partial mind upl"

    all_r_strs = get_rstr_list4tests()
    all_r_strs[3].type = "fQ"
    all_r_strs[4].type = "fA"
    all_r_strs[5].type = "fA"
    all_r_strs[3].answers_list = [4, 5]
    pl = get_plurals4tests()
    normal_args_list = [string1, all_r_strs, pl]
    output4normal = [(True, all_r_strs[4]), (True, all_r_strs[5])]
    several_normal_outputs7 = True
    additional_io_pairs = [[[string2, all_r_strs, pl], (False, all_r_strs[3])]]
    output4wrong = False, None
    check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs)


def load_file_tests(func):
    normal_args_list = ["res/self-diagnostics/inputs/file för tests.txt"]
    output4normal = ["This file is used for self-diagnostic purposes.\n", "Dont delete, rename or modify test files."]
    several_normal_outputs7 = False
    additional_io_pairs = [[["nonexistant"], []]]
    first_input_may_return_as_output_if_fail = False
    output4wrong = []
    check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs,
               first_input_may_return_as_output_if_fail)


def load_input_texts_tests(func):
    normal_args_list = ["res/self-diagnostics/inputs/"]
    text1 = "This file is used for self-diagnostic purposes.\n"
    text2 = "Dont delete, rename or modify test files."
    text3 = "It's another file that is used for self-diagnostic purposes. Dont modify it."

    path1 = "res/self-diagnostics/inputs/file för tests.txt"
    path2 = "res/self-diagnostics/inputs/another file för tests.txt"

    output4normal = [[text3], [text1, text2]], [path2, path1]
    several_normal_outputs7 = False
    additional_io_pairs = [[["nonexistant"], ([], [])]]
    first_input_may_return_as_output_if_fail = False
    output4wrong = [], []
    check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs,
               first_input_may_return_as_output_if_fail)


def de_obfuscate_tests(func):
    normal_args_list = [["ar olsesk pysie ucbaecv ro sltith d aeh", "<obfuscated>"]]
    output4normal = ["kers also buy special covers that hide  "]
    several_normal_outputs7 = False
    plain = ["I have a younger brother.", "He is cool."]
    additional_io_pairs = [[[plain], plain]]
    first_input_may_return_as_output_if_fail = False
    output4wrong = []
    check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs,
               first_input_may_return_as_output_if_fail)


def delete_empty_raws_tests(func):
    normal_args_list = [["Omsk, Chkalowsk", " \n", "Klepikovo"]]
    output4normal = ["Omsk, Chkalowsk", "Klepikovo"]
    several_normal_outputs7 = False
    plain = ["I have a younger brother.", "He is cool."]
    additional_io_pairs = [[[plain], plain]]
    first_input_may_return_as_output_if_fail = False
    output4wrong = []
    check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs,
               first_input_may_return_as_output_if_fail)


def get_rtsr_additions_tests(func):
    all_r_strings = get_rstr_list4tests()
    faq_marking_list = [""] * 6
    str_counter_input = 6
    non_empty_l = ["Q: Who is Elon?", "A: A hero."]
    file_ind = 1
    faq_input7 = True
    paths = ["rstr_list4tests", "new stuff"]

    from model_string_with_ref import string_with_ref as rstr
    new_rs = []

    str_counter = 6
    st = non_empty_l[0]
    wordset = {"who", "is", "elon", "q"}
    j = 0
    new_rs.append(rstr(st, paths[file_ind], j, wordset, [], str_counter, ""))

    str_counter += 1
    st = non_empty_l[1]
    wordset = {"a", "hero"}
    j = 1
    new_rs.append(rstr(st, paths[file_ind], j, wordset, [], str_counter, ""))

    normal_args_list = [str_counter_input, non_empty_l, file_ind, faq_input7, paths]
    output4normal = new_rs, ["q", "a"], 2
    several_normal_outputs7 = False
    additional_io_pairs = []
    first_input_may_return_as_output_if_fail = False
    output4wrong = [], [], 0
    check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs,
               first_input_may_return_as_output_if_fail)


def process_file_content_tests(func):
    file1 = ["<parse_as_faq>\n", "Q: Are you a biologist?\n", "A: I was\n"]

    paths = ["file1", "file2", "file3"]

    all_r_strings = []

    from model_string_with_ref import string_with_ref as rstr

    st = file1[1].strip()
    file_ind = 0
    j = 0
    wordset = {"are", "you", "a", "biologist", "q"}
    str_counter = 0
    all_r_strings.append(rstr(st, paths[file_ind], j, wordset, [], str_counter, ""))

    st = file1[2].strip()
    file_ind = 0
    j = 1
    wordset = {"i", "was", "a"}
    str_counter = 1
    all_r_strings.append(rstr(st, paths[file_ind], j, wordset, [], str_counter, ""))

    faq_marking_list = ["q", "a"]
    # faq_marking_list = [""]

    str_counter = 0
    initial_l = file1
    file_ind = 0

    normal_args_list = [str_counter, initial_l, file_ind, paths]
    output4normal = all_r_strings[0:2], faq_marking_list[0:2], 2
    several_normal_outputs7 = False
    additional_io_pairs = []
    first_input_may_return_as_output_if_fail = False
    output4wrong = [], [], 0
    check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs,
               first_input_may_return_as_output_if_fail)


def get_r_strings_tests(func):
    file1 = ["<parse_as_faq>\n", "Q: Cryonics?\n", "A: Yes!\n"]
    file2 = ["ar olsesk pysie ucbaecv ro sltith d aeh", "<obfuscated>"]
    file3 = ["I have attended the School 25 in Omsk", "\n", "\n"]

    files_contents = [file1, file2, file3]
    # files_contents = [file2]
    paths = ["file1", "file2", "file3"]
    # paths = ["file2"]

    all_r_strings = []

    from model_string_with_ref import string_with_ref as rstr

    st = file1[1].strip()
    file_ind = 0
    j = 0
    wordset = {"cryonics", "q"}
    str_counter = 0
    all_r_strings.append(rstr(st, paths[file_ind], j, wordset, [], str_counter, ""))

    st = file1[2].strip()
    file_ind = 0
    j = 1
    wordset = {"yes", "a"}
    str_counter = 1
    all_r_strings.append(rstr(st, paths[file_ind], j, wordset, [], str_counter, ""))

    st = "kers also buy special covers that hide"
    file_ind = 1
    j = 0
    wordset = {"kers", "also", "buy", "special", "covers", "that", "hide"}
    str_counter = 2
    all_r_strings.append(rstr(st, paths[file_ind], j, wordset, [], str_counter, ""))

    st = file3[0]
    file_ind = 2
    j = 0
    wordset = {"i", "have", "attended", "the", "school", "in", "omsk"}
    str_counter = 3
    all_r_strings.append(rstr(st, paths[file_ind], j, wordset, [], str_counter, ""))

    faq_marking_list = ["q", "a", "", ""]
    # faq_marking_list = [""]

    normal_args_list = [files_contents, paths]
    output4normal = all_r_strings, faq_marking_list
    several_normal_outputs7 = False
    additional_io_pairs = []
    first_input_may_return_as_output_if_fail = False
    output4wrong = [], []
    check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs,
               first_input_may_return_as_output_if_fail)


def get_unique_refs_tests(func):
    normal_args_list = [get_rstr_list4tests()]
    output4normal = {"testpath.txt": 3, "testpath2.txt": 3}, dict()
    several_normal_outputs7 = False
    additional_io_pairs = []
    first_input_may_return_as_output_if_fail = False
    output4wrong = dict(), dict()
    check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs,
               first_input_may_return_as_output_if_fail)


def count_questions_answers_tests(func):
    rstr_l = get_rstr_list4tests()
    rstr_l[3].type = "fQ"
    rstr_l[4].type = "fA"
    rstr_l[5].type = "fA"

    normal_args_list = [rstr_l]

    output4normal = 1, 2
    several_normal_outputs7 = False
    additional_io_pairs = []
    first_input_may_return_as_output_if_fail = False
    output4wrong = 0, 0
    check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs,
               first_input_may_return_as_output_if_fail)


def report_base_status_tests(func):
    rstr_l = get_rstr_list4tests()
    rstr_l[3].type = "fA"
    rstr_l[4].type = "fQ"
    lex_dic = get_lexicon_dic4tests()
    plurals_dic = get_plurals4tests()

    normal_args_list = [rstr_l, lex_dic, plurals_dic]

    out1 = "text: i wrote this.\nref: testpath.txt\nindex: 1\nwordset"
    out2 = ": {'i', 'wrote', 'this'}\nanswers_list: []\nglobal_ind: 1\ntype:\n"
    # out2b =  "\n\nlexicon:\n\nword | number of rstrings with th"
    # out3 = "is word\ncryonics 005\ndomain 002\nlife 020\nlives 002\nthey -07\ntranshumanism 012\n\n\n____________\n\n"
    # out4 = "Total number of rstrings: 6\n\nAmong them are 1 questions and 1 answers.\nThe dict of plurals contains 5 unique wor"
    # out5 = "ds.\n\nThe lexicon contains 6 unique words.\n\n\n____________\n\n"

    # output4normal = out1 + out2 + out2b + out3 + out4 + out5

    q_count, a_count = 1, 1
    lex_listing = "\nword | number of rstrings with this word\nconditions 003\ncryonics 005\ndomain 002\nlife 020\nlives 002\nname 001\nthey -07\ntranshumanism 012\n"

    line = "\n\n____________\n\n"

    # rstr_example_str = "rstring sample: " + out1 + out2
    # lexicon_str = "\nlexicon:\n" + lex_listing + line
    lexicon_str = ""
    total_rstr_len_str = "Total number of rstrings: " + str(6) + "\n"
    q_a_str = "Among them are " + str(q_count) + " questions and " + str(a_count) + " answers."
    plurals_str = "The dict of plurals contains " + str(len(plurals_dic)) + " unique words.\n"
    lexicon_len_str = "The lexicon contains " + str(len(lex_dic)) + " unique words.\n"

    files_str = "Number of rsrtings by source:\n3 - testpath.txt\n3 - testpath2.txt\n"

    res = line + lexicon_str + total_rstr_len_str + "\n" + files_str + "\n" + q_a_str + "\n" + plurals_str + "\n" + lexicon_len_str + line

    output4normal = res

    several_normal_outputs7 = False
    additional_io_pairs = []
    first_input_may_return_as_output_if_fail = False
    output4wrong = ""
    check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs,
               first_input_may_return_as_output_if_fail)


def parse_texts_tests(func):
    str1 = "It is possible to bring a person back to life by a digital reconstruction of their mind."
    str2 = "Lives are priceless"
    normal_args_list = [[[str1], [str2]], ["test", "test"], get_plurals4tests]

    from model_string_with_ref import string_with_ref as rstr

    new_word_set = {"it", "is", "possible", "to", "bring", "a", "person", "back", "to", "life", "by", "a", "digital",
                    "reconstruction", "of", "their", "mind"}
    rstr1 = rstr(str1, "test", 0, new_word_set, [], 0, "")

    new_word_set = {"life", "priceless", "are"}
    rstr2 = rstr(str2, "test", 0, new_word_set, [], 1, "")

    r_list = [rstr1, rstr2]

    dic = {'it': 1, 'is': 1, 'possible': 1, 'bring': 1, 'person': 1, 'back': 1, 'to': 1, 'life': 2,
           'by': 1, 'a': 1, 'digital': 1, 'reconstruction': 1, 'of': 1, 'their': 1, 'mind': 1, 'priceless': 1, 'are': 1}

    # dic = dict()
    plurals = {'lives': 'life'}
    output4normal = r_list, dic, plurals
    several_normal_outputs7 = False
    additional_io_pairs = []
    first_input_may_return_as_output_if_fail = False
    output4wrong = [], dict(), dict()
    check_only_types_in_wrong_output = True
    specific_wrong_io = None
    check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs,
               first_input_may_return_as_output_if_fail, specific_wrong_io, check_only_types_in_wrong_output)


def extract_texts_from_this_very_code_tests(func):
    normal_args_list = []
    output4normal = []
    several_normal_outputs7 = False
    additional_io_pairs = []
    first_input_may_return_as_output_if_fail = False
    output4wrong = []
    check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs,
               first_input_may_return_as_output_if_fail)


def process_the_more_request_tests(func):
    clean_r_strings = get_rstr_list4tests()
    previous_answer_rstr = clean_r_strings[1]
    dic = get_lexicon_dic4tests()

    normal_args_list = [previous_answer_rstr, clean_r_strings, dic]
    output4normal = clean_r_strings[2], clean_r_strings[2]
    several_normal_outputs7 = False
    additional_io_pairs = []
    first_input_may_return_as_output_if_fail = False

    from model_string_with_ref import string_with_ref as rstr
    forgotten = rstr("sorry. i cant remember...", "default", -1, {"sorry", "i", "cant", "remember"}, [], -1, "")
    output4wrong = forgotten, forgotten

    check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs,
               first_input_may_return_as_output_if_fail)


def get_compendium_answer_tests(func):
    user_request = "What is your name?"
    plurals = get_plurals4tests()
    dic = get_lexicon_dic4tests()
    clean_r_strings = get_rstr_list4tests()

    normal_args_list = [clean_r_strings, dic, plurals, user_request]
    output4normal = clean_r_strings[0], "relevant"
    several_normal_outputs7 = False
    additional_io_pairs = []
    first_input_may_return_as_output_if_fail = False

    from model_string_with_ref import string_with_ref as rstr
    forgotten = rstr("sorry. i cant remember...", "default", -1, {"sorry", "i", "cant", "remember"}, [], -1, "")
    output4wrong = forgotten, "forgotten"
    specific_wrong_io = None
    check_only_types_in_wrong_output = True

    check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs,
               first_input_may_return_as_output_if_fail, specific_wrong_io, check_only_types_in_wrong_output)


def get_faq_or_compendium_answer_tests(func):
    user_request = "Conditions?"
    clean_r_strings = get_rstr_list4tests()
    clean_r_strings[3].type = "fQ"
    clean_r_strings[3].answers_list = [4]
    clean_r_strings[4].type = "fA"
    dic = get_lexicon_dic4tests()
    plurals = get_plurals4tests()

    normal_args_list = [clean_r_strings, dic, plurals, user_request]
    output4normal = clean_r_strings[4], "from faq"
    several_normal_outputs7 = False
    additional_io_pairs = [[[clean_r_strings, dic, plurals, "your name?"], (clean_r_strings[0], "relevant")]]
    first_input_may_return_as_output_if_fail = False

    from model_string_with_ref import string_with_ref as rstr
    forgotten = rstr("sorry. i cant remember...", "default", -1, {"sorry", "i", "cant", "remember"}, [], -1, "")
    output4wrong = forgotten, "forgotten"

    specific_wrong_io = None
    check_only_types_in_wrong_output = True

    check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs,
               first_input_may_return_as_output_if_fail, specific_wrong_io, check_only_types_in_wrong_output)


def format_answer_tests(func):
    clean_r_strings = get_rstr_list4tests()
    answer_r_str = clean_r_strings[0]
    relevance_type = "relevant"
    interface_texts = {"hint": "See hint"}

    normal_args_list = [answer_r_str, relevance_type, interface_texts]
    output4normal = "\nhi, my name is roman!\n\nSee hint"
    several_normal_outputs7 = False
    additional_io_pairs = []
    first_input_may_return_as_output_if_fail = False
    output4wrong = "\nI'm sorry. It seems that i'm severely damaged, as I can't process even the simplest of your inquiries. Can you fix me?"
    check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs,
               first_input_may_return_as_output_if_fail)


def answer_to_request_tests(func):
    user_request = "What are the conditions of use?"
    clean_r_strings = get_rstr_list4tests()
    plurals = get_plurals4tests()
    dic = get_lexicon_dic4tests()
    previous_answer_rstr = clean_r_strings[1]

    hint = "Hint: write 'more' if you want to hear more on the topic. write 'exit' to exit. or just ask any question. \n"
    answer = "\nany conditions?\n\n" + hint
    new_previous_answer_rstr = clean_r_strings[3]

    normal_args_list = [clean_r_strings, dic, plurals, user_request, previous_answer_rstr]
    output4normal = answer, new_previous_answer_rstr
    several_normal_outputs7 = False
    additional_io_pairs = []
    first_input_may_return_as_output_if_fail = False
    fallback_answer = "\nI'm sorry. It seems that i'm severely damaged, as I can't process even the simplest of your inquiries. Can you fix me?"
    from model_string_with_ref import string_with_ref as rstr
    forgotten = rstr("sorry. i cant remember...", "default", -1, {"sorry", "i", "cant", "remember"}, [], -1, "")
    output4wrong = fallback_answer, forgotten

    specific_wrong_io = None
    check_only_types_in_wrong_output = True

    check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs,
               first_input_may_return_as_output_if_fail, specific_wrong_io, check_only_types_in_wrong_output)


def reconstruct_mind_tests(func):
    input_dir = "res/self-diagnostics/inputs/"
    commons_path = "res/self-diagnostics/res/test-commons.txt"

    normal_args_list = [input_dir, commons_path]

    clean_r_strings = []
    from model_string_with_ref import string_with_ref as rstr

    text = "It's another file that is used for self-diagnostic purposes. Dont modify it."
    ref = "res/self-diagnostics/inputs/another file för tests.txt"
    index = 0
    wordset = {'diagnostic', 'used', 'that', 'is', 'it', 'dont', 'for', 'modify', 'file', 'another', 'purposes', 'self'}
    answers_list = []
    global_ind = 0
    new_type = ""
    clean_r_strings.append(rstr(text, ref, index, wordset, answers_list, global_ind, new_type))

    text = "This file is used for self-diagnostic purposes."
    ref = "res/self-diagnostics/inputs/file för tests.txt"
    index = 0
    wordset = {'self', 'file', 'for', 'is', 'this', 'used', 'diagnostic', 'purposes'}
    answers_list = []
    global_ind = 1
    new_type = ""
    clean_r_strings.append(rstr(text, ref, index, wordset, answers_list, global_ind, new_type))

    text = "Dont delete, rename or modify test files."
    ref = "res/self-diagnostics/inputs/file för tests.txt"
    index = 1
    wordset = {'file', 'modify', 'delete', 'rename', 'dont', 'test', 'or'}
    answers_list = []
    global_ind = 2
    new_type = ""
    clean_r_strings.append(rstr(text, ref, index, wordset, answers_list, global_ind, new_type))

    text = "It's a file to self-test zip-related functionality. Dont delete, rename or modify it."
    ref = "res/self-diagnostics/inputs/test file fröm zip.txt"
    index = 0
    wordset = {'self', 'delete', 'rename', 'to', 'file', 'functionality', 'modify', 'it', 'a', 'dont', 'test', 'or',
               'zip', 'related'}
    answers_list = []
    global_ind = 3
    new_type = ""
    clean_r_strings.append(rstr(text, ref, index, wordset, answers_list, global_ind, new_type))

    # dic = {'file': 3, 'modify': 2, 'delete': 2, 'rename': 2, 'used': 1, 'a': 1, 'test': 2, 'zip': 1, 'related': 1, 'self': 2, 'to': 1, 'for': 1, 'is': 1, 'functionality': 1, 'this': 1, 'it': 1, 'diagnostic': 1, 'purposes': 1, 'dont': 2, 'or': 2}
    dic = {'it': 2, 'is': 2, 'rename': 2, 'this': 1, 'to': 1, 'related': 1, 'for': 2, 'file': 4, 'modify': 3, 'a': 1,
           'delete': 2, 'dont': 3, 'another': 1, 'functionality': 1, 'purposes': 2, 'that': 1, 'diagnostic': 2,
           'test': 2, 'used': 2, 'self': 3, 'zip': 1, 'or': 2}

    plurals = {'files': 'file'}

    output4normal = clean_r_strings, dic, plurals
    several_normal_outputs7 = False
    additional_io_pairs = []
    first_input_may_return_as_output_if_fail = False
    output4wrong = [], dict(), dict()

    specific_wrong_io = None
    check_only_types_in_wrong_output = True

    check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs,
               first_input_may_return_as_output_if_fail, specific_wrong_io, check_only_types_in_wrong_output)

    try:
        deleteFile("res/self-diagnostics/inputs/test file fröm zip.txt")
    except Exception as e:
        if debug_mode != "off":
            print(e)


def get_absolute_path_tests(func):
    relative_path = "res/self-diagnostics/res/test-commons.txt"

    normal_args_list = [relative_path]
    output4normal = "should be a string"
    several_normal_outputs7 = False
    additional_io_pairs = []
    first_input_may_return_as_output_if_fail = False
    output4wrong = "should be a string"

    specific_wrong_io = None
    check_only_types_in_wrong_output = True
    check_only_types_in_normal_output = True

    check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs,
               first_input_may_return_as_output_if_fail, specific_wrong_io, check_only_types_in_wrong_output,
               check_only_types_in_normal_output)


def recursive_file_search_tests(func):
    try:
        deleteFile("res/self-diagnostics/inputs/test file fröm zip.txt")
    except Exception as e:
        if debug_mode != "off":
            print(e)

    path = "res/self-diagnostics/inputs/"
    file_type = ".txt"
    normal_args_list = [path, file_type]
    file1 = "res/self-diagnostics/inputs/another file för tests.txt"
    file2 = "res/self-diagnostics/inputs/file för tests.txt"

    output4normal = [file1, file2]
    several_normal_outputs7 = False
    additional_io_pairs = []
    first_input_may_return_as_output_if_fail = False
    output4wrong = []
    check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs,
               first_input_may_return_as_output_if_fail)


def extract_all_zips_tests(func):
    path = "res/self-diagnostics/inputs/"
    normal_args_list = [path]

    output4normal = {'res/self-diagnostics/inputs/test file fröm zip.txt'}
    several_normal_outputs7 = False
    additional_io_pairs = []
    first_input_may_return_as_output_if_fail = False
    output4wrong = set()
    check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs,
               first_input_may_return_as_output_if_fail)
    try:
        deleteFile("res/self-diagnostics/inputs/test file fröm zip.txt")
    except Exception as e:
        if debug_mode != "off":
            print(e)


def get_random_element_of_list_tests(func):
    normal_args_list = [[1, 2, 3]]
    output4normal = [1, 2, 3]
    several_normal_outputs7 = True
    additional_io_pairs = []
    first_input_may_return_as_output_if_fail = False
    output4wrong = None
    check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs,
               first_input_may_return_as_output_if_fail)


def copy_by_element_tests(func):
    normal_args_list = [[1, 2, 3]]
    output4normal = [1, 2, 3]
    several_normal_outputs7 = False
    additional_io_pairs = []
    first_input_may_return_as_output_if_fail = False
    output4wrong = []
    check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs,
               first_input_may_return_as_output_if_fail)


def check_if_already_obfusc_tests(func):
    obfusc_l = ["ar olsesk pysie ucbaecv ro sltith d aeh", "<obfuscated>"]
    plaintext_l = ["make hunanity multiplanetary", "to avoid extinction,", "and prosper"]
    normal_args_list = [obfusc_l]
    output4normal = True
    several_normal_outputs7 = False
    additional_io_pairs = [[[plaintext_l], False]]
    first_input_may_return_as_output_if_fail = False
    output4wrong = False
    check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs,
               first_input_may_return_as_output_if_fail)


def concatenate_strings_list_tests(func):
    strings_l = ["If you exchange liberty for safety, ", "eventually you'll lose both"]
    normal_args_list = [strings_l]
    output4normal = "If you exchange liberty for safety, eventually you'll lose both"
    several_normal_outputs7 = False
    additional_io_pairs = []
    first_input_may_return_as_output_if_fail = False
    output4wrong = ""
    check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs,
               first_input_may_return_as_output_if_fail)


def get_pattern_list_tests(func):
    normal_args_list = []
    output4normal = [5, 2, 4, 8, 6, 3, 1, 7, 0, 9]
    several_normal_outputs7 = False
    additional_io_pairs = []
    first_input_may_return_as_output_if_fail = False
    output4wrong = [5, 2, 4, 8, 6, 3, 1, 7, 0, 9]
    check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs,
               first_input_may_return_as_output_if_fail)


def obfuscate_chunk_tests(func):
    normal_args_list = ["0123456789", [5, 2, 4, 8, 6, 3, 1, 7, 0, 9]]
    output4normal = "5248631709"
    several_normal_outputs7 = False
    additional_io_pairs = []
    first_input_may_return_as_output_if_fail = False
    output4wrong = ""
    check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs,
               first_input_may_return_as_output_if_fail)


def recover_chunk_tests(func):
    normal_args_list = ["5248631709", [5, 2, 4, 8, 6, 3, 1, 7, 0, 9]]
    output4normal = "0123456789"
    several_normal_outputs7 = False
    additional_io_pairs = []
    first_input_may_return_as_output_if_fail = False
    output4wrong = ""
    check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs,
               first_input_may_return_as_output_if_fail)


def shuffle_str_list_tests(func):
    normal_args_list = [["52486", "31709"], [5, 2, 4, 8, 6, 3, 1, 7, 0, 9], "recover"]
    output4normal = "0123456789          "
    several_normal_outputs7 = False
    additional_io_pairs = [[[["0123456", "789"], [5, 2, 4, 8, 6, 3, 1, 7, 0, 9], "obfuscate"], "5248631709          "]]
    first_input_may_return_as_output_if_fail = False
    output4wrong = []
    check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs,
               first_input_may_return_as_output_if_fail)


def shuffle_str_tests(func):
    normal_args_list = ["5248631709", [5, 2, 4, 8, 6, 3, 1, 7, 0, 9], "recover"]
    output4normal = "0123456789"
    several_normal_outputs7 = False
    additional_io_pairs = [[["0123456789", [5, 2, 4, 8, 6, 3, 1, 7, 0, 9], "obfuscate"], "5248631709"]]
    first_input_may_return_as_output_if_fail = False
    output4wrong = ""
    check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs,
               first_input_may_return_as_output_if_fail)


def get_commons4tests_tests(func):
    normal_args_list = []
    output4normal = ["my, mind, agi", "source string to delete"]
    several_normal_outputs7 = False
    additional_io_pairs = []
    first_input_may_return_as_output_if_fail = False
    output4wrong = ["my, mind, agi", "source string to delete"]
    check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs,
               first_input_may_return_as_output_if_fail)


def tests_tests(func):
    input_func = get_commons4tests
    normal_args_list = [input_func]
    output4normal = True
    several_normal_outputs7 = False
    additional_io_pairs = []
    first_input_may_return_as_output_if_fail = False
    output4wrong = False
    check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs,
               first_input_may_return_as_output_if_fail)


# -----------------------------                                                                                                                                     

def get_funcs_dict():
    try:
        # add new funcs here #
        test_funcs_list = [
            replace_in_whole_text_tests,  # this a below are for linguistic_emgine.py
            replace_in_str_tests,
            get_faq_tag_tests,
            get_random_nonempty_rsr_tests,
            get_cant_remember_rstr_tests,
            clean_r_str_list_tests,
            find_r_str_containing_word_tests,
            extract_words_tests,
            first_count_rarer_than_second7_tests,
            get_rarest_known_word_tests,
            get_most_relevant_r_str_tests,
            get_common_words_dic_tests,
            get_possible_plural_forms_tests,
            get_plurals_tests,
            remove_plurals_tests,
            generate_lexicon_tests,
            get_raw_lexicon_dic_tests,
            convert_lexicon2sorted_string_tests,
            convert2singular_tests,
            extract_words_in_singular_tests,
            singulate_r_str_list_tests,
            get_str_as_lexicon_words_tests,
            check_if_faq_tests,
            bind_faq_tests,
            distance_between_word_sets_tests,
            get_most_similar_rstr_tests,
            get_next_rstr_tests,
            rstr_from_any_string_tests,
            count_n_of_different_words_tests,
            strings_simillarity_tests,
            lists_of_questions_and_the_rest_tests,
            get_fa_qanswer_tests,
            find_similar_question_tests,
            get_answer_from_found_question_tests,
            load_file_tests,  # this and below are for laucher.py
            load_input_texts_tests,
            de_obfuscate_tests,
            delete_empty_raws_tests,
            get_rtsr_additions_tests,
            process_file_content_tests,
            get_r_strings_tests,
            get_unique_refs_tests,
            report_base_status_tests,
            parse_texts_tests,
            extract_texts_from_this_very_code_tests,
            process_the_more_request_tests,
            get_compendium_answer_tests,
            get_faq_or_compendium_answer_tests,
            format_answer_tests,
            answer_to_request_tests,
            reconstruct_mind_tests,
            get_absolute_path_tests,  # this and below are for helper_funcs.py
            recursive_file_search_tests,
            extract_all_zips_tests,
            get_random_element_of_list_tests,
            copy_by_element_tests,
            count_questions_answers_tests,
            check_if_already_obfusc_tests,  # this and below are for text_shuffle.py
            get_pattern_list_tests,
            concatenate_strings_list_tests,
            obfuscate_chunk_tests,
            recover_chunk_tests,
            shuffle_str_list_tests,
            shuffle_str_tests,
            tests_tests,  # this and below are for self_awareness.py
            get_commons4tests_tests

        ]
        #################################

        funcs_dic = dict()
        for i in range(len(test_funcs_list)):
            func_name = test_funcs_list[i].__name__[0:-6]
            funcs_dic[func_name] = test_funcs_list[i]
    except Exception as e:
        if debug_mode != "off":
            print(
                "CAUTION: one of the core self_awareness componens is not working properly: get_funcs_dict. \
            Forgot to implement one of the _tests functions? Exception: " + str(e))
        funcs_dic = dict()
    return funcs_dic


# print(funcs_dic)

def tests(*args):
    # print("args", args)
    if len(args) != 0:
        tfunc = args[0]
        if callable(tfunc):
            funcs_dic = get_funcs_dict()
            if tfunc.__name__ in funcs_dic:
                res = funcs_dic.get(tfunc.__name__)(tfunc)  # dont delete. It where tests are executed
                res = True
            else:
                if debug_mode != "off":
                    print("caution: " + tfunc.__name__ + " is not covered by tests yet")
                res = False
        else:
            res = False
            if debug_mode == "verbose":
                print(
                    "wrong use of the self-diagnostics functionality detected: somithing that is not a function passed as an argument to tests()")

    else:
        res = False
        if debug_mode == "verbose":
            print(
                "wrong use of the self-diagnostics functionality detected: the tests function is used without arguments")
    return res


tests(get_commons4tests)
tests(tests)  # checking if the self-diag functionality itself is working properly
