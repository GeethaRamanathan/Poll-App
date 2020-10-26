from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic
from .models import Choice,Question

def home(reqeust):
    return HttpResponse("Welcome")

class PollListView(generic.ListView):
    model = Question

class PollDetailView(generic.DetailView):
    model = Question

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except KeyError:
        return render(request, 'pollapp/question_detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.vote_count += 1
        selected_choice.save()
        return redirect("poll:poll_result",question_id)

class PollResultView(generic.DetailView):
    model = Question
    template_name = "pollapp/result_list.html"




