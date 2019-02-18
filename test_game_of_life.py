#test_game_of_life

import Game_of_life

def test_matrix():
    assert Game_of_life.matrix(0, 5, 5) == [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

def test_initial_matrix():
    assert Game_of_life.initial_matrix(1, [[0, 0, 0],[1, 1, 1], [0, 0, 0]]
) == [[0, 0, 0],[1, 1, 1], [0, 0, 0]]


    
def test_neighbours():
    assert Game_of_life.neighbours([[0, 0, 0],[1, 1, 1], [0, 0, 0]], [1, 1]) == [[0, 0], [0, 1], [0, 2], [1, 0], [1, 2], [2, 0], [2, 1], [2, 2]]
    assert Game_of_life.neighbours([[0, 0, 0],[1, 1, 1], [0, 0, 0]], [0, 0]) == [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]


def test_real_neighbours():
    assert Game_of_life.real_neighbours([[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]) == [[0, 1], [1, 0], [1, 1]]

def test_position_of_alive_elements():
    assert Game_of_life.position_of_alive_elements([[0, 0, 0],[1, 1, 1], [0, 0, 0]]) == [[1, 0], [1, 1], [1, 2]]
    assert Game_of_life.position_of_alive_elements([[0, 1, 0],[0, 1, 0], [0, 1, 0]]) == [[0, 1], [1, 1], [2, 1]]

def test_apply_rules():
    assert Game_of_life.main([[0, 0, 0],[1, 1, 1], [0, 0, 0]]) == [[0, 1, 0],[0, 1, 0], [0, 1, 0]]
