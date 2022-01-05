from rest_framework.serializers import ModelSerializer
from.models import goods

class goodsSerializers(ModelSerializer):
    class Meta:
        model=goods
        fields="__all__"