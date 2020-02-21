from django import forms


#编写form表单类
class UserForm(forms.Form):
    ##required    表示是否为空    默认True表示不可为空

    username = forms.CharField(min_length=6,max_length=32,label="用户名",required=True)
    password = forms.CharField(min_length=6,max_length=32,label="密码")
    email = forms.CharField(max_length=32)

    ##以下写的代码都是固定写法
    def clean_username(self):
        ##校验数据
        ##获取数据
        username = self.cleaned_data.get("username")
        if username == "admin":
            ##校验不通过
            self.add_error("username","用户名不能是admin")
        else:
            ##校验通过
                ##注册
            ##保存数据
            return username

    def clean_password(self):
        password = self.cleaned_data.get("password")
        if password == "12345":
            self.add_error("password","密码太简单")
        else:
            return password
    def clean_email(self):
        pass