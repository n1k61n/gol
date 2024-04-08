import os
import time


ROW = 10
COL = 10

world = [[" "] * COL for _ in range(ROW)]


def init_life(arr, x, y):
    arr[x + 0][y + 1] = "*"
    arr[x + 1][y + 2] = "*"
    arr[x + 2][y + 0] = "*"
    arr[x + 2][y + 1] = "*"
    arr[x + 2][y + 2] = "*"


def clear_life(arr, x, y):
    arr[x + 0][y + 1] = " "
    arr[x + 1][y + 2] = " "
    arr[x + 2][y + 0] = " "
    arr[x + 2][y + 1] = " "
    arr[x + 2][y + 2] = " "

def print_world(arr):
    for i in range(ROW):
        print("".join(arr[i]))


def main():
    for step in range(COL-2):
        os.system("cls")
        init_life(world, step, step)
        clear_life(world, step-1,step-1)
        print_world(world)
        time.sleep(1)


if __name__=="__main__":
    main()