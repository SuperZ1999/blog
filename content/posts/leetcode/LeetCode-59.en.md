---
title: "LeetCode 59"
date: 2022-09-26T21:53:13+08:00
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

同LeetCode-54，只不过这里是往里填元素，详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-54/>

### 我的代码

```java
class Solution {
    public int[][] generateMatrix(int n) {
        int upperBound = 0, lowerBound = n - 1;
        int leftBound = 0, rightBound = n - 1;

        int[][] matrix = new int[n][n];
        int num = 1;
        while (num <= n * n){
            if (upperBound <= lowerBound) {
                for (int i = leftBound; i <= rightBound; i++) {
                    matrix[upperBound][i] = num;
                    num++;
                }
                upperBound++;
            }

            if (leftBound <= rightBound) {
                for (int i = upperBound; i <= lowerBound; i++) {
                    matrix[i][rightBound] = num;
                    num++;
                }
                rightBound--;
            }

            if (upperBound <= lowerBound) {
                for (int i = rightBound; i >= leftBound; i--) {
                    matrix[lowerBound][i] = num;
                    num++;
                }
                lowerBound--;
            }

            if (leftBound <= rightBound) {
                for (int i = lowerBound; i >= upperBound; i--) {
                    matrix[i][leftBound] = num;
                    num++;
                }
                leftBound++;
            }
        }

        return matrix;
    }
}
```

### References

---

#### 1. [螺旋矩阵 II](https://leetcode.cn/problems/spiral-matrix-ii/)
