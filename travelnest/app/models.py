from django.db import models
# from .models import User
from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.forms import UserCreationForm

# Create your models here.
class User(AbstractUser):
    phone_number = models.CharField(max_length=20,null=True)
    address = models.CharField(max_length=200,null=True)
    avatar = models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.username

# class MyCreateUserForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['username','email','first_name','last_name','password1','password2']

class Tinh(models.Model):
    tentinh = models.CharField(max_length=200,null=True)
    anhtinh = models.ImageField(null=True,blank=True)
    def __str__(self):
        return self.tentinh
class KhachSan(models.Model):
    tenkhachsan = models.CharField(max_length=200,null=True)
    diachi = models.CharField(max_length=200,null=True)
    sdt = models.CharField(max_length=200,null=True)
    mota = models.CharField(max_length=200,null=True)
    email_ks = models.CharField(max_length=200,null=True)
    tinh = models.ForeignKey(Tinh,on_delete=models.SET_NULL,blank=True,null=True)
    anhkhachsan = models.ImageField(null=True,blank=True)
    ngay_them = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    def __str__(self):
        return self.tenkhachsan
    @property
    def diem_trung_binh(self):
        danhgia_list = Danhgia.objects.filter(phong__khachsan=self)
        # Tính tổng điểm từ tất cả các đánh giá
        tong_diem = sum([danhgia.diem for danhgia in danhgia_list])
        # Đếm số lượng đánh giá
        so_luong_danh_gia = danhgia_list.count()
        # Tính điểm trung bình hoặc đặt điểm mặc định là 10 nếu chưa có đánh giá
        diem_trung_binh = (tong_diem / so_luong_danh_gia) if so_luong_danh_gia > 0 else 10
        diem_tb= int(diem_trung_binh)
        return diem_tb
    @property
    def get_danh_gia_tb(self):
        if self.diem_trung_binh == 10:
            return "Tuyệt vời"
        elif self.diem_trung_binh == 8:
            return "Tốt"
        elif self.diem_trung_binh == 7:
            return "Tạm ổn"
        elif self.diem_trung_binh == 5:
            return "Không tốt"
    @property
    def sum_danh_gia(self):
         danhgia_list = Danhgia.objects.filter(phong__khachsan=self)
         so_luong_danh_gia = danhgia_list.count()
         return so_luong_danh_gia
class LoaiPhong(models.Model):
    tenloaiphong = models.CharField(max_length=200,null=True)
    mota_loaiphong = models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.tenloaiphong
class Phong(models.Model):
    loaiphong = models.ForeignKey(LoaiPhong,on_delete=models.SET_NULL,blank=True,null=True)
    loaigiuong = models.CharField(max_length=200,null=True)
    mota = models.CharField(max_length=200,null=True)
    dientich = models.CharField(max_length=200,null=True)
    phongtam = models.CharField(max_length=200,null=True)
    soluongnguoi = models.IntegerField()
    giaphong = models.FloatField()
    trangthaiphong = models.CharField(max_length=200,null=True)
    khachsan = models.ForeignKey(KhachSan,on_delete=models.SET_NULL,blank=True,null=True)
    def is_phong_trong_hien_tai(self, ngaynhan, ngaytra):
        ngay_da_dat =True
        cac_dat_phong = ChiTietHoaDon.objects.filter(phong=self)
        # Kiểm tra xem ngày hiện tại có nằm trong bất kỳ khoảng đặt phòng nào không
        for dat_phong in cac_dat_phong:
            ngay_nhan = dat_phong.ngay_gio_nhan.date()
            ngay_tra = dat_phong.ngay_gio_tra.date()
            if  not (ngay_nhan > ngaytra or ngay_tra < ngaynhan):
                ngay_da_dat = False  # Phòng trống
        return ngay_da_dat

class Anh(models.Model):
    anhphong = models.ImageField(null=True,blank=True)
    phong = models.ForeignKey(Phong,on_delete=models.SET_NULL,blank=True,null=True )
class Danhgia(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,blank=True,null=True)
    phong = models.ForeignKey(Phong,on_delete=models.SET_NULL,blank=True,null=True)
    diem = models.IntegerField()
    binhluan = models.CharField(max_length=200,null=True)
    ngay_danhgia = models.DateTimeField(auto_now_add=True)
    @property
    def get_danh_gia(self):
        if self.diem == 10:
            return "Tuyệt vời"
        elif self.diem == 8:
            return "Tốt"
        elif self.diem == 7:
            return "Tạm ổn"
        elif self.diem == 5:
            return "Không tốt"
        else:
            return "Chưa được đánh giá được đánh giá"
class TienNghi(models.Model):
    icon = models.ImageField(null=True,blank=True)
    tentiennghi = models.CharField(max_length=200,null=True)
    mota_tiennghi = models.TextField(blank=True,null=True)
    def __str__(self):
        return self.tentiennghi
class SapXepTN(models.Model):
    phong = models.ForeignKey(Phong,on_delete=models.SET_NULL,blank=True,null=True)
    tiennghi = models.ForeignKey(TienNghi,on_delete=models.SET_NULL,blank=True,null=True)
    ngaytrangbi = models.DateTimeField(auto_now_add=True)
class HoaDon(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,blank=True,null=True)
    trangthaihoanthanh = models.CharField(max_length=200,null=True)
    ngay_gio_dat = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.id)
class ChiTietHoaDon(models.Model):
    phong = models.ForeignKey(Phong,on_delete=models.SET_NULL,blank=True,null=True)
    hoadon = models.ForeignKey(HoaDon,on_delete=models.SET_NULL,blank=True,null=True)
    ngay_gio_nhan = models.DateTimeField()
    ngay_gio_tra = models.DateTimeField()
    soluong = models.IntegerField()
    dongia = models.FloatField()
    @property
    def total_dem(self):
        so_dem = (self.ngay_gio_tra - self.ngay_gio_nhan).days
        return so_dem
    @property
    def total_tien(self):
        tongtien = self.total_dem * self.dongia
        return tongtien
    
