import glob
import os

import self_awareness as sf

debug_mode = "off"


def get_absolute_path(*args):
    fallback_output = "unable to get path"
    log = ""
    try:
        relative_path = args[0]
        if isinstance(relative_path, str):
            fallback_output = relative_path
    except Exception as e:
        relative_path = "unable to get path"
        log += str(e)
    try:
        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        absolute_path = os.path.join(__location__, relative_path)
        res = absolute_path
    except Exception as e:
        res = fallback_output
        log += str(e)
    if debug_mode == "verbose":
        print(log)
    return res


sf.tests(get_absolute_path)


# takes file_type in the form like ".txt"
def recursive_file_search(*args):
    try:
        path, file_type = args
        files = [f for f in glob.glob(path + "**/*" + file_type, recursive=True)]
        if len(files) == 0:
            path = get_absolute_path(path)
            files = [f for f in glob.glob(path + "**/*" + file_type, recursive=True)]
        sorted_files = sorted(files)  # to make the order of the list deterministic (useful for tests etc)
        res = sorted_files
    except Exception as e:
        res = []
        if debug_mode == "verbose":
            print(e)
    return res


sf.tests(recursive_file_search)


# try:
#    import zlib 
#    compression = zipfile.zip_deflated
#    print("no zlib")
# except:
#    compression = zipfile.zip_stored
# print("compression", compression)

def extract_all_zips(*args):
    try:
        #    a = 2/0
        from zipfile import ZipFile

        input_dir = args[0]
        files_before = set(recursive_file_search(input_dir, ".txt"))
        paths = recursive_file_search(input_dir, ".zip")
        if len(paths) == 0:
            if debug_mode != "off":
                print("no zip files found in", input_dir)
        else:
            for p in paths:
                with ZipFile(p, "r") as zip_ref:
                    zip_ref.extractall(input_dir)
                if debug_mode != "off":
                    print("\nextracted", p)
        files_after = set(recursive_file_search(input_dir, ".txt"))
        res = files_after.difference(files_before)

    except Exception as e:
        res = set()
        if debug_mode == "verbose":
            print("Extract_all_zips raised an exception:", e)

    return res


sf.tests(extract_all_zips)


def get_random_element_of_list(*args):
    i_list = []
    log = ""
    try:
        temp = args[0]
        if isinstance(temp, list):
            i_list = temp
    except Exception as e:
        i_list = []
        log += str(e)
    if len(i_list) > 0:
        try:
            import random
            rnd_index = random.randint(0, len(i_list) - 1)
            res = i_list[rnd_index]
        except Exception as e:
            res = i_list[0]
            log += str(e)
    else:
        res = None
    if debug_mode == "verbose":
        print(log)
    return res


sf.tests(get_random_element_of_list)


def copy_by_element(*args):
    try:
        source_list = args[0]
        if isinstance(source_list, list):
            new_list = []
            for i in range(len(source_list)):
                new_list.append(source_list[i])
            res = new_list
        else:
            res = []
    except Exception as e:
        res = []
        if debug_mode == "verbose":
            print(e)
    return res


sf.tests(copy_by_element)
