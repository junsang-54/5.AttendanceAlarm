from datetime import datetime
import time
import random

#명언 모음
prov = ["생각하는대로 살지 않으면 사는 대로 생각하게 된다.\n-폴발레리-", "내가 확신하는 한 가지는 신체가 아닌 평화가 치유의 척도라는 것이다.\n-조지 멜턴",
       "사랑은 달콤한 꽃이다. 그러나  그것을 따기 위해서는 무서운 벼랑 끝까지 갈 용기가 있어야 한다.\n-스탕달",
       "인간사에는 안정된 것이 하나도 없음을 기억하라. 그러므로 성공에 들뜨거나 역경에 지나치게 의기 소침하지마라.\n-소크라테스",
       "왜 실패를 과정안에 안 끼워주지? 실패하는 것도 완성을 향해 달려가는 과정에 포함시켜줘야죠.\n-드라마 <런온> 중에서",
       "아무리 작은 일이라도 정성을 담아 10년간 꾸준히 하면 큰 힘이 된다. 20년을 하면 두려울 만큼 거대한 힘이 되고, 30년을 하면 역사가 된다.\n-중국속담",
       "보통의 능력밖에 없다면 근면은 부족함을 보충해줄 것이다.\n-J.레이놀즈"]
#퇴실 인사
bye = ["안녕히 가세요.", "오늘 하루도 고생하셨습니다.", "즐거운 저녁되세요!", "바이~ B.Y.E~~"]

#출석 확인 함수
def in_check():
    x = input("출석 눌렀습니까? \n[y/n]\n")    #출석 여부 확인
    if x == "y":        #출석 했을 때
        print("\n오늘의 명언:")
        print(random.choice(prov))      #명언 랜덤 출력
    elif x == "n":      #출석 안했을 때
        print("출석하세요!")
        time.sleep(180)     #180초 후 재질문
        return in_check()   #다시 출석 확인
    else:       #y/n 이외 입력했을 때
        print("잘못된 정보입니다.")
        return in_check()   #다시 출석 확인

#퇴실 확인 함수
def out_check():
    y = input("퇴실 눌렀습니까? \n[y/n]\n")    #퇴실 여부 확인
    if y == "y":        #퇴실 했을 때
        print(random.choice(bye))       #bye 랜덤 출력
    elif y == "n":      #퇴실 안했을 때
        print("퇴실하세요!\n퇴실하세요!\n퇴실하세요!\n")   #퇴실하라는 알림
        return out_check()  #다시 퇴실 확인
    else:       #y/n 이외 입력했을 때
        print("잘못된 정보입니다.")
        return out_check()  #다시 퇴실 확인



now = datetime.now()    #현재 시간 정의
print("지금은", now.year, "년", now.month, "월", now.day, "일", now.hour, "시", now.minute, "분입니다. \n")    #현재 시간 출력
# in_check()
if now.hour < 11:   #오전 11시 이전일 때
    in_check()      #출석 확인 함수 호출

elif now.hour in range(11, 18):     #오전 11시부터 오후 6시 사이일 때
    print("출석 시간이 아닙니다.\n")

elif now.hour >= 18:    #오후 6시 이후일 때
    out_check()         #퇴실 확인 함수 호출