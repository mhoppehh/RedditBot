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

def adj_score(p_score, p_curve):
    if p_score == 0:
        return p_score
    return pow(p_score, (1 / float(p_score)) * pow(10, -1 * p_curve))
	
def dic_score(in_word, bias):
    percent = float(dic_percent(in_word))
    return (1 - (adj_score(percent) * bias))
    
def dic_score_def(in_word, p_curve):
    percent = float(dic_percent(in_word))
    return adj_score(percent, p_curve) / adj_score(float(dic_percent('the')), p_curve)