---
title: "LeetCode 155"
date: 2022-12-25T18:59:39+08:00
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

这道题的关键是getMin的实现，可以用一个辅助栈来存储每个元素入栈时的最小值，这样的话当元素出栈时也可以很容易的获取最小值

### 代码

```java
class MinStack {
    private Deque<Integer> stack, minStack;

    public MinStack() {
        this.stack = new ArrayDeque<>();
        this.minStack = new ArrayDeque<>();
        minStack.push(Integer.MAX_VALUE);
    }
    
    public void push(int val) {
        stack.push(val);
        minStack.push(val < minStack.peek() ? val : minStack.peek());
    }
    
    public void pop() {
        stack.pop();
        minStack.pop();
    }
    
    public int top() {
        return stack.peek();
    }
    
    public int getMin() {
        return minStack.peek();
    }
}
```

### References

---

#### 1. [最小栈](https://leetcode.cn/problems/min-stack/)
