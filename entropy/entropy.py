import math
import string

# 词频计算
def wordfre(words):
    wordfrequency = {}
    for word in words:
        wordfrequency[word] = wordfrequency.get(word, 0) + 1
    return wordfrequency

#二元词频（x,y)联合出现的次数
def bigramfre(words):
    wordfrequency = {}
    #两个联系在一起的词频
    for i in range(len(words) - 1):
        wordfrequency[(words[i], words[i+1])] = wordfrequency.get((words[i], words[i+1]),0)+1
    return wordfrequency

# 一元计算信息熵
def ca_entropy(file_name):

    # 1、以空格为分割，将切好的词放入列表中
    f = open(file_name, "r", encoding='utf-8')
    content = f.readlines()
    list = []
    for i in range(0, content.__len__(), 1):
        for word in content[i].split():
            word = word.strip(string.whitespace)
            list.append(word)

    # 2、计算分词的总个数
    cnt_words = len(list)

    # 3、获取每个词出现的次数
    wordfrequency = wordfre(list)

    # 4、一元模型公式 -p(x)*log(p(x))
    entropy = 0
    for single_word in wordfrequency.items():
        px = ((single_word[1]) / cnt_words)
        logpx = math.log(px, 2)
        temp = entropy
        entropy = (-px) * logpx
        entropy = entropy + temp
    print("一元模型的信息熵为：", entropy)
    print("\n")

    # 5、二元模型，-p（x，y) * log P(x|y)
    bigram = bigramfre(list)
    entropy = 0
    bigram_words = 0
    #统计x,y的总个数
    for single_word in bigram.items():
        temp = bigram_words
        bigram_words = single_word[1]
        bigram_words = bigram_words + temp

    for single_word in bigram.items():
        pxy = single_word[1] / bigram_words
        px_y = single_word[1] / wordfrequency[single_word[0][0]]
        logpx_y = math.log(px_y, 2)
        temp = entropy
        entropy = (-pxy) * logpx_y
        entropy = entropy + temp
    print("二元模型信息熵为：",entropy)

if __name__ == '__main__':
    ca_entropy("split.txt")
