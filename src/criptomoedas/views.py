from rest_framework import viewsets

from .serializers import MoedaModelSerializer


# class UserList(generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = (IsAdminUser,)



class MoedaModelViewSet(viewsets.ModelViewSet):
    serializer_class = MoedaModelSerializer
    # permission_classes = (IsAuthenticated,)

    # def get_queryset(self):
    #     if self.request.user.entity is None:
    #         return Endereco.objects.filter(usuario=self.request.user)
    #     else:
    #         return Endereco.objects.filter(entidade=self.request.user.entity)
    #
    # def perform_create(self, serializer):
    #     serializer.save(usuario=self.request.user,
    #                     entidade=self.request.user.entity)