def dem_ly_tu_hoa_thuong(chuoi):
    hoa = 0
    thuong = 0
    for ki_tu in chuoi:
        if ki_tu.isupper():
            hoa += 1
        elif ki_tu.islower():
            thuong += 1
    return hoa, thuong

chuoi = input("Nhập chuỗi: ")
so_ky_tu_hoa, so_ky_tu_thuong = dem_ly_tu_hoa_thuong(chuoi)
print(f"Số lượng ký tự hoa trong chuỗi: {so_ky_tu_hoa}")
print(f"Số lượng ký tự thường trong chuỗi: {so_ky_tu_thuong}")
