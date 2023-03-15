from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Task
from api.serializer import TaskSerializer,UserSerializer
from rest_framework.viewsets import ViewSet,ModelViewSet
from rest_framework.decorators import action
from django.contrib.auth.models import User
from rest_framework import authentication,permissions

# class Taskviews(APIView):
#     def get(self,req,*args,**kw):
#         qs=Task.objects.all()
#         sz=TaskSerializer(qs,many=True)
#         return Response(data=sz.data)

#     def post(self,req,*args,**kw):
#         sz=TaskSerializer(data=req.data)
#         if sz.is_valid():
#             sz.save()
                        
#             return Response(data=sz.data)
#         else:
#             return Response(data=sz.errors)
# class TaskViewsDet(APIView):
#     def get(self,req,*args,**kw):
#         id=kw.get("id")
#         qs=Task.objects.get(id=id)
#         sz=TaskSerializer(qs,many=False)
#         return Response(data=sz.data)
#     def put(self,req,*args,**kw):
#         id=kw.get("id")
#         qs=Task.objects.get(id=id)
#         sz=TaskSerializer(data=req.data,instance=qs)
#         if sz.is_valid():
#             sz.save()
#             return Response(data=sz.data)
#         else:
#             return Response(data=sz.errors)
#     def delete(self,req,*args,**kw):
#         id=kw.get("id")
#         qs=Task.objects.filter(id=id).delete()
#         return Response(data="detelete")

# class TaskViewset(ViewSet):
#     def list(self,req,*args,**kw):
#         qs=Task.objects.all()
#         sz=TaskSerializer(qs,many=True)
#         return Response(data=sz.data)
#     def create(self,req,*args,**kw):
#         sz=TaskSerializer(data=req.data)
#         if sz.is_valid():
#             sz.save()
                        
#             return Response(data=sz.data)
#         else:
#             return Response(data=sz.errors)
#     def retrieve(self,req,*args,**kw):
#         id=kw.get("pk")
#         qs=Task.objects.get(id=id)
#         sz=TaskSerializer(qs)
#         return Response(data=sz.data) 
            
#     def update(self,req,*args,**kw):
#         id=kw.get("pk")
#         obj=Task.objects.get(id=id)
#         sz=TaskSerializer(data=req.data,instance=obj)
#         if sz.is_valid():
#             sz.save()
#             return Response(data=sz.data)
#         else:
#             return Response(data=sz.errors)
#     def destroy(self,req,*args,**kw):
#         id=kw.get("pk")
#         qs=Task.objects.filter(id=id).delete()
#         return Response(data="detelete")


class TaskModelViewset(ModelViewSet):
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    serializer_class=TaskSerializer
    queryset=Task.objects.all()
    
    
    
    
    def list(self,request, *args, **kwargs):
        qs=Task.objects.filter(user=request.user)# request .user is used to mention the logged in user
        sz=TaskSerializer(qs,many=True)
        return Response(data=sz.data)
    
    
    
    # def create(self, request, *args, **kwargs):
    #     sz=TaskSerializer(data=request.data)
    #     if sz.is_valid():
    #         sz.save(user=request.user)
    #         return Response(data=sz.data)
    #     else:
    #         return Response(data=sz.errors) 
    
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    


    @action(methods=["GET"],detail=False)
    #localhost:8000/Tasks/v1/finished_task/
    def finished_task(self,req,*args,**kw):
        qs=Task.objects.filter(status=True)
        sz=TaskSerializer(qs,many=True)
        return Response(data=sz.data)
    @action(methods=["GET"],detail=False) 
    #localhost:8000/Taskhttps://www.thunderclient.com/welcomes/v1/pending_task/  
    def pending_task(self,req,*args,**kw):
        qs=Task.objects.filter(status=False)
        sz=TaskSerializer(qs,many=True)
        return Response(data=sz.data)
    #localhost:8000/Tasks/v1/markasdone/
    @action(methods=["PUT"],detail=True)
    def markasdone(self,req,*args,**kw):
        id=kw.get("pk")
        qs=Task.objects.filter(id=id).update(status=True)
        return Response(data="status upated")
 
    
class UserView(ModelViewSet):
    serializer_class= UserSerializer
    queryset=User.objects.all()

    def create(self, request, *args, **kwargs):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            usr=User.objects.create_user(**serializer.validated_data)
            serializer=UserSerializer(usr,many=False)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)










# Create your views here.
