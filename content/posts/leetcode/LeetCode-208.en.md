---
title: "LeetCode 208"
date: 2022-12-06T16:41:25+08:00
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

经典前缀树（Trie）问题，直接套模板即可，详见思想篇章

### 代码

```java
class Trie {
    private TrieSet trieSet;

    public Trie() {
        this.trieSet = new TrieSet();
    }
    
    public void insert(String word) {
        trieSet.add(word);
    }
    
    public boolean search(String word) {
        return trieSet.contains(word);
    }
    
    public boolean startsWith(String prefix) {
        return trieSet.hasKeyWithPrefix(prefix);
    }
    
    class TrieSet { /* 见思想篇章 */ }

	class TrieMap { /* 见思想篇章 */ }
}
```

### References

---

#### 1. [实现 Trie (前缀树)](https://leetcode.cn/problems/implement-trie-prefix-tree/)
