---
title: "LeetCode 54"
date: 2022-09-26T21:39:37+08:00
tags: ["leetcode"]
draft: false
---

### 思路

**解题的核心思路是按照右、下、左、上的顺序遍历数组，并使用四个变量圈定未遍历元素的边界**：

![img](https://labuladong.gitee.io/algo/images/%e8%8a%b1%e5%bc%8f%e9%81%8d%e5%8e%86/6.png)

需要注意水平遍历需要判断upperBound<=lowerBound，垂直遍历需要判断leftBound<=rightBound

### 我的代码

```java
class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        int row = matrix.length, col = matrix[0].length;
        int upperBound = 0, lowerBound = row - 1;
        int leftBound = 0, rightBound = col - 1;

        List<Integer> ans = new ArrayList<>();
        while (ans.size() < row * col) {
            if (upperBound <= lowerBound) {
                for (int i = leftBound; i <= rightBound; i++) {
                    ans.add(matrix[upperBound][i]);
                }
                upperBound++;
            }

            if (leftBound <= rightBound) {
                for (int i = upperBound; i <= lowerBound; i++) {
                    ans.add(matrix[i][rightBound]);
                }
                rightBound--;
            }

            if (upperBound <= lowerBound) {
                for (int i = rightBound; i >= leftBound; i--) {
                    ans.add(matrix[lowerBound][i]);
                }
                lowerBound--;
            }

            if (leftBound <= rightBound) {
                for (int i = lowerBound; i >= upperBound; i--) {
                    ans.add(matrix[i][leftBound]);
                }
                leftBound++;
            }
        }

        return ans;
    }
}
```

### References

---

#### 1. [螺旋矩阵](https://leetcode.cn/problems/spiral-matrix/)
