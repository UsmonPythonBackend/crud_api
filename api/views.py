from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Artist, Albom, Song
from .serializers import ArtistSerializer, ArtistSerializerMobile, AlbomSerializer, SongSerializer


class ArtistAPIView(APIView):
    def get(self, request):
        queryset = Artist.objects.all()
        serializer = ArtistSerializer(queryset, many=True)
        return Response(data=serializer.data)


class ArtistAPIViewMobile(APIView):
    def get(self, request):
        queryset = Artist.objects.all()
        serializer = ArtistSerializerMobile(queryset, many=True)
        return Response(data=serializer.data)

    def post(self, request):
        serializer = ArtistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        context_error = {
            "status": 400,
            "data": serializer.data,
            "message": "Xatolik ro'y berdi"
        }
        return Response(data=context_error, status=status.HTTP_400_BAD_REQUEST)

class ArtistDetailAPIView(APIView):
    def get(self, request, id):
        try:
            artist = Artist.objects.get(id=id)
        except:
            context_error = {
                "status": 404,
                "message": "Artist not found"
            }
            return Response(data=context_error, status=status.HTTP_404_NOT_FOUND)
        print(f"-------------------{artist}")
        if artist:
            serializer = SongSerializer(artist)
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        context_error = {
            "status": 404,
            "message": "Artist not found"
        }
        return Response(data=context_error, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id):
        artist = Artist.objects.get(id=id)
        serializer = ArtistSerializer(instance=artist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):

        artist = Artist.objects.get(id=id)
        serializer = SongSerializer(instance=artist, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        artist = Artist.objects.get(id=id)
        artist.delete()
        context = {"status": 200, "message": "Artist deleted"}
        return Response(data=context, status=status.HTTP_204_NO_CONTENT)




class AlbomAPIView(APIView):
    def get(self, request):
        alboms = Albom.objects.all()
        albom_serializer = AlbomSerializer(alboms, many=True)
        return Response(data=albom_serializer.data)

    def post(self, request):
        serializer = AlbomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        context_error = {
                "status": 400,
                "data": serializer.data,
                "message": "Xatolik ro'y berdi"
        }
        return Response(data=context_error, status=status.HTTP_400_BAD_REQUEST)

class AlbomDetailAPIView(APIView):
    def get(self, request, id):
        try:
            albom = Albom.objects.get(id=id)
        except:
            context_error = {
                "status": 404,
                "message": "Albom not found"
            }
            return Response(data=context_error, status=status.HTTP_404_NOT_FOUND)
        print(f"-------------------{albom}")
        if albom:
            serializer = SongSerializer(albom)
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        context_error = {
            "status": 404,
            "message": "Albom not found"
        }
        return Response(data=context_error, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id):
        albom = Albom.objects.get(id=id)
        serializer = AlbomSerializer(instance=albom, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):

        albom = Albom.objects.get(id=id)
        serializer = SongSerializer(instance=albom, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        albom = Song.objects.get(id=id)
        albom.delete()
        context = {"status": 200, "message": "Albom deleted"}
        return Response(data=context, status=status.HTTP_204_NO_CONTENT)



class SongAPIView(APIView):
    def get(self, request):
        songs = Song.objects.all()
        serializer = SongSerializer(songs, many=True)
        return Response(data=serializer.data)

    def post(self, request):
        serializer = SongSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        context_error = {
            "status": 400,
            "data": serializer.data,
            "message": "Xatolik ro'y berdi"
        }
        return Response(data=context_error, status=status.HTTP_400_BAD_REQUEST)


class SongDetailAPIView(APIView):
    def get(self, request, id):
        try:
            song = Song.objects.get(id=id)
        except:
            context_error = {
                "status": 404,
                "message": "Song not found"
            }
            return Response(data=context_error, status=status.HTTP_404_NOT_FOUND)
        print(f"-------------------{song}")
        if song:
            serializer = SongSerializer(song)
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        context_error = {
            "status": 404,
            "message": "Song not found"
        }
        return Response(data=context_error, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id):
        song = Song.objects.get(id=id)
        serializer = SongSerializer(instance=song, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):

        song = Song.objects.get(id=id)
        serializer = SongSerializer(instance=song, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        song = Song.objects.get(id=id)
        song.delete()
        context = {"status": 200, "message": "Song deleted"}
        return Response(data=context, status=status.HTTP_204_NO_CONTENT)










