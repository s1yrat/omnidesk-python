# py-omni-wrap

Omnidesk API wrapper written in Python.

## Usage

```python
from py_omni_wrap import OmnideskAPI


omnidesk_config = {
    "sub_domain": "your_sub_domain",
    "domain": "omnidesk.ru/api/",
    "email": "your_email",
    "api_key": "your_api_key"
}

omnidesk = OmnideskAPI(**omnidesk_config)

staff = omnidesk.send_request("get", "staff")

```

## TODO:

- User-friendly methods (e. g. `omnidesk.get_staff()`).
- Support for more endpoints.
