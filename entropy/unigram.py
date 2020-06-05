import math
import string

def wordfre(words):
    wordfrequency = {}
    for word in words:
        wordfrequency[word] = wordfrequency.get(word, 0) +1
    return wordfrequency.items()

def ca_entropy(file_name):

    #1、以空格为分割，将切好的词放入列表中
    f = open(file_name, "r", encoding='utf-8')
    content = f.readlines()

    list = []
    for i in range(0, content.__len__(), 1):
        for word in content[i].split():
            word = word.strip(string.whitespace)
            list.append(word)

    #2、计算分词的总个数
    cnt_words = len(list)

    #3、获取每个词出现的次数
    wordfrequency = wordfre(list)

    entropy = 0
    #4、一元模型公式 -p(x)*log(p(x))
    for single_word in wordfrequency:
        px = ((single_word[1])/cnt_words)
        logpx = math.log(px, 2)
        temp = entropy
        entropy = (-px) * logpx
        entropy = entropy + temp

    print("一元模型的信息熵为：",entropy)




if __name__ == '__main__':
    ca_entropy("split.txt")