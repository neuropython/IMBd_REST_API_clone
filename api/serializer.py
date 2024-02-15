from rest_framework import serializers
from watchlist_app.models import WatchList
from rest_framework import validators
from watchlist_app.models import StreamPlatform
    
class WatchListSerializer(serializers.ModelSerializer):
    lenght = serializers.SerializerMethodField()
    
    class Meta:
        model = WatchList
        fields = '__all__'
        
    def get_lenght(self,object):
        return len(object.name)
    
    def validate(self,data):
        if data['name'] == data['description']:
            raise serializers.ValidationError('Name and Description should be different')
        else:
            return data
        
    def validate_name(self,value):
        if len(value) < 2:
            raise serializers.ValidationError('Name is too short')
        else:
            return value

class StreamPlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = StreamPlatform
        fields = '__all__'
    
    def validate_name(self,value):
        if len(value) < 2:
            raise serializers.ValidationError('Name is too short')
        else:
            return value

    
# def name_length(value):
#     if len(value) < 2:
#         raise serializers.ValidationError('Name is too short')
#     else:
#         return value

# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField()
    
#     def create (self,validated_data):
#         return Movies.objects.create(**validated_data)
    
#     def update(self,instance,validated_data):
#         instance.name = validated_data.get('name',instance.name)
#         instance.description = validated_data.get('description',instance.description)
#         instance.active = validated_data.get('active',instance.active)
#         instance.save()
#         return instance
    
#     def validate(self,data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError('Name and Description should be different')
#         else:
#             return data
    