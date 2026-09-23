from rest_framework.views import APIView
from .models import Restaurant
from .serializers import RestaurantSerializer
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404


class ResturantListCreateAPIView(APIView):

    # GET - All restaurants
    def get(self, request):
        resturant = Restaurant.objects.all()
        serializer = RestaurantSerializer(resturant, many=True)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    # POST - Create restaurant
    def post(self, request):
        serializer = RestaurantSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class ResturantDetailAPIView(APIView):

    def get_object(self, pk):
        return get_object_or_404(Restaurant, pk=pk)

    # GET - Single restaurant
    def get(self, request, pk):
        resturant = self.get_object(pk)
        serializer = RestaurantSerializer(resturant)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    # PUT - Update restaurant
    def put(self, request, pk):
        resturant = self.get_object(pk)

        serializer = RestaurantSerializer(
            resturant,
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    # PATCH - Partial update
    def patch(self, request, pk):
        resturant = self.get_object(pk)

        serializer = RestaurantSerializer(
            resturant,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    # DELETE - Delete restaurant
    def delete(self, request, pk):
        resturant = self.get_object(pk)
        resturant.delete()

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )
    




# from rest_framework.generics import GenericAPIView
# from rest_framework.mixins import (
#     ListModelMixin,
#     CreateModelMixin,
#     RetrieveModelMixin,
#     UpdateModelMixin,
#     DestroyModelMixin
# )

# from .models import Resturant
# from .serializers import ResturantSerializers


# # GET all + POST
# class ResturantListCreateAPIView(
#     ListModelMixin,
#     CreateModelMixin,
#     GenericAPIView
# ):
#     queryset = Resturant.objects.all()
#     serializer_class = ResturantSerializers

#     def get(self, request):
#         return self.list(request)

#     def post(self, request):
#         return self.create(request)


# # GET single + PUT + PATCH + DELETE
# class ResturantDetailAPIView(
#     RetrieveModelMixin,
#     UpdateModelMixin,
#     DestroyModelMixin,
#     GenericAPIView
# ):
#     queryset = Resturant.objects.all()
#     serializer_class = ResturantSerializers

#     def get(self, request, pk):
#         return self.retrieve(request, pk)

#     def put(self, request, pk):
#         return self.update(request, pk)

#     def patch(self, request, pk):
#         return self.partial_update(request, pk)

#     def delete(self, request, pk):
#         return self.destroy(request, pk)