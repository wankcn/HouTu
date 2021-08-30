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

**隐私转换**

1.   不同类型之间相互转换，大范围装小范围，比如无符号数：long->int->short->sbyte。

2.   decimal没有办法隐式转换double和float，但是可以装整形
3.   只要范围涵盖那个数就可以装
4.   浮点数可以装载任何类型整数
5.   char可以隐式转换成浮点型和整型，是一个ASCII码
6.   string无法转换

**显示转换**

1.   括号强转用于高精度转低精度。可能出现范围问题，浮点数注意精度问题

2.    把字符串类型转换成对应类型，使用Parse，且字符串可以必须转换成对应的类型，遵守变量范围

     ```c#
     int temp = int.Parse("123");
     Console.WriteLine(temp);
     ```

3.   Convert更准确的讲各种类型之间相互转换。Convert.To目标类型进行转换

     ```c#
     sbyte temp1 = Convert.ToSByte("1");
     short temp2 = Convert.ToInt16("1");
     int temp3 = Convert.ToInt32("1");
     long temp4 = Convert.ToInt64("1");
     
     byte temp5 = Convert.ToByte("1");
     ushort temp6 = Convert.ToUInt16("1");
     uint temp7 = Convert.ToUInt32("1");
     ulong temp8 = Convert.ToUInt64("1");
     
     float temp9 = Convert.ToSingle("1.1");
     double temp10 = Convert.ToDouble("1.1");
     decimal temp11 = Convert.ToDecimal("1.1");
     
     bool b = Convert.ToBoolean("true");
     char c = Convert.ToChar("A");
     string str = Convert.ToString(123);
     ```

     精度可以四舍五入。每个类型都存在对应的Convert方法

4.   其他类型转string，使用.ToString()


### 1.6 异常捕获
作用：避免代码错误造成程序卡死

```c#
try
{
    string str = Console.ReadLine();
    Console.WriteLine(int.Parse(str));
}
catch (Exception e)
{
    Console.WriteLine("输入非法！");
}
```

### 1.7 运算符

1.   赋值符号 = 
2.   算术运算符 +，-，*，/，% 乘除取余再加减
3.   符合运算符 +=，-=，*=，/=，%=
4.   自增自减 ++，--
5.   条件运算符
