#include <iostream>

void Introduction() {
    // Welcome messages to the terminal (intro)
    std::cout << "\n\nYou are a secret agent breaking into a secure server room...";
    std::cout << std::endl;
}

bool PlayGame(){

    std::cout << "\n\nEnter the correct code to continue...\n\n";

    // Declare 3 number code
    const int CodeA = 4;
    const int CodeB = 3;
    const int CodeC = 2;

    const int CodeSum = CodeA + CodeB + CodeC;
    const int CodeProduct = CodeA * CodeB * CodeC;

    std::cout << std::endl;

    int GuessA, GuessB, GuessC;

    std::cin >> GuessA;
    std::cin >> GuessB;
    std::cin >> GuessC;
//  std::cout <<    "You entered: " << GuessA << " " << GuessB << " " << GuessC;

    int GuessSum = GuessA + GuessB + GuessC;
    int GuessProduct = GuessA * GuessB * GuessC;

    std::cout << std::endl;
    std::cout << "The sum of the Guesses is: " << GuessSum;
    std::cout << std::endl;
    std::cout << "The product of the Guesses is: " << GuessProduct;
    std::cout << std::endl;

    if (GuessA == 5 && GuessB == 6 && GuessC == 7) {
        std::cout << "You Win!";
        return true;
    } else {
        std::cout << "You lost! Try again!";
        return false;
    }

}

int main()
{
    int LevelDifficulty = 1;
    Introduction();
    while (true) {
        bool LevelComplete = PlayGame();
        std::cin.clear();
        std::cin.ignore();

        if (LevelComplete) {
            // Increase the level difficulty
            ++LevelDifficulty;
        }
    }
    return 0;
}