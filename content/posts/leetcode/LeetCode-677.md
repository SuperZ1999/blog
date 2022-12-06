---
title: "LeetCode 677"
date: 2022-12-06T21:48:51+08:00
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

经典TrieMap问题，不解释

### 代码

```java
class MapSum {
    private TrieMap<Integer> trieMap;

    public MapSum() {
        this.trieMap = new TrieMap();
    }
    
    public void insert(String key, int val) {
        trieMap.put(key, val);
    }
    
    public int sum(String prefix) {
        List<String> keys = trieMap.keysWithPrefix(prefix);
        int res = 0;
        for (String key : keys) {
            res += trieMap.get(key);
        }
        return res;
    }
    
    class TrieMap { /* 见思想篇章 */ }
}
```

### References

---

#### 1. [键值映射](https://leetcode.cn/problems/map-sum-pairs/)
