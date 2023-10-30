import io

from PIL import Image
from django.test import TestCase, Client
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
# SimpleUploadedFile:アップロードしたいリアルなサンプルファイルを含むインスタンスを作ることができるオブジェクト

class UploadFormTest(TestCase):
    def _get_form_class(self):
        from .forms import UploadForm
        return UploadForm

    def create_test_image(self):
        # BytesIO:メモリ上でバイナリデータを扱うための機能
        file_obj = io.BytesIO() # バイト列のストリーム
        im = Image.new('RGB', size=(100, 100)) # Image.new():画像データ(PIL.Image)を新規に作成
        # RGB:3x8bitカラー画像
        im.save(file_obj, 'jpeg') # file_objにjpeg形式で保存
        file_obj.name = 'test.jpg'
        file_obj.seek(0) # seek(0)でストリームの先頭に
        return file_obj

    def test_create(self):
        # testing image & comment posting form
        img = self.create_test_image()
        Form = self._get_form_class()
        form = Form(
            data={'comment': 'This is the file for a test.'},
            files={'image': SimpleUploadedFile(
                img.name,
                img.read(),
                content_type='image/jpg')
            },
        )
        self.assertTrue(form.is_valid()) # assertTrue(x):bool(x) is True

    def test_list(self):
        # testing whether users are redirected (to login page) if they're not authenticated
        response = self.client.get(reverse('list'))
        # client.get()でアクセス。reverse()で'listのurlを生成->getの引数に。
        self.assertEqual(response.status_code, 302) # assertEqual(a, b):a == b
    
    def test_invalid_login(self):
        # testing whether login with invalid username & password fails
        client = Client()
        client.login(username='testuser', password='password')
        response = client.get('list')
        self.assertEqual(response.status_code, 404)
