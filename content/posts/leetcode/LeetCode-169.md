---
title: "LeetCode 169"
date: 2022-12-25T20:11:26+08:00
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

值得学习的就两种思路：

#### 哈希

遍历一遍统计出现次数，并同时判断有没有超过n/2

#### Boyer-Moore 投票算法

设置一个count变量和候选数字，遍历数组，如果当前遍历的元素是候选数字count++，否则count--，如果count变量为0就将候选数字设置为当前遍历的元素，这样遍历到最后，候选数字就是众数，可以这样理解，因为众数一定比其他数字加一块还多，所以最后众数一定会超过其他数字，那么一定会在某一个时刻候选数字变成众数，详见题解：<https://leetcode.cn/problems/majority-element/solutions/146074/duo-shu-yuan-su-by-leetcode-solution/>

### 代码

#### 哈希

```java
class Solution {
    public int majorityElement(int[] nums) {
        Map<Integer, Integer> map = new HashMap<>();
        int n = nums.length;
        for (int i = 0; i < n; i++) {
            map.put(nums[i], map.getOrDefault(nums[i], 0) + 1);
            if (map.get(nums[i]) > n / 2) {
                return nums[i];
            }
        }
        return -1;
    }
}
```

#### Boyer-Moore 投票算法

```java
class Solution {
    public int majorityElement(int[] nums) {
        int candidate = 0, count = 0;
        for (int num : nums) {
            if (count == 0) {
                candidate = num;
            }
            count += candidate == num ? 1 : -1;
        }
        return candidate;
    }
}
```

### References

---

#### 1. [多数元素](https://leetcode.cn/problems/majority-element/solutions/)
