# C#文档
[toc]
#### 多线程

```c#
Thread t = new Thread(FunName); // 传入执行逻辑的方法名
t.Start();             // 启动
t.IsBackground = true; // 设置为后台线程

// 通过标识结束线程死循环
private isRunning = true;
isRunning = false;    // 死循环while(isRunning)停止

t.Abort(); //终止线程 
t = null; // 释放

Thread.Sleep() // 让线程休眠多少毫秒，在哪个线程里执行，就休眠哪个线程 

// 多线程中访问同一块内存进行逻辑处理，避免逻辑顺序差错
lock(){} // lock(引用对象)
```

#### 预处理指令

```c#
// 编译器在实际编译开始之前对信息进行预处理
// 都是以#开始
// 不是语句不以；结束

#define  // 写在脚本文件最前面
#undef   // 取消定义一个符号
#if #elif #else #endif
#warring // 警告
#error   // 错误
```

#### 反射

概念

```c#
// 程序正在运行时，可以查看其他程序集或者自身的元数据。
// 一个运行的程序查看本身或者其他程序的元数据的行为叫做反射
// 程序运行时，通过反射可以得到其他程序集或者自己程序集代码的各种信息
```

**Type** 

```c#
// 类的信息类，反射功能的基础，访问元数据的主要方式
// 使用Type的成员获取有关类型声明的信息
```

三种获取Type的方式

```c#
int n = 0;
Type type = n.GetType();
Type type2 = typeof(int);
// 类名字获取类型 类名必须包含命名空间
Type type3 = Type.GetType("System.Int32"); 

// 上面三种获取Type的方式都指向堆中同一块内存地址
type.Assembly; // 得到类的程序集信息
```

获取类中的所有公共成员

```c#
// 使用前使用命名空间
using System.Reflection;
Type t = typeof(Test);
MemberInfo[] infos = t.GetMembers();
```

获取类的公共构造函数并调用

```c#
ConstructInfo[] ctors = t.GetConsturctors();
```

获取其中一个构造函数并执行

```c#
// 得到构造函数传入 Type数组   数组中内容按顺序是参数类型
// 执行构造函数传入 object数组 表示按顺序传入的参数

// 得到无参构造
ConstructInfo info = t.GetConstructor(new Type[0]);
// 执行 无参数传null info.Invoke(null); 
Test obj = info.Invoke(null) as Test; 

// 得到有参构造
ConstructInfo info2 = t.GetConstructor(new Type[]{typeof(int)});
obj = info2.Invoke(new object[]{2}) as Test;
```

获取类的公共成员变量

```c#
FieldInfo[] fields = t.GetFields();
FieldInfo info = t.GetField("str");  // str是一个变量名
```

通过反射获取和设置对象的值

```c#
info.GetValue(test);     // test是一个对象
info.SetValue(test,100)  // 传入对象和值
```

获得类的公共成员方法

```c#
Type strType = typeof(string);
MethodInfo[] methods = strType.GetMethods();
// 获得截取字符串的方法
MethodInfo subStr = strType.GetMethod("Substring",
                                      new Type[]{typeof(int),typeof(int)});
// 如果是静态方法，Invoke中的第一个参数传null
string str = "Hello World!";
// 第一个参数相当于是哪个对象执行这个成员方法
subStr.Invoke(str,new object[]{5,7}); // 从5的位置开始截取7个
```

