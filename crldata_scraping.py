#ライブラリのインストール
from bs4 import BeautifulSoup
import requests
import pandas as pd

#デッキ名を求める関数

list1 = []
list2 = []

def deckname1(set):

  if "three-musketeers" in list1:
    DN1 = "三銃士"

  elif "golem" in list1:
    DN1 = "ゴーレム"

  elif "pekka" in list1:
    if "ram-rider" in list1:
      DN1 = "ペッカラム"
    else:
      DN1 = "ペッカ"

  elif "lava-hound" in list1:
    DN1 = "ラバ"

  elif "royal-giant" in list1:
    DN1 = "ロイジャイ"

  elif "goblin-giant" in list1:
    DN1 = "ゴブジャイ"

  elif "giant-skeleton" in list1:
    DN1 = "巨大スケルトン"

  elif "giant" in list1:
    DN1 = "ジャイアント"

  elif "x-bow" in list1:
    DN1 = "クロスボウ"

  elif "balloon" in list1:
    DN1 = "バルーン"

  elif "royal-hog" in list1:
    DN1 = "ロイヤルホグ"

  elif "ram-rider" in list1:
    DN1 = "ラムライダー"

  elif "graveyard" in list1:
    DN1 = "スケルトンラッシュ"

  elif "mortar" in list1:
    DN1 = "迫撃"

  elif "hog-rider" in list1:
    DN1 = "ホグ"

  elif "miner" and "poison" in list1:
    DN1 = "ディガポイ"

  elif "goblin-barrel" and "princess" in list1:
    DN1 = "枯渇"

  elif "lumberjack" and "royal-ghost" and "'battle-ram" in list1:
    DN1 = "神器"

  elif "dark-prince" and "bandit" and "'battle-ram" in list1:
    DN1 = "神器"

  else:
    DN1 = "その他"

  return DN1


##DN2を求める関数

#list1 = list1_1 + list1_2
#list2 = list2_1 + list2_2

def deckname2(set):


  if "three-musketeers" in list2:
    DN2 = "三銃士"

  elif "golem" in list2:
    DN2 = "ゴーレム"

  elif "pekka" in list2:
    if "ram-rider" in list2:
      DN2 = "ペッカラム"
    else:
      DN2 = "ペッカ"

  elif "lava-hound" in list2:
    DN2 = "ラバ"

  elif "royal-giant" in list2:
    DN2 = "ロイジャイ"

  elif "goblin-giant" in list2:
    DN2 = "ゴブジャイ"

  elif "giant-skeleton" in list2:
    DN2 = "巨大スケルトン"

  elif "giant" in list2:
    DN2 = "ジャイアント"

  elif "x-bow" in list2:
    DN2 = "クロスボウ"

  elif "balloon" in list2:
    DN2 = "バルーン"

  elif "royal-hog" in list2:
    DN2 = "ロイヤルホグ"

  elif "ram-rider" in list2:
    DN2 = "ラムライダー"

  elif "graveyard" in list2:
    DN2 = "スケルトンラッシュ"

  elif "mortar" in list2:
    DN2 = "迫撃"

  elif "hog-rider" in list2:
    DN2 = "ホグ"

  elif "miner" and "poison" in list2:
    DN2 = "ディガポイ"

  elif "goblin-barrel" and "princess" in list2:
    DN2 = "枯渇"

  elif "lumberjack" and "royal-ghost" and "'battle-ram" in list2:
    DN2 = "神器"

  elif "dark-prince" and "bandit" and "'battle-ram" in list2:
    DN2 = "神器"

  else:
    DN2 = "その他"

  return DN2

##set=2の時



DN1 = deckname1(set)
DN2 = deckname2(set)

#df_CRLdata["DeckName1"] = DN1
#df_CRLdata["DeckName2"] = DN2

#df_CRLdata

#試合データ取得する取得する関数の作成

