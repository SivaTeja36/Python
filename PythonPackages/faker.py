from faker import Faker

# Create a Faker instance
fake = Faker()

# Generate fake data
name = fake.name()
address = fake.address()
email = fake.email()

print("Name:", name)
print("Address:", address)
print("Email:", email)