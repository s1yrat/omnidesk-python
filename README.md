# omni-wrap
Omnidesk API wrapper written in python

## Usage

```python
import omni-wrap

omnidesk-config = {
	'sub_domain': 'your_sub_domain',
	'domain': 'omnidesk.ru/api/',
	'email': 'your_email',
	'api_key': 'your_api_key'
}

omnidesk = OmnideskAPI(**omnidesk-config)

staff = omnidesk.send_request('get', 'staff')

```
