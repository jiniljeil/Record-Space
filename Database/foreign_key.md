# Foreign Key 

테이블이 다른 테이블의 데이터를 참조하여 테이블간의 관계를 연결하는 것

부모 테이블: 외래키 값을 제공하는 테이블 
자식 테이블: 외래키 값을 포함하는 테이블

## Condition 

1. Foreign Key 값은 참조 무결성 제약조건을 만족해야한다. 
   즉, 외래키 값은 NULL이거나 참조하는 릴레이션의 기본키 값과 동일해야 한다. 

2. 외래키로 지정할 두 테이블의 필드는 데이터 타입이 동일해야한다. 

3. 부모 테이블의 기본키, 고유기를 외래키로 지정 가능하며, 부모 테이블의 기본키 혹은 고유키가 여러 개의 컬럼으로 구성되어있다면 원하는 개수만큼 묶어서 외래키로 지정 가능하다. 

```SQL
CREATE TABLE parent (
  id INT PRIMARY KEY AUTO_INCREMENT, 
  age INT NOT NULL, 
  year INT NOT NULL
); 

CREATE TABLE child ( 
  id INT PRIMARY KEY AUTO_INCREMENT, 
  parent_id INT NOT NULL, 
  FOREIGN KEY (id) REFERENCES parent(id)
); 
```