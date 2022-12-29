---
title: "LeetCode 240"
date: 2022-12-29T22:00:13+08:00
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

从右上角看成一颗二叉搜索树即可，如果当前元素大于target说明整列都大于target，所以这一列可以忽略，去掉这一列的矩阵还是一个矩阵，如果当前元素小于target说明整行都小于target，所以这一行可以忽略，去掉这一行的矩阵还是一个矩阵，循环往复，其实就是一个Z字形查找，如果能找到，那就返回，如果查找时超过了边界，那就是查找失败

### 代码

```java
class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int m = matrix.length, n = matrix[0].length;
        int i = 0, j = n - 1;
        while (i < m && j >= 0) {
            if (matrix[i][j] == target) {
                return true;
            } else if (matrix[i][j] > target) {
                j--;
            } else if (matrix[i][j] < target) {
                i++;
            }
        }
        return false;
    }
}
```

### References

---

#### 1. [搜索二维矩阵 II](https://leetcode.cn/problems/search-a-2d-matrix-ii/)
