import jieba
import jieba.analyse
import codecs
from string import punctuation

def read_file(file_name):
    f = open(file_name, "r", encoding="utf-8")
    content = f.readlines()
    print(content)
    f.close()
    for i in range(len(content)):
        content[i] = content[i].rstrip("\n")
    return content

def write_file(file_name, content):
    f = open(file_name, "a+", encoding="utf-8")
    f.write(content)
    f.close()

#利用分词工具jieba，分词并写入split.txt
def cutwords():

    # 定义要删除的标点等字符
    add_punc = '，。、【 】 “”：；（）《》‘’{}？！⑦()、%^>℃：.”“^-——=&#@￥ …'
    all_punc = punctuation + add_punc

    f = codecs.open('2.txt', 'r', encoding="utf8")
    # 指定分词结果的保存文本
    target = codecs.open("split2.txt", 'w', encoding="utf8")

    line_num = 1
    line = f.readline()
    while line:
        # 第一次分词，用于移除标点等符号
        line_seg = " ".join(jieba.cut(line))
        # 移除标点等需要删除的符号
        testline = line_seg.split(' ')
        te2 = []
        for i in testline:
            te2.append(i)
            if i in all_punc:
                te2.remove(i)

        # 返回的te2是个list，转换为string后少了空格，因此需要再次分词
        line_seg2 = " ".join(jieba.cut(''.join(te2)))
        target.writelines(line_seg2)
        line_num = line_num + 1
        line = f.readline()
    f.close()
    target.close()

if __name__ == '__main__':
    cutwords()



