import requests
response = requests.get('https://jsonplaceholder.typicode.com/users')
users = response.text # use response.content for returning consumed data in bytes - use for images and other nontextual data
user_library = response.json()
user_three = user_library[2]
request = response.request
users_length = len(response.json())
print(users_length, "\n\n", users, "\n\n", response.status_code, "\n\n", response.reason, "\n\n", request.headers, "\n\n", user_library, "\n\n", user_three["name"])
def count_users():
    counter = 1
    for i in user_library:
        print(counter)
        counter += 1

count_users()