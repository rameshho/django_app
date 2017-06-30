from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from django.core.urlresolvers import reverse_lazy
from .models import Album
from .forms import UserForm

class IndexView(generic.ListView):
    '''
        As in index we have list of albums, we are importing listview from generic, and creating class
    '''
    template_name = 'music/index.html'
    context_object_name = 'all_albums'

    def get_queryset(self):
        '''
            Going to query the database for whatever albums we have and returns all the objects
        :return:
        '''
        return Album.objects.all()


class DetailView(generic.DetailView):
    '''
        This DetailView will get details of one object
        what model and what object you are trying to get details of need to mention
    '''

    model = Album
    template_name = 'music/detail.html'

class AlbumCreate(CreateView):
    '''
        It will create the new Album entry.
    '''

    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']


class AlbumUpdate(UpdateView):
    '''
        It will Update the existing Album entry.
    '''

    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']


class AlbumDelete(DeleteView):
    '''
        It will delete the existing Album.
    '''

    model = Album

    #It will take you to the home page after deleting an object.
    success_url = reverse_lazy('music:index')

class UserFormView(View):
    '''What is the blue print of the form'''
    form_class = UserForm
    template_name = 'music/registration_form.html'

    #display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    #Fill the form and post it. process form data
    def post(self, request):
        form = self.form_class(request.Post)

        if form.is_valid():
            #It creates an object from the form, and it doesn't save it to database.
            user = form.save()

            # cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.username = 'Ramesh'
            user.set_password(password)

            #This will save user to database
            user.save()

            #returns User Objects if credentials are correct.
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('music:index')

        return render(request, self.template_name, {'form': form})