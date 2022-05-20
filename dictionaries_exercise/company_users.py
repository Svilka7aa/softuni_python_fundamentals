def company_users():
    company_dict = {}
    while True:
        data = input()

        if data == "End":
            break

        data = data.split(" -> ")
        if data[0] not in company_dict.keys():
            company_dict[data[0]] = []
        if data[1] not in company_dict[data[0]]:
            company_dict[data[0]].append(data[1])

    for key, value in company_dict.items():
        print(key)
        for user in value:
            print(f"-- {user}")


company_users()
