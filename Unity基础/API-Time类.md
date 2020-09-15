Time类里面全部都是静态的一些变量
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200915202932167.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dhbmtjbg==,size_16,color_FFFFFF,t_70#pic_center)

图片来源：[官方文档](http://www.sikiedu.com/course/59/task/36833/show)

# 一些常用的TimeAPI
## 1.captureFramerate
通过设置帧的速率去进行屏幕截图，让屏幕截图在当前帧可以完成

## 2.deltaTime
代表当前帧所占用的时间。如果设置1秒60帧，由于计算机硬件性能等原因，它的值在1/60上下波动。
`Vector3.forward * Time.deltaTime` 控制物体移动每秒1米。速度乘时间=距离。不管修改帧率的大小，永远保持每秒固定运动。如果需要提高速度，在后面乘以相应的倍数。比如1秒3米`Vector3.forward * Time.deltaTime * 3` 

## 3.timeScale
对所有的deltaTime进行控制的运动做影响。`Time.timeScale = 0`可以在游戏中对deltaTime进行控制所有游戏物体停止运动。也可以对物体的速度进行控制。

## 4.fixedDeltaTime
如果设置1秒60帧，那么值固定为1/60

## 5.realtimeSinceStartup
做性能测试，测试某个方法是否占用性能。单位是秒
```csharp
public int count = 100000;
void Start()
{
    float time1 = Time.realtimeSinceStartup;
    for (int i = 0; i < count; i++)
    {
        test1();
    }
    float time2 = Time.realtimeSinceStartup;
    Debug.Log(time2-time1);
    
    float time3 = Time.realtimeSinceStartup;
    for (int i = 0; i < count; i++)
    {
        test2();
    }
    float time4 = Time.realtimeSinceStartup;
    Debug.Log(time4-time3);
}

void test1()
{
    int a = 1 + 2;
}

void test2()
{
    int a = 1 * 2;
}
```
测试结果可以看到乘法运算比加法运算稍微消耗性能一些。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200915214041736.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dhbmtjbg==,size_16,color_FFFFFF,t_70#pic_center)