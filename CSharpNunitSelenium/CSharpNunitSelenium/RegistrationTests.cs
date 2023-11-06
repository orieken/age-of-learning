using CSharpNunitSelenium.ABCMouse.Base;
using CSharpNunitSelenium.ABCMouse.Factories;
using CSharpNunitSelenium.ABCMouse.Pages;
using FluentAssertions;
using NUnit.Framework.Internal;

namespace CSharpNunitSelenium;

public class RegistrationTests
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
    public void RegisterWithoutEmail()
    {
        var landingPage = AbcMouse?.GetPage<LandingPage>(AbcMouse.Driver!)!;
        // this should be a wait for page load
        Thread.Sleep(TimeSpan.FromSeconds(3));
        
        landingPage.SignUp?.Click();
        var registrationPage = AbcMouse?.GetPage<RegistrationPage>(AbcMouse.Driver!)!;
        // this should be a wait for page load
        Thread.Sleep(TimeSpan.FromSeconds(3));
        registrationPage.Email?.SendKeys("");
        registrationPage.Submit?.Click();
        registrationPage.EmailErrorMessage?.Text.Should().Contain("Please enter a valid email address.");
    }

    [Test]
    [Ignore("Can only run one test at a time")]
    public void CanRegisterAUser()
    {
        var userFactory = new UserFactory();
        var user = userFactory.Create();
        
        var landingPage = AbcMouse?.GetPage<LandingPage>(AbcMouse.Driver!)!;
        // this should be a wait for page load
        landingPage.Wait(5);
        
        landingPage.SignUp?.Click();
        var registrationPage = AbcMouse?.GetPage<RegistrationPage>(AbcMouse.Driver!)!;
        // this should be a wait for page load
        registrationPage.Wait(5);
        registrationPage.Register(user.Email);
        var subscriptionPage = AbcMouse?.GetPage<SubscriptionPage>(AbcMouse.Driver!)!;
        // this should be a wait for page load
        subscriptionPage.Wait(5);
        subscriptionPage.Heading?.Text.Should().Contain("Create Your Account");
    }
    
 
 [Test]
 public void BecomeAMemberMessageIsDisplayed()
 {
     var registrationPage = AbcMouse?.GetPage<RegistrationPage>(AbcMouse.Driver!)!;
     // this should be a wait for page load
     registrationPage.Wait(5);
     registrationPage.BecomeAMemberMessage?.Displayed.Should().BeTrue();
     registrationPage.BecomeAMemberMessage?.Text.Should().Contain("Become a Member");
 }
}