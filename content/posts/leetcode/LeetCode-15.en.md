---
title: "LeetCode 15"
date: 2023-01-05T15:36:20+08:00
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

利用双指针的思想，这道题不是想象中的那样使用Map，而是使用双指针，这题的难点在于去重，可以先排序，然后遍历每一个元素，同时根据遍历的这个元素找相对应的两个元素，为了去重，从该元素后面找（否则会有重复解），寻找这两个元素的时候就可以使用双指针，如果加起来过大，就right--，过小就left++，遍历完所有元素即可

### 代码

```java
class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        int n = nums.length;
        List<List<Integer>> res = new ArrayList<>();
        Arrays.sort(nums);
        for (int i = 0; i < n; i++) {
            if (nums[i] > 0) {
                break;
            }
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }
            int left = i + 1, right = n - 1, target = -nums[i];
            while (left < right) {
                if (nums[left] + nums[right] == target) {
                    res.add(Arrays.asList(nums[i], nums[left], nums[right]));
                    left++;
                    right--;
                    while (left < right && nums[left] == nums[left - 1]) {
                        left++;
                    }
                    while (left < right && nums[right] == nums[right + 1]) {
                        right--;
                    }
                } else if (nums[left] + nums[right] > target) {
                    right--;
                } else {
                    left++;
                }
            }
        }
        return res;
    }
}
```

### References

---

#### 1. [三数之和](https://leetcode.cn/problems/3sum/)
