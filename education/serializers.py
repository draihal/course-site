from rest_framework import serializers

from education.models import Group


class GroupShortSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Group
        fields = ['id', 'url', 'name', 'category', ]

    def get_url(self, obj):
        request = self.context.get("request")
        return obj.get_api_url(request=request)
