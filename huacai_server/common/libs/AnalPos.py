import jieba
import heapq
import random

def calculate(test):
    char_list = []
    # test = open('test.txt', 'r', encoding='utf-8')
    for line in test:
        for char in line:
            char_list.append(char)
    char_num = len(char_list)
    # print(char_num)

    # with open("test.txt", "r", encoding='utf-8') as test:
    #     test = test.read()
    #     print("例句: ",test)

    ##爱人得分
    emotion_dic = {}
    filename = 'wordCount_爱人.txt'
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


    seg_list = jieba.cut(test, cut_all=True)#True效果更好
    string = "/ ".join(seg_list)
    string_list = string.split('/')
    emotion_index = 0

    new_list = [i.strip() for i in string_list]
    # print("例句分词结果：",new_list)
    # print("爱人 dict:",emotion_dic)

    for count in range(len(new_list)):
        if new_list[count] in emotion_dic:
            # print(float(emotion_dic[new_list[count]]))
            emotion_index += float(emotion_dic[new_list[count]])

    # print("单项分数:")
    # print(emotion_index)


    ##爱上得分
    emotion_dic1 = {}
    filename = 'wordCount_爱上.txt'
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
    # print("爱上 dict:",emotion_dic1)

    seg_list = jieba.cut(test, cut_all=True)#True效果更好
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



    ##痴迷得分
    emotion_dic2 = {}
    filename = 'wordCount_痴迷.txt'
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
    # print("痴迷 dict:",emotion_dic2)

    seg_list = jieba.cut(test, cut_all=True)#True效果更好
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


    ##感动得分
    emotion_dic3 = {}
    filename = 'wordCount_感动.txt'
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
    # print("感动得分 dict:",emotion_dic3)

    seg_list = jieba.cut(test, cut_all=True)#True效果更好
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


    ##感谢得分
    emotion_dic4 = {}
    filename = 'wordCount_感谢.txt'
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
    # print("感谢 dict:",emotion_dic4)

    seg_list = jieba.cut(test, cut_all=True)#True效果更好
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

    ##快乐得分
    emotion_dic5 = {}
    filename = 'wordCount_快乐.txt'
    with open(filename, 'r', encoding = 'utf-8') as file:
        while True:
            try:
                senList = file.readline()
                # print(senList)        
                senList = senList[:-1] 
                senList = senList.split(' ')
                emotion_dic5[senList[0]] = senList[1]
            except IndexError:
                break
    # print("快乐 dict:",emotion_dic5)

    seg_list = jieba.cut(test, cut_all=True)#True效果更好
    string = "/ ".join(seg_list)
    string_list = string.split('/')
    emotion_index5 = 0

    new_list = [i.strip() for i in string_list]

    for count5 in range(len(new_list)):
        if new_list[count5] in emotion_dic5:
            # print(float(emotion_dic5[new_list[count5]]))
            emotion_index5 += float(emotion_dic5[new_list[count5]])

    # print("单项分数:")
    # print(emotion_index5)

    ##迷恋得分
    emotion_dic6 = {}
    filename = 'wordCount_迷恋.txt'
    with open(filename, 'r', encoding = 'utf-8') as file:
        while True:
            try:
                senList = file.readline()
                # print(senList)        
                senList = senList[:-1] 
                senList = senList.split(' ')
                emotion_dic6[senList[0]] = senList[1]
            except IndexError:
                break
    # print("迷恋 dict:",emotion_dic6)

    seg_list = jieba.cut(test, cut_all=True)#True效果更好
    string = "/ ".join(seg_list)
    string_list = string.split('/')
    emotion_index6 = 0

    new_list = [i.strip() for i in string_list]

    for count6 in range(len(new_list)):
        if new_list[count6] in emotion_dic6:
            # print(float(emotion_dic6[new_list[count6]]))
            emotion_index6 += float(emotion_dic6[new_list[count6]])

    # print("单项分数:")
    # print(emotion_index6)

    ##治愈得分
    emotion_dic7 = {}
    filename = 'wordCount_治愈.txt'
    with open(filename, 'r', encoding = 'utf-8') as file:
        while True:
            try:
                senList = file.readline()
                # print(senList)        
                senList = senList[:-1] 
                senList = senList.split(' ')
                emotion_dic7[senList[0]] = senList[1]
            except IndexError:
              break
    # print("治愈 dict:",emotion_dic7)

    seg_list = jieba.cut(test, cut_all=True)#True效果更好
    string = "/ ".join(seg_list)
    string_list = string.split('/')
    emotion_index7 = 0

    new_list = [i.strip() for i in string_list]

    for count7 in range(len(new_list)):
        if new_list[count7] in emotion_dic7:
            # print(float(emotion_dic7[new_list[count7]]))
            emotion_index7 += float(emotion_dic7[new_list[count7]])

    # print("单项分数:")
    # print(emotion_index7)

    ##正向意象得分
    emotion_dic8 = {}
    filename = 'wordCount_正向意象.txt'
    with open(filename, 'r', encoding = 'utf-8') as file:
        while True:
            try:
                senList = file.readline()
                # print(senList)        
                senList = senList[:-1] 
                senList = senList.split(' ')
                emotion_dic8[senList[0]] = senList[1]
            except IndexError:
                break
    # print("正向意象 dict:",emotion_dic8)

    seg_list = jieba.cut(test, cut_all=True)#True效果更好
    string = "/ ".join(seg_list)
    string_list = string.split('/')
    emotion_index8 = 0

    new_list = [i.strip() for i in string_list]

    for count8 in range(len(new_list)):
        if new_list[count8] in emotion_dic8:
            # print(float(emotion_dic8[new_list[count8]]))
            emotion_index8 += float(emotion_dic8[new_list[count8]])
    emotion_index8 = emotion_index8*0.1

    # print("单项分数:")
    # print(emotion_index8)

    # print("总分:")
    # print(emotion_index+emotion_index1+emotion_index2+emotion_index3+emotion_index4+emotion_index5+emotion_index6+emotion_index7+emotion_index8)

    type_1 = emotion_index+emotion_index1+emotion_index2+emotion_index8+emotion_index6
    type_2 = emotion_index3+emotion_index4+emotion_index5+emotion_index8
    type_3 = emotion_index7+emotion_index8


    list_1 = [emotion_index, emotion_index1, emotion_index2, emotion_index3, emotion_index4, emotion_index5, emotion_index6, emotion_index7, emotion_index8]
    list_2 = [type_1, type_2, type_3]


    prob_emo = map(list_1.index, heapq.nlargest(1, list_1))
    prob_type = map(list_2.index, heapq.nlargest(1, list_2))

    # print("最大可能情感: ",list(prob_emo)[0]+1)
    # print("情感细分种类: \n1.热恋 2.爱上 3.痴迷 4.感动 5.感谢 6.快乐 7.迷恋 8.治愈 9.略有正向情感")
    # print("级别: ",list(prob_type)[0]+1)

    # print(list_2[0],list_2[1],list_2[2])

    denominator = 10
    if (char_num >200):
        denominator = 20

    list_score = [i/denominator for i in list_2]
    # print(list_score)

    custom = random.randint(0 , 10000)

    # f = open('score.txt','a')#二进制，且会清除源文件
    # for num in range(0, 3):
    #     f.write(str(list_score[num]))
    #     f.write(" ")
    return list_score

def getscore():
    return list_score
