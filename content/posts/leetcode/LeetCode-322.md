---
title: "LeetCode 322"
date: 2022-12-08T22:42:46+08:00
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

经典动态规划问题，具有最优子结构性质，“状态”为金额，“选择”为硬币的面值，dp数组定义为dp[金额] = 取得该金额需要的最少硬币，”basecase“为dp[0] = 0，状态转移方程如下：

![](https://labuladong.gitee.io/algo/images/%e5%8a%a8%e6%80%81%e8%a7%84%e5%88%92%e8%af%a6%e8%a7%a3%e8%bf%9b%e9%98%b6/coin.png)

直接递归存在重复子问题，所以用dp数组迭代方式

### 代码

```java
class Solution {
    public int coinChange(int[] coins, int amount) {
        int[] dp = new int[amount + 1];
        Arrays.fill(dp, amount + 1);
        dp[0] = 0;
        for(int i = 1; i <= amount; i++) {
            for (int coin : coins) {
                if (i - coin < 0) {
                    continue;
                }
                dp[i] = Math.min(dp[i], dp[i - coin] + 1);
            }
        }
        return dp[amount] == amount + 1 ? -1 : dp[amount];
    }
}
```

### References

---

#### 1. [零钱兑换](https://leetcode.cn/problems/coin-change/)
