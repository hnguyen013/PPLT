from prettytable import PrettyTable


class NhanVien:
    def __init__(self, ma_nv, ten):
        self.ma_nv = ma_nv
        self.ten = ten
    def tinh_luong(self):
        pass

class NhanVienFullTime(NhanVien):
    def __init__(self, ma_nv, ten, luong_co_ban):
        super().__init__(ma_nv, ten)
        self.luong_co_ban = luong_co_ban
    def tinh_luong(self):
        return self.luong_co_ban

class NhanVienPartTime(NhanVien):
    def __init__(self, ma_nv, ten, so_gio_lam, luong_theo_gio):
        super().__init__(ma_nv, ten)
        self.so_gio_lam = so_gio_lam
        self.luong_theo_gio = luong_theo_gio
    def tinh_luong(self):
        return self.so_gio_lam * self.luong_theo_gio

def hien_thi_nhan_vien(danh_sach_nv):

    bang = PrettyTable()
    bang.field_names = ["Mã NV", "Tên", "Loại", "Lương"]
    for nv in danh_sach_nv:
        if isinstance(nv, NhanVienFullTime):
            loai = "Full-time"
        else:
            loai = "Part-time"
        bang.add_row([
            nv.ma_nv,
            nv.ten,
            loai,
            nv.tinh_luong()
        ])
    print(bang)
    
danh_sach_nv = [
    NhanVienFullTime("FT01", "Nguyen Van", 15000000),
    NhanVienPartTime("PT01", "Tran Thi", 80, 50000),
    NhanVienFullTime("FT02", "Le Van", 12000000),
    NhanVienPartTime("PT02", "Pham Thi", 60, 40000)
]
hien_thi_nhan_vien(danh_sach_nv)