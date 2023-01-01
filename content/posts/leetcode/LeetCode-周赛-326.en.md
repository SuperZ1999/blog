---
title: "LeetCode 周赛 326"
date: 2023-01-01T11:39:09+08:00
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

挨个除就完事了，直接看代码

#### 第二题

遍历每个元素，并求出他们的质因数加入到set集合，最后统计set里的元素即可

#### 第三题

贪心算法，从左往右求出刚好小于k的数，统计数量即可

#### 第四题

用素数筛法求出所有素数，然后根据素数之差求出最接近的两个素数

#### 总结

这次比较简单，半小时结束战斗

### 代码

#### 第一题

```java
class Solution {
    public int countDigits(int num) {
        int n = num, res = 0;
        while (n != 0) {
            if (num % (n % 10) == 0) {
                res++;
            }
            n = n / 10;
        }
        return res;
    }
}
```

#### 第二题

```java
class Solution {
    public int distinctPrimeFactors(int[] nums) {
        Set<Integer> res = new HashSet<>();
        for (int num : nums) {
            for (int i = 2; i <= num;) {
                if (num % i == 0) {
                    res.add(i);
                    num /= i;
                } else {
                    i++;
                }
            }
        }
        return res.size();
    }
}
```

#### 第三题

```java
class Solution {
    public int minimumPartition(String s, int k) {
        int i = 0, j = 1, res = 0;
        while (i < s.length()) {
            long num = Long.parseLong(s.substring(i, j));
            if (num > k) {
                if (j == i + 1) {
                    return -1;
                } else {
                    res++;
                    i = j - 1;
                }
            } else {
                if (j == s.length()) {
                    res++;
                    break;
                }
                j++;
            }
        }
        return res;
    }
}
```

#### 第四题

```java
class Solution {
    public int[] closestPrimes(int left, int right) {
        boolean[] isPrime = new boolean[right + 1];
        Arrays.fill(isPrime, true);
        for (int i = 2; i <= right; i++) {
            if (!isPrime[i]) {
                continue;
            }
            for (int j = i + i; j <= right; j += i) {
                isPrime[j] = false;
            }
        }
        isPrime[0] = isPrime[1] = false;
        int[] res = new int[]{0, 1000000};
        int pre = -1;
        for (int i = left; i <= right; i++) {
            if (!isPrime[i]) {
                continue;
            }
            if (pre == -1) {
                pre = i;
            } else {
                if (i - pre < res[1] - res[0]) {
                    res[0] = pre;
                    res[1] = i;
                }
                pre = i;
            }
        }
        return res[0] == 0 && res[1] == 1000000 ? new int[]{-1, -1} : res;
    }
}
```

### References

---

#### 1. [统计能整除数字的位数](https://leetcode.cn/problems/count-the-digits-that-divide-a-number/)

#### 2. [数组乘积中的不同质因数数目](https://leetcode.cn/problems/distinct-prime-factors-of-product-of-array/)

#### 3. [将字符串分割成值不超过 K 的子字符串](https://leetcode.cn/problems/partition-string-into-substrings-with-values-at-most-k/)

#### 4. [范围内最接近的两个质数](https://leetcode.cn/problems/closest-prime-numbers-in-range/)
