from django.contrib.auth.models import User

from blog.models import Profile


def create_user_profile(username, password, first_name, last_name, email, phone, address, github, group):
    if User.objects.filter(username=username).exists():
        User.objects.get(username=username).delete()
    if User.objects.create_user(username=username, email=email,
                                first_name=first_name,
                                last_name=last_name):
        user = User.objects.get(username=username)
        user.set_password(password)
        user.save()
        Profile.objects.create(user=user,
                               phone=phone,
                               address=address,
                               github=github)
        user.groups.add(group)
