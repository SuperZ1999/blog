---
title: "LeetCode 406"
date: 2022-12-27T19:25:36+08:00
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

我们可以将每个人按照身高从大到小进行排序，然后依次将每个人放入队列中，那么当我们放入第 i 个人时，由于之后的人都比 i 矮，所以不会对 i 当前的插入位置产生影响，所以此时 i 插入的位置其实已经确定了，就是people\[i\]\[1\]个人后面

### 代码

```java
class Solution {
    public int[][] reconstructQueue(int[][] people) {
        List<int[]> queue = new LinkedList<>();
        Arrays.sort(people, (a, b) -> {
            if (a[0] == b[0]) {
                return a[1] - b[1];
            }
            return b[0] - a[0];
        });
        for (int i = 0; i < people.length; i++) {
            queue.add(people[i][1], people[i]);
        }
        queue.toArray(people);
        return people;
    }
}
```

### References

---

#### 1. [根据身高重建队列](https://leetcode.cn/problems/queue-reconstruction-by-height/)
