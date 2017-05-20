a = 0
while True :
    try :
        b = eval(input("숫자를 입력하시오 : "))
        a+=b
        if input("계속 ? (yes/no)") == "no":
            break
    except :
        print("잘못된 값 입력입니다 다시 시작합니다")
        a = 0
        continue
print("합계는 : {0}".format(a))
