---
title: "LeetCode 567"
date: 2022-09-25T18:13:05+08:00
tags: ["leetcode"]
draft: false
---

### 思路

我的思路：利用滑动窗口的思想，移入窗口一个字符，就收缩窗口直到这个移入的字符在窗口里的数目与s1保持一致，换句话说，保证窗口内不存在非法的字符，当窗口的长度和s1的长度一样时，就找到了这个子串

labuladong的思路：利用滑动窗口的思想，始终保持窗口大小为s1.size()-1，每次移入窗口一个元素，检查一下是否找到子串，如果没有，再让一个元素移出窗口，直到找到这个子串

### 我的代码

```java
class Solution {
    public boolean checkInclusion(String s1, String s2) {
        Map<Character, Integer> need = new HashMap<>();
        Map<Character, Integer> window = new HashMap<>();
        for (int i = 0; i < s1.length(); i++) {
            char c = s1.charAt(i);
            need.put(c, need.getOrDefault(c, 0) + 1);
        }

        int left = 0, right = 0, len = 0;
        while (right < s2.length()) {
            char c = s2.charAt(right);
            right++;
            window.put(c, window.getOrDefault(c, 0) + 1);
            len++;

            while (window.get(c) > need.getOrDefault(c, 0)) {
                char d = s2.charAt(left);
                left++;
                len--;
                window.put(d, window.get(d) - 1);
            }

            if (len == s1.length()) {
                return true;
            }
        }

        return false;
    }
}
```

### 另一种思路

```c++
// 判断 s 中是否存在 t 的排列
bool checkInclusion(string t, string s) {
    unordered_map<char, int> need, window;
    for (char c : t) need[c]++;

    int left = 0, right = 0;
    int valid = 0;
    while (right < s.size()) {
        char c = s[right];
        right++;
        // 进行窗口内数据的一系列更新
        if (need.count(c)) {
            window[c]++;
            if (window[c] == need[c])
                valid++;
        }

        // 判断左侧窗口是否要收缩
        while (right - left >= t.size()) {
            // 在这里判断是否找到了合法的子串
            if (valid == need.size())
                return true;
            char d = s[left];
            left++;
            // 进行窗口内数据的一系列更新
            if (need.count(d)) {
                if (window[d] == need[d])
                    valid--;
                window[d]--;
            }
        }
    }
    // 未找到符合条件的子串
    return false;
}
```

### References

---

#### 1. [字符串的排列](https://leetcode.cn/problems/permutation-in-string/)
