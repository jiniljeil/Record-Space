
## 논문 
Feature Based Approach for Detection of Smishing Messages in the Mobile Environment

Journal of Information Technology ResearchVolume 12Issue 2Apr 2019 pp 17–35. https://doi.org/10.4018/JITR.2019040102

<hr> 

본 연구에서는 모바일 스미싱 탐지에 적합한 특징(feature)들을 식별한다. message-history 또는 third-party services에 의존하지 않고 메세지 내용으로부터 특징들을 추출하였다. 제로 데이(zero-day) 스미싱 공격에도 높은 정확성을 보였다.

## 1. 스미싱 공격 사이클

1. 피싱 웹/앱 구축
   fake-website를 만들어 실제 웹 사이트 인 것처럼 위장한 다음 악성 앱을 다운로드 받도록 유도하는 방식
2. fake link 전송
   SMS에 fake link를 포함시켜 전송 
3. fake website에 접속하여 악성 앱 설치
   유저가 URL을 클릭하여 웹 사이트에 접속하게 될 경우, 악성 앱이 설치되는 방식
4. 개인 정보 탈취 
   신용 정보 또는 민감한 정보들을 탈취

## 2. 스미싱 유형

1. 카드/계좌 정지 (Card/Account Locked) 
2. 수상 & 자선 단체 (Award & Charity) 
3. 가짜 인증 및 업데이트 (Fake Verification and Update)
4. 가짜 온라인 세일 (Online Fake Sale) 
5. 가짜 환불 (Fake Refund) 
6. 가짜 판매 (Fake Trapping) 

## 3. 접근 방식

1. URL 블랙 리스트 확인
   Google safe browsing API를 사용하여 URL이 블랙 리스트에 포함되어있는지 확인 (Google safe browsingdms fake URL 리스트를 포함하며 정기적으로 업데이트 됨) 
2. 블랙 리스트에 없는 URL일 경우, 전처리 (Pre-processing)
   중복 제거, 토큰화, 띄어쓰기 교정, 소문자로 변환
3. 특징 추출 (Feature Extraction)
4. 학습 & 분류 (Learning & Classification)
   SVM (Support Vector Machine), Logistic Regression, Neural networks, Naive Bayes, Random Forest 

### 3.3 특징 추출 방법
$F={F_1,F_2,F_3,...,F_{10}}$ 중 $(F_1,F_2)$는 일반적으로 ham 문자에서 등장, $(F_3,..,F_8)$은 일반적으로 smishing 문자에서 등장한다.

$$
    value = 
        \begin {cases}
        1,\;\text{smishing}\\
        0,\;\text{ham}
        \end {cases}
$$

1. Greetings keywords
$$
    F_1 = 
        \begin {cases}
        0,\;\text{if\,message\,contains\,any\,greeting\,token}\\
        1,\;\text{otherwise}
        \end{cases}
$$
2. Presence of emotions
$$
    F_2 = 
        \begin {cases}
        0,\;\text{message\,contains\,positive\,or\,negative\,emotions}\\
        1,\;\text{otherwise}
        \end {cases}
$$
3. Presence of URL 
$$
    F_3 = 
        \begin {cases}
        1,\;\text{if\,URL\,present\,in\,message}\\
        0,\;\text{otherwise}
        \end {cases}
$$
4. Presence of Mathematical Symbols 
$$
    F_4 = 
        \begin {cases}
        1,\;\text{if\,message\,contains\,mathematical\,symbol}\\
        0,\;\text{otherwise}
        \end {cases}
$$
5. Message length
$$
    F_5 = 
        \begin {cases}
        1,\;\text{if\,message\,length}\geq\text{150}\\
        0,\;\text{otherwise}
        \end {cases}
$$
6. Self Answering Message
$$
    F_6 = 
        \begin {cases}
        1,\;\text{message\,is\,self\,answered\,type}\\
        0,\;\text{otherwise}
        \end {cases}
$$
7. Smishing symbol 
$$
    F_7 = 
        \begin {cases}
        1,\;\text{if\,message\,contain\,any\,smishing\,symbol}\\
        0,\;\text{otherwise}
        \end {cases}
$$
8. Smishing keywords
$$
    F_8 = 
        \begin {cases}
        1,\;\text{if\,message\,contain\,any\,smishing\,keyword}\\
        0,\;\text{otherwise}
        \end {cases}
$$
9.  Presence of mobile number
$$
    F_9 = 
        \begin {cases}
        1,\;\text{if\,message\,contain\,mobile\,number}\\
        0,\;\text{otherwise}
        \end {cases}
$$
10. Presence of email address
$$
    F_9 = 
        \begin {cases}
        1,\;\text{if\,message\,contain\,email\,address}\\
        0,\;\text{otherwise}
        \end {cases}
$$