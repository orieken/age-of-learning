using System.Reflection;
using CSharpNunitSelenium.ABCMouse.Base;
using CSharpNunitSelenium.ABCMouse.Pages;

namespace CSharpNunitSelenium.ABCMouse;

public class AbcMouse : Site
{
    
    
    public AbcMouse()
    {
        LoadPageClasses();
    }
    
    protected override string GetBaseUrl()
    {
        return "https://www.abcmouse.com";
    }
    
}