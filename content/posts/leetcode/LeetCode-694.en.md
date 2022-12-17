---
title: "LeetCode 694"
date: 2022-12-17T22:55:17+08:00
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

和其他岛屿类似，但是需要判断形状是否相同，解决办法也比较巧妙，通过遍历岛屿单元格的顺序来判断形状是否相同，还要把这些顺序序列化成字符串方便去重

### 代码

```java
public class Solution {
    private void dfs(int[][] grid, int i, int j, StringBuilder sb, int dir) {
        int m = grid.length, n = grid[0].length;
        if (i < 0 || i >= m || j < 0 || j >= n) {
            return;
        }
        if (grid[i][j] == 0) {
            return;
        }
        grid[i][j] = 0;
        sb.append(dir).append(',');

        dfs(grid, i + 1, j, sb, 1);
        dfs(grid, i - 1, j, sb, 2);
        dfs(grid, i, j + 1, sb, 3);
        dfs(grid, i, j - 1, sb, 4);

        sb.append(-dir).append(',');
    }

    public int numberofDistinctIslands(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        Set<String> res = new HashSet<>();
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) {
                    StringBuilder sb = new StringBuilder();
                    dfs(grid, i, j, sb, 666);
                    res.add(sb.toString());
                }
            }
        }
        return res.size();
    }
}
```

### References

---

#### 1. [不同岛屿的数量](https://leetcode.cn/problems/number-of-distinct-islands/)
