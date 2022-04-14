def moves(board):
    return [frozenset([(x, y) for (x, y) in board if x > px or y < py]) for (px, py) in board]


def memoize(f):
    cache = dict()

    def memof(x):
        try:
            return cache[x]
        except:
            cache[x] = f(x)
            return cache[x]
    return memof


@memoize
def wins(board):
    if not board: return True
    return [move for move in moves(board) if not wins(move)]
