## Security Objectives (정보보안의 3대 요소)

1. Integrity (무결성) 
    메세지 전송 도중 내용이 바뀌어선 안된다. 
2. Availability (가용성)
    권한을 가진 사람은 언제든 서비스를 이용할 수 있어야한다. 
3. Confidentiality (기밀성, privacy)
    송신자와 수신자만 메세지의 내용에 접근 가능해야한다. 

## Security vs Attack
- Integrity vs Modification
- Authentication vs Fabrication 
- Confidentiality vs Interception 
- Availability vs Interruption (Denial of Service)

### Non-repudiation
    어떤 일을 저지른 후에 자신이 하지 않았다고 부인하는 것

### Access Control 
    유저별 데이터 접근 권한 관리
- Role management
  유저(User)가 어떤 행위를 하는지에 중점
- Rule management
  자원(Resources)에 중점

### OSI Standard for Security Model 

- Authentication
- Access Control 
- Non-repudiation
- Data Integrity
- Confidentiality
- Availability or Assurance
- Signature or Notarization

## Security Attacks
- ### Passive Attacks (Interception)
  시스템 자원에 영향을 주지 않으면서 데이터를 훔쳐보는 것
  <strong>공격 유형: </strong> 
  - Release of message contents
  - Traffic analysis
  
  <strong>해결책: </strong> 일반적으로 탐지하기 어렵고 막아야한다.
- ### Active Attacks
  시스템 자원을 바꾸려고 시도하거나 영향을 주는 것
  <strong>공격 유형: </strong> 
  - Interruption (or Masquerade) 
    Masquerade : 자신이 유저 A인 것처럼 속이는 것
  - Modification (Replay attacks, Alterations)
    중간에서 메세지 갭쳐, 수정, 전송 
    - Replay attacks
      ex, 계좌에 10만원 송금을 반복적으로 요청
    - Alterations 
      ex, 메세지 내용 변경
  - Fabrication (DoS)
    시스템 이용을 불가능한 상태로 만듦

## 공격 유형

- Application-level Attacks 
  애플리케이션의 정보에 접근하거나, 수정 또는 막는 행위
- Network-level Attacks
  트래픽 증가

## 프로그램 공격 유형
- ### Virus 
    A virus is a computer program that attaches itself to another legitimate program, and causes damage to the computer system or to the network. 

    - A piece of program code that attaches itself to legitmate program code, and runs when the legitimate program runs. 

    - <strong>Viruses can also be triggered by specific events. </strong>
- ### Worm
    A worm does not perform any destructive actions, and instead, only consumes system resources to bring it down. 

    - A virus modifies a program, while a worm does not modify a program. <strong>it replicates itself again and again. </strong>
- ### Trojan Horse
    A Trojan horse allows an attacker to obtain some confidential information about a computer or a network. 
    - A Trojan horse is a hidden piece of code, like virus. 
    - A Trojan horse attempts to reveal confidential information to an attacker. 
