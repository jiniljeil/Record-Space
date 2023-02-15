## 세션 관리
```bash
# 세션 생성
$ tmux

# 이름을 지정하여 세션 생성
$ tmux new -s <session_name>
$ tmux new-session -s <session_name>

# 세션 이름 수정
[Ctrl] + b, $

# 세션 detach
[Ctrl] + b, d

# 세션 리스트보기
$ tmux ls

# 세션 attach
$ tmux attach -t <session number 혹은 session name>

# 세션 종료, 세션의 마지막 윈도우, 마지막 팬에서 실행
$ exit

# 세션 종료, 세션 밖에서 실행
$ tmux kill-session -t session_name
```

## 팬 관련

```bash
# 세로 화면 분할
[Ctrl] + b, %

# 가로 화면 분할
[Ctrl] + b, "

# 팬 이동 - 화면에 나오는 숫자로 이동
[Ctrl] + b, q

# 팬 이동 - 순서대로 이동
[Ctrl] + b, o

# 팬 이동 - 방향키로 이동
[Ctrl] + b, <방향키>

# 팬 삭제
[Ctrl] + d
[Ctrl] + b, x

# 팬 사이즈 조절 - 현재 포커스된 팬 전체화면(한번 더 실행하면 윈상복구)
[Ctrl] + b, z

# 팬 사이즈 조절 [Ctrl] + b 를 누른 후 :
[Ctrl] + b, :
resize-pane -L or -R or -U -D

# 팬 레이아웃 변경 (다양한 레이아웃으로 자동 전환)
[Ctrl] + b, spacebar
```