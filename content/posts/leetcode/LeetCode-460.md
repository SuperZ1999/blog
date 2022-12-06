---
title: "LeetCode 460"
date: 2022-12-06T14:58:18+08:00
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

经典LFU缓存问题，直接套LFU模板即可，详见思想篇章

### 代码

```java
class LFUCache {
    private Map<Integer, Integer> keyToVal;
    private Map<Integer, Integer> keyToFreq;
    private Map<Integer, LinkedHashSet<Integer>> freqToKeys;
    private int minFreq;
    private int capacity;

    public LFUCache(int capacity) {
        keyToVal = new HashMap<>();
        keyToFreq = new HashMap<>();
        freqToKeys = new HashMap<>();
        this.capacity = capacity;
        this.minFreq = 0;
    }
    
    public int get(int key) {
        if (!keyToVal.containsKey(key)) {
            return -1;
        }

        increaseFreq(key);
        return keyToVal.get(key);
    }
    
    public void put(int key, int value) {
        if (this.capacity == 0) {
            return;
        }

        if (keyToVal.containsKey(key)) {
            keyToVal.put(key, value);
            increaseFreq(key);
            return;
        }

        if (keyToVal.size() == this.capacity) {
            removeMinFreqKey();
        }
        keyToVal.put(key, value);
        keyToFreq.put(key, 1);
        freqToKeys.putIfAbsent(1, new LinkedHashSet<>());
        freqToKeys.get(1).add(key);
        this.minFreq = 1;
    }

    private void increaseFreq(int key) {
       int freq = keyToFreq.get(key);
       keyToFreq.put(key, freq + 1);
       freqToKeys.get(freq).remove(key);
       freqToKeys.putIfAbsent(freq + 1, new LinkedHashSet<>());
       freqToKeys.get(freq + 1).add(key);
       if (freqToKeys.get(freq).isEmpty()) {
           freqToKeys.remove(freq);
           if (this.minFreq == freq) {
               this.minFreq++;
           }
       }
    }

    private void removeMinFreqKey() {
        LinkedHashSet<Integer> keyList = freqToKeys.get(this.minFreq);
        int deleteKey = keyList.iterator().next();
        keyList.remove(deleteKey);
        if (keyList.isEmpty()) {
            freqToKeys.remove(this.minFreq);
            // 这里不用修改minFreq因为后面会置为1
        }
        keyToVal.remove(deleteKey);
        keyToFreq.remove(deleteKey);
    }
}
```

### References

---

#### 1. [LFU 缓存](https://leetcode.cn/problems/lfu-cache/)
