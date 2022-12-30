---
title: "LeetCode 301"
date: 2022-12-30T20:24:27+08:00
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

根本思想就是将字符串删去字符的所有情况都找出来，所以可以用DFS爆搜，就是对于每个括号字符，要么删，要么不删，并且在搜索过程中将不合理的情况剪枝（直接return即可），比如右括号比左括号多的情况，左括号或者右括号删多了的情况，如此一来只对合理情况进行判断，如果字符串是合理的，并且删除的左右括号数量也正确，那这个字符串就是结果之一，将这些字符串加入Set去重即可

详见：<https://leetcode.cn/problems/remove-invalid-parentheses/solutions/1068652/gong-shui-san-xie-jiang-gua-hao-de-shi-f-asu8/>

### 代码

```java
class Solution {
    private Set<String> res = new HashSet<>();
    private int max, n, len = -1;
    private String str;

    public List<String> removeInvalidParentheses(String s) {
        str = s;
        n = s.length();
        int left = 0, right = 0;
        int deleteLeft = 0, deleteRight = 0;
        for (char c : s.toCharArray()) {
            if (c == '(') {
                left++;
                deleteLeft++;
            } else if (c == ')') {
                right++;
                if (deleteLeft == 0) {
                    deleteRight++;
                } else {
                    deleteLeft--;
                }
            }
        }
        len = n - deleteLeft - deleteRight;
        max = Math.min(left, right);
        dfs(0, "", deleteLeft, deleteRight, 0);
        return new ArrayList<>(res);
    }

    private void dfs(int start, String curr, int deleteLeft, int deleteRight, int score) {
        if (score < 0 || score > max || deleteLeft < 0 || deleteRight < 0) {
            return;
        }
        if (deleteLeft == 0 && deleteRight == 0 && curr.length() == len) {
            res.add(curr);
        }
        if (start == n) {
            return;
        }
        char c = str.charAt(start);
        if (c == '(') {
            dfs(start + 1, curr + c, deleteLeft, deleteRight, score + 1);
            dfs(start + 1, curr,deleteLeft - 1, deleteRight, score);
        } else if (c == ')') {
            dfs(start + 1, curr + c, deleteLeft, deleteRight, score - 1);
            dfs(start + 1, curr, deleteLeft, deleteRight - 1, score);
        } else {
            dfs(start + 1, curr + c, deleteLeft, deleteRight, score);
        }
    }
}
```

### References

---

#### 1. [删除无效的括号](https://leetcode.cn/problems/remove-invalid-parentheses/)
