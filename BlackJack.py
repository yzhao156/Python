a=[['cards', 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 11, 11, 11, 11, 12, 12, 12, 12, 13, 13, 13, 13], ['player1',1,2,3,4,5], ['player2',1,2,13], ['dealer',1,11,2]]
import random
import time
import copy
def creatboard(cards,players,pairs):
    '''
    （list,str,str)->list
    :param cards: 初始list[[]]
    :param players: input
    :param pairs: input(模拟几副牌)
    :return: list[[牌库]，[玩家1,[玩家2],[荷官]]
    '''
    # 把几副牌放入牌库
    for i in range(1,14):
        for j in range(int(pairs)*4):
            cards[0].append(i)
    # 把player的list创造在cars里
    for i in range(1,int(players)+1):
        cards.append(['player{}'.format(i)])
    # 创建荷官的list在最后
    cards.append(['dealer'])
    return cards
# 审查：
# creatboard(cards,2,2)
# print(cards)

def dealing(cards,get):
    '''
    (list,int)->list
    发牌：从牌库中随机选择一张牌，读它的index然后添加到get的list中，最后在牌库中删除
    :param cards: 牌库
    :param get: 被发牌的人在listcards里的index
    :return: cards的list
    '''
    # 选取随机的牌
    length=len(cards[0])
    random_index=random.randint(1,length-1)
    card_a = cards[0][random_index]
    # 在cards中添加玩家的牌
    cards[get].append(card_a)
    # 在牌库中删除牌
    cards[0].remove(card_a)
    return cards
# 审查：
# cards=[['cards',1,2,3],['1'],['2'],['dealer']]
# dealing(cards,1)
# print(cards)

def listshow(cards,b=0):
    '''
    (list)->list
    把cards变成牌 ie：1->A
    :param cards: cards
    :return: Cards in str
    '''
    realcards=copy.deepcopy(cards)
    for i in range(len(realcards)):
        for j in range(1,len(realcards[i])):
            if realcards[i][j] == 1:
                realcards[i][j] = 'A'
            elif realcards[i][j] == 11:
                realcards[i][j] = 'J'
            elif realcards[i][j] == 12:
                realcards[i][j] = 'Q'
            elif realcards[i][j] == 13:
                realcards[i][j] = 'K'
            else:
                realcards[i][j] = str(realcards[i][j])
    if b == 0:
        if len(realcards[-1]) == 3:
            realcards[-1][-1] = '*'

    return realcards
# 审查：
# cards=[['c',1,2,3],['1',2,3],['2',1,1],['d',11,12]]
# realcards=listshow(cards)
# print(realcards)

def cal(cards,indexofcal):
    '''
    (str,int)->int
    :param cards: cards list
    :param indexofcal: index of cards that need to calculate in list cards
    :return: highest possible points
    '''
    copycards=copy.deepcopy(cards)    
    calcards = copycards[indexofcal]
    calcards.pop(0)
    for i in range(len(calcards)):
        if calcards[i] == 11:
            calcards[i] = 10
        if calcards[i] == 12:
            calcards[i] = 10
        if calcards[i] == 13:
            calcards[i] = 10
    if ((sum(calcards)<=11) and (calcards.count(1) != 0)):
        calcards.append(10)
    return sum(calcards)
# 审查：
# cards = [['CC'],['11',1,2],['22',1,2,13],['33',1,1,1],['44',10,11,12,13],['55'],['DD']]
# indexofcal = 2
# highestpoints = cal(cards,indexofcal)
# print(highestpoints)

def dealercalc(cards):
    '''
    return the points of cards
    (list)->int
    :param cards:cards list
    :return: points of dealer
    '''
    dcards=copy.deepcopy(cards)
    dealercards=dcards[-1]
    dealercards.pop(0)
    if (dealercards[0] == 1) and (dealercards[1] >= 10):
        return 21
    if (dealercards[1] == 1) and (dealercards[0] >= 10):
        return 21
    for i in range(len(dealercards)):
        if dealercards[i] == 11:
            dealercards[i] = 10
        if dealercards[i] == 12:
            dealercards[i] = 10
        if dealercards[i] == 13:
            dealercards[i] = 10
    if ((sum(dealercards)<11) and (dealercards.count(1) != 0)):
        if sum(dealercards) == 7:
            return sum(dealercards)
        else:
            dealercards.append(10)
    return sum(dealercards)
# 检查：
# print(dealercalc([[],[],['DD',1,6]]))
# print(dealercalc([[],[],['DD',1,9]]))
# print(dealercalc([[],[],['DD',2,1,1,1,1]]))
# print(dealercalc([[],[],['DD',13,1]]))

def split(cards,indexofplayer):
    '''
    insert
    (list,int)->list
    :param cards:
    :param indexofplayer:
    :return:
    '''
    deepcopy = copy.deepcopy(cards)
    num = cards[indexofplayer][1]
    cards[indexofplayer].pop(1)
    cards.insert(indexofplayer+1,['{}\'s split'.format(cards[indexofplayer][0])])
    cards[indexofplayer+1].append(num)
    return cards
def splitcards(cards):
    i=1
    while (i < (len(cards)-1)):        
        if (cards[i][1]) == (cards[i][2]):
            askforsplit = input('would you like to split? {} y for yes, n for no: '.format(cards[i][0]))
            if askforsplit == 'y':
                split(cards,i)
                printboard(cards,1)
                wholesend(cards,i)
                wholesend(cards,i+1)
                i+=1
            if askforsplit == 'n':
                printboard(cards,a=0)
                i+=1
        else:
            i+=1
