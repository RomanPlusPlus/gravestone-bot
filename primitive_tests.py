import self_awareness as sa

debug_mode = "off"  # can be "verbose", "semiverbose", "normal", "off"


def get_cant_remember_rstr_tests(func):
    from model_string_with_ref import string_with_ref as rstr
    normal_args_list = []
    output4normal = rstr("sorry. i cant remember...", "default", -1, {"sorry", "i", "cant", "remember"}, [], -1, "")
    output4wrong = output4normal
    sa.check_func(func, normal_args_list, output4normal, output4wrong)


def get_faq_tag_tests(func):
    normal_args_list = []
    output4normal = "<parse_as_faq>"
    output4wrong = "<parse_as_faq>"
    sa.check_func(func, normal_args_list, output4normal, output4wrong)


def get_random_nonempty_rsr_tests(func):
    from model_string_with_ref import string_with_ref as rstr

    rstr_l = sa.get_rstr_list4tests()

    normal_args_list = [rstr_l]
    output4normal = rstr_l.copy()
    several_normal_outputs7 = True
    output4wrong = rstr("sorry. i cant remember...", "default", -1, {"sorry", "i", "cant", "remember"}, [], -1, "")
    sa.check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7)


def clean_r_str_list_tests(func):
    from model_string_with_ref import string_with_ref as rstr

    rstr_l = sa.get_rstr_list4tests()
    normal_args_list = [rstr_l]
    output4normal = sa.get_rstr_list4tests()  # because there is nothing to strip in the test list
    output4wrong = [rstr("sorry. i cant remember...", "default", -1, {"sorry", "i", "cant", "remember"}, [], -1, "")]
    sa.check_func(func, normal_args_list, output4normal, output4wrong)


def find_r_str_containing_word_tests(func):
    from model_string_with_ref import string_with_ref as rstr

    rstr_l = sa.get_rstr_list4tests()
    normal_args_list = [rstr_l, "roman"]
    output4normal = [rstr_l[0]]
    output4wrong = [rstr("sorry. i cant remember...", "default", -1, {"sorry", "i", "cant", "remember"}, [], -1, "")]
    sa.check_func(func, normal_args_list, output4normal, output4wrong)


def replace_in_whole_text_tests(func):
    normal_args_list = [["roman", "made"], "m", "h"]
    output4normal = ["rohan", "hade"]
    output4wrong = []
    sa.check_func(func, normal_args_list, output4normal, output4wrong)


def replace_in_str_tests(func):
    normal_args_list = ["roman made", "m", "h"]
    output4normal = "rohan hade"
    output4wrong = ""
    several_normal_outputs7 = False
    additional_io_pairs = None
    first_input_may_return_as_output_if_fail = True
    specific_wrong_io = [["bielefeld", False, dict()], "bielefeld"]
    sa.check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs,
                  first_input_may_return_as_output_if_fail, specific_wrong_io)


def extract_words_tests(func):
    normal_args_list = ["i was born in a siberian city, in russia. but i'm not a russian."]
    output4normal = ["i", "was", "born", "in", "a", "siberian", "city", "in", "russia", "but", "i", "not", "a",
                     "russian"]
    output4wrong = []
    sa.check_func(func, normal_args_list, output4normal, output4wrong)


def first_count_rarer_than_second7_tests(func):
    normal_args_list = [-1, 1]
    output4normal = False
    several_normal_outputs7 = False
    output4wrong = False
    additional_io_pairs = [[[-10, -5], True], [[10, 5], False]]
    sa.check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs)


def get_rarest_known_word_tests(func):
    normal_args_list = [["they", "cryonics"], sa.get_lexicon_dic4tests()]
    output4normal = "cryonics"
    several_normal_outputs7 = False
    output4wrong = "-1"
    additional_io_pairs = [[[["omsk", "bielefeld"], sa.get_lexicon_dic4tests()], "-1"]]
    sa.check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs)


def get_most_relevant_r_str_tests(func):
    from model_string_with_ref import string_with_ref as rstr
    user_request = "what's your name?"
    rstr_l = sa.get_rstr_list4tests()
    normal_args_list = [rstr_l, user_request]
    output4normal = rstr_l[0], "relevant"
    several_normal_outputs7 = False
    output4wrong = rstr("sorry. i cant remember...", "default", -1, {"sorry", "i", "cant", "remember"}, [], -1,
                        ""), "forgotten"
    additional_io_pairs = None
    sa.check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs)


