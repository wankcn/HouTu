### C++四种常用智能指针
1. unique_ptr（局限性较大）
2. shared_ptr 和weak_ptr经常联合在一起用
3. weak_ptr
4. auto_ptr(C++11已经废弃，C++17中正是删除) deprecated 目前还能用，不久的将来将不支持。

### 从应用方面来分析智能指针
1. 应用场景（A. 对象所有权 B. 生命周期）
2. 性能分析


#### 1. auto_ptr
比较简单比较直接的做法，其实就是指针指向了某一个对象，也可以指向最基本的数据类型。
如果是在堆中产生，如果把指针本身销毁的时候，指针所指的对象也会被自动销毁掉。也就是说在auto_ptr对象销毁时，他所管理的对象也会被自动delete掉，他与对象的关联度较高。

**所有权转移**： 不小心把它传递给另外的智能指针，原来的指针就不再拥有这个对象了。在拷贝/赋值的过程中，会直接剥夺指针对原对象对内存的控制权，转交给新对象，然后再将原对象指针设置为nullptr。

堆中new对象，指针销毁时，对象本身失效；auto_ptr在其他对方对对象做操作的时候会让所有权发生转移。导致对象在被指针引用的时候产生诡异的现象，或者非常难以管理。如果一个程序员正在使用对象，另一个程序员不小心通过auto_ptr访问了这个对象，会导致原来程序员工作出现问题。引起管理混乱。有很大的安全隐患。

release用一个临时指针保存当前指针的对象，然后将当前指针置为0，将临时指针返回
reset 当前指针是否为空，不为空先释放，释放之后把临时指针穿进去。
操作动作很大，让度权没处理好会导致一系列内存问题。

```cpp
int main()
{
    {// 确定auto_ptr失效的范围
        // 对int使用
        auto_ptr<int> pI(new int(10));
        cout << *pI << endl;                // 10

        // auto_ptr	C++ 17中移除	拥有严格对象所有权语义的智能指针
        // auto_ptr原理：在拷贝 / 赋值过程中，直接剥夺原对象对内存的控制权，转交给新对象，
        // 然后再将原对象指针置为nullptr（早期：NULL）。这种做法也叫管理权转移。
        // 他的缺点不言而喻，当我们再次去访问原对象时，程序就会报错，所以auto_ptr可以说实现的不好，
        // 很多企业在其库内也是要求不准使用auto_ptr。
        auto_ptr<string> languages[5] = {
            auto_ptr<string>(new string("C")),
            auto_ptr<string>(new string("Java")),
            auto_ptr<string>(new string("C++")),
            auto_ptr<string>(new string("Python")),
            auto_ptr<string>(new string("Rust"))
        };
        cout << "There are some computer languages here first time: \n";
        for (int i = 0; i < 5; ++i)
        {
            cout << *languages[i] << endl;
        }
        auto_ptr<string> pC;
        pC = languages[2]; // languges[2] loses ownership. 将所有权从languges[2]转让给pC，
        //此时languges[2]不再引用该字符串从而变成空指针
        cout << "There are some computer languages here second time: \n";
        for (int i = 0; i < 2; ++i)
        {
            cout << *languages[i] << endl;
        }
        cout << "The winner is " << *pC << endl;
        //cout << "There are some computer languages here third time: \n";
        //for (int i = 0; i < 5; ++i)
        //{
        //	cout << *languages[i] << endl;
        //}
    }
    return 0;
}
```

```
10
There are some computer languages here first time: 
C
Java
C++
Python
Rust
There are some computer languages here second time: 
C
Java
The winner is C++
```

#### 2.unique_ptr
unique_ptr是专属所有权，它管理的内存，只能被一个对象所持有，不能赋值和复制。
移动语义：unique_ptr禁止了拷贝语义，有时候需要转移所有权，使用std::move();进行转移，原来的指针置为nullptr。

make_unique()最终会返回一个unique_ptr的指针。
```cpp
int main()
{
	// 在这个范围之外，unique_ptr被释放
	{
		auto i = unique_ptr<int>(new int(10));
		cout << *i << endl;
	}

	// unique_ptr
	// auto自动检测类型
	auto w = std::make_unique<int>(10);
	cout << *(w.get()) << endl;  // 10 get返回一个指针
	//auto w2 = w; // 编译错误，无法w复制给w2
	//  因为复制从语义上来说，两个对象将共享同一块内存。

	// unique_ptr 只支持移动语义, 即如下
	auto w2 = std::move(w); // w2 获得内存所有权，w 此时等于 nullptr
	cout << ((w.get() != nullptr) ? (*w.get()) : -1) << endl;  // -1 w已经转移为空
	cout << ((w2.get() != nullptr) ? (*w2.get()) : -1) << endl;  // 10
    return 0;
}
```
```
10
10
-1
10
```

**上述两种智能指针有一个缺陷，因为所有权的问题，在同一时刻，只能有一个智能指针指某一个分配对象。**

