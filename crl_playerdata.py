#df_CRLdataファイルの読み込み
import pandas as pd

df_CRLdata = pd.read_csv('CRLdata_goo.csv', encoding='utf-8',index_col=0)


#DeckNameのバグ修正、ただし、セット数ごとの条件分岐（2v2は2人のデッキを足す）はできてない。

def DNcheck(x):
    if  "three-musketeers" in x:
        return "三銃士"
    elif  ("golem" in x) and ("ice-golem" not in x):
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
      if "giant" in x:
        return "ジャイアント"
      else:
        return "ディガポイ"
    elif "goblin-barrel" and "princess" in x:
        return "枯渇"
    elif "lumberjack" and "royal-ghost" and "'battle-ram" in x:
        return "神器"
    elif "dark-prince" and "bandit" and "'battle-ram" in x:
        return "神器"
    elif "giant" in x:
        return "ジャイアント"
    else:
        return "その他"


df_CRLdata['DeckName1'] = df_CRLdata['deck1_1'].apply(DNcheck)
df_CRLdata["DeckName2"] = df_CRLdata["deck2_1"].apply(DNcheck)


# 特定の条件下でのデータ取り出し

#player
#playername = "RAD"

#df_onedata = df_CRLdata[(df_CRLdata.player1_1.str.contains(playername)|df_CRLdata.player2_1.str.contains(playername)|df_CRLdata.player1_2.str.contains(playername)|df_CRLdata.player2_2.str.contains(playername)) & (df_CRLdata.set==1)]
#df_onedata

# team
#tn = "ponos"
#df_onedata = df_CRLdata[(df_CRLdata.team1.str.contains(tn)|df_CRLdata.team2.str.contains(tn)) & (df_CRLdata.set==1)]#df_onedata
#df_onedata
#df_onedata.to_csv("KOH.csv", encoding='utf_8_sig')

# 選手個人ごとのデータフレームを作成
from collections import Counter
playerlist=[
    "みかん坊や","天GOD","Kota","RAD","ライキジョーンズ",
    "Jack","きたっしゃん","Dani","けんつめし",
    "Rolaporon","焼き鳥","ユイヒイロ","Blossom","KK19212",
    "れいや","HanexHane","Lewis","ピラメキ","天ぷら",
    "Asher","Eui Chan","DDaB0ngTV","X-Bow Master","Huni",
    "SB","The Rock","Xiake", "Master Hong","Yugiart",
    "Nuri","Alpha","Tru Fast","July","Line",
    "Trainer Ken","Manong Jhipee","Jaii","Tobi",
    "Edo","Sinchu","Sado","Greed",
    "Onion","Legend","Dios Stitch","Lampo","Maluntin","meat",
    "Ohh Yeahhh","JayTV","Benzer Ridel","Dexterz",
    "Victor","Thunder","TNT","One Crown","Dandelion"]
# huni,Line,Lampo,meatはつづり合ってるか分からん
#df_CRLdata = pd.read_csv("CRLdata.csv")
index=["Team","TotalWin","TotalLose","Win(set1)","Lose(set1)","Win(set2)","Lose(set2)","Win(set3)",
       "Lose(set3)","TotalWinRate","1v1WinRate","2v2WinRate","SelectBan","SelectedBan","UseDeck","TopUseDeck","DeckUseNum"]
df_pdata = pd.DataFrame()

df_sam = df_CRLdata.copy()

