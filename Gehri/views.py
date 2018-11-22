# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404

# Create your views 
from django.http import HttpResponseRedirect, HttpResponse
from django.http import Http404
from django.urls import reverse
from django.template import loader

from Gehri.models import Question,Choice
from django.views import generic



class IndexView(generic.ListView):
	template_name = 'Gehri/index.html'
	context_object_name = 'latest_question_list'

	def get_queryset(self):
		return Question.objects.order_by('pub_date')[:5]
	
	

class DetailView(generic.DetailView):
	model = Question
	template_name = 'Gehri/detail.html'

class ResultsView(generic.DetailView):
	model = Question
	template_name = 'Gehri/results.html'

def vote(request, question_id):
	question = get_object_or_404(Question, pk= question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
			return render(request, 'Gehri/detail.html', {
				'question': question,
				'error_message':"You didn't select a choice",
				})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		return HttpResponseRedirect(reverse('Gehri:results', args=(question.id,)))


