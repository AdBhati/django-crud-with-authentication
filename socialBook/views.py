from django.shortcuts import render
from rest_framework import serializers, viewsets
from rest_framework.response import Response
from socialBook.models import Upload,Comment,Like
from user.models import User
from django.db.models import Count

class UploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Upload
        fields = "__all__"

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = "__all__"

class UploadViewset(viewsets.ModelViewSet):
    serializer_class = UploadSerializer
    model = Upload

    def create(self, request):
        serializer = UploadSerializer(data = request.data)
        # existing_post = Upload.objects.filter(id=request.data.get('id'))
        # if existing_post:
        #     return Response("This Post is Already Uploaded")
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


    def view_all(self, request):
        allPost = Upload.objects.all()
        serializer = UploadSerializer(allPost, many=True).data
        return Response(serializer)

    def view_by_id(self,request,pk):
        # post = Upload.objects.get(pk=pk)
        post = Upload.objects.filter(id=pk)
        # if not post.exists():
        #     return Response({'detail': 'Post not found.'}, status=status.HTTP_404_NOT_FOUND)
        serializer = UploadSerializer(post, many=True).data
        return Response(serializer)

    def partial_update(self, request,pk):
        post = Upload.objects.get(pk=pk)
        if not post:
            return Response('Post not found')
        serializer = UploadSerializer(post, data= request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class CommentViewset(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    model = Comment

    def create(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def view_all(self, request):
        comment = Comment.objects.all()
        serializer = CommentSerializer(comment, many=True).data
        return Response(serializer)

    def view_user_comment(self, request, pk):
        comment = Comment.objects.get(pk=pk)
        serializer = CommentSerializer(comment, many=True).data
        return Response(serializer)

    def partial_update(self, request, pk):
        comment = Comment.objects.get(pk=pk)
        if not comment:
            return Response('Comment not found')
        serializer = CommentSerializer(comment, data=request.data, partial=True)   
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class LikeViewSet(viewsets.ModelViewSet):
    serializer_class= LikeSerializer
    model = Like

    def like_post(self, request):
        # user_id = User.objects.get(pk=request.data['user'])
        # print("user===>",user_id)
        # post_id = Upload.objects.get(pk=request.data['post'])
        # print("post===>",post_id)

        existing_like= Like.objects.filter(user=request.data['user'], post=request.data['post'])
        # print('existing_like ==>> ', existing_like[0])
        if existing_like:
            return Response("User Already Liked the post")

        serializer = LikeSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def like_post_by_user(self, request,pk):
        user_liked_post= Like.objects.filter(user = pk)
        serializer=LikeSerializer(user_liked_post,many=True).data
        return Response(serializer)

    def highest_like(self, request):
        highest_like = Upload.objects.annotate(like_count=Count('like_post')).order_by('-like_count').first()

        print("highest_like==>",highest_like)

        if highest_like :
            serializer = UploadSerializer(highest_like)
            print("highest_like====>",highest_like)
            return Response(serializer.data)
        return Response(serializer.errors)

        
        

       








