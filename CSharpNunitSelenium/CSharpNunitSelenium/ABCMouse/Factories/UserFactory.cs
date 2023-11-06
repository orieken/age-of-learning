using Bogus;
using CSharpNunitSelenium.ABCMouse.Models;

namespace CSharpNunitSelenium.ABCMouse.Factories;

public class UserFactory
{
    private readonly Faker<User> _faker;

    public UserFactory()
    {
        _faker = new Faker<User>()
            .RuleFor(u => u.Email, (f, u) => f.Internet.Email(u.Name));
    }

    public User Create(string? name = null)
    {
        if (string.IsNullOrEmpty(name))
        {
            return _faker.Generate();
        }
        else
        {
            return new User
            {
                Name = name,
                Email = _faker.Generate().Email
            };
        }
    }
}