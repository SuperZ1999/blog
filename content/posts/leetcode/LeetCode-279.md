---
title: "LeetCode 279"
date: 2022-12-26T14:21:39+08:00
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

#### 记忆化回溯

就是带备忘录的暴力算法，`numSquares`函数的定义为给定一个数n，返回n的完全平方数，具体做法就是将一个数有可能的平方数一个一个试，看看用哪个数最终答案会比较小，然后存进备忘录并返回，由于记忆化回溯等价于动态规划，所以还有动态规划的做法

#### 动态规划

设置dp数组，dp数组李存放当前索引的完全平方数，状态转移方程为：

```java
for (int j = 1; j <= sqrt; j++) {
    dp[i] = Math.min(dp[i], dp[i - j * j] + 1);
}
```

base case为dp[0] = 0，不能优化空间复杂度

#### 数学

四平方和定理证明了任意一个正整数都可以被表示为至多四个正整数的平方和。这给出了本题的答案的上界。四平方和定理证明了任意一个正整数都可以被表示为至多四个正整数的平方和。这给出了本题的答案的上界。详见：<https://leetcode.cn/problems/perfect-squares/solutions/822940/wan-quan-ping-fang-shu-by-leetcode-solut-t99c/>

### 代码

#### 记忆化回溯

```java
class Solution {
    private Map<Integer, Integer> memo = new HashMap<>();

    public int numSquares(int n) {
        if (n == 0) {
            return 0;
        }
        if (memo.containsKey(n)) {
            return memo.get(n);
        }
        int sqrt = (int) Math.sqrt(n);
        int min = Integer.MAX_VALUE;
        for (int i = sqrt; i >= 1; i--) {
            min = Math.min(min, numSquares( n - i * i));
        }
        memo.put(n, min + 1);
        return min + 1;
    }
}
```

#### 动态规划

```java
class Solution {
    public int numSquares(int n) {
        int[] dp = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            int sqrt = (int) Math.sqrt(i);
            dp[i] = Integer.MAX_VALUE;
            for (int j = 1; j <= sqrt; j++) {
                dp[i] = Math.min(dp[i], dp[i - j * j] + 1);
            }
        }
        return dp[n];
    }
}
```

#### 数学

```java
class Solution {
    public int numSquares(int n) {
        if (isPerfectSquare(n)) {
            return 1;
        }
        if (isAnswer4(n)) {
            return 4;
        }
        int sqrt = (int) Math.sqrt(n);
        for (int i = 1; i <= sqrt; i++) {
            if (isPerfectSquare(n - i * i)) {
                return 2;
            }
        }
        return 3;
    }

    private boolean isPerfectSquare(int n) {
        int sqrt = (int) Math.sqrt(n);
        return n == sqrt * sqrt;
    }

    private boolean isAnswer4(int n) {
        while (n % 4 == 0) {
            n /= 4;
        }
        return n % 8 == 7;
    }
}
```

### References

---

#### 1. [完全平方数](https://leetcode.cn/problems/perfect-squares/)
