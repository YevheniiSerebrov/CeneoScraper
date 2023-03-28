import requests
product_code = "122892647"
print(product_code)
# 122892647
url = f"https://www.ceneo.pl/{product_code}#tab-reviews"
response = requests.get(url)
print(response.status_code)