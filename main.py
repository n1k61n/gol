import os


ROW = 10
COL = 10

world = [[" "] * COL for _ in range(ROW)]
world[0][1] = "*"
world[1][2] = "*"
world[2][0] = "*"
world[2][1] = "*"
world[2][2] = "*"


def print_world(arr):
    os.system("cls")
    for i in range(ROW):
        print("".join(arr[i]))


def main():
    print_world(world)


if __name__=="__main__":
    main()