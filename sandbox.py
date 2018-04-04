import os
import re

def fixdata(filename):
    if not os.path.exists(".\\new"):
        os.makedirs(".\\new")
    file = open(filename, 'r')
    newfile = open(".\\new\\"+filename, 'w')

    data = file.readlines()
    newdata = re.sub(r',[\w \.]+? / (\d+?).*', r',\1', data)
    newfile.writelines(newdata)

