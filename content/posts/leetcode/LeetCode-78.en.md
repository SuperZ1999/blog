---
title: "LeetCode 78"
date: 2022-12-17T19:15:12+08:00
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

经典子集问题，不解释了，详见思想篇章

### 代码

```java
class Solution {
    List<List<Integer>> res = new LinkedList<>();
    List<Integer> track = new LinkedList<>();

    public List<List<Integer>> subsets(int[] nums) {
        backtrack(nums, 0);
        return res;
    }

    private void backtrack(int[] nums, int start) {
        res.add(new LinkedList<>(track));

        for (int i = start; i < nums.length; i++) {
            track.add(nums[i]);
            backtrack(nums, i + 1);
            track.remove(track.size() - 1);
        }
    }
}
```

### References

---

#### 1. [子集](https://leetcode.cn/problems/subsets/)
