# Pub.dev

- table_calendar
  - pub.dev [https://pub.dev/packages/table_calendar]
  - github [https://github.com/aleksanderwozniak/table_calendar]

```dart
Widget _calendar_content() {
  var _now = DateTime.now() ;

  CalendarFormat _calendarFormat = CalendarFormat.month;
  DateTime? _selectedDay;
  List<String> days = ['_', '월', '화', '수', '목', '금', '토', '일'];

  return Container(
    child: TableCalendar(
      firstDay: DateTime(_now.year, _now.month, 1),
      lastDay: DateTime(_now.year, _now.month + 1, 0),
      focusedDay: _now,
      calendarFormat: _calendarFormat,
      daysOfWeekHeight: 30,
      headerVisible: false,
      calendarBuilders: CalendarBuilders(
        dowBuilder: (context, day) {
          return Center(child: Text(days[day.weekday])) ;
        },

        todayBuilder: (context, date, _) {
          return Container(
          width: MediaQuery.of(context).size.width * 0.11,
          padding: const EdgeInsets.only(bottom: 5),
          child: Image.asset('assets/images/attendance.png',));
        },  
      ),
      selectedDayPredicate: (day) {
      // Use `selectedDayPredicate` to determine which day is currently selected.
      // If this returns true, then `day` will be marked as selected.

      // Using `isSameDay` is recommended to disregard
      // the time-part of compared DateTime objects.
      return isSameDay(_selectedDay, day);
      },
      onDaySelected: (selectedDay, focusedDay) {
        if (!isSameDay(_selectedDay, selectedDay)) {
          // Call `setState()` when updating the selected day
          setState(() {
            _selectedDay = selectedDay;
            _now = focusedDay;
          });
        }
      },
      onFormatChanged: (format) {
        if (_calendarFormat != format) {
          // Call `setState()` when updating calendar format
          setState(() {
          _calendarFormat = format;
          });
        }
      },
      onPageChanged: (focusedDay) {
      // No need to call `setState()` here
        _now = focusedDay;
      },
    ),
  )
}
```

## 코드 결과
<img src="images/table_calendar.png" width="300px"/>
