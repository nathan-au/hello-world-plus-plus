import string
import time

alphabet = list(string.ascii_lowercase)
target = input("what is the target? ")
target_list = list(target)
complete = ""

for l in target_list:
    for a in alphabet:
        print(complete + a)
        if a == l:
            break
        time.sleep(0.04)
    complete = complete + l