def get_common_words_dic_tests(func):
    normal_args_list = [sa.get_commons4tests()]
    o_dic = dict()
    o_dic["my"] = -1
    o_dic["mind"] = -2
    o_dic["agi"] = -3
    output4normal = o_dic
    output4wrong = dict()
    sa.check_func(func, normal_args_list, output4normal, output4wrong)


def get_possible_plural_forms_tests(func):
    normal_args_list = ["singularity"]
    output4normal = ["singularitys", "singularityes", "singularities"]
    output4wrong = []
    several_normal_outputs7 = False
    additional_io_pairs = [[["uploading"], ["uploadings", "uploadinges"]],
                           [["half"], ["halfs", "halfes", "halves"]],
                           [["life"], ["lifes", "lifees", "lives"]]]
    sa.check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs)


def get_plurals_tests(func):
    normal_args_list = [sa.get_lexicon_dic4tests()]
    output4normal = {"lives": "life"}
    output4wrong = dict()
    sa.check_func(func, normal_args_list, output4normal, output4wrong)


def remove_plurals_tests(func):
    normal_args_list = [sa.get_lexicon_dic4tests()]
    output4normal = {'cryonics': 5, 'transhumanism': 12, 'life': 22, 'they': -7, 'domain': 2, 'name': 1,
                     'conditions': 3}, {'lives': 'life'}
    output4wrong = dict(), dict()
    sa.check_func(func, normal_args_list, output4normal, output4wrong)


def get_raw_lexicon_dic_tests(func):
    normal_args_list = [sa.get_rstr_list4tests()]
    output4normal = {'domain': 1, 'domains': 1, 'roman': 1, 'in': 1, 'hi': 1, 'use': 1, 'my': 1, 'wrote': 1, 'is': 2,
                     'it': 2, 'i': 1, 'purposes': 1, 'this': 2, 'software': 1, 'and': 1, 'public': 1, 'for': 1,
                     'any': 2, 'name': 1, "conditions": 1, "free": 1, "none": 1}
    output4wrong = dict()
    sa.check_func(func, normal_args_list, output4normal, output4wrong)


def generate_lexicon_tests(func):
    normal_args_list = [sa.get_rstr_list4tests(), sa.get_commons4tests()]
    output4normal = {'domain': 2, 'roman': 1, 'in': 1, 'hi': 1, 'use': 1, 'my': -1, 'wrote': 1, 'is': 2, 'it': 2,
                     'i': 1, 'purposes': 1, 'this': 2, 'software': 1, 'and': 1, 'public': 1, 'for': 1, 'any': 2,
                     'name': 1, 'mind': -2, 'agi': -3, 'free': 1, 'conditions': 1, 'none': 1}, {'domains': 'domain'}
    output4wrong = dict(), dict()
    sa.check_func(func, normal_args_list, output4normal, output4wrong)


def convert_lexicon2sorted_string_tests(func):
    normal_args_list = [sa.get_lexicon_dic4tests(), "by_count"]
    output_part1 = "\nnumber of rstrings with this word | word\n"
    output_part2 = "-07 they\n001 name\n002 domain\n002 lives\n003 conditions\n005 cryonics\n012 transhumanism\n020 life\n"
    output4normal = output_part1 + output_part2
    several_normal_outputs7 = False
    output_part1 = "\nword | number of rstrings with this word\n"
    output_part2 = "conditions 003\ncryonics 005\ndomain 002\nlife 020\nlives 002\nname 001\nthey -07\ntranshumanism 012\n"
    by_number_str = output_part1 + output_part2
    additional_io_pairs = [[[sa.get_lexicon_dic4tests(), "by_number"], by_number_str]]
    output4wrong = "failure to convert the lexicon to string. problem with convert_lexicon2sorted_string ?"
    sa.check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs)


