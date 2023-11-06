
using CSharpNunitSelenium.ABCMouse.Pages;
using FluentAssertions;

namespace CSharpNunitSelenium;

public class Tests
{
    public ABCMouse.AbcMouse? AbcMouse;
    
    [SetUp]
    public void Setup()
    {
        AbcMouse = new ABCMouse.AbcMouse();
        AbcMouse.NavigateTo();
    }

    [TearDown]
    public void TearDown()
    {
        AbcMouse?.CloseBrowser();
    }

    [Test]
    [Ignore("Can only run one test at a time")]
    public void SignUpShouldBeDisplayed()
    {
        // wait for page load
        
        var landingPage = AbcMouse?.GetPage<LandingPage>(AbcMouse.Driver!)!;
        // this should be a wait for page load
        Thread.Sleep(TimeSpan.FromSeconds(3));

        // I would really like this to be 
        // landingPage?.SignUp?.Displayed.Should().BeDisplayed(); 
        landingPage.SignUp?.Displayed.Should().BeTrue();
        landingPage.SignUp?.Text.Should().Be("Sign Up");
    }
}