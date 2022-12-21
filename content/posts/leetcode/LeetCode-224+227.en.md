---
title: "LeetCode 224+227"
date: 2022-12-21T14:06:56+08:00
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

根本思想是建立一个栈，栈里存放目前遍历到的数字，比如`1-2+3`，栈里存放`1、-2、3`，最后将栈里的数字相加即可，详见：<https://labuladong.gitee.io/algo/4/33/127/>

### 代码

```java
class Solution {
    private int calculate(StringBuilder sb) {
        Deque<Integer> stack = new ArrayDeque<>();
        int num = 0;
        char sign = '+';
        while (sb.length() > 0) {
            char c = sb.charAt(0);
            sb.deleteCharAt(0);
            if (isDigit(c)) {
                num = num * 10 + c - '0';
            }
            if (c == '(') {
                num = calculate(sb);
            }
            if (!isDigit(c) && c != ' ' || sb.length() == 0) {
                switch (sign) {
                    case '+':
                        stack.push(num);
                        break;
                    case '-':
                        stack.push(-num);
                        break;
                    case '*':
                        stack.push(stack.pop() * num);
                        break;
                    case '/':
                        stack.push(stack.pop() / num);
                        break;
                }
                sign = c;
                num = 0;
            }
            if (c == ')') {
                break;
            }
        }
        int res = 0;
        while (!stack.isEmpty()) {
            res += stack.pop();
        }
        return res;
    }

    public int calculate(String s) {
        return calculate(new StringBuilder(s));
    }

    private boolean isDigit(char c) {
        if (c >= '0' && c <= '9') {
            return true;
        }
        return false;
    }
}
```

### References

---

#### 1. [基本计算器](https://leetcode.cn/problems/basic-calculator/)

#### 2. [基本计算器 II](https://leetcode.cn/problems/basic-calculator-ii/)