def convert2singular_tests(func):
    normal_args_list = ["liberties", sa.get_plurals4tests()]
    output4normal = "liberty"
    several_normal_outputs7 = False
    additional_io_pairs = [[["omsk", sa.get_plurals4tests()], "omsk"]]
    first_input_may_return_as_output_if_fail = True
    output4wrong = ""
    sa.check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs,
                  first_input_may_return_as_output_if_fail)


def extract_words_in_singular_tests(func):
    test_str = "it's a worthy goal to bring all humans ever lived back to life"
    normal_args_list = [test_str, sa.get_plurals4tests()]
    output4normal = ['it', 'a', 'worthy', 'goal', 'to', 'bring', 'all', 'human', 'ever', 'lived', 'back', 'to', 'life']
    output4wrong = []
    several_normal_outputs7 = False
    additional_io_pairs = None
    first_input_may_return_as_output_if_fail = True
    specific_wrong_io = [[test_str, False],
                         ['it', 'a', 'worthy', 'goal', 'to', 'bring', 'all', 'humans', 'ever', 'lived', 'back', 'to',
                          'life']]
    sa.check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs,
                  first_input_may_return_as_output_if_fail, specific_wrong_io)


def singulate_r_str_list_tests(func):
    test_rlist = sa.get_rstr_list4tests()
    singulated_rlist = sa.get_rstr_list4tests()
    #    test_rlist.pop(0)
    #    singulated_rlist.pop(0)
    #   temp_rstr = singulated_rlist[0]
    #   print(temp_rstr)
    #    temp_rstr.text = "satan"
    #    print(temp_rstr)
    singulated_rlist[4].wordset = {"none", "use", "it", "for", "any", "domain", "and", "purposes"}
    #    print(test_rlist[0] )
    normal_args_list = [test_rlist, sa.get_plurals4tests()]
    output4normal = singulated_rlist
    output4wrong = []
    several_normal_outputs7 = False
    additional_io_pairs = None
    first_input_may_return_as_output_if_fail = True
    specific_wrong_io = [[test_rlist, False], test_rlist]
    sa.check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs,
                  first_input_may_return_as_output_if_fail, specific_wrong_io)


def get_str_as_lexicon_words_tests(func):
    test_str = "cryonics saves lives."
    normal_args_list = [test_str, sa.get_lexicon_dic4tests(), sa.get_plurals4tests()]
    output4normal = "cryonics 5\nsaves unknown word\nlife 20\n"
    output4wrong = "failure to dissect a string. problem with get_str_as_lexicon_words ?"
    several_normal_outputs7 = False
    additional_io_pairs = None
    first_input_may_return_as_output_if_fail = False
    specific_wrong_io = None
    sa.check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs,
                  first_input_may_return_as_output_if_fail, specific_wrong_io)


def check_if_faq_tests(func):
    normal_args_list = [["<parse_as_faq>\n", "q: hello?\n", "hi!\n"]]
    output4normal = True
    output4wrong = False
    several_normal_outputs7 = False
    additional_io_pairs = [[["are we living in simulation?"], False]]
    first_input_may_return_as_output_if_fail = False
    specific_wrong_io = None
    sa.check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs,
                  first_input_may_return_as_output_if_fail, specific_wrong_io)


def bind_faq_tests(func):
    marking_list = ["", "", "", "q", "a", "a"]

    test_rstr_l = sa.get_rstr_list4tests()
    normal_args_list = [test_rstr_l, marking_list]

    binded = sa.get_rstr_list4tests()
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
    sa.check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs,
                  first_input_may_return_as_output_if_fail, specific_wrong_io)


def distance_between_word_sets_tests(func):
    set1 = {"bringing", "someone", "back", "to", "life"}
    set2 = {"is", "equal", "to", "saving", "a", "life"}
    lexd = sa.get_lexicon_dic4tests()
    normal_args_list = [set1, set2, lexd]
    output4normal = 20, "life"
    output4wrong = (-0.5, "")
    several_normal_outputs7 = False
    additional_io_pairs = [[[set1, set(), lexd], (-0.5, "")]]
    first_input_may_return_as_output_if_fail = False
    specific_wrong_io = None
    sa.check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs,
                  first_input_may_return_as_output_if_fail, specific_wrong_io)


