# C++ Primer Plus Notes

重学C++！《C++ Primer Plus》的读书笔记。

[toc]

## 1. HelloWorld

C++对大小写敏感，<font color = "red">区分</font>大写字符和小写字符

```c++
// 第一个C++程序
#include<iostream>
int main()
{
    using namespace std;
    cout << "c++ hello world!";
    cout << endl;
    cout << "My first Cpp!" << endl;
    return 0;
}
```

`#include` 预处理编译指令

`int main()`函数头

`using namesoace`编译指令

`{}`函数体

`cout`打印函数

`return`返回语句，结束函数

### 1.1 main()函数

**语句和分号：** 编译器需要知道一条语句何时结束，另一条语句何时开始。终止符是一个分号，它是语句的结束标记，是语句的组成部分。

**作为接口的函数头**

1.   函数头描述函数与调用它的函数之间的接口，<font color = "red">main()函数被启动代码调用</font>，描述main()函数和操作系统之间的接口。

2.   在c++中，`int main()`和`int main(void)`等效。

3.   如果编译器到达main()函数末尾时没有遇到返回语句，默认有一条return 0；这条语句只适用于main()函数。

**C++程序必须包含一个main()函数**

### 1.2 注释

```
// 注释
/* 注释 */
```

注释用来说明程序，程序越复杂，注释价值越大。

### 1.3 预处理器和iostream文件

