import numpy as np
import sys, getopt

def get_soundex_modified(word):
    word = word.upper()
    soundex = ""
    soundex += word[0]
    dictionary = {"BFPV": "1", "CGJKQSXZ":"2", "DT":"3", "L":"4", "MN":"5", "R":"6","EIY":"7","OU":"8","AHW":"."}
    for char in word[1:]:
        for key in dictionary.keys():
            if char in key:
                code = dictionary[key]
                if code != soundex[-1]:
                    soundex += code
    soundex = soundex.replace(".", "")
    soundex = soundex[:8].ljust(8, "0")
    return soundex

def get_clusters(cluster):
    return [['b','f','p','v'],['c','g','j','k','q','s','x','z'],['d','t'],['l'],['m','n'], ['r'],['e','i','y'],['o','u'],['a','h','w']][cluster - 1]

def get_random_chars(cluster):
    return np.random.choice(get_clusters(cluster), size = 1)[0]

def decode_soundex(soundex):
    s = ''
    for i in range(len(soundex)):
        if soundex[i] == '0':
            break
        elif soundex[i].isalpha():
            s += soundex[i]
        elif soundex[i].isdigit():
            s += get_random_chars(int(soundex[i]))
    return s

def get_gibberish(sentence):
    word_list = list(map(lambda word: decode_soundex(get_soundex_modified(word.strip())), sentence.split(' ')))
    return ' '.join(word_list)

if __name__ == '__main__':
    try:
        opts, args = getopt.getopt(sys.argv[1:],"w:",["word="])
    except getopt.GetoptError:
        print("python3 gibberish_generator.py -w <word>")
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-w", "--word"):
            print(get_gibberish(arg))
            sys.exit(0)
