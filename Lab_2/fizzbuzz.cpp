#include <iostream>
using namespace std;

int main() {
    int num = 0;
    int FizzBuzzCounter = 0;
    int FizzCounter = 0;
    int BuzzCounter = 0;

    cout << "Enter a positive integer between 10 and 100: ";

    while (true) {
        cin >> num;

        if (num >= 10 && num <= 100) {
            break;
        }
        cout << "Invalid input, enter again: ";
    }

    for (int x = 1; x <= num; x++) {

        if (x % 3 == 0 && x % 5 == 0) {
            FizzBuzzCounter++;
            cout << "FizzBuzz" << endl;
        }
        else if (x % 3 == 0) {
            FizzCounter++;
            cout << "Fizz" << endl;
        }
        else if (x % 5 == 0) {
            BuzzCounter++;
            cout << "Buzz" << endl;
        }
        else if (x % 7 == 0) {
            cout << x << " is skipped" << endl;
        }
        else {
            cout << x << endl;
        }
    }

    cout << "--- Summary ---" << endl;
    cout << "Fizz count: " << FizzCounter << endl;
    cout << "Buzz count: " << BuzzCounter << endl;
    cout << "FizzBuzz count: " << FizzBuzzCounter << endl;

    return 0;
}