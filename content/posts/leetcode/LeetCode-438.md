---
title: "LeetCode 438"
date: 2022-09-25T21:52:06+08:00
tags: ["leetcode"]
draft: false
---

### 思路

同LeetCode-567，只不过找到子串后不直接返回而是存一下，同样是两种思路，详见：<https://blog.zhangmengyang.tk/leetcodes/leetcode-567/>

### 我的代码

```java
class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        Map<Character, Integer> need = new HashMap<>();
        Map<Character, Integer> window = new HashMap<>();
        for (int i = 0; i < p.length(); i++) {
            char c = p.charAt(i);
            need.put(c, need.getOrDefault(c, 0) + 1);
        }

        int left = 0, right = 0, len = 0;
        List<Integer> ans = new ArrayList<>();
        while (right < s.length()) {
            char c = s.charAt(right);
            right++;
            window.put(c, window.getOrDefault(c, 0) + 1);
            len++;

            while (window.get(c) > need.getOrDefault(c, 0)) {
                char d = s.charAt(left);
                left++;
                len--;
                window.put(d, window.get(d) - 1);
            }

            if (len == p.length()) {
                ans.add(left);
                char d = s.charAt(left);
                left++;
                len--;
                window.put(d, window.get(d) - 1);
            }
        }

        return ans;
    }
}
```

### 另一种思路

```c++
vector<int> findAnagrams(string s, string t) {
    unordered_map<char, int> need, window;
    for (char c : t) need[c]++;

    int left = 0, right = 0;
    int valid = 0;
    vector<int> res; // 记录结果
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
            // 当窗口符合条件时，把起始索引加入 res
            if (valid == need.size())
                res.push_back(left);
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
    return res;
}
```

### References

---

#### 1. [找到字符串中所有字母异位词](https://leetcode.cn/problems/find-all-anagrams-in-a-string/)