for playername in playerlist:
  try:
    df_team = df_sam[(df_sam.player1_1.str.contains(playername)) |(df_sam.player1_2.str.contains(playername))]
    team = df_team.iloc[0,4]
  except:
    try:
      df_team = df_sam[(df_sam.player2_1.str.contains(playername)) |(df_sam.player2_2.str.contains(playername))]
      team = df_team.iloc[0,5]
    except:
      team = "不明"


  # 特定プレーヤーのセット２の勝ち数
  df_set2win = df_sam[((df_sam.player1_1.str.contains(playername)) & (df_sam["game winner"]==1) & (df_sam.set==2))
            | ((df_sam.player2_1.str.contains(playername)) & (df_sam["game winner"]==2) & (df_sam.set==2))]
  win2 = len(df_set2win)

  # 特定プレーヤーのセット１の勝ち数
  df_set1win = df_sam[((df_sam.player1_1.str.contains(playername)) & (df_sam["game winner"]==1) & (df_sam.set==1))
            | ((df_sam.player1_2.str.contains(playername)) & (df_sam["game winner"]==1) & (df_sam.set==1))
            | ((df_sam.player2_1.str.contains(playername)) & (df_sam["game winner"]==2) & (df_sam.set==1))
            | ((df_sam.player2_2.str.contains(playername)) & (df_sam["game winner"]==2) & (df_sam.set==1))]
  win1 = len(df_set1win)

  # 特定プレーヤーのセット３の勝ち数
  df_set3win = df_sam[((df_sam.player1_1.str.contains(playername)) & (df_sam["game winner"]==1) & (df_sam.set==3))
            | ((df_sam.player2_1.str.contains(playername)) & (df_sam["game winner"]==2) & (df_sam.set==3))]
  win3 = len(df_set3win)

  # 合計の勝ち
  twin = win1+win2+win3

  # 特定プレーヤーのセット２の負け数
  df_set2lose = df_sam[((df_sam.player1_1.str.contains(playername)) & (df_sam["game winner"]==2) & (df_sam.set==2))
            | ((df_sam.player2_1.str.contains(playername)) & (df_sam["game winner"]==1) & (df_sam.set==2))]
  lose2 = len(df_set2lose)

  # 特定プレーヤーのセット１の負け数
  df_set1lose = df_sam[((df_sam.player1_1.str.contains(playername)) & (df_sam["game winner"]==2) & (df_sam.set==1))
            | ((df_sam.player1_2.str.contains(playername)) & (df_sam["game winner"]==2) & (df_sam.set==1))
            | ((df_sam.player2_1.str.contains(playername)) & (df_sam["game winner"]==1) & (df_sam.set==1))
            | ((df_sam.player2_2.str.contains(playername)) & (df_sam["game winner"]==1) & (df_sam.set==1))]
  lose1 = len(df_set1lose)

  # 特定プレーヤーのセット３の負け数
  df_set3lose = df_sam[((df_sam.player1_1.str.contains(playername)) & (df_sam["game winner"]==2) & (df_sam.set==3))
            | ((df_sam.player2_1.str.contains(playername)) & (df_sam["game winner"]==1) & (df_sam.set==3))]
  lose3 = len(df_set3lose)

  # 合計の負け
  tlose = lose1+lose2+lose3

  # 勝率
  try:
    twinrate = twin/(twin+tlose)
  except:
    twinrate = 0
  try:
    winrate1 = (win2+win3)/(win2+win3+lose2+lose3) #1v1
  except:
    winrate1 = 0
  try:
    winrate2 = win1 / (win1+lose1) #2v2
  except:
    winrate2 = 0


  # ban
  df_ban1 = df_sam[((df_sam.player1_1.str.contains(playername)) & (df_sam.set==2)& (df_sam.game==1))]
  df_ban2 = df_sam[((df_sam.player2_1.str.contains(playername)) & (df_sam.set==2)& (df_sam.game==1))]
  a = df_ban1["ban1"]
  b = df_ban2["ban2"]
  se_e1 = pd.Series()
  se_e1 = se_e1.append(a).append(b)
  my = se_e1.values.tolist()
  myban = ' '.join(my)#change

  c = df_ban1["ban2"]
  d = df_ban2["ban1"]
  se_e2 = pd.Series()
  se_e2 = se_e2.append(c).append(d)
  your = se_e2.values.tolist()
  yourban = ' '.join(your)#change

  # 1v1 all deck
  df_deck1 = df_sam[((df_sam.player1_1.str.contains(playername)) & (df_sam.set!=1))]
  df_deck2 = df_sam[((df_sam.player2_1.str.contains(playername)) & (df_sam.set!=1))]
  e = df_deck1["deck1_1"]
  f = df_deck2["deck2_1"]
  se_d1 = pd.concat([e, f])
  se_d1 = se_d1.reset_index(drop=True)
  lst = se_d1.values.tolist()
  deck1 = [s.replace("'", "") for s in lst]

  # 1v1 NO1 usedeck

  try:
    g = df_deck1["DeckName1"]
    h = df_deck2["DeckName2"]
    se_d2 = pd.concat([g, h])
    se_d2 = se_d2.reset_index(drop=True)

    if se_d2.mode()[0]=="その他":
      deck2 = se_d2.mode()[1]
      num = se_d2.value_counts().iat[1]

    else:
      deck2 = se_d2.mode()[0]
      num = se_d2.value_counts().iat[0]

  except:
    deck2=None
    num=None



  se = pd.Series([team,twin,tlose,win1,lose1,win2,lose2,win3,lose3,twinrate,winrate1,winrate2,myban,yourban,deck1,deck2,num])
  df_pdata = df_pdata.append(se,ignore_index = True)


