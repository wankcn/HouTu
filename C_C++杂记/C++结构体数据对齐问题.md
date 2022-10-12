内存分布是4个字节连续，即32位连续。**`遵循缺省对齐的原则`**

### 32位CPU
char：任何地址
short：偶数地址
int：4的整数倍地址
double：8的整数倍地址

```cpp
int main() {
    struct MyStruct {
        char a[12];
        double x;
        int b;
    };

    cout << sizeof(MyStruct) << endl;
    return 0;
}
```
输出的应该是`32`，char占12，填充4使它是8的倍数，int需要填充4变为8的倍数。
```cpp
int main() {
    struct MyStruct {
        char a[12];
        int b;
        double x;
    };

    cout << sizeof(MyStruct) << endl;
    return 0;
}
```
更换double和int的位置，char占12和int的4补满8的倍数16，double占8，所以是`16+8=24`。

```cpp
struct MyStruct {
    char a[13];
    int b;
    double x;
};
```
如果char字符大小改为char a[13]; `char补3，int补4，结果为32`

### 修改默认编译原则
使得占用内存是连续在一块的
vc++:
```cpp
# pragma pack(1)  // 说明内存分布以1为单位
```
g++:
```cpp
_attribute_(aligned(n))
_attribute_(_packed_)
```

### 注意⚠️
如果没有编译选项的话，考虑内存布局问题，尽量把小的字节元素放在一起，如果分开放的话，两边都需要扩充大小，空间会很浪费。