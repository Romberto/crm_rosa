from django.core.serializers import json
from django.http import JsonResponse, HttpResponse
from django.views.generic import DetailView

from django.core import serializers
from butler.views import auth_decoration
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.utils.datetime_safe import date
from django.views import View

from manager.forms import NewCaseForm, MoreAddressForm, MoreTegsForm, MoreCommentForm
from manager.models import CaseModel, CommentModel, StatusModel
from django.views.decorators.csrf import csrf_exempt

""" Представление личный кабинет менеджера"""


class Main(View):
    def get(self, request):
        user = request.user.username
        user_firstName = User.objects.get(username=user)

        data = {'user': user_firstName, 'today': date.today()}

        return render(request, 'manager/index.html', data)


""" Представление обрабатывает новую сделку у менеджера"""


class NewCase(View):
    @auth_decoration
    def get(self, request):
        data = {'form': NewCaseForm()}
        return render(request, 'manager/new_case.html', data)

    def post(self, request):
        form = NewCaseForm(request.POST)
        if form.is_valid():
            user = User.objects.get(username=request.user.username)
            status_begin = StatusModel.objects.get(status="start")
            new_case = CaseModel()
            new_case.manager = user
            new_case.farmerName = form.cleaned_data['farmerName']
            new_case.companyName = form.cleaned_data['companyName']
            new_case.phone = form.cleaned_data['phone']
            new_case.tegName = form.cleaned_data['tegName']
            new_case.status = status_begin
            new_case.save()
            return redirect('/manager/my_case/')
        else:
            return redirect('manager/new_case/')


""" Представление мои сделки - менеджер """


class MyCase(View):
    @auth_decoration
    def get(self, request):
        user = User.objects.get(username=request.user.username)
        all_my_cases = CaseModel.objects.filter(manager=user)
        count = all_my_cases.count()
        data = {'cases': all_my_cases, 'count': count}

        return render(request, 'manager/my_case.html', data)


""" Представление отображает детальную информацию одной конкретной сделки"""


class More(View):

    def get(self, request, pk):
        if request.user.is_authenticated:
            case = CaseModel.objects.get(id=pk)
            comments = CommentModel.objects.filter(case=case).order_by('-date_created')[:5]
            all_status = StatusModel.objects.all()
            form_more_contact = MoreAddressForm(instance=case)
            form_more_tags = MoreTegsForm(instance=case)
            form_more_comment = MoreCommentForm()
            data = {"case": case, "comments": comments, 'form_more_contact': form_more_contact,
                    'form_more_tags': form_more_tags, 'form_more_comment': form_more_comment,
                    'all_status': all_status}
            return render(request, 'manager/more.html', data)
        else:
            return redirect('/')


@csrf_exempt
def ajax_address(request):
    if request.method == "POST" and request.is_ajax():
        case_id = request.POST.get('case_id', None)

        case = CaseModel.objects.get(id=case_id)
        form = MoreAddressForm(request.POST)
        if form.is_valid():
            case.companyName = form.cleaned_data['companyName']
            case.farmerName = form.cleaned_data['farmerName']
            case.phone = form.cleaned_data['phone']
            case.mail = form.cleaned_data['mail']
            case.address = form.cleaned_data['address']
            case.save()
            response = case.as_json()

            return JsonResponse(response, status=200)
    return redirect('/')


@csrf_exempt
def ajax_tags(request):
    if request.method == "POST" and request.is_ajax():
        case_id = request.POST.get('case_id', None)
        case = CaseModel.objects.get(id=case_id)
        form = MoreTegsForm(request.POST)
        if form.is_valid():
            case.tegName = form.cleaned_data['tegName']
            case.save()
            response = case.as_json()

            return JsonResponse(response, status=200)
        return redirect('/')


@csrf_exempt
def ajax_comment(request):
    if request.method == "POST" and request.is_ajax():
        case_id = request.POST.get('case_id', None)

        form = MoreCommentForm(request.POST)
        if form.is_valid():
            case = CaseModel.objects.get(id=case_id)
            new_comment = CommentModel()
            new_comment.case = case
            new_comment.text_comment = form.cleaned_data['text_comment']
            new_comment.save()
            comment_all = CommentModel.objects.filter(case=case).order_by('-date_created')[:5]
            response = {}
            for item in comment_all:
                comment_json = item.as_json()
                response.update({item.id: [comment_json]})
            print(response)
            return JsonResponse(response, status=200)
        return redirect('/')


@csrf_exempt
def ajax_status(request):
    if request.method == "POST" and request.is_ajax():
        case_id = request.POST.get('case_id', None)
        name_btn = request.POST.get('nameBtn', None)
        case = CaseModel.objects.get(id=case_id)
        new_status = StatusModel.objects.get(status=name_btn)
        if case and new_status:
            case.status = new_status
            case.save()
            response = {'status': new_status.status, 'description': new_status.description}
            return JsonResponse(response, status=200)
