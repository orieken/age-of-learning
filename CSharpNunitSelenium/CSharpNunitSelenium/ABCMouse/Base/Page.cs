using OpenQA.Selenium.Support.UI;

namespace CSharpNunitSelenium.ABCMouse.Base;

using OpenQA.Selenium;

public abstract class Page : IPage
{
    protected IWebDriver Driver { get; }
    protected readonly IJavaScriptExecutor? _jsExecutor;
    protected abstract string URL { get; set; }

    protected Page(IWebDriver driver)
    {
        Driver = driver;
        _jsExecutor = (IJavaScriptExecutor) driver;
    }
    
    public void NavigateTo()
    {
        Driver.Navigate().GoToUrl(URL);
    }
    
    public void Wait(double seconds)
    {
        Thread.Sleep(TimeSpan.FromSeconds(seconds));
    }

    public string GetUrl()
    {
        return Driver.Url;
    }
}
