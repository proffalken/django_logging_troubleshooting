import logging

logger = logging.getLogger(__name__)

from django.http import HttpResponse
from django.shortcuts import render
from .models import Room

# Create your views here.
def list_rooms(request):
    rooms = Room.objects.all()
    logger.info(f"Returned {len(rooms)} rooms")
    return HttpResponse(rooms)
