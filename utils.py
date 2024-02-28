from db import district_list


def create(new_district):
    new_id = max(district_list, key=lambda x: x["id"])["id"] + 1
    new_district["id"] = new_id
    district_list.append(new_district)
    print("District added !")
    print(district_list)


def retrieve(id):
    for district in district_list:
        if district["id"] == id:
            return district
    return None


def update(id, new_name):
    for index, district in enumerate(district_list):
        if district["id"] == id:
            district_list[index]["name"] = new_name
            print("District updated !")
            print(district_list)
            return
    print("District not found!")


def delete(id):
    for index, district in enumerate(district_list):
        if district["id"] == id:
            del district_list[index]
            print("District deleted!")
            print(district_list)
            return
    print(f"District not found!")

