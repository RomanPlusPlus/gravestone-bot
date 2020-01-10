# import pathlib
import datetime
import random
import os

from shutil import copyfile

from text_shuffle import get_pattern_list, shuffle_str_list, check_if_already_obfusc
from helper_funcs import recursive_file_search

input_folder_path = "input_texts/"
output_folder_path = "input_texts2/"

obfuscated_tag = "<obfuscated>"

pattern_l = get_pattern_list()


def create_folder(folder_path):
    from pathlib import Path
    Path(folder_path).mkdir(parents=True, exist_ok=True)
    # https://stackoverflow.com/questions/273192/how_can_i_safely_create_a_nested_directory


def read_file2list(f_path):
    temp_l = []
    with open(f_path) as f:
        temp_l = f.readlines()
    return temp_l


def write_l2file(path, shuffled_l):
    with open(path, 'w') as f:
        for i in range(len(shuffled_l)):
            f.write(shuffled_l[i])
        f.write("\n" + obfuscated_tag)


def clean_str_list(i_list):
    for i in range(len(i_list)):
        temp_str = i_list[i]
        i_list[i] = temp_str.strip()
    return i_list


# get a human_readable timestamp
def human_timestamp():
    now = datetime.datetime.now()
    time_st = now.strftime('%y%m%d%h%m%s%f')[:-3]
    time_st += str(random.randint(0, 9))  # to avoid rewriting the log if made at the same millisecond
    return time_st


# print(human_timestamp())

# get list of input files
f_list = recursive_file_search(input_folder_path, ".txt")
# print(f_list)

# backup input files to avoid possible data loss
backup_folder = "input_texts_backup" + human_timestamp() + "/"
create_folder(backup_folder)
for i in range(len(f_list)):  # using copyfile instead of copytree because copytree doesnt work on android
    src_f_path = f_list[i]
    dst_f_path = backup_folder + os.path.basename(src_f_path)
    copyfile(src_f_path, dst_f_path)
print("the input files were backed up to " + backup_folder + "\n")

for i in range(len(f_list)):
    in_path = f_list[i]
    str_l = read_file2list(in_path)
    #    str_l = clean_str_list(str_l)
    if check_if_already_obfusc(str_l):
        print(in_path + " is already obfuscated. exiting to prevent data loss.")
        exit()

    shuffled_l = shuffle_str_list(str_l, pattern_l, "obfuscate")

    #   s_path =output_folder_path + in_path[len(input_folder_path):]

    write_l2file(in_path, shuffled_l)
    print("obfuscated " + in_path)

print("done")
