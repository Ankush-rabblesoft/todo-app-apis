
from api.exceptions.general_exception import GeneralException
from api.services.api_response import ApiResponse
from api.services.token_service import TokenService
from api.models import TaskCategory

class Category():

    request = None
    token_service = None

    def __init__(self, request):

        self.request = request
        self.token_service = TokenService()

    def add_category(self):
        
        request = self.request
        request_data = request.json

        if not request_data:
            raise GeneralException("Request data not valid")

        if not request.method=="POST":
            raise GeneralException("Request method should be POST")
            
        categ = request_data.get("category")

        if not categ:
            raise GeneralException("category field is required")

        token = self.token_service.get_token_from_request(request)
        
        if not token:
            return ApiResponse.general_error(message="Not a valid token")

        user = self.token_service.get_user_from_token(token)

        if not user:
            return ApiResponse.general_error(message="User not found with this token")

        cate = TaskCategory()
        cate.user_id = user.id
        cate.category = categ
        cate.save()

        return ApiResponse.success(message="category added successfully")
    
    def update_category(self):
        
        request = self.request
        request_data = request.json

        if not request_data:
            raise GeneralException("Request data not valid")

        if not request.method=="POST":
            raise GeneralException("Request method should be POST")
            
        category = request_data.get("category")

        token = self.token_service.get_token_from_request(request)
        
        if not token:
            return ApiResponse.general_error(message="Not a valid token")

        user = self.token_service.get_user_from_token(token)

        if not user:
            return ApiResponse.general_error(message="User not found with this token")

        cat_id = request.GET.get('cat_id')
        
        if cat_id=="1":
            raise GeneralException("Can-not Change global category")

        if not cat_id:
            raise GeneralException(" query string parameter cat_id is missing")

        cate = TaskCategory.objects.filter(id = request.GET.get('cat_id')).first()
        
        if not cate:
            raise GeneralException("No category with this ID")
        
        cate.category = category
        cate.save()

        cate_details ={
                "id" : cate.id,
                "category": cate.category,
                "user_id": cate.user_id
            }

        return ApiResponse.success(data=cate_details, message="Category updated successfully")

    def dlt_category(self):
        
        request = self.request
       
        token = self.token_service.get_token_from_request(request)
        
        if not token:
            return ApiResponse.general_error(message="Not a valid token")

        user = self.token_service.get_user_from_token(token)

        if not user:
            return ApiResponse.general_error(message="User not found with this token")

        cat_id = request.GET.get('cat_id')
        
        if cat_id=="1":
            raise GeneralException("Can-not Delete global category")

        if not cat_id:
            raise GeneralException("Parameter cat_id is missing")

        cate = TaskCategory.objects.filter(id = request.GET.get('cat_id')).first()

        cate.delete()

        return ApiResponse.success(message="User Deleted Successfully")

    def get_categories(self):
        
        request = self.request
       
        token = self.token_service.get_token_from_request(request)
        
        if not token:
            return ApiResponse.general_error(message="Not a valid token")

        user = self.token_service.get_user_from_token(token)

        if not user:
            return ApiResponse.general_error(message="User not found with this token")

        cate = TaskCategory.objects.filter(user = user.id)
            
        categories = []

        for cat in cate:
            cate_details ={
                "id" : cat.id,
                "category": cat.category,
                "user_id": cat.user_id
            }
            categories.append(cate_details)

        return ApiResponse.success(data=categories)
