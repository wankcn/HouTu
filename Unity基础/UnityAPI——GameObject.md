# 1.给游戏物体添加组件
使用`AddComponent<>`可以添加组件，也可以添加脚本
```csharp
GameObject go = GameObject.CreatePrimitive(PrimitiveType.Cube);
go.AddComponent<Rigidbody>(); 
```

