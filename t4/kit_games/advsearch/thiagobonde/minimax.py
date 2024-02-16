import random
from typing import Tuple, Callable



def minimax_move(state, max_depth:int, eval_func:Callable) -> Tuple[int, int]:
    """
    Returns a move computed by the minimax algorithm with alpha-beta pruning for the given game state.
    :param state: state to make the move (instance of GameState)
    :param max_depth: maximum depth of search (-1 = unlimited)
    :param eval_func: the function to evaluate a terminal or leaf state (when search is interrupted at max_depth)
                    This function should take a GameState object and a string identifying the player,
                    and should return a float value representing the utility of the state for the player.
    :return: (int, int) tuple with x, y coordinates of the move (remember: 0 is the first row/column)
    """
    alpha = float('-inf')
    beta = float('inf')
    player = state.player

    if max_depth == -1:
        max_depth = float('inf')
    
    value, move = max_v(state, max_depth, eval_func, alpha, beta, player)

    return move
    
def max_v(state, max_depth, eval_func, alpha, beta, player):
    if state.is_terminal() or max_depth == 0:
        return eval_func(state, player), None
    
    value = float('-inf')
    move = None

    for move_coords in state.legal_moves():
        next_state = state.next_state(move_coords)
        min_value, _ = min_v(next_state, max_depth - 1, eval_func, alpha, beta, player)
        if min_value > value:
            value = min_value
            move = move_coords
        alpha = max(alpha, value)
        if alpha >= beta:
            break
    
    return value, move

def min_v(state, max_depth, eval_func, alpha, beta, player):
    if state.is_terminal() or max_depth == 0:
        return eval_func(state, player), None
        
    value = float('inf')
    move = None

    for move_coords in state.legal_moves():
        next_state = state.next_state(move_coords)
        max_value, _ = max_v(next_state, max_depth - 1, eval_func, alpha, beta, player)
        if max_value < value:
            value = max_value
            move = move_coords
        beta = min(beta, value)
        if beta <= alpha:
            break
    
    return value, move
