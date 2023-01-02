---
title: "LeetCode 6"
date: 2023-01-02T14:39:08+08:00
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

设置几个行，遍历字符串，每次将遍历到的字符加入行中，然后指针指向下一行，当指针到头之后，倒着改变指针就可以了

### 代码

```java
class Solution {
    public String convert(String s, int numRows) {
        if (numRows == 1) {
            return s;
        }
        StringBuilder[] rows = new StringBuilder[numRows];
        for (int i = 0; i < numRows; i++) {
            rows[i] = new StringBuilder();
        }
        int i = 0, flag = -1;
        for (char c : s.toCharArray()) {
            rows[i].append(c);
            if (i == 0 || i == numRows - 1) {
                flag = -flag;
            }
            i += flag;
        }
        StringBuilder res = new StringBuilder();
        for (int j = 0; j < numRows; j++) {
            res.append(rows[j]);
        }
        return res.toString();
    }
}
```

### References

---

#### 1. [Z 字形变换](https://leetcode.cn/problems/zigzag-conversion/)
