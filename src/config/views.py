from django.shortcuts import redirect
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny


@api_view(['GET'])
@permission_classes([AllowAny])
def root_view(request):
    if request.user.is_authenticated:
        return redirect('/api/')
    else:
        return redirect('api/token')
