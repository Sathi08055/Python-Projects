from question_model import Question
import requests, json
import html


def new_data():
    def api_connect():
        url = "https://opentdb.com/api.php"
        parameters = {
            "amount": 20,
            "category": 9,
            "difficulty": "easy",
            "type": "boolean",
        }

        response = requests.get(url=url, params=parameters)
        data = response.json()

        with open("Question.json","w+") as file:
            json.dump(data,file, indent=4)
        return data

    data=api_connect()

    ques_list = [Question(q_text=html.unescape(item["question"]), q_answer=html.unescape(item["correct_answer"])) for item in data["results"]]
    return ques_list

if __name__ == "__main__":
    new_data()