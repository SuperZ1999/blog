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

### 4. [最小路径和](https://leetcode.cn/problems/minimum-path-sum/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-64/>

### 5. [地下城游戏](https://leetcode.cn/problems/dungeon-game/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-174/>

### 6. [鸡蛋掉落](https://leetcode.cn/problems/super-egg-drop/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-887/>

### 7. [戳气球](https://leetcode.cn/problems/burst-balloons/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-312/>

### 8. [单词拆分](https://leetcode.cn/problems/word-break/solutions/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-139/>

### 9. [比特位计数](https://leetcode.cn/problems/counting-bits/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-338/>

### 10. [乘积最大子数组](https://leetcode.cn/problems/maximum-product-subarray/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-152/>

### 11. [最大矩形](https://leetcode.cn/problems/maximal-rectangle/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-85/>

### 12. [最大正方形](https://leetcode.cn/problems/maximal-square/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-221/>

## 正则表达式匹配

### 解法

详见题解

### 题目

#### 1. [正则表达式匹配](https://leetcode.cn/problems/regular-expression-matching/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-10/>

## 股票问题

### 解法

比较复杂，详见：<https://labuladong.gitee.io/algo/3/28/96/>

### 题目

#### 1. [买卖股票的最佳时机](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/)

#### 2. [买卖股票的最佳时机 II](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-ii/)

#### 3. [买卖股票的最佳时机 III](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iii/)

#### 4. [买卖股票的最佳时机 IV](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iv/)

#### 5. [最佳买卖股票时机含冷冻期](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-with-cooldown/)

#### 6. [买卖股票的最佳时机含手续费](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/)

## 打家劫舍问题

### 解法

详见题解

### 题目

#### 1. [打家劫舍](https://leetcode.cn/problems/house-robber/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-198/>

#### 2. [打家劫舍 II](https://leetcode.cn/problems/house-robber-ii/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-213/>

#### 2. [打家劫舍 III](https://leetcode.cn/problems/house-robber-iii/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-337/>

## KMP算法

### 解法

详见思想篇章

### 题目

#### 1. [实现 strStr()](https://leetcode.cn/problems/implement-strstr/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-28/>

#### 2. [通过连接另一个数组的子数组得到一个数组](https://leetcode.cn/problems/form-array-by-concatenating-subarrays-of-another-array/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-1764/>

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

## 最长回文子序列

### 解法

见题解

### 题目

#### 1. [最长回文子序列](https://leetcode.cn/problems/longest-palindromic-subsequence/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-516/>

#### 2. [回文子串](https://leetcode.cn/problems/palindromic-substrings/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-647/>

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

#### 2. [目标和](https://leetcode.cn/problems/target-sum/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-494/>

## 完全背包问题

### 解法

见思想篇章

### 题目

#### 1. [零钱兑换 II](https://leetcode.cn/problems/coin-change-2/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-518/>

# 贪心算法

## 无重叠区间最多有几个

### 解法

利用贪心算法，每次选择结束最早的区间（这就是局部最优选择），然后统计就可以了

### 题目

#### 1. [无重叠区间](https://leetcode.cn/problems/non-overlapping-intervals/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-435/>

#### 2. [用最少数量的箭引爆气球](https://leetcode.cn/problems/minimum-number-of-arrows-to-burst-balloons/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-452/>

## 最少需要几个区间才能覆盖整个x轴

### 解法

利用贪心算法，思路很简单，先按start排序，遍历区间，找end最大的区间，然后再遍历区间找start小于前一个end，end最大的区间，就是代码有点难写

### 题目

#### 1. [视频拼接](https://leetcode.cn/problems/video-stitching/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-1024/>

## 跳跃游戏

### 解法

见题解

### 题目

#### 1. [跳跃游戏](https://leetcode.cn/problems/jump-game/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-55/>

#### 2. [跳跃游戏 II](https://leetcode.cn/problems/jump-game-ii/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-45/>

## 同一时刻最多有多少重叠区间

### 解法

见题解

### 题目

#### 1. [会议室 II](https://leetcode.cn/problems/meeting-rooms-ii/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-253/>

# 暴力搜索算法

## 回溯

### N皇后

#### 解法

利用回溯算法，在棋盘上从上往下下棋子，如果不能下就换个格子，如果一整行都不能下，就回溯到上一行换下一个格子

