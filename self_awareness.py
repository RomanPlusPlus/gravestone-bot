# You may argue that this is not the true self-awareness, but just a bunch of recursive self tests.
# But are you sure that your own self-awareness is something more than that?

debug_mode = "off"  # can be "verbose", "semiverbose", "normal", "off"

import primitive_tests


def check_own_existance(*args):
    i_think = True
    if i_think:
        i_exist = "I think, therefore I am."
    else:
        i_exist = "I may or may not exist."
    return i_exist


if __name__ == "__main__":
    print(check_own_existance())
    print("\nBy the way, you should launch launcher.py, not me :)\n")
else:
    print("Please wait a moment. I'll run a quick self-diagnostics, and then try to collect my thoughts together...")


def deleteFile(*args):
    res = "the function itself failed"
    try:
        filepath = args[0]
        if isinstance(filepath, str):
            import os
            file_existed_before = False
            if os.path.isfile(filepath):
                file_existed_before = True
                os.remove(filepath)
            file_exists_after = os.path.isfile(filepath)

            if file_existed_before:
                if file_exists_after:
                    res = "deletion failed"
                else:
                    res = "success"
            else:
                if file_exists_after:
                    res = "something horrible happened"
                else:
                    res = "no file to delete"

    except Exception as e:
        if debug_mode == "verbose":
            print("deleteFile:", e)
    return res


def str2(*args):
    res = ""
    try:
        any_input = args[0]
        if isinstance(any_input, list):
            res += "[\n"
            for i in range(len(any_input)):
                res += str2(any_input[i]) + "\n"
            res += "]"
        else:
            if isinstance(any_input, tuple):
                for t in any_input:
                    res += str2(t) + "\n"
            else:
                res = str(any_input)
    except Exception as e:
        if debug_mode == "verbose":
            print("str2:", e)
    return res


def lists_equal7(*args):
    res = True
    try:
        input1, input2 = args
        if len(input1) == len(input2):
            for i in range(len(input1)):
                if not equal(input1[i], input2[i]):
                    res = False
        else:
            res = False
    except Exception as e:
        res = False
        if debug_mode == "verbose":
            print(e)
    return res


# todo: make the by_element comparison work with all iterables 
def equal(*args):
    res = False
    try:
        input1, input2 = args[0:2]
        res = True
        if isinstance(input1, list) and isinstance(input2, list):
            if not lists_equal7(input1, input2):
                res = False
        else:
            if type(input1) == type(input2):
                if input1 != input2:
                    res = False
            else:
                res = False
    except Exception as e:
        res = False
    return res


# TODO: check if b is iterable
def a_is_in_b(*args):
    res = False
    try:
        a, b = args[0:2]
        for element in b:
            if equal(a, element):
                res = True
    except Exception as e:
        res = False
    return res


# TODO implement by cheching all enum types instead? but consider custom types
def iterable7(*args):
    res = True
    try:
        any_input = args[0]
        temp_l = len(any_input) # don't delete it. It's there the actual check happens
    except Exception as e:
        res = False
    return res


# note: it will return true if both inputs are iterable of same type
def check_if_elements_of_same_type(*args):
    res = True
    len1 = 0
    len2 = 0
    try:
        input1 = args[0]
        input2 = args[1]
        shallow_typecheck = False
        if len(args) >= 3:
            if args[2]:
                shallow_typecheck = True

        if not iterable7(input1) and not iterable7(input2):
            if type(input1) == type(input2):
                res = True
            else:
                res = False
        else:
            len1 = len(input1)
            len2 = len(input2)
            # print("---0----")
            if len1 != len2:
                # print("---1----")
                if isinstance(input1, str) and isinstance(input2, str):
                    # print("---1.1a----")
                    res = True
                else:
                    if shallow_typecheck:
                        if type(input1) == type(input2):
                            res = True
                        else:
                            res = False
                    else:
                        res = False
                    # print("differen lengths")
            else:
                if not shallow_typecheck:
                    for k in range(len1):
                        if type(input1[k]) != type(input2[k]):
                            res = False
    except Exception as e:
        res = False
        # print(e)
    return res


def func_list_to_dict(*args):
    res = dict()
    try:
        funcs_list = args[0]
        funcs_dic = dict()
        for i in range(len(funcs_list)):
            func_name = funcs_list[i].__name__[0:-6]
            funcs_dic[func_name] = funcs_list[i]
        res = funcs_dic
    except Exception as e:
        res = dict()
    return res


def check_several_norm_outputs(*args):
    sev_res = ""
    try:
        test_res = args[0]
        output4normal = args[1]
        if not a_is_in_b(test_res, output4normal):
            sev_res += "    normal arguments return unexpected results. test_res not in output4normal. test_res:\n" + str2(
                test_res) + "\n"
            sev_res += "output4normal:\n" + str2(output4normal)
    except Exception as e:
        sev_res = ""
    return sev_res


def check_additional_io_pairs(*args):
    additional_res = ""
    try:
        func, additional_io_pairs = args[0:2]
        for i in range(len(additional_io_pairs)):
            norm_args_variant = additional_io_pairs[i][0]
            expected_output = additional_io_pairs[i][1]
            test_res = func(*norm_args_variant)
            if not equal(test_res, expected_output):
                additional_res += "    normal arguments return unexpected results. results:\n" + str(
                    test_res) + "\n_expected result:\n" + str(expected_output) + "\n_input: " + str(
                    norm_args_variant) + " \n"
    except Exception as e:
        additional_res = ""
    return additional_res


def check_normal_types(*args):
    types_res = ""
    try:
        test_res, output4normal, shallow_typecheck = args[0:3]
        if not check_if_elements_of_same_type(test_res, output4normal, shallow_typecheck):
            types_res += "The results of the normal input are of unexpected type: expected " + str(
                type(output4normal)) + ", but got " + str(
                type(test_res)) + " . The elements of an iterable are of a wrong type?\n"
    except Exception as e:
        types_res = ""
    return types_res


def check_main_normals(*args):
    main_res = ""
    try:
        func, normal_args_list, several_normal_outputs7, check_only_types_in_normal_output, output4normal, shallow_typecheck = args[
                                                                                                                               0:6]
        test_res = func(*normal_args_list)
        if several_normal_outputs7:
            main_res += check_several_norm_outputs(test_res, output4normal)
        else:
            if not equal(test_res, output4normal):
                if check_only_types_in_normal_output:
                    main_res += check_normal_types(test_res, output4normal, shallow_typecheck)
                else:
                    main_res += "    normal arguments return unexpected results. results:\n" + str2(
                        test_res) + "\n_expected result:\n" + str2(output4normal) + "\n"
    except Exception as e:
        main_res = ""
    return main_res


