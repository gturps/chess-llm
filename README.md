# Chess AI Flask App

## Overview
This Flask-based web application allows users to play chess against an OpenAI model. It uses the Python `chess` library to manage game mechanics and integrates with the OpenAI API to generate AI moves. Users can interact with a graphical chessboard, make moves, and receive suggestions from the AI.

## Features
- **Interactive Chessboard:** Play chess directly in your web browser.
- **AI Move Suggestions:** Get move suggestions from an advanced AI trained on numerous chess games.
- **Game State Management:** Track the current state of the game, including who's turn it is and whether the game is over.
- **Move Validation:** Ensures all moves are legal according to chess rules.

## Installation
To run this application, you'll need Python and Flask installed on your system. Follow these steps:

1. Clone the repository to your local machine.
2. Install the required Python packages: `pip install flask chess chess.svg requests openai`.
3. Set your OpenAI API key - do not share it with others or use an environment variable.
5. Run the Flask app: `python chess_app.py`.
6. Open your browser and navigate to `http://127.0.0.1:5000/`.

## Usage
- The homepage displays the chessboard. Choose a piece move by using the UCI notation ie g1f3.
- Click the "AI Move" button to request a move suggestion from the AI.
- Reset the board at any time by clicking the "Reset Board" button.

## Contributing
Feel free to fork the repository, make changes, and submit pull requests. Suggestions and improvements are welcome!

## License
This project is open-source and available under the MIT License.
