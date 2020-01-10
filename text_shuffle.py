import self_awareness as sf

debug_mode = "off"

obfuscated_tag = "<obfuscated>"


def get_pattern_list(*args):
    #  pattern_s = "5248631709"
    #  patt_list = []
    # for i in range(len(pattern_s)):
    # patt_list.append(int(pattern_s[i]))

    return [5, 2, 4, 8, 6, 3, 1, 7, 0,
            9]  # means that each 10-latter chunk of text will be shuffled like: 0123456789 --> 5248630719


sf.tests(get_pattern_list)


# shuffles the input string according to the pattern
# The input string must be of the same length as the pattern.
def obfuscate_chunk(*args):
    i_str = ""
    o_str = ""
    pattern_list = ""
    try:
        i_str = args[0]
        pattern_list = args[1]
        if len(i_str) != len(pattern_list):
            if debug_mode != "off":
                print("CAUTION: i_str and pattern_list lengths must be same. Pattern of wrong length?")
            o_str = ""
        else:
            o_str = ""
            for i in range(len(i_str)):
                o_str += i_str[pattern_list[i]]
    except Exception as e:
        o_str = ""
        if debug_mode != "off":
            print("obfuscate_chunk : ", str(e))

    return o_str


sf.tests(obfuscate_chunk)


# de-obfuscates the input string according to the pattern.
# The input string must be of the same length as the pattern.
def recover_chunk(*args):
    try:
        i_str = args[0]
        pattern_list = args[1]
        if len(i_str) != len(pattern_list):
            if debug_mode != "off":
                print("CAUTION: i_str and pattern_list lengths must be same. Pattern of wrong length?")
            o_str = ""
        o_str_list = [""] * len(i_str)
        for i in range(len(i_str)):
            o_str_list[pattern_list[i]] = i_str[i]
        o_str = ""
        for i in range(len(o_str_list)):
            o_str += o_str_list[i]

    except:
        o_str = ""
    return o_str


sf.tests(recover_chunk)


def concatenate_strings_list(*args):
    res = ""
    try:
        input_l = args[0]
        if isinstance(input_l, list):
            united_str = ""
            for i in range(len(input_l)):
                united_str += input_l[i]
            res = united_str
    except:
        res = ""
    return res


sf.tests(concatenate_strings_list)


# def split_string_into_list_by_template(i_str, tamplate_l, padding_len):
#    o_str_l = []
#    end_c = 0
#    for i in range(0, len(tamplate_l)):  
#        start_c = end_c
#        end_c += len(tamplate_l[i])    
#        o_str_l.append(i_str[start_c : end_c])
#    o_str_l.append(i_str[end_c : end_c+padding_len])
#    return o_str_l  
# sf.tests(split_string_into_list_by_template)


# the modes are "obfuscate" or "recover"    
def shuffle_str(*args):
    try:
        i_str, pattern_list, mode = args[0:4]
        pat_len = len(pattern_list)
        o_str = ""
        for i in range(int(len(i_str) / pat_len)):
            test_str = i_str[i * pat_len: (i + 1) * pat_len]
            if mode == "obfuscate":
                shuf_str = obfuscate_chunk(test_str, pattern_list)
            else:
                shuf_str = recover_chunk(test_str, pattern_list)
            o_str += shuf_str
    except:
        o_str = ""
    return o_str


sf.tests(shuffle_str)


# Obfuscates or de-obfuscates a text stored in a list of strings.
# The modes are "obfuscate" or "recover"
def shuffle_str_list(*args):
    try:
        str_l, pattern_list, mode = args
        united_str = concatenate_strings_list(str_l)
        pat_len = len(pattern_list)
        padding_len = pat_len - len(united_str) % pat_len
        united_str += " " * padding_len
        united_str_shuffled = shuffle_str(united_str, pattern_list, mode)
        # print(pat_len)
        res = united_str_shuffled
    except:
        res = []
    return res


sf.tests(shuffle_str_list)


def check_if_already_obfusc(*args):
    res = False
    try:
        str_l = args[0]
        if len(str_l) > 1:  # obfuscated files must have the tag about it, on a separate line
            test_str = str_l[-1].strip()
            if test_str == obfuscated_tag:
                res = True
            else:
                res = False
    except:
        res = False
    return res


sf.tests(check_if_already_obfusc)
