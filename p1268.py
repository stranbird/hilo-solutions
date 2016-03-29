import unittest


class Test(unittest.TestCase):
    def test_1(self):
        mat = [
            [0, 7, 2],
            [0, 5, 0],
            [0, 3, 0]
        ]

        expected_mat = [
            [6, 7, 2],
            [1, 5, 9],
            [8, 3, 4]
        ]

        self.assertListEqual(expected_mat, solve_mat(mat))


def rotate90(mat):
    # Transpose
    ans = [[None for i in range(3)] for i in range(3)]
    for i in range(3):
        for j in range(3):
            ans[i][j] = mat[j][i]

    # Flip
    ans = flip(ans)

    return ans


def fit(target, mat):
    for i in range(3):
        for j in range(3):
            if mat[i][j] > 0 and mat[i][j] != target[i][j]:
                return False

    return True


def flip(mat):
    ans = [[None for i in range(3)] for i in range(3)]
    for i in range(3):
        for j in range(3):
            ans[i][j] = mat[i][2 - j]

    return ans


def print_mat(mat):
    for row in mat:
        for num in row:
            print num,
        print


def solve_mat(mat):
    target = [
        [6, 7, 2],
        [1, 5, 9],
        [8, 3, 4]
    ]

    solutions = []

    # Rotate 90 degree, 180 degree, 270 degree, 360 degree
    for i in range(4):
        target = rotate90(target)
        if fit(target, mat):
            solutions.append(target)

    target = flip(target)
    for i in range(4):
        target = rotate90(target)
        if fit(target, mat):
            solutions.append(target)

    if len(solutions) > 1:
        raise Exception('Too Many')
    else:
        solved_mat = solutions[0]
        return solved_mat

if __name__ == '__main__':
    mat = []
    for i in range(3):
        mat.append([int(num) for num in raw_input().split()])

    try:
        ans = solve_mat(mat)
        print_mat(ans)
    except Exception, e:
        print e.message