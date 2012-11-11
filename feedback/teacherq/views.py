import json
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, get_object_or_404, render
from django.template import Context, loader, RequestContext
from teacherq.models import Question, AnswerOption, ActiveQuestion, UserProfile

def index(request):
	questions = {}

	for question in Question.objects.all():
		questions[question.id] = question.question

	return render_to_response('teacherq/index.html', 
		{"questions" : questions})

def askquestion(request):
	return render_to_response('teacherq/ask_question.html', {})

def submitquestion(request):
	q = request.GET['question']
	newquestion = Question(question = q)
	newquestion.save()
	
	ans_a = AnswerOption(question=newquestion, answer=request.GET['ans_a'], count=0)
	ans_b = AnswerOption(question=newquestion, answer=request.GET['ans_b'], count=0)
	ans_c = AnswerOption(question=newquestion, answer=request.GET['ans_c'], count=0)
	ans_d = AnswerOption(question=newquestion, answer=request.GET['ans_d'], count=0)
	ans_a.save()
	ans_b.save()
	ans_c.save()
	ans_d.save()
	
	
	return HttpResponse(newquestion.__unicode__() + ' added to database')
	#return render_to_response('teacherq/index.html', {})

def viewquestion(request):
	params = {}

	try:
		active_question = ActiveQuestion.objects.get()
		answer_options = AnswerOption.objects.filter(question=active_question)
		params = {
				'active_question': active_question,
				'answer_options': answer_options
				}
	except Exception, e:
		pass

	return render(request, 'teacherq/viewactive.html', params)
 
def submitanswer(request):
	id = request.GET['answer']
	answer = AnswerOption.objects.get(id=id)
	answer.count = answer.count + 1
	answer.save()
	return HttpResponse('question answered')


def showanswers(request):
 	id = request.GET['id']

 	question = Question.objects.get(id=id)
 
	answers = {}

 	for ans in AnswerOption.objects.filter(question__id=id):
 	 	answers[ans.answer] = ans.count

 	return render(request, 'teacherq/show_answers.html', {
 		'question' : question.question,
 		'answers': answers,
 		})

def confusedstudents(request):
	confused_users = UserProfile.objects.filter(is_confused=True).count()
	total_users = UserProfile.objects.all().count()
	confusion_level = confused_users * 100 / total_users

	response = { 'confusionLevel' : confusion_level }
	return HttpResponse(json.dumps(response), mimetype='application/json')


def showconfusion(request):
	return render(request, 'teacherq/showconfusion.html', {} )

