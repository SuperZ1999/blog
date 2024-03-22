---
title: "LeetCode Note 1"
date: 2022-09-23T10:21:48+08:00
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

# 链表

## 合并两个有序链表

### 解法

略

### 题目

#### 1. [合并两个有序链表](https://leetcode.cn/problems/merge-two-sorted-lists/)

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-21/>

## 单链表的分解

### 解法

从头到尾遍历一遍链表，将小于x的放到一个链表里，将大于等于x的放到一个链表里，最后再拼接这两个链表即可，注意dummy节点的使用。

### 题目

#### 1. [分隔链表](https://leetcode.cn/problems/partition-list/)

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-86/>

## 合并 k 个有序链表

### 解法

每次取出一个最小的加到链表中去，那问题就是怎么高效的获取最小的节点，这很明显用优先队列（二叉堆）就可以解决这个问题。

### 题目

#### 1. [合并K个升序链表](https://leetcode.cn/problems/merge-k-sorted-lists/)

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-23/>

## 寻找单链表的倒数第 k 个节点

### 解法

关键是找到倒数第n+1个节点，找到倒数第n个节点的做法：先让快指针走n步，然后快慢指针一起动，当快指针到头了的时候，慢指针指向的就是需要找的节点。

注意使用dummy节点可以避免特殊性，比如就5个节点，删除倒数第5个，那需要找倒数第6个节点，可是总共就5个节点，会有空指针。

### 题目

#### 1. [删除链表的倒数第 N 个结点](https://leetcode.cn/problems/remove-nth-node-from-end-of-list/)

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-19/>

## 单链表的中点

### 解法

利用快慢指针的思想，每当慢指针 `slow` 前进一步，快指针 `fast` 就前进两步，这样，当 `fast` 走到链表末尾时，`slow` 就指向了链表中点。

需要注意的是，如果链表长度为偶数，也就是说中点有两个的时候，我们这个解法返回的节点是靠后的那个节点。

### 题目

#### 1. [链表的中间结点](https://leetcode.cn/problems/middle-of-the-linked-list/)

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-876/>

## 判断链表是否包含环

### 解法

利用快慢指针的思想，如果快指针为空，说明没有环，如果快慢指针相遇说明有环

### 题目

#### 1. [环形链表](https://leetcode.cn/problems/linked-list-cycle/)

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-141/>

## 存在环的链表中寻找环起点

### 解法

利用快慢指针的思想并且稍做分析，即可得出结论：当快慢指针相遇时，让其中任一个指针指向头节点，然后让它俩以相同速度前进，再次相遇时所在的节点位置就是环开始的位置。

### 题目

#### 1. [环形链表 II](https://leetcode.cn/problems/linked-list-cycle-ii/)

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-142/>

#### 2. [寻找重复数](https://leetcode.cn/problems/find-the-duplicate-number/)

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-287/>

## 判断两个链表是否相交

### 解法

找到相交点的关键是将相交点之前的节点数凑成相等的，这样的话同时遍历，如果相等的话就是相交了。怎么凑呢？将两个链表连接一下，节点数不就想等了吗。

代码实现方面，可以考虑四种情况：

1. 长度相等，有相交
2. 长度相等，无相交
3. 长度不等，有相交
4. 长度不等，无相交

符合这四种情况的链表连接方法如下：

l1 -> null -> l2 -> null

l2 -> null -> l1 -> null

另一种做法：将某一条链表首尾相连，该问题就转换为寻找有环链表的环起点问题。

### 题目

#### 1. [相交链表](https://leetcode.cn/problems/intersection-of-two-linked-lists/)

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-160/>

## 反转单链表

### 解法

利用递归的思想，先反转head后面的，然后把head也反转即可。

### 思想

反转的过程就是改变指针方向的过程并且最后一个指向null，比如反转第2个---第5个：

1 -> 2 -> 3 -> 4 -> 5 -> null

反转后为：

1 -> 2 <- 3 <- 4 <- 5

​     null

### 题目

#### 1. [反转链表](https://leetcode.cn/problems/reverse-linked-list/)

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-206/>

## 反转链表前n个节点

### 解法

解决思路和反转整个链表差不多，只要稍加修改即可：

1、base case 变为 `n == 1`，反转一个元素，就是它本身，同时**要记录后驱节点**。

2、刚才我们直接把 `head.next` 设置为 null，因为整个链表反转后原来的 `head` 变成了整个链表的最后一个节点。但现在 `head` 节点在递归反转之后不一定是最后一个节点了，所以要记录后驱 `successor`（第 `n + 1` 个节点），反转之后将 `head` 连接上。

### 题目

无

题解详见：<https://superz1999.github.io/blog/posts/leetcode/反转链表前n个节点/>

## 反转链表节点(m, n)

### 解法

与反转链表前n个节点区别在于不是从第一个节点开始反转，而是从left开始，那么只需要利用递归一次head往后移一位，left和right分别减一的特性，把head移到left的位置，然后反转前n个节点即可。

### 题目

#### 1. [反转链表 II](https://leetcode.cn/problems/reverse-linked-list-ii/)

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-92/>

## K 个一组翻转链表

### 解法

**1、先反转以 `head` 开头的 `k` 个元素**。

**2、将第 `k + 1` 个元素作为 `head` 递归调用 `reverseKGroup` 函数**。

**3、将上述两个过程的结果连接起来**。

注意base case为最后元素不足 k 个时的情况

### 题目

#### 1. [K 个一组翻转链表](https://leetcode.cn/problems/reverse-nodes-in-k-group/)

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-25/>

## 链表的前后序遍历

```java
void traverse(ListNode head) {
    // 前序遍历代码
    traverse(head.next);
    // 后序遍历代码
}
```

## 回文串

### 寻找回文串

核心思想是从中心向两端扩展

### 判断回文串

核心思想是从两端向中间逼近

## 判断回文链表

### 解法

可以将链表全部反转，也可以部分反转

#### 链表全部反转

链表全部反转的方法共3种：

##### 将原链表反转，然后与原链表比较

略

##### 链表后序遍历

链表也可以后序遍历，这道题只需要使用后序遍历，然后提前存一下head，从两边向中间逼近就可以了。

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-234-链表后序遍历/>

##### 利用栈

同链表后序遍历

#### 链表部分反转

##### 快慢指针+反转链表

先用快慢指针找到链表的中点，从而找到回文串的后一半，然后将后一半反转，然后判断前后两部分是否相等就行了。

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-234-快慢指针+反转链表/>

### 题目

#### 1. [回文链表](https://leetcode.cn/problems/palindrome-linked-list/)

# 数组

## 快慢指针在数组中的应用

### 数组元素去重

#### 解法

慢指针指向当前已经去重的数据的最后一个，快指针去前面探路，碰到和slow不一样的数据就让这个数据放在slow后面，slow++。

具体变种详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-26+83+27+283/>

#### 题目

##### 1. [删除有序数组中的重复项](https://leetcode.cn/problems/remove-duplicates-from-sorted-array/)

##### 2. [删除排序链表中的重复元素](https://leetcode.cn/problems/remove-duplicates-from-sorted-list/)

##### 3. [移除元素](https://leetcode.cn/problems/remove-element/)

##### 4. [移动零](https://leetcode.cn/problems/move-zeroes/)

### 滑动窗口

#### 解法

`left` 指针在后，`right` 指针在前，两个指针中间的部分就是「窗口」，算法通过扩大和缩小「窗口」来解决某些问题。

详见思想章节

#### 题目

##### 1. [最小覆盖子串](https://leetcode.cn/problems/minimum-window-substring/)

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-76/>

##### 2. [字符串的排列](https://leetcode.cn/problems/permutation-in-string/)

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-567/>

##### 3. [找到字符串中所有字母异位词](https://leetcode.cn/problems/find-all-anagrams-in-a-string/)

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-438/>

##### 4. [无重复字符的最长子串](https://leetcode.cn/problems/longest-substring-without-repeating-characters/)

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-3/>

##### 5. [每种字符至少取 K 个](https://leetcode.cn/problems/take-k-of-each-character-from-left-and-right/)

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-6270/>

##### 6. [统计好子数组的数目](https://leetcode.cn/problems/count-the-number-of-good-subarrays/)

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-周赛-328/>

## 左右指针在数组中的应用

### 解法

见题解

### 题目

#### 1. [颜色分类](https://leetcode.cn/problems/sort-colors/)

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-75/>

### 二分查找

#### 解法

就是将搜索空间合理的分成两部分，摒弃不可能的那部分，缩减搜索空间，加快搜索速度，详见思想章节

#### 题目

##### 1. [在排序数组中查找元素的第一个和最后一个位置](https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/)

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-34/>

##### 2. [二分查找](https://leetcode.cn/problems/binary-search/)

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-704/>

##### 3. [搜索二维矩阵 II](https://leetcode.cn/problems/search-a-2d-matrix-ii/)

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-240/>

##### 4. [寻找两个正序数组的中位数](https://leetcode.cn/problems/median-of-two-sorted-arrays/)

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-4/>

##### 5. [搜索旋转排序数组](https://leetcode.cn/problems/search-in-rotated-sorted-array/)

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-33/>

##### 6. [正整数和负整数的最大计数](https://leetcode.cn/problems/maximum-count-of-positive-integer-and-negative-integer/)

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-周赛-327/>

##### 7. [最大化城市的最小供电站数目](https://leetcode.cn/problems/maximize-the-minimum-powered-city/)

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-双周赛-95/>

##### 8. [每个小孩最多能分到多少糖果](https://leetcode.cn/problems/maximum-candies-allocated-to-k-children/)

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-2226/>

### 两数之和

#### 解法

利用左右指针的思想，从两边向中间逼近，如果左右之和太大，那就right--，否则left++，直到左右之和等于target。

#### 题目

##### 1. [两数之和 II - 输入有序数组](https://leetcode.cn/problems/two-sum-ii-input-array-is-sorted/)

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-167/>

### 三数之和

#### 解法

先排序，然后确定一个数，剩下两个数用双指针确定，同两数之和，详见题解

#### 题目

##### 1. [三数之和](https://leetcode.cn/problems/3sum/)

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-15/>

##### 2. [最接近的三数之和](https://leetcode.cn/problems/3sum-closest/)

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-16/>

### 反转数组

#### 解法

利用左右指针的思想，从两边向中间逼近，同时交换左右的值

##### 扩展

###### 反转字符数组里的单词

先反转整个数组，然后再反转各个单词即可

###### 旋转矩阵

先按对角线对折矩阵（注意对折矩阵时，只需要遍历矩阵的一半即可，如果整个矩阵都遍历，那矩阵不会有任何变化，相当于对折了两次），再反转矩阵的每一行即可

#### 题目

##### 1. [反转字符串](https://leetcode.cn/problems/reverse-string/)

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-344/>

##### 2. [反转字符串中的单词](https://leetcode.cn/problems/reverse-words-in-a-string/)

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-151/>

##### 3. [旋转图像](https://leetcode.cn/problems/rotate-image/)

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-48/>

### 回文串判断

#### 解法

遍历一遍数组，同时从中心向两边寻找回文串，并且保存最长的即可。

#### 题目

##### 1. [最长回文子串](https://leetcode.cn/problems/longest-palindromic-substring/)

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-5/>

## 前缀和

### 一维数组中的前缀和

#### 解法

利用前缀和的思想轻松秒杀，需要注意在preSum中，第n + 1个元素存的时nums前n个元素的和，整体往后挪一位

