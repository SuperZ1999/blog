---
title: "LeetCode 739"
date: 2022-12-07T10:53:22+08:00
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

利用单调栈的思想即可，同[LeetCode-496](https://blog.zhangmengyang.tk/posts/leetcode/leetcode-496/)，只不过这次存的是索引而不是元素

### 代码

```java
class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        int n = temperatures.length;
        Deque<Integer> stack = new ArrayDeque<>();
        int[] res = new int[n];
        for (int i = n - 1; i >= 0; i--) {
            while (!stack.isEmpty() && temperatures[stack.peek()] <= temperatures[i]) {
                stack.pop();
            }
            res[i] = stack.isEmpty() ? 0 : (stack.peek() - i);
            stack.push(i);
        }
        return res;
    }
}
```

### References

---

#### 1. [每日温度](https://leetcode.cn/problems/daily-temperatures/)
