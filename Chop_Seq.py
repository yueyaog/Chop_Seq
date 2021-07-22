
import re
import argparse

parser = argparse.ArgumentParser(description="""
Seq_Chop.py takes a sequence file and it will split the long sequence in the file into required max length.

""")

parser.add_argument('-i','--input',dest='input_file_path',action="store",required=True,help="""
The input file is a sequence file.""")
parser.add_argument('-m','--maxLength',dest="maxLength",type=int,action='store',help="The max length of the sequence under each entry")
parser.add_argument('-o','--output',dest="output_file_path",action='store')
args = parser.parse_args()


with open(args.input_file_path) as file:
    seq = file.read()

scaffold_indexlist = re.findall('scaffold_[0-9]+',seq)


# Create a Dict for scaffold indexing
scaffold_Dict = {}
for i in seq.split('>'):
    for j in scaffold_indexlist:
        if j in i:
            scaffold_Dict[j] = re.sub('scaffold_[0-9]+','',i).strip()

# Create a fucntion to splice the string  based on maxlen 
def split_bylen(item, maxlen):
    split_list = [item[ind:ind+maxlen] for ind in range(0, len(item), maxlen)]
    return split_list

# Chop up the sequence based on the user input max length
max_len = args.maxLength
for key,val in scaffold_Dict.items():
    seq_len = len(val.strip())
    new_list = []
    if seq_len > max_len:
        for i in split_bylen(val,max_len):
            new_list.append(i)
    else:
        new_list.append(val)
    for count, value in enumerate(new_list):
        with open(args.output_file_path,'a') as file:
                content = file.write('\n>{}_chuck{}_{}bp\n'.format(key,count,len(value))+value)
