from django.contrib import admin
from .models import *

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display=('username','first_name','last_name','email','is_staff', 'date_joined','phone_number','address','custom_method')
    def custom_method(self, obj):
        return ', '.join([str(group) for group in obj.groups.all()])
    custom_method.short_description = 'Groups'
admin.site.register(User, UserAdmin)

class TinhAdmin(admin.ModelAdmin):
    list_display=('tentinh','anhtinh')
admin.site.register(Tinh,TinhAdmin)

class KhachSanAdmin(admin.ModelAdmin):
    list_display=('tenkhachsan','diachi','sdt','mota','email_ks','tinh','anhkhachsan')
admin.site.register(KhachSan,KhachSanAdmin)

class LoaiPhongAdmin(admin.ModelAdmin):
    list_display=('tenloaiphong','mota_loaiphong')
admin.site.register(LoaiPhong,LoaiPhongAdmin)
class PhongAdmin(admin.ModelAdmin):
    list_display=('loaiphong','loaigiuong','mota','dientich','phongtam','soluongnguoi','giaphong','trangthaiphong','khachsan')
admin.site.register(Phong,PhongAdmin)

class AnhAdmin(admin.ModelAdmin):
    list_display=('phong','anhphong')
admin.site.register(Anh,AnhAdmin)

class DanhGiaAdmin(admin.ModelAdmin):
    list_display=('user','phong','diem','binhluan','ngay_danhgia')
admin.site.register(Danhgia,DanhGiaAdmin)

class TienNghiAdmin(admin.ModelAdmin):
    list_display=('tentiennghi','mota_tiennghi','icon')
admin.site.register(TienNghi,TienNghiAdmin)

class SapXepTNAdmin(admin.ModelAdmin):
    list_display=('phong','tiennghi','ngaytrangbi')
admin.site.register(SapXepTN,SapXepTNAdmin)

class HoaDonAdmin(admin.ModelAdmin):
    list_display=('user','trangthaihoanthanh','ngay_gio_dat')
admin.site.register(HoaDon,HoaDonAdmin)

class ChiTietHoaDonAdmin(admin.ModelAdmin):
    list_display=('phong','hoadon','ngay_gio_nhan','ngay_gio_tra','soluong','dongia')
admin.site.register(ChiTietHoaDon,ChiTietHoaDonAdmin)
