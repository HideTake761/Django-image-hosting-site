from django.shortcuts import render, redirect
from .forms import SignupForm, LoginForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

def signup_view(request):
    if request.method == 'POST':

        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(to='/timeline/')

    else:
        form = SignupForm()
    
    param = {
        'form': form
    }

    return render(request, 'accounts/signup.html', param)

def login_view(request):
    if request.method == 'POST':
        next = request.POST.get('next') # クエリストリングとしてnextを定義
        # このnextは、元々ユーザーがアクセスしようとしていたページのパス
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()

            if user:
                login(request, user)
                if next == 'None':
                    return redirect(to='/accounts/user/')
                else:
                    return redirect(to=next)

    else: # GETメソッド(POSTメソッド以外)でリクエストされた際はTemplateを描画してログインのページの表示を行う
        form = LoginForm()
        next = request.GET.get('next')
    
    param = {
        'form': form,
        'next': next
    }

    return render(request, 'accounts/login.html', param)
    # render(HttpRequest, 使用するtempletes, )指定したテンプレートを読み込み、
    # レンダリングして(テンプレートに記述されている変数などを実際に使う値に置き換えて表示を完成させて)返す

def logout_view(request):
    logout(request)

    return render(request, 'accounts/logout.html')

@login_required
def user_view(request):
    user = request.user

    params = {
        'user': user
    }

    return render(request, 'accounts/user.html', params)
