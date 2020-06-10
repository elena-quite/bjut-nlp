import jieba
from math import log2
import string

# 频数统计
def tf(w,words):
    wordfrequency = {}
    for word in words:
        if w == word:
            wordfrequency[w] = wordfrequency.get(w, 0) + 1
    return wordfrequency.get(w, 0)

# 对示例句子分词
sent = '难道我也能够像游戏里面那样学会了这个技能就能使用 '
wsd_word = '技能'

jieba.add_word(wsd_word)
sent_cut = list(jieba.cut(sent, cut_all=False))

def dis_amb(file_name):
    f = open(file_name, "r", encoding='utf-8')
    result1 = []
    for line in f.readlines():
        line = line.split(" ")
        result1.extend(line)

    result = 0
    for cut in sent_cut:
        temp = tf(cut, result1)
        result = result + int(temp)

    return result

if __name__ == '__main__':
    result1 = dis_amb("split1.txt")
    result2 = dis_amb("split2.txt")
    print("该歧义句子各词语在词义1中出现：",result1,"次")
    print("该歧义句子各词语在词义2中出现：",result2,"次")

    if result1 > result2:
        print("句子中歧义词选第一种语义")
    if result1 < result2:
        print("句子中歧义词选第二种语义")





