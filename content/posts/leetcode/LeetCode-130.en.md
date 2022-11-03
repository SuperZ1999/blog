---
title: "LeetCode 130"
date: 2022-11-03T23:38:17+08:00
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

利用并查集的思想，设置一个dummy结点，想办法把与边界的'O'相连的'O'加入到dummy的集合中，然后遍历一遍二维数组，将不在dummy集合里的'O'改成'X'即可

### 代码

```java
class Solution {
    public void solve(char[][] board) {
        int m = board.length;
        int n = board[0].length;
        UF uf = new UF(m * n + 1);
        int dummy = m * n;

        for (int i = 0; i < m; i++) {
            if (board[i][0] == 'O') {
                uf.union(dummy,i * n);
            }
            if (board[i][n - 1] == 'O') {
                uf.union(dummy,i * n + n - 1);
            }
        }
        for (int i = 0; i < n; i++) {
            if (board[0][i] == 'O') {
                uf.union(dummy, i);
            }
            if (board[m - 1][i] == 'O') {
                uf.union(dummy, (m - 1) * n + i);
            }
        }

        int[][] d = new int[][]{{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
        for (int i = 1; i < m - 1; i++) {
            for (int j = 1; j < n - 1; j++) {
                if (board[i][j] == 'O') {
                    for (int k = 0; k < 4; k++) {
                        int x = i + d[k][0];
                        int y = j + d[k][1];
                        if (board[x][y] == 'O') {
                            uf.union(i * n + j, x * n + y);
                        }
                    }
                }
            }
        }
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (!uf.isConnected(i * n + j, dummy)) {
                    board[i][j] = 'X';
                }
            }
        }
    }

    class UF {
        private int[] parent;
        private int count;

        public UF(int n) {
            parent = new int[n];
            for (int i = 0; i < n; i++) {
                parent[i] = i;
            }
            count = n;
        }

        public int find(int x) {
            if (x != parent[x]) {
                parent[x] = find(parent[x]);
            }
            return parent[x];
        }

        public void union(int x, int y) {
            int xRoot = find(x);
            int yRoot = find(y);
            if (xRoot == yRoot) {
                return;
            }
            parent[xRoot] = yRoot;
            count--;
        }

        public boolean isConnected(int x, int y) {
            int xRoot = find(x);
            int yRoot = find(y);
            return xRoot == yRoot;
        }

        public int getCount() {
            return count;
        }
    }
}
```

### References

---

#### 1. [被围绕的区域](https://leetcode.cn/problems/surrounded-regions/)
