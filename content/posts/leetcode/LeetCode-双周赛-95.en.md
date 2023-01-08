---
title: "LeetCode 双周赛 95"
date: 2023-01-07T23:56:06+08:00
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

#### 第一题

不解释

#### 第二题

用count记录一下末尾有几个value，直接看代码

#### 第三题

其实就是计算数组各元素的异或，证明详见：<https://leetcode.cn/problems/find-xor-beauty-of-array/solutions/2050337/no6289-cha-xun-shu-zu-xor-mei-li-zhi-by-d5ylk/>

#### 第四题

利用二分查找的思想，从答案可能的区间里取中间的数，然后验证答案需要额外建造多少个供电站，最后判断修建的供电站是否超过 k ，如果超过说明选择的答案偏大，否则说明偏小，然后根据偏大还是偏小再进行二分就可以了

看到「最大化最小值」或者「最小化最大值」（其实就是那种要求一堆数字尽量平均的题）就要想到二分答案，这是一个固定的套路。

为什么？一般来说，二分的值越大，越能/不能满足要求；二分的值越小，越不能/能满足要求，有单调性，可以二分。

这道题使用前缀和来确定各个城市的电量，然后二分搜索答案，验证答案时用到了差分数组

因为没做出来就不贴代码了，详见：<https://leetcode.cn/problems/maximize-the-minimum-powered-city/solutions/2050272/er-fen-da-an-qian-zhui-he-chai-fen-shu-z-jnyv/>

### 代码

#### 第一题

```java
class Solution {
    public String categorizeBox(int length, int width, int height, int mass) {
        long v = (long) length * width * height;
        boolean Bulky = length >= 10000 || width >= 10000 || height >= 10000 || v >= 1000000000;
        boolean Heavy = mass >= 100;
        if (Bulky && Heavy) {
            return "Both";
        }
        if (Bulky) {
            return "Bulky";
        }
        if (Heavy) {
            return "Heavy";
        }
        return "Neither";
    }
}
```

#### 第二题

```java
class DataStream {
    private int value, k, count;

    public DataStream(int value, int k) {
        this.value = value;
        this.k = k;
        this.count = 0;
    }

    public boolean consec(int num) {
        if (num == value) {
            count++;
        } else {
            count = 0;
        }
        return count >= k;
    }
}
```

#### 第三题

```java
class Solution {
    public int xorBeauty(int[] nums) {
        int res = 0;
        for (int num : nums) {
            res ^= num;
        }
        return res;
    }
}
```

### References

---

#### 1. [根据规则将箱子分类](https://leetcode.cn/problems/categorize-box-according-to-criteria/)

#### 2. [找到数据流中的连续整数](https://leetcode.cn/problems/find-consecutive-integers-from-a-data-stream/)

#### 3. [查询数组 Xor 美丽值](https://leetcode.cn/problems/find-xor-beauty-of-array/)

#### 4. [最大化城市的最小供电站数目](https://leetcode.cn/problems/maximize-the-minimum-powered-city/)
