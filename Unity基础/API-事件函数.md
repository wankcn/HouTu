# 一、准备环境
## 1.创建场景01-MainScene
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200915135113906.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dhbmtjbg==,size_16,color_FFFFFF,t_70#pic_center)
## 2.添加GameObject并新建脚本
为GameObject添加测试时间函数的脚本`API01-EventFunction`
在Unity所有新建的脚本都继承自`MonoBehaviour`继承自`Behaviour`继承自`Component`继承自`Object`
所有创建的脚本都是继承自Component的，所以创建的脚本都是一个组件，组件继承自Object，游戏物体也是继承自Object。

# 二、事件函数的执行时机和顺序
## 如何找到Unity里支持的所有事件
官方文档:[https://docs.unity3d.com/Manual/index.html](https://docs.unity3d.com/Manual/index.html)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200915143417809.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dhbmtjbg==,size_16,color_FFFFFF,t_70#pic_center)
在Manul下找到Scripting。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200915144225538.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dhbmtjbg==,size_16,color_FFFFFF,t_70#pic_center)
**事件方法顺序里有一张SVG图**
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200915144447978.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dhbmtjbg==,size_16,color_FFFFFF,t_70#pic_center)![在这里插入图片描述](https://img-blog.csdnimg.cn/20200915144509926.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dhbmtjbg==,size_16,color_FFFFFF,t_70#pic_center)![在这里插入图片描述](https://img-blog.csdnimg.cn/20200915144552296.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dhbmtjbg==,size_16,color_FFFFFF,t_70#pic_center)
**这些事件方法都没有参数，但是要注意大小写的问题**

## 1.Start/Update
创建的脚本在Rider打开会有默认的两个方法`Start`和`Update`
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200915140613844.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dhbmtjbg==,size_16,color_FFFFFF,t_70#pic_center)
下面测试一下这两个方法
```csharp
public class API01EventFunction : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        Debug.Log("Start");
    }

    // Update is called once per frame
    void Update()
    {
        Debug.Log("Update");
    }
}
```
**在Unity运行进行输出观看结果**
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200915142950140.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dhbmtjbg==,size_16,color_FFFFFF,t_70#pic_center)
FPS大概稳定在87左右，说明Update每一秒执行87次。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200915141856156.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dhbmtjbg==,size_16,color_FFFFFF,t_70#pic_center)
可以发现start只执行了一次，update会一直进行输出。在我截图时已经执行了1463次。

## 2.Reset
Reset只会在Editor模式下出发，如果已经build之后，是不会触发的。也就是只在编辑器模式下，发布出来以后就不属于编辑器了。当被附加（指的是把脚本附加到GameObject）的时候或者reset的时候触发。

## 3.Awake
当整个场景运行起来的时候，Awake就会被调用，或者当一个游戏物体被实例化的时候，Awake也会被调用。

## 4.OnEnable/OnDisable
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200915150830221.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dhbmtjbg==,size_16,color_FFFFFF,t_70#pic_center)
当游戏运行起来的时候调用OnEnable，取消游戏物体的勾选不可用状态就会调用Disable，勾选上显示游戏物体就会调用OnEnable。
在代码里面通过SetActive设置为ture或者false来控制游戏物体可用与不可用。

## 5.FixedUpdate/Update/LateUpdate
FixedUpdate是固定的Update，一般是每秒60帧。FixedUpdate会先调用，然后是Update，最后是LateUpdate（每帧调用一次，后于update调用）。这三个都是每帧调用。
一般把与物理相关的，与控制运动相关放在FixedUpdate里，因为执行次数是固定的，所以运动的距离也是固定的，可以保证运动平滑，不会受电脑性能的影响。
FixedUpdate每帧可能调用多次，如果设置每秒60次，那么不管在任何时候，FixedUpdate都是每秒60次。Update会根据游戏的运行实际情况来决定，如果硬件差，运行可能会偏少。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200915185901639.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dhbmtjbg==,size_16,color_FFFFFF,t_70#pic_center)
如图Update和LateUpdate调用次数一样。

## 6.OnTrigger/OnCollision
分别用来触发触发器和碰撞器的

## 7.yield WaitForFixedUpdate
在FixedUpdate里面可以调用yield进行等待

## 8.OnMouseXX
输入事件，与鼠标操作有关的事件

## 9.Scene rendering
与场景渲染有关
## 10.OnDrawGizmos
绘制一些Gizmos，如图中的辅助线都是Gizmos。默认在Game窗口下不显示。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200915184741347.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dhbmtjbg==,size_16,color_FFFFFF,t_70#pic_center)
## 11.OnGUI
绘制GUI的，基本不用了，现在都用UGUI比较多。

## 12.OnApplicationPause/OnApplicationQuit
OnApplicationPause一般是点击Unity界面中的暂停的时候调用。
OnApplicationQuit退出游戏的时候。

## 13.OnDestroy
退出游戏的时候，所有游戏物体都会被销毁，此时调用OnDestroy。在调用OnDestroy之前会先调用一下OnDisable。