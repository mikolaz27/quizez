from quizez.models import Category, Question, Quiz


def sample_quiz(title, **params):
    defaults = {
        "description": "Some text",
        "category": Category.objects.create(),
    }
    defaults.update(params)
    return Quiz.objects.create(title=title, **defaults)


def sample_question(quiz, order_number, **params):
    defaults = {"text": "Some text"}
    defaults.update(params)
    return Question.objects.create(quiz=quiz, order_number=order_number, **defaults)