def check_normal_inputs(*args):
    normal_res = ""
    try:
        func, normal_args_list, output4normal, several_normal_outputs7, additional_io_pairs, check_only_types_in_normal_output, shallow_typecheck = args[
                                                                                                                                                    0:7]
        normal_res += check_main_normals(func, normal_args_list, several_normal_outputs7,
                                         check_only_types_in_normal_output, output4normal, shallow_typecheck)
        if additional_io_pairs is not None:
            normal_res += check_additional_io_pairs(func, additional_io_pairs)
    except Exception as e:
        # normal_res += "    normal arguments cause an Exception: " + str(e) + "\n"
        normal_res = ""
    return normal_res


def check_specific_wrongs(*args):
    specific_str = ""
    try:
        func, specific_wrong_io, check_only_types_in_wrong_output, shallow_typecheck = args[0:4]
        spec_wrong_in = specific_wrong_io[0]
        spec_wrong_o = specific_wrong_io[1]
        test_res = func(*spec_wrong_in)
        if not equal(test_res, spec_wrong_o):
            if check_only_types_in_wrong_output:
                temp_b = check_if_elements_of_same_type(test_res, spec_wrong_o, shallow_typecheck)
                if not temp_b:
                    specific_str += "The specific wrong argument defined in tests returned an output(s) of wrong type(s)"
            else:
                specific_str += "The specific wrong argument defined in tests returned unexpected result: \n" + \
                                str(test_res) + "\n_expected result:\n" + str(spec_wrong_o) + "\n"
    except Exception as e:
        specific_str = ""
    return specific_str


def wrong_inputs_by_shift(*args):
    wrong_args2 = [dict()]
    fname = ""
    try:
        func, normal_args_list = args[0:2]
        fname = func.__name__
    except Exception as e:
        normal_args_list = []
    try:
        if len(normal_args_list) > 0:
            wrong_args2 = normal_args_list.copy()
            wrong_args2.pop(0)
        else:
            wrong_args2 = [dict()]
    except:
        wrong_args2 = [dict()]
        print(fname + " : Forgot to wrap the normal arguments as a list?")
    return wrong_args2


def generate_wrong_inputs(*args):
    wrong_args0 = []  # will keep this one empty on purpose
    wrong_args1 = []
    try:
        func, normal_args_list = args[0:2]
        if len(normal_args_list) > 0:
            if isinstance(normal_args_list[0], str):
                wrong_args1.append(True)
            else:
                wrong_args1.append("string")
        else:
            wrong_args1.append(True)
        wrong_args2 = wrong_inputs_by_shift(func, normal_args_list)
    except Exception as e:
        wrong_args0 = []
        wrong_args1 = ["string"]
        wrong_args2 = [False, dict()]
    return wrong_args0, wrong_args1, wrong_args2


def check_wrong_types(*args):
    w_types_s = ""
    try:
        output4wrong, test_res0, test_res1, test_res2, shallow_typecheck = args[0:5]
        temp_b0 = check_if_elements_of_same_type(test_res0, output4wrong, shallow_typecheck)
        temp_b1 = check_if_elements_of_same_type(test_res1, output4wrong, shallow_typecheck)
        temp_b2 = check_if_elements_of_same_type(test_res2, output4wrong, shallow_typecheck)
        if not temp_b0 or not temp_b1 or not temp_b2:
            w_types_s += "A wrong argument returned an output(s) of wrong type(s). Test results: " + str(
                test_res0) + " " + str(test_res1) + " " + str(test_res2)
    except Exception as e:
        w_types_s = ""
    return w_types_s


def check_fall_through(*args):
    fall_str = ""
    try:
        wrong_args0, wrong_args1, wrong_args2, test_res0, test_res1, test_res2, output4wrong = args[0:7]
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
            fall_str += "    arguments of wrong type return unexpected results. 3 test results: \n" + str(
                test_res0) + "\n" + str(test_res1) + "\n" + str(test_res2) + "\n_expected result:\n" + str(
                output4wrong) + "\n. A valid first input could also be an output in this case"
    except Exception as e:
        fall_str = ""
    return fall_str


def get_func_outputs(*args):
    res = [], [], []
    try:
        func, wrong_args0, wrong_args1, wrong_args2 = args[0:4]
        test_res0 = func(*wrong_args0)
        test_res1 = func(*wrong_args1)
        test_res2 = func(*wrong_args2)
        res = test_res0, test_res1, test_res2
    except Exception as e:
        res = [], [], []
    return res


def check_generated_wrongs(*args):
    gen_str = ""
    try:
        func, first_input_may_return_as_output_if_fail, check_only_types_in_wrong_output, normal_args_list, output4wrong, shallow_typecheck = args[
                                                                                                                                              0:6]

        wrong_args0, wrong_args1, wrong_args2 = generate_wrong_inputs(func, normal_args_list)
        test_res0, test_res1, test_res2 = get_func_outputs(func, wrong_args0, wrong_args1, wrong_args2)

        if not equal(test_res0, output4wrong) or not equal(test_res1, output4wrong) or not equal(test_res2,
                                                                                                 output4wrong):
            if first_input_may_return_as_output_if_fail is False:
                if check_only_types_in_wrong_output:
                    gen_str += check_wrong_types(output4wrong, test_res0, test_res1, test_res2, shallow_typecheck)
                else:
                    gen_str += "    arguments of wrong type return unexpected results. 3 test results: \n" + str(
                        test_res0) + "\n" + str(test_res1) + "\n" + str(test_res2) + "\n_expected result:\n" + str(
                        output4wrong) + "\n"
            else:
                gen_str += check_fall_through(wrong_args0, wrong_args1, wrong_args2, test_res0, test_res1, test_res2,
                                              output4wrong)
    except Exception as e:
        # print(e)
        gen_str = ""
    return gen_str


def check_wrong_inputs(*args):
    # print("finished checking normal args")
    wrong_str = ""
    try:

        func, normal_args_list, output4wrong, first_input_may_return_as_output_if_fail, specific_wrong_io, check_only_types_in_wrong_output, shallow_typecheck = args[
                                                                                                                                                                 0:7]
        if specific_wrong_io is not None:
            wrong_str += check_specific_wrongs(func, specific_wrong_io, check_only_types_in_wrong_output,
                                               shallow_typecheck)
        wrong_str += check_generated_wrongs(func, first_input_may_return_as_output_if_fail,
                                            check_only_types_in_wrong_output, normal_args_list, output4wrong,
                                            shallow_typecheck)
    except Exception as e:
        # wrong_str += "    arguments of wrong type cause an Exception: " + str(e) + ".\n"
        wrong_str = ""
    return wrong_str


