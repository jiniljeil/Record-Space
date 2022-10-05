## 암호화/복호화 방법

### 1. Algorithm

DES, RSA 등 암호화 알고리즘을 사용하여 암호화/복호화하는 경우

### 2. Key

Symmetric Key, Asymmetric Key를 사용하여 암호화/복호화하는 경우

## Symmetric Key

같은 키(Symmetric Key)를 사용하여 암호화/복호화

## Asymmetric Key

공개키 (Public Key) / 비밀키 (Private Key)를 사용하여 암호화/복호화

<img src="https://github.com/jiniljeil/Record-Space/blob/master/Computer%20Security/images/key_compare.png" height="400px">

## Key exchange problem 

제 3자 없이 키를 어떻게 안전하게 분배할 수 있는가?

해결책 : Diffie-Hellman Key-Exchange / Agreement Algorithm 

## Diffie-Hellman Algorithm

*The Diffie–Hellman key exchange algorithm can be used only for key agreement, but not for encryption or decryption of messages.*

<img src="https://github.com/jiniljeil/Record-Space/blob/master/Computer%20Security/images/diffie-hellman.png" height="400px">

<img src="https://github.com/jiniljeil/Record-Space/blob/master/Computer%20Security/images/diffie-hellman_.png" height="400px">

예를 들어, n = 11, g = 7 이라고 가정

유저 A는 x = 3, 유저 B는 y = 6 선택

$$
    A = 7^3\ mod\ 11 = 343\ mod\ 11 = 2
$$

유저 A는 유저 B에게 2를 전달

$$
    B = 7^6\ mod\ 11 = 117649\ mod\ 11 = 4
$$

유저 B는 유저 A에게 4를 전달

유저 A
$$
    K1\ = 4^3\ mod\ 11 = 64\ mod\ 11 = 9
$$

유저 B
$$
    K2\ = 2^6\ mod\ 11 = 64\ mod\ 11 = 9
$$

**문제점**
"man in the middle attack" 

<img src="https://github.com/jiniljeil/Record-Space/blob/master/Computer%20Security/images/man_in_the_middle_attack.png" height="400px">

<img src="https://github.com/jiniljeil/Record-Space/blob/master/Computer%20Security/images/man_in_the_middle_attack_.png" height="400px">