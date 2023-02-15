#include <iostream> 

using namespace std; 

class Person { 

private: 
    int age ;
    int height ; 
    int weight ; 

public: 
    Person(int a, int h, int w) : age(a), height(h), weight(w) {} 

    void showState() {
        cout << "[showState()]" << '\n' ;
        cout << "age: " << age << ' ' << "height: " << height << ' ' << "weight: " << weight << '\n' ;  
    }

    void showState() const  { 
        cout << "[const showState()]" << '\n'; 
        cout << "age: " << age << ' ' << "height: " << height << ' ' << "weight: " << weight << '\n' ;  
    }
} ; 

int main(void) {

    Person p1(21, 155, 45) ;
    const Person p2(21, 155, 45) ; 

    p1.showState(); // showState() 
    p2.showState(); // const showState() 
    return 0 ;
}