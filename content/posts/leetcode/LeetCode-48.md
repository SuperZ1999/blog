---
title: "LeetCode 48"
date: 2022-09-26T11:12:45+08:00
tags: ["leetcode"]
draft: false
---

### 思路

先按对角线对折矩阵（注意对折矩阵时，只需要遍历矩阵的一半即可，如果整个矩阵都遍历，那矩阵不会有任何变化，相当于对折了两次），再反转矩阵的每一行即可

为什么这样做？因为旋转90°相当于把行变成列，而对折矩阵刚好可以把行变成列，但是位置不对，那再反转一下就行了

### 我的代码

```java
class Solution {
    public void rotate(int[][] matrix) {
        for (int i = 0; i < matrix.length; i++) {
            // 注意对折矩阵时，只需要遍历矩阵的一半即可，如果整个矩阵都遍历，相当于对折了两次，所以这里要写j = i + 1
            for (int j = i + 1; j < matrix[0].length; j++) {
                int temp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = temp;
            }
        }

        for (int i = 0; i < matrix.length; i++) {
            reverse(matrix[i]);
        }
    }

    private void reverse(int[] s) {
        int left = 0, right = s.length - 1;
        while (left < right) {
            int temp = s[left];
            s[left] = s[right];
            s[right] = temp;
            left++;
            right--;
        }
    }
}
```

### References

---

#### 1. [旋转图像](https://leetcode.cn/problems/rotate-image/)
