from rest_framework.routers import DefaultRouter
from todo.views import TodoViewSet

router = DefaultRouter()

app_name = "todolistapp"


router.register(
    prefix="todolist",
    viewset=TodoViewSet,
    basename="todolist",
)

urlpatterns = router.urls
