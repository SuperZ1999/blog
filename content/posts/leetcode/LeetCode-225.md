---
title: "LeetCode 225"
date: 2022-12-08T12:21:22+08:00
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

直接套用队列实现栈的模板即可，详见思想篇章

### 代码

```java
class MyStack {
    private Queue<Integer> q;
    private int topElem;

    public MyStack() {
        q = new LinkedList<>();
    }
    
    public void push(int x) {
        q.offer(x);
        topElem = x;
    }
    
    public int pop() {
        int size = q.size();
        while (size > 2) {
            q.offer(q.poll());
            size--;
        }
        topElem = q.peek();
        q.offer(q.poll());
        return q.poll();
    }
    
    public int top() {
        return topElem;
    }
    
    public boolean empty() {
        return q.isEmpty();
    }
}
```

### References

---

#### 1. [用队列实现栈](https://leetcode.cn/problems/implement-stack-using-queues/)