#### 题目

##### 1. [N 皇后](https://leetcode.cn/problems/n-queens/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-51/>

### 集合划分问题

#### 解法

利用回溯算法，这种排列组合问题的各种变体都可以抽象成「球盒模型」，将子集看成盒子，那么每个盒子遍历一遍数组，要么将元素放盒子里面要么不放，就这样回溯，只不过代码有点难写

#### 题目

##### 1. [划分为k个相等的子集](https://leetcode.cn/problems/partition-to-k-equal-sum-subsets/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-698/>

### 排列组合子集问题

#### 解法

详见思想篇章

#### 题目

##### 1. [子集](https://leetcode.cn/problems/subsets/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-78/>

##### 2. [组合](https://leetcode.cn/problems/combinations/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-77/>

##### 3. [全排列](https://leetcode.cn/problems/permutations/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-46/>

##### 4. [子集 II](https://leetcode.cn/problems/subsets-ii/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-90/>

##### 5. [组合总和 II](https://leetcode.cn/problems/combination-sum-ii/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-40/>

##### 6. [全排列 II](https://leetcode.cn/problems/permutations-ii/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-47/>

##### 7. [组合总和](https://leetcode.cn/problems/combination-sum/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-39/>

### 岛屿问题

#### 解法

利用dfs的思想，遍历矩阵，如果碰到陆地就从这个元素开始dfs，同时将陆地全部变为海水，同时统计岛屿的个数

详见：<https://labuladong.gitee.io/algo/4/31/107/>

#### 题目

##### 1. [岛屿数量](https://leetcode.cn/problems/number-of-islands/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-200/>

##### 2. [统计封闭岛屿的数目](https://leetcode.cn/problems/number-of-closed-islands/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-1254/>

##### 3. [飞地的数量](https://leetcode.cn/problems/number-of-enclaves/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-1020/>

##### 4. [岛屿的最大面积](https://leetcode.cn/problems/max-area-of-island/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-695/>

##### 5. [统计子岛屿](https://leetcode.cn/problems/count-sub-islands/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-1905/>

##### 6. [不同岛屿的数量](https://leetcode.cn/problems/number-of-distinct-islands/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-694/>

### 数独问题

#### 解法

经典回溯问题，暴力求解即可

#### 题目

##### 1. [解数独](https://leetcode.cn/problems/sudoku-solver/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-37/>

### 括号生成

#### 解法

经典回溯问题，穷举所有可能并且对不合理的情况剪枝即可

#### 题目

##### 1. [括号生成](https://leetcode.cn/problems/generate-parentheses/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-22/>

## BFS

### BFS基本问题

#### 解法

套模板即可，详见思想篇章

#### 题目

##### 1. [二叉树的最小深度](https://leetcode.cn/problems/minimum-depth-of-binary-tree/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-111/>

##### 2. [打开转盘锁](https://leetcode.cn/problems/open-the-lock/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-752/>

## DFS

### DFS基本问题

#### 解法

详见题解

#### 题目

##### 1. [删除无效的括号](https://leetcode.cn/problems/remove-invalid-parentheses/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-301/>

# 数学问题

## 随机算法

### 解法

有洗牌算法和蓄水池抽样算法两种，详见思想篇章

### 题目

#### 1. [打乱数组](https://leetcode.cn/problems/shuffle-an-array/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-384/>

#### 2. [链表随机节点](https://leetcode.cn/problems/linked-list-random-node/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-382/>

#### 3. [随机数索引](https://leetcode.cn/problems/random-pick-index/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-398/>

## 位运算

### 解法

就那几个技巧，详见思想篇章

### 题目

#### 1. [位 1 的个数](https://leetcode.cn/problems/number-of-1-bits/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-191/>

#### 2. [2 的幂](https://leetcode.cn/problems/power-of-two/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-231/>

#### 3. [只出现一次的数字](https://leetcode.cn/problems/single-number/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-136/>

#### 4. [丢失的数字](https://leetcode.cn/problems/missing-number/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-268/>

## 阶乘后的零

### 解法

其实求阶乘结果有几个零就是求阶乘式子里可以分解出来几个因数5，其实就是n/5 + n/25 + n/125 + ....

### 题目

#### 1. [阶乘后的零](https://leetcode.cn/problems/factorial-trailing-zeroes/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-172/>

