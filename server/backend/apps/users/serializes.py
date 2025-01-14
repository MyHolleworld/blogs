import hashlib
import os
from django.db.models import Q
from django.conf import settings
from apps.users.models import User
from utils.FaceTool import FaceTool


class UserSerializer:
    @staticmethod
    def login_validate(attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        imgBase64 = attrs.get('imgBase64', [])
        if not username:
            return "所有字段都是必填项"
        if password:
            # 使用MD5加密密码
            md5 = hashlib.md5()
            md5.update(password.encode('utf-8'))
            password = md5.hexdigest()

        user = User.objects.filter(Q(username=username) | Q(email=username) | Q(mobile=username)).first()
        if user and user.password == password:
            return {'user': user}
        elif imgBase64 and user:
            original_file_path = os.path.join(settings.BASE_DIR, user.face)
            if os.path.exists(original_file_path):
                verify_scores = FaceTool.verifyFace(imgBase64[0].split(',', 1)[1], original_file_path)
                print(verify_scores)
                if verify_scores:
                    return {'user': user}  # 直接通过验证
                else:
                    return "人脸识别不通过"
        else:
            return "密码错误或未找到该用户"

    @staticmethod
    def register_validate(attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        password_confirm = attrs.get('password_confirm')
        email = attrs.get('email')
        mobile = attrs.get('mobile')
        try:
            if not username or not password or not password_confirm or not email or not mobile:
                return "所有字段都是必填项"
            if len(username) > 20 or len(password) > 128 or len(str(mobile)) != 11:
                return "字段长度不满足要求"
            if password_confirm != password:
                return "两次密码输入不一致"
            if User.objects.filter(Q(username=username) | Q(email=email) | Q(mobile=mobile)).exists():
                return "用户已经存在"
        except Exception as e:
            return e
        # 使用MD5加密密码
        md5 = hashlib.md5()
        md5.update(password.encode('utf-8'))
        hashed_password = md5.hexdigest()
        return {
            'username': username,
            'password': hashed_password,
            'email': email,
            'mobile': mobile
        }

    @staticmethod
    def update_validate(personal_data,data):
        # 更新个人资料字段
        personal_data.school = data.get('school', personal_data.school)
        personal_data.address = data.get('address', personal_data.address)
        personal_data.city = data.get('city', personal_data.city)
        personal_data.state = data.get('state', personal_data.state)
        personal_data.zip = data.get('zip', personal_data.zip)
        personal_data.age = data.get('age', personal_data.age)
        personal_data.hobbies = data.get('hobbies', personal_data.hobbies)
        personal_data.linkedin = data.get('linkedin', personal_data.linkedin)
        personal_data.github = data.get('github', personal_data.github)
        personal_data.degree = data.get('degree', personal_data.degree)
        personal_data.major = data.get('major', personal_data.major)
        personal_data.graduation_year = data.get('graduation_year', personal_data.graduation_year)
        personal_data.company_name = data.get('company_name', personal_data.company_name)
        personal_data.job_title = data.get('job_title', personal_data.job_title)
        personal_data.job_description = data.get('job_description', personal_data.job_description)
        personal_data.skills = data.get('skills', personal_data.skills)
        personal_data.certificates = data.get('certificates', personal_data.certificates)
        personal_data.languages = data.get('languages', personal_data.languages)