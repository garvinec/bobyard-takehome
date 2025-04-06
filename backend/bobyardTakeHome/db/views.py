from rest_framework import viewsets
from db.models import Comment
from .serializers import CommentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


@api_view(['GET'])
def get_comments(request):
    comments = Comment.objects.all()
    serializer = CommentSerializer(comments, many=True)
    children_dict = {}
    # ideal format
    # {id, author, text, ..., children: Comment[]}
    for comment in serializer.data:
        if comment["parent"]:
            if comment["parent"] in children_dict:
                children_dict[comment["parent"]].append(comment)
            else:
                children_dict[comment["parent"]] = [comment]

    def populate_children(parent_comment):
        # returns [{comment1}, {comment2}, ...]
        children_list = []
        del parent_comment['parent']
        if parent_comment['id'] in children_dict:
            for child in children_dict[parent_comment['id']]:
                if child['id'] in children_dict:
                    child['children'] = populate_children(child)
                    children_list.append(child)
                else:
                    del child['parent']
                    child['children'] = []
                    children_list.append(child)

        return children_list

    comment_list = []
    for c in serializer.data:
        if 'parent' in c:
            if not c['parent']:
                c['children'] = populate_children(c)
                comment_list.append(c)

    return Response(comment_list, status=status.HTTP_200_OK)


@api_view(['POST'])
def create_comment(request):
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def update_comment(request, pk):
    try:
        comment = Comment.objects.get(pk=pk)

        if 'text' in request.data:
            comment.text = request.data['text']
            comment.save()

        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    except Comment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_comment(request, pk):
    comment = Comment.objects.get(pk=pk)
    comment.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
