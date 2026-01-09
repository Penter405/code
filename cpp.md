# C++ 對應 Python 常用功能所需 `#include`

這份文件的目標是：

> **把 Python 常見功能，對應到 C++ 需要 `#include` 什麼，以及基本用法方向**。

---

## 1. print / 輸出 {#print}

### C++ header

* [`<iostream>`](#header-iostream)
* 🔙 [回到 Header 對照表](#16-c-標頭檔--功能總對照表python-思維版)

### Python

```python
print("hello", x)
```

### C++

```cpp
#include <iostream>
std::cout << "hello" << x << std::endl;
```

---

## 2. input / 輸入 {#input}

### C++ header

* [`<iostream>`](#header-iostream)
* [`<string>`](#header-string)
* 🔙 [回到 Header 對照表](#16-c-標頭檔--功能總對照表python-思維版)

### Python

```python
x = input()
```

### C++

```cpp
#include <iostream>
#include <string>
std::string x;
std::cin >> x;
```

---

## 3. list / 動態陣列 {#list}

### C++ header

* [`<vector>`](#header-vector)
* 🔙 [回到 Header 對照表](#16-c-標頭檔--功能總對照表python-思維版)

### Python

```python
a = [1, 2, 3]
a.append(4)
```

### C++

```cpp
#include <vector>
std::vector<int> a = {1, 2, 3};
a.push_back(4);
```

---

## 4. dict / key-value {#dict}

### C++ header

* [`<map>`](#header-map)
* [`<unordered_map>`](#header-unordered-map)
* 🔙 [回到 Header 對照表](#16-c-標頭檔--功能總對照表python-思維版)

### Python

```python
d = {"a": 1, "b": 2}
```

### C++

```cpp
#include <map>
#include <string>
std::map<std::string, int> d;
d["a"] = 1;
d["b"] = 2;
```

---

## 5. set {#set}

### C++ header

* [`<set>`](#header-set)
* [`<unordered_set>`](#header-unordered-set)
* 🔙 [回到 Header 對照表](#16-c-標頭檔--功能總對照表python-思維版)

### Python

```python
s = {1, 2, 3}
```

### C++

```cpp
#include <set>
std::set<int> s = {1, 2, 3};
```

---

## 6. for loop / iterable {#for-loop}

### C++ header

* [`<vector>`](#header-vector)
* [`<iostream>`](#header-iostream)
* 🔙 [回到 Header 對照表](#16-c-標頭檔--功能總對照表python-思維版)

### Python

```python
for x in a:
    print(x)
```

### C++

```cpp
#include <vector>
#include <iostream>
for (int x : a) {
    std::cout << x << '\n';
}
```

---

## 7. len() {#len}

### C++ header

* [`<vector>`](#header-vector)
* 🔙 [回到 Header 對照表](#16-c-標頭檔--功能總對照表python-思維版)

### Python

```python
len(a)
```

### C++

```cpp
a.size();
```

---

## 8. string {#string}

### C++ header

* [`<string>`](#header-string)
* 🔙 [回到 Header 對照表](#16-c-標頭檔--功能總對照表python-思維版)

### Python

```python
s = "abc"
s += "def"
```

### C++

```cpp
#include <string>
std::string s = "abc";
s += "def";
```

---

## 9. sort {#sort}

### C++ header

* [`<algorithm>`](#header-algorithm)
* [`<vector>`](#header-vector)
* 🔙 [回到 Header 對照表](#16-c-標頭檔--功能總對照表python-思維版)

### Python

```python
a.sort()
```

### C++

```cpp
#include <algorithm>
#include <vector>
std::sort(a.begin(), a.end());
```

---

## 10. max / min {#max-min}

### C++ header

* [`<algorithm>`](#header-algorithm)
* 🔙 [回到 Header 對照表](#16-c-標頭檔--功能總對照表python-思維版)

### Python

```python
max(a)
min(a)
```

### C++

```cpp
#include <algorithm>
std::max(x, y);
std::min(x, y);
```

---

## 11. math {#math}

### C++ header

* [`<cmath>`](#header-cmath)
* 🔙 [回到 Header 對照表](#16-c-標頭檔--功能總對照表python-思維版)

### Python

```python
import math
math.sqrt(4)
```

### C++

```cpp
#include <cmath>
std::sqrt(4);
```

---

## 12. file I/O {#file-io}

### C++ header

* [`<fstream>`](#header-fstream)
* 🔙 [回到 Header 對照表](#16-c-標頭檔--功能總對照表python-思維版)

### Python

```python
with open("a.txt") as f:
    data = f.read()
```

### C++

```cpp
#include <fstream>
#include <string>
std::ifstream f("a.txt");
std::string data;
```

---

## 13. random {#random}

### C++ header

* [`<random>`](#header-random)
* 🔙 [回到 Header 對照表](#16-c-標頭檔--功能總對照表python-思維版)

### Python

```python
import random
random.randint(1, 10)
```

### C++

```cpp
#include <random>
std::random_device rd;
std::mt19937 gen(rd());
std::uniform_int_distribution<> dis(1, 10);
int x = dis(gen);
```

---

## 14. time / sleep {#time-sleep}

### C++ header

* [`<chrono>`](#header-chrono)
* [`<thread>`](#header-thread)
* 🔙 [回到 Header 對照表](#16-c-標頭檔--功能總對照表python-思維版)

### Python

```python
import time
time.sleep(1)
```

### C++

```cpp
#include <thread>
#include <chrono>
std::this_thread::sleep_for(std::chrono::seconds(1));
```

---

## 15. assert {#assert}

### C++ header

* [`<cassert>`](#header-cassert)
* 🔙 [回到 Header 對照表](#16-c-標頭檔--功能總對照表python-思維版)

### Python

```python
assert x > 0
```

### C++

```cpp
#include <cassert>
assert(x > 0);
```

---

## 16. C++ 標頭檔 → 功能總對照表（Python 思維版）

| C++ header                                                        | 對應 Python 思維         | 核心解釋（最小必要知識）                         |
| ----------------------------------------------------------------- | -------------------- | ------------------------------------ |
| <span id="header-iostream">[`<iostream>`](#print)</span>          | `print`, `input`     | 提供 `std::cout / std::cin`，負責所有基本 I/O |
| <span id="header-string">[`<string>`](#string)</span>             | `str`                | `std::string`，自動管理記憶體的字串型別           |
| <span id="header-vector">[`<vector>`](#list)</span>               | `list`               | 動態陣列，支援 `push_back`、`size`           |
| <span id="header-map">[`<map>`](#dict)</span>                     | `dict`（有序）           | 紅黑樹實作，key 會排序                        |
| <span id="header-unordered-map">[`<unordered_map>`](#dict)</span> | `dict`（無序）           | Hash table，平均 O(1) 查找                |
| <span id="header-set">[`<set>`](#set)</span>                      | `set`                | 有序、不重複元素集合                           |
| <span id="header-algorithm">[`<algorithm>`](#sort)</span>         | `sort`, `max`, `min` | 與容器解耦的泛型演算法                          |
| <span id="header-numeric">[`<numeric>`](#max-min)</span>          | `sum`                | `accumulate`、數值型演算法                  |
| <span id="header-cmath">[`<cmath>`](#math)</span>                 | `math`               | 數學函式（sqrt, pow, abs）                 |
| <span id="header-fstream">[`<fstream>`](#file-io)</span>          | `open()`             | 檔案 I/O                               |
| <span id="header-chrono">[`<chrono>`](#time-sleep)</span>         | `time`               | 型別安全的時間系統                            |
| <span id="header-thread">[`<thread>`](#time-sleep)</span>         | `sleep`, threading   | thread 與 sleep_for                   |
| <span id="header-cassert">[`<cassert>`](#assert)</span>           | `assert`             | 偵錯期條件檢查                              |

---
