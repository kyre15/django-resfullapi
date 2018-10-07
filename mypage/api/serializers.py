from rest_framework import serializers
from mypage.models import post

class postserializer(serializers.ModelSerializer):
    class Meta:
        model = post
        fields = ('title', 'content')
