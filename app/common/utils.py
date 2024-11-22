import uuid

from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode


def encode_uid(pk):
    return force_str(urlsafe_base64_encode(force_bytes(pk)))


def decode_uid(pk):
    return force_str(urlsafe_base64_decode(pk))


def generate_file_path(instance, filename):
    """
    Generate file path based on instance verbose_name_plural.
    File will be uploaded to MEDIA_ROOT/<model::verbose_name_plural>/<filename>
    """
    ext = filename.split(".")[-1]
    meta = getattr(instance, "_meta", None)
    base_path = (
        "generals"
        if meta is None
        else getattr(meta, "verbose_name_plural", "generals").lower()
    )
    return f"{base_path}/{uuid.uuid4()}.{ext}"


def remove_prefix(string: str, prefix: str):
    """
    Return a str with the given prefix removed if present.

    If the string starts with the prefix, return string[len(prefix):].
    Otherwise, return a copy of the original string.
    """
    return string[len(prefix) :] if string.startswith(prefix) else string[:]
