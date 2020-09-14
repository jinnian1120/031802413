# papers_check
import jieba
import re
import math


#读取原文和抄袭版论文到str1，str2中
str1 = open('orig.txt','rb').read()
str2 = open('orig_0.8_dis_1.txt','rb').read()

#使用结巴分词对str1,str2进行分词，将所有的词放在set中
cutwords = []
stops = open('stop_words.txt','r',encoding='utf-8-sig')
for oneword in stops:
    oneword = re.sub("\n","",oneword)   #将oneword中的'\n'替换为''
    cutwords.append(oneword)    #将该次放在cutwords的最后
stops.close()
str1_words = [i for i in jieba.cut(str1,cut_all=True) if (i not in cutwords) and i!='']
str2_words = [i for i in jieba.cut(str2,cut_all=True) if (i not in cutwords) and i!=''] #全模式切分
all_words = set(str1_words).union(set(str2_words)) #集合

#将str1,str2中的词进行编码
i = 0
word_dict = dict()  #创建字典
for word in all_words:
#    print(all_words)
    word_dict[word] = i
    i = i+1

#计算str1,str2中每个词出现的次数
str1_words_code = [0]*len(word_dict)

for word in str1_words:
    str1_words_code[word_dict[word]]+=1

str2_words_code = [0]*len(word_dict)
for word in str2_words:
    str2_words_code[word_dict[word]]+=1

#计算余弦值并输出结果
item1 = 0
item2 = 0
sum = 0
for i in range(len(str1_words_code)):
    sum += str1_words_code[i]*str2_words_code[i]
    item1 += pow(str1_words_code[i],2)
    item2 += pow(str2_words_code[i],2)

answer = round(float(sum)/(math.sqrt(item1)*math.sqrt(item2)),3)#返回浮点数四舍五入的值
print("%f"%answer)
