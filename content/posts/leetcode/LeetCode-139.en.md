---
title: "LeetCode 139"
date: 2022-12-26T10:44:05+08:00
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

两种思路：

#### 记忆化回溯

回溯算法暴力求解，一个一个单词试，不行就回溯，由于存在大量重叠子问题，所以可以用备忘录消除重叠子问题，又因为带备忘录的回溯就相当于动态规划，所以有了第二种思路

#### 动态规划

构建dp数组，数组元素为从当前索引元素开始的字符串，是否能被表示，状态转移方程为：

```java
for (String word : wordList) {
    if (match(s, i, word) && dp[i + word.length()]) {
        dp[i] = true;
        break;
    }
}
```

base case为dp数组最后一个元素设为true，不能优化空间复杂度

### 代码

#### 记忆化回溯

```java
class Solution {
    private Map<Character, List<String>> map = new HashMap<>();
    private Map<Integer, Boolean> memo = new HashMap<>();

    public boolean wordBreak(String s, List<String> wordDict) {
        for (String word : wordDict) {
            if (!map.containsKey(word.charAt(0))) {
                map.put(word.charAt(0), new LinkedList<>());
            }
            map.get(word.charAt(0)).add(word);
        }
        return backtrack(s, 0);
    }

    private boolean backtrack(String s, int start) {
        if (start == s.length()) {
            return true;
        }
        if (memo.containsKey(start)) {
            return memo.get(start);
        }
        List<String> wordList = map.get(s.charAt(start));
        if (wordList == null) {
            memo.put(start, false);
            return false;
        }
        for (String word : wordList) {
            if (!match(s, start, word)) {
                continue;
            }
            if (backtrack(s, start + word.length())) {
                return true;
            }
        }
        memo.put(start, false);
        return false;
    }

    private boolean match(String s, int start, String p) {
        if (p.length() > s.length() - start) {
            return false;
        }
        for (int i = 0; i < p.length(); i++) {
            if (s.charAt(start + i) != p.charAt(i)) {
                return false;
            }
        }
        return true;
    }
}
```

#### 动态规划

```java
class Solution {
    private Map<Character, List<String>> map = new HashMap<>();

    public boolean wordBreak(String s, List<String> wordDict) {
        for (String word : wordDict) {
            if (!map.containsKey(word.charAt(0))) {
                map.put(word.charAt(0), new LinkedList<>());
            }
            map.get(word.charAt(0)).add(word);
        }
        boolean[] dp = new boolean[s.length() + 1];
        dp[s.length()] = true;
        for (int i = s.length() - 1; i >= 0; i--) {
            List<String> wordList = map.get(s.charAt(i));
            if (wordList == null) {
                continue;
            }
            for (String word : wordList) {
                if (match(s, i, word) && dp[i + word.length()]) {
                    dp[i] = true;
                    break;
                }
            }
        }
        return dp[0];
    }

    private boolean match(String s, int start, String p) {
        if (p.length() > s.length() - start) {
            return false;
        }
        for (int i = 0; i < p.length(); i++) {
            if (s.charAt(start + i) != p.charAt(i)) {
                return false;
            }
        }
        return true;
    }
}
```

### References

---

#### 1. [单词拆分](https://leetcode.cn/problems/word-break/solutions/)
