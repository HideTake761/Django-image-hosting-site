from django.shortcuts import render, get_object_or_404
from .forms import UploadForm
from .models import UploadImage
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

@login_required
def list(request, num=1):
    data = UploadImage.objects.all()
    page = Paginator(data, 3)
    params = {
        'data': page.get_page(num),
    }
    return render(request, 'timeline/list.html', params)

@login_required
def create(request):
    params = {
        'upload_form': UploadForm(),
        'id': None,
    }

    if (request.method == 'POST'):
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            upload_data = form.save()

            params['id'] = upload_data.id

    return render(request, 'timeline/create.html', params)

@login_required
def preview(request, data_id=0):

    upload_data = get_object_or_404(UploadImage, id=data_id)

    if (request.method == 'POST'):
        delete(data_id)

        params = {
            'title': 'Photo is deleted.',
            'id': data_id,
            'url': None,
        }

        return render(request, 'timeline/delete.html', params)

    else:
        params = {
            'title': 'Will you delete this photo?',
            'id': upload_data.id,
            'image': upload_data.image.url,
            'comment': upload_data.comment,
        }

        return render(request, 'timeline/delete.html', params)

def delete(data_id=0):

    # get UploadImage instance
    upload_data = get_object_or_404(UploadImage, id=data_id)
    
    # delete photo
    upload_data.image.delete()
    
    # delete record
    upload_data.delete()
