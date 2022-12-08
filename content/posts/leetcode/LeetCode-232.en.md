---
title: "LeetCode 232"
date: 2022-12-08T12:09:36+08:00
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

直接套栈实现队列模板即可，详见思想篇章

### 代码

```java
class MyQueue {
    private Stack<Integer> s1, s2;

    public MyQueue() {
        s1 = new Stack<>();
        s2 = new Stack<>();
    }
    
    public void push(int x) {
        s2.push(x);
    }
    
    public int pop() {
        peek();
        return s1.pop();
    }
    
    public int peek() {
        if (s1.isEmpty()) {
            while (!s2.isEmpty()) {
                s1.push(s2.pop());
            }
        }
        return s1.peek();
    }
    
    public boolean empty() {
        return s1.isEmpty() && s2.isEmpty();
    }
}
```

### References

---

#### 1. [用栈实现队列](https://leetcode.cn/problems/implement-queue-using-stacks/)
