from django.http import HttpResponse, HttpResponseForbidden, HttpResponseNotFound
from django.contrib.auth.decorators import login_required
import datetime
import json


def status(request):
    if request.method == 'GET':
        return get_status()
    # elif request.method == 'POST':
    #     set_status()

    pass


@login_required
def update(request):
    if request.method == 'GET':
        HttpResponseNotFound("Nothing implemented for GET and update")
    if request.method == "POST":

        data = json.loads(request.data)

        status = data["status"]

        if status == "closed":
            pass
        elif status == "opened":
            pass

        return HttpResponse("Sucess")
