# C++Mooc学习笔记

[toc]

## 1. 基础数据类型

### 1.1 数据类型转换

**显示转换（强制转换）**

```c++
#include<iostream>
using namespace std;
int main()
{
    int a = 5;
    short b = (short)a;
    cout << a;
    return 0;
}
```

**隐式转换**

```c++
#include<iostream>
using namespace std;
int main()
{
    short c = 5;
    int d = c;
    cout << d;
    return 0;
}
```

**隐式转换遵守推演表**

<div><img src="imgs/image-c++01.png"></div>

### 1.2 算术运算符

```c++
#include<iostream>
using namespace std;
int main()
{
    int a = 10;
    int b = 5;
    float c = 5;
    cout << "a+b:" << a+b << endl;
    cout << "a-b:" << a-b << endl;
    cout << "a/b:" << a/b << endl;
    cout << "a/c:" << a/c << endl;
    cout << "a%b:" << a%b << endl;
    return 0;
}
```

### 1.3 赋值运算符

```c++
#include<iostream>
using namespace std;

int main()
{
    int a = 1;
    int b = 2;
    int c = a;
    a = b;
    b = c;
    cout << a << endl << b;
}
```

### 1.4 关系运算符

```c++
#include<iostream>
using namespace std;

int main()
{
    int a = 1; 
    int b = 2;
    
    cout << "a>b:" << (a > b) << endl;  // 0
    cout << "a>b:" << (a < b) << endl;  // 1
    cout << "a>=b:" << (a>=b) << endl;  // 0
    cout << "a<=b:" << (a<=b) << endl;  // 1
    cout << "a==b:" << (a==b) << endl;  // 0
    cout << "a!=b:" << (a!=b) << endl;  // 1
    
    return 0;
}
```

### 1.5 逻辑运算符

**逻辑与** `bool c = a && b;`

|   a   |   b   |   c   |
| :---: | :---: | :---: |
| true  | true  | true  |
| true  | false | false |
| false | true  | false |
| false | false | false |

**逻辑或 ** `bool c = a||b`

|   a   |   b   |   c   |
| :---: | :---: | :---: |
| true  | true  | true  |
| true  | false | true  |
| false | true  | true  |
| false | false | false |

**逻辑非** 

|   a   |  !a   |
| :---: | :---: |
| true  | false |
| false | true  |

## 2. 复合类型

### 2.1 数组

```c++
#include<iostream>
using namespace std;
int main()
{
    int a[] ={0,1,2,3,4};
    float b[6] = {1,2,4};
    for(int i = 0;i<=4;i++)
    {
        cout << a[i]<<"\t"<< b[i]<<endl;;
    }
}
```

### 2.2 结构体

```c++
#include<iostream>
using namespace std;

struct Student
{
    int math = 0;
    float english = 0.0f;
};

int main()
{
    struct Student stu[5];

    stu[2].math = 88;
    stu[2].english = 44;
    stu[8].math = 100;           // 特别注意！！！索引越界不会报错
    stu[8].english = 99.2;       // 特别注意！！！索引越界不会报错

    for(int i = 0;i<= 8;i++)
    {
        cout << i << ":" << stu[i].math << "/"
        << stu[i].english << endl;
    }
  
    return 0;
}


```

### 2.3 枚举

```c++
#include<iostream>
using namespace std;

enum Week
{
    Plac,Mon,Tue,Wed,Thu,Fri,Sat,Sun
};

int main()
{
    Week week = Week::Fri;
    cout << week;
    return 0;
}
```

