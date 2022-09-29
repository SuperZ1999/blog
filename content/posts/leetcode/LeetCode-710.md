---
title: "LeetCode 710"
date: 2022-09-27T15:05:11+08:00
tags: ["leetcode"]
draft: false
---

### 思路

既然要随机获取，那么肯定要用**数组**存，并且是**紧凑**的，由于有黑名单，所以我们应该想办法把不是黑名单的数组紧凑到前`n - blacklist.length`个格子里去，那么就可以把这些格子后面的不是黑名单的数字和前面黑名单的数字交换，这样就可以随机获取数字了

又由于数组大部分元素的值和下标是一样的，所以可以省略数组，用map记录那些交换的元素

### 我的代码

```java
class Solution {
    int size;
    Set<Integer> blackSet = new HashSet<>();
    Map<Integer, Integer> blackMap = new HashMap<>();

    public Solution(int n, int[] blacklist) {
        size = n - blacklist.length;
        for (int num : blacklist) {
            if (num >= size) {
                blackSet.add(num);
            }
        }

        int last = n - 1;
        for (int num : blacklist) {
            if (num < size) {
                while (blackSet.contains(last)) {
                    last--;
                }
                blackMap.put(num, last);
                last--;
            }
        }
    }
    
    public int pick() {
        int random = new Random().nextInt(size);
        if (blackMap.containsKey(random)) {
            return blackMap.get(random);
        }
        return random;
    }
}
```

### References

---

#### 1. [黑名单中的随机数](https://leetcode.cn/problems/random-pick-with-blacklist/)
