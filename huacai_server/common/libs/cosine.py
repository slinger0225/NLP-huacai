import pandas as pd
import numpy as np

INT_BITS = 32
MAX_INT = (1 << (INT_BITS - 1)) - 1  # Maximum Integer for INT_BITS

def indi_count(df1,aaa):           #计算曲库中伪hash值的计数
    cursor = 0

    dataa = df1.loc[:, ['Indi']].values
    aaa = [0] * 256
    for cursor in range(0, 256):
        aaa[cursor] = np.sum(dataa == cursor)
    # print(aaa)
    return aaa


def binary_count(num):  # 一个二进制数有几个1
    count = 0
    bit = 1
    while num and bit <= MAX_INT + 1:
        if bit & num:
            count += 1
            num -= bit
        bit = bit << 1
    return count

def cosine(music_list,dist,cus_data,music_data):
    music_list.append(music_data[0])  # 记录选进去的music_id
    dist.append(np.dot(cus_data[1:8], music_data[2:9]) / (np.linalg.norm(cus_data[1:8]) * np.linalg.norm(music_data[2:9])))


def init_data(Song_addr,Cus_addr):
    df1 = pd.read_excel(Song_addr);
    """读取歌曲库"""
    df2 = pd.read_excel(Cus_addr);
    """读取用户库"""
    indi_list = []
    indi_list = indi_count(indi_list)  # 统计特征值的多少
    # print (indi_list)
    data = pd.DataFrame(df1)  # 将所有歌曲信息放进一个dataframe中（几百首歌可以用，多了要想别的）
    cus =pd.DataFrame(df2)  #同上


def recommend_one(data,cus_temp,indi_list):
    rec_list = [] #返回值容器
    dist_top = []
    dist_sec = []
    dist_rev = []
    music_list_top = []
    music_list_sec = []
    music_list_rev = []
    cus_rev = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(0, 3):
        cus_rev[i + 1] = cus_temp[4 + i]
        cus_rev[4 + i] = cus_temp[i + 1]
    cus_rev[0] = cus_temp[0]
    cus_rev[7] = cus_temp[7]
    cusarr = np.array(cus_temp[1:8])
    cusarr_rev = np.array(cus_rev[1:8])

    rec_list.append(int(cus_temp[0]))
    # print (cus_rev)
    # print (cusarr)
    cus_result = np.argsort(-cusarr)
    cus_result_rev = np.argsort(-cusarr_rev)

    indi = 0
    indi_rev = 0
    for k in range(0, 2):  # 取用户两个最高的特征值计算
        indi += 2 ** (6 - cus_result[k]);
        indi_rev += 2 ** (6 - cus_result_rev[k])
    # print(indi)
    cursor = 1
    while (cursor):  # 所有歌全部读取 读到没有其他歌
        try:
            data_temp = data.loc[cursor - 1].values
        except:
            # print('no more data')
            cursor = 0

        else:
            cursor += 1
            if indi_list[indi] >= 3:
                if binary_count(indi & int(data_temp[9])) == 2:
                    cosine(music_list_top, dist_top, cus_temp, data_temp)

                elif binary_count(indi & int(data_temp[9])) == 1:
                    cosine(music_list_sec, dist_sec, cus_temp, data_temp)
                elif binary_count(indi_rev & int(data_temp[9])) == 2:
                    cosine(music_list_rev, dist_rev, cus_rev, data_temp)
            else:
                if binary_count(indi & int(data_temp[9])) >= 1:
                    cosine(music_list_sec, dist_sec, cus_temp, data_temp)

    arr_top = np.array(dist_top)
    arr_sec = np.array(dist_sec)
    arr_rev = np.array(dist_rev)
    result_top = np.argsort(-arr_top)
    result_sec = np.argsort(-arr_sec)
    result_rev = np.argsort(-arr_rev);  # 返回从小到大的索引值
    """
    print('Totaly', (music_list_top.__len__() + music_list_sec.__len__() + music_list_rev.__len__()), 'music compared,',
          music_list_top.__len__(), 'perfectly matched, ', music_list_sec.__len__(), 'partially matched and',
          music_list_rev.__len__(), 'on contrast')
    """
    if music_list_top.__len__() >= 3:
        for i in range(0, 3):
            try:
                data_temp = data.loc[music_list_top[result_top[i]] - 1].values  # 部分计算版
                rec_list.append(data_temp[0])
            except:
                print('No more matched results')
                break

        for i in range(0, 3):
            try:
                data_temp = data.loc[music_list_sec[result_sec[i]] - 1].values  # 有hash
                # data = df1.loc[result_sec[i]].values  # 无hash
                rec_list.append(data_temp[0])
            # print(cus)
            except:
                print('No more matched results')
                break

        for i in range(0, 3):
            try:
                data_temp = data.loc[music_list_rev[result_rev[i]] - 1].values  # 随机版
                rec_list.append(data_temp[0])

            # print(cus)
            except:
                print('No more matched results')
                break
    else:
        for i in range(0, 6):
            try:
                data_temp = data.loc[music_list_sec[result_sec[i]] - 1].values  # 随机版
                rec_list.append(data_temp[0])

            # print(cus)
            except:
                print('No more matched results')
                break
    return rec_list

def main(mode,input_cus = '' ):
    Song_addr="/home/huacai/flask/huacai/huacai_server/common/libs/Song_database.xlsx"
    #Cus_addr='test.xls'
    df1 = pd.read_excel(Song_addr);
    """读取歌曲库"""
    #df2 = pd.read_excel(Cus_addr);
    """读取用户库"""
    indi_list = []
    indi_list = indi_count(df1,indi_list)  # 统计特征值的多少
    # print (indi_list)
    data = pd.DataFrame(df1)  # 将所有歌曲信息放进一个dataframe中（几百首歌可以用，多了要想别的）
    cus = pd.DataFrame(df1)  # 同上

    #init_data(Song_addr,Cus_addr)
    if mode==1:
        rec_list = []
        cursor=1
        while(cursor):
            try:
                cus_temp=cus.loc[cursor-1].values
               # print(cus_temp)
            except:
                cursor=0
            else:
                cursor+=1
                rec_list.append(recommend_one(data,cus_temp,indi_list))
                #print (rec_list)"""
    elif mode==2:
        rec_list = recommend_one(data,input_cus,indi_list)
    else:
        return 0
    return rec_list


