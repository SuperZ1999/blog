---
title: "LeetCode 394"
date: 2022-12-27T15:38:04+08:00
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

两种思路：

#### 递归

一种是模拟递归（就是我写的），一种是利用文法（见：<https://leetcode.cn/problems/decode-string/solutions/264391/zi-fu-chuan-jie-ma-by-leetcode-solution/>）

模拟递归就是从左往右遍历字符串，碰到字母就加入结果中，碰到数字就读取数字，碰到'['就递归获取中括号里面的字符串用于拼接，碰到']'就直接返回，因为这里碰到']'就说明本次调用是求[]里面的字符串，正常情况下是不会碰到']'的，遍历完字符串就得到了结果

#### 栈

遍历这个字符串：

- 如果当前的字符为数位，解析出一个数字（连续的多个数位）并进栈
- 如果当前的字符为字母或者左括号，直接进栈
- 如果当前的字符为右括号，开始出栈，一直到左括号出栈，出栈序列反转后拼接成一个字符串，此时取出栈顶的数字，就是这个字符串应该出现的次数，我们根据这个次数和字符串构造出新的字符串并进栈

重复如上操作，最终将栈中的元素按照从栈底到栈顶的顺序拼接起来，就得到了答案。

### 代码

#### 递归

```java
class Solution {
    public String decodeString(String s) {
        StringBuilder sb = new StringBuilder();
        int num = 0;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c >= 'a' && c <= 'z') {
                sb.append(c);
            } else if (c >= '0' && c <= '9') {
                num = num * 10 + c - '0';
            } else if (c == '[') {
                String str = decodeString(s.substring(i + 1));
                while (num != 0) {
                    sb.append(str);
                    num--;
                }
                int needRight = 0;
                while (needRight != -1) {
                    i++;
                    c = s.charAt(i);
                    if (c == '[') {
                        needRight++;
                    }
                    if (c == ']') {
                        needRight--;
                    }
                }
            } else if (c == ']') {
                return sb.toString();
            }
        }
        return sb.toString();
    }
}
```

#### 栈

```java
class Solution {
    public String decodeString(String s) {
        int n = s.length(), i = 0;
        Deque<String> stack = new ArrayDeque<>();
        while (i < n) {
            char c = s.charAt(i);
            if (Character.isLetter(c) || c == '[') {
                stack.push(String.valueOf(c));
                i++;
            } else if (Character.isDigit(c)) {
                int num = 0;
                while (Character.isDigit(s.charAt(i))) {
                    num = num * 10 + s.charAt(i) - '0';
                    i++;
                }
                stack.push(String.valueOf(num));
            } else if (c == ']') {
                i++;
                String sub = "";
                while (!stack.peek().equals("[")) {
                    sub = stack.pop() + sub;
                }
                stack.pop();
                int num = Integer.parseInt(stack.pop());
                String t = "";
                while (num != 0) {
                    t = t + sub;
                    num--;
                }
                stack.push(t);
            }
        }
        String res = "";
        while (!stack.isEmpty()) {
            res = stack.pop() + res;
        }
        return res;
    }
}
```

### References

---

#### 1. [字符串解码](https://leetcode.cn/problems/decode-string/)
