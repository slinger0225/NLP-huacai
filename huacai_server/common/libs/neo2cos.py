import neo4j
from py2neo import Graph,Node, Relationship,NodeMatcher,RelationshipMatcher,PropertyDict,walk,Schema
import pandas as pd
import numpy as np

##连接neo4j数据库，输入地址、用户名、密码
graph = Graph('http://62.234.47.77:7474',username='neo4j',password='huacai@123')

#建立结点(输一次建立一次，少输)
#a=Node('Movie',Title='Star Wars',Year=1997,Score=9.757)
#graph.create(a)
matcher=NodeMatcher(graph)
Rmatcher=RelationshipMatcher(graph)
#建立结点和关系
"""a=Node('Person',Name='Elsa',Age=22)
b=Node('Person',Name='Lily',age=39)
graph.create(a)
graph.create(b)
r=Relationship(a,'KNOWS',b)
graph.create(r)
"""

def add_songs(id,name,author,a1,a2,a3,a4,a5,a6,a7):
    cus = [a1,a2,a3,a4,a5,a6,a7]
    #indi=  indicator_gen(cus)
    a=Node("Song",Id=id,Name=name,Author=author,Lovelorn=a1,Stressed=a2,Lonely=a3,Romantic=a4,Encourage=a5,Accompany=a6,Peaceful=a7)
    graph.create(a)
    return a

def create_r(a,relation,b):

    #a = matcher.match("Song").where('_.Id=1').first()
    aa =64
    #b = matcher.match("Attribute").where('_.Indi=' + str(aa)).first()  # finding node
    r = Relationship(a,relation, b)
    graph.create(r)


def create_songs(data):
    #a = Node("Song", Id=id, Name=name, Author=author, Lovelorn=a1, Stressed=a2, Lonely=a3, Romantic=a4, Encourage=a5,
          #  Accompany=a6, Peaceful=a7)
    #graph.create(a)
    a = Node()
    a=add_songs(int(data[0]), str(data[1]), 'None', float(data[2]), float(data[3]), float(data[4]), float(data[5]), float(data[6]), float(data[7]), float(data[8]))
    #print (a)
    sb = np.array(data[2:9])
    #print(sb)
    res = np.argsort(-sb)
    aa=2**(6-res[0])
    b = matcher.match("Attribute").where('_.Indi='+str(aa)).first()# finding node
    create_r(a, "First",b)
    bb = 2 ** (6 - res[1])
    c = matcher.match("Attribute").where('_.Indi=' + str(bb)).first()  # finding node
    create_r(a,"Second",c)

"""类型的link做不了，暂时不做"""
def create_user(id,name,attri1="None",attri2="None",attri3="None",attri4="None",attri5="None",attri6="None"):
    a=Node("User",Id=id,Name=name,attri1=attri1,attri2=attri2,attri3=attri3,attri4=attri4,attri5=attri5,attri6=attri6)
    graph.create(a)
    attri=[attri1,attri2,attri3,attri4,attri5,attri6]
    for item in attri:
        try:
            typpe=matcher.match("Type").where('_.Name='+str(item)).first()
        except:
            continue
        else:
            create_r(a,'Likes',typpe)


def strip_data(record):
    song_data=[]
    for sb in record:
        line=sb[0]
        data=[line["Id"],line["Lovelorn"],line["Stressed"],line["Lonely"],line["Romantic"],line["Encourage"],line["Accompany"],line["Peaceful"]]
        song_data.append(data)
    return song_data

def find_songs(cus):  #cus在这里面只包括一个id+七个情感值
    """第一步找cus最高的两个attri
        然后找两个attri对应的结点
        从这两个结点找中心结点
        返回做cosine
        第二步从其中一个attri遍历结点，但不包含一
        返回结点的list
        最后从attri的64/2**attri找两个结点
        返回结点"""
    so=np.array(cus[1:8])
    res = np.argsort(-so)
    first = 2**(6-res[0])
    second = 2**(6-res[1])
    comp_list=[]
    comp_list_sec = []
    comp_list_rev = []
    comp_list=list(graph.run("match (a:Attribute) --(c:Song)--(b:Attribute) where a.Indi="+str(first)+" and b.Indi="+str(second)+" return c"))
    #comp_list.append(aa)
    comp_list_sec=list(graph.run("match (a:Attribute) --(c:Song) where a.Indi="+str(first)+" or a.Indi="+str(second)+" return c"))
    comp_list_rev=list(graph.run("match (a:Attribute) --(c:Song)--(b:Attribute) where a.Indi="+str(128/first)+" and b.Indi="+str(64/second)+" return c"))
    comp_list=strip_data(comp_list)
    comp_list_sec = strip_data(comp_list_sec)
    comp_list_rev = strip_data(comp_list_rev)
    comp_list_sec=[v for v in comp_list_sec if v not in comp_list]  # 给comp_list_sec去重
    if len(comp_list_rev)+len(comp_list)+len(comp_list_sec)<=9:
        comp_list = strip_data(list(graph.run(
            "match (c:Song) return c")))
        comp_list_sec=[]
        comp_list_rev=[]
    return comp_list,comp_list_sec,comp_list_rev

def add_recom(rec_list):
    cus_id=rec_list[0]
    cus = matcher.match("User").where("_.Id="+str(rec_list[0])).first()
    create_r(cus,"Recommended",)
    for item in rec_list[1:]:
        try:
            a =matcher.match("Song").where("_.Id="+str(item)).first()
            create_r(cus,"Inclueded",a)
        except:
            print("rec_list fail")

"""
#a=Node("Type",Name="Jazz")
b=Node("Type",Name="Pop")
c=Node("Type",Name="Blues")
d=Node("Type",Name="R&B")
e=Node("Type",Name="Country")
f=Node("Type",Name="Rap")
g=Node("Type",Name="Rock")

sb={a,b,c,d,e,f,g}
for item in sb:
    graph.create(item)


pd1 =pd.read_excel('song_info.xls')
#print(pd1)


for i in range(0,70):

    data=pd1.loc[i].values
    print (data)

    create_songs(data)
    i+=1
    if data==[]:
       break
#create_r()

"""
