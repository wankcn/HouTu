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

**为什么main()不能使用其他名称？**

C++程序必须包含一个main()函数。运行C++程序的时候，通常从main()函数开始执行，当程序里面只有一个函数的时候，这个函数必须承担main的责任。如果没有main，程序不完整。

### 1.2 注释

```
// 注释
/* 注释 */
```

注释用来说明程序，程序越复杂，注释价值越大。

### 1.3 预处理器和iostream文件

C++使用预处理器在程序进行主编译之前对源文件进行处理，在编译程序时自动执行。

```c++
#include <iostream>
using namespace std;
```

**#include**编译指令使预处理器将iostream文件的内容添加到程序中。在源代码被编译前，替换或添加文本。

**为什么要iostream文件中的内容添加到程序中？**

#include编译指令导致iostream中的内容和源代码里的内容一起发送给编译器。iostream文件的内容将取代`#include <iostream>`这行代码。原始文件并没有被修改，而是将源代码文件和iostream文件组合成一个复合文件。编译的下一阶段使用这一文件。

使用cin和cout进行输入输出必须包含iostream文件。



