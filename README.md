# Chop_Seq
Some online resources limit the size of users queries, so users need to split the original sequence file into a set of smaller files. There are some solutions available for this problem, but they always require installing additional packages which might be an exhausting process. Chop_Seq offers some simply python solutions to solve your problem. No dependencies is required for running Chop_Seq.py. It takes a sequence fasta file and it will split the long sequence into required max length. 

Note: To avoid run out the memory of your own precious computer while processing large sequence file, I recommend you to use Chop_Seq on HPC clusters. 

## Test
Chop_Seq.py takes a sequence fasta file and it will split the long sequence in the file into required max length.

You can test this script using the ```Test.fa``` file.

```
python Chop_Seq.py -i Test.fa -m 15000 -o Test_parsed.fa
```
The output index is >scaffold_n_[chuck_index]_[length in bp]

## Command for running Chop_Seq.py
```
python Chop_Seq.py -i /path/to/input.fa -m [maxlength] -o /path/to/output.fa
```


## Details
```
python Chop_Seq.py -h
```