df_pdata.columns = index
df_pdata.index = playerlist


# 特定条件でのデータ取得
# team
#tn = "PONOS"
#df_onedata = df_pdata[(df_pdata.Team.str.contains(tn))]
#df_onedata


gal=["gamewith","detonation-gaming","op-gaming","talon-esports","bren-esports","sandbox"]
gbl=["ponos","fav-gaming","king-zone-dragonx","kix","chaos-theory","ogn-entus"]
teamlist=gal+gbl

df_td=pd.DataFrame()


def test(teamname):

  df_s = df_pdata.copy()

  #member
  df_mem = df_s[(df_s.Team.str.contains(teamname))]
  #mem = list(df_mem.index)
  mem1 = df_mem.index
  mem = mem1.tolist()
  #group
  if teamname in gal:
    group="A"
  elif teamname in gbl:
    group="B"
  else:
    group = "Error"

  ## match勝敗
  # 特定チームのマッチ勝ち数
  df_matchwin = df_sam[((df_sam.team1.str.contains(teamname)) & (df_sam["match winner"]==1) & (df_sam.set==1) & (df_sam.game==1))
                | ((df_sam.team2.str.contains(teamname)) & (df_sam["match winner"]==2) & (df_sam.set==1) & (df_sam.game==1))]
  mawin = len(df_matchwin)

  # 特定チームのマッチ負け数
  df_matchlose = df_sam[((df_sam.team1.str.contains(teamname)) & (df_sam["match winner"]==2) & (df_sam.set==1) & (df_sam.game==1))
                | ((df_sam.team2.str.contains(teamname)) & (df_sam["match winner"]==1) & (df_sam.set==1) & (df_sam.game==1))]
  malose = len(df_matchlose)


  ## set勝率
  # 特定チームのセット２の勝ち数
  df_s2win = df_sam[((df_sam.team1.str.contains(teamname)) & (df_sam["set winner"]==1) & (df_sam.set==2) & (df_sam.game==1))
                | ((df_sam.team2.str.contains(teamname)) & (df_sam["set winner"]==2) & (df_sam.set==2) & (df_sam.game==1))]
  win2 = len(df_s2win)

  # 特定チームのセット１の勝ち数
  df_s1win = df_sam[((df_sam.team1.str.contains(teamname)) & (df_sam["set winner"]==1) & (df_sam.set==1) & (df_sam.game==1))
            | ((df_sam.team2.str.contains(teamname)) & (df_sam["set winner"]==2) & (df_sam.set==1) & (df_sam.game==1))]
  win1 = len(df_s1win)

  # 特定チームのセット３の勝ち数
  df_s3win = df_sam[((df_sam.team1.str.contains(teamname)) & (df_sam["set winner"]==1) & (df_sam.set==3) & (df_sam.game==1))
            | ((df_sam.team2.str.contains(teamname)) & (df_sam["set winner"]==2) & (df_sam.set==3) & (df_sam.game==1))]
  win3 = len(df_s3win)


  # 特定チームのセット２の負け数
  df_s2lose = df_sam[((df_sam.team1.str.contains(teamname)) & (df_sam["set winner"]==2) & (df_sam.set==2) & (df_sam.game==1))
                | ((df_sam.team2.str.contains(teamname)) & (df_sam["set winner"]==1) & (df_sam.set==2) & (df_sam.game==1))]
  lose2 = len(df_s2lose)

  # 特定チームのセット１の負け数
  df_s1lose = df_sam[((df_sam.team1.str.contains(teamname)) & (df_sam["set winner"]==2) & (df_sam.set==1) & (df_sam.game==1))
            | ((df_sam.team2.str.contains(teamname)) & (df_sam["set winner"]==1) & (df_sam.set==1) & (df_sam.game==1))]
  lose1 = len(df_s1lose)

  # 特定チームのセット３の負け数
  df_set3lose = df_sam[((df_sam.team1.str.contains(teamname)) & (df_sam["set winner"]==2) & (df_sam.set==3) & (df_sam.game==1))
            | ((df_sam.team2.str.contains(teamname)) & (df_sam["set winner"]==1) & (df_sam.set==3) & (df_sam.game==1))]
  lose3 = len(df_set3lose)

  winrate1 = win1/(win1+lose1)
  winrate2 = win2/(win2+lose2)
  winrate3 = win3/(win3+lose3)


  ##1v1,2v2netwinrate
  #1v1win
  df_1v1win = df_sam[((df_sam.team1.str.contains(teamname)) & (df_sam["game winner"]==1) & (df_sam.set != 1)
                | ((df_sam.team2.str.contains(teamname)) & (df_sam["game winner"]==2) & (df_sam.set != 1)))]
  win11 = len(df_1v1win)
  #1v1lose
  df_1v1lose = df_sam[((df_sam.team1.str.contains(teamname)) & (df_sam["game winner"]==2) & (df_sam.set !=1)
                | ((df_sam.team2.str.contains(teamname)) & (df_sam["game winner"]==1) & (df_sam.set !=1)))]
  lose11 = len(df_1v1lose)
  #2v2win
  df_2v2win = df_sam[((df_sam.team1.str.contains(teamname)) & (df_sam["game winner"]==1) & (df_sam.set==1)
                | ((df_sam.team2.str.contains(teamname)) & (df_sam["game winner"]==2) & (df_sam.set==1)))]
  win22 = len(df_2v2win)
  #2v2lose
  df_2v2lose = df_sam[((df_sam.team1.str.contains(teamname)) & (df_sam["game winner"]==2) & (df_sam.set==1)
                | ((df_sam.team2.str.contains(teamname)) & (df_sam["game winner"]==1) & (df_sam.set==1)))]
  lose22 = len(df_2v2lose)
  winrate1v1 = win11/(win11+lose11)
  winrate2v2 = win22/(win22+lose22)

  #2v2ban
  df_ban1 = df_sam[((df_sam.team1.str.contains(teamname)) & (df_sam.set==1)& (df_sam.game==1))]
  df_ban2 = df_sam[((df_sam.team2.str.contains(teamname)) & (df_sam.set==1)& (df_sam.game==1))]
  a = df_ban1["ban1"]
  b = df_ban2["ban2"]
  se_e1 = pd.Series()
  se_e1 = se_e1.append(a).append(b)
  my = se_e1.values.tolist()
  myban = ' '.join(my)#change

  c = df_ban1["ban2"]
  d = df_ban2["ban1"]
  se_e2 = pd.Series()
  se_e2 = se_e2.append(c).append(d)
  your = se_e2.values.tolist()
  yourban = ' '.join(your)

  #bestplayer
  df = df_pdata[((df_pdata.Team.str.contains(teamname))) ]
  wr1 = df["1v1WinRate"].max()
  p1 = df["1v1WinRate"].idxmax()
  p2_1 = df["2v2WinRate"].idxmax()
  p2_2 = df["2v2WinRate"].idxmax(2)
  wr2_1 = df["2v2WinRate"].max()


  df_1 =  pd.DataFrame(
      data={'Member': [mem], 'Group': [group], 'Matchwin': [mawin], 'MatchLose': [malose], 'WinRate(set1)': [winrate1],'WinRate(set2)': [winrate2],'WinRate(set3)': [winrate3],'WinRate(1v1)': [winrate1v1],'WinRate(2v2)': [winrate2v2],
            'SelectBan(2v2)': [myban],'SelectedBan(2v2)': [yourban],'BestPlayer(1v1)': [p1],'PlayersWinrate': [wr1],'BestPlayer(2v2)': [p2_1],'PlayersWinRate(2v2)': [wr2_1]},
      columns = ['Member','Group','Matchwin','MatchLose','WinRate(set1)','WinRate(set2)','WinRate(set3)','WinRate(1v1)','WinRate(2v2)','SelectBan(2v2)',
                 'SelectedBan(2v2)','BestPlayer(1v1)','PlayersWinrate','BestPlayer(2v2)','PlayersWinRate(2v2)'])

  return df_1

