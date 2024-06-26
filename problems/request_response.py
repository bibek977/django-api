import requests

url = "https://jsonplaceholder.typicode.com/posts"

get_response = requests.get(url)

# print(get_response.json())
# print(get_response.status_code)

payload = {
    'userId':2,
    'title':'custom',
    'body':'test for request post'
}

# post_response = requests.post(url,json=payload)
# print(post_response.json())
# print(post_response.status_code)

delete_response = requests.delete(f"{url}/1/")

