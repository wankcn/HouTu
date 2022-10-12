### 1.一般类型指针 T*
```cpp
int i = 1;int *iP = &i;cout << *iP << endl;
double d = 13.14;double *dP = &d;cout << *dP << endl;
char c = 'a';char *cP = &c;cout << *cP << endl;
```
```
1
13.14
a
```
### 2.指针的数组T* t[ ]
是一个数组，每一个值都是指针,多个指针 int* a[4]

### 3.数组的指针T(*t) []
有一个指针指向一个数组 int *a[] 

### 4.const pointer 与pointer to const
```cpp
// const pointer 与 pointer to const
char strHelloWorld[] = {"helloWorld"};
char const *pStr1 = "helloWorld";  // const修饰左侧的char
char *const pStr2 = "helloWorld";
char const *const pStr3 = "helloWorld";

pStr1 = strHelloWorld;
//    pStr2 = strHelloWorld;  // pStr2不可改
//    pStr3 = strHelloWorld;  // pStr3不可改
```
**关于const修饰符**
1. 看左侧最近的部分；
2. 如果左侧没有，则看右侧

`char const *pStr1 = "helloWorld"; `  // const修饰左侧的char，*pStr指针指向允许改变，但是它指向的空间里的内容不允许改变。

`char *const pStr2 = "helloWorld";`  // const左侧*，它修饰的是指针，pStr2一旦指向了 “helloWorld”内存空间，const的指针pStr2指向不允许发生变化。

`char const *const pStr3 = "helloWorld";`  // const左侧有指针和char，说明pStr3指向的地址和指向的空间中的内容都不允许改变。

### 5.指向指针的指针
```cpp
int a = 97;
int *b = &a;
int **c = &b; // 二级指针
```

*指针操作符具有从左向右的结合性

**表达式相当于` * (*c)`，必须从里向外逐层求值

*c得到的是c指向的位置，即b，得到值是定义完引用的时候得到结果

` * (*c)`相当于*b，得到a的值


### 6.未初始化和非法指针

```cpp
int *a;
*a = 12;
```
a定位到非法地址，程序出错终止。
最坏的情况：a定位到一个可以访问的地址并无意修改了它，无法定位错误。

**`用指针进行间接访问前，确保它已经初始化并被恰当的赋值`**

### 7.NULL指针
一个特殊的指针变量，表示不指向任何东西的一种状态。`int *a = NULL;` 比如有一个指针不准备使用了，为初始化时，让它指向NULL。
不知道一开始赋值定义为NULL，不产生副作用。
在对一个指针间接引用前，判断指针是否为NULL

```cpp
int a = 97;
int *pA = NULL;
pA = &a;
if (pA != NULL) // 判断
    cout << *pA << endl;
pA = NULL; // 不使用设置为NULL
```

### 8.杜绝野指针
指向“垃圾”内存的指针，if判断对他们没有作用，因为没有设置NULL。

**野指针一般有三种情况**
1. 指针变量没有初始化
2. 已经释放的指针没有设置NULL，delete和free之后的指针
3. 指针操作超越了变量的作用范围

**`未初始化、不使用的或者超出范围的指针设置为NULL`**