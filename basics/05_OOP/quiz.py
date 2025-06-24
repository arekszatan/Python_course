import requests
import html


class Question:
    def __init__(self, category, question_str, correct_answer_flag):
        self.category = category
        self.question_str = question_str
        self.correct_answer_flag = correct_answer_flag


class Quiz:
    def __init__(self, num_questions):
        self.api_url = "https://opentdb.com/api.php?difficulty=easy&type=boolean&amount="
        self.num_questions = num_questions
        self.questions_list = []
        self.load_questions(num_questions)

    def load_questions(self, num_questions):
        response = requests.get(self.api_url + str(num_questions))
        if response.ok:
            # print(response.json())
            data = response.json()
            result = data['results']
            for q in result:
                category = q['category']
                question_type = q['type'] # True or False
                difficulty = q['difficulty']
                question_str = html.unescape(q['question'])
                # print(question_str)
                correct_answer_flag = q['correct_answer'].lower() in ['true', '1', 'yes']
                q_obj = Question(category, question_str, correct_answer_flag)
                self.questions_list.append(q_obj)

    def start_quiz(self):
        print("\nWelcome in Quiz!")
        num_correct_user_answers = 0
        n = 0
        num_questions = len(self.questions_list)
        while n < num_questions:
            q = self.questions_list[n]
            print("Question number " + str(n) + " : ", q.question_str)
            print(q.correct_answer_flag)
            answer = input("Give correct answer as y/n: ")
            answer_bool = False
            if answer == 'y': answer_bool = True
            if answer_bool == q.correct_answer_flag:
                print("Correct!")
                num_correct_user_answers += 1
            else:
                print("Not correct!")
            n += 1
        print("Number of correct answers: ", num_correct_user_answers,
              " from ", len(self.questions_list))



quiz = Quiz(10)
quiz.start_quiz()