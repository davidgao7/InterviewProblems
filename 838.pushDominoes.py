from collections import deque


class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dom = list(dominoes)
        q = deque()

        # NOTE: process in order: choose from left to right
        for i, d in enumerate(dom):
            if d != ".":
                q.append((i, d))

        # BFS with queue
        while q:
            i, d = q.popleft()  # start from left

            if d == "L":
                # check if it can make left one til left
                if i > 0 and dom[i - 1] == ".":
                    # store the updated left one state, push to queue to cause further effects
                    q.append((i - 1, "L"))
                    dom[i - 1] = "L"

            elif d == "R":
                if (
                    i < len(dom) - 1 and dom[i + 1] == "."
                ):  # see if next one on the right can till right
                    if (
                        i + 2 < len(dom) and dom[i + 2] == "L"
                    ):  # if the next next one on the right is till left
                        # / . \
                        # we should pop the current one which is till right
                        # because for the next iteration in the while loop, we will
                        # meet this till left, it will go to 1st if statement,
                        # causing the current become left, which is not true
                        # basically skipping next dominoes
                        q.popleft()
                    else:
                        q.append((i - 1, "L"))
                        dom[i + 1] = "R"  # the dominoes just go koncked over

        return "".join(dom)


if __name__ == "__main__":
    dominoes = ".L.R...LR..L.."
    s = Solution()
    print(s.pushDominoes(dominoes))  # "LL.RR.LLRRLL.."
    print("LL.RR.LLRRLL..")
