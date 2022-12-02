
import traceback

from django.views.decorators.csrf import csrf_exempt
from api.controllers.classes.task import Tasks

from api.decorators.decorators import auth_api
from api.exceptions.general_exception import GeneralException
from api.services.api_response import ApiResponse


@csrf_exempt
@auth_api
def add_task(request):
    try:

        task = Tasks(request)
        return task.add_task()

    except GeneralException as e:
        return ApiResponse.general_error(message = e.message)

    except BaseException as e:
        tb = traceback.format_exc()
        print(tb)

        return ApiResponse.internal_error(e, message=e.message)

@csrf_exempt
@auth_api
def edit_task(request):
    try:

        task = Tasks(request)
        return task.update_task()

    except GeneralException as e:
        return ApiResponse.general_error(message = e.message)

    except BaseException as e:
        tb = traceback.format_exc()
        print(tb)

        return ApiResponse.internal_error(e, message=e.message)

@csrf_exempt
@auth_api
def get_tasks(request):
    try:

        task = Tasks(request)
        return task.task_listing()

    except GeneralException as e:
        return ApiResponse.general_error(message = e.message)

    except BaseException as e:
        tb = traceback.format_exc()
        print(tb)

        return ApiResponse.internal_error(e, message=e.message)

@csrf_exempt
@auth_api
def delete_task(request):
    try:

        task = Tasks(request)
        return task.dlt_task()

    except GeneralException as e:
        return ApiResponse.general_error(message = e.message)

    except BaseException as e:
        tb = traceback.format_exc()
        print(tb)

        return ApiResponse.internal_error(e, message=e.message)