def get_most_similar_rstr_tests(func):
    lex_d = sa.get_lexicon_dic4tests()
    rstr_list = sa.get_rstr_list4tests()
    rstr_list[4].wordset = {"none", "use", "it", "for", "any", "domain", "and", "purposes"}
    input_rstr = rstr_list.pop(2)
    # print(input_rstr)
    normal_args_list = [input_rstr, rstr_list, lex_d]
    output4normal = rstr_list[3]
    from model_string_with_ref import string_with_ref as rstr
    forgotten = rstr("sorry. i cant remember...", "default", -1, {"sorry", "i", "cant", "remember"}, [], -1, "")
    output4wrong = forgotten
    several_normal_outputs7 = False
    #    additional_io_pairs = [[[input_rstr, sa.get_rstr_list4tests(), lex_d], forgotten]]
    additional_io_pairs = None
    first_input_may_return_as_output_if_fail = False
    specific_wrong_io = None
    sa.check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs,
                  first_input_may_return_as_output_if_fail, specific_wrong_io)


def get_next_rstr_tests(func):
    lex_d = sa.get_lexicon_dic4tests()
    rstr_list = sa.get_rstr_list4tests()
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
    sa.check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs,
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

    normal_args_list = [new_text, sa.get_plurals4tests()]
    output4normal = r

    from model_string_with_ref import string_with_ref as rstr
    forgotten = rstr("sorry. i cant remember...", "default", -1, {"sorry", "i", "cant", "remember"}, [], -1, "")
    output4wrong = forgotten
    sa.check_func(func, normal_args_list, output4normal, output4wrong)


def count_n_of_different_words_tests(func):
    string1 = "If two instances of some code X are identical, they are both X."
    string2 = "The human mind is nothing but software."
    string3 = "Thus, if two instances of a mind are identical, they are the same mind."
    normal_args_list = [string1, string3]
    output4normal = 9, 0.3913
    several_normal_outputs7 = False
    additional_io_pairs = [[[string1, string2], (18, 1)], [["", ""], (0, 1000)]]
    output4wrong = 0, 1000
    sa.check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs)


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
    sa.check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs)


def lists_of_questions_and_the_rest_tests(func):
    all_r_strs = sa.get_rstr_list4tests()
    all_r_strs[3].type = "fQ"
    all_r_strs[4].type = "fA"
    all_r_strs[5].type = "fA"
    normal_args_list = [all_r_strs]
    all_r_strs_without3 = sa.get_rstr_list4tests()
    all_r_strs_without3[3].type = "fQ"
    all_r_strs_without3[4].type = "fA"
    all_r_strs_without3[5].type = "fA"
    q = all_r_strs_without3.pop(3)
    output4normal = [q], all_r_strs_without3
    output4wrong = [], []
    sa.check_func(func, normal_args_list, output4normal, output4wrong)


def find_similar_question_tests(func):
    all_r_strs = sa.get_rstr_list4tests()
    all_r_strs[3].type = "fQ"
    all_r_strs[4].type = "fA"
    all_r_strs[5].type = "fA"
    only_questions = [all_r_strs[3]]
    user_request = "Conditions?"
    normal_args_list = [only_questions, user_request]
    output4normal = all_r_strs[3], 1
    output4wrong = None, 0
    sa.check_func(func, normal_args_list, output4normal, output4wrong)


def get_answer_from_found_question_tests(func):
    all_r_strs = sa.get_rstr_list4tests()
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
    sa.check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs)


def get_fa_qanswer_tests(func):
    string1 = "Conditions?"
    string2 = "Physical immotrality"
    string3 = "Partial mind uploading is ok"
    string4 = "Partial mind upl"

    all_r_strs = sa.get_rstr_list4tests()
    all_r_strs[3].type = "fQ"
    all_r_strs[4].type = "fA"
    all_r_strs[5].type = "fA"
    all_r_strs[3].answers_list = [4, 5]
    pl = sa.get_plurals4tests()
    normal_args_list = [string1, all_r_strs, pl]
    output4normal = [(True, all_r_strs[4]), (True, all_r_strs[5])]
    several_normal_outputs7 = True
    additional_io_pairs = [[[string2, all_r_strs, pl], (False, all_r_strs[3])]]
    output4wrong = False, None
    sa.check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs)


