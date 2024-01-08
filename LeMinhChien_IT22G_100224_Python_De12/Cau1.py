class Sach:
    def __init__(self, maSach, tieuDe, tacGia, namXuatBan):
        self.__maSach = maSach
        self.__tieuDe = tieuDe
        self.__tacGia = tacGia
        self.__namXuatBan = namXuatBan

    @property
    def maSach(self):
        return self.__maSach

    @maSach.setter
    def maSach(self, maSach):
        self.__maSach = maSach

    @property
    def tieuDe(self):
        return self.__tieuDe

    @tieuDe.setter
    def tieuDe(self, tieuDe):
        self.__tieuDe = tieuDe

    @property
    def tacGia(self):
        return self.__tacGia

    @tacGia.setter
    def tacGia(self, tacGia):
        self.__tacGia = tacGia

    @property
    def namXuatBan(self):
        return self.__namXuatBan

    @namXuatBan.setter
    def namXuatBan(self, namXuatBan):
        self.__namXuatBan = namXuatBan

    def thanhTien(self):
        pass

    def __str__(self):
        return "Ma sach: " + self.__maSach + "\nTieu de: " + self.__tieuDe + "\nTac gia: " + self.__tacGia + "\nNam xuat ban: " + self.__namXuatBan


class SachGiaoKhoa(Sach):
    def __init__(self, maSach, tieuDe, tacGia, namXuatBan, soTrang):
        super().__init__(maSach, tieuDe, tacGia, namXuatBan)
        self.__soTrang = soTrang

    @property
    def soTrang(self):
        return self.__soTrang

    @soTrang.setter
    def soTrang(self, soTrang):
        self.__soTrang = soTrang

    def thanhTien(self):
        return self.__soTrang * 200


maSach = input("Nhap ma sach: ")
tieuDe = input("Nhap tieu de: ")
tacGia = input("Nhap tac gia: ")
namXuatBan = input("Nhap nam xuat ban: ")
soTrang = int(input("Nhap so trang: "))
sgk = SachGiaoKhoa(maSach, tieuDe, tacGia, namXuatBan, soTrang)
print(sgk)
print("Thanh tien:", sgk.thanhTien())
