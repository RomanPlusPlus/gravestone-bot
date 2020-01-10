debug_mode = "off"


class string_with_ref:
    def __init__(self, new_text, new_ref, new_index, new_word_set, new_answers_list, new_global_ind, new_type):
        self.text = new_text
        self.ref = new_ref  # the file path where the text is stored
        self.index = new_index  # index of the string in the source file
        self.wordset = new_word_set  # the set of words the text field contains
        self.answers_list = new_answers_list
        self.global_ind = new_global_ind  # index of this rstr in the list of all rstrs
        self.type = new_type

    #        self.next_rstr_index = new_next_rstr_index # index of the thematically next rstr in the list of rstr

    def __str__(self):
        return "text: " + self.text + "\nref: " + self.ref + "\nindex: " + str(self.index) + "\nwordset: " + str(
            self.wordset) + "\nanswers_list: " + str(self.answers_list) + "\nglobal_ind: " + str(
            self.global_ind) + "\ntype:" + str(self.type) + "\n"

    def __eq__(self, other):
        res = True
        log = ""
        if not isinstance(other, string_with_ref):
            res = False
            log += "not rstring\n"
        if self.text != other.text:
            res = False
            log += "text different:\n>" + self.text + "<\n>" + other.text + "<\n"
        if self.ref != other.ref:
            res = False
            log += "ref different\n"
        if self.index != other.index:
            res = False
            log += "index different\n"
        if self.wordset != other.wordset:
            res = False
            log += "wordset different\n"
        if self.answers_list != other.answers_list:
            res = False
            log += "answers_list different\n"
        if self.global_ind != other.global_ind:
            res = False
            log += "global ind different\n"
        if self.type != other.type:
            res = False
            log += " type different\n"

        if debug_mode == "verbose":
            print(log)

        return res
