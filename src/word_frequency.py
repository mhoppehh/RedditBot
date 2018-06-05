import os

file_path = os.path.abspath('../bin/word_frequency.csv')

def dic_length():
    with open(file_path) as f:
        for i, l in enumerate(f):
            pass
    return i + 1
	
def dic_percent(in_word):
    with open(file_path) as f:
        for i, line in enumerate(f):
            line.split(",")
            f_word,per=line.split(",")
			
            if f_word.lower() == in_word.lower():
                return per
            pass
    return 0
	
def dic_score(in_word, bias):
    percent = float(dic_percent(in_word))
    return (1 - (percent * bias))