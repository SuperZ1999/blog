---
title: "LeetCode 3"
date: 2022-09-25T22:16:07+08:00
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

利用滑动窗口的思想，如果窗口内相同元素超过1个，那么就开始收缩直到相同元素被移出，此时窗口内必定没有重复元素，记录一下此时的窗口大小，找出窗口最大时的长度就可以了

### 代码

```java
class Solution {
    public int lengthOfLongestSubstring(String s) {
        int n = s.length(), left = 0, right = 0, res = 0;
        Set<Character> window = new HashSet<>();
        while (right < n) {
            char c = s.charAt(right);
            right++;

            while (window.contains(c)) {
                char d = s.charAt(left);
                left++;
                window.remove(d);
            }
            window.add(c);
            res = Math.max(res, window.size());
        }
        return res;
    }
}
```

### References

---

#### 1. [无重复字符的最长子串](https://leetcode.cn/problems/longest-substring-without-repeating-characters/)
