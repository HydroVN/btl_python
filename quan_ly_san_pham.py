import json
with open("d:/btl_python/san_pham.json", "r", encoding="utf-8") as f:
    danh_sach1 = json.load(f)
def nhap_san_pham():
    try:
        while True:
            them_ma_san_pham = input("Nhập mã sản phẩm mới: ").strip()
            # Kiểm tra mã sản phẩm đã tồn tại
            if any(sp.get("ma_sp", "").lower() == them_ma_san_pham.lower() for sp in danh_sach1): #any: kiểm tra mã sản phẩm đã tồn tại hay không
                # Nếu mã sản phẩm đã tồn tại (trả về true), yêu cầu nhập lại và ngược lại (trả về false) thì tiếp tục
                print("Mã sản phẩm đã tồn tại. Vui lòng nhập mã khác.")
                continue  # Quay lại vòng lặp để nhập lại mã sản phẩm
            ten_san_pham = input("Nhập tên sản phẩm: ").strip()
            # Kiểm tra tên sản phẩm đã tồn tại
            if any(sp.get("ten_sp", "").lower() == ten_san_pham.lower() for sp in danh_sach1):
                print("Tên sản phẩm đã tồn tại. Vui lòng nhập tên khác.")
                continue  
            nha_cung_cap = input("Nhập nhà cung cấp: ")
            gia_ban = float(input("Nhập giá bán: "))
            so_luong = int(input("Nhập số lượng: "))
            # Thêm sản phẩm mới vào danh sách
            danh_sach1.append({
                "ma_sp": them_ma_san_pham,
                "ten_sp": ten_san_pham,
                "nha_cung_cap": nha_cung_cap,
                "gia": gia_ban,
                "so_luong": so_luong
            })
            break
    except FileNotFoundError:
        print("Không tìm thấy file sản phẩm.")
    except json.JSONDecodeError:
        print("Lỗi khi đọc file sản phẩm.")
    except ValueError:
        print("Giá trị không hợp lệ. Vui lòng nhập lại.")
    else:
        with open("d:/btl_python/san_pham.json", "w", encoding="utf-8") as f:
            json.dump(danh_sach1, f, ensure_ascii=False, indent=4)
            print("Đã thêm sản phẩm thành công.")
def hien_thi_danh_sach():
    try:
        if not danh_sach1:
            print("Danh sách sản phẩm trống.")
            return
        print(f"{'Mã sản phẩm':<15} | {'Tên sản phẩm':<30} | {'NCC':<20} | {'Giá':<8} | {'Số lượng':<10}")
        print("-" * 95)
        for sp in danh_sach1:
            print(f"{sp['ma_sp']:<15} | {sp['ten_sp']:<30} | {sp['nha_cung_cap']:<20} | {sp['gia']:<8} | {sp['so_luong']:<10}")
    except FileNotFoundError:
        print("Không tìm thấy file sản phẩm.")
    except json.JSONDecodeError:
        print("Lỗi khi đọc file sản phẩm.")
def tim_san_pham():
    ma_sp = input("Nhập mã sản phẩm cần tìm: ").strip()
    try:
        for sp in danh_sach1:
            if sp["ma_sp"].lower() == ma_sp.lower():
                print(f"Mã sản phẩm: {sp['ma_sp']}")
                print(f"Tên sản phẩm: {sp['ten_sp']}")
                print(f"Nhà cung cấp: {sp['nha_cung_cap']}")
                print(f"Giá bán: {sp['gia']}")
                print(f"Số lượng: {sp['so_luong']}")
                return
        print("Không tìm thấy sản phẩm.")
    except FileNotFoundError:
        print("Không tìm thấy file sản phẩm.")
    except json.JSONDecodeError:
        print("Lỗi khi đọc file sản phẩm.")
def cap_nhat_thong_tin_san_pham():
    ma_sp = input("Nhập mã sản phẩm cần cập nhật: ").strip()
    try:
        for sp in danh_sach1:
            if sp["ma_sp"].lower() == ma_sp.lower():
                ten_san_pham = input("Nhập tên sản phẩm mới: ").strip()
                nha_cung_cap = input("Nhập nhà cung cấp mới: ")
                gia_ban = float(input("Nhập giá bán mới: "))
                so_luong = int(input("Nhập số lượng mới: "))
                sp.update({
                    "ten_sp": ten_san_pham,
                    "nha_cung_cap": nha_cung_cap,
                    "gia": gia_ban,
                    "so_luong": so_luong
                })
                with open("d:/btl_python/san_pham.json", "w", encoding="utf-8") as f:
                    json.dump(danh_sach1, f, ensure_ascii=False, indent=4)
                print("Cập nhật thành công.")
                return
        print("Không tìm thấy sản phẩm.")
    except FileNotFoundError:
        print("Không tìm thấy file sản phẩm.")
    except json.JSONDecodeError:
        print("Lỗi khi đọc file sản phẩm.")
    except ValueError:
        print("Giá trị không hợp lệ. Vui lòng nhập lại.")
    except Exception as e:
        print(f"Lỗi không xác định: {e}")
def xoa_san_pham():
    ma_sp = input("Nhập mã sản phẩm cần xóa: ").strip()
    try:
        for sp in danh_sach1:
            if sp["ma_sp"].lower() == ma_sp.lower():
                danh_sach1.remove(sp)
                with open("d:/btl_python/san_pham.json", "w", encoding="utf-8") as f:
                    json.dump(danh_sach1, f, ensure_ascii=False, indent=4)
                print("Xóa sản phẩm thành công.")
                return
        print("Không tìm thấy sản phẩm.")
    except FileNotFoundError:
        print("Không tìm thấy file sản phẩm.")
    except json.JSONDecodeError:
        print("Lỗi khi đọc file sản phẩm.")
if __name__ == "__main__":
    while True:
        print("=== QUẢN LÝ CỬA HÀNG ===")
        print("1. Thêm sản phẩm mới")
        print("2. Hiển thị danh sách sản phẩm")
        print("3.Tìm sản phẩm theo mã")
        print("4. Cập nhật thông tin sản phẩm")
        print("5. Xóa sản phẩm")
        print("6. Thêm khách hàng")
        print("7. Hiển thị danh sách khách hàng")
        print("8. Tìm khách hàng theo mã")
        print("9. Cập nhật thông tin khách hàng")
        print("10. Xóa khách hàng")
        print("11. Thêm nhân viên")
        print("12. Hiển thị danh sách nhân viên")
        print("13. Tìm nhân viên theo mã")
        print("14. Cập nhật thông tin nhân viên")
        print("15. Xóa nhân viên")
        print("16. Lập hóa đơn bán hàng")
        print("17. Thống kê doanh thu")
        print("18. Thống kê số lượng sản phẩm đã bán")
        print("19. Thống kê số lượng sản phẩm tồn kho")
        print("20. Thoát")
        print("============================")
        lua_chon = int(input("Nhập lựa chọn của bạn (1–7): "))
        if lua_chon == 1:
            nhap_san_pham()
        elif lua_chon == 2:
            hien_thi_danh_sach()
        elif lua_chon == 3:
            tim_san_pham()
        elif lua_chon == 20:
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng nhập lại.")
