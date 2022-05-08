from faker import Faker

fake = Faker(locale="fr_FR")

print(fake.unique.name())

for _ in range(50):
    print(fake.name())