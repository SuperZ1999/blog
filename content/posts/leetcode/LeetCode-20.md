---
title: "LeetCode 20"
date: 2022-12-21T16:10:56+08:00
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

用栈即可，直接看代码

### 代码

```java
class Solution {
    public boolean isValid(String s) {
        Deque<Character> stack = new ArrayDeque<>();
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == '(' || c == '[' || c == '{') {
                stack.push(c);
            } else {
                if (stack.isEmpty() || stack.pop() != leftOf(c)) {
                    return false;
                }
            }
        }
        return stack.isEmpty();
    }

    private char leftOf(char c) {
        if (c == ')') {
            return '(';
        }
        if (c == ']') {
            return '[';
        }
        if (c == '}') {
            return '{';
        }
        return ' ';
    }
}
```

### References

---

#### 1. [有效的括号](https://leetcode.cn/problems/valid-parentheses/)
