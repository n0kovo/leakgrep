import os
import sys
import subprocess
from tqdm import tqdm
import termcolor



string_to_find = sys.argv[1]
dir_to_search = sys.argv[2]
files = os.listdir(dir_to_search)


print
print termcolor.colored("[+] Searching for \"" + sys.argv[1] + "\":\n", "green", attrs=['bold', 'underline'])


def print_result(file, result):
    if len(result) > 3000:
        tqdm.write(termcolor.colored('String found in \"' + file + '\"', attrs=['bold', 'underline']))
        print termcolor.colored("(HUGE OUTPUT TRUNCATED TO 3000 CHARS!)", "red", attrs=['bold', 'underline'])
        tqdm.write(result[0:3000])
        tqdm.write('')

    else:

        if len(result) > 1:
            result = result.replace("\n", "").replace(string_to_find, termcolor.colored(string_to_find, 'red'))
            tqdm.write(termcolor.colored('String found in \"' + file + '\"', attrs=['bold', 'underline']))
            tqdm.write(result)
            tqdm.write('')

        else:
            pass


for file in tqdm(files):
    full_path = dir_to_search + file
    filename, file_extension = os.path.splitext(full_path)

    if file_extension.endswith(".zip"):
        p = subprocess.Popen(["zipgrep", string_to_find, full_path], stdout=subprocess.PIPE)
        result = p.communicate()[0].replace("\n", "")
        print_result(file, result)

    else:
        p = subprocess.Popen(["rg", "-z", string_to_find, full_path], stdout=subprocess.PIPE)
        result = p.communicate()[0].replace("\n", "")
        print_result(file, result)
