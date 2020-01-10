# asks the user qustions and saves the answers to
# the input folder of the chatbot.
# useful during the chatbot creation.

import os.path

from helper_funcs import get_random_element_of_list
from linguistic_engine import get_faq_tag

path2questions = "res/interview_qs.txt"
path2answers = "input_texts/interview_as.txt"

faq_tag = get_faq_tag()


def add_additional_answer(answer, question):
    with open(path2answers) as aq:
        aq_strings = aq.readlines()
    aq_strings.pop(0)  # delete tag
    for i in range(len(aq_strings)):
        aq_strings[i] = aq_strings[i].strip()
    #    print(aq_strings)
    q_index = aq_strings.index("Q: " + question)
    #    print(q_index)
    aq_strings.insert(q_index + 1, "A: " + answer)
    #    print(aq_strings)
    with open(path2answers, 'w') as answers_file:
        answers_file.write(faq_tag + "\n")
        for fi in range(len(aq_strings)):
            answers_file.write(aq_strings[fi] + "\n")


def load_answered_qs(answers_path):
    answered = []
    if os.path.isfile(answers_path):
        with open(answers_path) as aq:
            aq_strings = aq.readlines()
        for i in range(len(aq_strings)):
            st = aq_strings[i].strip()
            if st[0:2] == "Q:":
                answered.append(st[3:])
    return answered


def save_answer(answer, question, first_answer7):
    answered_l = load_answered_qs(path2answers)
    already_answered7 = False
    if question in answered_l:
        already_answered7 = True

    if already_answered7:
        add_additional_answer(answer, question)
    else:  # append to the end of file
        with open(path2answers, 'a') as f:
            if first_answer7:
                f.write(faq_tag + "\n")
            f.write("q: " + question + "\n_a: " + answer + "\n")


def select_question(all_questions):
    # try to find an unanswered
    answered = load_answered_qs(path2answers)
    found = False
    c = 0
    good_q_s = ""
    while (found is False) and (c < len(all_questions)):
        test_s = all_questions[c]
        #        print(test_s)
        if test_s not in answered:
            found = True
            good_q_s = test_s
        c += 1
    #    print(found)
    if found is False:  # all are answered. choose a random one
        good_q_s = get_random_element_of_list(all_questions)
    return good_q_s, found


# load questions
with open(path2questions) as f:
    q_strings = f.readlines()
for i in range(len(q_strings)):
    temp_s = q_strings[i].strip()
    q_strings[i] = temp_s

# check if some answers are already answered 
first_answer7 = True
answered_l = []
if os.path.isfile(path2answers):
    first_answer7 = False
    answered_l = load_answered_qs(path2answers)

# print(answered_l)

# main q&a routine
print(
    "this is a helper program. it helps to improve the bot. it asks the user (you) to answer some common questions. answers are immediately saved. you can exit at any time by typing exit and then pressing enter. \n")
answer = ""
q_count = 0
notified_about_all_ansered7 = False
while True:
    question, unanswered_exist7 = select_question(q_strings)
    if notified_about_all_ansered7 == False and unanswered_exist7 == False:
        print(
            "\n_congratulations, you've answered all questions. you can exit, or provide additional answers' variants to the same questions. the more variants there are, the more natural thr conversation will sound. be creative! \n")
        notified_about_all_ansered7 = True
    answer = input(question + "\n")
    if answer != "exit":
        save_answer(answer, question, first_answer7)
        if q_count >= 0:
            first_answer7 = False
        q_count += 1
    else:
        break
