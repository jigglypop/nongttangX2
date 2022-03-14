import pyautogui as pg
import pyperclip as pp
import time

def he_is_comming(second):
    time.sleep(1)
    print(f"마우스 이벤트 시작 {second}초 전")
    return

def get_im_ji_sungs_legacy():
    f = open('./im_ji_sung.js', 'r')
    return "".join(f.readlines())  

def step(callback):
    time.sleep(0.5)
    callback

def im_ji_sungs_legacy():
    text = get_im_ji_sungs_legacy()
    func_step = [
        pg.click(),
        pp.copy(text),
        pg.hotkey('ctrl', 'v'),
        pg.press('enter'),
        pg.move(-500, 0, duration=0.5),
        pg.click(),
        pg.press('enter'),
        pg.press('enter'),
        pg.move(500, 0, duration=0.5),
        pg.click(),
    ]
    list(map(step, func_step))

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
        # 아래 두 함수 중 택 1
        # 건너뛰기 사용()
        im_ji_sungs_legacy() 
        # 그냥 클릭 사용
        # pg.click()

init(5, True)