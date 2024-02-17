from rest_framework import serializers
from watchlist_app.models import WatchList, Review
from rest_framework import validators
from watchlist_app.models import StreamPlatform

# ------- Using ModelSerializer Class ---------

class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Review
        exclude = ['watchlist']
        

class WatchListSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    
 
    class Meta:
        model = WatchList
        fields = ['name','description','active','time', 'platform', 'created', 'reviews', 'avg_rating', 'num_of_rating']
        
        
class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist = WatchListSerializer(many=True, read_only=True)
    
    class Meta:
        model = StreamPlatform
        fields = ['name', 'about', 'website', 'watchlist']
    

# ------- Using Serializer Class --------- 

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
    