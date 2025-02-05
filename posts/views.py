import json
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse 
from django.views.decorators.http import require_http_methods
from .models import Post, Comment

from .serializers import PostSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

from rest_framework.permissions import IsAuthenticatedOrReadOnly

# Create your views here.

def hello_world(request):
    if request.method == "GET":
        return JsonResponse({
            'status' : 200,
            'success' : True,
            'message' : '메시지 전달 성공!',
            'data': "Hello world"
        })

@require_http_methods(["POST"])
def create_post(request):
    body = json.loads(request.body.decode('utf-8'))
		
		# ORM을 통해 새로운 데이터를 DB에 생성함
    new_post = Post.objects.create(
        writer = body['writer'],
        content = body['content'],
        category = body['category']
    )
		
		# Response에서 보일 데이터 내용을 Json 형태로 예쁘게 만들어줌
    new_post_json = {
        "id": new_post.post_id,
        "writer": new_post.writer,
        "content": new_post.content,
        "category": new_post.category
    }

    return JsonResponse({
        'status': 200,
        'message': '게시글 목록 조회 성공',
        'data': new_post_json
    })

@require_http_methods(["GET"])
def get_post_all(request):
@require_http_methods(["GET"])
def get_post_all(request):

		# Post 데이터베이스에 있는 모든 데이터를 불러와 queryset 형식으로 저장함
    post_all = Post.objects.all()
		# Post 데이터베이스에 있는 모든 데이터를 불러와 queryset 형식으로 저장함
    post_all = Post.objects.all()
    
		# 각 데이터를 Json 형식으로 변환하여 리스트에 저장함
    post_json_all = []
    for post in post_all:
        post_json = {
            "id": post.id,
            "writer": post.writer,
            "category": post.category
        }
        post_json_all.append(post_json)
		# 각 데이터를 Json 형식으로 변환하여 리스트에 저장함
    post_json_all = []
    for post in post_all:
        post_json = {
            "id": post.id,
            "writer": post.writer,
            "category": post.category
        }
        post_json_all.append(post_json)
    
    return JsonResponse({
        'status': 200,
        'message': '게시글 목록 조회 성공',
        'data': post_json_all
    })
    return JsonResponse({
        'status': 200,
        'message': '게시글 목록 조회 성공',
        'data': post_json_all
    })


@require_http_methods(["GET", "PATCH", "DELETE"])
def post_detail(request, id):
		# 요청 메소드가 GET일 때는 게시글을 조회하는 View가 동작하도록 함
    if request.method == "GET":
        post = get_object_or_404(Post, pk=id)
@require_http_methods(["GET", "PATCH", "DELETE"])
def post_detail(request, id):
		# 요청 메소드가 GET일 때는 게시글을 조회하는 View가 동작하도록 함
    if request.method == "GET":
        post = get_object_or_404(Post, pk=id)
        
        post_json = {
            "id": post.id,
            "writer": post.writer,
            "content": post.content,
            "category": post.category,
        }
        post_json = {
            "id": post.id,
            "writer": post.writer,
            "content": post.content,
            "category": post.category,
        }

        return JsonResponse({
            'status': 200,
            'message': '게시글 조회 성공',
            'data': post_json
        })
        return JsonResponse({
            'status': 200,
            'message': '게시글 조회 성공',
            'data': post_json
        })
		
		# 요청 메소드가 GET일 때는 게시글을 조회하는 View가 동작하도록 함
    elif request.method == "PATCH":
        body = json.loads(request.body.decode('utf-8'))
        update_post = get_object_or_404(Post, pk=id)
		# 요청 메소드가 GET일 때는 게시글을 조회하는 View가 동작하도록 함
    elif request.method == "PATCH":
        body = json.loads(request.body.decode('utf-8'))
        update_post = get_object_or_404(Post, pk=id)

        update_post.content = body['content']
        update_post.save()
        update_post.content = body['content']
        update_post.save()

        update_post_json = {
            "id": update_post.id,
            "writer": update_post.writer,
            "content": update_post.content,
            "category": update_post.category,
        }
        update_post_json = {
            "id": update_post.id,
            "writer": update_post.writer,
            "content": update_post.content,
            "category": update_post.category,
        }

        return JsonResponse({
            'status': 200,
            'message': '게시글 수정 성공',
            'data': update_post_json
        })
        return JsonResponse({
            'status': 200,
            'message': '게시글 수정 성공',
            'data': update_post_json
        })

    elif request.method == "DELETE":
        delete_post = get_object_or_404(Post, pk=id)
        delete_post.delete()
    elif request.method == "DELETE":
        delete_post = get_object_or_404(Post, pk=id)
        delete_post.delete()

        return JsonResponse({
                'status': 200,
                'message': '게시글 삭제 성공',
                'data': None
        })
        return JsonResponse({
                'status': 200,
                'message': '게시글 삭제 성공',
                'data': None
        })


