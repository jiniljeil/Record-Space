# Container에 배경으로 이미지 추가하는 방법

1. assets 폴더에 이미지 업로드 
2. pubspec.yaml 에서 이미지 경로 추가 후, pug get
3. 아래 코드 작성
4. 재시작

Scaffold 

```dart
Container(
  decoration: const BoxDecoration(
    image: DecorationImage(
      fit: BoxFit.cover, 
      image: AssetImage('image path'), 
    ), 
  ), 
)
```

## 키보드 생성으로 인해 이미지가 올라가는 경우 (해결책) 

```dart
Scaffold(
  ... 
  resizeToAvoidBottomInset: false,
  ... 
) 
```
