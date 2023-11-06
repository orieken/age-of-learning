using CSharpNunitSelenium.ABCMouse.Base;
using OpenQA.Selenium;

namespace CSharpNunitSelenium.ABCMouse.Pages;

public class LandingPage : Page
{
    
    protected override string URL { get; set; } = "https://www.abcmouse.com/abc/";
    public IWebElement? SignUp => (IWebElement) _jsExecutor!.ExecuteScript(
        "return document.querySelector(\"body > route-view\")" +
        ".shadowRoot.querySelector(\"#page-component\")" +
        ".shadowRoot.querySelector" +
        "(\"main-layout > header > home-header > authstate-context:nth-child(3) > signup-button\")"
        );
    public LandingPage(IWebDriver driver) : base(driver)
    {
    }
    
}
