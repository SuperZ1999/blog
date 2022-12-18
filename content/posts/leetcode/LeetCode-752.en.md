---
title: "LeetCode 752"
date: 2022-12-18T20:03:24+08:00
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

四个拨轮，每个都可以向上或者向下，所以有8种选择，由此可以抽象为一个图，BFS算法第一次碰到target时走过的长度就是开锁的最少操作次数，注意deadends可以当成已经访问过的结点

### 代码

```java
class Solution {
    public int openLock(String[] deadends, String target) {
        Queue<String> queue = new ArrayDeque<>();
        Set<String> visited = new HashSet<>();
        for (String deadend : deadends) {
            visited.add(deadend);
        }
        if (visited.contains("0000")) {
            return -1;
        }
        queue.offer("0000");
        visited.add("0000");
        int step = 0;
        while (!queue.isEmpty()) {
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                String cur = queue.poll();
                if (cur.equals(target)) {
                    return step;
                }
                for (int j = 0; j < 4; j++) {
                    String minus = minusOne(cur, j);
                    if (!visited.contains(minus)) {
                        queue.offer(minus);
                        visited.add(minus);
                    }
                    String plus = plusOne(cur, j);
                    if (!visited.contains(plus)) {
                        queue.offer(plus);
                        visited.add(plus);
                    }
                }
            }
            step++;
        }
        return -1;
    }

    private String minusOne(String s, int i) {
        char[] chars = s.toCharArray();
        chars[i] = (char) ((chars[i] - '0' + 9) % 10 + '0');
        return new String(chars);
    }

    private String plusOne(String s, int i) {
        char[] chars = s.toCharArray();
        chars[i] = (char) ((chars[i] - '0' + 1) % 10 + '0');
        return new String(chars);
    }
}
```

### References

---

#### 1. [打开转盘锁](https://leetcode.cn/problems/open-the-lock/)
