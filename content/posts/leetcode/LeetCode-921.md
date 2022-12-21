---
title: "LeetCode 921"
date: 2022-12-21T16:53:56+08:00
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

设置left和right变量，代表需要的左括号数量和右括号数量，从左往右遍历一遍，碰到左括号right++，碰到右括号right--，当right<0时，说明左括号不够了，那就left++，最后left+right就是需要的左右括号数量

### 代码

```java
class Solution {
    public int minAddToMakeValid(String s) {
        int left = 0, right = 0;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == '(') {
                right++;
            } else {
                right--;
                if (right == -1) {
                    right = 0;
                    left++;
                }
            }
        }
        return left + right;
    }
}
```

### References

---

#### 1. [使括号有效的最少添加](https://leetcode.cn/problems/minimum-add-to-make-parentheses-valid/)