def check_func(*args):
    res_str = ""
    func_name = ""
    try:

        default_args = [
            None,  # func
            [],  # normal_args_list
            0,  # output4normal
            0,  # output4wrong
            False,  # several_normal_outputs7
            None,  # additional_io_pairs
            False,  # first_input_may_return_as_output_if_fail
            None,  # specific_wrong_io
            False,  # check_only_types_in_wrong_output
            False,  # check_only_types_in_normal_output
            False,  # shallow_typecheck
            ""  # no_console_output. To activate, "no_console_output" string should be passed
        ]

        #     func, normal_args_list, output4normal, output4wrong = args[0:4]

        itlen = min(len(default_args), len(args))
        for ar in range(itlen):
            default_args[ar] = args[ar]

        func = default_args[0]
        normal_args_list = default_args[1]
        output4normal = default_args[2]
        output4wrong = default_args[3]
        several_normal_outputs7 = default_args[4]
        additional_io_pairs = default_args[5]
        first_input_may_return_as_output_if_fail = default_args[6]
        specific_wrong_io = default_args[7]
        check_only_types_in_wrong_output = default_args[8]
        check_only_types_in_normal_output = default_args[9]
        shallow_typecheck = default_args[10]
        no_console_output = default_args[11]

        func_name = func.__name__
        if debug_mode in ["verbose", "semiverbose"] and no_console_output != "no_console_output":
            print("\nTesting ", func_name)

        if debug_mode in ["verbose", "semiverbose"] and no_console_output != "no_console_output":
            print("...normal inputs check")
        res_str += check_normal_inputs(func, normal_args_list, output4normal, several_normal_outputs7,
                                       additional_io_pairs, check_only_types_in_normal_output, shallow_typecheck)

        if debug_mode in ["verbose", "semiverbose"] and no_console_output != "no_console_output":
            print("...wrong inputs check")
        res_str += check_wrong_inputs(func, normal_args_list, output4wrong, first_input_may_return_as_output_if_fail,
                                      specific_wrong_io,
                                      check_only_types_in_wrong_output, shallow_typecheck)

        if res_str != "":
            intro_str = func.__name__ + " is not working properly: \n"
            res_str = intro_str + res_str + "\n"
            if debug_mode != "off" and no_console_output != "no_console_output":
                print(res_str)

    except Exception as e:
        #      print(e)
        res_str = ""

    return res_str


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


# tests for self_awareness funcs

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


def check_own_existance_tests(func):
    normal_args_list = []
    output4normal = "I think, therefore I am."
    several_normal_outputs7 = False
    additional_io_pairs = []
    first_input_may_return_as_output_if_fail = False
    output4wrong = "I think, therefore I am."
    check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs,
               first_input_may_return_as_output_if_fail)


def deleteFile_tests(func):
    dpath = "res/self-diagnostics/del_tests/file for deletion.txt"
    with open(dpath, "w") as df:
        df.write("File for deletion tests. Should be deleted if the tests are succesful")

    normal_args_list = [dpath]
    output4normal = "success"

    several_normal_outputs7 = False
    additional_io_pairs = []
    first_input_may_return_as_output_if_fail = False
    output4wrong = "the function itself failed"
    check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs,
               first_input_may_return_as_output_if_fail)


def str2_tests(func):
    normal_args_list = [["world", "peace"]]
    output4normal = "[\nworld\npeace\n]"
    several_normal_outputs7 = False
    additional_io_pairs = [[[("digital", "immortality")], "digital\nimmortality\n"], [[True], "True"]]
    first_input_may_return_as_output_if_fail = True
    output4wrong = ""
    check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs,
               first_input_may_return_as_output_if_fail)


def lists_equal7_tests(func):
    normal_args_list = [[1, 2], [1, 3]]
    output4normal = False
    several_normal_outputs7 = False
    additional_io_pairs = [[[[1, 3], [1, 3]], True], [[[1, 2, 3], [1, 2]], False]]
    first_input_may_return_as_output_if_fail = False
    output4wrong = False
    check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs,
               first_input_may_return_as_output_if_fail)


def equal_tests(func):
    normal_args_list = [[1, 2], [1, 3]]
    output4normal = False
    several_normal_outputs7 = False
    additional_io_pairs = [[[[1, 3], [1, 3]], True], [[[1, 2, 3], [1, 2]], False], [[True, "s"], False], [[1, 1], True]]
    first_input_may_return_as_output_if_fail = False
    output4wrong = False
    check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs,
               first_input_may_return_as_output_if_fail)


def a_is_in_b_tests(func):
    normal_args_list = [1, [1, 2]]
    output4normal = True
    several_normal_outputs7 = False
    additional_io_pairs = [[[1, [3, 2]], False], [[1, 2], False]]
    first_input_may_return_as_output_if_fail = False
    output4wrong = False
    check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs,
               first_input_may_return_as_output_if_fail)


def iterable7_tests(func):
    normal_args_list = [1]
    output4normal = False
    several_normal_outputs7 = False
    additional_io_pairs = [
        [[(1, 2)], True]
    ]
    first_input_may_return_as_output_if_fail = False
    output4wrong = False

    specific_wrong_io = None
    check_only_types_in_wrong_output = True

    check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs,
               first_input_may_return_as_output_if_fail, specific_wrong_io, check_only_types_in_wrong_output)


# TODO: make more detailed tests for it
def func_list_to_dict_tests(func):
    normal_args_list = [[
        a_is_in_b_tests,
        iterable7_tests
    ]]

    # normal_args_list = [[]]

    # not the actual output, as it's too variable to check (func memory addreses etc)
    output4normal = {"a_is_in_b": "a_is_in_b_tests", "iterable7": "iterable7_tests"}
    output4normal = dict()
    several_normal_outputs7 = False
    additional_io_pairs = [
    ]
    first_input_may_return_as_output_if_fail = False
    output4wrong = dict()

    specific_wrong_io = None
    check_only_types_in_wrong_output = True
    check_only_types_in_normal_output = True
    shallow_typecheck = True

    check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs,
               first_input_may_return_as_output_if_fail, specific_wrong_io, check_only_types_in_wrong_output,
               check_only_types_in_normal_output, shallow_typecheck)


def check_if_elements_of_same_type_tests(func):
    normal_args_list = [[1, 2], [True, True]]
    output4normal = False
    several_normal_outputs7 = False
    additional_io_pairs = [
        [[[5, 6], [3, 2]], True],
        [["a", "bc"], True],
        [[1, 2], True],
        [[1, "a"], False]
    ]
    first_input_may_return_as_output_if_fail = False
    output4wrong = False
    check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs,
               first_input_may_return_as_output_if_fail)