# 関数をforで回してチームごとのデータフレームを作成
for teamname in teamlist:
  df_td = df_td.append(test(teamname))

df_td.index = teamlist



# 図の表示
%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
"""
# セットごとの勝率と全体の勝ち数の相関
ax = df_td.plot.scatter(x='WinRate(set1)',y='Matchwin',color='b',label="Set1")
ax1 = df_td.plot.scatter(x='WinRate(set2)',y='Matchwin',color='g',label="Set2",ax=ax)
ax2 = df_td.plot.scatter(x='WinRate(set3)',y='Matchwin',color='r',label="Set3",ax=ax1);
a = ax2.set_xlabel('WinRate')

#ax.annotate("point A", xy = (0.5, 4), size = 15, color = "black");
for k, v in df_td.iterrows():
    ax2.annotate(k[:5], xy=(v[4],v[2]), size=7)
    ax2.annotate(k[:5], xy=(v[5]+0.015,v[2]+0.15), size=7)
    ax2.annotate(k[:5], xy=(v[6]+0.03,v[2]+0.3), size=7)
    #ax.annotate(df_td.index.values[a], xy = (0.5, 4), size = 6, color = "black");

plt;
#df_corr = df_td.corr()
#df_corr

plt.savefig('figure.png',format = 'png', dpi=300)
from google.colab import files
files.download('figure.png')
"""

