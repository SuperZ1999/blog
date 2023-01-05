---
title: "LeetCode 17"
date: 2023-01-05T20:59:58+08:00
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

经典回溯问题，对于每个数字都有几种选择，套模板即可

### 代码

```java
class Solution {
    private List<String> res = new LinkedList<>();
    private char[][] table = new char[][]{
            {},
            {},
            {'a', 'b', 'c'},
            {'d', 'e', 'f'},
            {'g', 'h', 'i'},
            {'j', 'k', 'l'},
            {'m', 'n', 'o'},
            {'p', 'q', 'r', 's'},
            {'t', 'u', 'v'},
            {'w', 'x', 'y', 'z'}
    };

    public List<String> letterCombinations(String digits) {
        if (digits.isEmpty()) {
            return res;
        }
        backtrack("", digits, 0);
        return res;
    }

    private void backtrack(String s, String digits, int start) {
        if (start == digits.length()) {
            res.add(s);
            return;
        }
        char[] choices = table[digits.charAt(start) - '0'];
        for (char c : choices) {
            backtrack(s + c, digits, start + 1);
        }
    }
}
```

### References

---

#### 1. [电话号码的字母组合](https://leetcode.cn/problems/letter-combinations-of-a-phone-number/)
