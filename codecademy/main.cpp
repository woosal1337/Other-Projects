#include <iostream>

// Define is_palindrome() here:
void is_palindrome(std::string text) {
    std::string rev = text.rbegin(),text.rend();
    std::cout << rev;
}


int main() {

    std::cout << is_palindrome("madam") << "\n";
    std::cout << is_palindrome("ada") << "\n";
    std::cout << is_palindrome("lovelace") << "\n";

}