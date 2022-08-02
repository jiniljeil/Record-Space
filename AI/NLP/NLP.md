# NLP (Natural Language Processing)
> 인공지능의 한 분야로서 머신러닝을 사용하여 텍스트와 데이터를 처리하고 해석하는 기술

## 임베딩 (Embedding) 
> 자연어 처리(NLP) 분야에서 임베딩이란 사람이 쓰는 자연어를 기계가 이해할 수 있는 숫자의 나열인 벡터로 바꾼 결과 혹은 그 일련의 과정 전체를 의미 

임베딩은 단어나 문장 각각을 벡터로 변환해 벡터 공간에 '끼워 넣는다'는 취지에서 임베딩이라는 이름이 붙었다. 컴퓨터는 임베딩을 계산, 처리해 자연어 형식의 답변을 출력함으로써 인간과 상호작용할 수 있게 된다. 

<strong>즉, 임베딩은 컴퓨터가 자연어를 이해하도록 하는 첫 관문으로 매우 중요한 기능을 한다. </strong>

<details>
<summary>임베딩의 발전 과정</summary>
임베딩 기법은 아래와 같이 발전해왔다.   

1. 통계 기반에서 뉴럴 네트워크 기반
2. 단어 수준에서 문장 수준 기반
3. 엔드투엔드에서 프리트레인/파인 튜닝 방식
   
</details>
### :star: 임베딩이 중요해진 이유 
<strong>특정 문제를 풀기 위해 학습한 모델을 다른 문제를 푸는 데 재사용하는 기법인 전이 학습(transfer learning)과 품질 좋은 임베딩을 쓰면 원하는 모델을 빠르고 효율적으로 학습할 수 있기 때문이다. </strong>

#### :bulb: 전이학습 (transfer learning) 이란? 
임베딩은 다른 딥러닝 모델의 입력값으로 자주 쓰이는데 품질 좋은 임베딩을 사용하면 분류 정확도와 학습 속도가 올라간다. 이렇게 임베딩을 다른 딥러닝 모델의 입력값으로 쓰는 기법을 전이학습이라고 한다. 

전이 학습은 사람의 학습과 유사하여 전이 학습 모델은 0부터 시작하지 않고 대규모 말뭉치(corpus)를 활용해 임베딩을 미리 만들어 놓는다. 임베딩은 의미적, 문법적 정보 등이 녹아있다. 

## :star: 임베딩의 역할 
단어를 벡터로 임베딩하는 순간 단어 벡터들 사이의 유사도(similarity)를 계산하는 일이 가능해진다. <strong>즉, 자연어일 때는 불가능했던 코사인 유사도 계산이 임베딩 덕분에 가능해졌다. </strong>

- 단어/문장 간 관련도 계산
- 의미적/문법적 정보 함축
- 전이 학습

단어 수준의 임베딩 기법은 동음이의어를 분간하기 어렵다는 단점을 가지고 있다. 반면에, 문장 수준의 임베딩 기법은 개별 단어가 아닌 단어 시퀀스 전체의 문맥적 의미를 함축하기 때문에 단어 임베딩 기법보다 전이 효과(transfer learning) 효과가 좋은 것으로 알려져있다. 

## 1. 단어 수준의 임베딩 기법   

- NPLM
- Word2Vec
- FastText
- LSA
- GloVe
- Swivel

## 2. 문장 수준의 임베딩 기법    

- LSA
- Doc2Vec
- LDA
- ELMo
- BERT

## :star: 임베딩의 종류와 성능

### 1. 행렬 분해 기반 방법 (GloVe, Swivel)

말뭉치(corpus) 정보가 들어있는 원래 행렬을 두 개 이상의 작은 행렬로 쪼개는 방식의 임베딩 기법을 가리킨다. 분해한 후 둘 중 하나의 행렬만 쓰거나 둘을 더하거나 이어 붙여 임베딩으로 사용한다. 

### 2. 예측 기반 방법 (Word2Vec, FastText, BERT, ELMo, GPT)

어떤 단어 주변에 특정 단어가 나타날지 예측하거나, 이전 단어들이 주어졌을 때 다음 단어가 무엇일지 예측하거나, 문장 내 일부 단어를 지우고 해당 단어가 무엇일지 맞추는 과정에서 학습하는 방법이다. 

### 3. 토픽 기반 방법 (LDA) 

주어진 문서에 잠재된 주제를 추론하는 방식으로 임베딩을 수행하는 기법이다.  

#### 사전 지식 
- 벡터 공간 (vector space)
- 벡터와 행렬의 미분 (vector, matrix, derivative)
- 벡터의 내적 (inner product), 코사인 유사도 (cosine similarity)
- 고유 분해 (eigendecomposition)
- 우도 함수 (likelihood function)와 최대우도추정 (maximum likelihood estimation)
- 엔트로피 (entropy), 크로스 엔트로피 (cross entropy)
- 그래디언트 디센트 (gradient descent)
- 사전 확률 (prior probability), 사후 확률 (posterior probability)
- 선형회귀 (linear regression)
- 이항 로지스틱 회귀 (binomial logistic regression), 시그모이드 함수 (sigmoid)
- 다항 로지스틱 회귀 (multinomial logistic regression), 소프트맥스 함수 (softmax)
- 피드포워드 뉴럴 네트워크 (feedforward neural network)
- CNN
- RNN
