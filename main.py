import pyautogui as pg
import time
from functools import reduce

def he_is_comming(second):
    time.sleep(1)
    print(f"마우스 이벤트 시작 {second}초 전")
    return
    
def init(second, isAllowMoving):
    list(map(he_is_comming, [i + 1 for i in reversed(range(second))]))
    print("자동클릭 이벤트가 시작되었습니다. 마우스를 움직이면 자동으로 중지됩니다")
    before = pg.position() 
    while True:
        after = pg.position()
        # 마우스 위치 바뀌었으면 루프문 탈출
        if before != after and isAllowMoving:
            print("자동클릭이 중지되었습니다")
            break
        pg.click() 

init(10, True)