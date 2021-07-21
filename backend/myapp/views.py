
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer


@api_view(['GET', 'POST'])
def meme_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        meme =User.objects.all().order_by('-id')[:100]
        serializer = UserSerializer(meme,many =True )
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"id": serializer.data["id"]}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def meme_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        meme = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(meme)
        return Response(serializer.data)
