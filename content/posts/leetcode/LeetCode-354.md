---
title: "LeetCode 354"
date: 2022-12-09T20:39:25+08:00
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

本质上就是最长递增子序列问题，见[LeetCode-300](https://blog.zhangmengyang.tk/posts/leetcode/leetcode-300/)，只不过需要先对width升序排序，然后计算height的最长递增子序列即可

ps：此版本会超时，需要融合二分查找

### 代码

```java
class Solution {
    public int maxEnvelopes(int[][] envelopes) {
        int n = envelopes.length;
        Arrays.sort(envelopes, (a, b) -> {
            return a[0] != b[0] ? a[0] - b[0] : b[1] - a[1];
        });
        int[] dp = new int[n];
        Arrays.fill(dp, 1);
        int res = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (envelopes[j][1] < envelopes[i][1]) {
                    dp[i] = Math.max(dp[i], dp[j] + 1);
                }
            }
            res = Math.max(res, dp[i]);
        }
        return res;
    }
}
```

### References

---

#### 1. [俄罗斯套娃信封问题](https://leetcode.cn/problems/russian-doll-envelopes/)
