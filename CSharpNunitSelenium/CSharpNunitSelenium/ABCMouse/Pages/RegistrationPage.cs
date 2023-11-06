using CSharpNunitSelenium.ABCMouse.Base;
using OpenQA.Selenium;

namespace CSharpNunitSelenium.ABCMouse.Pages;

public class RegistrationPage : Page
{
    
    protected override string URL { get; set; } = "https://www.abcmouse.com/abc/prospect-register/";
    
    public IWebElement? Email => (IWebElement)_jsExecutor!.ExecuteScript(
        "return document.querySelector(\"body > route-view\")" +
        ".shadowRoot.querySelector(\"#page-component\")" +
        ".shadowRoot.querySelector(\"#email\")"
        );

    public IWebElement? EmailErrorMessage => (IWebElement)_jsExecutor.ExecuteScript(
        "return document.querySelector(\"body > route-view\")" +
        ".shadowRoot.querySelector(\"#page-component\")" +
        ".shadowRoot.querySelector(\"#email-error-message\")"
    );

    public IWebElement? Submit => (IWebElement)_jsExecutor.ExecuteScript(
        "return document.querySelector(\"body > route-view\")" +
        ".shadowRoot.querySelector(\"#page-component\")" +
        ".shadowRoot.querySelector(\"#submit-button\")"
    );
    
    public IWebElement? BecomeAMemberMessage => (IWebElement)_jsExecutor!.ExecuteScript(
        "return document" +
        ".querySelector(\"body > route-view\")" +
        ".shadowRoot.querySelector(\"#page-component\")" +
        ".shadowRoot.querySelector(\"#become-member\")"
    );

    public RegistrationPage(IWebDriver driver) : base(driver)
    {
    }
    
    public void Register(string email)
    {
        Email?.SendKeys(email);
        Submit?.Click();
    }
}