class TaiKhoan:
    def __init__(self, ten_chu_the, so_du=0):
        self.ten_chu_the = ten_chu_the
        self.__so_du = so_du

    def gui_tien(self, so_tien):
        if so_tien > 0:
            self.__so_du += so_tien
            print("Gửi tiền thành công!")
        else:
            print("Số tiền không hợp lệ!")

    def rut_tien(self, so_tien):
        if so_tien > 0 and so_tien <= self.__so_du:
            self.__so_du -= so_tien
            print("Rút tiền thành công!")
        else:
            print("Rút tiền thất bại!")

    def kiem_tra_so_du(self):
        return self.__so_du

tk1 = TaiKhoan("Nguyen Van A", 1000)
tk1.gui_tien(500)
tk1.rut_tien(300)
print("Số dư hiện tại:", tk1.kiem_tra_so_du())