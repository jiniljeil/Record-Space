# Machine Learning

> <cite>Field of study that gives computers the ability to learn without being explicitly programmed -- Arthur Samuel (1959)
</cite>


- Limitations of explicit programming 
  - Spam filter: many rules
  - Automatic driving: too many rules


스팸 필터와 자율 주행과 같은 경우는 너무나도 많은 경우의 수(Rules)들이 존재한다. 

## Supervised/Unsupervised learning

학습을 위해 미리 데이터가 주어져야한다. 학습하는 방법에 따라 두 가지로 나누어질 수 있다. 

### Supervised learning 
> 정해져있는 데이터로 학습하는 것 
- learning with labeled examples - dataset

#### 예시
  - Image labeling: learning from tagged images
  - Email spam filter: learning from labeld (spam or ham) email
  - Predicting exam score: learning from previous exam score and time spent

#### ML Algorithm 
- <strong>Regression</strong>
  - ex) Predicting final exam score based on time spent (0 ~ 100) 
- <strong>Binary classification</strong>
  - ex) Pass/non-pass based on time spent (P/F)
- <strong>Multi-label classification</strong>
  - ex) Letter grade (A,B,C,E and F) based on time spent

### Unsupervised learning
> 레이블들이 정의되지 않은 데이터로 학습하는 것
- Google news grouping
    유사한 뉴스를 Grouping 하는 작업 - 미리 레이블을 지정하기 어렵다.
- Word clustering
    비슷한 단어들을 모으는 작업 - 데이터를 보고 스스로 학습함. 


