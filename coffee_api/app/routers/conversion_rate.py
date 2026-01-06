from fastapi import APIRouter, Depends

router = APIRouter(prefix="/conversion", tags=["conversion"])

@router.get("/")
def tinh_thanh(do_nguyen:int, do_le:int, khoi_luong: float, gia_nhan: float):
    trong_luong = 0
    table = {
        15: [0, 0.1, 0.2, 0.37, 0.47, 0.57, 0.67, 0.77, 0.88, 0.99],
        16: [1.13, 1.24, 1.35, 1.46, 1.57, 1.68, 1.8, 1.9, 2.04, 2.16],
        17: [2.31, 2.44, 2.6, 2.7, 2.88, 2.96, 3.1, 3.2, 3.38, 3.52],
        18: [3.67, 3.81, 3.96, 4.11, 4.26, 4.41, 4.56, 4.7, 4.87, 5.05],
        19: [5.5, 5.67, 5.84, 6.01, 6.18, 6.35, 6.53, 6.7, 6.89, 7.07],
        20: [7.25, 7.43, 7.61, 7.79, 7.89, 8.16, 8.43, 8.6, 8.83, 9.03],
        21: [9.21, 9.44, 9.66, 9.88, 10.09, 10.32, 10.51, 11, 11.21, 11.22],
        22: [11.4, 11.7, 11.9, 12.13, 12.36, 12.59, 12.85, 13, 13.4, 13.6],
        23: [13.9, 14.1, 14.35, 14.6, 14.9, 15.2, 15.2, 16, 16.1, 16.4],
        24: [16.7, 17, 17.35, 17.7, 18.05, 18.4, 18.75, 19, 19.5, 19.8],
    }
    row = do_nguyen
    col = do_le
    if row in table and 0 <= col <= 9:
        trong_luong = table[row][col]
        print("Kết quả:", trong_luong)
    else:
        print("Giá trị nhập không hợp lệ!")

    ty_trong = trong_luong*khoi_luong/100
    hieu_ty_trong = khoi_luong - ty_trong
    thanh = 1000 / hieu_ty_trong
    gia_tuoi = gia_nhan / thanh
    return  {"trong_luong":trong_luong,"ty_trong": ty_trong,"hieu_ty_trong": hieu_ty_trong,"thanh":thanh,"gia_tuoi": gia_tuoi}