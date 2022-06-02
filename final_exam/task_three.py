followers_dict = dict()

data = input()

while data != "Log out":
    data = data.split(": ")

    if data[0] == "New follower":
        username = data[1]
        if username not in followers_dict:
            followers_dict[username] = username
            followers_dict[username] = dict()
            followers_dict[username]["likes"] = 0
            followers_dict[username]['comments'] = 0
        else:
            pass

    elif data[0] == "Like":
        username = data[1]
        count = int(data[2])
        if username not in followers_dict:
            followers_dict[username] = username
            followers_dict[username] = dict()
            followers_dict[username]["likes"] = count
            followers_dict[username]["comments"] = 0
        else:
            followers_dict[username]["likes"] += count

    elif data[0] == "Comment":
        username = data[1]
        if username not in followers_dict:
            followers_dict[username] = username
            followers_dict[username] = dict()
            followers_dict[username]["likes"] = 0
            followers_dict[username]["comments"] = 1
        else:
            followers_dict[username]["comments"] += 1

    elif data[0] == "Blocked":
        username = data[1]
        if username in followers_dict:
            followers_dict.pop(username)
        else:
            print(f"{username} doesn't exist.")
    data = input()

print(f"{len(followers_dict)} followers")
for key, value in followers_dict.items():
    print(f"{key}: {value['likes'] + value['comments']}")
