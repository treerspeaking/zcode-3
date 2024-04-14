#include <iostream>
using namespace std;

// int somefunc(int a, int a){
//     return a;
// }


int main(){
    int a = 0;

    if(true) int a = 1;
    cout << a <<endl;
    if(true) {int a = 2; cout << a <<endl;}
    cout << a <<endl;
}