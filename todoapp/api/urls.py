
from django.urls import path 


from api.controllers import auth_controller, category_controller, task_controller

urlpatterns = [
    path('register/', auth_controller.register_user),
    path('login/', auth_controller.login_user),
    path('logout/', auth_controller.logout_user),
    path('update-password/', auth_controller.reset_password),
    path('update-profile/', auth_controller.edit_profile),
    path('user/', auth_controller.get_user_profile),
    path('delete-user/', auth_controller.delete_user),
    path('users/', auth_controller.user_listing),

    path('categories/', category_controller.add_category),
    path('category/', category_controller.edit_category),
    path('delete-category/', category_controller.delete_category),
    path('get-categories/', category_controller.get_category),
    
    path('tasks/',task_controller.add_task),
    path('edit-task/',task_controller.edit_task),
    path('get-tasks/',task_controller.get_tasks),
    path('delete-task/',task_controller.delete_task),
    
]
