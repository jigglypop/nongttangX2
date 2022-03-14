# 농땡농땡

~~마치 고양이처럼 퇴근하고 오면 자동으로 다 들어져 있는 프로그램~~

__빨래 널고 오면 다 들어져 있는 프로그램__

__단, 불안하면 아래의 주석처리된 클릭 이벤트를 사용하세요__

### 임지성님의 자동 스킵기능을 추가했습니다. 기여에 감사드립니다

![](https://images.mypetlife.co.kr/content/uploads/2019/12/09151959/%EC%8B%AC%EC%8B%AC%ED%95%9C_%EA%B3%A0%EC%96%91%EC%9D%B42.png)

![IzLmo84UQg10xLdWQeK45JJ9bXgU](https://user-images.githubusercontent.com/52653682/157766102-a6321b70-ba3d-4ea6-b904-8a25b3412fae.gif)

#### 사용법

**주의 : 파이썬이 설치되어 있지 않으면 귀찮을 수 있습니다**

0. 파이썬 설치

1. nh-tong 로그인

2. venv(파이썬 가상환경 만들기)

    ```bash
     python -m venv venv
    ```

3. 가상환경 실행
    ```bash
    source ./venv/Scripts/activate
    ```
4. requirements.txt 자동 설치

    ```bash
    pip3 install -r requirements.txt
    ```

    번외) requirements.txt에 모든 가상환경 패키지 버전이 들어있음
    현재 버전 기록하기)

    ```bash
    pip3 freeze > requirements.txt
    ```

5. 로그인 후 ctrl + shift + i 를 켜고 다음 위치에 마우스를 올려놓고 화면을 반반으로 다음과 같이 세팅한다
![사본 -제목 없음](https://user-images.githubusercontent.com/52653682/158211115-69b6dc3d-425e-4102-b2d1-9b07c3152036.png)


6. 프로그램 실행 후 딜레이에 맞게 빠르게 마우스를 가져다 놓는다

    ```bash
    python ./main.py
    ```

    번외) 딜레이 옵션

    ```python
    init(
        5, 		#몇초인지
        True    #마우스가 움직이면 중지시킬지 결정(True시 마우스 움직임에 매크로 정지)
    )

    ```

7. 밀린 빨래를 한다
