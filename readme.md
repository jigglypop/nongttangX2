### 농땡농땡

_마치 고양이처럼 퇴근하고 오면 자동으로 다 들어져 있는 프로그램_

![](https://images.mypetlife.co.kr/content/uploads/2019/12/09151959/%EC%8B%AC%EC%8B%AC%ED%95%9C_%EA%B3%A0%EC%96%91%EC%9D%B42.png)

![IzLmo84UQg10xLdWQeK45JJ9bXgU](https://user-images.githubusercontent.com/52653682/157766102-a6321b70-ba3d-4ea6-b904-8a25b3412fae.gif)

#### 사용법

**주의 : 파이썬이 설치되어 있지 않으면 귀찮을 수 있습니다**

0. 파이썬 설치

21 블루스택 등 핸드폰 가상화 프로그램 아무거나 설치(아래는 블루스택 주소)

https://www.bluestacks.com/ko/index.html?utm_campaign=aw-ded-AndroidonPC-ko-kr-s-1&gclid=Cj0KCQjwsYb0BRCOARIsAHbLPhFoC1MkYlkziNvG9Yd12MOL8SXv6yCbdVFQxpanqelUy3CsVGCPfJwaAkOzEALw_wcB

1. 블루스택 로그인 후 블루스택 내의 **크롬 주소창**에 받은 android용 apk 받아서 블루스택 가상머신 내에 강의 앱 설치( 보안상 링크는 생략합니다 )

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

5. 모바일과 같이 로그인 후 동영상 킴

6. 모바일에 다음 동영상으로 가는 버튼 위치에 비슷하게 마우스를 올려놓고 매크로 실행

    ```bash
    python ./main.py
    ```

    번외) 딜레이 옵션

    ```python
    init(5, 		True)
    	#몇초인지	#마우스가 움직이면 중지시킬지 결정(True시 마우스 움직임에 매크로 정지)
    ```

7. 출근
