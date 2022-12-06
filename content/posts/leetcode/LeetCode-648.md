---
title: "LeetCode 648"
date: 2022-12-06T16:58:09+08:00
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

经典前缀树（Trie）问题，只不过需要注意将dictionary添加进set即可（因为只添加进set的字符串才能充当前缀）

### 代码

```java
class Solution {
    public String replaceWords(List<String> dictionary, String sentence) {
        TrieSet trieSet = new TrieSet();
        for (String key : dictionary) {
            trieSet.add(key);
        }
        String[] words = sentence.split(" ");
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < words.length; i++) {
            String word = words[i];
            String prefix = trieSet.shortestPrefixOf(word);
            if (prefix.isEmpty()) {
                sb.append(word);
            } else {
                sb.append(prefix);
            }

            if (i != words.length - 1) {
                sb.append(" ");
            }
        }
        return sb.toString();
    }
    
    class TrieSet { /* 见思想篇章 */ }

	class TrieMap { /* 见思想篇章 */ }
}
```

### References

---

#### 1. [单词替换](https://leetcode.cn/problems/replace-words/)
