########################################################################
# Does a lossless compression of text, with a twist:  
# the result remains to be human-readable. 

# It was written to compress a long list of questions. 
# It could also work on some other semi-repititive texts.   

# A sample input:

# Where are you? 
# Where are you from?
# Where do you live?
# Where do you prefer to go when going outside?

# In this case, the output is:

# Where
#	are
#		you?
#		you from?
#	do
#		you
#			live?
#			prefer to go when going outside?

# On a list of common questions, a compression rate of ~20% can be achieved. 
########################################################################


spacer = "	"


# TODO: replace it with the already implemented func
def string_2_list_of_words(s):
    l = s.split()
    return l


def get_words_by_row(temp_rows):
    words_by_row = []
    for i in range(len(temp_rows)):
        words_by_row.append(string_2_list_of_words(temp_rows[i]))
    return words_by_row


def cut_position(full_words_l, word_ind):
    cutted_words_l = full_words_l[0:word_ind + 1]
    sum_of_word_lens = 0
    for wrd in cutted_words_l:
        sum_of_word_lens += len(wrd)
    sum_of_word_lens += len(cutted_words_l) - 1  # to add " " between words
    return sum_of_word_lens


def remove_tildas(tilded_rows):
    processed_l = []
    for rt in range(len(tilded_rows)):
        processed_l.append(tilded_rows[rt].replace("~", ""))
    return processed_l


def has_tildas7(text_l):
    res = False
    for row in text_l:
        if "~" in row:
            res = True
    return res


def emulgate_word(temp_l, words_l):
    compressed_strings_l = []
    counter = 0
    while counter < len(words_l):
        # print("Check ", temp_l[counter])
        test_word = words_l[counter][0]
        if counter < len(words_l) - 1 and test_word == words_l[counter + 1][0]:
            if test_word[0] == "~":
                key = test_word[1:]
            else:
                key = test_word
            compressed_strings_l.append("#" + key)

            w = words_l[counter][0]
            tl = len(w) + 1
            # tl = cut_position(words_l[counter], 0)
            # print(words_l[counter])
            # print("cut_position", tl)

            while w == test_word:
                w = words_l[counter][0]
                if w == test_word:
                    compressed_strings_l.append("~" + temp_l[counter][tl:])
                counter += 1
            counter -= 1
            # print("string number:", counter+1)
        else:
            compressed_strings_l.append("#" + temp_l[counter])
            counter += 1
            # print("string number:", counter+1)
    return compressed_strings_l


def compress(input_path, output_path):
    # f_path = "input.txt"
    with open(input_path) as f:
        loaded_rows = f.readlines()

    raw_rows = []
    for i in range(len(loaded_rows)):
        raw_txt = loaded_rows[i].strip()
        raw_txt = raw_txt.strip(spacer)
        raw_rows.append(raw_txt)

    sorted(raw_rows)

    still_tildas = True
    passes = 0
    while still_tildas:
        passes += 1
        rows_without_tildas = remove_tildas(raw_rows)
        words_by_row = get_words_by_row(rows_without_tildas)
        raw_rows = emulgate_word(rows_without_tildas, words_by_row)
        still_tildas = has_tildas7(raw_rows)

    # convert the hash sign into the ~ sign
    compressed_strings_l = []
    for i in range(len(raw_rows)):
        test_raw = raw_rows[i]
        num_of_hashes = test_raw.count("#")
        num_of_tildas = passes - num_of_hashes
        for j in range(num_of_tildas):
            test_raw = spacer + test_raw
        test_raw = test_raw.replace("#", "")
        compressed_strings_l.append(test_raw)

    for i in range(len(compressed_strings_l)):
        # print(temp_l[i])
        print(compressed_strings_l[i])

    with open(output_path, 'w') as f:
        for i in range(len(compressed_strings_l)):
            f.write(compressed_strings_l[i] + "\n")


def count_missing_words(compressed_s):
    counter = compressed_s.count(spacer)
    return counter


def replace_spacer_with_word_at_position(istr, position, word):
    return istr[0:position] + word + " " + istr[position + 1:]


def replace_spacers_with_word_l(istr, word_l):
    res = ""
    word_n = len(word_l)
    for rsw in range(word_n):
        res += word_l[rsw] + " "
    res = res + istr[word_n:]
    return res


def find_missing_word(raw_rows, raw_ind, word_pos):
    p = raw_ind
    res = ""
    while p >= 0:
        test_str = raw_rows[p]
        if test_str[word_pos] != spacer:
            res = test_str.strip()
            break
        p -= 1
    return res, p


# mode can be "to_file" or "to_memory"
def recover(mode, input_path, output_path="output_recovered.txt"):
    with open(input_path) as f:
        loaded_rows = f.readlines()

    missing_counts = []
    for i in range(len(loaded_rows)):
        missing_counts.append(count_missing_words(loaded_rows[i]))

    recovered_rows = []
    for i in range(len(loaded_rows)):
        recovered_rows.append(loaded_rows[i])

    sources = []
    for i in range(len(loaded_rows)):
        missing_num = count_missing_words(loaded_rows[i])
        wordl = []
        for j in range(missing_num):
            mword, source_ind = find_missing_word(loaded_rows, i, j)
            wordl.append(mword)
            sources.append(source_ind)

        recovered_rows[i] = replace_spacers_with_word_l(loaded_rows[i], wordl)

    no_duplicates = []
    for i in range(len(recovered_rows)):
        if (i not in sources):
            no_duplicates.append(recovered_rows[i])

    if mode == "to_file":
        with open(output_path, 'w') as f:
            for i in range(len(no_duplicates)):
                f.write(no_duplicates[i].strip() + "\n")
    return no_duplicates

# compress("input.txt", "input_compressed.txt")
# res = recover("to_file","input_compressed.txt")

# print(res)

# print(count_missing_words("		age"))

# print(replace_spacer_with_word_at_position("		age", 0, "what"))

# raw_rows = [
#    "Can",
#    "	I help you?",
#    "	you",
#    "		do me a favor?",
#    "		help me?"
# ]

# print(find_missing_word(raw_rows, 4, 0))
