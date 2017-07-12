#coding=utf-8
import re

f = open("letter.txt",encoding="utf-8")
wc_map = {}
for item in f:
	#print(item)
	each_line_list = re.split(r'[,.! ]',item)
	for each_word in each_line_list:
		if len(each_word.strip())>0:
			wc_map[each_word]= wc_map.get(each_word,0) + 1
print(wc_map)
for key in wc_map.keys():
	print(key + " " + str(wc_map[key]))