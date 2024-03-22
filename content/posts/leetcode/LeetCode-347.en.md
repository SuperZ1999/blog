---
title: "LeetCode 347"
date: 2022-12-26T21:35:21+08:00
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

#### 简单粗暴版

用map统计次数，用优先队列根据次数选择前k个，具体看代码

#### 最小堆

用map统计次数，然后将map转为entry数组，原问题就转换为了求数组里的前 k 大的值，这个问题用最小堆即可解决，同[LeetCode-215](https://superz1999.github.io/blog/posts/leetcode/leetcode-215/)

#### 快速选择

用map统计次数，然后将map转为entry数组，原问题就转换为了求数组里的前 k 大的值，利用快速选择的思想，每次随机确定一个中枢的位置，如果比中枢大的元素等于k个，那就找到了这k个元素，如果小于k个，那么就确定了比中枢大的几个元素，其他元素在中枢左边，对左边继续这个过程，如果大于k个，对右边继续这个过程

### 代码

#### 简单粗暴版

```java
class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> counter = new HashMap<>();
        for (int num : nums) {
            counter.put(num, counter.getOrDefault(num, 0) + 1);
        }
        Queue<Map.Entry<Integer, Integer>> pq = new PriorityQueue<>((a, b) -> {
            return b.getValue() - a.getValue();
        });
        pq.addAll(counter.entrySet());
        int[] res = new int[k];
        for (int i = 0; i < k; i++) {
            res[i] = pq.poll().getKey();
        }
        return res;
    }
}
```

#### 最小堆

```java
class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> counter = new HashMap<>();
        for (int num : nums) {
            counter.put(num, counter.getOrDefault(num, 0) + 1);
        }
        Queue<Map.Entry<Integer, Integer>> pq = new PriorityQueue<>(k, (a, b) -> {
            return a.getValue() - b.getValue();
        });
        for (Map.Entry<Integer, Integer> entry : counter.entrySet()) {
            if (pq.size() < k) {
                pq.offer(entry);
            } else {
                if (entry.getValue() > pq.peek().getValue()) {
                    pq.poll();
                    pq.offer(entry);
                }
            }
        }
        int[] res = new int[k];
        for (int i = 0; i < k; i++) {
            res[i] = pq.poll().getKey();
        }
        return res;
    }
}
```

#### 快速选择

```java
class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> counter = new HashMap<>();
        for (int num : nums) {
            counter.put(num, counter.getOrDefault(num, 0) + 1);
        }
        Map.Entry<Integer, Integer>[] entries = new Map.Entry[counter.size()];
        counter.entrySet().toArray(entries);
        int[] res = new int[k];
        quickSort(entries, 0, entries.length - 1, res, 0, k);
        return res;
    }

    private void quickSort(Map.Entry<Integer, Integer>[] entries, int left, int right,
                           int[] res, int resIndex, int k) {
        int picked = new Random().nextInt(right - left + 1) + left;
        swap(entries, left, picked);

        int pivot = entries[left].getValue();
        int index = left;
        for (int i = left + 1; i <= right; i++) {
            if (entries[i].getValue() > pivot) {
                swap(entries, index + 1, i);
                index++;
            }
        }
        swap(entries, left, index);

        if (index - left > k) {
            quickSort(entries, left, index - 1, res, resIndex, k);
        } else {
            for (int i = left; i < index; i++) {
                res[resIndex++] = entries[i].getKey();
            }
            if (index - left <= k -1) {
                res[resIndex++] = entries[index].getKey();
                if (index - left < k -1) {
                    quickSort(entries, index + 1, right, res, resIndex, k - index + left - 1);
                }
            }
        }
    }

    private void swap(Map.Entry<Integer, Integer>[] entries, int a, int b) {
        Map.Entry<Integer, Integer> temp = entries[a];
        entries[a] = entries[b];
        entries[b] = temp;
    }
}
```

### References

---

#### 1. [前 K 个高频元素](https://leetcode.cn/problems/top-k-frequent-elements/)
