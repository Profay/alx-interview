#!/usr/bin/python3
""" This module determine the fewest number of coin needed
Return: fewest number of coins needed to meet total
If total is 0 or less, return 0
If total cannot be met by any number of coins you have, return -1
"""


def makeChange(coins, total):
    while total