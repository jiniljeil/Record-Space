#include <iostream> 

using namespace std; 

class Person { 

private: 
    int age ;
    int height ; 
    int weight ; 

public: 

    // copy constructor 
    Person(int a, int h, int w) : age(a), height(h), weight(w) { 
        cout << "[1] This is a copy constructor!" << '\n' ;
    } 

    Person(Person &copy) : age(copy.age), height(copy.height), weight(copy.weight) { 
        cout << "[2] This is a copy constructor!" << '\n' ;
    } 

    void showState() { 
        cout << "age: " << age << ' ' << "height: " << height << ' ' << "weight: " << weight << '\n' ;  
    }
} ;


int main(void) { 

    Person p1(25, 182, 80) ; 

    p1.showState() ; 

    Person p2 = p1 ;

    p2.showState() ;  
    
    return 0 ;
}