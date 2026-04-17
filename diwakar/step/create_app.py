# step 1:-
#          create a project.

# step 2:-
#          command = cd _____(project name) /change directory 

# step 3:-
#         python manage.py startaap _______(app name)

# step 4:-
#         register app in proj setting.py 

#                  Open settings.py and add:-
#         INSTALLED_APPS = [ 
#                              'myapp',
#                             ]

# step 5:-
#         cteate  a view
#                     In views.py file:-

        # from django.http import HttpResponse
         
        # def home(request):
        #     return HttpResponse("Hello, Django!")

# step 6:-
#         connect url (update project urls.py)
#         Edit urls.py file:
#         from django.contrib import admin
#         from django.urls import path
#         from myapp.views import home
        
#         urlpatterns = [
#            path('admin/', admin.site.urls),
#            path('', home),
#         ]

      
# step 7 :-
#           python manage.py runserver
#          👉 Open:
#          http://127.0.0.1:8000/

# step 8:-
#        open new terminal and change direcotory
#        cd diwakar (project name)

# step 9:-
#        run 2 command.
#        1. python manage.py makemigration
#        2. python manage.py migrate
#  step 10:-
#        create super user .
#       command = python manage.py createsuperuser

# step 11:- 
#          python manage.py runserver
# #          👉 Open:
# #          http://127.0.0.1:8000/
        
 