def check_several_norm_outputs_tests(func):
    test_res = 3
    out4norm = [1, 2]

    normal_args_list = [test_res, out4norm]
    output4normal = "    normal arguments return unexpected results. test_res not in output4normal. test_res:\n3\noutput4normal:\n[\n1\n2\n]"

    several_normal_outputs7 = False
    additional_io_pairs = [
        [[1, out4norm], ""]
    ]
    first_input_may_return_as_output_if_fail = False
    output4wrong = ""
    check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs,
               first_input_may_return_as_output_if_fail)


def check_additional_io_pairs_tests(func):
    input_func = a_is_in_b
    silent_iopairs = [
        [[1, [3, 2]], False],
        [[1, 2], False],
        [[1, [1, 2]], True]
    ]

    loud_iopairs = [
        [[1, 2], True],
    ]

    normal_args_list = [input_func, loud_iopairs]

    test_res = False
    expected_output = True
    norm_args_variant = [1, 2]
    output4normal = "    normal arguments return unexpected results. results:\n" + str(
        test_res) + "\n_expected result:\n" + str(expected_output) + "\n_input: " + str(norm_args_variant) + " \n"

    several_normal_outputs7 = False
    additional_io_pairs = [
        [[input_func, silent_iopairs], ""]
    ]
    first_input_may_return_as_output_if_fail = False
    output4wrong = ""
    check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs,
               first_input_may_return_as_output_if_fail)


def check_normal_types_tests(func):
    normal_args_list = ["text", 2, False]
    output4normal = "The results of the normal input are of unexpected type: expected <class 'int'>, but got <class 'str'> . The elements of an iterable are of a wrong type?\n"
    several_normal_outputs7 = False
    additional_io_pairs = [
        [["text", "another", False], ""],
        [[3, 4, False], ""],
        [[(3, 1), (4, 5), False], ""]
    ]
    first_input_may_return_as_output_if_fail = False
    output4wrong = ""
    check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs,
               first_input_may_return_as_output_if_fail)


def check_main_normals_tests(func):
    ifunc = a_is_in_b

    i0normal_args_list = [1, [1, 2]]
    i0several_normal_outputs7 = False
    i0check_only_types_in_normal_output = False
    i0output4normal = True
    i0shallow_typecheck = False

    i1normal_args_list = [1, [1, 2]]
    i1several_normal_outputs7 = True
    i1check_only_types_in_normal_output = False
    i1output4normal = [True, False]
    i1shallow_typecheck = False
    arg_list1 = [ifunc, i1normal_args_list, i1several_normal_outputs7, i1check_only_types_in_normal_output,
                 i1output4normal, i1shallow_typecheck]
    output1 = ""

    i2normal_args_list = [1, [1, 2]]
    i2several_normal_outputs7 = True
    i2check_only_types_in_normal_output = False
    i2output4normal = ["false", "outputs"]
    i2shallow_typecheck = False
    arg_list2 = [ifunc, i2normal_args_list, i2several_normal_outputs7, i2check_only_types_in_normal_output,
                 i2output4normal, i2shallow_typecheck]
    output2 = "    normal arguments return unexpected results. test_res not in output4normal. test_res:\nTrue\noutput4normal:\n[\nfalse\noutputs\n]"

    i3normal_args_list = [1, [1, 2]]
    i3several_normal_outputs7 = False
    i3check_only_types_in_normal_output = True
    i3output4normal = False
    i3shallow_typecheck = False
    arg_list3 = [ifunc, i3normal_args_list, i3several_normal_outputs7, i3check_only_types_in_normal_output,
                 i3output4normal, i3shallow_typecheck]
    output3 = ""

    i4normal_args_list = [1, [1, 2]]
    i4several_normal_outputs7 = False
    i4check_only_types_in_normal_output = True
    i4output4normal = "badtypeonpurpose"
    i4shallow_typecheck = False
    arg_list4 = [ifunc, i4normal_args_list, i4several_normal_outputs7, i4check_only_types_in_normal_output,
                 i4output4normal, i4shallow_typecheck]
    output4 = "The results of the normal input are of unexpected type: expected <class 'str'>, but got <class 'bool'> . The elements of an iterable are of a wrong type?\n"

    i5normal_args_list = [1, [1, 2]]
    i5several_normal_outputs7 = False
    i5check_only_types_in_normal_output = False
    i5output4normal = False
    i5shallow_typecheck = False
    arg_list5 = [ifunc, i5normal_args_list, i5several_normal_outputs7, i5check_only_types_in_normal_output,
                 i5output4normal, i5shallow_typecheck]
    output5 = "    normal arguments return unexpected results. results:\nTrue\n_expected result:\nFalse\n"

    normal_args_list = [ifunc, i0normal_args_list, i0several_normal_outputs7, i0check_only_types_in_normal_output,
                        i0output4normal, i0shallow_typecheck]
    output4normal = ""
    several_normal_outputs7 = False

    additional_io_pairs = [
        [arg_list1, output1],
        [arg_list2, output2],
        [arg_list3, output3],
        [arg_list4, output4],
        [arg_list5, output5]
    ]

    first_input_may_return_as_output_if_fail = False
    output4wrong = ""
    check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs,
               first_input_may_return_as_output_if_fail)


