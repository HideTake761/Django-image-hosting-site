import io

from PIL import Image
from django.test import TestCase, Client
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse

class UploadFormTest(TestCase):
    def _get_form_class(self):
        from .forms import UploadForm
        return UploadForm

    def create_test_image(self):
        file_obj = io.BytesIO()
        im = Image.new('RGB', size=(10, 10))
        im.save(file_obj, 'jpeg')
        file_obj.name = 'test.jpg'
        file_obj.seek(0)
        return file_obj

    def test_create(self):
        #testing image & comment posting form
        img = self.create_test_image()
        Form = self._get_form_class()
        form = Form(
            data={'comment': 'This is the file for a test.'},
            files={'image': SimpleUploadedFile(
                img.name,
                img.read(),
                content_type='image/jpg',
            )},
        )
        self.assertTrue(form.is_valid())

    def test_list(self):
        #testing whether users are redirected (to login page) if they're not authenticated
        response = self.client.get(reverse('list'))
        self.assertEqual(response.status_code, 302)
    
    def test_invalid_login(self):
        #testing whether login with invalid username & password fails
        client = Client()
        client.login(username='testuser', password='password')
        response = client.get('list')
        self.assertEqual(response.status_code, 404)
