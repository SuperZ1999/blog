---
title: "LeetCode 503"
date: 2022-12-07T11:08:46+08:00
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

利用单调栈的思想，同[LeetCode-496](https://superz1999.github.io/blog/posts/leetcode/leetcode-496/)，只不过牵扯到循环数组的问题，常用套路就是将数组长度翻倍，代码实现的时候也可以用i % nums.length来模拟数组长度翻倍

### 代码

```java
class Solution {
    public int[] nextGreaterElements(int[] nums) {
        int n = nums.length;
        Deque<Integer> stack = new ArrayDeque<>();
        int[] res = new int[n];
        for (int i = 2 * n - 1; i >= 0; i--) {
            while (!stack.isEmpty() && stack.peek() <= nums[i % n]) {
                stack.pop();
            }
            res[i % n] = stack.isEmpty() ? -1 : stack.peek();
            stack.push(nums[i % n]);
        }
        return res;
    }
}
```

### References

---

#### 1. [下一个更大元素 II](https://leetcode.cn/problems/next-greater-element-ii/)