#### 题目

##### 1. [区域和检索 - 数组不可变](https://leetcode.cn/problems/range-sum-query-immutable/)

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-303/>

##### 2. [和为 K 的子数组](https://leetcode.cn/problems/subarray-sum-equals-k/)

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-560/>

##### 3. [除自身以外数组的乘积](https://leetcode.cn/problems/product-of-array-except-self/)

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-238/>

### 二维数组中的前缀和

#### 解法

利用前缀和的思想轻松秒杀，需要注意在preSum中，第[n + 1, n+1]个元素存的是matrix前n*n个元素的和，整体往右下挪一位

还需要注意做减法时，会多减一块区域，需要加回来

#### 题目

##### 1. [二维区域和检索 - 矩阵不可变](https://leetcode.cn/problems/range-sum-query-2d-immutable/)

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-304/>

### 二叉树中的前缀和

#### 解法

我们利用先序遍历二叉树，记录下根节点 root 到当前节点 p 的路径上所有节点的前缀和，并且将该前缀和加入数据结构中，并且遍历完当前结点记得将前缀和从数据结构中去除，以免影响其他结点的前缀和

#### 题目

##### 1. [路径总和 III](https://leetcode.cn/problems/path-sum-iii/)

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-437/>

## 差分数组

### 一维差分数组

#### 解法

详见思想章节

#### 题目

##### 1. [航班预订统计](https://leetcode.cn/problems/corporate-flight-bookings/)

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-1109/>

##### 2. [拼车](https://leetcode.cn/problems/car-pooling/)

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-1094/>

### 二维差分数组

#### 解法

详见题解

#### 题目

##### 1. [子矩阵元素加 1](https://leetcode.cn/problems/increment-submatrices-by-one/)

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-周赛-328/>

## 矩阵的螺旋遍历

### 解法

**解题的核心思路是按照右、下、左、上的顺序遍历数组，并使用四个变量圈定未遍历元素的边界**：

