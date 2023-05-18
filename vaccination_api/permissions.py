from rest_framework.permissions import BasePermission



class IsAdminRole(BasePermission):
    '''
    Allows access only to users who are Admin.
    '''
    def has_permission(self, request, view):
        tier = request.user.role
        is_true = ((tier == 1))
        return bool(is_true and request.user.is_authenticated)


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Allow GET, HEAD, or OPTIONS requests (read-only permissions)
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True

        # Check if the user is the owner of the object
        return obj.owner == request.user


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        return request.user and request.user.is_superuser

# class PostOnlyPermissions(BasePermssion):
#     def has_permission(self, request, view):
#         if self.action in ('create', ): // for POST method the action in DRF is create
#             return True
#         return False


# class IsOwner(permissions.BasePermission):
#     '''
#     Allows access only to users who are Admin.
#     '''
#     def has_permission(self, request, view):
#         return obj.own==request.user


# class IsPostOrIsAuthenticated(permissions.BasePermission):        

#     def has_permission(self, request, view):
#         # allow all POST requests
#         if request.method == 'POST':
#             return True

#         # Otherwise, only allow authenticated requests
#         # Post Django 1.10, 'is_authenticated' is a read-only attribute
#         return request.user and request.user.is_authenticated


# class IsObjectOwner(permissions.BasePermission):
#     def has_object_permission(self, request, view, obj):
#         # return super().has_object_permission(request, view, obj)
#         return obj.owner==request.user



# class IsVaccinecenterOwner(permissions.BasePermission):
#     def has_object_permission(self, request, view, obj):
#         # return super().has_object_permission(request, view, obj)
#         return obj.created_by==request.user

# class AdminOrReadonly(permissions.IsAdminUser):
#     def has_permission(self, request, view):
#         admin_permission = bool(request.user and request.user.is_staff)
#         return request.method == "GET" or admin_permission

# class IsAdminUserTest(permissions.BasePermission):
#     '''
#     Allows access only to users who are Tier 2 or above.
#     '''
    # def has_permission(self, request, view):
    #     if request.user.is_authenticated():
    #         role = request.user.role
    #         is_true = (role == 1)
    #         # return bool(is_true and request.user.is_authenticated)
    #         return bool(is_true)
    #     return False

    # def has_permission(self, request, view):
    #     if request.user.is_authenticated():
    #         return True
    
    # def has_object_permission(self, request, view, obj):
    #     if request.user.is_authenticated():
    #         role = request.user.role
    #         is_true = (role == 1)
    #         # return bool(is_true and request.user.is_authenticated)
    #         return bool(is_true)
        # return False


# class OwnerPermission(BasePermission):

#     def has_permission(self, request, view):

#         if view.basename == "product":
#             return bool(request.user and request.user.is_authenticated and request.user.is_owner)
#         return False

#     def has_object_permission(self, request, view, obj):

#         # Make sure that an owner can only modify and access its own products

#         if obj.shop.owner == request.owner:
#             return True

#         return False

# class ConsumerPermission(BasePermission):

#     def has_permission(self, request, view):
#         if view.basename == "product" and request.method in SAFE_METHODS:
#             return bool(request.user and request.user.is_authenticated and request.user.is_consumer)

#         return False   