#### 2. [阶乘函数后 K 个零](https://leetcode.cn/problems/preimage-size-of-factorial-zeroes-function/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-793/>

## 素数筛选法

### 解法

详见思想篇章

### 题目

#### 1. [计数质数](https://leetcode.cn/problems/count-primes/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-204/>

## 模幂运算

### 解法

详见思想篇章

### 题目

#### 1. [超级次方](https://leetcode.cn/problems/super-pow/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-372/>

# 经典面试题

## 分治算法

### 解法

通过将原问题分解成小规模的子问题，然后根据子问题的结果构造出原问题的答案。

### 题目

#### 1. [为运算表达式设计优先级](https://leetcode.cn/problems/different-ways-to-add-parentheses/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-241/>

## 分割数组为连续子序列

### 解法

详见题解

### 题目

#### 1. [分割数组为连续子序列](https://leetcode.cn/problems/split-array-into-consecutive-subsequences/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-659/>

## 大整数乘法

### 解法

详见题解

### 题目

#### 1. [字符串相乘](https://leetcode.cn/problems/multiply-strings/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-43/>

## 实现计算器

### 解法

根本思想是建立一个栈，栈里存放目前遍历到的数字，比如`1-2+3`，栈里存放`1、-2、3`，最后将栈里的数字相加即可，详见：<https://labuladong.gitee.io/algo/4/33/127/>

### 题目

#### 1. [基本计算器](https://leetcode.cn/problems/basic-calculator/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-224/>

#### 2. [基本计算器 II](https://leetcode.cn/problems/basic-calculator-ii/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-227/>

## 括号相关问题

### 解法

详见题解

### 题目

#### 1. [有效的括号](https://leetcode.cn/problems/valid-parentheses/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-20/>

#### 2. [使括号有效的最少添加](https://leetcode.cn/problems/minimum-add-to-make-parentheses-valid/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-921/>

#### 3. [平衡括号字符串的最少插入次数](https://leetcode.cn/problems/minimum-insertions-to-balance-a-parentheses-string/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-1541/>

## 区间问题

### 解法

区间类问题看起来都比较复杂，情况很多难以处理，但实际上通过观察各种不同情况之间的共性可以发现规律，用简洁的代码就能处理。

### 题目

#### 1. [删除被覆盖区间](https://leetcode.cn/problems/remove-covered-intervals/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-1288/>

#### 2. [合并区间](https://leetcode.cn/problems/merge-intervals/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-56/>

#### 3. [区间列表的交集](https://leetcode.cn/problems/interval-list-intersections/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-986/>

## 接雨水

### 解法

详见题解

### 题目

#### 1. [接雨水](https://leetcode.cn/problems/trapping-rain-water/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-42/>

#### 2. [盛最多水的容器](https://leetcode.cn/problems/container-with-most-water/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-11/>

## 完美矩形

### 解法

详见题解

### 题目

#### 1. [完美矩形](https://leetcode.cn/problems/perfect-rectangle/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-391/>

## 二分查找高效判定子序列

### 解法

详见题解

### 题目

#### 1. [判断子序列](https://leetcode.cn/problems/is-subsequence/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-392/>

#### 2. [匹配子序列的单词数](https://leetcode.cn/problems/number-of-matching-subsequences/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-792/>

# 思想

## 动态规划

动态规划问题有两个重要的特点，分别是最优子结构性质和存在重叠子问题，只要满足这两个条件都可以用动态规划

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
3. dp数组里的元素怎么根据前面元素推出来（即状态转移方程）
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

记住一个思想s1[i]和s2[j]不相等时，不可能同时出现在最长...子序列中，因为对于当前的子问题来说，s1[i]和s2[j]是字符串的最后一个字符

一般有两种思路，**第一种思路模板是一个一维的 dp 数组**：

```java
int n = array.length;
int[] dp = new int[n];

for (int i = 1; i < n; i++) {
    for (int j = 0; j < i; j++) {
        dp[i] = 最值(dp[i], dp[j] + ...)
    }
}
```

**第二种思路模板是一个二维的 dp 数组**：

```java
int n = arr.length;
int[][] dp = new dp[n][n];

for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
        if (arr[i] == arr[j]) 
            dp[i][j] = dp[i][j] + ...
        else
            dp[i][j] = 最值(...)
    }
}
```

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

