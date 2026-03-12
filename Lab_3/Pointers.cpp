#include <iostream>
using namespace std;

int* createArray(int size) {
    int* arr = new int[size];
    return arr;
}

void printArray(int* arr, int size) {
    for(int* i=arr;i<size + arr;i++) {
        cout<<*i<<" ";
    }
    cout<<endl;
}

int findSum(int* arr, int size) {
    int sum = 0;
    for(int* i=arr; i<(size+arr); i++) {
        sum += *i;
    }
    return sum;
}

void swapValues(int* x, int* y) {
    int temp = *x;
    *x = *y;
    *y = temp;
}

void shiftRight(int* arr, int size) {
    int last = *(arr+size-1);

    for(int* i=(arr+size-1); i>arr; i--) {
        *i = *(i-1);
    }

    *arr = last;
}

void deleteArray(int* arr) {
    delete[] arr;
}

int main() {
    cout<<"Creating dynamic array..."<<endl<<endl;
    cout<<"Enter array size: ";
    int size;
    cin>>size;

    int* values = createArray(size);

    cout<<"Enter values: ";
    for(int i=0;i<size;i++) {
        cin>>values[i];
    }

    cout<<endl<<"Array elements: "<<endl;
    printArray(values, size);

    cout<<endl<<"Sum of elements: ";
    cout<<findSum(values, size);
    cout<<endl<<"------------------------------"<<endl;

    cout<<"swapping two numbers"<<endl<<endl;
    cout<<"Before swap"<<endl;
    int a = 5;
    int b = 8;
    cout<<"a = "<<a<<endl;
    cout<<"b = "<<b<<endl<<endl;

    swapValues(&a, &b);

    cout<<"After swap"<<endl;
    cout<<"a = "<<a<<endl;
    cout<<"b = "<<b<<endl;
    cout<<"---------------------------------"<<endl;

    cout<<"Shifting Array to the right..."<<endl<<endl;
    shiftRight(values, size);

    cout<<"Array after shiftRight:"<<endl;
    printArray(values, size);
    cout<<"----------------------------"<<endl;

    cout<<"Deleting array..."<<endl;
    deleteArray(values);
    cout<<"Memory released successfully.";


    return 0;

}