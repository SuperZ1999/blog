---
title: "LeetCode 560"
date: 2022-12-27T20:48:06+08:00
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

#### 枚举

把所有情况都求出来，简单粗暴

#### 前缀和+哈希表优化

利用前缀和的思想，假如[i...j]的和为k，那么就是`preSum[j] - preSum[i - 1] == k -> preSum[j] - k == preSum[i - 1]`，那么遍历到preSum[j]时，只要判断一下preSum[j]前有没有元素等于preSum[j] - k就可以了，为了加快查找速度，可以设置map，key为preSum里的元素，value为该元素值的个数，详见：<https://leetcode.cn/problems/subarray-sum-equals-k/solutions/238572/he-wei-kde-zi-shu-zu-by-leetcode-solution/>

### 代码

#### 枚举

```java
class Solution {
    public int subarraySum(int[] nums, int k) {
        int n = nums.length, res = 0;
        for (int i = 0; i < n; i++) {
            int sum = 0;
            for (int j = i; j < n; j++) {
                sum += nums[j];
                if (sum == k) {
                    res++;
                }
            }
        }
        return res;
    }
}
```

#### 前缀和+哈希表优化

```java
class Solution {
    public int subarraySum(int[] nums, int k) {
        int n = nums.length, pre = 0, res = 0;
        Map<Integer, Integer> map = new HashMap<>();
        map.put(0, 1);
        for (int i = 0; i < n; i++) {
            pre += nums[i];
            if (map.containsKey(pre - k)) {
                res += map.get(pre - k);
            }
            map.put(pre, map.getOrDefault(pre, 0) + 1);
        }
        return res;
    }
}
```

### References

---

#### 1. [和为 K 的子数组](https://leetcode.cn/problems/subarray-sum-equals-k/)
