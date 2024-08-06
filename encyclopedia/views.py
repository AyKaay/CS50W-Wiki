import markdown2
import random

from django import forms
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, redirect
from django.urls import reverse

from . import util, forms
from .forms import EntryForm
def index(request):
    
    return render(request, "encyclopedia/index.html", {"entries": util.list_entries()
    })
    
def about_page(request):
    
    return render(request, "encyclopedia/about_page.html")

# Render an entry when clicked
def entry_page(request, title):
    content = util.get_entry(title)
    if content is None:
        raise Http404("Entry not found")
    
    entry_html = markdown2.markdown(content)
    return render(request, "encyclopedia/entry_page.html",{
        "title": title,
        "content": entry_html,
    })

# Search for typed entry
def search(request):
    query = request.GET.get('q','')
    if query:
        entries = util.list_entries()
        # Dont understand how this works. edit: apparently it's called 'list comprehension'
        matching_entries = [entry for entry in entries if query.lower() in entry.lower()] 
        if len(matching_entries) == 1 and matching_entries[0].lower == query.lower():
            # Redirect to the entry page if there's an exact match
            return redirect('entry_page', title=matching_entries[0])
        else:
            return render(request, "encyclopedia/search_results.html", {
                "query": query,
                "entries": matching_entries,
            })
    else:
        return redirect('index')
    

# Making new entry (kinda broken, dont touch!)
def new_page(request,title):
    context = {
        'title': 'new_page',
        'message': "Welcome to the new page!"
    }
    return render(request, 'encyclopedia/new_page.html', context)

# Making new entry
def create_entry(request):
    # Links to forms.py
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            util.save_entry(title, content)
            return redirect('index')
    else:
        form = EntryForm()
    return render(request, 'encyclopedia/new_page.html', {'forms': form})

# Edit existing entry
def edit_entry(request, title):
    if request.method == 'POST':
        #existing_content = util.get_entry(title)
        title = request.POST['title']
        content = request.POST['content']
        util.save_entry(title, content)
        return redirect('index')
    
    else:
        existing_content = util.get_entry(title)
        if existing_content:
            initial_data = {
                'title': title,
                'content': existing_content,                
            }
            form = EntryForm(initial = initial_data)
            return render(request, 'encyclopedia/edit_entry.html',{
                'form': form,
            })
        else:
            raise Http404("Entry not found")

# Randomly direct to existing entry       
def random_entry(request):
    # Be advised, these are not using random.choice
    entries = util.list_entries()
    entry_number_map = {}
    number = 1
    entries_number = len(entries)
    
    # Assigning entries with numbers in a dictionary
    for entry in entries:
        entry_number_map[entry] = number
        number += 1

    # Randomizing the value to get the key
    random_int = random.randint(1, entries_number) 
    random_entry_title = entries[random_int - 1]
    return redirect('entry_page', title=random_entry_title)