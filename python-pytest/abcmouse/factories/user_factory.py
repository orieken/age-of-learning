from faker import Faker

from abcmouse.models.user import User


class UserFactory:
    def __init__(self):
        self.fake = Faker()
        pass

    @staticmethod
    def create_user(name=None):
        fake = Faker()
        if name:
            # If a name is provided, use it to create the email
            email = f"{name.replace(' ', '.').lower()}@{fake.domain_name().lower}"
        else:
            # Generate a random name and email using Faker
            name = fake.name()
            email = fake.email()

        # Create a User instance with the data
        return User(name, email)
