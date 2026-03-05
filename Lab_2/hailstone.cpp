#include <iostream>
using namespace std;
int main() {
    cout<<"Please enter a positive integer greater than 1: ";
    int num;
    cin>>num;
    int counter = 0;

    while(num!=1) {
        if(num%2==0) {
            num = num/2;
            counter++;
            cout<<num << " ==> ";
        }
        else {
            num = (num*3)+1;
            counter++;
            cout<<num << " ==> ";
        }
    }
    cout<<"\nTotal Steps: "<< counter;
}