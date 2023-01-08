---
title: "LeetCode 2226"
date: 2023-01-08T23:05:14+08:00
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

看到「最大化最小值」或者「最小化最大值」（其实就是那种要求一堆数字尽量平均的题）就要想到二分答案，这是一个固定的套路。

这里求小孩最多能拿到多少糖果，其实就是尽量平均的问题，那么可以二分搜索答案，每次选定一个答案都要验证这个答案，根据验证结果去选择在左区间还是右区间继续二分查找，不过要注意每次二分要排除不可能的情况，也就是说可能的情况要全部保留，不要将可能的情况扔掉，相关代码如下所示：

```java
if (count >= k) {
    left = mid;
} else {
    right = mid - 1;
}
```

### 代码

```java
class Solution {
    public int maximumCandies(int[] candies, long k) {
        int left = 0, right = 10000000;
        while (left < right) {
            int mid = left + (right - left + 1) / 2;
            long count = 0;
            for (int i = 0; i < candies.length; i++) {
                count += candies[i] / mid;
            }
            if (count >= k) {
                left = mid;
            } else {
                right = mid - 1;
            }
        }
        return left;
    }
}
```

### References

---

#### 1. [每个小孩最多能分到多少糖果](https://leetcode.cn/problems/maximum-candies-allocated-to-k-children/)
