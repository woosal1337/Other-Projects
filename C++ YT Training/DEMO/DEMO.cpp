#include <iostream>
#include <vector>
#include <numeric>
#include <string>
#include <functional>
using namespace std;


int main(void) {
    std::vector <std::string> v = { "Hello", "World" };
    std::string sum;

    for (auto i : v) {
        sum += i;
        sum += ' ';
    }

    std::cout << sum << std::endl;

    return 0;
}