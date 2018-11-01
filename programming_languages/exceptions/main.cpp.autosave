#include <iostream>

double harm(const int&, const int&);

int main() {
    int a,b;
    double ans;
    std::cout << "Enter two numbers to count harmonic mean:\n";
    while (std::cin >> a >> b) {
        try {
            ans = harm(a, b);
        } catch (const char *ex) {
           std::cout << ex << std::endl;
           std::cout << "Enter a new pair of numbers:\n";
           continue;
        }
        std::cout << "Answer is " << ans << std::endl;
    }
    return 0;
}

double harm(const int &m, const int &n) {
    if (m == -n)
        throw "bad arguments: m = -n is now allowed!";
    return 2.0 * m * n / (m + n);
}
