 #Game_of_life


def neighbours_of_position(matrix, position):
    """ for providing neighbours of a particular position and return all the eight neighbours of that position """
    for sub_list in matrix:
        for j in range(len(matrix)):
            for i in range(len(sub_list)):
                my_pos = [j, i]
                if my_pos == position:
                    neighbours_list = [[j-1, i-1], [j-1, i], [j-1, i+1], [j, i-1], [j, i+1], [j+1, i-1], [j+1, i], [j+1, i+1]]
                    return  neighbours_list

def neighbours(matrix):
    """ provides the eight neighbours of all positions of matrix """
    for sub_list in matrix:
        for j in range(len(matrix)):
            for i in range(len(sub_list)): 
                neighbours_list = [[j-1, i-1], [j-1, i], [j-1, i+1], [j, i-1], [j, i+1], [j+1, i-1], [j+1, i], [j+1, i+1]]
                return  neighbours_list

def real_neighbours(neighbours_list):
    """provide onboard neighbours of all position form total neighbours """
    real_neib_list = []
    for neighbour in neighbours_list:
        for elements in neighbour:
            if elements < 0 or elements > 2:
                neighbour.remove(elements)
        real_neib_list.append(neighbour)
        for posi_list in real_neib_list:
            if len(posi_list) == 1:
                real_neib_list.remove(posi_list)
    return real_neib_list

def count_alive_neighbours(matrix):
    """count number of living neighbours (1) of each position in a matrix """
    rows = len(matrix)
    cols = len(matrix[0])
    result = [[None for i in range(cols)] for j in range(rows)]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            position = [i, j]
            count = 0
            neib = real_neighbours(neighbours_of_position(matrix, position))
            for a in neib:
                row_position = a[0]
                column_position = a[1]
                row = matrix[row_position]
                element = row[column_position]
                if element == 1:
                    count = count + 1        
            result[i][j] = count
    return result

def apply_rules(alive_list, matrix):
    """ Applying four Conway's Game of Life rules"""
    rows = len(matrix)
    columns = len(matrix[0])    
    for i in range(rows):
        for j in range(columns):
            """first and second rules"""
            if matrix[i][j]:
                if alive_list[i][j] < 2 or  alive_list[i][j] > 3:
                    matrix[i][j] = 0
            """third rule"""        
            if matrix[i][j]:
                if alive_list[i][j] == 3 or alive_list[i][j] == 2:
                    matrix[i][j] = 1
            """fourth rule"""
            if matrix[i][j] == 0 and alive_list[i][j] == 3:
                matrix[i][j] = 1
    return matrix
                
def display(board):
    """display the game output in a combination of zeros and period"""
    row = len(board)
    column = len(board[0])
    showcase = ""
    for i in range(row):
        for j in range(column):
            if j == 0:
                showcase += "\n"
            if board[i][j] == 1:
                showcase += "\u0fc7 "
            if board[i][j] == 0:
                showcase += ", "
            
    return showcase
    
