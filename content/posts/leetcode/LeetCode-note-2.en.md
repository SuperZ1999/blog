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

## 编辑距离

### 解法

利用动态规划的思想，dp数组里存*s1[0..i-1] 和 s2[0..j-1]*的编辑距离，可以由以下元素推出来：

![img](https://labuladong.gitee.io/algo/images/editDistance/4.jpg)

base case是第一行和第一列，可以优化空间复杂度但是懒得弄了

补充：具体s1是怎么转换为s2的，可以在dp数组的每个元素里补充额外的信息，详见：<https://labuladong.gitee.io/algo/3/26/75/>

### 题目

#### 1. [编辑距离](https://leetcode.cn/problems/edit-distance/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-72/>

## 最大子数组和

### 解法

dp数组里放以该元素结尾的最大子数组和，可以由前面那个元素推出来，base case是dp[0] = nums[0]，可以优化空间复杂度

还可以利用滑动窗口和前缀和数组解决

### 题目

#### 1. [最大子数组和](https://leetcode.cn/problems/maximum-subarray/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-53/>

## 最长公共子序列

### 解法

利用动态规划的思想，dp数组里存s1[0...i]和s2[0...j]的最长公共子序列，如果s1[i]==s2[j]，dp\[i\]\[j\]由dp\[i-1\]\[j-1\]+1得来，否则dp\[i\]\[j\]由max(dp\[i\]\[j-1\], dp\[i-1\]\[j\])得来，base case是dp\[0\]\[...\]和dp\[...\]\[0\]为0，可以优化空间复杂度

### 题目

#### 1. [最长公共子序列](https://leetcode.cn/problems/longest-common-subsequence/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-1143/>

#### 2. [两个字符串的删除操作](https://leetcode.cn/problems/delete-operation-for-two-strings/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-583/>

#### 3. [两个字符串的最小ASCII删除和](https://leetcode.cn/problems/minimum-ascii-delete-sum-for-two-strings/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-712/>

# 背包问题

## 0-1背包问题

### 解法

见思想篇章

## 子集背包问题

### 解法

见思想篇章

### 题目

#### 1. [分割等和子集](https://leetcode.cn/problems/partition-equal-subset-sum/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-416/>

## 完全背包问题

### 解法

见思想篇章

### 题目

#### 1. [零钱兑换 II](https://leetcode.cn/problems/coin-change-2/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-518/>

# 思想

## 动态规划

动态规划问题有两个重要的特点，分别是最优子结构性质和存在重叠子问题

### 流程

1. 明确状态方程y = f(x)的定义

   1. 确定「状态」，就是能描述一个问题局面所需的变量，也是原问题和子问题中会变化的变量。即y = f(x)中的x
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

一般y = f(x)的x都是数组的索引，y是以这个索引对应的元素结尾的最长...子序列或者数组[0...x]的最长...子序列，两个数组同理，只不过是二维的

如果是两个字符串，求最长...子序列，一个常用的思路就是根据每两个字符是否相同来判断他们是否在结果子序列中，从而避免了对所有子序列进行穷举。

#### 背包问题

##### 0-1背包问题

构造二维dp数组，dp\[i\]\[w\] 的定义如下：对于前 i 个物品，当前背包的容量为 w，这种情况下可以装的最大价值是 dp\[i\]\[w\]。base case是第一行和第一列取值为0，可以优化空间复杂度，模板如下：

```java
int knapsack(int W, int N, int[] wt, int[] val) {
    assert N == wt.length;
    // base case 已初始化
    int[][] dp = new int[N + 1][W + 1];
    for (int i = 1; i <= N; i++) {
        for (int w = 1; w <= W; w++) {
            if (w - wt[i - 1] < 0) {
                // 这种情况下只能选择不装入背包
                dp[i][w] = dp[i - 1][w];
            } else {
                // 装入或者不装入背包，择优
                dp[i][w] = Math.max(
                    dp[i - 1][w - wt[i-1]] + val[i-1], 
                    dp[i - 1][w]
                );
            }
        }
    }
    
    return dp[N][W];
}
```

详见：<https://labuladong.gitee.io/algo/3/27/81/>

##### 子集背包问题

与0-1背包问题相似，就是背包的容量是nums数组和/2，并且问题不是该背包能装多少东西，而是能不能被刚好装满

构造二维dp数组，dp\[i\]\[w\] 的定义如下：对于前 i 个物品，当前背包的容量为 w，这种情况下 dp\[i\]\[w\]表示能否将该背包装满。base case是第一列取值为true，可以优化空间复杂度，但是要注意j需要倒着遍历

模板如下：

```java
boolean canPartition(int[] nums) {
    int sum = 0;
    for (int num : nums) sum += num;
    // 和为奇数时，不可能划分成两个和相等的集合
    if (sum % 2 != 0) return false;
    int n = nums.length;
    sum = sum / 2;
    boolean[][] dp = new boolean[n + 1][sum + 1];
    // base case
    for (int i = 0; i <= n; i++)
        dp[i][0] = true;

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= sum; j++) {
            if (j - nums[i - 1] < 0) {
                // 背包容量不足，不能装入第 i 个物品
                dp[i][j] = dp[i - 1][j];
            } else {
                // 装入或不装入背包
                dp[i][j] = dp[i - 1][j] || dp[i - 1][j - nums[i - 1]];
            }
        }
    }
    return dp[n][sum];
}
```

详见：<https://labuladong.gitee.io/algo/3/27/82/>

##### 完全背包问题

与0-1背包问题相似，构造二维dp数组，dp\[i\]\[w\] 的定义如下：对于前 i 个物品，当前背包的容量为 w，可以重复选择第i个物品，这种情况下正好将背包装满的方式有 dp\[i\]\[w\] 种。base case是第一列取值为1，可以优化空间复杂度，模板如下：

```java
int change(int amount, int[] coins) {
    int n = coins.length;
    int[][] dp = int[n + 1][amount + 1];
    // base case
    for (int i = 0; i <= n; i++) 
        dp[i][0] = 1;

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= amount; j++)
            if (j - coins[i-1] >= 0)
                dp[i][j] = dp[i - 1][j] 
                         + dp[i][j - coins[i-1]];
            else 
                dp[i][j] = dp[i - 1][j];
    }
    return dp[n][amount];
}
```

详见：<https://labuladong.gitee.io/algo/3/27/83/>

# 其他

## 零碎



## 待做

https://labuladong.gitee.io/algo/3/26/79/没看

## 技巧



## 学习方法

