# Python Rename Files
Xin chào, mình là Vinh đây. 

[![Python Rename Files](http://img.youtube.com/vi/aRmBLWA_czA/0.jpg)](http://www.youtube.com/watch?v=aRmBLWA_czA)

Đây là code Python Đổi tên Files hàng loạt một cách miễn phí, nhanh chóng. Có thể xử lý bao nhiêu cũng được, tốc độ nhanh.


## Giới thiệu

Dự án này bao gồm 2 script Python nhằm mục đích đổi tên hàng loạt file trong một thư mục. Bạn có thể tùy chỉnh cách đổi tên file bằng cách thêm tiền tố (prefix), hậu tố (suffix), hoặc dùng một mã định danh với số thứ tự tự động.

---

## Các tệp trong dự án

### 1. `file_renamer.py`

**Mục đích**: Đổi tên các file trong thư mục được chỉ định bằng việc thêm tiền tố (prefix) hoặc hậu tố (suffix).

**Cách hoạt động**: 
  - Lọc các file dựa trên loại file (phần mở rộng ví dụ như `.txt`, `.jpg`).
  - Thêm prefix và/hoặc suffix vào tên của file mà không thay đổi phần mở rộng.

**Các tham số đầu vào**:
  - `folder_path`: Đường dẫn đến thư mục chứa file cần đổi tên.
  - `input_types`: Danh sách các phần mở rộng file muốn đổi (có thể để trống để áp dụng cho tất cả).
  - `prefix`: Thêm tiền tố vào tên file.
  - `suffix`: Thêm hậu tố vào tên file.

**Ví dụ**:
  - File ban đầu: `document.txt`
  - Sau khi đổi tên (prefix: `new_`, suffix: `_v1`): `new_document_v1.txt`.

---

### 2. `file_renamer2.py`

**Mục đích**: Đổi tên các file trong thư mục bằng cách sử dụng một tên gốc (base name) kết hợp với số thứ tự.

**Cách hoạt động**:
  - Lọc các file cần đổi tên dựa trên loại file (phần mở rộng file).
  - Gán tên mới với định dạng: `[base_name]-[số_thứ_tự].[phần_mở_rộng]`.

**Các tham số đầu vào**:
  - `folder_path`: Đường dẫn đến thư mục chứa file cần đổi tên.
  - `input_types`: Danh sách các phần mở rộng file muốn đổi (có thể để trống để áp dụng cho tất cả).
  - `base_name`: Tên gốc để áp dụng cho các file. Mặc định là `image`.

**Ví dụ**:
  - File ban đầu: `photo.jpg`
  - Sau khi đổi tên (base_name: `custom`): `custom-1.jpg`.

---

Đọc thêm tại: https://vinhweb.com/blog/code-python-optimize-toi-uu-hinh-anh-mien-phi

Nhiều source code hay hơn nữa tại website: https://vinhweb.com/.

Hãy mua để ủng hộ Vinh phát triển thêm nhé. Cảm ơn bạn.


## Hướng dẫn setup:
Hướng setup Python Project để chạy được source này tại [đây](https://mango-freesia-da4.notion.site/Doc-H-ng-d-n-Setup-Python-Project-VinhWeb-19274673f5db80679725d682c13c7f90?pvs=74)