#### 3. shared_ptr
是一个可以共享同一个对象的指针。多个shared_ptr可以访问同一个对象，使用`引用计数`（当有一个智能指针去使用对象的时候，通过引用计数+1），某一时刻，shared_ptr不再访问对象了，引用计数-1。

shared_ptr是为了解决auto_ptr包括unique_ptr在对象所有权上的局限性。由于使用了引用计数机制，所以需要额外开销。
当引用计数为0，对象没有任何指针使用，可以把它析构掉。

**引用计数带来的副作用** `循环引用问题`
A对象的指针指向B对象，B对象的指针指向了A对象。两个指针相互指向。`造成堆里的内存无法正常回收，造成内存泄漏。`

为了避免循环引用问题，STL提供weak_ptr。

```cpp
#include <iostream>
#include <memory>
using namespace std;
int main()
{
	//// shared_ptr 基本使用
	//{
	//	//shared_ptr 代表的是共享所有权，即多个 shared_ptr 可以共享同一块内存。
	//	auto wA = shared_ptr<int>(new int(20));
	//	{
	//		auto wA2 = wA;
	//		cout << ((wA2.get() != nullptr) ? (*wA2.get()) : -1) << endl;       // 20
	//		cout << ((wA.get() != nullptr) ? (*wA.get()) : -1) << endl;           // 20
	//		cout << wA2.use_count() << endl;                                              // 2
	//		cout << wA.use_count() << endl;                                                // 2
	//	}
	//	//cout << wA2.use_count() << endl;                                               
	//	cout << wA.use_count() << endl;                                                    // 1
	//	cout << ((wA.get() != nullptr) ? (*wA.get()) : -1) << endl;               // 20
	//	//shared_ptr 内部是利用引用计数来实现内存的自动管理，每当复制一个 shared_ptr，
	//	//	引用计数会 + 1。当一个 shared_ptr 离开作用域时，引用计数会 - 1。
	//	//	当引用计数为 0 的时候，则 delete 内存。
	//}

	// move 语法
	auto wAA = std::make_shared<int>(30);
	auto wAA2 = std::move(wAA); // 此时 wAA 等于 nullptr，wAA2.use_count() 等于 1
	cout << ((wAA.get() != nullptr) ? (*wAA.get()) : -1) << endl;          // -1
	cout << ((wAA2.get() != nullptr) ? (*wAA2.get()) : -1) << endl;      // 30
	cout << wAA.use_count() << endl;                                                  // 0
	cout << wAA2.use_count() << endl;                                                // 1
	//将 wAA 对象 move 给 wAA2，意味着 wAA 放弃了对内存的所有权和管理，此时 wAA对象等于 nullptr。
	//而 wAA2 获得了对象所有权，但因为此时 wAA 已不再持有对象，因此 wAA2 的引用计数为 1。

    return 0;
}
```
```
-1
30
0
1
```
#### 4.weak_ptr
被设计为与shared_ptr共同工作，用一种观察者模式工作。

作用是协助shared_ptr，可以获得资源的观测权。像旁观者那样观测资源的使用情况。
weak_ptr只对shared_ptr进行引用，而不改变它的引用计数，当被观察的shared_ptr失效后，相应的weak_ptr也跟着失效。

```cpp
// 产生对象就会产生循环引用问题
struct B;
struct A {
	shared_ptr<B> pb;
	~A()
	{
		cout << "~A()" << endl;
	}
};
struct B {
	shared_ptr<A> pa;
	~B()
	{
		cout << "~B()" << endl;
	}
};

// pa 和 pb 存在着循环引用，根据 shared_ptr 引用计数的原理，pa 和 pb 都无法被正常的释放。
// weak_ptr 是为了解决 shared_ptr 双向引用的问题。
struct BW;
struct AW
{
	shared_ptr<BW> pb;
	~AW()
	{
		cout << "~AW()" << endl;
	}
};
struct BW
{
	weak_ptr<AW> pa;
	~BW()
	{
		cout << "~BW()" << endl;
	}
};

void Test()
{
	cout << "Test shared_ptr and shared_ptr:  " << endl;
	shared_ptr<A> tA(new A());                                         // 1
	shared_ptr<B> tB(new B());                                         // 1
	cout << tA.use_count() << endl;
	cout << tB.use_count() << endl;
	tA->pb = tB;
	tB->pa = tA;
	cout << tA.use_count() << endl;                                    // 2
	cout << tB.use_count() << endl;                                    // 2
}
void Test2()
{
	cout << "Test weak_ptr and shared_ptr:  " << endl;
	shared_ptr<AW> tA(new AW());
	shared_ptr<BW> tB(new BW());
	cout << tA.use_count() << endl;                                     // 1
	cout << tB.use_count() << endl;                                     // 1
	tA->pb = tB;
	tB->pa = tA;
	cout << tA.use_count() << endl;                                     // 1
	cout << tB.use_count() << endl;                                     // 2
}

int main()
{
	Test();
	Test2();
    return 0;
}

```

```
Test shared_ptr and shared_ptr:  
1
1
2
2
Test weak_ptr and shared_ptr:  
1
1
1
2
~AW()
~BW()

```