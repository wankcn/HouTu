### *sizeof()* 
返回变量的大小，sizeof(a) 返回4 a为整型

### Condition?X:Z
三目运算符，条件为真X，否则Y

### ,
逗号运算符，执行一系列运算，最终的返回值是逗号最后一个表达式的值

### .（点）和->（箭头）
成员运算符，用于引用类、结构和共用体的成员

### Cast
强制类型转换 int(2.2000) 返回2

### &和*
指针运算符，&a返回变量的实际地址
*a指向一个变量a

### 测试用例

```cpp
int A = 10, B = 20;
cout << sizeof(A) << endl;
int C = A > B ? 1 : 0;
cout << C << endl;
int D = A < B ? 1 : 0;
cout << D << endl;
int E = (A, B, C);
cout << E << endl;
float F = float(E);
cout << F << endl;
cout << &F << endl;
float *P = &F;
cout << P << endl;
cout << *P << endl;
```
```
4
0
1
0
0
0x7ffee77c29d4
0x7ffee77c29d4
0
```