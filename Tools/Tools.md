# Tools



## 时间相关

转换时间戳

```c#
public static DateTime GetDateTime(long milliseconds)
{
    DateTime dtStart = TimeZone.CurrentTimeZone.ToLocalTime(new DateTime(1970, 1, 1));
    long lTime = long.Parse(milliseconds + "0000");
    TimeSpan toNow = new TimeSpan(lTime);
    return dtStart.Add(toNow);
}
```



