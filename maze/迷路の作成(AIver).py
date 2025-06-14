import random

def generate_maze(size, wall_prob):
    maze = []
    for i in range(size):
        row = []
        for j in range(size):
            if random.random() < wall_prob:
                row.append(1)
            else:
                row.append(0)
        maze.append(row)
    return maze

size = 30
wall_prob = 0.4

maze = generate_maze(size, wall_prob)

for row in maze:
    print(f"    {row},")

start = (0, 0)
goal = (size-19, size-19)

print(f"スタート地点: {start}")
print(f"ゴール地点: {goal}")