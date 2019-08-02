import requests

def get_ron_swanson_quote():
  response = requests.get('https://ron-swanson-quotes.herokuapp.com/v2/quotes')
  return response

# result = get_ron_swanson_quote()
# response_json = result.json()
# print(response_json[0])