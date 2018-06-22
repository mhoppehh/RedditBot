from collections import namedtuple
import os
from word_frequency import dic_score
from data_import import poll_reddit
from word_weight import *

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
            words = name.lower().split()
            
            #for word in words:
            #    print(word + " ", end="")
            #print()
            list_of_posts[i]=Post(name,url,score,words)

def create_master():
    for Post in list_of_posts:
        for word in Post.words:
            add_score(word, int(Post.score))
            
freq_bias = 7.00451340024
def_bias = 7
curve = 6
adj = 6.935583824

poll_reddit()

file_name= os.path.abspath('../bin/data.csv')
file_len=len_of_file(file_name)


Post = namedtuple("Post", "name url score words")
list_of_posts = [0] * len_of_file(file_name)

read_file(file_name)

create_master()

export_list()
export_list_adjusted_frequency(def_bias, curve)
