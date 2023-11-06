using CSharpNunitSelenium.ABCMouse.Base;
using OpenQA.Selenium;

namespace CSharpNunitSelenium.ABCMouse.Pages;

public class SubscriptionPage : Page
{
    protected override string URL { get; set; } = "https://www.abcmouse.com/abt/subscription";

    public IWebElement? Heading => (IWebElement)_jsExecutor.ExecuteScript(
        "return document" +
        ".querySelector(\"body > route-view\")" +
        ".shadowRoot.querySelector(\"#page-component\")" +
        ".shadowRoot.querySelector(\"#subscription-form > h3\")"
    );
    public SubscriptionPage(IWebDriver driver) : base(driver)
    {
    }

}