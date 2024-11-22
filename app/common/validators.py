import ipaddress
import re

from django.core import validators
from django.utils.translation import gettext_lazy as _


class KeyValidator(validators.RegexValidator):
    regex = r"^\w{2,255}$"
    message = _(
        "Enter a valid key. This value may contain only English letters, "
        "numbers, and _ character."
    )
    flags = re.ASCII


class UsernameValidator(validators.RegexValidator):
    regex = r"^\w{2,40}$"
    message = _(
        "Enter a valid username. This value may contain only English letters, "
        "numbers, and _ character."
    )
    flags = re.ASCII


class MobileNumberValidator(validators.RegexValidator):
    regex = r"^\+[1-9]\d{1,18}$"
    message = _(
        "Enter a valid mobile number. This value may contain only + sign"
        "and numbers up to 20 digits. example: +123456789"
    )


def valid_ip_or_cidr(ip):
    try:
        ipaddress.IPv4Address(ip)
        return True
    except ValueError:
        pass
    try:
        ipaddress.IPv4Network(ip)
        return True
    except ValueError:
        return False
