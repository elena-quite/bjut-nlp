import jieba

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
    content = read_file("全能奇才.txt")
    for line in content:
        seg_list = jieba.cut(line, cut_all=False, HMM=True)
        fd1str = " ".join(seg_list)
        write_file("split.txt", fd1str)



if __name__ == '__main__':
    cutwords()