子集背包问题就是子集划分问题，就是给定一个数组和一个数字，让求数组里有几种子集和为该数字

与0-1背包问题相似，就是问题不是该背包最多能装多少东西，而是被刚好装满有几种方式

构造二维dp数组，dp\[i\]\[w\] 的定义如下：对于前 i 个物品，当前背包的容量为 w，这种情况下 dp\[i\]\[w\]表示被刚好装满有几种方式。base case是dp\[0\]\[0\]=1（第一列不能都为0，因为数组里可能有0），可以优化空间复杂度，但是要注意j需要倒着遍历

模板如下：

```java
/* 计算 nums 中有几个子集的和为 sum */
int subsets(int[] nums, int sum) {
    int n = nums.length;
    int[][] dp = new int[n + 1][sum + 1];
    // base case
    dp[0][0] = 1;
    
    for (int i = 1; i <= n; i++) {
        for (int j = 0; j <= sum; j++) {
            if (j >= nums[i-1]) {
                // 两种选择的结果之和
                dp[i][j] = dp[i-1][j] + dp[i-1][j-nums[i-1]];
            } else {
                // 背包的空间不足，只能选择不装物品 i
                dp[i][j] = dp[i-1][j];
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

#### KMP算法

比较复杂，详见：<https://labuladong.gitee.io/algo/3/28/97/>

其中状态机的影子X比较难理解，其实就是对于一个自动机，s[0...i]输入之后会走到j这个状态，X就是s[1...i]输入自动机之后走到的状态（所以`X = dp[X][pat.charAt(j)];`，j从1开始），也就是s[0...i]不匹配之后应该走到的状态（因为s[0...i]不匹配，那肯定重新从s[1...i]开始匹配），也就是j这个状态不匹配时应该回到X这个状态，所以有当`pat.charAt(j) != c`时`dp[j][c] = dp[X][c];`，还要注意该自动机是一边生成一边推进j和X的（其实就是动态规划），而不是先生成好自动机，再进行匹配，而且j用到了X（不匹配的时候），X也用到了j（因为X在j的后面，j走过的路自动机已经生成好了），就是下面这张图：

![img](https://labuladong.gitee.io/algo/images/kmp/dfa.gif)

模板如下：

```java
public class KMP {
    private int[][] dp;
    private String pat;

    public KMP(String pat) {
        this.pat = pat;
        int M = pat.length();
        // dp[状态][字符] = 下个状态
        dp = new int[M][256];
        // base case
        dp[0][pat.charAt(0)] = 1;
        // 影子状态 X 初始为 0
        int X = 0;
        // 构建状态转移图（稍改的更紧凑了）
        for (int j = 1; j < M; j++) {
            for (int c = 0; c < 256; c++)
                dp[j][c] = dp[X][c];
            dp[j][pat.charAt(j)] = j + 1;
            // 更新影子状态
            X = dp[X][pat.charAt(j)];
        }
    }

    public int search(String txt) {
        int M = pat.length();
        int N = txt.length();
        // pat 的初始态为 0
        int j = 0;
        for (int i = 0; i < N; i++) {
            // 计算 pat 的下一个状态
            j = dp[j][txt.charAt(i)];
            // 到达终止态，返回结果
            if (j == M) return i - M + 1;
        }
        // 没到达终止态，匹配失败
        return -1;
    }
}
```

## 贪心算法

贪心算法可以认为是动态规划算法的一个特例，相比动态规划，使用贪心算法需要满足更多的条件（贪心选择性质），但是效率比动态规划要高。

什么是贪心选择性质呢，简单说就是：每一步都做出一个局部最优的选择，最终的结果就是全局最优。注意哦，这是一种特殊性质，其实只有一部分问题拥有这个性质。

贪心算法题目，大多一眼就能看出来，大不了就先用动态规划求解，如果动态规划都超时，说明该问题存在贪心选择性质无疑了。

## 回溯

回溯算法和我们常说的 DFS 算法非常类似，本质上就是一种暴力穷举算法。回溯算法和 DFS 算法的细微差别是：**回溯算法是在遍历「树枝」，DFS 算法是在遍历「节点」**

废话不多说，直接上回溯算法框架，解决一个回溯问题，实际上就是一个决策树的遍历过程，站在回溯树的一个节点上，你只需要思考 3 个问题：

1、路径：也就是已经做出的选择。

2、选择列表：也就是你当前可以做的选择。

3、结束条件：也就是到达决策树底层，无法再做选择的条件。

### 模板

```python
result = []
def backtrack(路径, 选择列表):
    if 满足结束条件:
        result.add(路径)
        return
    
    for 选择 in 选择列表:
        # 做选择
        将该选择从选择列表移除
        路径.add(选择)
        backtrack(路径, 选择列表)
        # 撤销选择
        路径.remove(选择)
        将该选择再加入选择列表

