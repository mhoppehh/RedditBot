from collections import namedtuple

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
            
            list_of_posts[i]=Post(name,url,score)


file_name 	= 'bin\data.csv'
file_len	=len_of_file(file_name)

Post = namedtuple("Post", "name url score")
list_of_posts = [0] * len_of_file(file_name)

read_file(file_name)

