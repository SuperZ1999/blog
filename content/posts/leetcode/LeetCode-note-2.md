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

# 回溯问题

## N皇后

### 解法

利用回溯算法，在棋盘上从上往下下棋子，如果不能下就换个格子，如果一整行都不能下，就回溯到上一行换下一个格子

### 题目

#### 1. [N 皇后](https://leetcode.cn/problems/n-queens/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-51/>

## 集合划分问题

### 解法

利用回溯算法，这种排列组合问题的各种变体都可以抽象成「球盒模型」，将子集看成盒子，那么每个盒子遍历一遍数组，要么将元素放盒子里面要么不放，就这样回溯，只不过代码有点难写

### 题目

#### 1. [划分为k个相等的子集](https://leetcode.cn/problems/partition-to-k-equal-sum-subsets/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-698/>

## 排列组合子集问题

### 解法

详见思想篇章

### 题目

#### 1. [子集](https://leetcode.cn/problems/subsets/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-78/>

#### 2. [组合](https://leetcode.cn/problems/combinations/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-77/>

#### 3. [全排列](https://leetcode.cn/problems/permutations/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-46/>

#### 4. [子集 II](https://leetcode.cn/problems/subsets-ii/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-90/>

#### 5. [组合总和 II](https://leetcode.cn/problems/combination-sum-ii/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-40/>

#### 6. [全排列 II](https://leetcode.cn/problems/permutations-ii/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-47/>

#### 7. [组合总和](https://leetcode.cn/problems/combination-sum/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-39/>

## 岛屿问题

### 解法

利用dfs的思想，遍历矩阵，如果碰到陆地就从这个元素开始dfs，同时将陆地全部变为海水，同时统计岛屿的个数

详见：<https://labuladong.gitee.io/algo/4/31/107/>

### 题目

#### 1. [岛屿数量](https://leetcode.cn/problems/number-of-islands/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-200/>

#### 2. [统计封闭岛屿的数目](https://leetcode.cn/problems/number-of-closed-islands/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-1254/>

#### 3. [飞地的数量](https://leetcode.cn/problems/number-of-enclaves/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-1020/>

#### 4. [岛屿的最大面积](https://leetcode.cn/problems/max-area-of-island/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-695/>

#### 5. [统计子岛屿](https://leetcode.cn/problems/count-sub-islands/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-1905/>

#### 6. [不同岛屿的数量](https://leetcode.cn/problems/number-of-distinct-islands/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-694/>

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

其实想想看，回溯算法和动态规划是不是有点像呢？动态规划的三个需要明确的点就是「状态」「选择」和「base case」，正好就对应着走过的「路径」，当前的「选择列表」和「结束条件」

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

# 其他

## 零碎



## 待做

LinkedHashMap是什么

https://labuladong.gitee.io/algo/3/28/88/没看

https://labuladong.gitee.io/algo/3/28/89/没看

https://labuladong.gitee.io/algo/3/28/93/没看

https://labuladong.gitee.io/algo/3/28/94/没看

https://labuladong.gitee.io/algo/3/28/91/没看

https://labuladong.gitee.io/algo/3/28/92/没看

山谷(Valley)问题是什么（二分查找）

## 技巧



## 学习方法

