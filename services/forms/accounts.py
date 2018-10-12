from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from infrastructure.models import CustomUser as User


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=20,
                               required=True,
                               error_messages={
                                   'required': 'そのユーザ名は既に使用されています'
                               },
                               widget=forms.TextInput(attrs={
                                   'class': 'input-text',
                                   'placeholder': 'ユーザー名'
                               }))
    email = forms.EmailField(required=True,
                             error_messages={
                                 'required': 'そのメールアドレスは既に使用されています'
                             },
                             widget=forms.TextInput(attrs={
                                 'class': 'input-text',
                                 'placeholder': 'メールアドレス'
                             }))
    password1 = forms.CharField(required=True,
                                max_length=255,
                                widget=forms.PasswordInput(attrs={
                                    'class': 'input-text',
                                    'placeholder': 'パスワード'
                                }))
    password2 = forms.CharField(required=True,
                                max_length=255,
                                widget=forms.PasswordInput(attrs={
                                    'class': 'input-text',
                                    'placeholder': '確認用パスワード'
                                }))

    class Meta:
        model = User
        fields = (
            "username", "email", "password1", "password2",
        )


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=50,
                               label='メールアドレス',
                               required=True,
                               error_messages={
                                   'required': '正しいメールアドレスを入力してください'
                               })
    password = forms.PasswordInput()


class EmailChangeForm(forms.Form):
    error_messages = {
        'email_mismatch': "パスワードが一致していません",
        'email_inuse': "指定のメールアドレスは既に別のアカウントで使用されています",
        'password_incorrect': "パスワードが正しくありません",
    }

    current_password = forms.CharField(
        widget=forms.PasswordInput,
        required=True
    )

    new_email1 = forms.EmailField(
        max_length=254,
        required=True
    )

    new_email2 = forms.EmailField(
        max_length=254,
        required=True
    )

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(EmailChangeForm, self).__init__(*args, **kwargs)

    def clean_current_password(self):
        """
        Validates that the password field is correct.
        """
        current_password = self.cleaned_data["current_password"]
        if not self.user.check_password(current_password):
            raise forms.ValidationError(self.error_messages['password_incorrect'], code='password_incorrect', )
        return current_password

    def clean_new_email1(self):
        """
        Prevents an e-mail address that is already registered from being registered by a different user.
        """
        email1 = self.cleaned_data.get('new_email1')
        if User.objects.filter(email=email1).count() > 0:
            raise forms.ValidationError(self.error_messages['email_inuse'], code='email_inuse', )
        return email1

    def clean_new_email2(self):
        """
        Validates that the confirm e-mail address's match.
        """
        email1 = self.cleaned_data.get('new_email1')
        email2 = self.cleaned_data.get('new_email2')
        if email1 and email2:
            if email1 != email2:
                raise forms.ValidationError(self.error_messages['email_mismatch'], code='email_mismatch', )
        return email2

    def save(self, commit=True):
        self.user.email = self.cleaned_data['new_email1']
        if commit:
            self.user.save()
        return self.user


class EditProfilePassword(PasswordChangeForm):
    error_css_class = 'has-error'
    error_messages = {'password_incorrect': "入力されたパスワードは間違っています"}
    old_password = forms.CharField(required=True, label='現在のパスワード',
                                   widget=forms.PasswordInput(attrs={
                                       'class': 'form-control'}),
                                   error_messages={
                                       'required': '現在のパスワードを入力してください'})

    new_password1 = forms.CharField(required=True, label='新しいパスワード',
                                    widget=forms.PasswordInput(attrs={
                                        'class': 'form-control'}),
                                    error_messages={
                                        'required': '新しいパスワードを入力してください'})
    new_password2 = forms.CharField(required=True, label='新しいパスワード(確認用)',
                                    widget=forms.PasswordInput(attrs={
                                        'class': 'form-control'}),
                                    error_messages={
                                        'required': '新しいパスワードを入力してください'})
