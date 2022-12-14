---
title: "LeetCode 45"
date: 2022-12-14T21:14:41+08:00
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

利用贪心算法，每次跳的时候选择一个最有潜力的结点跳，只不过代码有点难写

### 代码

```java
class Solution {
    public int jump(int[] nums) {
        int n = nums.length, farthest = 0, jumps = 0, end = 0;
        for (int i = 0; i < n - 1; i++) {
            farthest = Math.max(farthest, i + nums[i]);
            if (i == end) {
                jumps++;
                end = farthest;
            }
        }
        return jumps;
    }
}
```

### References

---

#### 1. [跳跃游戏 II](https://leetcode.cn/problems/jump-game-ii/)