def dealerprocess(cards,t,space):
    #荷官去掉星号
    print('\n'*space)
    listforshow = listshow(cards,1)
    printnice(listforshow,N)###########################################
    time.sleep(t)
    #荷官开始加牌
    while dealercalc(cards)<17:
        dealing(cards,-1)
        print('\n'*space)
        listforshow = listshow(cards,1)
        printnice(listforshow,N)#############################################
        time.sleep(t)
def winer(cards):
    print('Score:')
    for i in range(1,len(cards)):
        print('{}\'s score is {}'.format(cards[i][0],cal(cards,i)))
    print('\n\n\nWinner:')
    if cal(cards,-1) > 21:
        for i in range(1,len(cards)-1):
            if cal(cards,i)<= 21 :
                print('{} wins'.format(cards[i][0]))
            if cal(cards,i)> 21 :
                print('{} loses'.format(cards[i][0]))
    if cal(cards,-1) <= 21:
        for i in range(1,len(cards)-1):
            if cal(cards,i)>21:
                print('{} loses'.format(cards[i][0]))
            elif cal(cards,i)< cal(cards,-1) :
                print('{} loses'.format(cards[i][0]))
            elif cal(cards,i)> cal(cards,-1) :
                print('{} wins'.format(cards[i][0]))
            elif cal(cards,i)== cal(cards,-1):
                print('{} push'.format(cards[i][0]))
    return

def askforcards(cards,t,space):
    for i in range(1,len(cards)-1):
        a = input('{} add? y for yes, n for no: '.format(cards[i][0]))
        if a == 'n':
            printboard(listshow(cards))
        if a == 'y':
            wholesend(cards,i)
            while a != 'n' and cal(cards,i)<=21 :
                a = input('{} add? y for yes, n for no: '.format(cards[i][0]))
                if a == 'y':
                    wholesend(cards,i)
                if a == 'n':
                    printboard(listshow(cards))
        if cal(cards,i)>21:
            print('{}, you are out!\nNow turn to {}'.format(cards[i][0],cards[i+1][0]))
            NN=input('press enter to continue')
            printboard(cards)
        if cal(cards,i)<=21:
            print('Now turn to {}'.format(cards[i+1][0]))
            MM=input('press enter to continue')
            printboard(cards)
      
def printboard(cards,a=0):
    if a == 0:
        listforshow=listshow(cards)#显示牌（显示荷官第二张）
    if a == 1:#荷官第二张不显示
        listforshow=listshow(cards,1)
    if a == -1:
        listforshow=listshow(cards,1)
    print('\n'*space)
    printnice(listforshow,N)#############################
    time.sleep(t)
def printnice(cards,N):
    c=copy.deepcopy(cards)
    longest = len(c[1])
    for i in range(1,len(c)):
        if len(c[i])>longest:
            longest = len(c[i])
    for i in range(1,len(c)):
        while len(c[i])<longest:
            c[i].append(' ')
    for j in range(len(c[-1])):
        for i in range(1,len(c)):
            L=len(c[i][j])
            SS=N-L
            OO=SS//2
            x=(N-len(c[i][j]))//2
            MMM=N-OO-L
##            print(x,len(c[i][j]),N-x,L,SS,OO,MMM)
            
            print(' '*MMM+str(c[i][j]),end = ' '*(OO))
        print('\n')
            


def wholesend(cards,i):
    dealing(cards,i)
    listforshow = listshow(cards)
    printboard(listforshow)

def tworounds(cards,t,space):
    for j in range(2):
        for i in range(1,len(cards)):
            wholesend(cards,i)
def glo(X):
    global N
    N=X
    return
    
def welcome():
    #问好
    a = 'Welcome to 21 points'
    b='Winer Winer Chicken Diner'
    l = max(len(a),len(b))
    print('\n'+'*'*(l+6)+'\n*'+' '*(l+4)+'*'+'\n*     '+a+'    *\n'+('*  '+b+'  *')+'\n*'+' '*(l+4)+'*'+'\n'+'*'*(l+6)+'\n'*3)
    return 
# 检查：
# print(split([[],['player1',2,2],['heguan',7,7]],2))




def play(cards,t,space):
    #发两轮牌
    tworounds(cards,t,space)
    #分牌
    splitcards(cards)                
    #询问要牌
    askforcards(cards,t,space)
    #荷官开始 去掉星号 开始加牌
    dealerprocess(cards,t,space)
    #游戏结束，开始结算
    winer(cards)
    #询问是否继续
    a = input('Do you want to continue? \ny for yes, n for no\n')
    return a


    


######2.设计print的格式（#####已经标出）

if __name__ == '__main__':
    #问好,询问信息
    welcome()
    #请求输入
    t=0.2
    space=60
    glo(15)
    SJ=input('press enter to strat the game')
    print('\n'*60)
    players = int(input('How many players do you want to play with?\n'))
    pairs = int(input('How many pairs of cards do you want to play with?\n'))    
    c = 'y'
    while c == 'y':     
        cards=[['cards']]
        print('\n'*60)
        cards = creatboard(cards,players,pairs)
        c = play(cards,t,space)
    print('\n\nThank you for playing...\nHave a nice day!')
    exit =input('')


