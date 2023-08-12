"""
https://github.com/Python-oop/Api_practice
http://open-notify.org/Open-Notify-API/ISS-Location-Now/
https://www.webfx.com/web-development/glossary/http-status-codes/
https://docs.python-requests.org/en/latest/
"""

import  requests


response = requests.get(url='http://api.open-notify.org/iss-now.json')