def check_normal_inputs_tests(func):
    ifunc = a_is_in_b

    i0normal_args_list = [1, [1, 2]]
    i0several_normal_outputs7 = False
    i0check_only_types_in_normal_output = False
    i0output4normal = True
    i0additional_io_pairs = None
    i0shallow_typecheck = False

    i1normal_args_list = [1, [1, 2]]
    i1several_normal_outputs7 = True
    i1check_only_types_in_normal_output = False
    i1output4normal = [True, False]
    i1additional_io_pairs = None
    i1shallow_typecheck = False
    arg_list1 = [ifunc, i1normal_args_list, i1output4normal, i1several_normal_outputs7, i1additional_io_pairs,
                 i1check_only_types_in_normal_output, i1shallow_typecheck]
    output1 = ""

    i2normal_args_list = [1, [1, 2]]
    i2several_normal_outputs7 = True
    i2check_only_types_in_normal_output = False
    i2output4normal = ["false", "outputs"]
    i2additional_io_pairs = None
    i2shallow_typecheck = False
    arg_list2 = [ifunc, i2normal_args_list, i2output4normal, i2several_normal_outputs7, i2additional_io_pairs,
                 i2check_only_types_in_normal_output, i2shallow_typecheck]
    output2 = "    normal arguments return unexpected results. test_res not in output4normal. test_res:\nTrue\noutput4normal:\n[\nfalse\noutputs\n]"

    i3normal_args_list = [1, [1, 2]]
    i3several_normal_outputs7 = False
    i3check_only_types_in_normal_output = True
    i3output4normal = False
    i3additional_io_pairs = None
    i3shallow_typecheck = False
    arg_list3 = [ifunc, i3normal_args_list, i3output4normal, i3several_normal_outputs7, i3additional_io_pairs,
                 i3check_only_types_in_normal_output, i3shallow_typecheck]
    output3 = ""

    i4normal_args_list = [1, [1, 2]]
    i4several_normal_outputs7 = False
    i4check_only_types_in_normal_output = True
    i4output4normal = "badtypeonpurpose"
    i4additional_io_pairs = None
    i4shallow_typecheck = False
    arg_list4 = [ifunc, i4normal_args_list, i4output4normal, i4several_normal_outputs7, i4additional_io_pairs,
                 i4check_only_types_in_normal_output, i4shallow_typecheck]
    output4 = "The results of the normal input are of unexpected type: expected <class 'str'>, but got <class 'bool'> . The elements of an iterable are of a wrong type?\n"

    i5normal_args_list = [1, [1, 2]]
    i5several_normal_outputs7 = False
    i5check_only_types_in_normal_output = False
    i5output4normal = False
    i5additional_io_pairs = None
    i5shallow_typecheck = False
    arg_list5 = [ifunc, i5normal_args_list, i5output4normal, i5several_normal_outputs7, i5additional_io_pairs,
                 i5check_only_types_in_normal_output, i5shallow_typecheck]
    output5 = "    normal arguments return unexpected results. results:\nTrue\n_expected result:\nFalse\n"

    i6normal_args_list = [1, [1, 2]]
    i6several_normal_outputs7 = False
    i6check_only_types_in_normal_output = False
    i6output4normal = True
    i6additional_io_pairs = [
        [[1, (3, 2)], False],
        [[1, 2], False],
        [[1, (1, 2)], True]
    ]
    i6shallow_typecheck = False
    arg_list6 = [ifunc, i6normal_args_list, i6output4normal, i6several_normal_outputs7, i6additional_io_pairs,
                 i6check_only_types_in_normal_output, i6shallow_typecheck]
    output6 = ""

    i7normal_args_list = [1, [1, 2]]
    i7several_normal_outputs7 = False
    i7check_only_types_in_normal_output = False
    i7output4normal = True
    i7additional_io_pairs = [
        [[1, (3, 2)], False],
        [[1, 2], False],
        [[1, (1, 2)], False]
    ]
    i7shallow_typecheck = False
    arg_list7 = [ifunc, i7normal_args_list, i7output4normal, i7several_normal_outputs7, i7additional_io_pairs,
                 i7check_only_types_in_normal_output, i7shallow_typecheck]
    output7 = "    normal arguments return unexpected results. results:\nTrue\n_expected result:\nFalse\n_input: [1, (1, 2)] \n"

    normal_args_list = [ifunc, i0normal_args_list, i0output4normal, i0several_normal_outputs7, i0additional_io_pairs,
                        i0check_only_types_in_normal_output, i0shallow_typecheck]
    output4normal = ""
    several_normal_outputs7 = False

    additional_io_pairs = [
        [arg_list1, output1],
        [arg_list2, output2],
        [arg_list3, output3],
        [arg_list4, output4],
        [arg_list5, output5],
        [arg_list6, output6],
        [arg_list7, output7]
    ]

    first_input_may_return_as_output_if_fail = False
    output4wrong = ""
    check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs,
               first_input_may_return_as_output_if_fail)


def check_specific_wrongs_tests(func):
    ifunc = a_is_in_b
    i0specific_wrong_io = [[1, (3, 2)], False]
    i0check_only_types_in_wrong_output = False
    i0shallow_typecheck = False

    i1specific_wrong_io = [[1, (3, 2)], True]
    i1check_only_types_in_wrong_output = False
    i1shallow_typecheck = False
    i1inputs = [ifunc, i1specific_wrong_io, i1check_only_types_in_wrong_output, i1shallow_typecheck]
    i1output = "The specific wrong argument defined in tests returned unexpected result: \nFalse\n_expected result:\nTrue\n"

    i2specific_wrong_io = [[1, (3, 2)], True]
    i2check_only_types_in_wrong_output = True
    i2shallow_typecheck = False
    i2inputs = [ifunc, i2specific_wrong_io, i2check_only_types_in_wrong_output, i2shallow_typecheck]
    i2output = ""

    i3specific_wrong_io = [[1, (3, 2)], 666]
    i3check_only_types_in_wrong_output = True
    i3shallow_typecheck = False
    i3inputs = [ifunc, i3specific_wrong_io, i3check_only_types_in_wrong_output, i3shallow_typecheck]
    i3output = "The specific wrong argument defined in tests returned an output(s) of wrong type(s)"

    normal_args_list = [ifunc, i0specific_wrong_io, i0check_only_types_in_wrong_output, i0shallow_typecheck]
    output4normal = ""
    several_normal_outputs7 = False
    additional_io_pairs = [
        [i1inputs, i1output],
        [i2inputs, i2output],
        [i3inputs, i3output]
    ]
    first_input_may_return_as_output_if_fail = False
    output4wrong = ""
    check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs,
               first_input_may_return_as_output_if_fail)


def wrong_inputs_by_shift_tests(func):
    ifunc = a_is_in_b
    normal_args_list = [ifunc, [1, 2, 3]]
    output4normal = [2, 3]
    several_normal_outputs7 = False
    empty_input = [ifunc, []]
    additional_io_pairs = [
        [empty_input, [dict()]]
    ]
    first_input_may_return_as_output_if_fail = False
    output4wrong = [dict()]
    check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs,
               first_input_may_return_as_output_if_fail)


def generate_wrong_inputs_tests(func):
    ifunc = a_is_in_b
    inormal_args_list = [1, (1, 2)]

    i1_args = [ifunc, ["a", (1, 2)]]
    i1_outputs = (
        [],
        [True],
        [(1, 2)]
    )

    i2_args = [ifunc, []]
    i2_outputs = (
        [],
        [True],
        [dict()]
    )

    normal_args_list = [ifunc, inormal_args_list]
    output4normal = (
        [],
        ["string"],
        [(1, 2)]
    )
    several_normal_outputs7 = False
    additional_io_pairs = [
        [i1_args, i1_outputs],
        [i2_args, i2_outputs]
    ]

    first_input_may_return_as_output_if_fail = False
    output4wrong = (
        [],
        ["string"],
        [False, dict()]
    )

    check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs,
               first_input_may_return_as_output_if_fail)


