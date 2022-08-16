# DateTime

## 현재 날짜 값 가져오는 코드 

```dart 
var now = DateTime.now() ; 
```

## 현재 달 첫날, 마지막 날 구하기

```dart
DateTime(now.year, now.month, 1); // 현재 달 첫날 
DateTime(now.year, now.month + 1, 0); // 현재 달 마지막 날 
```
