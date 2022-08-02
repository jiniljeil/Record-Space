# Flutter Emoji


Emoji의 유니코드는 아래와 같이 되어 있다.
ex) U+1234

'\u{}' 안에 넣고자 하는 이모지의 유니코드를 입력하면 된다.
여기에서 U+ 이후의 부분을 괄호 안에 작성해주면 된다.


Emoji(이모티콘)들의 유니코드는 아래의 사이트에서 참고하여 사용하면 된다.
https://apps.timwhitlock.info/emoji/tables/unicode

```dart
Text("\u{1F622}"); // 울음 이모지
```