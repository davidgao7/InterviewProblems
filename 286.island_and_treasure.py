"""
n * n grid
-1: wall
0: gate

rest marked with INF
fill each empty room with the distance to its nearest gate

ex:
human-readable:
[
[room, wall, gate, room],
[room, room, room, wall],
[room, wall, room, wall],
[gate, wall, room, room]
]

rooms = [
    [INF, -1, 0, INF],
    [INF, INF, INF, -1],
    [INF, -1, INF, -1],
    [0, -1, INF, INF]
]

output = [
    [3, -1, 0, 1],  # [3steps from cloest gate, wall, gate, 1step from gate]
    [2, 2, 1, -1], 
    [1, -1, 2, -1],
    [0, -1, 3, 4]
]
"""

from collections import deque
from typing import List


class Solution:

    def walls_and_gates(self, rooms: List[List[int]]):

        if not rooms:
            return
        ROWS, COLS = len(rooms), len(rooms[0])
        visit = set()
        q = deque()

        def add_room(r, c):
            # check if the room is valid
            # if not valid, return
            # if valid, add to queue and mark as visited
            if (
                r < 0
                or c < 0
                or r >= ROWS
                or c >= COLS
                or rooms[r][c] == -1
                or (r, c) in visit
            ):
                return
            q.append((r, c))
            visit.add((r, c))

        # add all the gates to the queue and mark as visited
        for i in range(ROWS):
            for j in range(COLS):
                if rooms[i][j] == 0:
                    # if crruent position is gate, append to queue
                    q.append((i, j))
                    visit.add((i, j))

        # bfs
        # then we will start from the gate and go through all the rooms
        distance = 0
        while q:
            # go through all the gates at this distance
            for _ in range(len(q)):
                # get the current gate position
                r, c = q.popleft()

                # update gate to current distance in the current room matrix
                rooms[r][c] = distance

                # go 1 step in all 4 directions to find the rooms
                add_room(r + 1, c)  # down
                add_room(r - 1, c)  # up
                add_room(r, c + 1)  # right
                add_room(r, c - 1)  # left

            # update distance
            distance += 1

    # in the end the rooms will be updated with the distance from the gate
    # THE END


if __name__ == "__main__":
    s = Solution()
    rooms = [
        [float("inf"), -1, 0, float("inf")],
        [float("inf"), float("inf"), float("inf"), -1],
        [float("inf"), -1, float("inf"), -1],
        [0, -1, float("inf"), float("inf")],
    ]
    s.walls_and_gates(rooms)
    print(rooms)
    # output = [
    #     [3, -1, 0, 1],
    #     [2, 2, 1, -1],
    #     [1, -1, 2, -1],
    #     [0, -1, 3, 4]
    # ]
    # assert rooms == output
