'''
This scripts counts the letters and its usage frequancy in a given sentence.
'''
user_sentence = input('Please write down a sentence: ')

counter = 0
lenght = len(user_sentence)
sentence_dict = {}

for i in user_sentence:
    keys = sentence_dict.keys()
    if i in keys:
        sentence_dict[i] += 1
    else:
        sentence_dict[i] = 1
print (sentence_dict)