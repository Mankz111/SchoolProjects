#include <SFML/Graphics.hpp>
#include <SFML/Window.hpp>
#include <iostream>
#include <random>
#include <string>

using namespace std;

// Function to get the computer's random choice
string getComputerChoice() {
    random_device rd;
    mt19937 generator(rd());
    uniform_int_distribution<int> dist(1, 3);
    int choice = dist(generator);

    if (choice == 1) return "Rock";
    if (choice == 2) return "Paper";
    return "Scissors";
}

// Function to determine the winner
string determineWinner(const string& player, const string& computer) {
    if (player == computer) return "It's a Tie!";
    if ((player == "Rock" && computer == "Scissors") ||
        (player == "Paper" && computer == "Rock") ||
        (player == "Scissors" && computer == "Paper")) {
        return "You Win!";
    }
    return "Computer Wins!";
}

int main() {
    // Create SFML Window
    sf::RenderWindow window(sf::VideoMode(600, 400), "Rock Paper Scissors");

    // Font and Text setup
    sf::Font font;
    if (!font.loadFromFile("DejaVuSans.ttf")) {
    cerr << "Error loading font. Ensure 'DejaVuSans.ttf' is in the executable directory." << endl;
    return 1;
}

    sf::Text title("Rock Paper Scissors", font, 30);
    title.setPosition(150, 20);
    title.setFillColor(sf::Color::White);

    sf::Text resultText("", font, 25);
    resultText.setPosition(150, 300);
    resultText.setFillColor(sf::Color::Yellow);

    // Button setup
    sf::RectangleShape rockButton(sf::Vector2f(120, 50));
    rockButton.setPosition(100, 150);
    sf::Text rockText("Rock", font, 20);
    rockText.setPosition(130, 160);

    sf::RectangleShape paperButton(sf::Vector2f(120, 50));
    paperButton.setPosition(250, 150);
    sf::Text paperText("Paper", font, 20);
    paperText.setPosition(280, 160);

    sf::RectangleShape scissorsButton(sf::Vector2f(120, 50));
    scissorsButton.setPosition(400, 150);
    sf::Text scissorsText("Scissors", font, 20);
    scissorsText.setPosition(420, 160);

    string playerChoice, computerChoice, result;

    // Game Loop
    while (window.isOpen()) {
        sf::Event event;
        while (window.pollEvent(event)) {
            if (event.type == sf::Event::Closed) {
                window.close();
            }

            // Detect mouse clicks on buttons
            if (event.type == sf::Event::MouseButtonPressed) {
                if (rockButton.getGlobalBounds().contains(event.mouseButton.x, event.mouseButton.y)) {
                    playerChoice = "Rock";
                } else if (paperButton.getGlobalBounds().contains(event.mouseButton.x, event.mouseButton.y)) {
                    playerChoice = "Paper";
                } else if (scissorsButton.getGlobalBounds().contains(event.mouseButton.x, event.mouseButton.y)) {
                    playerChoice = "Scissors";
                }

                if (!playerChoice.empty()) {
                    computerChoice = getComputerChoice();
                    result = determineWinner(playerChoice, computerChoice);
                    resultText.setString("You: " + playerChoice + "\nComputer: " + computerChoice + "\n" + result);
                }
            }
        }

        // Render
        window.clear(sf::Color::Black);
        window.draw(title);
        window.draw(rockButton);
        window.draw(rockText);
        window.draw(paperButton);
        window.draw(paperText);
        window.draw(scissorsButton);
        window.draw(scissorsText);
        window.draw(resultText);
        window.display();
    }

    return 0;
}