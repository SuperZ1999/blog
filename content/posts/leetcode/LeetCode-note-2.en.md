---
title: "LeetCode Note 2"
date: 2022-12-09T19:25:56+08:00
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

# 动态规划基本问题

## 解法

经典动态规划问题，详见思想篇章

## 题目

### 1. [斐波那契数](https://leetcode.cn/problems/fibonacci-number/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-509/>

### 2. [零钱兑换](https://leetcode.cn/problems/coin-change/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-322/>

### 3. [下降路径最小和](https://leetcode.cn/problems/minimum-falling-path-sum/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-931/>

# 子序列问题

## 最长递增子序列

### 解法

利用动态规划的思想，y=f(x)的x是数组的索引，y是以这个索引的元素结尾的最长递增子序列的长度，选择为x之前所有元素的索引，base case为f(0) = 1，具有最优子结构，状态转移方程为f(x) = ....(懒得写了)，会有重叠子问题所以用dp数组记录，无法优化空间复杂度

### 题目

#### 1. [最长递增子序列](https://leetcode.cn/problems/longest-increasing-subsequence/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-300/>

#### 2. [俄罗斯套娃信封问题](https://leetcode.cn/problems/russian-doll-envelopes/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-354/>

# 思想

## 动态规划

动态规划问题有两个重要的特点，分别是最优子结构性质和存在重叠子问题

### 流程

1. 明确状态方程y = f(x)的定义

   1. 确定「状态」，也就是原问题和子问题中会变化的变量。即y = f(x)中的x
   2. 确定y = f(x)中的y，一般是问题要求我们计算的量
   3. 确定「选择」，也就是导致「状态」产生变化的行为。即状态转移方程里的x应该选择哪一个
   4. 确定base case
2. 写出状态转移方程（列出状态转移方程，就是在解决“如何穷举”的问题。），这个过程就是判断问题是否具有最优子结构性质（就是能否通过子问题的最优解求出原问题的最优解），此时可以通过状态转移方程写出递归写法，递归写法就是自顶向下的解法，但是这种写法一般存在重叠子问题
3. 判断问题是否具有重叠子问题，如果有，使用DP table代替f(x)函数，同时将递归改成迭代（也就是自底向上），DP table起到了记录子问题的作用，DP table 就是在追求“如何聪明地穷举”
4. 优化空间复杂度，如果我们发现每次状态转移只需要 DP table 中的一部分，那么可以尝试缩小 DP table 的大小，只记录必要的数据，从而降低空间复杂度

#### 精简流程

1. 构造一个dp数组
2. 确定dp数组里面放什么
3. dp数组里的元素怎么根据前面元素推出来
4. base case
5. 优化空间复杂度

### 注意点

- 动态规划的核心问题是“如何穷举”（状态转移方程），然后考虑“如何聪明地穷举”（消除重叠子问题、剪枝）
- 算法设计无非就是先思考“如何穷举”，然后再追求“如何聪明地穷举”
- 递归是自顶向下，dp table迭代是自底向上
- dp数组的大小有时候要比原问题大一点，目的是防止特殊判断和dummy node的原理类似
- dp 数组的遍历方向只要保证两点即可
  - 遍历的过程中，所需的状态必须是已经计算出来的
  - 遍历结束后，存储结果的那个位置必须已经被计算出来

### 经典问题

#### 子序列问题

一般y = f(x)的x都是数组的索引，y是以这个索引对应的元素结尾的最长...子序列
