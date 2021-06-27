from faker import Faker

if __name__ == '__main__':
    fake = Faker()

    profiles = []
    for elem in range(0, 100):
        profiles.append(fake.profile())

    for profile in profiles:
        print(profile['name'])
        print(profile['mail'])
        print()

    for elem in dir(fake):
        if elem.startswith('__') and elem.endswith('__'):
            continue
        else:
            print(f"Attributes:{callable(elem)}:{elem}")
