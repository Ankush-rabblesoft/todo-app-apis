
import traceback

from django.views.decorators.csrf import csrf_exempt
from api.controllers.classes.category import Category

from api.decorators.decorators import auth_api
from api.exceptions.general_exception import GeneralException
from api.services.api_response import ApiResponse


@csrf_exempt
@auth_api
def add_category(request):
    try:

        cat = Category(request)
        return cat.add_category()

    except GeneralException as e:
        return ApiResponse.general_error(message = e.message)

    except BaseException as e:
        tb = traceback.format_exc()
        print(tb)

        return ApiResponse.internal_error(e, message=e.message)

@csrf_exempt
@auth_api
def edit_category(request):
    try:

        auth = Category(request)
        return auth.update_category()

    except GeneralException as e:
        return ApiResponse.general_error(message = e.message)

    except BaseException as e:
        tb = traceback.format_exc()
        print(tb)

        return ApiResponse.internal_error(e, message=e.message)

@csrf_exempt
@auth_api
def delete_category(request):
    try:

        auth = Category(request)
        return auth.dlt_category()

    except GeneralException as e:
        return ApiResponse.general_error(message = e.message)

    except BaseException as e:
        tb = traceback.format_exc()
        print(tb)

        return ApiResponse.internal_error(e, message=e.message)

@csrf_exempt
@auth_api
def get_category(request):
    try:

        auth = Category(request)
        return auth.get_categories()

    except GeneralException as e:
        return ApiResponse.general_error(message = e.message)

    except BaseException as e:
        tb = traceback.format_exc()
        print(tb)

        return ApiResponse.internal_error(e, message=e.message)