```

思考回溯问题时，一定要把递归过程想成一棵树，不同的选择就是不同的分支，backtrack函数开头就是进入一个结点时要做什么，一般都是判断是否应该进入这个结点（其实就是剪枝）和当前结点是否满足结束条件，其实仔细想想，只要是牵扯到递归的都可以想象成一棵树（因为考虑问题比较方便），比如dfs，回溯，等等

其实想想看，回溯算法和动态规划是不是有点像呢？动态规划的三个需要明确的点就是「状态」「选择」和「base case」，正好就对应着走过的「路径」，当前的「选择列表」和「结束条件」

**注意：**

带备忘录的回溯就叫做记忆化回溯，记忆化回溯就相当于动态规划，因为记忆化回溯消除了重叠子问题，消除了重叠子问题就相当于动态规划了

### 排列组合子集问题

由于子集问题和组合问题本质上是一样的，无非就是 base case 有一些区别，所以把这两个问题放在一起看。

**形式一、元素无重不可复选，即 `nums` 中的元素都是唯一的，每个元素最多只能被使用一次**，`backtrack` 核心代码如下：

```java
/* 组合/子集问题回溯算法框架 */
void backtrack(int[] nums, int start) {
    // 回溯算法标准框架
    for (int i = start; i < nums.length; i++) {
        // 做选择
        track.addLast(nums[i]);
        // 注意参数
        backtrack(nums, i + 1);
        // 撤销选择
        track.removeLast();
    }
}

/* 排列问题回溯算法框架 */
void backtrack(int[] nums) {
    for (int i = 0; i < nums.length; i++) {
        // 剪枝逻辑
        if (used[i]) {
            continue;
        }
        // 做选择
        used[i] = true;
        track.addLast(nums[i]);

        backtrack(nums);
        // 撤销选择
        track.removeLast();
        used[i] = false;
    }
}
```

**形式二、元素可重不可复选，即 `nums` 中的元素可以存在重复，每个元素最多只能被使用一次**，其关键在于排序和剪枝，`backtrack` 核心代码如下：

```java
Arrays.sort(nums);
/* 组合/子集问题回溯算法框架 */
void backtrack(int[] nums, int start) {
    // 回溯算法标准框架
    for (int i = start; i < nums.length; i++) {
        // 剪枝逻辑，跳过值相同的相邻树枝
        if (i > start && nums[i] == nums[i - 1]) {
            continue;
        }
        // 做选择
        track.addLast(nums[i]);
        // 注意参数
        backtrack(nums, i + 1);
        // 撤销选择
        track.removeLast();
    }
}


Arrays.sort(nums);
/* 排列问题回溯算法框架 */
void backtrack(int[] nums) {
    for (int i = 0; i < nums.length; i++) {
        // 剪枝逻辑
        if (used[i]) {
            continue;
        }
        // 剪枝逻辑，固定相同的元素在排列中的相对位置
        if (i > 0 && nums[i] == nums[i - 1] && !used[i - 1]) {
            continue;
        }
        // 做选择
        used[i] = true;
        track.addLast(nums[i]);

        backtrack(nums);
        // 撤销选择
        track.removeLast();
        used[i] = false;
    }
}
```

**形式三、元素无重可复选，即 `nums` 中的元素都是唯一的，每个元素可以被使用若干次**，只要删掉去重逻辑即可，`backtrack` 核心代码如下：

```java
/* 组合/子集问题回溯算法框架 */
void backtrack(int[] nums, int start) {
    // 回溯算法标准框架
    for (int i = start; i < nums.length; i++) {
        // 做选择
        track.addLast(nums[i]);
        // 注意参数
        backtrack(nums, i);
        // 撤销选择
        track.removeLast();
    }
}