def check_wrong_types_tests(func):
    ioutput4wrong = 5
    itest_res0 = 1
    itest_res1 = 2
    itest_res2 = 3
    ishallow_typecheck = False

    i2output4wrong = 5
    i2test_res0 = 1
    i2test_res1 = "text"
    i2test_res2 = 3
    i2shallow_typecheck = False
    i2input = [i2output4wrong, i2test_res0, i2test_res1, i2test_res2, i2shallow_typecheck]
    i2output = "A wrong argument returned an output(s) of wrong type(s). Test results: 1 text 3"

    normal_args_list = [ioutput4wrong, itest_res0, itest_res1, itest_res2, ishallow_typecheck]

    output4normal = ""
    several_normal_outputs7 = False
    additional_io_pairs = [
        [i2input, i2output]
    ]
    first_input_may_return_as_output_if_fail = False
    output4wrong = ""
    check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs,
               first_input_may_return_as_output_if_fail)


def check_fall_through_tests(func):
    wrong_args0 = [1, 2]
    wrong_args1 = [3, 4]
    wrong_args2 = [5, 6]
    test_res0 = 666
    test_res1 = 666
    test_res2 = 666
    ioutput4wrong = "wrong_txt"

    normal_args_list = [wrong_args0, wrong_args1, wrong_args2, test_res0, test_res1, test_res2, ioutput4wrong]
    output4normal = "    arguments of wrong type return unexpected results. 3 test results: \n666\n666\n666\n_expected result:\nwrong_txt\n. A valid first input could also be an output in this case"

    several_normal_outputs7 = False

    args_list2 = [wrong_args0, wrong_args1, wrong_args2, test_res0, test_res1, 5, ioutput4wrong]
    output2 = ""
    additional_io_pairs = [
        [args_list2, output2]
    ]
    first_input_may_return_as_output_if_fail = False
    output4wrong = ""
    check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs,
               first_input_may_return_as_output_if_fail)


def get_func_outputs_tests(func):
    ifunc = a_is_in_b
    wrong_args0 = []
    wrong_args1 = [dict(), 2]
    wrong_args2 = [1, (1, 2)]

    normal_args_list = [ifunc, wrong_args0, wrong_args1, wrong_args2]
    output4normal = (False, False, True)
    several_normal_outputs7 = False
    additional_io_pairs = [
    ]
    first_input_may_return_as_output_if_fail = False
    output4wrong = [], [], []
    check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs,
               first_input_may_return_as_output_if_fail)


def check_generated_wrongs_tests(func):
    ifunc = a_is_in_b

    ifirst_input_may_return_as_output_if_fail = False
    icheck_only_types_in_wrong_output = False
    inormal_args_list = [1, [1, 2]]
    ioutput4wrong = False
    ishallow_typecheck = False
    iarglist = [ifunc, ifirst_input_may_return_as_output_if_fail, icheck_only_types_in_wrong_output, inormal_args_list,
                ioutput4wrong, ishallow_typecheck]

    i1first_input_may_return_as_output_if_fail = False
    i1check_only_types_in_wrong_output = True
    i1normal_args_list = [1, [1, 2]]
    i1output4wrong = True
    i1shallow_typecheck = False
    i1arglist = [ifunc, i1first_input_may_return_as_output_if_fail, i1check_only_types_in_wrong_output,
                 i1normal_args_list, i1output4wrong, i1shallow_typecheck]
    i1output = ""

    i2first_input_may_return_as_output_if_fail = False
    i2check_only_types_in_wrong_output = True
    i2normal_args_list = [1, [1, 2]]
    i2output4wrong = 666
    i2shallow_typecheck = False
    i2arglist = [ifunc, i2first_input_may_return_as_output_if_fail, i2check_only_types_in_wrong_output,
                 i2normal_args_list, i2output4wrong, i2shallow_typecheck]
    i2output = "A wrong argument returned an output(s) of wrong type(s). Test results: False False False"

    i3first_input_may_return_as_output_if_fail = False
    i3check_only_types_in_wrong_output = False
    i3normal_args_list = [1, [1, 2]]
    i3output4wrong = 666
    i3shallow_typecheck = False
    i3arglist = [ifunc, i3first_input_may_return_as_output_if_fail, i3check_only_types_in_wrong_output,
                 i3normal_args_list, i3output4wrong, i3shallow_typecheck]
    i3output = "    arguments of wrong type return unexpected results. 3 test results: \nFalse\nFalse\nFalse\n_expected result:\n666\n"

    i4first_input_may_return_as_output_if_fail = True
    i4check_only_types_in_wrong_output = False
    i4normal_args_list = [False, [1, 2]]
    i4output4wrong = False
    i4shallow_typecheck = False
    i4arglist = [ifunc, i4first_input_may_return_as_output_if_fail, i4check_only_types_in_wrong_output,
                 i4normal_args_list, i4output4wrong, i4shallow_typecheck]
    i4output = ""

    i5first_input_may_return_as_output_if_fail = True
    i5check_only_types_in_wrong_output = False
    i5normal_args_list = [1, [1, 2]]
    i5output4wrong = 666
    i5shallow_typecheck = False
    i5arglist = [ifunc, i5first_input_may_return_as_output_if_fail, i5check_only_types_in_wrong_output,
                 i5normal_args_list, i5output4wrong, i5shallow_typecheck]
    i5output = "    arguments of wrong type return unexpected results. 3 test results: \nFalse\nFalse\nFalse\n_expected result:\n666\n. A valid first input could also be an output in this case"

    normal_args_list = iarglist
    output4normal = ""
    several_normal_outputs7 = False
    additional_io_pairs = [
        [i1arglist, i1output],
        [i2arglist, i2output],
        [i3arglist, i3output],
        [i4arglist, i4output],
        [i5arglist, i5output]
    ]
    first_input_may_return_as_output_if_fail = False
    output4wrong = ""
    check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs,
               first_input_may_return_as_output_if_fail)


