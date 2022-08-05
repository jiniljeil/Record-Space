
## 논문 
Feature Based Approach for Detection of Smishing Messages in the Mobile Environment

Journal of Information Technology ResearchVolume 12Issue 2Apr 2019 pp 17–35. https://doi.org/10.4018/JITR.2019040102

<hr> 

## Personal thinking

본 논문의 경우, 스미싱 유형을 탐지하기 위해 여러 가지 특징들을 추출하는 과정을 거친다. 총 10가지 정도의 특징이 스미싱을 탐지하는데 있어 유미의한 라벨들로 활용될 수 있다고 생각한다. 

하지만, 전처리 이후 데이터 셋에 5,169개 문자 중 스미싱 문자 개수가 362개 밖에 안된다는 점에서 스미싱 데이터가 조금 더 있었으면 더 좋은 결과가 나오지 않았을까 하는 생각이 들었다.
<hr>

본 연구에서는 모바일 스미싱 탐지에 적합한 특징(feature)들을 식별한다. message-history 또는 third-party services에 의존하지 않고 메세지 내용으로부터 특징들을 추출하였다. 제로 데이(zero-day) 스미싱 공격에도 높은 정확성을 보였다.

## 1. 스미싱 공격 사이클

일반적으로 스미싱 공격이 이루어지는 방식은 아래와 같다. 

1. 피싱 웹/앱 구축
   fake-website를 만들어 실제 웹 사이트 인 것처럼 위장한 다음 악성 앱을 다운로드 받도록 유도하는 방식
2. fake link 전송
   SMS에 fake link를 포함시켜 전송 
3. fake website에 접속하여 악성 앱 설치
   유저가 URL을 클릭하여 웹 사이트에 접속하게 될 경우, 악성 앱이 설치되는 방식
4. 개인 정보 탈취 
   신용 정보 또는 민감한 정보들을 탈취

## 2. 스미싱 유형

본 논문에서 지정한 스미싱 유형은 아래와 같이 총 6가지로 구성되어있다. 

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
   
본 논문에서는 정상 문자의 경우 0을 스미싱의 경우 1로 지정하였다.   
   
$$
    value = 
        \begin {cases}
        1, \text{smishing}\\
        0, \text{ham}
        \end {cases}
$$

1. Greetings keywords
   ex. Good Morning, Good Afternoon, Good evening, etc.

$$
    F_1 = 
        \begin {cases}
        0, \text{if message contains any greeting token}\\
        1, \text{otherwise}
        \end{cases}
$$

2. Presence of emotions
   ex. ":)", ":(", etc.

$$
    F_2 = 
        \begin {cases}
        0, \text{message contains positive or negative emotions}\\
        1, \text{otherwise}
        \end {cases}
$$

3. Presence of URL 
   Long URL로 전환

$$
    F_3 = 
        \begin {cases}
        1, \text{if URL present in message}\\
        0, \text{otherwise}
        \end {cases}
$$

4. Presence of Mathematical Symbols 
    '+', '%', '-', '/', '^' 수학 기호 확인

$$
    F_4 = 
        \begin {cases}
        1, \text{if message contains mathematical symbol}\\
        0, \text{otherwise}
        \end {cases}
$$

5. Message length
   공백, 기호, 특수 문자 등을 포함한 문자 길이

$$
    F_5 = 
        \begin {cases}
        1, \text{if message length}\geq\text{150}\\
        0, \text{otherwise}
        \end {cases}
$$

6. Self Answering Message
   'yes', 'no'를 묻는 메세지

$$
    F_6 = 
        \begin {cases}
        1, \text{message is self answered type}\\
        0, \text{otherwise}
        \end {cases}
$$

7. Smishing symbol 
   '\$' (Dollar), '£' (Pound) 

$$
    F_7 = 
        \begin {cases}
        1, \text{if message contain any smishing symbol}\\
        0, \text{otherwise}
        \end {cases}
$$

8. Smishing keywords
   award, congratulation, winner, alert, claim, activate, verify, attempts, gift voucher, blocked, suspend, unlock, won, prize, subscribe, activity, update, coupon, refund

$$
    F_8 = 
        \begin {cases}
        1, \text{if message contain any smishing keyword}\\
        0, \text{otherwise}
        \end {cases}
$$

9.  Presence of mobile number

$$
    F_9 = 
        \begin {cases}
        1, \text{if message contain mobile number}\\
        0, \text{otherwise}
        \end {cases}
$$

10. Presence of email address

$$
    F_{10} = 
        \begin {cases}
        1, \text{if message contain email address}\\
        0, \text{otherwise}
        \end {cases}
$$

## 4. 데이터 셋 & 평가

5,574 text messages (4,827 ham and 747 spam) 

전처리 이후, 5,169 (4,808 ham and 362 spam) 

$$
Accuracy = \frac{TP + TN}{TP + FN + TN + FP}
$$

## 5. 실험 Setup & Outcome

### 5.1 Setup 
10-fold cross-validation 

- Training dataset: 90 %
- Testing dataset: 10 %

### 5.2 Outcome

#### 5.2.1 Confusion Matrix 
<table>
    <thead> 
        <tr> 
            <td></td>
            <td style="text-align: center">Smishing Messages</td>
            <td style="text-align: center">Ham Messages</td>
        </tr>
    </thead> 
    <tbody> 
        <tr>
            <td>Classified as Smishing</td>
            <td style="text-align: center">TP = 341</td>
            <td style="text-align: center">FP = 44 </td> 
        </tr>
        <tr>
            <td>Classified as Ham</td> 
            <td style="text-align: center">FN = 21</td>
            <td style="text-align: center">TN = 4764</td>
        </tr>
    </tbody>
</table> 


#### 5.2.2 Results of proposed approach on popular classifiers

Random Forest ROC Curve = 0.9879

<table> 
    <thead>
        <tr> 
            <td></td>
            <td style="text-align: center">SVM</td>
            <td style="text-align: center">Logisitic Regression</td>
            <td style="text-align: center">Neural Network</td>
            <td style="text-align: center">Naive Bayes</td>
            <td style="text-align: center">Random Forest</td>
        </tr>
    </thead> 
    <tbody> 
        <tr> 
            <td>TPR (%)</td> 
            <td style="text-align: center">89.50%</td>
            <td style="text-align: center">93.92%</td>
            <td style="text-align: center">88.67%</td>
            <td style="text-align: center">94.20%</td>
            <td style="text-align: center">94.20%</td>
        </tr>
        <tr> 
            <td>TNR (%)</td> 
            <td style="text-align: center">99.08%</td>
            <td style="text-align: center">98.73%</td>
            <td style="text-align: center">98.86%</td>
            <td style="text-align: center">98.69%</td>
            <td style="text-align: center">99.08%</td>
        </tr>
        <tr> 
            <td>Accuracy (%)</td> 
            <td style="text-align: center">98.41%</td>
            <td style="text-align: center">98.39%</td>
            <td style="text-align: center">98.14%</td>
            <td style="text-align: center">98.37%</td>
            <td style="text-align: center; font-weight:bold">98.74%</td>
        </tr>
    </tbody>
</table>

#### 5.2.3 Information gain values of proposed feature set

1. Smishing Keywords (0.25109) 
2. Smishing Symbol (0.15977) 
3. Presence of Mobile number (0.13883) 
4. Presence of URL (0.06092) 
5. Mathematical symbol (0.05917) 
6. Message Length (0.0552) 
7. Self Answering SMS (0.01053) 
8. Emotion symbols (0.00683) 
9. Greeting token (0.00525) 
10. Presence of email address (0.00488)

