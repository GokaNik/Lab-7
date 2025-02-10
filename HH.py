import requests

def get_vacancies():
    url = "https://api.hh.ru/vacancies"
    params = {
        "text": "Python разработчик",
        "area": 1,  # Москва
        "per_page": 5
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()

        print("Найденные вакансии:\n")
        for vacancy in data["items"]:
            name = vacancy["name"]
            employer = vacancy["employer"]["name"]
            salary = vacancy.get("salary")
            salary_text = "Не указана"
            if salary:
                salary_text = f"{salary.get('from', 'Не указано')} - {salary.get('to', 'Не указано')} {salary.get('currency', '')}"
            url = vacancy["alternate_url"]

            print(f"{name} ({employer})")
            print(f"Зарплата: {salary_text}")
            print(f"Ссылка: {url}\n")

    else:
        print(f"Ошибка {response.status_code}: {response.text}")

if __name__ == "__main__":
    get_vacancies()
