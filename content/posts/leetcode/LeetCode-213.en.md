---
title: "LeetCode 213"
date: 2022-12-12T14:25:48+08:00
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

同[LeetCode-198](https://superz1999.github.io/blog/posts/leetcode/leetcode-198/)，只不过首尾不能同时偷，共有三种情况，其中第一种情况不需要考虑因为肯定比其他两种小

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/gibkIz0MVqdG9kDIzE6qfsOcugRP3xn8nlATHI4e9ib8SUiar0s2OR8zQdvficwknUKDwfcKWV0sc3WwL1lC0Cw5GQ/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

### 代码

```java
class Solution {
    private int robRange(int[] nums, int start, int end) {
        int dp_i_0 = 0, dp_i_1 = 0, dp_i_2 = 0;
        for (int i = 2 + start; i < end + 3; i++) {
            dp_i_2 = Math.max(dp_i_1, dp_i_0 + nums[i - 2]);
            dp_i_0 = dp_i_1;
            dp_i_1 = dp_i_2;
        }
        return dp_i_2;
    }

    public int rob(int[] nums) {
        if (nums.length == 1) {
            return nums[0];
        }
        return Math.max(robRange(nums, 0, nums.length - 2),
                robRange(nums, 1, nums.length - 1));
    }
}
```

### References

---

#### 1. [打家劫舍 II](https://leetcode.cn/problems/house-robber-ii/)