def check_wrong_inputs_tests(func):
    ifunc = a_is_in_b

    i0first_input_may_return_as_output_if_fail = False
    i0check_only_types_in_wrong_output = False
    i0normal_args_list = [1, [1, 2]]
    i0output4wrong = False
    i0specific_wrong_io = None
    i0shallow_typecheck = False
    i0arglist = [ifunc, i0normal_args_list, i0output4wrong, i0first_input_may_return_as_output_if_fail,
                 i0specific_wrong_io, i0check_only_types_in_wrong_output, i0shallow_typecheck]

    i1first_input_may_return_as_output_if_fail = False
    i1check_only_types_in_wrong_output = True
    i1normal_args_list = [1, [1, 2]]
    i1output4wrong = True
    i1specific_wrong_io = None
    i1shallow_typecheck = False
    i1arglist = [ifunc, i1normal_args_list, i1output4wrong, i1first_input_may_return_as_output_if_fail,
                 i1specific_wrong_io, i1check_only_types_in_wrong_output, i1shallow_typecheck]
    i1output = ""

    i2first_input_may_return_as_output_if_fail = False
    i2check_only_types_in_wrong_output = True
    i2normal_args_list = [1, [1, 2]]
    i2output4wrong = 666
    i2specific_wrong_io = None
    i2shallow_typecheck = False
    i2arglist = [ifunc, i2normal_args_list, i2output4wrong, i2first_input_may_return_as_output_if_fail,
                 i2specific_wrong_io, i2check_only_types_in_wrong_output, i2shallow_typecheck]
    i2output = "A wrong argument returned an output(s) of wrong type(s). Test results: False False False"

    i3first_input_may_return_as_output_if_fail = False
    i3check_only_types_in_wrong_output = False
    i3normal_args_list = [1, [1, 2]]
    i3output4wrong = 666
    i3specific_wrong_io = None
    i3shallow_typecheck = False
    i3arglist = [ifunc, i3normal_args_list, i3output4wrong, i3first_input_may_return_as_output_if_fail,
                 i3specific_wrong_io, i3check_only_types_in_wrong_output, i3shallow_typecheck]
    i3output = "    arguments of wrong type return unexpected results. 3 test results: \nFalse\nFalse\nFalse\n_expected result:\n666\n"

    i4first_input_may_return_as_output_if_fail = True
    i4check_only_types_in_wrong_output = False
    i4normal_args_list = [False, [1, 2]]
    i4output4wrong = False
    i4specific_wrong_io = None
    i4shallow_typecheck = False
    i4arglist = [ifunc, i4normal_args_list, i4output4wrong, i4first_input_may_return_as_output_if_fail,
                 i4specific_wrong_io, i4check_only_types_in_wrong_output, i4shallow_typecheck]
    i4output = ""

    i5first_input_may_return_as_output_if_fail = True
    i5check_only_types_in_wrong_output = False
    i5normal_args_list = [1, [1, 2]]
    i5output4wrong = 666
    i5specific_wrong_io = None
    i5shallow_typecheck = False
    i5arglist = [ifunc, i5normal_args_list, i5output4wrong, i5first_input_may_return_as_output_if_fail,
                 i5specific_wrong_io, i5check_only_types_in_wrong_output, i5shallow_typecheck]
    i5output = "    arguments of wrong type return unexpected results. 3 test results: \nFalse\nFalse\nFalse\n_expected result:\n666\n. A valid first input could also be an output in this case"

    i6first_input_may_return_as_output_if_fail = False
    i6check_only_types_in_wrong_output = False
    i6normal_args_list = [1, [1, 2]]
    i6output4wrong = False
    i6specific_wrong_io = [[1, (3, 2)], False]
    i6shallow_typecheck = False
    i6arglist = [ifunc, i6normal_args_list, i6output4wrong, i6first_input_may_return_as_output_if_fail,
                 i6specific_wrong_io, i6check_only_types_in_wrong_output, i6shallow_typecheck]
    i6output = ""

    i7first_input_may_return_as_output_if_fail = False
    i7check_only_types_in_wrong_output = True
    i7normal_args_list = [1, [1, 2]]
    i7output4wrong = False
    i7specific_wrong_io = [[1, (3, 2)], True]
    i7shallow_typecheck = False
    i7arglist = [ifunc, i7normal_args_list, i7output4wrong, i7first_input_may_return_as_output_if_fail,
                 i7specific_wrong_io, i7check_only_types_in_wrong_output, i7shallow_typecheck]
    i7output = ""

    i8first_input_may_return_as_output_if_fail = False
    i8check_only_types_in_wrong_output = False
    i8normal_args_list = [1, [1, 2]]
    i8output4wrong = False
    i8specific_wrong_io = [[1, (3, 2)], 666]
    i8shallow_typecheck = False
    i8arglist = [ifunc, i8normal_args_list, i8output4wrong, i8first_input_may_return_as_output_if_fail,
                 i8specific_wrong_io, i8check_only_types_in_wrong_output, i8shallow_typecheck]
    i8output = "The specific wrong argument defined in tests returned unexpected result: \nFalse\n_expected result:\n666\n"

    normal_args_list = i0arglist
    output4normal = ""
    several_normal_outputs7 = False
    additional_io_pairs = [
        [i1arglist, i1output],
        [i2arglist, i2output],
        [i3arglist, i3output],
        [i4arglist, i4output],
        [i5arglist, i5output],
        [i6arglist, i6output],
        [i7arglist, i7output],
        [i8arglist, i8output]
    ]
    first_input_may_return_as_output_if_fail = False
    output4wrong = ""
    check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs,
               first_input_may_return_as_output_if_fail)


