import base64
import hashlib
import hmac
from urllib.parse import urlparse

thumbor_key = b"your_actual_thumbor_key"
url_to_sign = "/some/image.jpg?300x200/smart/thumbor.readthedocs.io/en/latest/_images/logo-thumbor.png"


def main():
    _hmac = hmac.new(thumbor_key, digestmod=hashlib.sha1)
    _hmac = _hmac.copy()
    _hmac.update(url_to_sign.encode())
    signature = base64.urlsafe_b64encode(_hmac.digest()).decode("ascii")

    parsed_url = urlparse(url_to_sign)
    q = parsed_url.query
    p = parsed_url.path.strip("/")
    d = base64.urlsafe_b64encode(f"/{signature}/{q}".encode()).decode().strip("=")

    return f"http://127.0.0.1:8888/{p}?{d}"


if __name__ == "__main__":
    print("Thumbor URL:", main())
