import numpy as np
import random


def ChessBorad(tr, tc, dr, dc, size):
    global title
    if size == 1:
        return
    title += 1
    t = title
    s = size // 2
    if dr < tr + s and dc < tc + s:
        ChessBorad(tr, tc, dr, dc, s)
    else:
        num[tr + s - 1][tc + s - 1] = t
        ChessBorad(tr, tc, tr + s - 1, tc + s - 1, s)

    if dr < tr + s and dc >= tc + s:
        ChessBorad(tr, tc + s, dr, dc, s)
    else:
        num[tr + s - 1][tc + s] = t
        ChessBorad(tr, tc + s, tr + s - 1, tc + s, s)

    if dr >= tr + s and dc < tc + s:
        ChessBorad(tr + s, tc, dr, dc, s)
    else:
        num[tr + s][tc + s - 1] = t
        ChessBorad(tr + s, tc, tr + s, tc + s - 1, s)

    if dr >= tr + s and dc >= tc + s:
        ChessBorad(tr + s, tc + s, dr, dc, s)
    else:
        num[tr + s][tc + s] = t
        ChessBorad(tr + s, tc + s, tr + s, tc + s, s)


if __name__ == '__main__':
    size = 8
    title = 0
    num = np.zeros((size, size), dtype=np.int)
    dr, dc = random.randint(0, 15), random.randint(0, 15)
    ChessBorad(0, 0, dr, dc, size)
    print(num)
