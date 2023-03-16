---
title: "LeetCode 16"
date: 2023-03-06T18:57:09+08:00
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

同[LeetCode-15](https://blog.zhangmengyang.tk/posts/leetcode/leetcode-15/)，只不过每次找到一个三元组，都判断一下跟target的距离，去最小距离的三元组

### 代码

```java
class Solution {
    public int threeSumClosest(int[] nums, int target) {
        int n = nums.length, res = 100000;
        Arrays.sort(nums);
        for (int i = 0; i < n; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }
            int left = i + 1, right = n - 1;
            while (left < right) {
                int sum = nums[i] + nums[left] + nums[right];
                if (sum == target) {
                    return target;
                }
                if (Math.abs(sum - target) < Math.abs(res - target)) {
                    res = sum;
                }
                if (sum > target) {
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

#### 1. [最接近的三数之和](https://leetcode.cn/problems/3sum-closest/)
