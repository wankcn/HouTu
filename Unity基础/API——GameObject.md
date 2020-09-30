# 场景、游戏物体、组件的关系
一个游戏由多个场景组成，同理，一个场景由多个游戏物体组成，一个游戏物体由多个组件组成。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200930154034388.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dhbmtjbg==,size_16,color_FFFFFF,t_70#pic_center)

在unity中操作资源，预制体等所有类的共同基类是UnityEngine.Object，在C#中的共同基类是System.Object。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200930154645424.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dhbmtjbg==,size_16,color_FFFFFF,t_70#pic_center)
戏物体是由多个组件组成的，但是GameObject和Component都继承自UnityEngine同一个类，这是因为他们存在一些相同的变量和方法。

在API文档里GameObject继承的成员如下图：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200930155627205.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dhbmtjbg==,size_16,color_FFFFFF,t_70#pic_center)
# 共有的游戏变量与方法
## 1.name
`GameObject的名字是继承来的，它是UnityEngine里的成员`。通过GameObject获取的名字就是游戏物体的名字。
通过组件获取的名字不是组件名，因为它只有类名。获取到的是组件所在游戏物体的名字。即`GameObject和Componet.name获取到的是同一个值`。

组件继承自Object，所以Object有的成员组件都有。
```csharp
public GameObject go;
void Start()
{
    Debug.Log(go.name);
    Debug.Log(go.GetComponent<Transform>().name);
}
```
![在这里插入图片描述](https://img-blog.csdnimg.cn/2020093016113183.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dhbmtjbg==,size_16,color_FFFFFF,t_70#pic_center)
如上图都输出了游戏物体名字。

## 2.Destroy / DestroyImmediate
DestroyImmediate会立刻把游戏物体在场景中删除，可能会导致空指针。

Destroy是静态方法，需要通过类名进行调用。既可以销毁游戏物体，也可以销毁游戏组件。调用Destroy不会立即销毁，但是调用后游戏物体在场景当中不存在，但是它还没有被立刻回收，Unity会把需要进行销毁的游戏物体统一进行管理放在垃圾池里，确保游戏物体没有使用，再将它进行销毁。
销毁某个组件，指将游戏物体的某一组件进行移除，其他组件不受影响。销毁某一游戏物体的时候可以指定int类型的时间，`Destroy(gameObject, 5);`

## 3.DontDestroyOnLoad
DontDestroyOnLoad需要传递一个游戏物体如`DontDestroyOnLoad(this.gameObject);`它指的是不要销毁游戏物体。一般情况下，由A场景跳转到B场景的话，A场景中所有的游戏物体都会被销毁，然后加载B场景中的东西。如果在A场景中某一游戏物体调用了DontDestroyOnLoad()，那么这一游戏物体不会在场景跳转的时候被销毁，它会带到下一个场景里。即在场景切换的时候这一游戏物体始终存在，除非退出游戏它才会被销毁。

DontDestroyOnLoad可以用来设置某一个共享的游戏物体。

## 4.FindObjectOfType / FindObjectsOfType
**FindObjectOfType**根据组件的类型去查找组件，Find会从全局去搜索场景当中所有的游戏物体身上所有的组件，找到符合Type类型的组件。它的返回值只有一个，所以当找到符合条件的第一个组件的时候就会返回。如果有多个也`只返回找到的第一个`。

如果场景中有多个Type类型组件，可以使用`FindObjectsOfType，它返回一个数组Objects[]`。不会查找已禁用的游戏物体。

这两个方法不能通过对象调用，是静态方法。

```csharp
// 获取光源组件并关闭
Light light = FindObjectOfType<Light>();
light.enabled = false;
```
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200930190810528.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dhbmtjbg==,size_16,color_FFFFFF,t_70#pic_center)
## 5.Instantiate
Instantiate实例化，下图是提供的重载方法。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200930225053868.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dhbmtjbg==,size_16,color_FFFFFF,t_70#pic_center)

# GameObject独有的静态方法
**CreatePrimitive** 创建几何体
**Find** 根据名字进行查找，遍历场景中所有的游戏物体，当场景中游戏物体很多的时候，使用Find方法很耗费性能
**FindGameObjectsWithTag**	根据标签进行查找所有游戏物体，返回数组
**FindWithTag** 根据标签查找返回第一个符合条件的

# GameObject公有方法
## 1.AddComponent
往游戏物体身上添加组件，必须是游戏物体的对象来调用

## 2.CompareTag
判断两个游戏物体的标签是否一样

## 3.SetActive
禁用或激活某个游戏物体

## 4.Message有关的
**BroadcastMessage** 广播消息，传递某一方法名，不光调用自身，还会搜索所有的子物体。只要自身和子物体身上有这一传递的方法，都会被调用。可以减少游戏物体之间的耦合性。

`广播消息简单的说就是调用方法，为什么不直接调用某个方法？`
因为直接调用某个方法，需要先拿到方法所在组件的引用，拿到引用相对繁琐，还有部分情况下无法拿到引用。这时可以通过广播消息的方式传递方法名。不需要知道消息接收者具体是谁。
```csharp
public GameObject target;
void Start()
{
    target.BroadcastMessage("Attack",null,SendMessageOptions.DontRequireReceiver);
}
```
接收消息的脚本定义Attack方法
```csharp
// 接收消息只需要完成传递的方法名
void Attack(){
    Debug.Log(this.gameObject + "正在攻击");
}
```
只要子物体有Attack方法都会被调用
![在这里插入图片描述](https://img-blog.csdnimg.cn/20201001000743455.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dhbmtjbg==,size_16,color_FFFFFF,t_70#pic_center)


**SendMessage** 发送消息
只在当前游戏物体身上调用，不会在子物体身上调用

```csharp
public GameObject target;
void Start()
{
    target.SendMessage("Attack",null,SendMessageOptions.DontRequireReceiver);
}
```
![在这里插入图片描述](https://img-blog.csdnimg.cn/20201001000612629.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dhbmtjbg==,size_16,color_FFFFFF,t_70#pic_center)

**SendMessageUpwards** 发送消息和BroadcastMessage相反，BroadcastMessage是所有子物体和自身调用，而SendMessageUpwards是发送当前游戏物体以及他所有的父亲。需要注意的是Broadcast孩子可能有多个，但是Upwards父亲可能只有一个。
```csharp
public GameObject target;
void Start()
{
    target.SendMessageUpwards("Attack",null,SendMessageOptions.DontRequireReceiver);
}
```
![在这里插入图片描述](https://img-blog.csdnimg.cn/20201001001931482.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dhbmtjbg==,size_16,color_FFFFFF,t_70#pic_center)

## 5.得到组件相关方法
**GetComponent**	如果游戏对象附加了类型为 type 的组件，则将其返回，否则返回 null。
**GetComponentInChildren**	使用深度首次搜索返回 GameObject 或其任何子项中类型为 type 的组件。
**GetComponentInParent**	获取 GameObject 或其任何父项中 Type type 的组件。
**GetComponents**	返回 GameObject 中类型为 type 的所有组件。
**GetComponentsInChildren**	 返回 GameObject 或其任何子项中类型为 type 的所有组件。
**GetComponentsInParent** 返回 GameObject 或其任何父项中类型为 type 的所有组件。
**TryGetComponent**	获取指定类型的组件（如果存在）。

具体的内容可查看Unity手册。