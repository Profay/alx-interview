#!/usr/bin/python3
""" rotates n x n 2D matrix in-place by 90 degrees clockwise
"""


def rotate_2d_matrix(matrix):
    """ in-place 2D matrix rotation """
    left, right = 0, len(matrix) - 1

    while left < right:
        for i in range(right - left):
            top, bottom = left, right

            # save the top left element
            topleft = matrix[top][left + i]

            # move bottom left into top left
            matrix[top][left + i] = matrix[bottom - i][left]

            # move bottom right into bottom left
            matrix[bottom - i][left] = matrix[bottom][right - i]

            # move top right into bottom right
            matrix[bottom][right - i] = matrix[top + i][right]

            # move top left into top right
            matrix[top + i][right] = topleft
        right -= 1
        left += 1
