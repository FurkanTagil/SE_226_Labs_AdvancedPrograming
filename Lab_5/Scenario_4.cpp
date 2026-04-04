#include <iostream>
using namespace std;

double geometricSum(int n, double r) {
    
    if (n == 0)
        return 1;

    return (r * geometricSum(n - 1, r)) + 1;
}

int main() {
    int n;
    double r;

    cout << "Enter n (number of terms): ";
    cin >> n;

    cout << "Enter r (common ratio): ";
    cin >> r;

    double result = geometricSum(n, r);

    cout << "Geometric Sum: " << result << endl;

    return 0;
}