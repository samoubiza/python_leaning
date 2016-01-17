"""read text in file and returns a 'word count' for each word in text in new file."""
with open('C:/Temp/python/google class/basic/alice.txt', 'r') as myfile:

    line = myfile.read().replace('/n','')


word_count_dict={}

for word in line.lower().split():

    if word not in word_count_dict:

        word_count_dict[word]=1

    else:

        word_count_dict[word] +=1


out=open('C:/Temp/python/google class/basic/result.txt','w')
for word in sorted(word_count_dict, key=word_count_dict.get, reverse=True):
##for word in sorted(word_count_dict, key=word_count_dict.get, reverse=True)[:20]:  ##retun only N elements of the dict
    print_str = word + ' ' + str(word_count_dict[word]) + '\n'
    out.write(print_str)

out.close()