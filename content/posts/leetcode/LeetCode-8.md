---
title: "LeetCode 8"
date: 2023-01-02T15:41:56+08:00
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

#### 一次遍历

先去除前导空格，然后判断符号位，最后读取数字，注意溢出判断可以通过res除以10是否等于之前的res来判断，详见代码

#### 自动机

详见：<https://leetcode.cn/problems/string-to-integer-atoi/solutions/183164/zi-fu-chuan-zhuan-huan-zheng-shu-atoi-by-leetcode-/>

可以把这个当成模板

### 代码

#### 一次遍历

```java
class Solution {
    public int myAtoi(String s) {
        int res = 0, sign = 1, i = 0, n = s.length();
        for (; i < n; i++) {
            if (s.charAt(i) != ' ') {
                break;
            }
        }
        if (i < n && (s.charAt(i) == '+' || s.charAt(i) == '-')) {
            if (s.charAt(i) == '-') {
                sign = -1;
            }
            i++;
        }
        for (; i < n; i++) {
            if (s.charAt(i) < '0' || s.charAt(i) > '9') {
                break;
            }
            int pre = res;
            res = res * 10 + s.charAt(i) - '0';
            if (res / 10 != pre) {
                return sign == 1 ? Integer.MAX_VALUE : Integer.MIN_VALUE;
            }
        }
        return sign * res;
    }
}
```

#### 自动机

```java
class Solution {
    public int myAtoi(String s) {
        Automaton automaton = new Automaton();
        for (char c : s.toCharArray()) {
            automaton.get(c);
        }
        return (int) (automaton.sign * automaton.res);
    }

    class Automaton {
        int sign = 1;
        long res = 0;
        String state = "start";
        Map<String, String[]> table = new HashMap<>() {
            {
                put("start", new String[]{"start", "signed", "in_number", "end"});
                put("signed", new String[]{"end", "end", "in_number", "end"});
                put("in_number", new String[]{"end", "end", "in_number", "end"});
                put("end", new String[]{"end", "end", "end", "end"});
            }
        };

        public void get(char c) {
            state = table.get(state)[getCol(c)];
            if (state == "in_number") {
                res = res * 10 + c - '0';
                res = sign == 1 ? Math.min(res, Integer.MAX_VALUE) : Math.min(res, -(long) Integer.MIN_VALUE);
            } else if (state == "signed") {
                sign = c == '+' ? 1 : -1;
            }
        }

        private int getCol(char c) {
            if (c == ' ') {
                return 0;
            }
            if (c == '+' || c == '-') {
                return 1;
            }
            if (c >= '0' && c <= '9') {
                return 2;
            }
            return 3;
        }
    }
}
```

### References

---

#### 1. [字符串转换整数 (atoi)](https://leetcode.cn/problems/string-to-integer-atoi/)
