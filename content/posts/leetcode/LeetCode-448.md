---
title: "LeetCode 448"
date: 2022-12-27T20:00:06+08:00
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

原地哈希即可，同[LeetCode-41](https://blog.zhangmengyang.tk/posts/leetcode/leetcode-41/)

### 代码

```java
class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        int n = nums.length, i = 0;
        while (i < n) {
            if (nums[i] == nums[nums[i] - 1]) {
                i++;
                continue;
            }
            swap(nums, i, nums[i] - 1);
        }
        List<Integer> res = new LinkedList<>();
        for (int j = 0; j < n; j++) {
            if (nums[j] != j + 1) {
                res.add(j + 1);
            }
        }
        return res;
    }

    private void swap(int[] nums, int a, int b) {
        int temp = nums[a];
        nums[a] = nums[b];
        nums[b] = temp;
    }
}
```

### References

---

#### 1. [找到所有数组中消失的数字](https://leetcode.cn/problems/find-all-numbers-disappeared-in-an-array/)