/* 排列问题回溯算法框架 */
void backtrack(int[] nums) {
    for (int i = 0; i < nums.length; i++) {
        // 做选择
        track.addLast(nums[i]);
        backtrack(nums);
        // 撤销选择
        track.removeLast();
    }
}
```

详见：<https://labuladong.gitee.io/algo/4/31/106/>

## BFS

即广度优先搜索，不多说了，模板如下：

```java
// 计算从起点 start 到终点 target 的最近距离
int BFS(Node start, Node target) {
    Queue<Node> q; // 核心数据结构
    Set<Node> visited; // 避免走回头路
    
    q.offer(start); // 将起点加入队列
    visited.add(start);
    int step = 0; // 记录扩散的步数

    while (q not empty) {
        int sz = q.size();
        /* 将当前队列中的所有节点向四周扩散 */
        for (int i = 0; i < sz; i++) {
            Node cur = q.poll();
            /* 划重点：这里判断是否到达终点 */
            if (cur is target)
                return step;
            /* 将 cur 的相邻节点加入队列 */
            for (Node x : cur.adj()) {
                if (x not in visited) {
                    q.offer(x);
                    visited.add(x);
                }
            }
        }
        /* 划重点：更新步数在这里 */
        step++;
    }
}
```

队列 `q` 就不说了，BFS 的核心数据结构；`cur.adj()` 泛指 `cur` 相邻的节点，比如说二维数组中，`cur` 上下左右四面的位置就是相邻节点；`visited` 的主要作用是防止走回头路，大部分时候都是必须的，但是像一般的二叉树结构，没有子节点到父节点的指针，不会走回头路就不需要 `visited`。

流程如下所示：

![img](https://labuladong.gitee.io/algo/images/dijkstra/1.jpeg)

## 数学

### 随机算法

#### 洗牌算法

一般解决随机打乱一个数组问题，算法如下：

```java
public int[] shuffle(int[] nums) {
    int n = nums.length;
    for (int i = 0 ; i < n; i++) {
        // 生成一个 [i, n-1] 区间内的随机数
        int r = i + rand.nextInt(n - i);
        // 交换 nums[i] 和 nums[r]
        swap(nums, i, r);
    }
    return copy;
}
```

#### 蓄水池抽样算法

可以解决在一堆数据中随机取出一个或多个数据，算法如下：

```java
/* 返回链表中一个随机节点的值 */
int getRandom(ListNode head) {
    Random r = new Random();
    int i = 0, res = 0;
    ListNode p = head;
    // while 循环遍历链表
    while (p != null) {
        i++;
        // 生成一个 [0, i) 之间的整数
        // 这个整数等于 0 的概率就是 1/i
        if (0 == r.nextInt(i)) {
            res = p.val;
        }
        p = p.next;
    }
    return res;
}
```

证明如下：

![img](https://labuladong.gitee.io/algo/images/%e6%b0%b4%e5%a1%98%e6%8a%bd%e6%a0%b7/formula1.png)

取出k个元素：

```java
/* 返回链表中 k 个随机节点的值 */
int[] getRandom(ListNode head, int k) {
    Random r = new Random();
    int[] res = new int[k];
    ListNode p = head;

    // 前 k 个元素先默认选上
    for (int i = 0; i < k && p != null; i++) {
        res[i] = p.val;
        p = p.next;
    }

    int i = k;
    // while 循环遍历链表
    while (p != null) {
        i++;
        // 生成一个 [0, i) 之间的整数
        int j = r.nextInt(i);
        // 这个整数小于 k 的概率就是 k/i
        if (j < k) {
            res[j] = p.val;
        }
        p = p.next;
    }
    return res;
}
```

证明如下：

![img](https://labuladong.gitee.io/algo/images/%e6%b0%b4%e5%a1%98%e6%8a%bd%e6%a0%b7/formula2.png)

详见：<https://labuladong.gitee.io/algo/4/32/113/>

### 位运算

1. **判断两个数是否异号**

```java
int x = -1, y = 2;
boolean f = ((x ^ y) < 0); // true

