def word_search(board, word):
    rows, cols = len(board), len(board[0])
    
    def dfs(r, c, i):
        # r for current row
        # c for current column
        # i for current index in the word

        if i == len(word):
            return True
        if r<0 or c<0 or r>=rows or c>=cols or board[r][c] != word[i]:
            return False
        
        temp = board[r][c]
        board[r][c] = "#"  # mark visited
        
        # explore in 4 directions
        # down (r+1)
        # up (r-1)
        # right (c+1)
        # left (c-1)
        found = (dfs(r+1, c, i+1) or dfs(r-1, c, i+1) or dfs(r, c+1, i+1) or dfs(r, c-1, i+1))
        
        board[r][c] = temp  # unmark
        return found

    for r in range(rows):
        for c in range(cols):
            if dfs(r, c, 0):
                return True
    return False

# Example usage
print(word_search(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"))



# ✅ dfs(0, 0, 0)
# r=0, c=0, i=0

# word[0]='A', board[0][0]='A' → match

# temp = 'A'

# Mark cell: board[0][0] = '#'

# Now try directions with i=1 ('B')

# 🚫 dfs(1, 0, 1)
# r=1, c=0, i=1

# board[1][0]='S', word[1]='B' → no match → return False

# 🚫 dfs(-1, 0, 1)
# Out of bounds → return False

# ✅ dfs(0, 1, 1)
# r=0, c=1, i=1

# board[0][1]='B', word[1]='B' → match

# temp = 'B'

# Mark: board[0][1] = '#'

# Try directions with i=2 ('C')

# 🚫 dfs(1, 1, 2)
# board[1][1]='F' ≠ 'C' → return False

# 🚫 dfs(-1, 1, 2)
# Out of bounds → return False

# ✅ dfs(0, 2, 2)
# board[0][2]='C', word[2]='C' → match

# temp = 'C'

# Mark: board[0][2] = '#'

# Try directions with i=3 ('C' again)

# ✅ dfs(1, 2, 3)
# board[1][2]='C', word[3]='C' → match

# temp = 'C'

# Mark: board[1][2] = '#'

# Try directions with i=4 ('E')

# ✅ dfs(2, 2, 4)
# board[2][2]='E', word[4]='E' → match

# temp = 'E'

# Mark: board[2][2] = '#'

# Try directions with i=5 ('D')

# 🚫 dfs(3, 2, 5) → out of bounds
# 🚫 dfs(1, 2, 5) → visited → return False
# 🚫 dfs(2, 3, 5) → 'E' ≠ 'D'
# ✅ dfs(2, 1, 5)
# board[2][1]='D', word[5]='D' → match

# temp = 'D'

# Mark: board[2][1] = '#'

# ✅ dfs(?, ?, 6) → i == len(word) → return True
# 🔁 Backtracking begins:
# dfs(2, 1, 5) returns True

# Unmark board[2][1] = 'D'

# found = True, return True

# Then back up:

# dfs(2, 2, 4) → unmark → found = True, return True

# dfs(1, 2, 3) → unmark → return True

# dfs(0, 2, 2) → unmark → return True

# dfs(0, 1, 1) → unmark → return True

# dfs(0, 0, 0) → unmark → return True

# ✅ Final result:
# word_search() returns True because we found a valid path.

# 🧾 Recap of Values at Each Step:

# Step	r,c,i	board[r][c]	word[i]	Match?	temp	Action	found
# 1	0,0,0	A	A	✅	A	Mark #	
# 2	0,1,1	B	B	✅	B	Mark #	
# 3	0,2,2	C	C	✅	C	Mark #	
# 4	1,2,3	C	C	✅	C	Mark #	
# 5	2,2,4	E	E	✅	E	Mark #	
# 6	2,1,5	D	D	✅	D	Mark #	True
# ...						Unmark up ↑	True