def getCRLdata(we,ma,set):
  df_all = pd.DataFrame()
  list1_1=[]
  list1_2=[]
  list2_1=[]
  list2_2=[]
  ga=1

  index=["week","match","set","game","team1","team2","player1_1","player1_2","player2_1","player2_2","game winner","ban1","ban2","deck1_1","deck1_2","deck2_1","deck2_2","DeckName1","DeckName2"]

###ゲーム1の時
  url="https://royaleapi.com/crl/2019/battles?region=asia&season=spring&week=%d&match=%d&set=%d" % (we,ma,set)
  html_doc = requests.get(url).text
  soup=BeautifulSoup(html_doc,"html.parser")

  tag3 = soup.find_all("a")[76]
  tag4 = soup.find_all("a")[77]
  tag5 = soup.find_all("a")[78]
  if we==8:
    if ma == 3:
      if "card" in soup.find_all("a")[71].get("href"):
        ban1 = soup.find_all("a")[70].get("href")[6:]
        ban2 = soup.find_all("a")[71].get("href")[6:]
      else:
        pass
    else:
      if "card" in soup.find_all("a")[71].get("href"):
        ban1 = soup.find_all("a")[71].get("href")[6:]
        ban2 = soup.find_all("a")[72].get("href")[6:]
      else:
        pass
  else:

    if "019" in tag5.get("href")[6:]:
      ban1 = tag3.get("href")[6:]
      ban2 = tag4.get("href")[6:]
    else:
      ban1 = tag4.get("href")[6:]
      ban2 = tag5.get("href")[6:]



  tag5 = soup.find_all("img")[7]
  team1 = tag5.get("src")[25:].split('.')[0]
  tag6 = soup.find_all("img")[11]
  team2 = tag6.get("src")[25:].split('.')[0]


  if set==1:

    pl1_1 = soup.find_all("a",{"class":"player_name_header"})[0].string
    pl1_2 = soup.find_all("a",{"class":"player_name_header"})[1].string
    pl2_1 = soup.find_all("a",{"class":"player_name_header"})[2].string
    pl2_2 = soup.find_all("a",{"class":"player_name_header"})[3].string

    win1 = soup.find_all("div")[142].text
    if "Blue" in win1:
      winner1=1
    else:
      winner1=2

    for num in range(14,22):
      tag = soup.find_all("img")[num]
      a = tag.get("alt")
      list1_1.append(a)

    for num in range(22,30):
      tag = soup.find_all("img")[num]
      a = tag.get("alt")
      list1_2.append(a)

    for num in range(30,38):
      tag = soup.find_all("img")[num]
      a = tag.get("alt")
      list2_1.append(a)

    for num in range(38,46):
      tag = soup.find_all("img")[num]
      a = tag.get("alt")
      list2_2.append(a)

    list1 = list1_1 + list1_2
    list2 = list2_1 + list2_2
    DN1 = deckname1(set)
    DN2 = deckname2(set)

  elif set==2:
    pl1_1 = soup.find_all("a",{"class":"player_name_header"})[0].string
    pl2_1 = soup.find_all("a",{"class":"player_name_header"})[1].string
    pl1_2 = None
    pl2_2 = None

    win1 = soup.find_all("div")[143].text
    if "Blue" in win1:
      winner1=1
    else:
      winner1=2

    for num in range(14,22):
      tag = soup.find_all("img")[num]
      a = tag.get("alt")
      list1_1.append(a)

    for num in range(22,30):
      tag = soup.find_all("img")[num]
      a = tag.get("alt")
      list2_1.append(a)

    list1_2 = None
    list2_2 = None

    list1 = list1_1
    list2 = list2_1
    DN1 = deckname1(set)
    DN2 = deckname2(set)

  elif set==3:
    pl1_1 = soup.find_all("a",{"class":"player_name_header"})[0].string
    pl2_1 = soup.find_all("a",{"class":"player_name_header"})[1].string
    pl1_2 = None
    pl2_2 = None

    win1 = soup.find_all("div")[143].text
    if "Blue" in win1:
      winner1=1
    else:
      winner1=2

    for num in range(14,22):
      tag = soup.find_all("img")[num]
      a = tag.get("alt")
      list1_1.append(a)

    for num in range(22,30):
      tag = soup.find_all("img")[num]
      a = tag.get("alt")
      list2_1.append(a)

    list1_2 = None
    list2_2 = None

    list1 = list1_1
    list2 = list2_1
    DN1 = deckname1(set)
    DN2 = deckname2(set)

  else:
    print("Error")


  se = pd.Series([we,ma,set,ga,team1,team2,pl1_1,pl1_2,pl2_1,pl2_2,winner1,ban1,ban2,list1_1,list1_2,list2_1,list2_2,DN1,DN2])
  df_all = df_all.append(se,ignore_index = True)
  df_all = df_all.rename(columns={0:"week",1:"match",2:"set",3:"game",4:"team1",5:"team2",6:"player1_1",7:"player1_2",8:"player2_1",9:"player2_2",10:"game winner",11:"ban1",12:"ban2",13:"deck1_1",14:"deck1_2",15:"deck2_1",16:"deck2_2",17:"DeckName1",18:"DeckName2"})


