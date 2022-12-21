---
title: "LeetCode 659"
date: 2022-12-20T10:40:04+08:00
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

从前往后遍历，遍历到一个元素v，只要能将所有元素分配到一个序列中即可，关键在于，我们怎么知道当前元素 `v` 如何进行分配呢？

肯定得分情况讨论，把情况讨论清楚了，题目也就做出来了。

总共有两种情况：

**1、当前元素 `v` 自成一派，「以自己开头」构成一个长度至少为 3 的序列**。

**2、当前元素 `v` 接到已经存在的子序列后面**。

如果这两种情况都可以，应该**优先判断自己是否能够接到其他序列后面**，因为只要能自成一派，那接在其他序列后面肯定没问题，接在其他序列后面没问题，不一定能自成一派，用两个hash表即可实现这个过程，详见代码

### 代码

```java
class Solution {
    public boolean isPossible(int[] nums) {
        Map<Integer, Integer> freq = new HashMap<>();
        Map<Integer, Integer> need = new HashMap<>();
        for (int num : nums) {
            freq.put(num, freq.getOrDefault(num, 0) + 1);
        }
        for (int num : nums) {
            if (freq.get(num) == 0) {
                continue;
            }
            if (need.getOrDefault(num, 0) > 0) {
                freq.put(num, freq.get(num) - 1);
                need.put(num, need.get(num) - 1);
                need.put(num + 1, need.getOrDefault(num + 1, 0) + 1);
            } else if (freq.getOrDefault(num, 0) > 0
            && freq.getOrDefault(num + 1, 0) > 0
            && freq.getOrDefault(num + 2, 0) > 0) {
                freq.put(num, freq.get(num) - 1);
                freq.put(num + 1, freq.get(num + 1) - 1);
                freq.put(num + 2, freq.get(num + 2) - 1);
                need.put(num + 3, need.getOrDefault(num + 3, 0) + 1);
            } else {
                return false;
            }
        }
        return true;
    }
}
```

### References

---

#### 1. [分割数组为连续子序列](https://leetcode.cn/problems/split-array-into-consecutive-subsequences/)
