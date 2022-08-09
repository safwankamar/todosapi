from django.urls import path
from todo import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('todosviewset',views.TodoViewSet,basename='todoviewset')
router.register("todosmodelviewset",views.TodoModelViewSet,basename="todomodel"
                                                                    "viewset")

urlpatterns=[
    path('todo',views.TodosView.as_view()),
    path('todo/<int:todo_id>',views.TodoDetail.as_view()),
    path('users/accounts/signup',views.UserCreationView.as_view()),
    path('users/accounts/login',views.SigninView.as_view()),
    path('todosmixin',views.TodosMixinView.as_view()),
    path('todosmixin/details/<int:todo_id>',views.TodominDetailsView.as_view()),
]+router.urls