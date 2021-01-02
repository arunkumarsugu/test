import requests
import json
import csv



def list_of_all_users():
    all_user_data = json.load(open("document.json"))
    return all_user_data


def particular_users(login):
    single_user_data = requests.get(f"https://api.github.com/users/{login}").json()
    return single_user_data


def followers_list(login):
    followers_data = requests.get(f"https://api.github.com/users/{login}/followers").json()
    return followers_data




all_user_data = list_of_all_users()
rows = []
for user in all_user_data:
    if user["id"] % 10 == 0:
        single_user_data = particular_users(user["login"])
        followers_details = followers_list(single_user_data["login"])

        for followers in followers_details:
            rows.append([user["id"], user["login"], single_user_data["name"], followers["id"], followers['login']])

with open("my_data.csv", 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['UserId', 'UserLogin', 'UserName', 'FollowerId', 'FollowerLogin'])
    csvwriter.writerows(rows)
