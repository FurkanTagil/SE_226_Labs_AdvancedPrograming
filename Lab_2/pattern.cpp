#include <iostream>
using namespace std;

int main() {
    int n;

    cout << "Please enter a number between 3 and 9: ";
    cin >> n;

    while (n < 3 || n > 9) {
        cout << "Invalid input, enter again: ";
        cin >> n;
    }

    for (int i=1; i<=2*n-1; i++) {

        int k;

        if (i <= n) {
            k = i;
        }
        else {
            k = 2*n - i;
        }
        for (int j = 1; j <= k; j++) {
            cout << "*";
        }

        cout << endl;
    }

    return 0;
}