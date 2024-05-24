#include <iostream>
#include <string>

using namespace std;

long long int factorial(long long int n) {
    if (n == 0 || n == 1)
        return 1;
    return n * factorial(n - 1);
}

long long int nCr(long long int n, long long int k) {
    long long int result = 1;
    for (long long int i = 1; i <= k; ++i) {
        result *= (n - i + 1);
        result /= i;
    }
    return result;
}

string BinomialTheorem(long long int n) {
    string result = "";
    for (long long int k = 0; k <= n; k++) {
        long long int coefficient = nCr(n, k);
        if (coefficient != 1) {
            result += to_string(coefficient);
        }
        if (n - k > 0) {
            if (coefficient != 1) {
                result += "*";
            }
            result += "a";
            if (n - k > 1) {
                result += "^" + to_string(n - k);
            }
        }
        if (k > 0) {
            if (coefficient != 1 || (n - k > 0)) {
                result += "*";
            }
            result += "b";
            if (k > 1) {
                result += "^" + to_string(k);
            }
        }
        if (k < n) {
            result += " + ";
        }
    }
    return result;
}

int main() {
    long long int n;
    cout << "Enter the value of n: ";
    cin >> n;

    string expansion = BinomialTheorem(n);
    cout << "Expansion: " << expansion << endl;

    return 0;
}
