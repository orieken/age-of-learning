using System.Reflection;
using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;

namespace CSharpNunitSelenium.ABCMouse.Base;


public abstract class Site
{
    public IWebDriver? Driver { get; private set; }
    
    protected readonly Dictionary<string, Type> Pages;

    protected Site()
    {
        Pages = new Dictionary<string, Type>();
        InitializeWebDriver();
    }
    
    protected abstract string GetBaseUrl();

    private void InitializeWebDriver()
    {
        var options = new ChromeOptions();
        IsHeadless(options);
        Driver = new ChromeDriver(options);
        Driver.Manage().Timeouts().PageLoad = TimeSpan.FromSeconds(30);
    }

    private static void IsHeadless(ChromeOptions options)
    {
        string? headless = Environment.GetEnvironmentVariable("HEADLESS");
        if (headless is "true")
        {
            options.AddArgument("--headless");
        }
    }

    public void NavigateTo(string relativeUrl = "/")
    {
        string baseUrl = GetBaseUrl();
        string fullUrl = baseUrl + relativeUrl;

        // Navigate to the specified URL
        Driver!.Navigate().GoToUrl(fullUrl);
    }

    public void CloseBrowser()
    {
        // Close the WebDriver and release resources
        Driver!.Quit();
    }
    
    protected void LoadPageClasses()
    {
        var pagesAssembly = Assembly.GetExecutingAssembly();
        var pageTypes = GetPageTypesInNamespace(pagesAssembly, "CSharpNunitSelenium.ABCMouse.Pages");

        foreach (var pageType in pageTypes)
        {
            Pages[pageType.Name.ToLower()] = pageType;
        }
    }

    private IEnumerable<Type> GetPageTypesInNamespace(Assembly assembly, string targetNamespace)
    {
        return assembly.GetTypes()
            .Where(type => IsInNamespace(type, targetNamespace) && typeof(IPage).IsAssignableFrom(type));
    }

    private bool IsInNamespace(Type type, string targetNamespace)
    {
        return type.Namespace != null && type.Namespace.StartsWith(targetNamespace);
    } 
    
    public TPage GetPage<TPage>(IWebDriver driver) where TPage : IPage
    {
        var pageTypeName = typeof(TPage).Name.ToLower();

        if (Pages.ContainsKey(pageTypeName))
        {
            return CreatePageInstance<TPage>(driver, pageTypeName);
        }
        else
        {
            throw new ArgumentException($"Page '{pageTypeName}' not found.");
        }
    }

    private TPage CreatePageInstance<TPage>(IWebDriver driver, string pageTypeName) where TPage : IPage
    {
        var pageType = Pages[pageTypeName];
        var pageInstance = (TPage)Activator.CreateInstance(pageType, new object[] { driver })!;
        return pageInstance;
    }
}
