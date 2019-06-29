import email_validator


def is_valid(email: str) -> bool:
    try:
        email_validator.validate_email(email)
        return True
    except:
        return False


def masked(email: str):
    masked_email = email.split('@')
    return masked_email[0][:2] + '*' * (len(masked_email[0]) - 2) + '@' + masked_email[1]