@require_http_methods(["GET"])
def get_comment(request, post_id):
    comments = Comment.objects.filter(post=post_id)

    comment_json_list = []
    for comment in comments:
        commet_json = {
            'writer':comment.writer,
            'content':comment.content
        }
        comment_json_list.append(commet_json)
    
    return JsonResponse({
        'status':200,
        'message':'댓글 읽어오기 성공',
        'data':comment_json_list
    })


@require_http_methods(["GET"])
def get_post_all(request):
		# Post 데이터베이스에 있는 모든 데이터를 불러와 queryset 형식으로 저장함
    post_all = Post.objects.all()
    
		# 각 데이터를 Json 형식으로 변환하여 리스트에 저장함
    post_json_all = []
    for post in post_all:
        post_json = {
            "id": post.post_id,
            "writer": post.writer,
            "category": post.category
        }
        post_json_all.append(post_json)
    
    return JsonResponse({
        'status': 200,
        'message': '게시글 목록 조회 성공',
        'data': post_json_all
    })

require_http_methods(["GET"])
def get_comment(request, post_id):
    comments = Comment.objects.filter(post= post_id)

    comment_json_list = []
    for comment in comments:
        comment_json = {
            'writer' : comment.writer,
            'content' : comment.content
        }
        comment_json_list.append(comment_json)

    return JsonResponse({
        'status' : 200,
        'message' : '댓글 읽어오기 성공',
        'data' : comment_json_list
    })

##APIView
class PostList(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def post(self, request, format=None):
        serializer = PostSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   

    def get(self, request, format = None):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many = True)
        return Response(serializer.data)

class PostDetail(APIView):
    def get(self, request,id):
        post = get_object_or_404(Post, post_id=id)
        serializer = PostSerializer(post)
        return Response(serializer.data)
    
    def put(self, request,id):
        post = get_object_or_404(Post, post_id=id) # 이녀석은 어떤 모델에서 어떤 칼럼값을 기준으로 가져올지 넘겨주는 함수
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        post = get_object_or_404(Post, post_id=id)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

from rest_framework import mixins
from rest_framework import generics
from rest_framework import mixins
from rest_framework import generics

class PostListMixins(mixins.ListModelMixin,mixins.CreateModelMixin, generics.GenericAPIView):
class PostListMixins(mixins.ListModelMixin,mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


    def get(self, request, *args, **kwargs):
        return self.list(request)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class PostDetailMixins(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
        
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
        return self.destroy(request, *args, **kwargs)
    

##Generics APIView
class PostListGenericAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetailGenericAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


#############viewset

#############viewset
from rest_framework import viewsets

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# post_list = PostViewSet.as_view({
#     'get':'list',
#     'post':'create'
#     'get':'list',
#     'post':'create'
# })

# post_detail_vs = PostViewSet.as_view({
#     'get':'retrieve',
#     'put':'update',
#     'patch':'partial_update',
#     'delete':'destroy'
# post_detail_vs = PostViewSet.as_view({
#     'get':'retrieve',
#     'put':'update',
#     'patch':'partial_update',
#     'delete':'destroy'
# })