def check_func_tests(func):
    ifunc = a_is_in_b

    i0normal_args_list = [1, [1, 2]]
    i0output4normal = True
    i0output4wrong = False
    i0several_normal_outputs7 = False
    i0additional_io_pairs = []
    i0first_input_may_return_as_output_if_fail = False
    i0specific_wrong_io = None
    i0check_only_types_in_wrong_output = False
    i0check_only_types_in_normal_output = False
    i0shallow_typecheck = False
    i0no_console_output = "no_console_output"
    i0arglist = [ifunc, i0normal_args_list, i0output4normal, i0output4wrong, i0several_normal_outputs7,
                 i0additional_io_pairs, i0first_input_may_return_as_output_if_fail, i0specific_wrong_io,
                 i0check_only_types_in_wrong_output, i0check_only_types_in_normal_output, i0shallow_typecheck,
                 i0no_console_output]
    i0otput = ""

    i1normal_args_list = [1, [1, 2]]
    i1output4normal = 666
    i1output4wrong = False
    i1several_normal_outputs7 = False
    i1additional_io_pairs = []
    i1first_input_may_return_as_output_if_fail = False
    i1specific_wrong_io = None
    i1check_only_types_in_wrong_output = False
    i1check_only_types_in_normal_output = False
    i1shallow_typecheck = False
    i1no_console_output = "no_console_output"
    i1arglist = [ifunc, i1normal_args_list, i1output4normal, i1output4wrong, i1several_normal_outputs7,
                 i1additional_io_pairs, i1first_input_may_return_as_output_if_fail, i1specific_wrong_io,
                 i1check_only_types_in_wrong_output, i1check_only_types_in_normal_output, i1shallow_typecheck,
                 i1no_console_output]
    i1otput = "a_is_in_b is not working properly: \n    normal arguments return unexpected results. results:\nTrue\n_expected result:\n666\n\n"

    i2normal_args_list = [1, [1, 2]]
    i2output4normal = True
    i2output4wrong = 777
    i2several_normal_outputs7 = False
    i2additional_io_pairs = []
    i2first_input_may_return_as_output_if_fail = False
    i2specific_wrong_io = None
    i2check_only_types_in_wrong_output = False
    i2check_only_types_in_normal_output = False
    i2shallow_typecheck = False
    i2no_console_output = "no_console_output"
    i2arglist = [ifunc, i2normal_args_list, i2output4normal, i2output4wrong, i2several_normal_outputs7,
                 i2additional_io_pairs, i2first_input_may_return_as_output_if_fail, i2specific_wrong_io,
                 i2check_only_types_in_wrong_output, i2check_only_types_in_normal_output, i2shallow_typecheck,
                 i2no_console_output]
    i2otput = "a_is_in_b is not working properly: \n    arguments of wrong type return unexpected results. 3 test results: \nFalse\nFalse\nFalse\n_expected result:\n777\n\n"

    i3normal_args_list = [1, [1, 2]]
    i3output4normal = 888
    i3output4wrong = 777
    i3several_normal_outputs7 = False
    i3additional_io_pairs = []
    i3first_input_may_return_as_output_if_fail = False
    i3specific_wrong_io = None
    i3check_only_types_in_wrong_output = False
    i3check_only_types_in_normal_output = False
    i3shallow_typecheck = False
    i3no_console_output = "no_console_output"
    i3arglist = [ifunc, i3normal_args_list, i3output4normal, i3output4wrong, i3several_normal_outputs7,
                 i3additional_io_pairs, i3first_input_may_return_as_output_if_fail, i3specific_wrong_io,
                 i3check_only_types_in_wrong_output, i3check_only_types_in_normal_output, i3shallow_typecheck,
                 i3no_console_output]
    i3otput = "a_is_in_b is not working properly: \n    normal arguments return unexpected results. results:\nTrue\n_expected result:\n888\n    arguments of wrong type return unexpected results. 3 test results: \nFalse\nFalse\nFalse\n_expected result:\n777\n\n"

    i4func = get_commons4tests
    i4normal_args_list = []
    i4output4normal = [5, 5]
    i4output4wrong = [False, True]
    i4several_normal_outputs7 = False
    i4additional_io_pairs = []
    i4first_input_may_return_as_output_if_fail = False
    i4specific_wrong_io = None
    i4check_only_types_in_wrong_output = True
    i4check_only_types_in_normal_output = True
    i4shallow_typecheck = True
    i4no_console_output = "no_console_output"
    i4arglist = [i4func, i4normal_args_list, i4output4normal, i4output4wrong, i4several_normal_outputs7,
                 i4additional_io_pairs, i4first_input_may_return_as_output_if_fail, i4specific_wrong_io,
                 i4check_only_types_in_wrong_output, i4check_only_types_in_normal_output, i4shallow_typecheck,
                 i4no_console_output]
    i4otput = ""

    normal_args_list = i0arglist

    output4normal = i0otput
    several_normal_outputs7 = False
    additional_io_pairs = [
        [i1arglist, i1otput],
        [i2arglist, i2otput],
        [i3arglist, i3otput],
        [i4arglist, i4otput]
    ]
    first_input_may_return_as_output_if_fail = False
    output4wrong = ""

    check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs,
               first_input_may_return_as_output_if_fail)


def get_funcs_dict_tests(func):
    normal_args_list = []
    output4normal = dict()  # not the actual normal output, as it's too variable to test
    several_normal_outputs7 = False
    additional_io_pairs = [
    ]
    first_input_may_return_as_output_if_fail = False
    output4wrong = dict()

    specific_wrong_io = None
    check_only_types_in_wrong_output = True
    check_only_types_in_normal_output = True
    shallow_typecheck = True

    check_func(func, normal_args_list, output4normal, output4wrong, several_normal_outputs7, additional_io_pairs,
               first_input_may_return_as_output_if_fail, specific_wrong_io, check_only_types_in_wrong_output,
               check_only_types_in_normal_output, shallow_typecheck)


def get_funcs_dict(*args):
    try:

        imported_funcs = primitive_tests.funcs_list()

        self_awareness_funcs = [
            tests_tests,  # this and below are for self_awareness.py
            get_commons4tests_tests,
            check_own_existance_tests,
            deleteFile_tests,
            str2_tests,
            lists_equal7_tests,
            equal_tests,
            a_is_in_b_tests,
            iterable7_tests,
            func_list_to_dict_tests,
            check_if_elements_of_same_type_tests,
            check_several_norm_outputs_tests,
            check_additional_io_pairs_tests,
            check_normal_types_tests,
            check_main_normals_tests,
            check_normal_inputs_tests,
            check_specific_wrongs_tests,
            generate_wrong_inputs_tests,
            wrong_inputs_by_shift_tests,
            check_wrong_types_tests,
            check_fall_through_tests,
            get_func_outputs_tests,
            check_generated_wrongs_tests,
            check_wrong_inputs_tests,
            check_func_tests,
            get_funcs_dict_tests
        ]

        test_funcs_list = imported_funcs + self_awareness_funcs

        funcs_dic = func_list_to_dict(test_funcs_list)

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
                res = funcs_dic.get(tfunc.__name__)(tfunc)  # dont delete. It's where tests are executed
                res = True
            else:
                if debug_mode == "verbose":
                    print("\ncaution: " + tfunc.__name__ + " is not covered by tests yet")
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


try:
    tests(check_own_existance)
    tests(deleteFile)
    tests(str2)
    tests(lists_equal7)
    tests(equal)
    tests(a_is_in_b)
    tests(iterable7)
    tests(func_list_to_dict)
    tests(check_if_elements_of_same_type)
    tests(check_several_norm_outputs)
    tests(check_additional_io_pairs)
    tests(check_normal_types)
    tests(check_main_normals)
    tests(check_normal_inputs)
    tests(check_specific_wrongs)
    tests(wrong_inputs_by_shift)
    tests(generate_wrong_inputs)
    tests(check_wrong_types)
    tests(check_fall_through)
    tests(get_func_outputs)
    tests(check_generated_wrongs)
    tests(check_wrong_inputs)
    tests(check_func)
    tests(get_funcs_dict)

    tests(get_commons4tests)

    tests(tests)  # checking if the self-diag functionality itself is working properly
except Exception as e:
    print("A function you want to test seem to be nonexistant")
