## BackTracking = DFS + pruning
import argparse


def print_solution(n, a):
    global solution_count
    print(f"Solution {solution_count}:")
    for i in range(n):
        row = ['-'] * n
        row[a[i]] = 'Q'  # 在 a[i] 位置放皇后
        print(' '.join(row))
    print()
    solution_count += 1


def dfs(i, n, a, b, c, d):
    """
    :param i: 棋盘第i行
    :param n: 棋盘总行数
    :param a: 棋盘， a[i]则表示第i行的皇后放在第a[i]列
    :param b: bool类型，判断当前列是否可用
    :param c: bool类型，判断当前对角线是否可用（左下到右上）
    :param d: bool类型，判断当前对角线是否可用（左上到右下）
    :return:

    算法思路：比如在一个4X4的棋盘中，我们在[3, 2]这个位置放了一个Queen，横坐标用 i 表示，纵坐标用 j 表示
      1   2   3   4
    +---+---+---+---+
1   |   |   |   | O |
    +---+---+---+---+
2   | ✔ |   | O |   |
    +---+---+---+---+
3   |   | Q |   |   |
    +---+---+---+---+
4   |O  |   | ✔ |   |
    +---+---+---+---+
    那么左上到右下这个对角线上所有的坐标（[2, 1]和[4, 3]），i - j = 1恒成立（需要防止 i-j 为负数的情况）
    同理，左下到右上这个对角线上所有的坐标（[1, 4]和[2, 3], [4, 1]），i + j = 5恒成立
    那么只要我们确定了Queen的位置，修改bcd对应的i，j坐标为False，即可标记不可在这些位置摆放。
    修改为False之后，尝试进入下一行摆放
    """
    if i == n:
        print_solution(n, a)
        return

    for j in range(n):
        if b[j] and c[i + j] and d[i - j + n - 1]: # 剪枝： 核心逻辑为跳过已经被占用或者为False不可摆放的位置 否则时间复杂度过高

            a[i] = j
            b[j] = c[i + j] = d[i - j + n - 1] = False

            dfs(i + 1, n, a, b, c, d)

            b[j] = c[i + j] = d[i - j + n - 1] = True  #回溯 恢复状态


def n_queen(n):
    global solution_count
    solution_count = 1

    a = [0] * n  # 棋盘， a[i]则表示第i行的皇后放在第a[i]列
    b = [True] * n # bool类型，判断当前列是否可用
    c = [True] * (2 * n - 1) # bool类型，判断当前对角线是否可用（左下到右上）
    d = [True] * (2 * n - 1) # bool类型，判断当前对角线是否可用（左上到右下）
    dfs(0, n, a, b, c, d)



def main(args):
    assert args.n > 0, 'n must > 0!'
    n_queen(args.n)



def get_argparser():
    parser = argparse.ArgumentParser('Python N-Queens Solution Script', add_help=False)
    parser.add_argument("--n", type=int, default=4, help="number of queens")
    return parser

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        'Python N-Queens Solution Script', parents=[get_argparser()])
    args = parser.parse_args()
    main(args)