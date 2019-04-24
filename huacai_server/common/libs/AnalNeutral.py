import jieba
import heapq


def calculate(test):
    char_list = []
    # test = open('test.txt', 'r', encoding='utf-8')
    for line in test:
        for char in line:
            char_list.append(char)
    char_num = len(char_list)
    # print(char_num)

    # with open("test.txt", "r", encoding='utf-8') as text:
    #     test = text.read()
    #     print("例句: ",test)

    ##平静得分
    emotion_dic = {}
    filename = '/home/huacai/flask/huacai/huacai_server/common/libs/wordCount_平静.txt'
    with open(filename, 'r', encoding = 'utf-8') as file:
        while True:
            try:
                senList = file.readline()
                # print(senList)        
                senList = senList[:-1] 
                senList = senList.split(' ')
                emotion_dic[senList[0]] = senList[1]
            except IndexError:
                break


    seg_list = jieba.cut(test, cut_all=False)#True效果更好
    string = "/ ".join(seg_list)
    string_list = string.split('/')
    emotion_index = 0

    new_list = [i.strip() for i in string_list]
    # print("例句分词结果：",new_list)
    # print("平静 dict:",emotion_dic)

    for count in range(len(new_list)):
        if new_list[count] in emotion_dic:
            # print(float(emotion_dic[new_list[count]]))
            emotion_index += float(emotion_dic[new_list[count]])

    # print("单项分数:")
    # print(emotion_index)


    ##洒脱得分
    emotion_dic1 = {}
    filename = '/home/huacai/flask/huacai/huacai_server/common/libs/wordCount_洒脱.txt'
    with open(filename, 'r', encoding = 'utf-8') as file:
        while True:
            try:
                senList = file.readline()
                # print(senList)        
                senList = senList[:-1] 
                senList = senList.split(' ')
                emotion_dic1[senList[0]] = senList[1]
            except IndexError:
                break
    # print("洒脱 dict:",emotion_dic1)

    seg_list = jieba.cut(test, cut_all=False)#True效果更好
    string = "/ ".join(seg_list)
    string_list = string.split('/')
    emotion_index1 = 0

    new_list = [i.strip() for i in string_list]



    for count1 in range(len(new_list)):
        if new_list[count] in emotion_dic1:
            # print(float(emotion_dic1[new_list[count1]]))
            emotion_index1 += float(emotion_dic1[new_list[count1]])

    # print("单项分数:")
    # print(emotion_index1)



    ##释然得分
    emotion_dic2 = {}
    filename = '/home/huacai/flask/huacai/huacai_server/common/libs/wordCount_释然.txt'
    with open(filename, 'r', encoding = 'utf-8') as file:
        while True:
            try:
                senList = file.readline()
                # print(senList)        
                senList = senList[:-1] 
                senList = senList.split(' ')
                emotion_dic2[senList[0]] = senList[1]
            except IndexError:
                break
    # print("释然 dict:",emotion_dic2)

    seg_list = jieba.cut(test, cut_all=False)#True效果更好
    string = "/ ".join(seg_list)
    string_list = string.split('/')
    emotion_index2 = 0

    new_list = [i.strip() for i in string_list]

    for count2 in range(len(new_list)):
        if new_list[count2] in emotion_dic2:
            # print(float(emotion_dic2[new_list[count2]]))
            emotion_index2 += float(emotion_dic2[new_list[count2]])

    # print("单项分数:")
    # print(emotion_index2)


    ##自由得分
    emotion_dic3 = {}
    filename = '/home/huacai/flask/huacai/huacai_server/common/libs/wordCount_自由.txt'
    with open(filename, 'r', encoding = 'utf-8') as file:
        while True:
            try:
                senList = file.readline()
                # print(senList)        
                senList = senList[:-1] 
                senList = senList.split(' ')
                emotion_dic3[senList[0]] = senList[1]
            except IndexError:
                break
    # print("自由 dict:",emotion_dic3)

    seg_list = jieba.cut(test, cut_all=False)#True效果更好
    string = "/ ".join(seg_list)
    string_list = string.split('/')
    emotion_index3 = 0

    new_list = [i.strip() for i in string_list]

    for count3 in range(len(new_list)):
        if new_list[count3] in emotion_dic3:
            # print(float(emotion_dic3[new_list[count3]]))
            emotion_index3 += float(emotion_dic3[new_list[count3]])

    # print("单项分数:")
    # print(emotion_index3)


    ##中性意象得分
    emotion_dic4 = {}
    filename = '/home/huacai/flask/huacai/huacai_server/common/libs/wordCount_中性意象.txt'
    with open(filename, 'r', encoding = 'utf-8') as file:
        while True:
            try:
                senList = file.readline()
                # print(senList)        
                senList = senList[:-1] 
                senList = senList.split(' ')
                emotion_dic4[senList[0]] = senList[1]
            except IndexError:
                break
    # print("中性意象 dict:",emotion_dic4)

    seg_list = jieba.cut(test, cut_all=False)#True效果更好
    string = "/ ".join(seg_list)
    string_list = string.split('/')
    emotion_index4 = 0

    new_list = [i.strip() for i in string_list]

    for count4 in range(len(new_list)):
        if new_list[count4] in emotion_dic4:
            # print(float(emotion_dic4[new_list[count4]]))
            emotion_index4 += float(emotion_dic4[new_list[count4]])

    # print("单项分数:")
    # print(emotion_index4)

    # print("总分:")
    # print(emotion_index+emotion_index1+emotion_index2+emotion_index3+emotion_index4)


    list_1 = [emotion_index, emotion_index1, emotion_index2, emotion_index3, emotion_index4]

    prob_emo = map(list_1.index, heapq.nlargest(2, list_1))

    div = 10
    if(char_num>300):
        div = 20
    if(char_num>500):
        div = 30
    return (emotion_index+emotion_index1+emotion_index2+emotion_index3+emotion_index4)/div

    # print("最大可能情感: ",list(prob_emo)[0]+1)#list中输出最大项
    # print("情感细分种类: \n1.平静 2.洒脱 3.释然 4.自由 5.情感总体呈中性")


    # f = open('score.txt','a')#二进制，追加
    # f.write(str((emotion_index+emotion_index1+emotion_index2+emotion_index3+emotion_index4)/10))#write() argument must be str
    # f.write("\n")

def getscore():
    return (emotion_index+emotion_index1+emotion_index2+emotion_index3+emotion_index4)/10
