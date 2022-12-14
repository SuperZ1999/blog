---
title: "LeetCode 51"
date: 2022-12-14T23:18:28+08:00
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

利用回溯算法，在棋盘上从上往下下棋子，如果不能下就换个格子，如果一整行都不能下，就回溯到上一行换下一个格子

### 代码

```java
class Solution {
    List<List<String>> res = new LinkedList<>();

    public List<List<String>> solveNQueens(int n) {
        List<StringBuilder> board = new ArrayList<>();
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            sb.append('.');
        }
        for (int i = 0; i < n; i++) {
            board.add(new StringBuilder(sb.toString()));
        }
        backtrack(board, 0);
        return res;
    }

    private void backtrack(List<StringBuilder> board, int row) {
        if (row == board.size()) {
            List<String> r = new LinkedList<>();
            for (int i = 0; i < board.size(); i++) {
                r.add(board.get(i).toString());
            }
            res.add(r);
            return;
        }
        for (int col = 0; col < board.get(row).length(); col++) {
            if (!canPlace(board, row, col)) {
                continue;
            }
            board.get(row).replace(col, col + 1, "Q");
            backtrack(board, row + 1);
            board.get(row).replace(col, col + 1, ".");
        }
    }

    private boolean canPlace(List<StringBuilder> board, int row, int col) {
        int n = board.size();
        for (int i = 0; i < row; i++) {
            if (board.get(i).charAt(col) == 'Q') {
                return false;
            }
        }
        for (int i = row - 1, j = col - 1;
             i >= 0 && j >= 0; i--, j--) {
            if (board.get(i).charAt(j) == 'Q') {
                return false;
            }
        }
        for (int i = row - 1, j = col + 1;
             i >= 0 && j < n; i--, j++) {
            if (board.get(i).charAt(j) == 'Q') {
                return false;
            }
        }

        return true;
    }
}
```

### References

---

#### 1. [N 皇后](https://leetcode.cn/problems/n-queens/)
