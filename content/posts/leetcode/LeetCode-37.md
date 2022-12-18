---
title: "LeetCode 37"
date: 2022-12-18T16:16:02+08:00
categories: ["leetcode"]
tags: ["leetcode"]
description: ""
weight:
slug: ""
draft: false
disableShare: false
cover:
    image: ""
    caption: ""
    alt: ""
    relative: false
---

### 思路

经典回溯问题，暴力求解即可

### 代码

```java
class Solution {
    public void solveSudoku(char[][] board) {
        backtrack(board, 0, 0);
    }

    private boolean backtrack(char[][] board, int i, int j) {
        if (j == 9) {
            i++;
            j = 0;
        }
        if (i == 9) {
            return true;
        }
        if (board[i][j] != '.') {
            return backtrack(board, i, j + 1);
        }

        boolean[] isValid = getValidNum(board, i, j);
        for (int k = 1; k <= 9; k++) {
            if (!isValid[k - 1]) {
                continue;
            }
            board[i][j] = (char) ('0' + k);
            if (backtrack(board, i, j + 1)) {
                return true;
            }
            board[i][j] = '.';
        }
        return false;
    }

    private boolean[] getValidNum(char[][] board, int i, int j) {
        boolean[] isValid = new boolean[9];
        Arrays.fill(isValid, true);
        for (int k = 0; k < 9; k++) {
            if (board[i][k] != '.') {
                isValid[board[i][k] - '0' - 1] = false;
            }
            if (board[k][j] != '.') {
                isValid[board[k][j] - '0'- 1] = false;
            }
            if (board[i / 3 * 3 + k / 3][j / 3 * 3 + k % 3] != '.') {
                isValid[board[i / 3 * 3 + k / 3][j / 3 * 3 + k % 3] - '0' - 1] = false;
            }
        }
        return isValid;
    }
}
```

### References

---

#### 1. [解数独](https://leetcode.cn/problems/sudoku-solver/)
