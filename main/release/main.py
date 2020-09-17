# papers_check
import jieba
import re
import math

#符号处理
filename1 = "orig.txt"
filename2 = "orig_0.8_rep.txt"
outfilename1 = "out1.txt"
outfilename2 = "out2.txt"
str1_ = open(filename1, 'r', encoding='UTF-8')
str2_ = open(filename2, 'r', encoding='UTF-8')
outputs1 = open(outfilename1, 'w', encoding='UTF-8')
outputs2 = open(outfilename2, 'w', encoding='UTF-8')

punc = '~`!#$%^&*()_+-=|\';":/.,?><~·！@#￥%……&*（）——+-=““：‘’；、。，？》《{}'

for line in str1_:
    line_seg = re.sub(r"[%s]+" %punc, "",line)
    outputs1.write(line_seg + '\n')
for line in str2_:
    line_seg = re.sub(r"[%s]+" %punc, "",line)
    outputs2.write(line_seg + '\n')

#读取原文和抄袭版论文到str1，str2中
str1 = open('out1.txt','rb').read()
str2 = open('out2.txt','rb').read()

#使用结巴分词与停用词表对str1,str2进行分词，将所有的词放在set中
cutwords = []
stops = open('stopwords.txt','r',encoding='utf-8-sig')
for oneword in stops:
    oneword = re.sub("\n","",oneword)   #将oneword中的'\n'替换为''
    cutwords.append(oneword)    #将该次放在cutwords的最后
stops.close()
str1_words = [i for i in jieba.cut(str1,cut_all=True) if (i not in cutwords) and i!='']
str2_words = [i for i in jieba.cut(str2,cut_all=True) if (i not in cutwords) and i!=''] #全模式切分
all_words = set(str1_words).union(set(str2_words)) #集合

#将str1,str2中的词进行编码
i = 0
#print(all_words)
word_dict = dict()  #创建字典
for word in all_words:
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

try:
    answer = round(float(sum)/(math.sqrt(item1)*math.sqrt(item2)),3)#返回浮点数四舍五入的值
except ZeroDivisionError:   #出现异常情况
    answer = 0.00
data = open("ans.txt",'w+')
print(filename1)
print(filename2)
print("余弦相似度 = %f"%answer)
#print("%f"%answer,file=data)
data.close()
