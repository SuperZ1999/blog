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

其实就是计算数组各元素的异或，证明如下：



#### 第四题



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

#### 第四题



### References

---

#### 1. [根据规则将箱子分类](https://leetcode.cn/problems/categorize-box-according-to-criteria/)

#### 2. [找到数据流中的连续整数](https://leetcode.cn/problems/find-consecutive-integers-from-a-data-stream/)

#### 3. [查询数组 Xor 美丽值](https://leetcode.cn/problems/find-xor-beauty-of-array/)

#### 4. [最大化城市的最小供电站数目](https://leetcode.cn/problems/maximize-the-minimum-powered-city/)
