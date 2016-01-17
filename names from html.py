#-------------------------------------------------------------------------------
# Name:        модуль2
# Purpose:
#
# Author:      onovikov
#
# Created:     11.01.2016
# Copyright:   (c) onovikov 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

import os, re, json
dir_name = "C:/Temp/python/google class/babynames/"
for file in os.listdir(dir_name):
    if file.endswith(".html"):
        print(file)
        with open(dir_name+file, 'r') as myfile:
            array = []
            for line in myfile:
                array.append(line)
        names_dict = {}
        for line in array:
            if line.find('<tr align="right">' )==0:
                num_match = re.search(r'\d+', line)
                name_tuples = re.findall(r'([A-Z]\w+)<\/td><td>([A-Z]\w+)', line)
                names_dict[num_match.group()] = name_tuples[0]

        for line in array:
            if line.find('Popularity in' )>0:
                year_match = re.search(r'\d\d\d\d', line)
                names_dict['year'] = year_match.group()
                print(year_match.group())
        out=open('C:/Temp/python/google class/basic/result.txt','a')
        json.dump(names_dict, out)
        out.write('\n')
        out.write('\n')
        out.close()
