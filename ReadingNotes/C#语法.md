# C#语法

[toc]

## 1 语法入门

### 1.1 控制台输入打印基础语句

```c#
Console.WriteLine("Hello World!");  // 结束换行
Console.Write("xxxxxxxx");          // 结束不换行
Console.ReadLine();                 // 输入直到回车结束
Console.ReadKey();                  // 检测是否有输入，按任意键结束
```

**习题：** 输入用户名、年龄、班级

### 1.2 变量

**折叠代码** 

```c#
#region 折叠代码
#endregion
```

**C#中的14种变量**

1.   有符号整型变量。 `sbyte`（-128～127），` int`（-21亿～21亿多），` short`（-32768～32767），` long`（-9百万兆～9百万兆）
2.   无符号整型变量。`byte`（0～255），`uint`（0～42亿多），`ushort`（0～65535），`ulong`，（0～18百万兆）
3.   浮点数 `float`（存储7/8位有效数字，不计入0，多余四舍五入，后面加f/F），`double`（存储15～17位有效数字），`decimal`（存储27～28位的有效数字，不建议使用，后面加m/M）
4.   特殊类型。 `bool`，`char`，`string`

变量的本质是二进制

### 1.3 常量

```c#
const byte age = 18;
```

1.   必须初始化
2.   不能被修改
3.   用来声明常用的不变的变量

应用：数学计算常量，角度转弧度，弧度转角度，重力加速度 / 游戏中玩家血量极值等。

### 1.4 转义字符

**\加字符**

```c#
string str = "\'";        // 单引号
string str = "\"";        // 双引号
string str = "\n";        // 换行
string str = "\\";        // 斜杠  
string str = "\t";        // 制表符
string str = "\b";        // 光标退格
string str = "\0";        // 空字符
string str = "\a";        // 警告音
```

**取消转义字符** 前面加@

```c#
string str = @"https://www.baidu.com/";   
```

### 1.5 类型转换

不同变量之间的相互转换

**隐私转换**，不同类型之间相互转换，大范围装小范围





