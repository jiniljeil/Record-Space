## Cryptography

> Cryptography is the art of achieving security by **encoding** messages to make them **non-readable**. 

## Cryptanalysis (code breaking)

> Cryptanalysis is the technique of **decoding** messages from a non-readable format back to a readable format **without knowing how they were initially converted from readable format to non-readable format**. 

## Cryptology 

> Cryptology is a combination of cryptography and cryptanalysis. 

## Basic Concept 

Plain Text (Clear Text) : 쉽게 이해할 수 있는 언어
Cipher Text : 이해할 수 없는 언어

## Transformation 

- ### Substitution
    In the substitution cipher technique, the characters of a plain-text message are replaced by other characters, numbers or symbols. 

- ### Transposition
    

- ### Product Cipher
  Substitution + Transposition = Product Cipher

## Substitution

  - ### Caesar Cipher 
  
    카이사르 암호화 방식은 알파벳의 자리를 옮겨 평문을 서로 매칭되는 알파벳으로 변환하는 암호화 방식

    예를 들어, 알파벳 자리를 2칸씩 옮긴 경우, A -> C, B -> D, Z -> B

    Brute-force 공격 시, 바로 해독 가능 

  - ### Mono-alphabetic Cipher (one-to-one) 
  
    *Mono-alphabetic ciphers pose a difficult problem for a cryptanalyst because it can be very difficullt to crack, thanks to the high number of permutations and combinations.*
    
    **Additive Cipher (Shift Cipher)** (경우의 수)

    $$
        4 \times 10^{26} = (26 \times 25 \times 24\ ...\ 2)
    $$

    $$    
        C = (P + K)\ mod\ 26,\ P = (C - K)\ mod \ 26
    $$

    **한계점** 
    영어에서 알파벳 별 빈도수 통계 값을 활용하면 금방 해독 가능 

  - ### Homophonic Substitution Cipher (one-to-many) 
    
    *Homophonic substitution cipher also involves substitution of one plain-text character with a cipher-text character at a time, however the cipher-text character can be any one of the chosen set.* 

    - one plain-text alphabet can map to more than one cipher-text alphabet. 
    
    **예시**
    A = [D, H, P, R] 예를 들어, 알파벳 A가 D, H, P, R 중에 하나로 변경하여 암호화

  - ### Polygram Substitution Cipher (block-to-block)
    Polygram substitution cipher technique **replaces one block of plain text with another block of cipher text**. it does not work on a character-by-character basis.

    For instance, 
    - HELLO -> YUQQW
    - HELL -> TEUT
    
  - ### Poly-alphabetic Substitution Cipher (one-to-many, the period of the cipher)
     
    - It uses a set of related **monoalphabetic substitution rules**.
    - It uses **a key that determines which rule is used for which transformation**.
    
    For instance,
    - hello hi (07 04 11 11 14 07 08) + key (12 00 19 13 5) = (21 04 4 24 19 19 08) 
      
## Transposition 

*A transposition cipher does not substitute one symbol for another, instead it changes the location of the symbols.*

**A transposition cipher reorders symbols**

  - ### Rail Fence (Keyless transposition)
    *Rail-fence technique involves writing plain text as a sequence of diagonals and then reading it row by row to produce cipher text.*

    For instance, 
    "Come home tomorrow" -> "Cmhmtmrooeoeoorw" 

  - ### Simple Columnar Transposition (Keyless transposition)
    *The simple columnar transposition technique simply arranges the plain text as a sequence of rows of a rectangle that are read in columns randomly.*

    For instance, the number of columns is four. 
    "the school is good"

        t h e s  
        c h o o
        l i s g
        o o d

    the order of columns as some random order, say 2, 3, 1, 4. 
    Encrpytion: **"hhioeosdtclosog"**

  - ### Simple Columnar Transposition with Multiple Rounds (Keyless transposition)
    
    *Cipher text produced by the simple columnar transposition technique with multiple rounds is much more complex to crack as compared to the basic technique.*
    
    Round 2, "hhioeosdtclosog" , [2, 3, 1, 4]

        h h i o 
        e o s d
        t c l o 
        s o g

    Encryption: **"hocoislghetsodo"**

  - ### Vernam Cipher (One Time Pad, Keyed transposition) 
    
    *Vernam Cipher uses a one-time pad, which is discarded after a single use, and therefore, is suitable only for short messages.*

    For instance, Poly-alphabetic Substitution Cipher 와는 달리 One-time pad 를 다시 사용하지 않음

    <img src="https://github.com/jiniljeil/Record-Space/blob/master/Computer%20Security/images/vernam_cipher.png" height="200px">

    짧은 문장에서 유용하며, 긴 문장에서는 실용적이지 않다. 