##ゲーム２の時

  ga = 2
  list1_1=[]
  list1_2=[]
  list2_1=[]
  list2_2=[]

  if set==1:

    win2 = soup.find_all("div")[225].text
    if "Blue" in win2:
      winner2=1
    else:
      winner2=2

    for num in range(53,61):
      tag = soup.find_all("img")[num]
      a = tag.get("alt")
      list1_1.append(a)

    for num in range(61,69):
      tag = soup.find_all("img")[num]
      a = tag.get("alt")
      list1_2.append(a)

    for num in range(69,77):
      tag = soup.find_all("img")[num]
      a = tag.get("alt")
      list2_1.append(a)

    for num in range(77,85):
      tag = soup.find_all("img")[num]
      a = tag.get("alt")
      list2_2.append(a)

    list1 = list1_1 + list1_2
    list2 = list2_1 + list2_2
    DN1 = deckname1(set)
    DN2 = deckname2(set)

  elif set==2:

    win2 = soup.find_all("div")[192].text
    if "Blue" in win2:
      winner2=1
    else:
      winner2=2


    for num in range(37,45):
      tag = soup.find_all("img")[num]
      a = tag.get("alt")
      list1_1.append(a)


    for num in range(45,53):
      tag = soup.find_all("img")[num]
      a = tag.get("alt")
      list2_1.append(a)

    list1_2 = None
    list2_2 = None


    list1 = list1_1
    list2 = list2_1
    DN1 = deckname1(set)
    DN2 = deckname2(set)

  elif set==3:
    pl1_1 = soup.find_all("a",{"class":"player_name_header"})[2].string
    pl2_1 = soup.find_all("a",{"class":"player_name_header"})[3].string
    pl1_2 = None
    pl2_2 = None

    win2 = soup.find_all("div")[192].text
    if "Blue" in win2:
      winner2=1
    else:
      winner2=2

    for num in range(37,45):
      tag = soup.find_all("img")[num]
      a = tag.get("alt")
      list1_1.append(a)

    for num in range(45,53):
      tag = soup.find_all("img")[num]
      a = tag.get("alt")
      list2_1.append(a)

    list1_2 = None
    list2_2 = None

    list1 = list1_1
    list2 = list2_1
    DN1 = deckname1(set)
    DN2 = deckname2(set)

  else:
    print("Error")

  se = pd.Series([we,ma,set,ga,team1,team2,pl1_1,pl1_2,pl2_1,pl2_2,winner2,ban1,ban2,list1_1,list1_2,list2_1,list2_2,DN1,DN2],index=index)
  df_all = df_all.append(se,ignore_index = True)


