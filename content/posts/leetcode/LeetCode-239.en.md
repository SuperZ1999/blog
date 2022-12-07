---
title: "LeetCode 239"
date: 2022-12-07T13:49:34+08:00
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

利用单调队列的思想即可，保持队列中为单调递减那么队头就是最大值，入栈时把小于两头的元素全部出队（因为这些元素不可能充当窗口内最大值的角色），详见思想篇章

### 代码

```java
class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        int n = nums.length;
        List<Integer> res = new ArrayList<>();
        MonotonicQueue window = new MonotonicQueue();
        for (int i = 0; i < n; i++) {
            if (i < k - 1) {
                window.push(nums[i]);
            } else {
                window.push(nums[i]);
                res.add(window.max());
                window.poll(nums[i - k + 1]);
            }
        }
        int[] arr = new int[res.size()];
        for (int i = 0; i < res.size(); i++) {
            arr[i] = res.get(i);
        }
        return arr;
    }

    class MonotonicQueue {
        LinkedList<Integer> queue = new LinkedList<>();

        private void push(int n) {
            while (!queue.isEmpty() && queue.getLast() < n) {
                queue.pollLast();
            }
            queue.addLast(n);
        }

        private void poll(int n) {
            if (n == queue.getFirst()) {
                queue.pollFirst();
            }
        }

        private int max() {
            return queue.getFirst();
        }
    }
}
```

### References

---

#### 1. [滑动窗口最大值](https://leetcode.cn/problems/sliding-window-maximum/)