![img](https://labuladong.gitee.io/algo/images/%e8%8a%b1%e5%bc%8f%e9%81%8d%e5%8e%86/6.png)

需要注意水平遍历需要判断upperBound<=lowerBound，垂直遍历需要判断leftBound<=rightBound

### 题目

#### 1. [螺旋矩阵](https://leetcode.cn/problems/spiral-matrix/)

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-54/>

#### 2. [螺旋矩阵 II](https://leetcode.cn/problems/spiral-matrix-ii/)

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-59/>

## 带权重的随机选择算法

### 解法

可以想象成一条线段，分成好几段，每段长度不一样，然后往上面撒石子，返回石子撒到了第几条线段上，直接把这个线段当成一个数组不现实，因为数值有可能很大，所以可以压缩一下，把每一段的长度当成一个元素，但这样寻找随机数处在哪一段还得把前面都加起来，不方便，那就压缩成一个前缀和数组，这样只需要从左往右遍历前缀和数组找第一个大于等于随机数的元素就行了，但是前缀和数组是一个有序数组，我们寻找第一个大于等于随机数的元素使用二分查找就可以快速定位，不需要从头遍历一遍

有两个需要注意的地方：

1. ”线段“和前缀和的”格子“的对应关系需要想清楚，这个画张图就明白了
2. 寻找第一个大于等于随机数的元素，需要用寻找左边界的二分查找，而不是寻找右边界的二分查找，详见思想章节二分查找注意点第10条

### 题目

#### 1. [按权重随机选择](https://leetcode.cn/problems/random-pick-with-weight/)

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-528/>

## 常数时间删除/查找数组中的任意元素

### 解法

为了随机选取元素，需要用到数组，并且得是紧凑的，但是数组增删不是O(1)的，所以再来个map，key是数组元素的值，value是数组的索引，这样就做到了O(1)的数组增删，增删的时候注意修改map和数组

核心思想就是为了随机选取元素，肯定得用**数组**存，并且得是**紧凑**的

### 题目

#### 1. [O(1) 时间插入、删除和获取随机元素](https://leetcode.cn/problems/insert-delete-getrandom-o1/)

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-380/>

#### 2. [黑名单中的随机数](https://leetcode.cn/problems/random-pick-with-blacklist/)

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-710/>

## 原地哈希

### 解法

将元素和索引一一对应，不对应的交换元素使其对应

### 题目

#### 1. [找到所有数组中消失的数字](https://leetcode.cn/problems/find-all-numbers-disappeared-in-an-array/)

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-448/>

#### 2. [寻找重复数](https://leetcode.cn/problems/find-the-duplicate-number/)

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-287/>

#### 3. [缺失的第一个正数](https://leetcode.cn/problems/first-missing-positive/)

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-41/>

# 二叉树

## 遍历问题

### 解法

利用前中后序遍历模板（见思想），用一个 traverse 函数配合外部变量来实现。

搞清楚二叉树的每一个节点需要做什么，需要在什么时候（前中后序）做。

### 题目

#### 1. [二叉树的最大深度](https://leetcode.cn/problems/maximum-depth-of-binary-tree/)

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-104/>

#### 2. [二叉树的前序遍历](https://leetcode.cn/problems/binary-tree-preorder-traversal/)

题解略

#### 3. [翻转二叉树](https://leetcode.cn/problems/invert-binary-tree/)

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-226/>

#### 4. [填充每个节点的下一个右侧节点指针](https://leetcode.cn/problems/populating-next-right-pointers-in-each-node/)

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-116/>

#### 5. [二叉树的中序遍历](https://leetcode.cn/problems/binary-tree-inorder-traversal/)

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-94/>

## 分解问题

### 解法

主要思想就是定义一个递归函数，通过子问题（子树）的答案推导出原问题的答案

首先写出这个递归函数的定义，并充分利用这个函数的返回值(这个返回值就是需要用到的子树信息)。

搞清楚二叉树的每一个节点需要做什么，需要在什么时候（前中后序）做。

### 题目

#### 1. [二叉树的最大深度](https://leetcode.cn/problems/maximum-depth-of-binary-tree/)

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-104/>

#### 2. [二叉树的直径](https://leetcode.cn/problems/diameter-of-binary-tree/)

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-543/>

#### 3. [翻转二叉树](https://leetcode.cn/problems/invert-binary-tree/)

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-226/>

#### 4. [二叉树展开为链表](https://leetcode.cn/problems/flatten-binary-tree-to-linked-list/)

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-114/>

## 层序遍历

### 解法

就是一个BFS，可以计算一些类似结点与root之间的距离的问题。详见思想里的模板

### 题目

#### 1. [填充每个节点的下一个右侧节点指针](https://leetcode.cn/problems/populating-next-right-pointers-in-each-node/)

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-116/>

## 构造二叉树

### 解法

二叉树的构造问题一般都是使用「分解问题」的思想：构造整棵树 = 根节点 + 构造左子树 + 构造右子树。

### 题目

#### 1. [最大二叉树](https://leetcode.cn/problems/maximum-binary-tree/)

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-654/>

#### 2. [从前序和中序遍历序列构造二叉树](https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-105/>

#### 3. [从后序和中序遍历序列构造二叉树](https://leetcode.cn/problems/construct-binary-tree-from-inorder-and-postorder-traversal/)

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-106/>

#### 4. [根据前序和后序遍历构造二叉树](https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-postorder-traversal/)

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-889/>

## 二叉搜索树性质

### 解法

只需要利用二叉树左边子树全部小于根节点，右边全部大于根节点，中序遍历就是升序序列就可以了

### 题目

#### 1. [二叉搜索树中第 K 小的元素](https://leetcode.cn/problems/kth-smallest-element-in-a-bst/)

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-230/>

#### 2. [把二叉搜索树转换为累加树](https://leetcode.cn/problems/convert-bst-to-greater-tree/)

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-538/>

## 二叉搜索树合法性

### 解法

利用二叉树的分解思想，将原问题分解为：root左边的的结点都比root小右边的的结点都比root大+左子树是BST+右子树是BST，问题在于root只能获得左右孩子的值，从而判断是都大于小于root，想要让整个子树都小于或大于自己，需要将min和max传下去

### 题目

#### 1. [验证二叉搜索树](https://leetcode.cn/problems/validate-binary-search-tree/)

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-98/>

## 二叉搜索树增删改查

### 解法

见思想

### 题目

#### 1. [二叉搜索树中的搜索](https://leetcode.cn/problems/search-in-a-binary-search-tree/)

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-700/>

#### 2. [二叉搜索树中的插入操作](https://leetcode.cn/problems/insert-into-a-binary-search-tree/)

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-701/>

#### 3. [删除二叉搜索树中的节点](https://leetcode.cn/problems/delete-node-in-a-bst/)

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-504/>

## n个结点的BST的种类

### 解法

#### 递归思路

递归函数定义为n个结点可以组成几种BST，那么对于n个结点的BST的种类=将n个结点逐个当成root，左右子树的种类相乘，再把这些结果相加就是n个结点BST的种类

#### 动态规划

递归明显有重复计算的问题，我们可以对已经计算好的数据进行存储，需要时就不需要重新计算了，这种重复利用子问题的解的方式就是动态规划

### 题目

#### 1. [不同的二叉搜索树](https://leetcode.cn/problems/unique-binary-search-trees/)

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-96/>

#### 2. [不同的二叉搜索树 II](https://leetcode.cn/problems/unique-binary-search-trees-ii/)

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-95/>

## 扁平化嵌套列表迭代器

### 解法

#### 思路一

将NestedInteger当成树的节点，list当成该节点的孩子，那么只需要遍历该树就可以完成迭代了，直接看代码

#### 思路二

思路一会在构造的时候将此树遍历一遍，所以速度会很慢，最好弄成懒惰式的，所以可以把NestedInteger当成一个队列，循环把第一个元素展开，直到第一个元素为数字为止，这样就可以完成迭代

### 题目

#### 1. [扁平化嵌套列表迭代器](https://leetcode.cn/problems/flatten-nested-list-iterator/)

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-341/>

## 最近公共祖先

### 解法

主要思想就是遍历二叉树，同时查找左子树和右子树是否分别含有一个节点，如果是，那么这个结点就是LCA

### 题目

#### 1. [二叉树的最近公共祖先](https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/)

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-236/>

#### 2. [二叉搜索树的最近公共祖先](https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-search-tree/)

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-235/>

## 最近公共祖先

### 解法

主要思想就是遍历二叉树，同时查找左子树和右子树是否分别含有一个节点，如果是，那么这个结点就是LCA

### 题目

#### 1. [二叉树的最近公共祖先](https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/)

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-236/>

#### 2. [二叉搜索树的最近公共祖先](https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-search-tree/)

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-235/>

## 完全二叉树的结点个数

### 解法

普通二叉树需要对二叉树进行遍历才能统计结点个数，满二叉树只需要知道树的高度就可以计算出来，那么完全二叉树可以结合这两个的做法，如果左边和右边高度相同，就用满二叉树的计算方式，如果不同那就遍历二叉树，同时判断该节点为root的树是不是满二叉树

这种做法时间复杂度是O(logn*logn)，详见：<https://labuladong.gitee.io/algo/2/21/48/>

### 题目

#### 1. [完全二叉树的节点个数](https://leetcode.cn/problems/count-complete-tree-nodes/)

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-222/>

## 合并二叉树

### 解法

详见题解

### 题目

#### 1. [合并二叉树](https://leetcode.cn/problems/merge-two-binary-trees/)

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-617/>

# 图

## 图的遍历

### 解法

直接套模板，详见思想章节

### 题目

#### 1. [所有可能的路径](https://leetcode.cn/problems/all-paths-from-source-to-target/)

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-797/>

## 环检测

### 解法

#### 思路一

利用图的DFS，首先构建图，把prerequisites当成图的边，然后利用图的DFS遍历模板遍历该图，同时记录路径里的结点，如果路径里的结点重复就是有环，记录结果并返回

#### 思路二

利用图的BFS，首先构建图，把prerequisites当成图的边，注意BFS时，只能让入度为零的结点入队列，出队相当于访问该节点，环里的结点不会入队列，最后判断访问过的结点个数是否等于总结点个数即可

### 题目

#### 1. [课程表](https://leetcode.cn/problems/course-schedule/)

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-207/>

## 拓扑排序

### 解法

#### 思路一

利用图的DFS，只要是无环的有向图，就有拓扑排序，所以需要像207题一样判断是否有环，如果无环，那么只需要反转该图的后序遍历序列就得到了该图的拓扑排序

#### 思路二

利用图的BFS，只不过只把入度为零的结点加入队列，出队相当于访问该节点，队列出队的序列就是该图的拓扑排序

### 题目

#### 1. [课程表 II](https://leetcode.cn/problems/course-schedule-ii/)

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-210/>

## 二分图的判断

### 解法

利用二分图判断模板即可，有dfs和bfs两种做法，详见思想章节

### 题目

#### 1. [判断二分图](https://leetcode.cn/problems/is-graph-bipartite/)

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-785/>

#### 2. [可能的二分法](https://leetcode.cn/problems/possible-bipartition/)

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-886/>

## 并查集

### 解法

利用并查集模板即可，详见思想章节

### 题目

#### 1. [被围绕的区域](https://leetcode.cn/problems/surrounded-regions/)

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-130/>

#### 2. [等式方程的可满足性](https://leetcode.cn/problems/satisfiability-of-equality-equations/)

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-990/>

#### 3. [寻找图中是否存在路径](https://leetcode.cn/problems/find-if-path-exists-in-graph/)

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-1971/>

#### 4. [除法求值](https://leetcode.cn/problems/evaluate-division/)

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-399/>

## dijkstra问题

### 解法

利用dijkstra模板即可，注意dijkstra的变种需要修改adj和weight函数，详见思想章节

### 题目

#### 1. [网络延迟时间](https://leetcode.cn/problems/network-delay-time/)

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-743/>

#### 2. [最小体力消耗路径](https://leetcode.cn/problems/path-with-minimum-effort/)

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-1631/>

#### 3. [概率最大的路径](https://leetcode.cn/problems/path-with-maximum-probability/)

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-1514/>

## kruskal问题

### 解法

利用kruskal算法即可，详见思想章节

### 题目

#### 1. [连接所有点的最小费用](https://leetcode.cn/problems/min-cost-to-connect-all-points/)

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-1584/>

## prim问题

### 解法

利用prim算法即可，详见思想章节

### 题目

#### 1. [连接所有点的最小费用](https://leetcode.cn/problems/min-cost-to-connect-all-points/)

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-1584/>

# 设计数据结构

## LRU

### 解法

直接套LRU模板即可，详见思想篇章

### 题目

#### 1. [LRU 缓存](https://leetcode.cn/problems/lru-cache/)

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-146/>

## LFU

### 解法

直接套LFU模板即可，详见思想篇章

### 题目

#### 1. [LFU 缓存](https://leetcode.cn/problems/lfu-cache/)

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-460/>

## TrieMap和TrieSet

### 解法

直接套模板即可，详见思想篇章

### 题目

#### 1. [实现 Trie (前缀树)](https://leetcode.cn/problems/implement-trie-prefix-tree/)

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-208/>

#### 2. [单词替换](https://leetcode.cn/problems/replace-words/)

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-648/>

#### 3. [添加与搜索单词 - 数据结构设计](https://leetcode.cn/problems/design-add-and-search-words-data-structure/)

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-211/>

#### 4. [键值映射](https://leetcode.cn/problems/map-sum-pairs/)

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-677/>

## 数据流的中位数

### 解法

用两个优先队列（最大/小堆），等量的将数据流分成两部分，最大堆放小的那一部分，最小堆放大的那一部分，中位数就是堆顶的元素平均数，详见：<https://mp.weixin.qq.com/s/oklQN_xjYy--_fbFkd9wMg>

### 题目

#### 1. [数据流的中位数](https://leetcode.cn/problems/find-median-from-data-stream/)

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-295/>

## 单调栈问题

### 下一个更大元素

#### 解法

利用单调栈的思想即可，倒着入栈，碰到栈顶比自己小就出栈直到比自己大，那么这么就把两个较大元素中间的小元素去除掉了，剩下的两个元素就可以充当下一个更大元素的角色（中间去除的元素是无法充当这种角色的），那么此时栈顶就是当前元素下一个更大元素

#### 题目

##### 1. [下一个更大元素 I](https://leetcode.cn/problems/next-greater-element-i/)

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-496/>

##### 2. [每日温度](https://leetcode.cn/problems/daily-temperatures/)

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-739/>

##### 3. [下一个更大元素 II](https://leetcode.cn/problems/next-greater-element-ii/)

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-503/>

##### 4. [接雨水](https://leetcode.cn/problems/trapping-rain-water/)

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-42/>

## 单调队列问题

### 滑动窗口最大值

#### 解法

利用单调队列的思想即可，保持队列中为单调递减那么队头就是最大值，入栈时把小于两头的元素全部出队（因为这些元素不可能充当窗口内最大值的角色），详见思想篇章

#### 题目

##### 1. [滑动窗口最大值](https://leetcode.cn/problems/sliding-window-maximum/)

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-239/>

## 用栈实现队列

### 解法

直接套栈实现队列模板即可，详见思想篇章

### 题目

#### 1. [用栈实现队列](https://leetcode.cn/problems/implement-queue-using-stacks/)

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-232/>

## 用队列实现栈

### 解法

直接套用队列实现栈的模板即可，详见思想篇章

### 题目

#### 1. [用队列实现栈](https://leetcode.cn/problems/implement-stack-using-queues/)

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-225/>

## 最小栈

### 解法

这道题的关键是getMin的实现，可以用一个辅助栈来存储每个元素入栈时的最小值，这样的话当元素出栈时也可以很容易的获取最小值

### 题目

#### 1. [最小栈](https://leetcode.cn/problems/min-stack/)

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-155/>

# 排序

## 快速选择

### 解法

详见题解

### 题目

#### 1. [数组中的第K个最大元素](https://leetcode.cn/problems/kth-largest-element-in-an-array/solutions/)

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-215/>

#### 2. [前 K 个高频元素](https://leetcode.cn/problems/top-k-frequent-elements/)

题解详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-347/>

# 思想

## 双指针

就是两个指针，分为左右指针和快慢指针，只要数组有序，就应该想到双指针技巧

### 左右指针

两个指针一个左一个右

使用时一定要确定什么时候动左指针，什么时候动右指针，对于已排序的数组一般是相加的和，小了动左指针，大了动右指针

#### 二分查找

就是将搜索空间合理的分成两部分，摒弃不可能的那部分，缩减搜索空间，加快搜索速度

##### 经典思路

```java
public int search(int[] nums, int target) {
    int left = 0, right = nums.length - 1;

    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (nums[mid] == target) {
            return mid;
        } else if (nums[mid] > target) {
            right = mid -1;
        } else if (nums[mid] < target) {
            left = mid + 1;
        }
    }

    return -1;
}
```

这种就是一边缩减搜索空间，一边寻找要找的元素。

但是有时候问题并不是这么简单，比如寻找一个可能在数组里不存在，或者是找边界这样的问题，这时使用进阶思路 ，在循环体内排除一定不存在目标元素的区间会更简单一些。

经典思路是寻找元素

进阶思路是排除n-1个不可能的元素

##### 进阶思路

```java
class Solution {
    public int search(int[] nums, int target) {
        // 此思路搜索空间为[left, right]，闭闭空间
        int left = 0, right = nums.length - 1;

        // 循环条件写成left<right，因为循环体内把数组分成两部分，那么一定会达到left和right重合的状态
        // 所以循环条件写成left<right，可以保证退出循环时left等于right
        while (left < right) {
            // 求中点，left=mid+1时不需要向上取整
            int mid = left + (right - left) / 2;
            // left=mid时需要向上取整，记忆方式：left和mid要有一个+1
            // 这么做的原因是：向下取整时，如果还剩下两个元素，刚好又走到left=mid这个分支，就死循环了，因为此时mid就等于left
            //int mid = left + (right - left + 1) / 2;
            // 下面是核心逻辑，分成两个区间是因为这样扩展性更强
            // 这块主要就是筛选不可能的区间，然后缩减搜索空间，具体问题具体分析，注意left没加一时mid要加一
            // 左边界，记忆方式：左边界是小于等于，下面的语句是...=mid，第二个语句和第一个语句互补，left没加一时mid要加一
            /*if (target <= nums[mid]) {
                right = mid;
            } else {
                left = mid + 1;
            }*/
            // 右边界
            /*if (target >= nums[mid]) {
                left = mid;
            } else {
                right = mid -1;
            }*/
        }

        // 此时left一定等于right，所以返回left或者right都一样
        // 排除了n-1个不可能的元素，还剩下[left, right]区间的元素，而left=right，就看剩下这个是不是要寻找的元素了
        // 如果该题一定存在指定的元素，那么下一步可以省略，直接return left就好了
        /* 如果查找与target相等的值 */
        if (nums[left] == target) {
            return -1;
        }
        /* 如果查找target的左侧边界 */
        if (nums[left] < target) {
            return -1;
        }
        /* 如果查找target的右侧边界 */
        if (nums[left] > target) {
            return -1;
        }

        return left;
    }
}
```

###### 步骤

1. left和right分别设置为搜索空间的左右端点，注意是闭区间
2. 循环条件写成left<right
3. 求中点，先写成`int mid = left + (right - left) / 2;`
4. 根据具体问题将搜索空间分成两部分，其中一部分必须是不可能的区域，然后根据这个不可能区域的特征写出第一个if，然后else里写和if互补的区域就好了，注意如果结果是left=mid，上面求中点要改成`int mid = left + (right - left + 1) / 2;`
5. 如果根据题意不能判断出一定存在寻找的元素，需要判断下`nums[left]`是不是寻找的元素，是则`return left`，否则未找到该元素；如果根据题意能判断出一定存在寻找的元素，那直接`return left`就好了

###### 注意点

1. 可以把这里的nums[i] = x看成一个函数，只要是具有单调性的函数都可以使用二分查找，比如y = func(x)，给定一个y让你找对应的x也可以用二分查找，二分查找的使用很广泛，只要函数有单调性即可
2. 此思路搜索空间为[left, right]，闭闭空间
3. 循环条件写成left<right，因为循环体内把数组分成两部分，并且根据left的取值选择mid是向上或向下取整，那么一定会达到left和right重合的状态（把所有情况都模拟一边就可以得出这个结论），所以循环条件写成left<right，可以保证退出循环时left等于right
4. 求中点时，如果使用`(left + right) / 2`有可能相加溢出，为了防止溢出使用`left + (right - left) / 2`
5. 求中点时，left=mid+1时不需要向下取整，left=mid时需要向上取整，记忆方式：left和mid要有一个+1。这么做的原因是：向下取整时，如果还剩下两个元素，刚好又走到left=mid这个分支，就死循环了，因为此时mid就等于left。right=mid时需要向下取整，原因同理
6. 把搜索空间分成两个区间是因为这样扩展性更强
7. 缩减搜索空间时，将搜索空间分成两部分需要注意分出不可能的区间，然后缩减搜索空间，具体问题具体分析，根据这个不可能区间的特征写出第一个if，然后else里写和if互补的区域
8. 注意left没加一时mid要加一
9. 退出循环后left和right相等，并且是唯一有希望的元素（只是有希望，有可能不是它，还要再判断一下，如果该题一定存在指定的元素，那么直接`return left`就好了）
10. 对于寻找左右侧边界的二分查找，在缩减搜索空间时一定要考虑>=或<=的情况，因为这样才能使用找左或右侧这个性质，比如`target <= nums[mid]`，可以寻找左边界，因为这时左边界不可能在mid右边所以直接`right=mid`就可以找到左边界，右边界同理。为什么找到的是左边界，因为此时，`nums[mid]`要么大于`target`，要么等于`target`，不管那种情况，左边界一定在`mid`处或`mid`左边，也可以这么理解：`target <= nums[mid]`->`right=mid`，所以`target > nums[mid]`->`left=mid + 1`，此时left左边全部都小于target，因为退出循环时如果能找到target，left指向的就是target，又因为left左边全部都小于target，所以此时left指向左边界。找右边界同理。
11. 对于寻找左侧边界的二分查找，说是寻找该元素的左侧边界，实际上是寻找大于等于target的所有元素的左侧边界，同理，寻找右侧边界的二分查找实际上是寻找小于等于target的所有元素的右侧边界，也可以理解成左侧边界的左边都小于target右边都大于等于target，右侧边界的右边都大于target左边都小于等于target，并且左右边界不一定等于target，所以如果target不存在时，左边界是比target大的第一个元素，右边界是比target小的第一个元素

详见：leetcode笔记word版和<https://leetcode.cn/leetbook/read/learning-algorithms-with-leetcode/xs41qg/>

#### 其他

见上面各知识点章节

### 快慢指针

两个指针一个快一个慢

#### 滑动窗口

`left` 指针在后，`right` 指针在前，两个指针中间的部分就是「窗口」，算法通过扩大和缩小「窗口」来解决某些问题。

##### 模板

```java
/* 滑动窗口算法模板 */
void slidingWindow(String s) {
       Map<Character, Integer> window = new HashMap<>();

    int left = 0, right = 0;
    // 这里用<而不用<=不是说明使用的闭闭区间，而是right当前位置的元素是我们下一个要入窗口的元素，所以这里其实是闭开窗口
    while (right < s.length()) {
        // 获取移入窗口的元素，并扩大窗口
        char c = s.charAt(right);
        right++;
        // 进行扩大窗口时数据的一系列更新
        ...

        // debug位置
        // System.out.println("left:" + left + "\t" + "right:" + right);

        // 判断左侧窗口是否要收缩
        while (window needs shrink) {
            // 获取移出窗口的元素，并收缩窗口
            char d = s.charAt(left);
            left++;
            // 进行收缩窗口时数据的一系列更新，一般与上面扩大窗口时数据更新相反
            ...
        }
    }
}
```

##### 步骤

1. 设置存储窗口内元素的数据结构，并且设置循环`while (right < s.length())`
2. 扩大窗口，并更新相关的数据
3. 判断是否需要收缩窗口，如需要，则收缩窗口，并更新相关的数据
4. 退出循环后，返回相应的数据

##### 注意点

1. 此模板采用闭开区间，循环条件用<而不用<=是因为right当前位置的元素是我们下一个要入窗口的元素
2. 收缩窗口和扩大窗口对数据的更新一般是相反的（更新顺序和加减等都是相反的）

详见：<https://labuladong.gitee.io/algo/2/20/27/>

##### 进阶

==RABIN KARP 字符匹配算法==，详见：<https://labuladong.gitee.io/algo/2/20/28/>

#### 其他

见上面各知识点章节

## 递归

一个问题 = 规模更小的同类问题 + 扩展成该问题要解决的问题

这种情况就可以用递归，递归的关键是不要跳进递归，而是明确递归函数的定义

递归由两部分组成：递归出口和递归公式

注意递归需要递归出口（也就是base case）

值得一提的是，递归操作链表并不高效。和迭代解法相比，虽然时间复杂度都是 O(N)，但是迭代解法的空间复杂度是 O(1)，而递归解法需要堆栈，空间复杂度是 O(N)。

## 前缀和与差分

前缀和数组的差分是原数组，差分数组的前缀和是原数组，两者互逆。

### 前缀和

对于一个数组，求此数组[left, right]区域内的和时，不需要从left--right逐个相加，直接right+1前的和减去left前的和即可，要想使用这种方式就得有一个前缀和数组，用来存该数组前k个的和。注意也可能是二维数组，稍作修改即可。

**主要适用的场景是原始数组不会被修改的情况下，频繁查询某个区间的累加和**。

详见：<https://labuladong.gitee.io/algo/2/20/24/>

#### 标准模板

```JAVA
class NumArray {
    int[] preSum;

    public NumArray(int[] nums) {
        preSum = new int[nums.length + 1];

        for (int i = 1; i < preSum.length; i++) {
            preSum[i] = preSum[i - 1] + nums[i - 1];
        }
    }

    public int sumRange(int left, int right) {
        return preSum[right + 1] - preSum[left];
    }
}
```

二维前缀和，详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-304/>

### 差分数组

**差分数组的主要适用场景是频繁对原始数组的某个区间的元素进行增减**

类似前缀和构造的 `preSum` 数组，我们先对 `nums` 数组构造一个 `diff` 差分数组，**`diff[i]` 就是 `nums[i]` 和 `nums[i-1]` 之差**，通过这个 `diff` 差分数组是可以反推出原始数组 `nums` 的，理解：diff[0]就是原数组的第一个元素，其他元素就是比前一个元素高多少

**这样构造差分数组 `diff`，就可以快速进行区间增减的操作**，如果你想对区间 `nums[i..j]` 的元素全部加 3，那么只需要让 `diff[i] += 3`，然后再让 `diff[j+1] -= 3` 即可

**原理很简单，回想 `diff` 数组反推 `nums` 数组的过程，`diff[i] += 3` 意味着给 `nums[i..]` 所有的元素都加了 3，然后 `diff[j+1] -= 3` 又意味着对于 `nums[j+1..]` 所有元素再减 3，那综合起来，就是对 `nums[i..j]` 中的所有元素都加 3 了**

详见：<https://labuladong.gitee.io/algo/2/20/25/>

#### 标准模板

```java
class Difference {
    private int[] diff;

    public Difference(int[] nums) {
        assert nums.length > 0;
        diff = new int[nums.length];

        diff[0] = nums[0];
        for (int i = 1; i < nums.length; i++) {
            diff[i] = nums[i] - nums[i-1];
        }
    }

    public void increment(int i, int j, int val) {
        diff[i] += val;
        // 注意这里j有可能是最后一个元素，此时的意思就是i后面的元素全部加val，所以不需要减val了
        if (j + 1 < diff.length) {
            diff[j + 1] -= val;
        }
    }

    public int[] result() {
        int[] res = new int[diff.length];
        res[0] = diff[0];

        for (int i = 1; i < diff.length; i++) {
            res[i] = res[i - 1] + diff[i];
        }
        return res;
    }
}
```

二维差分数组，详见：<https://superz1999.github.io/blog/posts/leetcode/leetcode-周赛-328/>

## 二叉树

### 前中后序理解

前中后序是遍历二叉树过程中处理每一个节点的三个特殊时间点：

前序位置的代码在刚刚进入一个二叉树节点的时候执行；

后序位置的代码在将要离开一个二叉树节点的时候执行；

中序位置的代码在一个二叉树节点左子树都遍历完，即将开始遍历右子树的时候执行。

![img](https://labuladong.gitee.io/algo/images/%e4%ba%8c%e5%8f%89%e6%a0%91%e6%94%b6%e5%ae%98/2.jpeg)

比如快速排序就是个二叉树的前序遍历，归并排序就是个二叉树的后序遍历

### 遍历模板

```java
void traverse(TreeNode root) {
    if (root == null) {
        return;
    }
    // 前序位置
    traverse(root.left);
    // 中序位置
    traverse(root.right);
    // 后序位置
}
```

多叉树的遍历模板：

```java
/* 多叉树遍历框架 */
void traverse(TreeNode root) {
    if (root == null) return;
    // 前序位置
    for (TreeNode child : root.children) {
        traverse(child);
    }
    // 后序位置
}
```

### 做题思路

有两种思路，分别是**分解问题**和**遍历二叉树**

遇到一道二叉树的题目时的通用思考过程是：

1、是否可以通过遍历一遍二叉树得到答案？如果可以，用一个 traverse 函数配合外部变量来实现。

2、是否可以定义一个递归函数，通过子问题（子树）的答案推导出原问题的答案？如果可以，写出这个递归函数的定义，并充分利用这个函数的返回值(这个返回值就是需要用到的子树信息)，这样的话递归函数就会一直分解这个问题，直到该问题不能再分解，所以我们还需要考虑base case(递归出口)。

3、无论使用哪一种思维模式，你都要明白二叉树的每一个节点需要做什么，需要在什么时候（前中后序）做。

### 后序位置的特殊之处

因为前序位置的代码执行是自顶向下的，而后序位置的代码执行是自底向上的，所以：

前序位置的代码只能从函数参数中获取父节点传递来的数据，而后序位置的代码不仅可以获取参数数据，还可以获取到子树通过函数返回值传递回来的数据。一旦你发现题目和子树有关，那大概率要给函数设置合理的定义和返回值，在后序位置写代码了。

### 层序遍历

就是一个BFS，可以计算一些类似结点与root之间的距离的问题。

#### 模板

```java
// 输入一棵二叉树的根节点，层序遍历这棵二叉树
void levelTraverse(TreeNode root) {
    if (root == null) return;
    Queue<TreeNode> q = new LinkedList<>();
    q.offer(root);

    // 从上到下遍历二叉树的每一层
    while (!q.isEmpty()) {
        int sz = q.size();
        // 从左到右遍历每一层的每个节点
        for (int i = 0; i < sz; i++) {
            TreeNode cur = q.poll();
            // 将下一层节点放入队列
            if (cur.left != null) {            // 注意不要把null放队列里面
                q.offer(cur.left);
            }
            if (cur.right != null) {        // 注意不要把null放队列里面
                q.offer(cur.right);
            }
        }
    }
}
```

### 注意点

前序中序，后序中序可以唯一确定一颗二叉树，或者带空指针的任意一个遍历序列都可以唯一确定一棵二叉树

前序后序不能唯一确定一颗二叉树，因为：

当节点左右子树都存在时，可以确定左右子树，但是当其中一个为空时，无法确定不为空的子树是左子树还是右子树

### 二叉搜索树

#### 性质

二叉树左边子树全部小于根节点，右边全部大于根节点，中序遍历就是升序序列，并且中序遍历到一个结点时，比该结点小的结点全部都遍历过了，这个性质可以用于二叉搜索树的累加上，二叉搜索树最左边是最小的结点，最右边是最大的结点

#### 合法性

利用二叉树的分解思想，将原问题分解为：root左边的的结点都比root小右边的的结点都比root大+左子树是BST+右子树是BST，问题在于root只能获得左右孩子的值，从而判断是都大于小于root，想要让整个子树都小于或大于自己，需要将min和max传下去，如果当前节点会对下面的子节点有整体影响，可以通过辅助函数增长参数列表，借助参数传递信息。

#### 增删改查

在二叉树递归框架之上，扩展出一套 BST 代码框架：

```java
void BST(TreeNode root, int target) {
    if (root.val == target)
        // 找到目标，做点什么
    if (root.val < target) 
        BST(root.right, target);
    if (root.val > target)
        BST(root.left, target);
}
```

根据代码框架掌握了 BST 的增删查改操作。

## 图

### 存储方式

#### 邻接表

优点：省空间

```java
// 邻接表
// graph[x] 存储 x 的所有邻居节点以及对应的权重
List<int[]>[] graph;
```

#### 邻接矩阵

优点：可以随机访问

```java
// 邻接矩阵
// matrix[x][y] 记录 x 指向 y 的边的权重，0 表示不相邻
int[][] matrix;
```

### 遍历模板

#### DFS

和多叉树类似，只不过需要记录访问过的结点

```java
// 记录被遍历过的节点
boolean[] visited;
// 记录从起点到当前节点的路径
boolean[] onPath;

/* 图遍历框架 */
void traverse(Graph graph, int s) {
    if (visited[s]) return;
    // 进入结点时
    // 经过节点 s，标记为已遍历
    visited[s] = true;
    // 做选择：标记节点 s 在路径上
    onPath[s] = true;
    for (int neighbor : graph.neighbors(s)) {
        traverse(graph, neighbor);
    }
    // 离开结点时
    // 撤销选择：节点 s 离开路径
    onPath[s] = false;
}
```

#### BFS

```java
// 记录被遍历过的节点
boolean[] visited;

void traverse(Graph graph, int s) {
    Queue<Integer> queue = new ArrayDeque<>();
    queue.offer(s);
    while (!queue.isEmpty()) {
        int node = queue.poll();
        visited[node] = true;
        for (int neighbor : graph.neighbors(s)) {
            if (!visited[neighbor]) {
                queue.offer(next);
            }
        }
    }
}
```

### 图的拓扑排序

#### 拓扑排序

直观地说就是，让你把一幅图「拉平」，而且这个「拉平」的图里面，所有箭头方向都是一致的

如果一个图里存在环，是无法进行拓扑排序的，反之，如果图里没有环那么一定可以拓扑排序

注意有向无环图不一定是树

#### 如何拓扑排序

1. 将后序遍历的结果进行反转，就是拓扑排序的结果。至于原因由于需要严格的数学证明，就不用看了，可以自己画个图看一看
2. 利用图的BFS，每次只让入度为零的结点入队列，此时遍历的结果就是拓扑排序的结果

### 二分图

![img](https://labuladong.gitee.io/algo/images/%e4%ba%8c%e5%88%86%e5%9b%be/0.png)

如图所示就是二分图，可以使用染色法判断一个图是否为二分图，如下所示：

![img](https://labuladong.gitee.io/algo/images/algo4/1.jpg)

在某些场景下二分图也可以作为存储键值对的数据结构（符号表）

#### 判断二分图（染色）模板

其实就是图的遍历，只不过一边遍历一边染色

##### DFS

```java
/* 判断二分图框架(DFS) */
private boolean[] color;
private boolean[] visited;
void traverse(Graph graph, int v) {
    visited[v] = true;
    // 遍历节点 v 的所有相邻节点 neighbor
    for (int neighbor : graph.neighbors(v)) {
        if (!visited[neighbor]) {
            // 相邻节点 neighbor 没有被访问过
            // 那么应该给节点 neighbor 涂上和节点 v 不同的颜色
            color[neighbor] = !color[v];
            traverse(graph, neighbor);
        } else {
            // 相邻节点 neighbor 已经被访问过
            // 那么应该比较节点 neighbor 和节点 v 的颜色
            // 若相同，则此图不是二分图
        }
    }
}
```

##### BFS

```java
/* 判断二分图框架(BFS) */
private boolean[] color;
private boolean[] visited;
void traverse(Graph graph, int start) {
    Deque<Integer> queue = new ArrayDeque<>();
    visited[start] = true;
    queue.offer(start);
    while (!queue.isEmpty()) {
        int v = queue.poll();
        // 从节点 v 向所有相邻节点扩散
        for (int w : graph[v]) {
            if (!visited[w]) {
                // 相邻节点 w 没有被访问过
                // 那么应该给节点 w 涂上和节点 v 不同的颜色
                color[w] = !color[v];
                // 标记 w 节点，并放入队列
                visited[w] = true;
                queue.offer(w);
            } else {
                // 相邻节点 w 已经被访问过
                // 根据 v 和 w 的颜色判断是否是二分图
                if (color[w] == color[v]) {
                    // 若相同，则此图不是二分图
                    return;
                }
            }
        }
    }
}
```

### 并查集

就是可以1、方便的合并两个集合，2、快速的判断两个结点是否处于一个集合中的树状数据结构，长下面这个样子

![img](https://labuladong.gitee.io/algo/images/unionfind/4.jpg)

#### 模板

```java
class UF {
    // 连通分量个数
    private int count;
    // 存储每个节点的父节点
    private int[] parent;

    // n 为图中节点的个数
    public UF(int n) {
        this.count = n;
        parent = new int[n];
        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }
    }

    // 将节点 p 和节点 q 连通
    public void union(int p, int q) {
        int rootP = find(p);
        int rootQ = find(q);

        if (rootP == rootQ)
            return;

        parent[rootQ] = rootP;
        // 两个连通分量合并成一个连通分量
        count--;
    }

    // 判断节点 p 和节点 q 是否连通
    public boolean connected(int p, int q) {
        int rootP = find(p);
        int rootQ = find(q);
        return rootP == rootQ;
    }

    public int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }

    // 返回图中的连通分量个数
    public int count() {
        return count;
    }
}
```

这里做了路径压缩的优化，在 `find` 函数中进行路径压缩，保证任意树的高度保持在常数，使得各个 API 时间复杂度为 O(1)。使用了路径压缩之后，可以不使用 `size` 数组的平衡优化。

### dijkstra问题

dijkstra是求最短路径的算法，实际上是由图的BFS演化而来，模板如下：

```java
class State {
    // 图节点的 id
    int id;
    // 从 start 节点到当前节点的距离
    int distFromStart;

    State(int id, int distFromStart) {
        this.id = id;
        this.distFromStart = distFromStart;
    }
}

// 返回节点 from 到节点 to 之间的边的权重
int weight(int from, int to);

// 输入节点 s 返回 s 的相邻节点
List<Integer> adj(int s);

// 输入一幅图和一个起点 start，计算 start 到其他节点的最短距离
int[] dijkstra(int start, List<Integer>[] graph) {
    // 图中节点的个数
    int V = graph.length;
    // 记录最短路径的权重，你可以理解为 dp table
    // 定义：distTo[i] 的值就是节点 start 到达节点 i 的最短路径权重
    int[] distTo = new int[V];
    // 求最小值，所以 dp table 初始化为正无穷
    Arrays.fill(distTo, Integer.MAX_VALUE);
    // base case，start 到 start 的最短距离就是 0
    distTo[start] = 0;

    // 优先级队列，distFromStart 较小的排在前面
    Queue<State> pq = new PriorityQueue<>((a, b) -> {
        return a.distFromStart - b.distFromStart;
    });

    // 从起点 start 开始进行 BFS
    pq.offer(new State(start, 0));

    while (!pq.isEmpty()) {
        State curState = pq.poll();
        int curNodeID = curState.id;
        int curDistFromStart = curState.distFromStart;

        // 如果只需要start到end的最短距离加上这句就可以了
        // if (curNodeID == end) {
            // return curDistFromStart;
        // }

        if (curDistFromStart > distTo[curNodeID]) {
            // 已经有一条更短的路径到达 curNode 节点了
            continue;
        }
        // 将 curNode 的相邻节点装入队列
        for (int nextNodeID : adj(curNodeID)) {
            // 看看从 curNode 达到 nextNode 的距离是否会更短
            int distToNextNode = distTo[curNodeID] + weight(curNodeID, nextNodeID);
            if (distTo[nextNodeID] > distToNextNode) {
                // 更新 dp table
                distTo[nextNodeID] = distToNextNode;
                // 将这个节点以及距离放入队列
                pq.offer(new State(nextNodeID, distToNextNode));
            }
        }
    }
    return distTo;
}
```

解释：同一个结点可能会入队多个State，一定会先遍历到dist较小的那个，结点的第一次遍历，就确定了这个结点的最短距离，然后按照这个最短距离刷新start到其他节点的距离，之后这个结点的任务就算是结束了，以后再碰到这个结点直接continue就可以了。

注意dijkstra的变种需要修改adj和weight函数

### kruskal问题

用于求解最小生成树问题，主要思路就是先把边按权重排序，从小到大添加边，同时判断边添加后是否有环（这一步可以用并查集做），模板如下：

```java
int minimumCost(int n, int[][] edges) {
    UF uf = new UF(n);
    // 对所有边按照权重从小到大排序
    Arrays.sort(edges, (a, b) -> (a[2] - b[2]));
    // 记录最小生成树的权重之和
    int mst = 0;
    for (int[] edge : edges) {
        int u = edge[0];
        int v = edge[1];
        int weight = edge[2];
        // 若这条边会产生环，则不能加入 mst
        if (uf.connected(u, v)) {
            continue;
        }
        // 若这条边不会产生环，则属于最小生成树
        mst += weight;
        uf.union(u, v);
    }
    // 保证所有节点都被连通
    // uf.count() == 1 说明所有节点被连通
    return uf.count() == 1 ? mst : -1;
}

class UF {
    // 见上文并查集模板
}
```

详见：<https://mp.weixin.qq.com/s/dJ9gqR3RVoeGnATlpMG39w>

### prim问题

用于求解最小生成树问题，原理就是横切边中最小的一定是最小生成树的一条边，可以每次添加一个结点找横切边（这样比较方便），然后把最小生成树的边都找到就可以了，模板如下：

```java
class Prim {
    // 核心数据结构，存储「横切边」的优先级队列
    private PriorityQueue<int[]> pq;
    // 类似 visited 数组的作用，记录哪些节点已经成为最小生成树的一部分
    private boolean[] inMST;
    // 记录最小生成树的权重和
    private int weightSum = 0;
    // graph 是用邻接表表示的一幅图，
    // graph[s] 记录节点 s 所有相邻的边，
    // 三元组 int[]{from, to, weight} 表示一条边
    private List<int[]>[] graph;

    public Prim(List<int[]>[] graph) {
        this.graph = graph;
        this.pq = new PriorityQueue<>((a, b) -> {
            // 按照边的权重从小到大排序
            return a[2] - b[2];
        });
        // 图中有 n 个节点
        int n = graph.length;
        this.inMST = new boolean[n];

        // 随便从一个点开始切分都可以，我们不妨从节点 0 开始
        inMST[0] = true;
        cut(0);
        // 不断进行切分，向最小生成树中添加边
        while (!pq.isEmpty()) {
            int[] edge = pq.poll();
            int to = edge[1];
            int weight = edge[2];
            if (inMST[to]) {
                // 节点 to 已经在最小生成树中，跳过
                // 否则这条边会产生环
                continue;
            }
            // 将边 edge 加入最小生成树
            weightSum += weight;
            inMST[to] = true;
            // 节点 to 加入后，进行新一轮切分，会产生更多横切边
            cut(to);
        }
    }

    // 将 s 的横切边加入优先队列
    private void cut(int s) {
        // 遍历 s 的邻边
        for (int[] edge : graph[s]) {
            int to = edge[1];
            if (inMST[to]) {
                // 相邻接点 to 已经在最小生成树中，跳过
                // 否则这条边会产生环
                continue;
            }
            // 加入横切边队列
            pq.offer(edge);
        }
    }

    // 最小生成树的权重和
    public int weightSum() {
        return weightSum;
    }

    // 判断最小生成树是否包含图中的所有节点
    public boolean allConnected() {
        for (int i = 0; i < inMST.length; i++) {
            if (!inMST[i]) {
                return false;
            }
        }
        return true;
    }
}
```

详见：<https://labuladong.gitee.io/algo/2/22/55/>

## 回溯

回溯和DFS的区别：

回溯关注的是树枝，DFS关注的是结点，反映到代码上：

```java
// DFS 算法，关注点在节点
void traverse(TreeNode root) {
    if (root == null) return;
    printf("进入节点 %s", root);
    for (TreeNode child : root.children) {
        traverse(child);
    }
    printf("离开节点 %s", root);
}

// 回溯算法，关注点在树枝
void backtrack(TreeNode root) {
    if (root == null) return;
    for (TreeNode child : root.children) {
        // 做选择
        printf("从 %s 到 %s", root, child);
        backtrack(child);
        // 撤销选择
        printf("从 %s 到 %s", child, root);
    }
}
```

## 设计数据结构

### LRU

即Least Recently Used，也就是每次淘汰那些最久没被使用的数据，主要就是利用了哈希链表（在Java中是`LinkedHashMap`）这种数据结构，如下图所示：

![img](https://labuladong.gitee.io/algo/images/LRU%e7%ae%97%e6%b3%95/4.jpg)

手写轮子模板：

```java
class LRUCache {
    // key -> Node(key, val)
    private Map<Integer, Node> map;
    // Node(k1, v1) <-> Node(k2, v2)...
    private DoubleList cache;
    // 最大容量
    private int capacity;

    public LRUCache(int capacity) {
        this.capacity = capacity;
        map = new HashMap<>();
        cache = new DoubleList();
    }

    public int get(int key) {
        if (!map.containsKey(key)) {
            return -1;
        }
        // 将该数据提升为最近使用的
        makeRecently(key);
        return map.get(key).val;
    }

    public void put(int key, int val) {
        if (map.containsKey(key)) {
            // 删除旧的数据
            deleteKey(key);
            // 新插入的数据为最近使用的数据
            addRecently(key, val);
            return;
        }

        if (cap == cache.size()) {
            // 删除最久未使用的元素
            removeLeastRecently();
        }
        // 添加为最近使用的元素
        addRecently(key, val);
    }

    /* 将某个 key 提升为最近使用的 */
    private void makeRecently(int key) {
        Node x = map.get(key);
        // 先从链表中删除这个节点
        cache.remove(x);
        // 重新插到队尾
        cache.addLast(x);
    }

    /* 添加最近使用的元素 */
    private void addRecently(int key, int val) {
        Node x = new Node(key, val);
        // 链表尾部就是最近使用的元素
        cache.addLast(x);
        // 别忘了在 map 中添加 key 的映射
        map.put(key, x);
    }

    /* 删除某一个 key */
    private void deleteKey(int key) {
        Node x = map.get(key);
        // 从链表中删除
        cache.remove(x);
        // 从 map 中删除
        map.remove(key);
    }

    /* 删除最久未使用的元素 */
    private void removeLeastRecently() {
        // 链表头部的第一个元素就是最久未使用的
        Node deletedNode = cache.removeFirst();
        // 同时别忘了从 map 中删除它的 key
        int deletedKey = deletedNode.key;
        map.remove(deletedKey);
    }

    class Node {
        int key, val;
        Node prev, next;

        public Node(int key, int val) {
            this.key = key;
            this.val = val;
        }
    }

    class DoubleList {
        // 头尾虚节点
        private Node head, tail;  
        // 链表元素数
        private int size;

        public DoubleList() {
            // 初始化双向链表的数据
            head = new Node(0, 0);
            tail = new Node(0, 0);
            head.next = tail;
            tail.prev = head;
            size = 0;
        }

        // 在链表尾部添加节点 x，时间 O(1)
        public void addLast(Node x) {
            x.prev = tail.prev;
            x.next = tail;
            tail.prev.next = x;
            tail.prev = x;
            size++;
        }

        // 删除链表中的 x 节点（x 一定存在）
        // 由于是双链表且给的是目标 Node 节点，时间 O(1)
        public void remove(Node x) {
            x.prev.next = x.next;
            x.next.prev = x.prev;
            size--;
        }

        // 删除链表中第一个节点，并返回该节点，时间 O(1)
        public Node removeFirst() {
            if (size == 0) {
                return null;
            }
            Node first = head.next;
            remove(first);
            return first;
        }

        // 返回链表长度，时间 O(1)
        public int size() {
            return size;
        }
    }
}
```

使用`LinkedHashMap`模板：

```java
class LRUCache {
    int cap;
    LinkedHashMap<Integer, Integer> cache = new LinkedHashMap<>();
    public LRUCache(int capacity) { 
        this.cap = capacity;
    }

    public int get(int key) {
        if (!cache.containsKey(key)) {
            return -1;
        }
        // 将 key 变为最近使用
        makeRecently(key);
        return cache.get(key);
    }

    public void put(int key, int val) {
        if (cache.containsKey(key)) {
            // 修改 key 的值
            cache.put(key, val);
            // 将 key 变为最近使用
            makeRecently(key);
            return;
        }

        if (cache.size() >= this.cap) {
            // 链表头部就是最久未使用的 key
            int oldestKey = cache.keySet().iterator().next();
            cache.remove(oldestKey);
        }
        // 将新的 key 添加链表尾部
        cache.put(key, val);
    }

    private void makeRecently(int key) {
        int val = cache.get(key);
        // 删除 key，重新插入到队尾
        cache.remove(key);
        cache.put(key, val);
    }
}
```

### LFU

Least Frequently Used，也就是每次淘汰那些使用次数最少的数据，主要利用了keyToVal，keyToFreq，freqToKeys三个数据结构相互配合，详见：<https://mp.weixin.qq.com/s/oXv03m1J8TwtHwMJEZ1ApQ>，模板如下：

```java
class LFUCache {
    // key 到 val 的映射，我们后文称为 KV 表
    HashMap<Integer, Integer> keyToVal;
    // key 到 freq 的映射，我们后文称为 KF 表
    HashMap<Integer, Integer> keyToFreq;
    // freq 到 key 列表的映射，我们后文称为 FK 表
    HashMap<Integer, LinkedHashSet<Integer>> freqToKeys;
    // 记录最小的频次
    int minFreq;
    // 记录 LFU 缓存的最大容量
    int cap;

    public LFUCache(int capacity) {
        keyToVal = new HashMap<>();
        keyToFreq = new HashMap<>();
        freqToKeys = new HashMap<>();
        this.cap = capacity;
        this.minFreq = 0;
    }

    public int get(int key) {
        if (!keyToVal.containsKey(key)) {
            return -1;
        }
        // 增加 key 对应的 freq
        increaseFreq(key);
        return keyToVal.get(key);
    }

    public void put(int key, int val) {
        if (this.cap <= 0) return;

        /* 若 key 已存在，修改对应的 val 即可 */
        if (keyToVal.containsKey(key)) {
            keyToVal.put(key, val);
            // key 对应的 freq 加一
            increaseFreq(key);
            return;
        }

        /* key 不存在，需要插入 */
        /* 容量已满的话需要淘汰一个 freq 最小的 key */
        if (this.cap <= keyToVal.size()) {
            removeMinFreqKey();
        }

        /* 插入 key 和 val，对应的 freq 为 1 */
        // 插入 KV 表
        keyToVal.put(key, val);
        // 插入 KF 表
        keyToFreq.put(key, 1);
        // 插入 FK 表
        freqToKeys.putIfAbsent(1, new LinkedHashSet<>());
        freqToKeys.get(1).add(key);
        // 插入新 key 后最小的 freq 肯定是 1
        this.minFreq = 1;
    }

    private void increaseFreq(int key) {
        int freq = keyToFreq.get(key);
        /* 更新 KF 表 */
        keyToFreq.put(key, freq + 1);
        /* 更新 FK 表 */
        // 将 key 从 freq 对应的列表中删除
        freqToKeys.get(freq).remove(key);
        // 将 key 加入 freq + 1 对应的列表中
        freqToKeys.putIfAbsent(freq + 1, new LinkedHashSet<>());
        freqToKeys.get(freq + 1).add(key);
        // 如果 freq 对应的列表空了，移除这个 freq
        if (freqToKeys.get(freq).isEmpty()) {
            freqToKeys.remove(freq);
            // 如果这个 freq 恰好是 minFreq，更新 minFreq
            if (freq == this.minFreq) {
                this.minFreq++;
            }
        }
    }

    private void removeMinFreqKey() {
        // freq 最小的 key 列表
        LinkedHashSet<Integer> keyList = freqToKeys.get(this.minFreq);
        // 其中最先被插入的那个 key 就是该被淘汰的 key
        int deletedKey = keyList.iterator().next();
        /* 更新 FK 表 */
        keyList.remove(deletedKey);
        if (keyList.isEmpty()) {
            freqToKeys.remove(this.minFreq);
            // 问：这里需要更新 minFreq 的值吗？
            // 这里不用修改minFreq因为后面会置为1
        }
        /* 更新 KV 表 */
        keyToVal.remove(deletedKey);
        /* 更新 KF 表 */
        keyToFreq.remove(deletedKey);
    }
}
```

### TrieMap和TrieSet

Trie 树又叫字典树、前缀树、单词查找树，是一种二叉树衍生出来的高级数据结构，主要应用场景是处理字符串前缀相关的操作。结构如下所示：

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/gibkIz0MVqdHbPt3iaYMdmqUMxEpq0F5AMuKFmpJEB0gM7FJuVjAicfIoWB7HtdISJ18bcqKfwlnibeth3ZibVD35Sg/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

底层是Trie树的Map就是TrieMap，TrieMap就是key是字符串，value是任何类型的map，TrieSet就是没用到value的TrieMap，详见：<https://mp.weixin.qq.com/s?__biz=MzAxODQxMDM0Mw==&mid=2247495471&idx=1&sn=fd180d7e207e92a87a9c9cce69b8cdb9>

TrieMap模板如下：

```java
class TrieMap<V> {
    // ASCII 码个数
    private static final int R = 256;
    // 当前存在 Map 中的键值对个数
    private int size = 0;
    // Trie 树的根节点
    private TrieNode<V> root = null;

    private static class TrieNode<V> {
        V val = null;
        TrieNode<V>[] children = new TrieNode[R];
    }

    /***** 增/改 *****/

    // 在 map 中添加或修改键值对
    public void put(String key, V val) {
        if (!containsKey(key)) {
            // 新增键值对
            size++;
        }
        // 需要一个额外的辅助函数，并接收其返回值
        root = put(root, key, val, 0);
    }

    // 定义：向以 node 为根的 Trie 树中插入 key[i..]，返回插入完成后的根节点
    private TrieNode<V> put(TrieNode<V> node, String key, V val, int i) {
        if (node == null) {
            // 如果树枝不存在，新建
            node = new TrieNode<>();
        }
        if (i == key.length()) {
            // key 的路径已插入完成，将值 val 存入节点
            node.val = val;
            return node;
        }
        char c = key.charAt(i);
        // 递归插入子节点，并接收返回值
        node.children[c] = put(node.children[c], key, val, i + 1);
        return node;
    }

    /***** 删 *****/

    // 在 Map 中删除 key
    public void remove(String key) {
        if (!containsKey(key)) {
            return;
        }
        // 递归修改数据结构要接收函数的返回值
        root = remove(root, key, 0);
        size--;
    }

    // 定义：在以 node 为根的 Trie 树中删除 key[i..]，返回删除后的根节点
    private TrieNode<V> remove(TrieNode<V> node, String key, int i) {
        if (node == null) {
            return null;
        }
        if (i == key.length()) {
            // 找到了 key 对应的 TrieNode，删除 val
            node.val = null;
        } else {
            char c = key.charAt(i);
            // 递归去子树进行删除
            node.children[c] = remove(node.children[c], key, i + 1);
        }
        // 后序位置，递归路径上的节点可能需要被清理
        if (node.val != null) {
            // 如果该 TireNode 存储着 val，不需要被清理
            return node;
        }
        // 检查该 TrieNode 是否还有后缀
        for (int c = 0; c < R; c++) {
            if (node.children[c] != null) {
                // 只要存在一个子节点（后缀树枝），就不需要被清理
                return node;
            }
        }
        // 既没有存储 val，也没有后缀树枝，则该节点需要被清理
        return null;
    }

    /***** 查 *****/

    // 搜索 key 对应的值，不存在则返回 null
    public V get(String key) {
        // 从 root 开始搜索 key
        TrieNode<V> x = getNode(root, key);
        if (x == null || x.val == null) {
            // x 为空或 x 的 val 字段为空都说明 key 没有对应的值
            return null;
        }
        return x.val;
    }

    // 判断 key 是否存在在 Map 中
    public boolean containsKey(String key) {
        return get(key) != null;
    }

    // 判断是和否存在前缀为 prefix 的键
    public boolean hasKeyWithPrefix(String prefix) {
        // 只要能找到一个节点，就是存在前缀
        return getNode(root, prefix) != null;
    }

    // 在所有键中寻找 query 的最短前缀
    public String shortestPrefixOf(String query) {
        TrieNode<V> p = root;
        // 从节点 node 开始搜索 key
        for (int i = 0; i < query.length(); i++) {
            if (p == null) {
                // 无法向下搜索
                return "";
            }
            if (p.val != null) {
                // 找到一个键是 query 的前缀
                return query.substring(0, i);
            }
            // 向下搜索
            char c = query.charAt(i);
            p = p.children[c];
        }

        if (p != null && p.val != null) {
            // 如果 query 本身就是一个键
            return query;
        }
        return "";
    }

    // 在所有键中寻找 query 的最长前缀
    public String longestPrefixOf(String query) {
        TrieNode<V> p = root;
        // 记录前缀的最大长度
        int max_len = 0;

        // 从节点 node 开始搜索 key
        for (int i = 0; i < query.length(); i++) {
            if (p == null) {
                // 无法向下搜索
                break;
            }
            if (p.val != null) {
                // 找到一个键是 query 的前缀，更新前缀的最大长度
                max_len = i;
            }
            // 向下搜索
            char c = query.charAt(i);
            p = p.children[c];
        }

        if (p != null && p.val != null) {
            // 如果 query 本身就是一个键
            return query;
        }
        return query.substring(0, max_len);
    }

    // 搜索前缀为 prefix 的所有键
    public List<String> keysWithPrefix(String prefix) {
        List<String> res = new LinkedList<>();
        // 找到匹配 prefix 在 Trie 树中的那个节点
        TrieNode<V> x = getNode(root, prefix);
        if (x == null) {
            return res;
        }
        // DFS 遍历以 x 为根的这棵 Trie 树
        traverse(x, new StringBuilder(prefix), res);
        return res;
    }

    // 遍历以 node 节点为根的 Trie 树，找到所有键
    private void traverse(TrieNode<V> node, StringBuilder path, List<String> res) {
        if (node == null) {
            // 到达 Trie 树底部叶子结点
            return;
        }

        if (node.val != null) {
            // 找到一个 key，添加到结果列表中
            res.add(path.toString());
        }

        // 回溯算法遍历框架
        for (char c = 0; c < R; c++) {
            // 做选择
            path.append(c);
            traverse(node.children[c], path, res);
            // 撤销选择
            path.deleteCharAt(path.length() - 1);
        }
    }

    // 通配符 . 匹配任意字符
    public List<String> keysWithPattern(String pattern) {
        List<String> res = new LinkedList<>();
        traverse(root, new StringBuilder(), pattern, 0, res);
        return res;
    }

    // 遍历函数，尝试在「以 node 为根的 Trie 树中」匹配 pattern[i..]
    private void traverse(TrieNode<V> node, StringBuilder path, String pattern, int i, List<String> res) {
        if (node == null) {
            // 树枝不存在，即匹配失败
            return;
        }
        if (i == pattern.length()) {
            // pattern 匹配完成
            if (node.val != null) {
                // 如果这个节点存储着 val，则找到一个匹配的键
                res.add(path.toString());
            }
            return;
        }
        char c = pattern.charAt(i);
        if (c == '.') {
            // pattern[i] 是通配符，可以变化成任意字符
            // 多叉树（回溯算法）遍历框架
            for (char j = 0; j < R; j++) {
                path.append(j);
                traverse(node.children[j], path, pattern, i + 1, res);
                path.deleteCharAt(path.length() - 1);
            }
        } else {
            // pattern[i] 是普通字符 c
            path.append(c);
            traverse(node.children[c], path, pattern, i + 1, res);
            path.deleteCharAt(path.length() - 1);
        }
    }

    // 判断是和否存在前缀为 prefix 的键
    public boolean hasKeyWithPattern(String pattern) {
        // 从 root 节点开始匹配 pattern[0..]
        return hasKeyWithPattern(root, pattern, 0);
    }

    // 函数定义：从 node 节点开始匹配 pattern[i..]，返回是否成功匹配
    private boolean hasKeyWithPattern(TrieNode<V> node, String pattern, int i) {
        if (node == null) {
            // 树枝不存在，即匹配失败
            return false;
        }
        if (i == pattern.length()) {
            // 模式串走到头了，看看匹配到的是否是一个键
            return node.val != null;
        }
        char c = pattern.charAt(i);
        // 没有遇到通配符
        if (c != '.') {
            // 从 node.children[c] 节点开始匹配 pattern[i+1..]
            return hasKeyWithPattern(node.children[c], pattern, i + 1);
        }
        // 遇到通配符
        for (int j = 0; j < R; j++) {
            // pattern[i] 可以变化成任意字符，尝试所有可能，只要遇到一个匹配成功就返回
            if (hasKeyWithPattern(node.children[j], pattern, i + 1)) {
                return true;
            }
        }
        // 都没有匹配
        return false;
    }

    // 从节点 node 开始搜索 key，如果存在返回对应节点，否则返回 null
    private TrieNode<V> getNode(TrieNode<V> node, String key) {
        TrieNode<V> p = node;
        // 从节点 node 开始搜索 key
        for (int i = 0; i < key.length(); i++) {
            if (p == null) {
                // 无法向下搜索
                return null;
            }
            // 向下搜索
            char c = key.charAt(i);
            p = p.children[c];
        }
        return p;
    }

    public int size() {
        return size;
    }
}
```

TrieSet模板如下：

```java
class TrieSet {
    // 底层用一个 TrieMap，键就是 TrieSet，值仅仅起到占位的作用
    // 值的类型可以随便设置，我参考 Java 标准库设置成 Object
    private final TrieMap<Object> map = new TrieMap<>();

    /***** 增 *****/

    // 在集合中添加元素 key
    public void add(String key) {
        map.put(key, new Object());
    }

    /***** 删 *****/

    // 从集合中删除元素 key
    public void remove(String key) {
        map.remove(key);
    }

    /***** 查 *****/

    // 判断元素 key 是否存在集合中
    public boolean contains(String key) {
        return map.containsKey(key);
    }

    // 在集合中寻找 query 的最短前缀
    public String shortestPrefixOf(String query) {
        return map.shortestPrefixOf(query);
    }

    // 在集合中寻找 query 的最长前缀
    public String longestPrefixOf(String query) {
        return map.longestPrefixOf(query);
    }

    // 在集合中搜索前缀为 prefix 的所有元素
    public List<String> keysWithPrefix(String prefix) {
        return map.keysWithPrefix(prefix);
    }

    // 判断集合中是否存在前缀为 prefix 的元素
    public boolean hasKeyWithPrefix(String prefix) {
        return map.hasKeyWithPrefix(prefix);
    }

    // 通配符 . 匹配任意字符，返回集合中匹配 pattern 的所有元素
    public List<String> keysWithPattern(String pattern) {
        return map.keysWithPattern(pattern);
    }

    // 通配符 . 匹配任意字符，判断集合中是否存在匹配 pattern 的元素
    public boolean hasKeyWithPattern(String pattern) {
        return map.hasKeyWithPattern(pattern);
    }

    // 返回集合中元素的个数
    public int size() {
        return map.size();
    }
}
```

### 单调栈

就是元素单调递增或递减的栈，比如单减栈，入栈的时候将小于入栈元素的栈顶出栈，就可以保证栈的单调递减，一般可以用在「下一个更大元素」，「上一个更小元素」等问题上，「下一个更大元素」模板如下：

```java
int[] nextGreaterElement(int[] nums) {
    int n = nums.length;
    // 存放答案的数组
    int[] res = new int[n];
    Stack<Integer> s = new Stack<>(); 
    // 倒着往栈里放
    for (int i = n - 1; i >= 0; i--) {
        // 判定个子高矮
        while (!s.isEmpty() && s.peek() <= nums[i]) {
            // 矮个起开，反正也被挡着了。。。
            s.pop();
        }
        // nums[i] 身后的更大元素
        res[i] = s.isEmpty() ? -1 : s.peek();
        s.push(nums[i]);
    }
    return res;
}
```

### 单调队列

就是元素单调递增或递减的队列，比如单减队列，入队的时候将小于入队元素的队尾出队，就可以保证队的单调递减，一般可以用在「滑动窗口最大值」问题上，模板如下：

```java
/* 单调队列的实现 */
class MonotonicQueue {
    LinkedList<Integer> maxq = new LinkedList<>();
    public void push(int n) {
        // 将小于 n 的元素全部删除
        while (!maxq.isEmpty() && maxq.getLast() < n) {
            maxq.pollLast();
        }
        // 然后将 n 加入尾部
        maxq.addLast(n);
    }

    public int max() {
        return maxq.getFirst();
    }

    public void poll(int n) {
        if (n == maxq.getFirst()) {
            maxq.pollFirst();
        }
    }
}
```

### 二叉堆

就是最大堆或最小堆，是一颗完全二叉树，所以可以放在数组里面，用简单的计算就能得到结点的父节点和左右孩子，基于二叉堆开发出了优先队列，优先队列插入时将插入结点放到数组最后面然后对该节点执行上浮操作，删除时将堆顶删除，然后将数组最后面的结点放到堆顶的位置，然后对堆顶做下沉操作。模板如下：

#### 通用版

```java
public class MaxPQ
    <Key extends Comparable<Key>> {
    // 存储元素的数组
    private Key[] pq;
    // 当前 Priority Queue 中的元素个数
    private int size = 0;

    public MaxPQ(int cap) {
        // 索引 0 不用，所以多分配一个空间
        pq = (Key[]) new Comparable[cap + 1];
    }

    /* 返回当前队列中最大元素 */
    public Key max() {
        return pq[1];
    }

    /* 插入元素 e */
    public void insert(Key e) {
        size++;
        // 先把新元素加到最后
        pq[size] = e;
        // 然后让它上浮到正确的位置
        swim(size);
    }

    /* 删除并返回当前队列中最大元素 */
    public Key delMax() {
        // 最大堆的堆顶就是最大元素
        Key max = pq[1];
        // 把这个最大元素换到最后，删除之
        swap(1, size);
        pq[size] = null;
        size--;
        // 让 pq[1] 下沉到正确位置
        sink(1);
        return max;
    }

    /* 上浮第 x 个元素，以维护最大堆性质 */
    private void swim(int x) {
        // 如果浮到堆顶，就不能再上浮了
        while (x > 1 && less(parent(x), x)) {
            // 如果第 x 个元素比上层大
            // 将 x 换上去
            swap(parent(x), x);
            x = parent(x);
        }
    }

    /* 下沉第 x 个元素，以维护最大堆性质 */
    private void sink(int x) {
        // 如果沉到堆底，就沉不下去了
        while (left(x) <= size) {
            // 先假设左边节点较大
            int max = left(x);
            // 如果右边节点存在，比一下大小
            if (right(x) <= size && less(max, right(x)))
                max = right(x);
            // 结点 x 比俩孩子都大，就不必下沉了
            if (less(max, x)) break;
            // 否则，不符合最大堆的结构，下沉 x 结点
            swap(x, max);
            x = max;
        }
    }

    /* 交换数组的两个元素 */
    private void swap(int i, int j) {
        Key temp = pq[i];
        pq[i] = pq[j];
        pq[j] = temp;
    }

    /* pq[i] 是否比 pq[j] 小？ */
    private boolean less(int i, int j) {
        return pq[i].compareTo(pq[j]) < 0;
    }

    // 父节点的索引
    private int parent(int root) {
        return root / 2;
    }
    // 左孩子的索引
    private int left(int root) {
        return root * 2;
    }
    // 右孩子的索引
    private int right(int root) {
        return root * 2 + 1;
    }
}
```

#### 整形版

```java
class MaxPQ {
    private int[] nums;
    private int size = 0;
    private int capacity;

    public MaxPQ(int capacity) {
        this.capacity = capacity;
        nums = new int[capacity + 1];
    }

    public boolean isEmpty() {
        return size == 0;
    }

    public boolean isFull() {
        return size == capacity;
    }

    public int max() {
        return nums[1];
    }

    private int parent(int root) {
        return root / 2;
    }

    private int left(int root) {
        return root * 2;
    }

    private int right(int root) {
        return root * 2 + 1;
    }

    private void swap(int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }

    public void insert(int num) {
        size++;
        nums[size] = num;
        swim(size);
    }

    public int delMax() {
        int max = nums[1];
        nums[1] = nums[size];
        size--;
        sink(1);
        return max;
    }

    private void swim(int x) {
        while (x > 1 && nums[x] > nums[parent(x)]) {
            swap(x, parent(x));
            x = parent(x);
        }
    }

    private void sink(int x) {
        while (left(x) <= size) {
            int max = left(x);
            if (right(x) <= size && nums[right(x)] > nums[max]) {
                max = right(x);
            }
            if (nums[x] > nums[max]) {
                break;
            }
            swap(x, max);
            x = max;
        }
    }
}
```

#### 无类版

```java
private void buildHeap(int[] heap) {
    int size = heap.length - 1;
    for (int i = size / 2; i >= 1; i--) {
        sink(heap, i);
    }
}

private void sink(int[] heap, int x) {
    int size = heap.length - 1;
    while (x * 2 <= size) {
        int min = x * 2;
        if (x * 2 + 1 <= size && heap[x * 2 + 1] < heap[min]) {
            min = x * 2 + 1;
        }
        if (heap[x] < heap[min]) {
            break;
        }
        swap(heap, x, min);
        x = min;
    }
}

private void swap(int[] heap, int i, int j) {
    int temp = heap[i];
    heap[i] = heap[j];
    heap[j] = temp;
}
```

### 队列实现栈以及栈实现队列

栈实现队列用两个栈即可，入栈相当于入队，出栈时先将一个栈里的元素出栈到另一个栈中，栈顶就是队头，模板如下：

```java
class MyQueue {
    private Stack<Integer> s1, s2;

    public MyQueue() {
        s1 = new Stack<>();
        s2 = new Stack<>();
    }

    /** 添加元素到队尾 */
    public void push(int x) {
        s1.push(x);
    }

    /** 返回队头元素 */
    public int peek() {
        if (s2.isEmpty())
            // 把 s1 元素压入 s2
            while (!s1.isEmpty())
                s2.push(s1.pop());
        return s2.peek();
    }

    /** 删除队头的元素并返回 */
    public int pop() {
        // 先调用 peek 保证 s2 非空
        peek();
        return s2.pop();
    }

    /** 判断队列是否为空 */
    public boolean empty() {
        return s1.isEmpty() && s2.isEmpty();
    }
}
```

栈实现队列简单粗暴，pop的时候把除了队尾的其他都出队再加入到队尾即可，模板如下：

```java
class MyStack {
    Queue<Integer> q = new LinkedList<>();
    int top_elem = 0;

    /** 添加元素到栈顶 */
    public void push(int x) {
        // x 是队列的队尾，是栈的栈顶
        q.offer(x);
        top_elem = x;
    }

    /** 返回栈顶元素 */
    public int top() {
        return top_elem;
    }

    /** 删除栈顶的元素并返回 */
    public int pop() {
        int size = q.size();
        // 留下队尾 2 个元素
        while (size > 2) {
            q.offer(q.poll());
            size--;
        }
        // 记录新的队尾元素
        top_elem = q.peek();
        q.offer(q.poll());
        // 删除之前的队尾元素
        return q.poll();
    }

    /** 判断栈是否为空 */
    public boolean empty() {
        return q.isEmpty();
    }
}
```

## 排序

### 快速排序

快速排序的确定中枢位置的过程叫做快速选择，可以快速确定一个数在排序以后的位置，模板如下：

```java
/**
 * @Description 一趟快速排序：將序列分片，基准元素左边的都是小于它的，右边的都是大于它的
 * @Param [arr, left, right]
 */
public static int partition(int[] arr, int left, int right){
    int pivot = arr[left];        	// 选取第一个为基准元素
    while(left<right){
        /* 先从右往左移动，直到遇见小于 pivot 的元素 */
        while (left<right && arr[right]>=pivot){
            right--;
        }
        arr[left] = arr[right];         // 记录小于 pivot 的值
        
        /* 再从左往右移动，直到遇见大于 pivot 的元素 */
        while(left<right && arr[left]<=pivot){
            left++;
        }
        arr[right] = arr[left];         // 记录大于 pivot 的值
    }
    arr[left] = pivot;            		// 记录基准元素到当前指针指向的区域
    return left;						// 返回基准元素的索引
}
```

快速选择可以解决数组中的第K个最大元素这种问题

快速排序模板如下：

```java
public static void quickSort(int[] arr, int left, int right){
    if (left < right){
        // 把数组分块
        int pivot = partition(arr, left, right);
        // 基准元素左边递归
        quickSort(arr, left, pivot-1);
        // 基准元素右边递归
        quickSort(arr, pivot+1, right);
    }
}

public static int partition(int[] arr, int left, int right){
    int pivot = arr[left];        	// 选取第一个为基准元素
    while(left<right){
        /* 先从右往移动，直到遇见小于 pivot 的元素 */
        while (left<right && arr[right]>=pivot){
            right--;
        }
        arr[left] = arr[right];         // 记录小于 pivot 的值
        
        /* 再从左往右移动，直到遇见大于 pivot 的元素 */
        while(left<right && arr[left]<=pivot){
            left++;
        }
        arr[right] = arr[left];         // 记录大于 pivot 的值
    }
    arr[left] = pivot;            		// 记录基准元素到当前指针指向的区域
    return left;						// 返回基准元素的索引
}

```

# 其他

## 零碎

从整体到细节，自顶向下，从抽象到具体的框架思维是通用的，不只是学习数据结构和算法，学习其他任何知识都是高效的。

数据结构的物理存储方式就是链式和顺序两种，基本操作就是增删改查，遍历方式无非迭代和递归。

计算机算法的本质就是枚举，只不过这里枚举需要做到两个方面：无遗漏和无冗余，有时候还可以利用一些定理进行优化（缩小搜索范围），比如剪枝和数学定理

难点在无遗漏的问题：

难点在无冗余的问题：递归类问题（动态规划）

难点在优化的问题：非递归类问题（并查集，贪心，KMP）

Java里优先队列就是二叉堆，也就是PriorityQueue

base case就是最基本的情况，从递归的角度理解就是递归出口，从分解问题(分治)的角度理解就是最基本的问题（不能再分了）

如果需要通过值找到其在数组的索引，将数组遍历一遍是一种做法，还可以创建一个valToIndex的hashmap

序列化就是把结构化的数据（比如树）打平（比如转换为字符串）

序列化和反序列化的目的：以某种特定格式组织数据，使得数据可以独立于编程语言。

Boyer-Moore(摩尔) 投票算法详见：<https://leetcode.cn/problems/majority-element/solutions/146074/duo-shu-yuan-su-by-leetcode-solution/>

负数取余得到的结果还是负数

注意二分查找的左边界是第一个大于等于target的数，右边界是从右往左第一个小于等于target的数

python里自带了二分查找左边界和右边界的函数，Java里有基本版的二分查找

看到「最大化最小值」或者「最小化最大值」（其实就是那种要求一堆数字尽量平均的题）就要想到二分答案，这是一个固定的套路。为什么？一般来说，二分的值越大，越能/不能满足要求；二分的值越小，越不能/能满足要求，有单调性，可以二分。

前缀和中preSum[i + 1]是[0...i]的元素之和

差分数组的前缀和就是原数组

## 待做

https://labuladong.gitee.io/algo/1/3/的那几个算法框架及之后的几个框架文章都没看

https://labuladong.gitee.io/algo/2/21/41/没看

https://labuladong.gitee.io/algo/2/21/45/没看

https://labuladong.gitee.io/algo/2/22/57/没看

https://labuladong.gitee.io/algo/2/23/67/没看

https://labuladong.gitee.io/algo/2/20/29/没看

## 技巧

dummy（虚拟头结点)：可以很好的避免第一个节点的特殊性，将第一个节点当作第二个节点，也即是所有节点统一处理

把 return 语句都放在函数开头，因为一般 return 语句都是 base case，集中放在一起可以让算法结构更清晰。

将二维坐标映射到一维的常用技巧：将二维坐标 `(x,y)` 转换成 `x * n + y` 这个数（`m` 是棋盘的行数，`n` 是棋盘的列数）

方向数组 d 是上下左右搜索的常用手法：`int[][] d = new int[][]{{1,0}, {0,1}, {0,-1}, {-1,0}};`

## 学习方法

以后做题，先想这道题考察什么知识点。
