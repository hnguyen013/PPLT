from prettytable import PrettyTable

class Sach:
    def __init__(self, ma_sach, ten_sach, tac_gia):
        self.ma_sach = ma_sach
        self.ten_sach = ten_sach
        self.tac_gia = tac_gia
        self.trang_thai = "Sẵn sàng"

    def hien_thi(self):
        return [
            self.ma_sach,
            self.ten_sach,
            self.tac_gia,
            self.trang_thai
        ]

class QuanLyThuVien:
    def __init__(self):
        self.danh_sach_sach = []
    def them_sach(self, sach_moi):
        self.danh_sach_sach.append(sach_moi)
        print("Thêm sách thành công!")
    def hien_thi_tat_ca(self):
        if len(self.danh_sach_sach) == 0:
            print("Thư viện chưa có sách!")
            return
        bang = PrettyTable()
        bang.field_names = [
            "Mã sách",
            "Tên sách",
            "Tác giả",
            "Trạng thái"
        ]
        for sach in self.danh_sach_sach:
            bang.add_row(sach.hien_thi())
        print(bang)
    def muon_sach(self, ma_sach):
        for sach in self.danh_sach_sach:
            if sach.ma_sach == ma_sach:
                if sach.trang_thai == "Sẵn sàng":
                    sach.trang_thai = "Đã mượn"
                    print("Mượn sách thành công!")
                    return
                else:
                    print("Sách đã được mượn!")
                    return
        print("Không tìm thấy sách!")

def main():

    ql = QuanLyThuVien()

    while True:
        print("\n===== QUẢN LÝ THƯ VIỆN =====")
        print("1. Thêm sách")
        print("2. Hiển thị danh sách sách")
        print("3. Mượn sách")
        print("4. Thoát")
        lua_chon = input("Nhập lựa chọn: ")
        if lua_chon == "1":
            ma_sach = input("Nhập mã sách: ")
            ten_sach = input("Nhập tên sách: ")
            tac_gia = input("Nhập tác giả: ")
            sach = Sach(ma_sach, ten_sach, tac_gia)
            ql.them_sach(sach)
        elif lua_chon == "2":
            ql.hien_thi_tat_ca()
        elif lua_chon == "3":
            ma_sach = input("Nhập mã sách cần mượn: ")
            ql.muon_sach(ma_sach)
        elif lua_chon == "4":
            print("Thoát chương trình!")
            break
        else:
            print("Lựa chọn không hợp lệ!")
main()