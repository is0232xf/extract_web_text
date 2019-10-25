# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 23:33:55 2019

@author: User
"""

import nltk
import os
from nltk.corpus import wordnet as wn
from search_word_mean_on_web import search_on_weblio
from operator import itemgetter

nltk.download('all')
category_list = ["NN", "NNS", "VB", "VBG", "VBD", "VBN", "VBN", "VBP", "JJ", "RB"]
# category_list = ["NN", "VB"]

path = "./text/"
count = len(os.listdir(path))

input_file_list = []

def make_input_file_list():
    print(count)
    for i in range(count-1):
        i = i + 1
        file_name = "./text/text" + str(i) + ".txt"
        input_file_list.append(file_name)

def split_sentence(sentence):
    split_sentence = str(sentence)
    split_sentence = split_sentence.split(" ")
    return split_sentence

def exclude_special_characters(data_lines):
    data_lines = data_lines.replace("-", "")
    data_lines = data_lines.replace("-", "")
    data_lines = data_lines.replace(",", "")
    data_lines = data_lines.replace(".", "")
    data_lines = data_lines.replace("(", "")
    data_lines = data_lines.replace(")", "")
    data_lines = data_lines.replace("[", "")
    data_lines = data_lines.replace("]", "")
    data_lines = data_lines.replace("%", "")
    data_lines = data_lines.replace(":", "")
    data_lines = data_lines.replace(";", "")
    data_lines = data_lines.replace("&", "")
    data_lines = data_lines.replace("”", "")
    data_lines = data_lines.replace("“", "")
    data_lines = data_lines.replace("/", "")
    data_lines = data_lines.replace("'", "")
    return data_lines

make_input_file_list()

whole_data = []
large_whole_data = []
for input_text in input_file_list:
    with open(input_text, "r") as myfile:
        data=myfile.read()
        data = data.split('. ')
        large_whole_data = large_whole_data + data

        for i in range(len(data)):
            data[i] = data[i].lower()
        whole_data = whole_data + data

new_data = []

for sentence in whole_data:
    data = split_sentence(sentence)
    for num in range(len(data)):
        data[num] = exclude_special_characters(data[num])
        original_word = wn.morphy(data[num])
        if len(data[num]) > 2:
            if original_word == None:
                new_data.append(data[num])
            else:
                new_data.append(original_word)
        else:
            pass

fdist1 = nltk.FreqDist(new_data)

common_list = fdist1.most_common(1000) # 多い単語と数を出力
words = []
word_list = []

for i in range(len(common_list)):
    if common_list[i][1] > 2:
        word_list.append(common_list[i][0])
tagged_word_list = nltk.pos_tag(word_list[1:1000]) # 上位500をタグ付け
important_words = []

for j in range(len(tagged_word_list)):
    if tagged_word_list[j][1] in category_list:
        important_words.append(tagged_word_list[j]) # 必要な品詞タグが付いた単語だけを取り出す

word_result = []

for k in range(len(important_words)):
    word_result.append(important_words[k][0])

#print(word_result)

weblio_result = search_on_weblio(word_result)
#print(weblio_result)

sortted_list = sorted(weblio_result, key=itemgetter(2))
print(sortted_list)

"""
trans = Translator()

dictionaliy = []

for en_word in word_result:
    ja_word = trans.translate(en_word, dest="ja").text
    word_pair = (en_word, ja_word)
    dictionaliy.append(word_pair)

output_text_file = open("usage_list.txt", "w", encoding="utf-8")
star_line = "★★★★★★★★★★★★★★★★★★★★★★★★★"
sepa_line = "=============================================================================================="
new_line = "\n"

for target_word in word_result:
    output_text_file.write(new_line)
    output_text_file.write(new_line)
    output_text_file.write(star_line)
    output_text_file.write(new_line)
    output_text_file.write(target_word)
    output_text_file.write(new_line)
    output_text_file.write(star_line)
    output_text_file.write(new_line)
    for sentence in large_whole_data:
        small_sentence = sentence
        for i in range(len(small_sentence)):
            small_sentence = small_sentence.lower()
        if target_word in small_sentence:
            line = sentence + ". "
            output_text_file.write(line)
            output_text_file.write(new_line)
            output_text_file.write(sepa_line)
            output_text_file.write(new_line)
output_text_file.close()
output_text = "deck.tsv"
#print(word_pair)
with open(output_text, mode="w", encoding="utf-8") as f:
    for data in dictionaliy:
        data_line = data[0] + "\t" + data[1] + "\t" + "0" + "\t" + "0" + "\n"
        f.write(data_line)
"""