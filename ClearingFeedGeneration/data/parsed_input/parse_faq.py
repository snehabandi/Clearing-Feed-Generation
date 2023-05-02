# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 18:39:19 2018

@author: sneha
"""

f=open('bank_faqs.json', 'r', encoding='utf-8')#encoding needs to be specified 
#https://stackoverflow.com/questions/49562499/how-to-fix-unicodedecodeerror-charmap-codec-cant-decode-byte-0x9d-in-positine = ""
# use readline() to read the first line 
# If the file is not empty keep reading one line
# at a time, till the file is empty
line = " "
questions = [""]
answers = [""]
i=0
while line:
    # in python 2+
    # print line
    # in python 3 print is a builtin function, so
    # use realine() to read next line
    line = str(f.readline())#.split("")
    if i%2==0:
        questions.append(line)
    else:
        answers.append(line)
    print(line)
    i+=1
f.close()#lines = f.readlines()
#json_decode=json.loads(input_file)
#for item in json_decode:

f = open("faq_questions.txt","w+")
for question in questions:
    f.write(question)
f.close()
f = open("faq_answers.txt","w+")
for answer in answers:
    f.write(answer)
f.close()
print("END")
