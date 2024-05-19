from django.contrib.auth.models import Group, Permission
from django.core.management import BaseCommand

class Command(BaseCommand):
    help = 'Assign "staff" permission to a group'

    def handle(self, *args, **options):
        # Tạo hoặc lấy một nhóm
        group, created = Group.objects.get_or_create(name='khachhang')
        # Lấy quyền "staff" (thay thế 'staff_codename' bằng codename bạn tìm thấy)
        permission = Permission.objects.get(codename='Staff status')
        # Gán quyền cho nhóm
        group.permissions.add(permission)
        self.stdout.write(self.style.SUCCESS('Successfully assigned "staff" permission to "My Group"'))
