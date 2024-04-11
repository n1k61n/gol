import os
import time


ROW = 20
COL = 30

world = [[0] * COL for _ in range(ROW)]
world[0][1] = 1
world[1][2] = 1
world[2][0] = 1
world[2][1] = 1
world[2][2] = 1




def gameOfLife( board: list[list[int]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    m, n = len(board), len(board[0])
    neighbors = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
    transition_map = {(0, 0): 0, (0, 1): 2, (1, 0): 3, (1, 1): 1}
    
    def count_neighbors(idx, jdx):
        count = 0
        # Count living neighbors
        for neighbor in neighbors:
            kdx, ldx = idx+neighbor[0], jdx+neighbor[1]
            if 0<=kdx<m and 0<=ldx<n:
                if board[kdx][ldx] == 1 or board[kdx][ldx] == 3:
                    count += 1
        # Decide life based on neighbors
        return count

    def decide_life(idx, jdx):
        curr_state = board[idx][jdx]
        alive_neighbors_count = count_neighbors(idx, jdx)
        
        if curr_state == 1:
            if alive_neighbors_count < 2:
                next_state = 0
            if 1 < alive_neighbors_count < 4:
                next_state = 1
            else:
                next_state = 0
        else:
            if alive_neighbors_count == 3:
                next_state = 1
            else:
                next_state = 0

        key = (curr_state, next_state)
        board[idx][jdx] = transition_map[key]
        
    # Change board state to either of values 0, 1, 2, 3 based 
    # on the transition
    for idx in range(m):
        for jdx in range(n):
            decide_life(idx, jdx)

    # Change board state back to binary
    for idx in range(m):
        for jdx in range(n):
            if board[idx][jdx] == 1 or board[idx][jdx] == 2:
                board[idx][jdx] = 1
            else:
                board[idx][jdx] = 0


def print_world(arr):
    for i in range(ROW):
        for j in range(COL):
            if arr[i][j] == 1:
                print("0",end="")
            else:
                print(" ",end="")
        print()


def main():
    for step in range(COL-2):
        os.system("cls")
        gameOfLife(world)
        print_world(world)
        time.sleep(1)


if __name__=="__main__":
    main()