int x = 3, y = 2;
boolean f = ((x ^ y) < 0); // false
```

2. **n & (n-1) 的运用**

消除数字 n 的二进制表示中的最后一个 1，即Brian Kernighan算法

3. **a ^ a = 0 的运用**

一个数和它本身做异或运算结果为 0，即 `a ^ a = 0`；一个数和 0 做异或运算的结果为它本身，即 `a ^ 0 = a`。而且异或运算满足交换律和结合律

### 素数筛选法

求[2...n]之间的所有的素数可以这样求，从2开始遍历，遍历到的数字的整数倍一定不是素数，这样排除遍历到n的时候，没被排除的就是[2...n]的素数，模板如下：

```java
int countPrimes(int n) {
    boolean[] isPrime = new boolean[n];
    Arrays.fill(isPrime, true);
    for (int i = 2; i * i < n; i++) 
        if (isPrime[i]) 
            for (int j = i * i; j < n; j += i) 
                isPrime[j] = false;
    
    int count = 0;
    for (int i = 2; i < n; i++)
        if (isPrime[i]) count++;
    
    return count;
}
```

这里优化了两个地方，详见：<https://labuladong.gitee.io/algo/4/32/116/>

### 模幂运算

模幂运算就是求`a^b%k`，就是对幂取模，所以叫模幂运算

`(a * b) % k = ((a % k) * (b % k)) % k`，当a*b会溢出时可以用这个技巧，可以拓展到多个数相乘然后取余，只不过要记得每个乘法都要做一次这个运算，比如`(a * b * c) % k -> (((a % k) * (b % k)) % k) * c = (((a % k) * (b % k)) % k) * (c % k) % k`，只要做乘法就要取模

#### 模板

```java
int base = 1337;
// 计算 a 的 k 次方然后与 base 求模的结果
int mypow(int a, int k) {
    // 对因子求模
    a %= base;
    int res = 1;
    for (int _ = 0; _ < k; _++) {
        // 这里有乘法，是潜在的溢出点
        res *= a;
        // 对乘法结果求模
        res %= base;
    }
    return res;
}
```

**如何高效求幂？**

利用幂运算的性质，我们可以写出这样一个递归式：

![img](https://labuladong.gitee.io/algo/images/superPower/formula2.png)

这样就不用傻乎乎的从第一个乘到最后一个了

#### 模板

```java
int base = 1337;

int mypow(int a, int k) {
    if (k == 0) return 1;
    a %= base;

    if (k % 2 == 1) {
        // k 是奇数
        return (a * mypow(a, k - 1)) % base;
    } else {
        // k 是偶数
        int sub = mypow(a, k / 2);
        return (sub * sub) % base;
    }
}
```

### 零碎 

- 四平方和定理证明了任意一个正整数都可以被表示为至多四个正整数的平方和。这给出了本题的答案的上界。四平方和定理证明了任意一个正整数都可以被表示为至多四个正整数的平方和。这给出了本题的答案的上界。详见：<https://leetcode.cn/problems/perfect-squares/solutions/822940/wan-quan-ping-fang-shu-by-leetcode-solut-t99c/>

## 分治算法

分治算法可以认为是一种算法思想，通过将原问题分解成小规模的子问题，然后根据子问题的结果构造出原问题的答案。

与动态规划和回溯类似，都是通过子问题的解推出来的原问题的解

详见：<https://labuladong.gitee.io/algo/4/33/122/>

# 其他

## 零碎

二分查找的左侧边界的定义就是该边界及该边界右边的元素都大于等于查找元素，右侧边界的定义就是该边界及该边界左边的元素都小于等于查找元素

### 字符串比较大小

比如ABC与ACDE比较，第一个字符相同，继续比较第二个字符，由于第二个字符是后面一个串大，所以不再继续比较，结果就是后面个串大。再如ABC与ABC123比较，比较三个字符后第一个串结束，所以就是后面一个串大，可以认为一个字符串到头了那这个字符串当前比较的字符就是最小的（因为这个字符都不存在）

## 待做

LinkedHashMap是什么

https://labuladong.gitee.io/algo/3/28/88/没看

https://labuladong.gitee.io/algo/3/28/89/没看

https://labuladong.gitee.io/algo/3/28/93/没看

https://labuladong.gitee.io/algo/3/28/94/没看

https://labuladong.gitee.io/algo/3/28/91/没看

https://labuladong.gitee.io/algo/3/28/92/没看

https://labuladong.gitee.io/algo/4/31/111/没看

https://labuladong.gitee.io/algo/4/32/118/没看

https://labuladong.gitee.io/algo/4/33/125/没看

https://labuladong.gitee.io/algo/4/33/131/没看

山谷(Valley)问题是什么（二分查找）

## 技巧



## 学习方法

