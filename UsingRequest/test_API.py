import requests


def test_api_get():

    res = requests.get("https://reqres.in/api/users?page=2")
    print(res.json())

    assert res.status_code == 200, "status code is not 200.Rather found  " + str(res.status_code)
    for record in res.json()['data']:

        if record['id'] == 11:
            assert record['first_name'] == "George", \
                "Data not matched! Expected : Eve, but found : " + str(record['first_name'])
            assert record['last_name'] == "Edwards", \
                "Data not matched! Expected : Holt, but found : " + str(record['last_name'])


def test_api_post():
    data = {
            "name": "morpheus",
            "job": "QA"
          }
    res = requests.post("https://reqres.in/api/users", data=data)
    data = res.json()
    print(40*"_")
    print(data)
    assert res.status_code == 201, " Status code is not found 201."
    assert data["name"] == "morpheus", "User created with wrong name. \
        Expected : John, but found : " + str(data['name'])
    assert data['job'] == "QA", "User created with wrong job. \
        Expected : QA, but found : " + str(data['job'])


def test_api_put():
    data = {
             "name": "morpheus",
             "job": "zion resident"
             }

    user_data = requests.get("https://reqres.in/api/users/7").json()
    print(user_data)

    update_data = requests.put("https://reqres.in/api/users/7", data=data).json()
    print(50*"__")
    print(update_data)

    assert update_data['name'] == "morpheus"


def test_api_delete():
    res = requests.delete("https://reqres.in/api/users/7")
    print(res)

    assert res.status_code == 204


