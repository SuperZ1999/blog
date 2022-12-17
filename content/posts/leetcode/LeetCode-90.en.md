---
title: "LeetCode 90"
date: 2022-12-17T19:50:57+08:00
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

经典带重复元素的子集问题，详见思想篇章

### 代码

```java
class Solution {
    List<List<Integer>> res = new LinkedList<>();
    List<Integer> track = new LinkedList<>();

    private void backtrack(int[] nums, int start) {
        res.add(new LinkedList<>(track));

        for (int i = start; i < nums.length; i++) {
            if (i > start && nums[i] == nums[i - 1]) {
                continue;
            }
            track.add(nums[i]);
            backtrack(nums, i + 1);
            track.remove(track.size() - 1);
        }
    }

    public List<List<Integer>> subsetsWithDup(int[] nums) {
        Arrays.sort(nums);
        backtrack(nums, 0);
        return res;
    }
}
```

### References

---

#### 1. [子集 II](https://leetcode.cn/problems/subsets-ii/)
