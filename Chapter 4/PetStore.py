from prettytable import PrettyTable
class ThuCung:
    def __init__(self, ma_thu_cung, ten, loai, gia_tien):
        self.__ma_thu_cung = ma_thu_cung
        self.ten = ten
        self.loai = loai
        self.gia_tien = gia_tien
    def get_ma_thu_cung(self):
        return self.__ma_thu_cung
    def get_ten(self):
        return self.ten
    def get_loai(self):
        return self.loai
    def get_gia_tien(self):
        return self.gia_tien
    def hien_thi(self):
        return [
            self.__ma_thu_cung,
            self.ten,
            self.loai,
            self.gia_tien
        ]
    
class CuaHangService:
    def __init__(self):
        self.kho_hang = []
        self.doanh_thu = 0
    def nhap_thu_cung(self, thu_cung):
        self.kho_hang.append(thu_cung)
        print("Thêm thú cưng thành công!")
    def xem_kho_hang(self):
        if len(self.kho_hang) == 0:
            print("Kho hàng trống!")
            return
        bang = PrettyTable()
        bang.field_names = [
            "Mã",
            "Tên",
            "Loại",
            "Giá tiền"
        ]
        for tc in self.kho_hang:
            bang.add_row(tc.hien_thi())
        print(bang)
    def ban_thu_cung(self, ma_thu_cung):
        for tc in self.kho_hang:
            if tc.get_ma_thu_cung() == ma_thu_cung:
                self.doanh_thu += tc.get_gia_tien()
                self.kho_hang.remove(tc)
                print("Bán thú cưng thành công!")
                return
        print("Không tìm thấy thú cưng!")
    def xem_doanh_thu(self):
        print("Tổng doanh thu:", self.doanh_thu)

class GiaoDienConsole:
    def __init__(self):
        self.service = CuaHangService()
    def chay(self):
        while True:
            print("\n===== PET STORE =====")
            print("1. Nhập thú cưng mới")
            print("2. Hiển thị kho hàng")
            print("3. Bán thú cưng")
            print("4. Xem tổng doanh thu")
            print("5. Thoát")
            lua_chon = input("Nhập lựa chọn: ")
            if lua_chon == "1":
                ma = input("Nhập mã thú cưng: ")
                ten = input("Nhập tên thú cưng: ")
                loai = input("Nhập loại thú cưng: ")
                gia = float(input("Nhập giá tiền: "))
                tc = ThuCung(ma, ten, loai, gia)
                self.service.nhap_thu_cung(tc)
            elif lua_chon == "2":
                self.service.xem_kho_hang()
            elif lua_chon == "3":
                ma = input("Nhập mã thú cưng cần bán: ")
                self.service.ban_thu_cung(ma)
            elif lua_chon == "4":
                self.service.xem_doanh_thu()
            elif lua_chon == "5":
                print("Thoát chương trình!")
                break
            else:
                print("Lựa chọn không hợp lệ!")

app = GiaoDienConsole()
app.chay()