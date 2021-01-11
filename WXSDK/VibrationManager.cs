using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using WeChatWASM;

public class VibrationManager : MonoBehaviour
{
    
    private static bool _vibrationsActive = true;
    
    /// 启用或禁用通过这个类调用的所有触觉
    public static void SetHapticsActive(bool status)
    {
        Debug.LogError("设置震动开关状态: " + status);
        _vibrationsActive = status;
    }
    
    /// 震动反馈
    public static void Haptic(HapticTypes type, bool defaultToRegularVibrate = false, bool alsoRumble = false,
        MonoBehaviour coroutineSupport = null, int controllerID = -1)
    {
        if (!_vibrationsActive)
        {
            Debug.LogError("vibrationsActive不震动时的值： "+ _vibrationsActive); 
            //   ------------------------------ [ 不震动测试 ] ------------------------------
            switch (type)
            {
                case HapticTypes.None:         Debug.LogError("------ 00 -----");  break;
                case HapticTypes.Selection:    Debug.LogError("------ 11 -----");  break;
                case HapticTypes.Success:      Debug.LogError("------ 22 -----");  break;
                case HapticTypes.Warning:      Debug.LogError("------ 33 -----");  break;
                case HapticTypes.Failure:      Debug.LogError("------ 44 -----");  break;
                case HapticTypes.LightImpact:  Debug.LogError("------ 55 -----");  break;
                case HapticTypes.MediumImpact: Debug.LogError("------ 66 -----");  break;
                case HapticTypes.HeavyImpact:  Debug.LogError("------ 77 -----");  break;
                case HapticTypes.RigidImpact:  Debug.LogError("------ 88 -----");  break;
                case HapticTypes.SoftImpact:   Debug.LogError("------ 99 -----");  break;
            }
            return;
        }
        
        //   ------------------------------ [ 震动测试 ] ------------------------------
        Debug.LogError("进入实现微信震动接口： ");
        Debug.LogError("vibrationsActive的值： "+ _vibrationsActive);
#if WXGAME && !UNITY_EDITOR
       switch (type)
        {
            case HapticTypes.None:         Debug.LogError("------ 0 -----"); break;
            case HapticTypes.Selection:    Debug.LogError("------ 1 -----"); WX.VibrateLong(); break;
            case HapticTypes.Success:      Debug.LogError("------ 2 -----"); WX.VibrateLong(); break;
            case HapticTypes.Warning:      Debug.LogError("------ 3 -----"); WX.VibrateLong(); break;
            case HapticTypes.Failure:      Debug.LogError("------ 4 -----"); WX.VibrateLong(); break;
            case HapticTypes.LightImpact:  Debug.LogError("------ 5 -----"); WX.VibrateLong(); break;
            case HapticTypes.MediumImpact: Debug.LogError("------ 6 -----"); WX.VibrateLong(); break;
            case HapticTypes.HeavyImpact:  Debug.LogError("------ 7 -----"); WX.VibrateLong(); break;
            case HapticTypes.RigidImpact:  Debug.LogError("------ 8 -----"); WX.VibrateLong(); break;
            case HapticTypes.SoftImpact:   Debug.LogError("------ 9 -----"); WX.VibrateLong(); break;
        } 
#endif
        switch (type)
        {
            case HapticTypes.None:         Debug.LogError("------ 0 -----");  break;
            case HapticTypes.Selection:    Debug.LogError("------ 1 -----");  break;
            case HapticTypes.Success:      Debug.LogError("------ 2 -----");  break;
            case HapticTypes.Warning:      Debug.LogError("------ 3 -----");  break;
            case HapticTypes.Failure:      Debug.LogError("------ 4 -----");  break;
            case HapticTypes.LightImpact:  Debug.LogError("------ 5 -----");  break;
            case HapticTypes.MediumImpact: Debug.LogError("------ 6 -----");  break;
            case HapticTypes.HeavyImpact:  Debug.LogError("------ 7 -----");  break;
            case HapticTypes.RigidImpact:  Debug.LogError("------ 8 -----");  break;
            case HapticTypes.SoftImpact:   Debug.LogError("------ 9 -----");  break;
        } 
    }
    
}