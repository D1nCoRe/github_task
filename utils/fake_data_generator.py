from faker import Faker


def get_fake_name():
    fake = Faker()
    fake_name = fake.unique.first_name()
    return fake_name
