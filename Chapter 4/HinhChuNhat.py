class HinhChuNhat:
    def __init__(self, chieu_dai, chieu_rong):
        self.chieu_dai = chieu_dai
        self.chieu_rong = chieu_rong
    def tinh_chu_vi(self):
        return (self.chieu_dai + self.chieu_rong) * 2
    def tinh_dien_tich(self):
        return self.chieu_dai * self.chieu_rong
hcn1 = HinhChuNhat(10, 5)
print(hcn1.tinh_chu_vi())
print(hcn1.tinh_dien_tich())