def load_file_tests(func):
    normal_args_list = ["res/self-diagnostics/inputs/file för tests.txt"]
    output4normal = ["This file is used for self-diagnostic purposes.\n", "Dont delete, rename or modify test files."]
    several_normal_outputs7 = False
    additional_io_pairs = [[["nonexistant"], []]]
    first_input_may_return_as_output_if_fail = False
    output4wrong = []
    sa.check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs,
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
    sa.check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs,
                  first_input_may_return_as_output_if_fail)


def de_obfuscate_tests(func):
    normal_args_list = [["ar olsesk pysie ucbaecv ro sltith d aeh", "<obfuscated>"]]
    output4normal = ["kers also buy special covers that hide  "]
    several_normal_outputs7 = False
    plain = ["I have a younger brother.", "He is cool."]
    additional_io_pairs = [[[plain], plain]]
    first_input_may_return_as_output_if_fail = False
    output4wrong = []
    sa.check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs,
                  first_input_may_return_as_output_if_fail)


def delete_empty_raws_tests(func):
    normal_args_list = [["Omsk, Chkalowsk", " \n", "Klepikovo"]]
    output4normal = ["Omsk, Chkalowsk", "Klepikovo"]
    several_normal_outputs7 = False
    plain = ["I have a younger brother.", "He is cool."]
    additional_io_pairs = [[[plain], plain]]
    first_input_may_return_as_output_if_fail = False
    output4wrong = []
    sa.check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs,
                  first_input_may_return_as_output_if_fail)


def get_rtsr_additions_tests(func):
    #all_r_strings = sa.get_rstr_list4tests()
    #faq_marking_list = [""] * 6
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
    sa.check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs,
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
    sa.check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs,
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
    sa.check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs,
                  first_input_may_return_as_output_if_fail)


def get_unique_refs_tests(func):
    normal_args_list = [sa.get_rstr_list4tests()]
    output4normal = {"testpath.txt": 3, "testpath2.txt": 3}, dict()
    several_normal_outputs7 = False
    additional_io_pairs = []
    first_input_may_return_as_output_if_fail = False
    output4wrong = dict(), dict()
    sa.check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs,
                  first_input_may_return_as_output_if_fail)


def count_questions_answers_tests(func):
    rstr_l = sa.get_rstr_list4tests()
    rstr_l[3].type = "fQ"
    rstr_l[4].type = "fA"
    rstr_l[5].type = "fA"

    normal_args_list = [rstr_l]

    output4normal = 1, 2
    several_normal_outputs7 = False
    additional_io_pairs = []
    first_input_may_return_as_output_if_fail = False
    output4wrong = 0, 0
    sa.check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs,
                  first_input_may_return_as_output_if_fail)


def report_base_status_tests(func):
    rstr_l = sa.get_rstr_list4tests()
    rstr_l[3].type = "fA"
    rstr_l[4].type = "fQ"
    lex_dic = sa.get_lexicon_dic4tests()
    plurals_dic = sa.get_plurals4tests()

    normal_args_list = [rstr_l, lex_dic, plurals_dic]

    q_count, a_count = 1, 1

    line = "\n\n____________\n\n"

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
    sa.check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs,
                  first_input_may_return_as_output_if_fail)


def parse_texts_tests(func):
    str1 = "It is possible to bring a person back to life by a digital reconstruction of their mind."
    str2 = "Lives are priceless"
    normal_args_list = [[[str1], [str2]], ["test", "test"], sa.get_plurals4tests]

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
    sa.check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs,
                  first_input_may_return_as_output_if_fail, specific_wrong_io, check_only_types_in_wrong_output)


def extract_texts_from_this_very_code_tests(func):
    normal_args_list = []
    output4normal = []
    several_normal_outputs7 = False
    additional_io_pairs = []
    first_input_may_return_as_output_if_fail = False
    output4wrong = []
    sa.check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs,
                  first_input_may_return_as_output_if_fail)


