from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("", views.index, name="index_Emp"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register_view, name="register"),
    path("create_task", views.create_task_view, name="create_task"),
    path("create_order", views.create_order_view, name="create_order"),
    path("task_list", views.task_list_view, name="task_list"),
    path("task_emp_list", views.task_emp_list_view, name="task_emp_list"),
    path("order_list", views.order_list_view, name="order_list"),
]
