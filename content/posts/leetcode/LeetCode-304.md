---
title: "LeetCode 304"
date: 2022-09-25T23:11:19+08:00
tags: ["leetcode"]
draft: false
---

### 思路

利用前缀和的思想轻松秒杀，需要注意在preSum中，第[n + 1, n+1]个元素存的是matrix前n*n个元素的和，整体往右下挪一位

还需要注意做减法时，会多减一块区域，需要加回来

### 我的代码

```java
class NumMatrix {
    int[][] preSum;

    public NumMatrix(int[][] matrix) {
        preSum = new int[matrix.length + 1][matrix[0].length + 1];

        for (int i = 1; i < preSum.length; i++) {
            for (int j = 1; j < preSum[0].length; j++) {
                preSum[i][j] = preSum[i - 1][j] + preSum[i][j - 1] - preSum[i - 1][j - 1] + matrix[i - 1][j - 1];
            }
        }
    }
    
    public int sumRegion(int row1, int col1, int row2, int col2) {
        return preSum[row2 + 1][col2 + 1] - preSum[row1][col2 + 1]
                - preSum[row2 + 1][col1] + preSum[row1][col1];
    }
}
```

### References

---

#### 1. [二维区域和检索 - 矩阵不可变](https://leetcode.cn/problems/range-sum-query-2d-immutable/)
