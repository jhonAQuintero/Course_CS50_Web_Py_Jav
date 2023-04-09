from django.shortcuts import render, HttpResponse
from django import forms
from . import util
from django.core.handlers.wsgi import WSGIRequest
from io import StringIO
import random
import markdown2

class search_form(forms.Form):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Search Encyclopedia'}))

class create_form(forms.Form):
    entry =  forms.CharField(widget=forms.TextInput(attrs={'name':'entry'}))
    body = forms.CharField(label='', widget=forms.Textarea(attrs={'name':'body', 'rows': 8, 'cols': 3}))
    
class edit_form(forms.Form):
    def __init__(self, entry = '', body = '', *args, **kwargs):
        super().__init__(*args, **kwargs) #Llamamos al a la clase superpadre
        self.fields['entry'] =  forms.CharField(widget=forms.TextInput(attrs={'name':'entry'}), initial=entry)
        self.fields['body'] = forms.CharField(label='', widget=forms.Textarea(attrs={'name':'body', 'rows': 8, 'cols': 3}), initial=body)


def index(request):
    form = search_form()
    return render(request, "encyclopedia/index.html", {
        'entries': util.list_entries(),
        'form' : form
    })


def entry_page(request, title):
    form = search_form()
    entry = markdown2.markdown(util.get_entry(title))
    if not entry:
        entry='There is no exact information about this entry in our encyclopedia'
        
        context={'form': form, 'title': title, 'entry': entry, 'classStyle': 'red'}
    else:
        context={'form': form, 'title': title, 'entry': entry, 'editPage': True}
    return render(request, template_name="encyclopedia/page.html", context=context)


def search_page(request):
    if request.method == 'POST':
        form = search_form(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            entry = util.get_entry(title)
            if entry:
                entry_mrk =  markdown2.markdown(entry)
                return render(request, template_name="encyclopedia/page.html", context={'form': form, 'title': title, 'entry': entry_mrk, 'editPage': True})
            else:
                entry = 'There is no exact information about this entry in our encyclopedia'
                context={'form': form, 'title': title, 'entry': entry, 'classStyle': 'red'}
            entries_search = []
            for item in util.list_entries():
                if item.lower().find(title.lower()) != -1:
                    entries_search.append(item)
            context['entries_search'] = entries_search
            return render(request, template_name="encyclopedia/page.html", context=context)
    else:
        form = search_form()
        return render(request, 'encyclopedia/index.html', {'entries': util.list_entries(),'form' : form})
    

def form_create_page(request):
    if request.method == 'POST':
        form = search_form()
        form_page = create_form(request.POST)
        if form_page.is_valid():
            title = form_page.cleaned_data['entry']
            body = form_page.cleaned_data['body']
            entry = util.get_entry(title)
            if entry:
                body = 'This entry already exists'
                context={'form': form, 'title': title, 'entry': body, 'classStyle':'red'}
                return render(request, template_name="encyclopedia/page.html", context=context)
        
            util.save_entry(title=title, content=body)
            entry_mrk = markdown2.markdown(body)
            context={'form': form, 'title': title, 'entry': entry_mrk}
            return render(request, template_name="encyclopedia/page.html", context=context)
    else:
        form = search_form()
        form_page = create_form()
        return render(request, 'encyclopedia/handlepage.html', {'form' : form, 'form_page' : form_page})
    

def form_edit_page(request, title):
    form = search_form()
    if request.method == 'POST':
        util.save_entry(title=title, content=request.POST['body'])
        context={'form': form, 'title': title, 'entry': request.POST['body'], 'is_edited': True}
        return render(request, template_name="encyclopedia/page.html", context=context)
    else:
        entry = util.get_entry(title)
        form_page = edit_form(title, entry)
        return render(request, 'encyclopedia/handlepage.html', {'form' : form,'form_page' : form_page})


def random_page(request):
    form = search_form()
    entries = util.list_entries()
    rdn_entry = entries[random.randint(0, len(entries) - 1)]
    entry = util.get_entry(rdn_entry)
    entry_mrk =  markdown2.markdown(entry)
    context={'form': form, 'title': rdn_entry, 'entry': entry_mrk, 'editPage': True}
    return render(request, template_name="encyclopedia/page.html", context=context)
    
    
    

