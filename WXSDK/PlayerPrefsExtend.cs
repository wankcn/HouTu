using System.Collections;
using System.Collections.Generic;
using UnityEngine;


public class PlayerPrefsExtend
{
    public static void SetInt(string key, int value)
    {
#if !(UNITY_EDITOR) && (WXGAME)
        WeChatWASM.WX.StorageSetIntSync(key, value);
#else
        PlayerPrefs.SetInt(key, value);
#endif  
    }

    public static int GetInt(string key, int defaultValue = 0)
    {
#if !(UNITY_EDITOR) && (WXGAME)
        return WeChatWASM.WX.StorageGetIntSync(key, defaultValue);
#else
        return PlayerPrefs.GetInt(key, defaultValue);
#endif
    }

    public static void SetFloat(string key, float value)
    {
#if !(UNITY_EDITOR) && (WXGAME)
        WeChatWASM.WX.StorageSetFloatSync(key, value);
#else
        PlayerPrefs.SetFloat(key, value);
#endif
    }

    public static float GetFloat(string key, float defaultValue = 0.0f)
    {
#if !(UNITY_EDITOR) && (WXGAME)
        return WeChatWASM.WX.StorageGetFloatSync(key, defaultValue);
#else
        return PlayerPrefs.GetFloat(key, defaultValue);
#endif
    }

    public static void SetString(string key, string value)
    {
#if !(UNITY_EDITOR) && (WXGAME)
        WeChatWASM.WX.StorageSetStringSync(key, value);
#else
        PlayerPrefs.SetString(key, value);
#endif
    }

    public static string GetString(string key, string defaultValue = "")
    {
#if !(UNITY_EDITOR) && (WXGAME)
        return WeChatWASM.WX.StorageGetStringSync(key, defaultValue);
#else
        return PlayerPrefs.GetString(key, defaultValue);
#endif
    }

    public static bool HasKey(string key)
    {
#if !(UNITY_EDITOR) && (WXGAME)
        return WeChatWASM.WX.StorageHasKeySync(key);
#else
        return PlayerPrefs.HasKey(key);
#endif
    }

    public static void DeleteAll()
    {
#if !(UNITY_EDITOR) && (WXGAME)
        WeChatWASM.WX.StorageDeleteAllSync();
#else
        PlayerPrefs.DeleteAll();
#endif
    }
}

