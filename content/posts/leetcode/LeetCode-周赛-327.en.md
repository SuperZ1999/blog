---
title: "LeetCode 周赛 327"
date: 2023-01-08T19:32:53+08:00
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

两种思路：

##### 暴力解法

遍历一遍并统计

##### 二分查找

因为数组是有序的，分别查找0的左边界和右边界就可以得到正数负数的范围了，注意左边界是第一个大于等于target的数，右边界是从右往左第一个小于等于target的数，python里自带了二分查找左边界和右边界的函数，Java里有基本版的二分查找

#### 第二题

利用贪心算法的思想，每次取最大的，所以用最大堆即可，向上取整可以用(val + 2) / 3，即(val + n - 1) / n

#### 第三题

将两个字符串转为两个map，然后将两个map里的字母交换，同时判断交换后map的entry数目是否相等即可，因为总共就26个字母，所以不会超时，而且其实不用真的交换，直接通过数学计算就好了

#### 第四题

模拟题，没什么好说的，就是想办法用代码模拟这个过程，[这个答案](https://leetcode.cn/problems/time-to-cross-a-bridge/solutions/2050900/by-endlesscheng-nzqo/)比较简洁，我写的就是一坨屎山

### 代码

#### 第一题

##### 暴力解法

```java
class Solution {
    public int maximumCount(int[] nums) {
        int a = 0, b = 0;
        for (int num : nums) {
            if (num < 0) {
                a++;
            } else if (num > 0) {
                b++;
            }
        }
        return Math.max(a, b);
    }
}
```

##### 二分查找

```java
class Solution {
    public int maximumCount(int[] nums) {
        int a = searchLeft(nums, 0);
        int b = searchRight(nums, 0);
        return Math.max(a, nums.length - b - 1);
    }

    private int searchLeft(int[] nums, int target) {
        int left = 0, right = nums.length - 1;
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (target <= nums[mid]) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return nums[left] < target ? nums.length : left;
    }

    private int searchRight(int[] nums, int target) {
        int left = 0, right = nums.length - 1;
        while (left < right) {
            int mid = left + (right - left + 1) / 2;
            if (target >= nums[mid]) {
                left = mid;
            } else {
                right = mid - 1;
            }
        }
        return nums[left] > target ? -1 : left;
    }
}
```

#### 第二题

```java
class Solution {
    public long maxKelements(int[] nums, int k) {
        Queue<Integer> pq = new PriorityQueue<>((a, b) -> {
            return b - a;
        });
        for (int num : nums) {
            pq.offer(num);
        }
        long res = 0;
        while (k-- != 0) {
            res += pq.peek();
            pq.offer((pq.poll() + 2) / 3);
        }
        return res;
    }
}
```

#### 第三题

```java
class Solution {
    public boolean isItPossible(String word1, String word2) {
        Map<Character, Integer> map1 = new HashMap<>();
        Map<Character, Integer> map2 = new HashMap<>();
        for (char c : word1.toCharArray()) {
            map1.put(c, map1.getOrDefault(c, 0) + 1);
        }
        for (char c : word2.toCharArray()) {
            map2.put(c, map2.getOrDefault(c, 0) + 1);
        }
        Set<Character> keySet1 = new HashSet<>(map1.keySet());
        Set<Character> keySet2 = new HashSet<>(map2.keySet());
        for (Character c1 : keySet1) {
            for (Character c2 : keySet2) {
                swap(map1, map2, c1, c2);
                if (map1.size() == map2.size()) {
                    return true;
                }
                swap(map1, map2, c2, c1);
            }
        }
        return false;
    }

    private void swap(Map<Character, Integer> map1, Map<Character, Integer> map2, char c1, char c2) {
        Integer v1 = map1.get(c1);
        Integer v2 = map2.get(c2);
        if (v1 == 1) {
            map1.remove(c1);
        } else {
            map1.put(c1, map1.get(c1) - 1);
        }
        if (v2 == 1) {
            map2.remove(c2);
        } else {
            map2.put(c2, map2.get(c2) - 1);
        }
        map1.put(c2, map1.getOrDefault(c2, 0) + 1);
        map2.put(c1, map2.getOrDefault(c1, 0) + 1);
    }
}
```

#### 第四题

```java
class Solution {
    public int findCrossingTime(int n, int k, int[][] time) {
        Queue<Worker> pq1 = new PriorityQueue<Worker>((a, b) -> {
            if (a.time[0] + a.time[2] > b.time[0] + b.time[2] || a.time[0] + a.time[2] == b.time[0] + b.time[2] && a.index > b.index) {
                return -1;
            } else {
                return 1;
            }
        });
        Queue<Worker> pq2 = new PriorityQueue<Worker>((a, b) -> {
            if (a.time[0] + a.time[2] > b.time[0] + b.time[2] || a.time[0] + a.time[2] == b.time[0] + b.time[2] && a.index > b.index) {
                return -1;
            } else {
                return 1;
            }
        });
        for (int i = 0; i < time.length; i++) {
            pq1.offer(new Worker("waitBridge", 0, i, time[i]));
        }
        boolean bridgeIsUsed = false;
        List<Worker> workerList = new ArrayList<>();
        int t = -1, pickOldCount = 0, minTime = 1;
        while (true) {
            t += minTime;
            int newMinTime = Integer.MAX_VALUE;
            // 工作
            for (int i = 0; i < workerList.size(); i++) {
                Worker worker = workerList.get(i);
                switch (worker.state) {
                    case "leftToRight":
                        worker.leftTime -= minTime;
                        if (worker.leftTime == 0) {
                            worker.state = "pickOld";
                            worker.leftTime = worker.time[1];
                            bridgeIsUsed = false;
                            pickOldCount++;
                        }
                        newMinTime = Math.min(newMinTime, worker.leftTime);
                        break;
                    case "rightToLeft":
                        worker.leftTime -= minTime;
                        if (worker.leftTime == 0) {
                            worker.state = "putNew";
                            worker.leftTime = worker.time[3];
                            bridgeIsUsed = false;
                            if (n == 0 && pickOldCount == 0) {
                                return t;
                            }
                        }
                        newMinTime = Math.min(newMinTime, worker.leftTime);
                        break;
                    case "pickOld":
                        worker.leftTime -= minTime;
                        if (worker.leftTime == 0) {
                            worker.state = "waitBridge";
                            pq2.offer(worker);
                            workerList.remove(i);
                            i--;
                        } else {
                            newMinTime = Math.min(newMinTime, worker.leftTime);
                        }
                        break;
                    case "putNew":
                        worker.leftTime -= minTime;
                        if (worker.leftTime == 0) {
                            worker.state = "waitBridge";
                            pq1.offer(worker);
                            workerList.remove(i);
                            i--;
                        } else {
                            newMinTime = Math.min(newMinTime, worker.leftTime);
                        }
                        break;
                }
            }

            if (!bridgeIsUsed && !pq2.isEmpty()) {
                Worker poll = pq2.poll();
                poll.state = "rightToLeft";
                poll.leftTime = poll.time[2];
                workerList.add(poll);
                newMinTime = Math.min(newMinTime, poll.leftTime);
                bridgeIsUsed = true;
                pickOldCount--;
            }
            if (!bridgeIsUsed && n != 0 && !pq1.isEmpty()) {
                Worker poll = pq1.poll();
                poll.state = "leftToRight";
                poll.leftTime = poll.time[0];
                workerList.add(poll);
                newMinTime = Math.min(newMinTime, poll.leftTime);
                bridgeIsUsed = true;
                n--;
            }
            minTime = newMinTime;
        }
    }

    class Worker {
        String state;
        int leftTime, index;
        int[] time;

        public Worker(String state, int leftTime, int index, int[] time) {
            this.state = state;
            this.leftTime = leftTime;
            this.index = index;
            this.time = time;
        }
    }
}
```

### References

---

#### 1. [正整数和负整数的最大计数](https://leetcode.cn/problems/maximum-count-of-positive-integer-and-negative-integer/)

#### 2. [执行 K 次操作后的最大分数](https://leetcode.cn/problems/maximal-score-after-applying-k-operations/)

#### 3. [使字符串总不同字符的数目相等](https://leetcode.cn/problems/make-number-of-distinct-characters-equal/)

#### 4. [过桥的时间](https://leetcode.cn/problems/time-to-cross-a-bridge/)
