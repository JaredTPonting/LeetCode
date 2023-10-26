import numpy as np


def longestCommonPrefix(strs: list[str]) -> str:
    a = strs[0]
    """Set a to be the smallest string in list"""
    for i in strs:
        if len(i) < len(a):
            a = i

    longest_prefix = ''
    """Cycle through list to find common prefix"""
    for index, letter in enumerate(a):
        b = all([letter == word[index] for word in strs])
        if b:
            longest_prefix += letter
        else:
            return longest_prefix
    return longest_prefix


if __name__ == '__main__':
    check = longestCommonPrefix(["flower", "flow", "flight", ''])
    print(check)