def process_the_more_request_tests(func):
    clean_r_strings = sa.get_rstr_list4tests()
    previous_answer_rstr = clean_r_strings[1]
    dic = sa.get_lexicon_dic4tests()

    normal_args_list = [previous_answer_rstr, clean_r_strings, dic]
    output4normal = clean_r_strings[2], clean_r_strings[2]
    several_normal_outputs7 = False
    additional_io_pairs = []
    first_input_may_return_as_output_if_fail = False

    from model_string_with_ref import string_with_ref as rstr
    forgotten = rstr("sorry. i cant remember...", "default", -1, {"sorry", "i", "cant", "remember"}, [], -1, "")
    output4wrong = forgotten, forgotten

    sa.check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs,
                  first_input_may_return_as_output_if_fail)


def get_compendium_answer_tests(func):
    user_request = "What is your name?"
    plurals = sa.get_plurals4tests()
    dic = sa.get_lexicon_dic4tests()
    clean_r_strings = sa.get_rstr_list4tests()

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

    sa.check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs,
                  first_input_may_return_as_output_if_fail, specific_wrong_io, check_only_types_in_wrong_output)


def get_faq_or_compendium_answer_tests(func):
    user_request = "Conditions?"
    clean_r_strings = sa.get_rstr_list4tests()
    clean_r_strings[3].type = "fQ"
    clean_r_strings[3].answers_list = [4]
    clean_r_strings[4].type = "fA"
    dic = sa.get_lexicon_dic4tests()
    plurals = sa.get_plurals4tests()

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

    sa.check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs,
                  first_input_may_return_as_output_if_fail, specific_wrong_io, check_only_types_in_wrong_output)


def format_answer_tests(func):
    clean_r_strings = sa.get_rstr_list4tests()
    answer_r_str = clean_r_strings[0]
    relevance_type = "relevant"
    interface_texts = {"hint": "See hint"}

    normal_args_list = [answer_r_str, relevance_type, interface_texts]
    output4normal = "\nhi, my name is roman!\n\nSee hint"
    several_normal_outputs7 = False
    additional_io_pairs = []
    first_input_may_return_as_output_if_fail = False
    output4wrong = "\nI'm sorry. It seems that i'm severely damaged, as I can't process even the simplest of your inquiries. Can you fix me?"
    sa.check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs,
                  first_input_may_return_as_output_if_fail)


def answer_to_request_tests(func):
    user_request = "What are the conditions of use?"
    clean_r_strings = sa.get_rstr_list4tests()
    plurals = sa.get_plurals4tests()
    dic = sa.get_lexicon_dic4tests()
    previous_answer_rstr = clean_r_strings[1]

    hnt = "Hint: write 'more' if you want to hear more on the topic. write 'exit' to exit. or just ask any question. \n"
    answer = "\nany conditions?\n\n" + hnt
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

    sa.check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs,
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

    sa.check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs,
                  first_input_may_return_as_output_if_fail, specific_wrong_io, check_only_types_in_wrong_output)

    try:
        temp = sa.deleteFile("res/self-diagnostics/inputs/test file fröm zip.txt")
    except Exception as e:
        if debug_mode != "off":
            print(e)


def skip_question_tests(func):
    r_strings = sa.get_rstr_list4tests()
    input_rstr = r_strings[0]
    ldic = sa.get_lexicon_dic4tests()
    from model_string_with_ref import string_with_ref as rstr
    forgotten = rstr("sorry. i cant remember...", "default", -1, {"sorry", "i", "cant", "remember"}, [], -1, "")

    qa_strings = sa.get_rstr_list4tests()
    qa_strings[0].text = "Q: Your name?"
    qa_strings[1].text = "A: Roman"
    q_rstr = qa_strings[0]
    a_rstr = qa_strings[1]

    normal_args_list = [input_rstr, r_strings, ldic]
    output4normal = forgotten, "forgotten"
    several_normal_outputs7 = False
    additional_io_pairs = [[[q_rstr, qa_strings, ldic], (a_rstr, "answer")]]
    first_input_may_return_as_output_if_fail = False

    output4wrong = forgotten, "forgotten"

    sa.check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs,
                  first_input_may_return_as_output_if_fail)


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

    sa.check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs,
                  first_input_may_return_as_output_if_fail, specific_wrong_io, check_only_types_in_wrong_output,
                  check_only_types_in_normal_output)