"""
#　エースの存在と勝ち数の散布図
ax = df_td.plot.scatter(x='PlayersWinrate',y='Matchwin',color='b',label="1v1")
ax1 = df_td.plot.scatter(x='PlayersWinRate(2v2)',y='Matchwin',color='g',label="2v2",ax=ax);
a = ax1.set_xlabel("BestPlayersWinRate")

#ax.annotate("point A", xy = (0.5, 4), size = 15, color = "black");
for k, v in df_td.iterrows():
    ax1.annotate(k[:5], xy=(v[12],v[2]), size=7)
    ax1.annotate(k[:5], xy=(v[14]+0.015,v[2]+0.15), size=7)
    #ax.annotate(df_td.index.values[a], xy = (0.5, 4), size = 6, color = "black");

plt;
df_corr = df_td.corr()
df_corr

plt.savefig('figure2.png',format = 'png', dpi=300)
from google.colab import files
files.download('figure2.png')

"""

#全体のdeckごとの勝率を測る
#1v1と2v2
columns=["DeckWin(1v1)","Decklose(1v1)","DeckWinRate(1v1)","DeckWin(2v2)","Decklose(2v2)","DeckWinRate(2v2)"]
df_deckwinrate = pd.DataFrame()

df_deckwin1 = df_CRLdata.copy()
df_deckwin2 = df_CRLdata.copy()
df_decklose1 = df_CRLdata.copy()
df_decklose2 = df_CRLdata.copy()
decklist=["三銃士","ゴーレム","ペッカラム","ペッカ","ラバ","ロイジャイ","ゴブジャイ","巨大スケルトン" ,"クロスボウ","バルーン",
          "ジャイアント","ロイヤルホグ","ラムライダー" ,"スケルトンラッシュ", "迫撃","ホグ","ディガポイ","枯渇","神器", "その他"]

for deck in decklist:
  df_deckwin1 = df_CRLdata.copy()
  df_deckwin2 = df_CRLdata.copy()
  df_decklose1 = df_CRLdata.copy()
  df_decklose2 = df_CRLdata.copy()

  df_deckwin1 = df_deckwin1[((df_deckwin1.DeckName1.str.contains(deck)) & (df_deckwin1["game winner"]==1) & (df_deckwin1.set != 1)
                | ((df_deckwin1.DeckName2.str.contains(deck)) & (df_deckwin1["game winner"]==2) & (df_deckwin1.set != 1)))]

  df_deckwin2 = df_deckwin2[((df_deckwin2.DeckName1.str.contains(deck)) & (df_deckwin2["game winner"]==1) & (df_deckwin2.set == 1)
                | ((df_deckwin2.DeckName2.str.contains(deck)) & (df_deckwin2["game winner"]==2) & (df_deckwin2.set == 1)))]

  df_decklose1 = df_decklose1[((df_decklose1.DeckName1.str.contains(deck)) & (df_decklose1["game winner"]==2) & (df_decklose1.set != 1)
                | ((df_decklose1.DeckName2.str.contains(deck)) & (df_decklose1["game winner"]==1) & (df_decklose1.set != 1)))]

  df_decklose2 = df_decklose2[((df_decklose2.DeckName1.str.contains(deck)) & (df_decklose2["game winner"]==2) & (df_decklose2.set == 1)
                | ((df_decklose2.DeckName2.str.contains(deck)) & (df_decklose2["game winner"]==1) & (df_decklose2.set == 1)))]

  winnum1 = len(df_deckwin1)
  winnum2 = len(df_deckwin2)
  losenum1 = len(df_decklose1)
  losenum2 = len(df_decklose2)
  if winnum1 + losenum1 != 0:
    winrate1 = winnum1/(winnum1 + losenum1)
  else:
    winrate1 = 0
  if winnum2 + losenum2 !=0:
    winrate2 = winnum2/(winnum2 + losenum2)
  else:
    winrate2 = 0
  se =pd.Series([winnum1,losenum1,winrate1,winnum2,losenum2,winrate2])

  df_deckwinrate = df_deckwinrate.append(se,ignore_index=True)

