import os
from word_frequency import dic_score_def

file_path = os.path.abspath('../bin/biases.csv')
adj_file_path = os.path.abspath('../bin/biases_adj_freq.csv')

class stru:
    def __init__(self):
        self.literal = ""
        self.score = 0


master_list = []

def add_score(p_literal, p_score):
    index = find_literal(p_literal)
    if index == -1:
        insert_Word(p_literal, p_score)
    else:
        master_list[index].score = (int(master_list[index].score) + int(p_score))

def find_literal(p_literal):
    for i, word in enumerate(master_list):
        t_literal = word.literal
        if p_literal == t_literal:
            return i
    return -1
    
def get_score(p_literal):
    for stru in master_list:
        t_literal = Word.literal
        if p_literal == t_literal:
            return int(stru.score)
    return -1
    
def insert_Word(p_literal, p_score):
    temp = stru()
    temp.literal = p_literal
    temp.score = p_score
    master_list.append(temp)
    
def print_list():
    master_list.sort(key=lambda x: x.score, reverse=True)
    for stru in master_list:
        print(stru.score)
    print(len(master_list))
    
def export_list():
    master_list.sort(key=lambda x: x.score, reverse=True)

    f= open(file_path,"w+")
    f.write("Word,Score\n")

    for stru in master_list:
        f.write('{},{}\n'.format(stru.literal,stru.score))

    f.close()
    
def export_list_adjusted_frequency(p_def_bias, p_curve):
    master_list.sort(key=lambda x: x.score, reverse=True)

    f= open(adj_file_path,"w+")
    f.write("Word,Score\n")

    for stru in master_list:
        f.write('{},{}\n'.format(stru.literal,stru.score*(1 - round(dic_score_def(stru.literal, p_curve), 10) )) )

    f.close()