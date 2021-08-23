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

### 1.3 



