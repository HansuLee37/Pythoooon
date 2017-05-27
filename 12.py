dic = {"커피음료" : 7, "펜" : 3, "종이컵" : 2, "우유" : 1, "콜라" : 4, "책" : 5}
while(True) :
    a = input("Input : ")
    if a in dic.keys() :
        print(dic[a])
    else :
        print("취급 안함")
    
