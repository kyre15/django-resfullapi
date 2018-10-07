from rest_framework.generics import ListAPIView, RetrieveAPIView
from mypage.models import post
from .serializers import postserializer

class postListView(ListAPIView):
    queryset = post.objects.all()
    serializer_class = postserializer

class postDetailView(RetrieveAPIView):
    queryset = post.objects.all()
    serializer_class = postserializer