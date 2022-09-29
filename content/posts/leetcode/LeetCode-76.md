---
title: "LeetCode 76"
date: 2022-09-25T17:01:39+08:00
tags: ["leetcode"]
draft: false
---

### 思路

利用滑动窗口的思想，窗口内包含t的所有字符后收缩窗口，同时维护最小覆盖子串的两端的位置，详见LeetCode-note思想章节

### 我的代码

```java
class Solution {
    public String minWindow(String s, String t) {
        Map<Character, Integer> need = new HashMap<>();
        Map<Character, Integer> window = new HashMap<>();
        for (int i = 0; i < t.length(); i++) {
            char c = t.charAt(i);
            need.put(c, need.getOrDefault(c, 0) + 1);
        }

        int left = 0, right = 0, valid = 0, begin = 0, end = Integer.MAX_VALUE;
        // 这里用<而不用<=不是说明使用的闭闭区间，而是right当前位置的元素是我们下一个要入窗口的元素
        // 所以这里其实是闭开窗口
        while (right < s.length()) {
            char c = s.charAt(right);
            right++;
            if (need.containsKey(c)) {
                window.put(c, window.getOrDefault(c, 0) + 1);
                if (window.get(c).equals(need.get(c))) {
                    valid++;
                }
            }

            while (valid == need.size()) {
                if (end - begin > right - left) {
                    begin = left;
                    end = right;
                }
                c = s.charAt(left);
                left++;
                if (need.containsKey(c)) {
                    if (window.get(c).equals(need.get(c))) {
                        valid--;
                    }
                    window.put(c, window.get(c) - 1);
                }
            }
        }

        return end == Integer.MAX_VALUE ? "" : s.substring(begin, end);
    }
}
```

### References

---

#### 1. [最小覆盖子串](https://leetcode.cn/problems/minimum-window-substring/)
