Vector是`面向对象方式的动态数组`，可以实现自动扩容

*size();* // 元素个数
*capacity();* // 容积大小
*push_back();* // 末尾添加，空间不够扩容，删除元素但不会缩容 
*end()-1;*// 指向末尾，end()应用时-1
*begin();* // 指向数组头部
*insert();* // 插入元素
*pop_back();* // 末尾删除一个元素
*vec.erase()；*// 指定位置删除

```cpp
#include <vector>

vector<int> vec = {1, 2, 3, 4};
cout << "begin size is: " << vec.size() << endl;
cout << "begin capacity is: " << vec.size() << endl;

vec.push_back(5);
vecForeach(vec);
cout << endl << "now size is: " << vec.size();
cout << endl << "now capacity is: " << vec.capacity() << endl;

// 插入一个元素
vec.insert(vec.begin(), 0);
vecForeach(vec);

// 从尾部删除元素
vec.pop_back();
// 指定位置删除元素
vec.erase(vec.begin());
vecForeach(vec);
vec.erase(vec.begin() + 1); // 1，3，4
vec.erase(vec.end() - 1);
vecForeach(vec);
cout << endl << "now size is: " << vec.size();
cout << endl << "now capacity is: " << vec.capacity() << endl;
```
进行了2倍扩容，但并没有缩容。
```
begin size is: 4
begin capacity is: 4
1 2 3 4 5 

now size is: 5
now capacity is: 8
0 1 2 3 4 5 
1 2 3 4 
1 3 

now size is: 2
now capacity is: 8

```