from common.libs.AnalNeg import calculate as calculateNeg
from common.libs.AnalPos import calculate as calculatePos
from common.libs.AnalNeutral import calculate as calculateNeu
#from common.libs.cosine import main as cosine
from common.libs.cosine_neo import main as cosine
import pandas as pd
import xlrd
import heapq

def sent_rec(content):#传入用户的id，用户文本内容
	'''计算用户情感得分'''
	all_list = []
	all_list.append(int(0))

	neg_p = calculateNeg(content)#计算三个得分
	pos_p = calculatePos(content)
	neu_p = calculateNeu(content)

	for item in neg_p:
		all_list.append(item)
	for item in pos_p:
		all_list.append(item)
	all_list.append(neu_p)
	# print(all_list)#包括用户id和7个分数



	reco = []  # 推荐结果
	#df2 = pd.read_excel('test.xls');
	# cus_temp = df2.loc[0].values
	# print (cus_temp)
	cus_temp = all_list
	# print(cus_temp)
	# print(cosine.main(1))    #从本机xls读取客户
	# print(cosine.main(2,cus_temp)) #传递客户情况 包括Customer_ID	Lovelorn	Stressed	Lonely	Romantic	Encourage	Accompany	Peaceful

	""" 全部梳理xls版
    for item in cosine.main(2,cus_temp):
        if item[0] == int(cus_id):
            reco = item[1:]
    """
	item = cosine(2, cus_temp)
	item[0] == int(0)
	reco = item[1:]

	'''POST推荐结果'''
	xls_songinfo = xlrd.open_workbook('/home/huacai/flask/huacai/huacai_server/common/libs/song_info.xls')
	songsheet = xls_songinfo.sheet_by_index(0)
	#song_num = songsheet.col_values(0)
	# song_num = song_num[1:]
	# song_num = [int(x) for x in song_num]
	
	reco_all = []
	for items in reco:
		com_list = {}
		com_list.update(lovelorn=songsheet.cell(items, 1).value)
		com_list.update(stressed=songsheet.cell(items, 2).value)
		com_list.update(lonely=songsheet.cell(items, 3).value)
		com_list.update(romantic=songsheet.cell(items, 4).value)
		com_list.update(encourage=songsheet.cell(items, 5).value)
		com_list.update(accompany=songsheet.cell(items, 6).value)
		com_list.update(peaceful=songsheet.cell(items, 7).value)
		com_list.update(song_num=songsheet.cell(items, 14).value)
		com_list.update(song_name=songsheet.cell(items, 16).value)
		reco_all.append(com_list)

	sentiment = all_list[1:]
	max_sentiment = map(sentiment.index, heapq.nlargest(1, sentiment))
	sent = ['Lovelorn', 'Stressed', 'Lonely', 'Romantic', 'Encourage', 'Accompany', 'Peaceful']
	reco_dict = {str("music_info"): reco_all, "customer_emotion":cus_temp, 'sentiment': sent[list(max_sentiment)[0]]}
	return reco_dict


# o = sent_rec(209,'我没有写完，但是如果写完可以去开心一下')
# print(o)

