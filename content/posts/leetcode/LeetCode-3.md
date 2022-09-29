---
title: "LeetCode 3"
date: 2022-09-25T22:16:07+08:00
tags: ["leetcode"]
draft: false
---

### 思路

利用滑动窗口的思想，如果窗口内相同元素超过1个，那么就开始收缩直到相同元素被移出，此时窗口内必定没有重复元素，记录一下此时的窗口大小，找出窗口最大时的长度就可以了

### 我的代码

```java
class Solution {
    public int lengthOfLongestSubstring(String s) {
        Map<Character, Integer> window = new HashMap<>();

        int left = 0, right = 0, ans = 0;
        while (right < s.length()) {
            char c = s.charAt(right);
            right++;
            window.put(c, window.getOrDefault(c, 0) + 1);

            while (window.get(c) > 1) {
                char d = s.charAt(left);
                left++;
                window.put(d, window.get(d) - 1);
            }

            ans = Integer.max(ans, right - left);
        }

        return ans;
    }
}
```

### References

---

#### 1. [无重复字符的最长子串](https://leetcode.cn/problems/longest-substring-without-repeating-characters/)
