---
title: "LeetCode 496"
date: 2022-12-07T10:35:40+08:00
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

利用单调栈的思想即可，倒着入栈，碰到栈顶比自己小就出栈直到比自己大，那么这么就把两个较大元素中间的小元素去除掉了，剩下的两个元素就可以充当下一个更大元素的角色（中间去除的元素是无法充当这种角色的），那么此时栈顶就是当前元素下一个更大元素

### 代码

```java
class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        int n = nums2.length;
        Deque<Integer> stack = new ArrayDeque<>();
        Map<Integer, Integer> res = new HashMap<>();
        for (int i = n - 1; i >= 0; i--) {
            while (!stack.isEmpty() && stack.peek() <= nums2[i]) {
                stack.pop();
            }
            res.put(nums2[i], stack.isEmpty() ? -1 : stack.peek());
            stack.push(nums2[i]);
        }
        for (int i = 0; i < nums1.length; i++) {
            nums1[i] = res.get(nums1[i]);
        }
        return nums1;
    }
}
```

### References

---

#### 1. [下一个更大元素 I](https://leetcode.cn/problems/next-greater-element-i/)
