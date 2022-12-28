---
title: "LeetCode 621"
date: 2022-12-28T21:37:50+08:00
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

这道题明显符合贪心性质，即每次选择需要执行次数最多的且可以执行的任务，这样执行完任务所需的时间就是最优解，以此为根据有两种思路：

#### 模拟

建立一个大根堆，里面放各种任务所需的执行次数，每次弹出min(queue.size(),n)这么多个元素，每个元素都让他都减一，然后再把元素放回去，res += n，最终得到的res就是答案

#### 脑筋急转弯-构造（桶思想）

如下图，把一轮任务的执行想象成一个桶即可，如果能把桶填满，那所需时间就是tasks.length，如果不能那就是桶所占的空间，会不会出现C这个任务在第四行开始，然后排到下一列的第三行呢？这样的话C的执行就冲突了，答：不会，因为我们是按照降序的顺序将任务排列的，如果这样的话C就有5个了，一定会单独占一列，从中间开始排，说明C肯定是小于5的

![image.png](https://pic.leetcode-cn.com/8993d48fb4109d5d207f135bf73e10fd22c898c25113e5fa09bc91829790f9a0-image.png)

详见：<https://leetcode.cn/problems/task-scheduler/solutions/196302/tong-zi-by-popopop/>

### 代码

#### 模拟

```java
class Solution {
    public int leastInterval(char[] tasks, int n) {
        Map<Character, Integer> counter = new HashMap<>();
        for (char task : tasks) {
            counter.put(task, counter.getOrDefault(task, 0) + 1);
        }
        Queue<Integer> queue = new PriorityQueue<>((a, b) -> {
            return b - a;
        });
        for (Integer value : counter.values()) {
            queue.offer(value);
        }
        int res = 0;
        while (!queue.isEmpty()) {
            int count = n + 1;
            List<Integer> temp = new LinkedList<>();
            while (!queue.isEmpty() && count != 0) {
                int i = queue.poll() - 1;
                res++;
                count--;
                if (i != 0) {
                    temp.add(i);
                }
            }
            if (!temp.isEmpty()) {
                res += count;
            }
            queue.addAll(temp);
        }
        return res;
    }
}
```

#### 脑筋急转弯-构造（桶思想）

```java
class Solution {
    public int leastInterval(char[] tasks, int n) {
        int max = Integer.MIN_VALUE;
        Map<Character, Integer> counter = new HashMap<>();
        for (char task : tasks) {
            counter.put(task, counter.getOrDefault(task, 0) + 1);
            max = Math.max(max, counter.get(task));
        }
        int count = 0;
        for (Integer value : counter.values()) {
            if (value == max) {
                count++;
            }
        }
        return Math.max(tasks.length, (max - 1) * (n + 1) + count);
    }
}
```

### References

---

#### 1. [任务调度器](https://leetcode.cn/problems/task-scheduler/)
