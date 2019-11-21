from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect, get_list_or_404
from .models import Faculty
from .forms import SearchForm
from django.http.response import Http404

# Create your views here.
@login_required
def search_faculty(request):
    '''
    Seach the faculty by first_name, last_name and department
    '''

    form = SearchForm()
    f_name = l_name = dept = None
    results = []
    # Need to validate in a different way
    if 'first_name' in request.GET:
        form = SearchForm(request.GET)
        form.full_clean()
        
        if form.cleaned_data['first_name']!='' and form.cleaned_data['last_name']!='' \
            and form.cleaned_data['department'] != '':
            f_name = form.cleaned_data['first_name']
            l_name = form.cleaned_data['last_name']
            dept = form.cleaned_data['department']
            results = get_list_or_404(Faculty,faculty_department=dept,\
                faculty_fname=f_name,faculty_lname=l_name)

        else:
            try:
                if form.cleaned_data['first_name']!='' and form.cleaned_data['last_name']!='':
                    results = get_list_or_404(Faculty,faculty_fname=\
                            form.cleaned_data['first_name'],
                            faculty_lname=form.cleaned_data['last_name'])
                elif form.cleaned_data['first_name']!='' and form.cleaned_data['department']!='':
                    results = get_list_or_404(Faculty,faculty_fname=\
                            form.cleaned_data['first_name'],
                            faculty_department=form.cleaned_data['department'])
                elif form.cleaned_data['last_name']!='' and form.cleaned_data['department']!='':
                    results = get_list_or_404(Faculty,faculty_lname=\
                            form.cleaned_data['last_name'],
                            faculty_department=form.cleaned_data['department'])
                elif form.cleaned_data['first_name']!='' and form.cleaned_data['last_name']=='' and\
                    form.cleaned_data['department']=='':
                    results = get_list_or_404(Faculty,faculty_fname=\
                            form.cleaned_data['first_name'])
                elif form.cleaned_data['last_name']!='' and form.cleaned_data['department']=='' and \
                    form.cleaned_data['first_name']=='':
                    results = get_list_or_404(Faculty,faculty_lname=\
                            form.cleaned_data['last_name'])
                elif form.cleaned_data['department']!='' and form.cleaned_data['first_name']=='' and\
                    form.cleaned_data['last_name']=='':
                    results = get_list_or_404(Faculty,
                            faculty_department=form.cleaned_data['department'])
            except Http404:
                raise Http404("No match is availabe for the given query %s %s %s" \
                    %(form.cleaned_data['first_name'],form.cleaned_data['last_name'],\
                        form.cleaned_data['department']))
            
            print(results)
    return render(request,'faculty/search.html',{'form':form,\
            'results':results})