# ゲーム３
  ga=3
  list1_1=[]
  list1_2=[]
  list2_1=[]
  list2_2=[]

  try:

    if set==1:

      win3 = soup.find_all("div")[309].text
      if "Blue" in win3:
        winner3=1
      else:
        winner3=2


      for num in range(92,100):
        tag = soup.find_all("img")[num]
        a = tag.get("alt")
        list1_1.append(a)

      for num in range(100,108):
        tag = soup.find_all("img")[num]
        a = tag.get("alt")
        list1_2.append(a)

      for num in range(108,116):
        tag = soup.find_all("img")[num]
        a = tag.get("alt")
        list2_1.append(a)

      for num in range(116,124):
        tag = soup.find_all("img")[num]
        a = tag.get("alt")
        list2_2.append(a)

      list1 = list1_1 + list1_2
      list2 = list2_1 + list2_2
      DN1 = deckname1(set)
      DN2 = deckname2(set)

    elif set==2:

      win3 = soup.find_all("div")[244].text
      if  "Blue" in win3:
        winner3=1
      else:
        winner3=2

      for num in range(60,68):
        tag = soup.find_all("img")[num]
        a = tag.get("alt")
        list1_1.append(a)

      for num in range(68,76):
        tag = soup.find_all("img")[num]
        a = tag.get("alt")
        list2_1.append(a)


      list1_2 = None
      list2_2 = None

      list1 = list1_1
      list2 = list2_1
      DN1 = deckname1(set)
      DN2 = deckname2(set)

    elif set==3:
      pl1_1 = soup.find_all("a",{"class":"player_name_header"})[4].string
      pl2_1 = soup.find_all("a",{"class":"player_name_header"})[5].string
      pl1_2 = None
      pl2_2 = None

      win3 = soup.find_all("div")[244].text
      if "Blue" in win3:
        winner3=1
      else:
        winner3=2

      for num in range(60,68):
        tag = soup.find_all("img")[num]
        a = tag.get("alt")
        list1_1.append(a)

      for num in range(68,76):
        tag = soup.find_all("img")[num]
        a = tag.get("alt")
        list2_1.append(a)

      list1_2 = None
      list2_2 = None

      list1 = list1_1
      list2 = list2_1
      DN1 = deckname1(set)
      DN2 = deckname2(set)


    se = pd.Series([we,ma,set,ga,team1,team2,pl1_1,pl1_2,pl2_1,pl2_2,winner3,ban1,ban2,list1_1,list1_2,list2_1,list2_2,DN1,DN2],index=index)
    df_all = df_all.append(se,ignore_index = True)

  except:
    pass

#ゲーム４
  ga=4
  list1_1=[]
  list1_2=[]
  list2_1=[]
  list2_2=[]

  try:
    if set==3:
      pl1_1 = soup.find_all("a",{"class":"player_name_header"})[6].string
      pl2_1 = soup.find_all("a",{"class":"player_name_header"})[7].string
      pl1_2 = None
      pl2_2 = None

      win4 = soup.find_all("div")[295].text
      if "Blue" in win4:
        winner4=1
      else:
        winner4=2

      for num in range(83,91):
        tag = soup.find_all("img")[num]
        a = tag.get("alt")
        list1_1.append(a)

      for num in range(91,99):
        tag = soup.find_all("img")[num]
        a = tag.get("alt")
        list2_1.append(a)

      list1_2 = None
      list2_2 = None

      list1 = list1_1
      list2 = list2_1
      DN1 = deckname1(set)
      DN2 = deckname2(set)


      se = pd.Series([we,ma,set,ga,team1,team2,pl1_1,pl1_2,pl2_1,pl2_2,winner4,ban1,ban2,list1_1,list1_2,list2_1,list2_2,DN1,DN2],index=index)
      df_all = df_all.append(se,ignore_index = True)
    else:
      pass
  except:
    pass

