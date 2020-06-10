from gensim.models import word2vec
import numpy as np

content = ['难道 ', '我', '也', '像', '游戏', '里面', '那样', '学会', '了','这个','技能','就','能','使用']
des1 = ['学习','知识经验','专业技术','能力','练习']    #个体运用已有的知识经验,通过练习而形成的一定的动作方式或智力活动方式。 [1]  指掌握并能运用专门技术的能力。指技术、能力。
des2 = ['《王者荣耀》','召唤师','腾讯','英雄']  #技能的另一个意思召唤师技能是腾讯公司天美工作室群研发的手游《王者荣耀》中每个玩家只要满足条件就能够拥有的，区别于英雄技能。
def word2():
    setences = word2vec.Text8Corpus("split.txt")
    model = word2vec.Word2Vec(setences)
    model.save("result.model")
    print(model.most_similar('技能'))

def w2v_mean(essay,model):
    ls=np.zeros(400)
    for unit in essay:
        try:
            ls+=np.array(model.wv[unit])
        except:
            pass
    return ls/len(essay)

if __name__ == '__main__':
    word2()
    model = word2vec.Word2Vec.load("result.model")
    content = w2v_mean(content, model)
    des1 = w2v_mean(des1, model)
    print(np.dot(des1,content)/(np.linalg.norm(des1)*np.linalg.norm(content)))
    des2 = w2v_mean(des2, model)
