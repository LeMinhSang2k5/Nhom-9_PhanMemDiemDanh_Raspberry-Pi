import pandas as pd
import os

excel_file = "diem_danh.xlsx"  # Đảm bảo tên file đúng

def read_attendance():
    if not os.path.exists(excel_file):
        print("⚠ File diem_danh.xlsx không tồn tại! Tạo file mới...")
        df = pd.DataFrame(columns=["MSSV", "Họ_tên", "Giới_tính", "Lớp", "Ngày", "Thời_gian"])
        df.to_excel(excel_file, index=False)  # Tạo file mới nếu chưa có
        return df

    return pd.read_excel(excel_file)
