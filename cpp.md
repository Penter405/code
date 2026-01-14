# C++ 對應 Python 常用功能所需 `#include`

這份文件的目標是：

> **把 Python 常見功能，對應到 C++ 需要 #include 什麼，以及基本用法方向**。

---

## 1. print / 輸出 {#func-print}

### C++ header

* [`<iostream>`](#header-iostream)
* 🔙 [回到 Header 對照表](#cpp-headers-table)

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

## 2. input / 輸入 {#func-input}

### C++ header

* [`<iostream>`](#header-iostream)
* [`<string>`](#header-string)
* 🔙 [回到 Header 對照表](#cpp-headers-table)

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

## 3. list / 動態陣列 {#func-list}

### C++ header

* [`<vector>`](#header-vector)
* 🔙 [回到 Header 對照表](#cpp-headers-table)

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

## 4. dict / key-value {#func-dict}

### C++ header

* [`<map>`](#header-map)
* [`<unordered_map>`](#header-unordered-map)
* 🔙 [回到 Header 對照表](#cpp-headers-table)

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

## 5. set {#func-set}

### C++ header

* [`<set>`](#header-set)
* [`<unordered_set>`](#header-unordered-set)
* 🔙 [回到 Header 對照表](#cpp-headers-table)

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

## 6. for loop / iterable {#func-for-loop}

### C++ header

* [`<vector>`](#header-vector)
* [`<iostream>`](#header-iostream)
* 🔙 [回到 Header 對照表](#cpp-headers-table)

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

## 7. len() {#func-len}

### C++ header

* [`<vector>`](#header-vector)
* 🔙 [回到 Header 對照表](#cpp-headers-table)

### Python

```python
len(a)
```

### C++

```cpp
a.size();
```

---

## 8. string {#func-string}

### C++ header

* [`<string>`](#header-string)
* 🔙 [回到 Header 對照表](#cpp-headers-table)

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

## 9. sort {#func-sort}

### C++ header

* [`<algorithm>`](#header-algorithm)
* [`<vector>`](#header-vector)
* 🔙 [回到 Header 對照表](#cpp-headers-table)

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

## 10. max / min {#func-max-min}

### C++ header

* [`<algorithm>`](#header-algorithm)
* 🔙 [回到 Header 對照表](#cpp-headers-table)

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

## 11. math {#func-math}

### C++ header

* [`<cmath>`](#header-cmath)
* 🔙 [回到 Header 對照表](#cpp-headers-table)

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

## 12. file I/O {#func-file-io}

### C++ header

* [`<fstream>`](#header-fstream)
* 🔙 [回到 Header 對照表](#cpp-headers-table)

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

## 13. random {#func-random}

### C++ header

* [`<random>`](#header-random)
* 🔙 [回到 Header 對照表](#cpp-headers-table)

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

## 14. time / sleep {#func-time-sleep}

### C++ header

* [`<chrono>`](#header-chrono)
* [`<thread>`](#header-thread)
* 🔙 [回到 Header 對照表](#cpp-headers-table)

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

## 15. assert {#func-assert}

### C++ header

* [`<cassert>`](#header-cassert)
* 🔙 [回到 Header 對照表](#cpp-headers-table)

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

## 16. C++ 標頭檔 → 功能總對照表（Python 思維版） {#cpp-headers-table}

| C++ header                                 | 對應 Python 思維         | 核心解釋（最小必要知識）                         |
| ------------------------------------------ | -------------------- | ------------------------------------ |
| [`<iostream>`](#header-iostream)           | `print`, `input`     | 提供 `std::cout / std::cin`，負責所有基本 I/O |
| [`<string>`](#header-string)               | `str`                | `std::string`，自動管理記憶體的字串型別           |
| [`<vector>`](#header-vector)               | `list`               | 動態陣列，支援 `push_back`、`size`           |
| [`<map>`](#header-map)                     | `dict`（有序）           | 紅黑樹實作，key 會排序                        |
| [`<unordered_map>`](#header-unordered-map) | `dict`（無序）           | Hash table，平均 O(1) 查找                |
| [`<set>`](#header-set)                     | `set`                | 有序、不重複元素集合                           |
| [`<unordered_set>`](#header-unordered-set) | `set`                | 無序集合，Hash table 基礎                   |
| [`<algorithm>`](#header-algorithm)         | `sort`, `max`, `min` | 與容器解耦的泛型演算法                          |
| [`<numeric>`](#header-numeric)             | `sum`                | `accumulate`、數值型演算法                  |
| [`<cmath>`](#header-cmath)                 | `math`               | 數學函式（sqrt, pow, abs）                 |
| [`<fstream>`](#header-fstream)             | `open()`             | 檔案 I/O                               |
| [`<chrono>`](#header-chrono)               | `time`               | 型別安全的時間系統                            |
| [`<thread>`](#header-thread)               | `sleep`, threading   | thread 與 sleep_for                   |
| [`<cassert>`](#header-cassert)             | `assert`             | 偵錯期條件檢查                              |

---
