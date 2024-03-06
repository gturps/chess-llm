from flask import Flask, render_template, jsonify, request
from openai import OpenAI
import chess
import chess.svg
import requests

client = OpenAI(api_key='Your_API_key')

app = Flask(__name__)
board = chess.Board()  # Create a new chess board instance

def get_turn():
    return 'White' if board.turn else 'Black'

def get_response(prompt):
  # Create a request to the chat completions endpoint
  response = client.chat.completions.create(
    model="gpt-4-0125-preview",
    # Assign the role and content for the message
    messages=[{"role": "user", "content": prompt}], 
    temperature = 0)
  return response.choices[0].message.content

@app.route('/')
def home():
    # Render the chess board on the homepage
    return render_template('index.html', board=chess.svg.board(board=board), turn=get_turn())

@app.route('/ai_move', methods=['GET'])
def ai_move():
    # Convert the board to a string format or FEN that the AI can understand
    board_fen = ""
    board_fen = board.fen()
        
    prompt = f"""Act as a grandmaster analyzing the chessboard represented by this FEN: {board_fen}.
Instructions:
1. Your task is to determine a legal and strategic next move.
2. Ensure the move is valid based on the board's current state, follows all chess rules, and does not repeat previous moves.
3. Provide your best move in UCI notation ONLY. Do NOT use standard algebraic notation (e.g., avoid 'Nf3').
4. Provide your chain of thoughts and explain your choice.
5. Provide the move delimited by 3# ie ###g1f3###
"""
    
    # Extract the move from the response
    ai_answer = get_response(prompt)
    print(ai_answer)
    split_text = ai_answer.split("###")
    ai_move = split_text[1]
    

    # Validate and make the AI move
    try:
        move = chess.Move.from_uci(ai_move)
        if move in board.legal_moves:
            board.push(move)
            return jsonify({'board': chess.svg.board(board=board), 'status': 'success', 'game_over': board.is_game_over(), 'turn': get_turn()})
        else:
            return jsonify({'status': 'error', 'message': 'AI made an illegal move'})
    except ValueError:
        return jsonify({'status': 'error', 'message': 'AI move could not be interpreted'})



@app.route('/move', methods=['POST'])
def make_move():
    data = request.json
    try:
        move = chess.Move.from_uci(data['move'])
        if move in board.legal_moves:
            board.push(move)  # Make the move
            return jsonify({'board': chess.svg.board(board=board), 'status': 'success', 'game_over': board.is_game_over(), 'turn': get_turn()})
        else:
            return jsonify({'status': 'error', 'message': 'Illegal move'})
    except ValueError:
        # This handles cases where the move is not in UCI format or is invalid
        return jsonify({'status': 'error', 'message': 'Invalid move format'})

@app.route('/reset', methods=['GET'])
def reset_board():
    board.reset()
    return jsonify({'board': chess.svg.board(board=board), 'status': 'success', 'game_over': False, 'turn': get_turn()})

if __name__ == '__main__':
    app.run(debug=True)