df_deckwinrate.columns=["DeckWin(1v1)","Decklose(1v1)","DeckWinRate(1v1)","DeckWin(2v2)","Decklose(2v2)","DeckWinRate(2v2)"]
df_deckwinrate.index=decklist


#1v1のデッキごとの勝率（自分と相手の使用デッキ）
pn = "焼き鳥"

columns=["DeckWin(My)","Decklose(My)","DeckWinRate(My)","DeckWin(Ene)","Decklose(Ene)","DeckWinRate(Ene)"]
df_deckwinrate = pd.DataFrame()

df_deckwin1 = df_CRLdata.copy()
df_deckwin2 = df_CRLdata.copy()
df_decklose1 = df_CRLdata.copy()
df_decklose2 = df_CRLdata.copy()
decklist=["三銃士","ゴーレム","ペッカラム","ペッカ","ラバ","ロイジャイ","ゴブジャイ","巨大スケルトン" ,"クロスボウ","バルーン",
          "ジャイアント","ロイヤルホグ","ラムライダー" ,"スケルトンラッシュ", "迫撃","ホグ","ディガポイ","枯渇","神器", "その他"]

for deck in decklist:
  df_deckwin1 = df_CRLdata.copy()
  df_deckwin2 = df_CRLdata.copy()
  df_decklose1 = df_CRLdata.copy()
  df_decklose2 = df_CRLdata.copy()

  df_deckwin1 = df_deckwin1[((df_deckwin1.DeckName1.str.contains(deck)) & (df_deckwin1.player1_1.str.contains(pn))& (df_deckwin1["game winner"]==1) & (df_deckwin1.set != 1)
                | ((df_deckwin1.DeckName2.str.contains(deck))& (df_deckwin1.player2_1.str.contains(pn)) & (df_deckwin1["game winner"]==2) & (df_deckwin1.set != 1)))]

  df_deckwin2 = df_deckwin2[((df_deckwin2.DeckName2.str.contains(deck))& (df_deckwin2.player1_1.str.contains(pn)) & (df_deckwin2["game winner"]==1) & (df_deckwin2.set != 1)
                | ((df_deckwin2.DeckName1.str.contains(deck))& (df_deckwin2.player2_1.str.contains(pn)) & (df_deckwin2["game winner"]==2) & (df_deckwin2.set != 1)))]

  df_decklose1 = df_decklose1[((df_decklose1.DeckName1.str.contains(deck))& (df_decklose1.player1_1.str.contains(pn)) & (df_decklose1["game winner"]==2) & (df_decklose1.set != 1)
                | ((df_decklose1.DeckName2.str.contains(deck))& (df_decklose1.player2_1.str.contains(pn)) & (df_decklose1["game winner"]==1) & (df_decklose1.set != 1)))]

  df_decklose2 = df_decklose2[((df_decklose2.DeckName2.str.contains(deck))& (df_decklose2.player1_1.str.contains(pn)) & (df_decklose2["game winner"]==2) & (df_decklose2.set != 1)
                | ((df_decklose2.DeckName1.str.contains(deck)) & (df_decklose2.player2_1.str.contains(pn))& (df_decklose2["game winner"]==1) & (df_decklose2.set != 1)))]

  winnum1 = len(df_deckwin1)
  winnum2 = len(df_deckwin2)
  losenum1 = len(df_decklose1)
  losenum2 = len(df_decklose2)
  if winnum1 + losenum1 != 0:
    winrate1 = winnum1/(winnum1 + losenum1)
  else:
    winrate1 = 0
  if winnum2 + losenum2 !=0:
    winrate2 = winnum2/(winnum2 + losenum2)
  else:
    winrate2 = 0
  se =pd.Series([winnum1,losenum1,winrate1,winnum2,losenum2,winrate2])

  df_deckwinrate = df_deckwinrate.append(se,ignore_index=True)

df_deckwinrate.columns=columns
df_deckwinrate.index=decklist
