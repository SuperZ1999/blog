---
title: "LeetCode 5"
date: 2022-09-24T15:30:02+08:00
tags: ["leetcode"]
draft: false
---

### 思路

遍历一遍数组，同时从中心向两边寻找回文串，并且保存最长的即可。

### 我的代码

```java
class Solution {
    public String longestPalindrome(String s) {
        String res = "";
        for (int i = 0; i < s.length(); i++) {
            // 从中心向两边寻找回文串
            String s1 = findPalindrome(s, i, i);
            String s2 = findPalindrome(s, i, i + 1);
            res = res.length() >= s1.length() ? res : s1;
            res = res.length() >= s2.length() ? res : s2;
        }
        return res;
    }

    private String findPalindrome(String s, int left, int right) {
        while (left >= 0 && right < s.length()
                && s.charAt(left) == s.charAt(right)) {
            left--;
            right++;
        }

        return s.substring(left + 1, right);
    }
}
```

### References

---

#### 1. [最长回文子串](https://leetcode.cn/problems/longest-palindromic-substring/)
