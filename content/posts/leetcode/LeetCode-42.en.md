---
title: "LeetCode 42"
date: 2022-12-23T12:26:57+08:00
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

四种思路：

#### 按列求

只需要找到每一列左边最大值和右边最大值的较小值，就可以求出这一列可以接多少雨水

#### 动态规划

按列求中，求左边右边的最大值是一个一个遍历的，这个过程可以优化一下，构建dp_left和dp_right数组，里面存放当前元素左边的最大值（右边的最大值），状态转移方程为：`dp_left[i] = Math.max(height[i - 1], dp_left[i - 1])`，base case为dp[0] = 0，可以优化空间复杂度

#### 双指针

其实就是动态规划的优化空间复杂度版本，每个格子能装多少水取决于这个格子左边最高的格子和右边最高的格子，所以可以使用双指针，分别指向左边和右边的格子，遍历这个数组，当左边最大值小于右边最大值时就可以确定左指针的元素能装多少水，因为能装多少水取决于这个格子左边最高的格子和右边最高的格子，而左边最大值小于右边最大值，即使右边有更大的也对结果没影响，然后移动左指针，并且更新左边的最大值即可

#### 单调栈

维护一个单调不增栈，当碰到元素大于栈顶时，出栈，然后取新栈顶和当前元素的较小值，将较小值减去出栈元素就是接的雨水的高度，再乘以新栈顶和当前元素的距离就是接的雨水，直到碰到比当前元素大的栈顶，将当前元素入栈，维护栈为单调不减栈的作用是保证每次计算的雨水都是一层或多层的雨水，详见：<https://leetcode.cn/problems/trapping-rain-water/solutions/9112/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-by-w-8/>

### 代码

#### 按列求

略

#### 动态规划

```java
class Solution {
    public int trap(int[] height) {
        int n = height.length, max = 0;
        int[] left = new int[n], right = new int[n];
        for (int i = 0; i < n; i++) {
            left[i] = max;
            max = Math.max(max, height[i]);
        }
        max = 0;
        for (int i = n - 1; i >= 0; i--) {
            right[i] = max;
            max = Math.max(max, height[i]);
        }
        int res = 0;
        for (int i = 0; i < n; i++) {
            if (Math.min(left[i], right[i]) > height[i]) {
                res += Math.min(left[i], right[i]) - height[i];
            }
        }
        return res;
    }
}
```

#### 双指针

```java
class Solution {
    public int trap(int[] height) {
        int left = 0, right = height.length - 1;
        int l_max = height[left], r_max = height[right];
        int res = 0;
        while (left <= right) {
            l_max = Math.max(l_max, height[left]);
            r_max = Math.max(r_max, height[right]);
            if (l_max < r_max) {
                res += l_max - height[left];
                left++;
            } else {
                res += r_max - height[right];
                right--;
            }
        }
        return res;
    }
}
```

#### 单调栈

```java
class Solution {
    public int trap(int[] height) {
        Deque<Integer> stack = new ArrayDeque<>();
        int i = 0, n = height.length, res = 0;
        while (i < n) {
            while (!stack.isEmpty() && height[i] > height[stack.peek()]) {
                int h = height[stack.pop()];
                if (stack.isEmpty()) {
                    break;
                }
                int distance = i - stack.peek() - 1;
                res += (Math.min(height[i], height[stack.peek()]) - h) * distance;
            }
            stack.push(i);
            i++;
        }
        return res;
    }
}
```

### References

---

#### 1. [接雨水](https://leetcode.cn/problems/trapping-rain-water/)
