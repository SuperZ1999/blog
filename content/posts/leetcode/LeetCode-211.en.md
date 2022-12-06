---
title: "LeetCode 211"
date: 2022-12-06T17:05:05+08:00
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

利用Trie树的思想即可，详见思想篇章

### 代码

```java
class WordDictionary {
    private TrieNode root;

    private static class TrieNode {
        boolean isEnd = false;
        TrieNode[] children = new TrieNode[26];
    }

    public WordDictionary() {
        this.root = new TrieNode();
    }

    public void addWord(String word) {
        this.root = put(root, word, 0);
    }

    private TrieNode put(TrieNode node, String word, int i) {
        if (node == null) {
            node = new TrieNode();
        }
        if (i == word.length()) {
            node.isEnd = true;
            return node;
        }

        int c = word.charAt(i) - 'a';
        node.children[c] = put(node.children[c], word, i + 1);
        return node;
    }

    public boolean search(String word) {
        return hasKeyWithPattern(root, word, 0);
    }

    private boolean hasKeyWithPattern(TrieNode node, String word, int i) {
        if (node == null) {
            return false;
        }

        if (i == word.length()) {
            return node.isEnd;
        }

        char c = word.charAt(i);
        if (c != '.') {
            return hasKeyWithPattern(node.children[c - 'a'], word, i + 1);
        }
        for (int j = 0; j < 26; j++) {
            if (hasKeyWithPattern(node.children[j], word, i + 1)) {
                return true;
            }
        }
        return false;
    }
}
```

### References

---

#### 1. [添加与搜索单词 - 数据结构设计](https://leetcode.cn/problems/design-add-and-search-words-data-structure/)