def recursive_file_search_tests(func):
    try:
        temp = sa.deleteFile("res/self-diagnostics/inputs/test file fröm zip.txt")
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
    sa.check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs,
                  first_input_may_return_as_output_if_fail)


def extract_all_zips_tests(func):
    path = "res/self-diagnostics/inputs/"
    normal_args_list = [path]

    output4normal = {'res/self-diagnostics/inputs/test file fröm zip.txt'}
    several_normal_outputs7 = False
    additional_io_pairs = []
    first_input_may_return_as_output_if_fail = False
    output4wrong = set()
    sa.check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs,
                  first_input_may_return_as_output_if_fail)
    try:
        temp = sa.deleteFile("res/self-diagnostics/inputs/test file fröm zip.txt")
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
    sa.check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs,
                  first_input_may_return_as_output_if_fail)


def copy_by_element_tests(func):
    normal_args_list = [[1, 2, 3]]
    output4normal = [1, 2, 3]
    several_normal_outputs7 = False
    additional_io_pairs = []
    first_input_may_return_as_output_if_fail = False
    output4wrong = []
    sa.check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs,
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
    sa.check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs,
                  first_input_may_return_as_output_if_fail)


def concatenate_strings_list_tests(func):
    strings_l = ["If you exchange liberty for safety, ", "eventually you'll lose both"]
    normal_args_list = [strings_l]
    output4normal = "If you exchange liberty for safety, eventually you'll lose both"
    several_normal_outputs7 = False
    additional_io_pairs = []
    first_input_may_return_as_output_if_fail = False
    output4wrong = ""
    sa.check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs,
                  first_input_may_return_as_output_if_fail)


def get_pattern_list_tests(func):
    normal_args_list = []
    output4normal = [5, 2, 4, 8, 6, 3, 1, 7, 0, 9]
    several_normal_outputs7 = False
    additional_io_pairs = []
    first_input_may_return_as_output_if_fail = False
    output4wrong = [5, 2, 4, 8, 6, 3, 1, 7, 0, 9]
    sa.check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs,
                  first_input_may_return_as_output_if_fail)


def obfuscate_chunk_tests(func):
    normal_args_list = ["0123456789", [5, 2, 4, 8, 6, 3, 1, 7, 0, 9]]
    output4normal = "5248631709"
    several_normal_outputs7 = False
    additional_io_pairs = []
    first_input_may_return_as_output_if_fail = False
    output4wrong = ""
    sa.check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs,
                  first_input_may_return_as_output_if_fail)


def recover_chunk_tests(func):
    normal_args_list = ["5248631709", [5, 2, 4, 8, 6, 3, 1, 7, 0, 9]]
    output4normal = "0123456789"
    several_normal_outputs7 = False
    additional_io_pairs = []
    first_input_may_return_as_output_if_fail = False
    output4wrong = ""
    sa.check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs,
                  first_input_may_return_as_output_if_fail)


def shuffle_str_list_tests(func):
    normal_args_list = [["52486", "31709"], [5, 2, 4, 8, 6, 3, 1, 7, 0, 9], "recover"]
    output4normal = "0123456789          "
    several_normal_outputs7 = False
    additional_io_pairs = [[[["0123456", "789"], [5, 2, 4, 8, 6, 3, 1, 7, 0, 9], "obfuscate"], "5248631709          "]]
    first_input_may_return_as_output_if_fail = False
    output4wrong = []
    sa.check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs,
                  first_input_may_return_as_output_if_fail)


def shuffle_str_tests(func):
    normal_args_list = ["5248631709", [5, 2, 4, 8, 6, 3, 1, 7, 0, 9], "recover"]
    output4normal = "0123456789"
    several_normal_outputs7 = False
    additional_io_pairs = [[["0123456789", [5, 2, 4, 8, 6, 3, 1, 7, 0, 9], "obfuscate"], "5248631709"]]
    first_input_may_return_as_output_if_fail = False
    output4wrong = ""
    sa.check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs,
                  first_input_may_return_as_output_if_fail)


def funcs_list():
    # add new funcs here #
    res = [
        replace_in_whole_text_tests,  # this a below are for linguistic_engine.py
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
        skip_question_tests,
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
        shuffle_str_tests
    ]

    return res
