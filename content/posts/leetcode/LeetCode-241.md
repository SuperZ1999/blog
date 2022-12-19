---
title: "LeetCode 241"
date: 2022-12-19T22:46:17+08:00
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

经典分治思想，根据式子的运算符分成左右两个子问题，然后将两个子问题合并，就得到了原问题的答案，详见思想篇章

### 代码

```java
class Solution {
    private Map<String, List<Integer>> memo = new HashMap<>();

    public List<Integer> diffWaysToCompute(String expression) {
        if (memo.containsKey(expression)) {
            return memo.get(expression);
        }
        List<Integer> res = new LinkedList<>();
        for (int i = 0; i < expression.length(); i++) {
            char c = expression.charAt(i);
            if (c == '+' || c == '-' || c == '*') {
                List<Integer> left = diffWaysToCompute(expression.substring(0, i));
                List<Integer> right = diffWaysToCompute(expression.substring(i + 1));
                for (Integer l : left) {
                    for (Integer r : right) {
                        if (c == '+') {
                            res.add(l + r);
                        } else if (c == '*') {
                            res.add(l * r);
                        } else if (c == '-') {
                            res.add(l - r);
                        }
                    }
                }
            }
        }
        if (res.isEmpty()) {
            res.add(Integer.parseInt(expression));
        }
        memo.put(expression, res);
        return res;
    }
}
```

### References

---

#### 1. [为运算表达式设计优先级](https://leetcode.cn/problems/different-ways-to-add-parentheses/)