#ゲーム５
  ga=5
  list1_1=[]
  list1_2=[]
  list2_1=[]
  list2_2=[]


  try:
    if set==3:
      pl1_1 = soup.find_all("a",{"class":"player_name_header"})[8].string
      pl2_1 = soup.find_all("a",{"class":"player_name_header"})[9].string
      pl1_2 = None
      pl2_2 = None

      win5 = soup.find_all("div")[346].text
      if "Blue" in win5:
        winner5=1
      else:
        winner5=2

      for num in range(106,114):
        tag = soup.find_all("img")[num]
        a = tag.get("alt")
        list1_1.append(a)

      for num in range(114,122):
        tag = soup.find_all("img")[num]
        a = tag.get("alt")
        list2_1.append(a)

      list1_2 = None
      list2_2 = None

      list1 = list1_1
      list2 = list2_1
      DN1 = deckname1(set)
      DN2 = deckname2(set)


      se = pd.Series([we,ma,set,ga,team1,team2,pl1_1,pl1_2,pl2_1,pl2_2,winner5,ban1,ban2,list1_1,list1_2,list2_1,list2_2,DN1,DN2],index=index)
      df_all = df_all.append(se,ignore_index = True)
    else:
      pass
  except:
    pass

  return df_all

#for文で回して全データをdfに収納（時間かかる）

df_CRLdata = pd.DataFrame()

for week in range(1,9):
  for match in range(1,10):
    for set in range(1,4):
      try:
        df_CRLdata = df_CRLdata.append(getCRLdata(week,match,set))
      except:
        pass #set3がない場合の対処を追加


df_CRLdata.reset_index(drop=True, inplace=True)

#　セット勝者、マッチ勝者の列をdfに追加

df_CRLdata['set winner'] = df_CRLdata.groupby(['week','match','set'])['game winner'].transform(lambda d:d.mode()[0])
df_CRLdata['match winner'] = df_CRLdata.groupby(['week','match'])['set winner'].transform(lambda d:d.mode()[0])
df_CRLdata = df_CRLdata[["week","match","set","game","team1","team2","player1_1","player1_2","player2_1","player2_2","game winner","set winner","match winner","ban1","ban2","deck1_1","deck1_2","deck2_1","deck2_2","DeckName1","DeckName2"]]
df_CRLdata

#DeckNameのバグ修正、ただし、セット数ごとの条件分岐（2v2は2人のデッキを足す）はできてない。

def DNcheck(x):
    if  "three-musketeers" in x:
        return "三銃士"
    elif  "golem" in x:
        return "ゴーレム"
    elif "pekka" in x:
      if "ram-rider" in x:
         return "ペッカラム"
      else:
        return "ペッカ"
    elif "lava-hound" in x:
        return "ラバ"
    elif "royal-giant" in x:
        return "ロイジャイ"
    elif "goblin-giant" in x:
        return "ゴブジャイ"
    elif "giant-skeleton" in x:
        return "巨大スケルトン"
    elif "giant" in x:
        return "ジャイアント"
    elif "x-bow" in x:
        return "クロスボウ"
    elif "balloon" in x:
        return "バルーン"
    elif "royal-hog" in x:
        return "ロイヤルホグ"
    elif "ram-rider" in x:
        return "ラムライダー"
    elif "graveyard" in x:
        return "スケルトンラッシュ"
    elif "mortar" in x:
        return "迫撃"
    elif "hog-rider" in x:
        return "ホグ"
    elif "miner" and "poison" in x:
        return "ディガポイ"
    elif "goblin-barrel" and "princess" in x:
        return "枯渇"
    elif "lumberjack" and "royal-ghost" and "'battle-ram" in x:
        return "神器"
    elif "dark-prince" and "bandit" and "'battle-ram" in x:
        return "神器"
    else:
        return "その他"


df_CRLdata['DeckName1'] = df_CRLdata['deck1_1'].apply(DNcheck)
df_CRLdata["DeckName2"] = df_CRLdata["deck2_1"].apply(DNcheck)
df_CRLdata

df_CRLdata.to_csv("CRLdata_goo.csv", encoding='utf_8_sig')
