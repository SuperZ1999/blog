---
title: "LeetCode 338"
date: 2022-12-26T20:18:26+08:00
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

两种思路：

#### 常规思路

可以使用`i & (i - 1)可以去掉i最右边的一个1`这个技巧，提升计算一个数比特1数目的速度

#### 动态规划

对于所有的数字，只有两类：

- 奇数，二进制表示中，奇数一定比前面那个偶数多一个 1，因为多的就是最低位的 1
- 偶数：二进制表示中，偶数中 1 的个数一定和除以 2 之后的那个数一样多。因为最低位是 0，除以 2 就是右移一位，也就是把那个 0 抹掉而已，所以 1 的个数是不变的

另外，0 的 1 个数为 0，这就是base case，动态规划即可，dp定义与状态转移方程详见代码

还有其他动态规划的方式，详见：<https://leetcode.cn/problems/counting-bits/solutions/627418/bi-te-wei-ji-shu-by-leetcode-solution-0t1i/>

### 代码

#### 常规思路

```java
class Solution {
    public int[] countBits(int n) {
        int[] res = new int[n + 1];
        for (int i = 0; i <= n; i++) {
            res[i] = getCount(i);
        }
        return res;
    }

    private int getCount(int n) {
        int count = 0;
        while (n != 0) {
            n = n & (n - 1);
            count++;
        }
        return count;
    }
}
```

#### 动态规划

```java
class Solution {
    public int[] countBits(int n) {
        int[] dp = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            if (i % 2 == 1) {
                dp[i] = dp[i - 1] + 1;
            } else {
                dp[i] = dp[i / 2];
            }
        }
        return dp;
    }
}
```

### References

---

#### 1. [比特位计数](https://leetcode.cn/problems/counting-bits/)
