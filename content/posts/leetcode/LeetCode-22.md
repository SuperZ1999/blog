---
title: "LeetCode 22"
date: 2022-12-18T19:16:38+08:00
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

经典回溯问题，穷举所有可能并且对不合理的情况剪枝即可，剪枝代码如下：

```java
if (right < left) {
    return;
}
if (right < 0 || left < 0) {
    return;
}
```

### 代码

```java
class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> res = new LinkedList<>();
        StringBuilder track = new StringBuilder();
        backtrack(track, n, n, res);
        return res;
    }

    private void backtrack(StringBuilder track, int left, int right, List<String> res) {
        if (right < left) {
            return;
        }
        if (right < 0 || left < 0) {
            return;
        }
        if (right == 0 && left == 0) {
            res.add(track.toString());
        }
        track.append('(');
        backtrack(track, left - 1, right, res);
        track.deleteCharAt(track.length() - 1);
        track.append(')');
        backtrack(track, left, right - 1, res);
        track.deleteCharAt(track.length() - 1);
    }
}
```

### References

---

#### 1. [括号生成](https://leetcode.cn/problems/generate-parentheses/)
