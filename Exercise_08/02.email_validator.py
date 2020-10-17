import exceptions


def simbol_validator(email):
    if '@' not in email:
        raise exceptions.MustContainAtSymbolError('Email must contain @')


def name_validator(email):
    username = email.split('@')[0]
    if len(username) <= 4:
        raise exceptions.NameTooShortError(
            'Name must be more than 4 characters')


def domain_validator(email, valid_domains):
    domain = email.split('.')[-1]
    if domain not in valid_domains:
        raise exceptions.InvalidDomainError(
            'Domain must be one of the following: .com, .bg, .org, .net')


email = input()
valid_domains = ('com', 'bg', 'net', 'org')


while email != 'End':
    simbol_validator(email)
    name_validator(email)
    domain_validator(email, valid_domains)
    print("Email is valid")
    email = input()
