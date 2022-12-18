---
title: "LeetCode 398"
date: 2022-12-18T22:40:35+08:00
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

不解释了，直接看代码

### 代码

```java
class Solution {
    private Map<Integer, List<Integer>> map;

    public Solution(int[] nums) {
        map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            if (!map.containsKey(nums[i])) {
                map.put(nums[i], new LinkedList<>());
            }
            map.get(nums[i]).add(i);
        }
    }
    
    public int pick(int target) {
        List<Integer> list = map.get(target);
        return list.get(new Random().nextInt(list.size()));
    }
}
```

### References

---

#### 1. [随机数索引](https://leetcode.cn/problems/random-pick-index/)
