
# 트리거 생성 시 에러

`You do not have the SUPER privilege and binary logging is enabled (you *might* want to use the less safe log_bin_trust_function_creators variable)`

트리거를 생성하려고 시도하였을 때, 위와 같은 메세지가 뜨면서 트리거를 등록할 수 없을 경우가 발생할 수 있다. 

이는 `log_bin_trust_function_creators` 속성이 디폴트 값으로 OFF로 설정되어있어 뜨는 것이다. 

## 해결 방법

1. log_bin_trust_function_creators = ON

안정성 체크를 하지 않게되어, 일반 계정으로도 트리거, 함수 등 생성이 가능해지게 된다. 

```SQL
mysql> set global log_bin_trust_function_creators=on ; 
```

2. 생성 작업을 하는 계정에 super 권한을 준다.


