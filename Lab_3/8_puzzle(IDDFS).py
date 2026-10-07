
goal = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]]

puzzle = [[1, 2, 3],
          [4, 6, 8],
          [7, 5, 0]]

moves = [(-1, 0, "Up"), (1, 0, "Down"),
         (0, -1, "Left"), (0, 1, "Right")]

def dfs(board, r, c, depth, path, prev):
    if board == goal:
        return path[:]

    if depth == 0:
        return None

    for dr, dc, name in moves:
        nr, nc = r + dr, c + dc

        if 0 <= nr < 3 and 0 <= nc < 3:
            if (nr, nc) == prev:
                continue

            board[r][c], board[nr][nc] = board[nr][nc], board[r][c]
            path.append((name, [row[:] for row in board]))

            result = dfs(board, nr, nc, depth - 1,
                         path, (r, c))

            if result is not None:
                return result

            path.pop()
            board[r][c], board[nr][nc] = board[nr][nc], board[r][c]

    return None

def iddfs(board):
    r, c = next((i, j) for i in range(3)
                for j in range(3) if board[i][j] == 0)

    depth = 0

    while True:
        print("Depth limit:", depth)
        result = dfs(board, r, c, depth, [], (-1, -1))

        if result is not None:
            print("\nGoal found!")
            for move, state in result:
                print("\nMove:", move)
                for row in state:
                    print(*row)
            print("\nTotal moves:", len(result))
            return

        depth += 1

print("Initial state:")
for row in puzzle:
    print(*row)

iddfs(puzzle)
