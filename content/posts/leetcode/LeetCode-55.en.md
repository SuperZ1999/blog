---
title: "LeetCode 55"
date: 2022-12-14T20:55:31+08:00
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

利用贪心算法，每一步都计算一下从当前位置最远能够跳到哪里，然后和一个全局最优的最远位置 `farthest` 做对比，通过每一步的最优解，更新全局最优解

### 代码

```java
class Solution {
    public boolean canJump(int[] nums) {
        int n = nums.length;
        int farthest = 0;
        for (int i = 0; i < n - 1; i++) {
            farthest = Math.max(farthest, i + nums[i]);
            if (farthest == i) {
                return false;
            }
        }
        return farthest >= n - 1;
    }
}
```

### References

---

#### 1. [跳跃游戏](https://leetcode.cn/problems/jump-game/)
