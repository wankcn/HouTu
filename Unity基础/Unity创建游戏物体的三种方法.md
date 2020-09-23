# 1.使用构造方法
可以直接new一个GameObject
在start函数里创建，游戏物体可以在任何地方创建，测试创建一次
```csharp
void Start()
{
    new GameObject();
}
```
在unity游戏物体上添加脚本并执行。如下图1是运行前，图2是运行游戏后。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200922180228849.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dhbmtjbg==,size_16,color_FFFFFF,t_70#pic_center)
游戏运行时创建了新的游戏物体，只有Transform组件。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200922180520863.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dhbmtjbg==,size_16,color_FFFFFF,t_70#pic_center)
当游戏结束新游戏物体销毁
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200922180636365.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dhbmtjbg==,size_16,color_FFFFFF,t_70#pic_center)
在新创建游戏物体时指定参数。
```csharp
void Start()
{
    new GameObject("Cube");
}
```
参数即新创建游戏物体名。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200922181316736.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dhbmtjbg==,size_16,color_FFFFFF,t_70#pic_center)
# 2.Instance
instance是静态方法，可以通过`GameObject.Instantiate();`	调用，需要传递一个prefab。通常情况下是根据prefab进行初始化的。
```csharp
public GameObject prefab;

void Start()
{
    GameObject.Instantiate(prefab);
}
```
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200922182754439.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dhbmtjbg==,size_16,color_FFFFFF,t_70#pic_center)
运行游戏
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200922182837444.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dhbmtjbg==,size_16,color_FFFFFF,t_70#pic_center)
可以发现新建的游戏物体后有一个Clone，说明是通过某个预制体克隆出来的。他也可以根据游戏物体克隆。

# 3.CreatePrimitive
primitive解释为原始的。指的是创建的系统原始的图形。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200922184500146.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dhbmtjbg==,size_16,color_FFFFFF,t_70#pic_center)
```csharp
void Start()
{
    GameObject.CreatePrimitive(PrimitiveType.Plane);
    GameObject.CreatePrimitive(PrimitiveType.Cube);
}
```
假设创建了一个平面和立方体。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200922184834714.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dhbmtjbg==,size_16,color_FFFFFF,t_70#pic_center)

# 总结
1. 构造方法一般用来新建一个空的游戏物体
2. Instance用来实例化特效、游戏角色等各种各样的东西
3. CreatePrimitive可以创建一些基本的图形