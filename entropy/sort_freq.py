import string

# 词频计算
def wordfre(words):
    wordfrequency = {}
    for word in words:
        wordfrequency[word] = wordfrequency.get(word, 0) + 1
    return wordfrequency

def sort_freq(file_name, sort_name):
    # 1、以空格为分割，将切好的词放入列表中
    f = open(file_name, "r", encoding='utf-8')
    content = f.readlines()
    list = []
    cnt = 0
    for i in range(0, content.__len__(), 1):
        for word in content[i].split():
            word = word.strip(string.whitespace)
            list.append(word)
            cnt = cnt + 1

    #获取词频表
    result = {}
    wordfrequency = wordfre(list)
    for word in wordfrequency.items():
        result[word[0]] = int(word[1]) / cnt
    #排序
    word_list = sorted(result.items(), key=lambda x:x[1], reverse=True)

    #写入sort.txt文件
    for single_word in word_list:
        f = open(sort_name, "a+", encoding="utf-8")
        line = str(single_word[0]) + ":" + str(single_word[1])
        f.write(line)
        f.write("\n")
        f.close()

if __name__ == '__main__':
    sort_freq("split.txt", "sort.txt")