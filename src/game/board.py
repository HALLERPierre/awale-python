from .constants import CONST_PEBBLE_COUNT

def newBoard(size):
    if size is None or size % 2 != 0:
        raise ValueError("Board size size must be even.")

    # Create a new board, simple array
    return [CONST_PEBBLE_COUNT] * size

def render(board):
    renderStr = ''

    half = int(len(board) / 2)

    #Board top
    renderStr += displayRow(board[:half])

    renderStr += '\n'

    #Board bottom
    renderStr += displayRow(board[half:], half)

    return renderStr


def displayRow(board, startIndex = 0):
    #Display with index

    renderStr = ''

    for index, row in enumerate(board):
        renderStr += str(index + 1 + startIndex) +  '(' + str(row) + ') '

    return renderStr

def canPlay(player, board, position):
    return True
