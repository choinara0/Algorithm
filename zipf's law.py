# f = open('/Users/choenara/Downloads/Les_Miserables-Victor_Hugo.txt', 'r')
#
# line = f.read().split()
# wordcount = {}
# for i in line:
#     i = i.lower()
#     i = i.replace(".", "")
#     i = i.replace(",", "")
#     i = i.replace("'", "")
#     i = i.replace("\"", "")
#     i = i.replace("!", "")
#     i = i.replace("?", "")
#     i = i.replace("(", "")
#     i = i.replace(")", "")
#     i = i.replace(";", "")
#     i = i.replace(":", "")
#     i = i.replace("-", "")
#
#     if i not in wordcount:
#         wordcount[i] = 1
#     else:
#         wordcount[i] += 1
# print(sorted(wordcount.items(), key=lambda x:x[1], reverse=True))

f = open('/Users/choenara/Downloads/Les_Miserables-Victor_Hugo.txt', 'w')
data = 'end of story'
f.write(data)
f.close()