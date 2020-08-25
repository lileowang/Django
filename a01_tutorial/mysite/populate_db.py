from django.utils import timezone
from polls.models import Question, Choice

# populate Question table
Question.objects.all().delete()
q = Question(question_text='q1', pub_date=timezone.now())
q.save()
q = Question(question_text='q2', pub_date=timezone.now())
q.save()
q = Question(question_text='q3', pub_date=timezone.now())
q.save()

q = Question.objects.all()
print('Question fields: id, question_text, pub_date')
for d in q:
    print(d.id, d.question_text, d.pub_date)

# populate Choice table
Choice.objects.all().delete()
q = Question.objects.get(question_text='q1')
q.choice_set.create(choice_text='c11', votes=0)
q.choice_set.create(choice_text='c12', votes=0)
q.choice_set.create(choice_text='c12', votes=0)

q = Question.objects.get(question_text='q2')
q.choice_set.create(choice_text='c21', votes=0)
q.choice_set.create(choice_text='c22', votes=0)
q.choice_set.create(choice_text='c22', votes=0)

q = Question.objects.get(question_text='q3')
q.choice_set.create(choice_text='c31', votes=0)
q.choice_set.create(choice_text='c32', votes=0)
q.choice_set.create(choice_text='c32', votes=0)

c = Choice.objects.all()
print('Choice fields: id, question, choice_text, votes')
for d in c:
    print(d.id, d.question, d.choice_text, d.votes)
