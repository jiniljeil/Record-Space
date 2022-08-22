# TextButton Background Color

`ButtonStyle` 에 backgroundColor는 `MaterialStateProperty.all<Color>(Colors.green)`를 사용하여 변경한다. 

## Code 

```dart
Widget _check_button() {
    return TextButton(
        style: ButtonStyle(
            backgroundColor: MaterialStateProperty.all<Color>(AppTheme.blueText), 
        ),
        child: const Text('확인', style: AppTheme.whitetitle),
        onPressed: () { },
    );
}
```