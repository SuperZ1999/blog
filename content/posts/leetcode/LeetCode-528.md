---
title: "LeetCode 528"
date: 2022-09-26T22:42:24+08:00
tags: ["leetcode"]
draft: false
---

### 思路

可以想象成一条线段，分成好几段，每段长度不一样，然后往上面撒石子，返回石子撒到了第几条线段上，直接把这个线段当成一个数组不现实，因为数值有可能很大，所以可以压缩一下，把每一段的长度当成一个元素，但这样寻找随机数处在哪一段还得把前面都加起来，不方便，那就压缩成一个前缀和数组，这样只需要从左往右遍历前缀和数组找第一个大于等于随机数的元素就行了，但是前缀和数组是一个有序数组，我们寻找第一个大于等于随机数的元素使用二分查找就可以快速定位，不需要从头遍历一遍

有两个需要注意的地方：

1. ”线段“和前缀和的”格子“的对应关系需要想清楚，这个画张图就明白了
2. 寻找第一个大于等于随机数的元素，需要用寻找左边界的二分查找，而不是寻找右边界的二分查找，详见LeetCode-note的思想章节二分查找注意点第10条

### 我的代码

```java
class Solution {
    int[] preSum;

    public Solution(int[] w) {
        preSum = new int[w.length + 1];
        for (int i = 1; i < preSum.length; i++) {
            preSum[i] = preSum[i - 1] + w[i - 1];
        }
    }

    public int pickIndex() {
        int random = new Random().nextInt(preSum[preSum.length - 1]) + 1;

        // 二分法寻找random所在的索引
        int left = 0, right = preSum.length - 1;
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (random <= preSum[mid]) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }

        return left - 1;
    }
}
```

### References

---

#### 1. [按权重随机选择](https://leetcode.cn/problems/random-pick-with-weight/)
