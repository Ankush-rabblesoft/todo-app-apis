
from api.exceptions.general_exception import GeneralException
from api.forms.add_task_form import TaskForm
from api.models import Task, TaskCategory, TaskPriority
from api.services.api_response import ApiResponse
from api.services.token_service import TokenService
from api.controllers.classes.auth import striphtml


class Tasks():

    request = None
    token_service = None

    def __init__(self, request):

        self.request = request
        self.token_service = TokenService()

    def add_task(self):
        
        request = self.request
        request_data = request.json

        if not request_data:
            raise GeneralException("Request data not valid")

        if not request.method=="POST":
            raise GeneralException("Request method should be POST")
            
        title = request_data.get("title")
        description = request_data.get("description")
        time= request_data.get("time")
        category_id = request_data.get("category_id",1)
        tag = request_data.get("tag")
        pin_status = request_data.get("pin_status",0)
        priority_id = request_data.get("priority_id", 4)
        
        token = self.token_service.get_token_from_request(request)
        
        if not token:
            return ApiResponse.general_error(message="Not a valid token")

        user = self.token_service.get_user_from_token(token)

        if not user:
            return ApiResponse.general_error(message="User not found with this token")

        form = TaskForm(request_data)

        if not form.is_valid():

            message = "Parameter missing"
            messages = {}
            for error in form.errors:
               messages[error] = striphtml(str(form.errors[error]))

            raise GeneralException({
                    "message": message,
                    'errors': messages
                })

        category = TaskCategory.objects.filter(id = category_id).first()

        if not category:
            raise GeneralException("No category with this category_id")

        priority = TaskPriority.objects.filter(id = priority_id).first()

        if not priority:
            raise GeneralException("No priority type with this priority_id")

        task = Task()
        task.title = title
        task.description = description
        task.time = time
        task.user_id = user.id
        task.category_id = category_id
        task.tag = tag
        task.priority_id = priority_id
        task.pin_status = pin_status
        task.save()

        task_details ={
            "id" : task.id,
            "title": task.title,
            "description": task.description,
            "time": task.time,
            "tag": task.tag,
            "category_id": task.category_id,
            "pin_status": task.pin_status,
            "tag": task.tag,
            "priority_id": task.priority_id,
            "user_id":task.user_id
            }
            
        task_details['user'] = {
        "id": task.user.id,
        "name": task.user.name,
        "email": task.user.email,
        "phone": task.user.phone
        }

        return ApiResponse.success(data=task_details, message="Task added successfully")

    def update_task(self):
        
        request = self.request
        request_data = request.json

        if not request_data:
            raise GeneralException("Request data not valid")

        if not request.method=="POST":
            raise GeneralException("Request method should be POST")

        task_id = request.GET.get('task_id')
    
        if not task_id:
            raise GeneralException(" Query string parameter task_id missing")

        task = Task.objects.filter(id =task_id).first()
        
        if not task:
            raise GeneralException("No task with this Task ID")

        title = request_data.get("title", task.id) 
        description = request_data.get("description", task.description)
        time= request_data.get("time", task.time)
        category_id = request_data.get("category_id", task.category_id)
        tag = request_data.get("tag", task.tag)
        pin_status = request_data.get("pin_status", task.pin_status)
        priority_id = request_data.get("priority_id", task.priority_id)
        
        token = self.token_service.get_token_from_request(request)
        
        if not token:
            return ApiResponse.general_error(message="Not a valid token")

        user = self.token_service.get_user_from_token(token)

        if not user:
            return ApiResponse.general_error(message="User not found with this token")

        category = TaskCategory.objects.filter(id = category_id).first()

        if not category:
            raise GeneralException("No category with this category_id")
        
        priority = TaskPriority.objects.filter(id = priority_id).first()

        if not priority:
            raise GeneralException("No priority type with this priority_id")

        task.title = title
        task.description = description
        task.time = time
        task.category_id = category_id
        task.tag = tag
        task.pin_status = pin_status
        task.priority_id = priority_id
        task.save()

        task_details ={
            "id" : task.id,
            "title": task.title,
            "description": task.description,
            "time": task.time,
            "tag": task.tag,
            "category_id": task.category_id,
            "pin_status": task.pin_status,
            "tag": task.tag,
            "priority_id": task.priority_id,
            "user_id":task.user_id
            }
            
        task_details['user'] = {
        "id": task.user.id,
        "name": task.user.name,
        "email": task.user.email,
        "phone": task.user.phone
        }

        return ApiResponse.success(data=task_details, message="Task updated successfully")

    def task_listing(self):
        
        request = self.request

        if not request.method=="GET":
            raise GeneralException("Request method should be GET")
        
        token = self.token_service.get_token_from_request(request)
        
        if not token:
            return ApiResponse.general_error(message="Not a valid token")

        user = self.token_service.get_user_from_token(token)

        if not user:
            return ApiResponse.general_error(message="User not found with this token")

        tasks = Task.objects.filter(user_id =user.id)
        
        tasks_list = []

        for task in tasks:
            task_details ={
                "id" : task.id,
                "title": task.title,
                "description": task.description,
                "time": task.time,
                "tag": task.tag,
                "category": task.category.category,
                "category_id": task.category_id,
                "pin_status": task.pin_status,
                "tag": task.tag,
                "priority_id": task.priority_id,
            }
            
            task_details['user'] = {
            "id": task.user.id,
            "name": task.user.name,
            "email": task.user.email,
            "phone": task.user.phone
            }

            tasks_list.append(task_details)

        return ApiResponse.success(data=tasks_list)

    def dlt_task(self):
        
        request = self.request
        
        token = self.token_service.get_token_from_request(request)
        
        if not token:
            return ApiResponse.general_error(message="Not a valid token")

        user = self.token_service.get_user_from_token(token)

        if not user:
            return ApiResponse.general_error(message="User not found with this token")
        
        task_id = request.GET.get('task_id')
    
        if not task_id:
            raise GeneralException(" Query string parameter task_id missing")
        
        task = Task.objects.filter(id =task_id).first()
        
        if not task:
            raise GeneralException("No task with this Task Id")

        task.delete()

        return ApiResponse.success(message="Task Deleted successfully")    
