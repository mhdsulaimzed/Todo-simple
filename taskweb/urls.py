from django.urls import path
from taskweb import views
urlpatterns=[
path("signup",views.SingupView.as_view(),name="register"),
path("",views.LoginView.as_view(),name="signin"),
path("index",views.IndexView.as_view(),name="home"),
path("task/add",views.TaskCreateView.as_view(),name="task-add"),
path("task/list",views.TaskListView.as_view(),name="task-list"),
path('task/det/<int:id>',views.TaskDetailView.as_view(),name="task-det"),
path('task/remove/<int:id>',views.TaskDeleteView.as_view(),name="task-del"),
path('task/<int:id>/change',views.TaskEditView.as_view(),name="task-edit"),
path('task/singout/',views.LogoutView.as_view(),name="sign-out")

]


