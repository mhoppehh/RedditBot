from collections import namedtuple
import os
from word_frequency import dic_score
from data_import import poll_reddit

freq_bias = 7.00451340024

def len_of_file(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1
	
def read_file(file):
    with open(file) as fp:
        for i, line in enumerate(fp):
            line.split(",")
            name,url,score=line.split(",")
            words = name.split()
            
            for word in words:
                print(word + " ", end="")
            print()
            list_of_posts[i]=Post(name,url,score,words)

poll_reddit()

file_name= os.path.abspath('../bin/data.csv')
file_len=len_of_file(file_name)


Post = namedtuple("Post", "name url score words")
list_of_posts = [0] * len_of_file(file_name)

read_file(file_name)

print(dic_score('the', freq_bias))

