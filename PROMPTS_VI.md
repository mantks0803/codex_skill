# Prompt để sử dụng lần lượt trong Codex

Các đoạn bên dưới dán vào ô chat Codex khi đang mở đúng dự án D: này.
Đây không phải lệnh PowerShell. Dấu $experiment là cách gọi skill.

## 1. Kiểm tra nạp hướng dẫn

```text
Cho biết thư mục làm việc hiện tại. Liệt kê đường dẫn các file hướng dẫn dự án
và skill experiment đang được nạp. Đọc AGENTS.md và giải thích 5 quy tắc quan trọng
cho người mới. Nếu chưa thấy skill, nói rõ; đừng chỉ suy đoán nó đã hoạt động.
```

## 2. Bài đơn giản: không cần experiment

```text
Đọc data/raw/customers.csv và examples/profile_data.py. Chạy ví dụ 1 bằng Python
trong .venv. Giải thích từng cột, dòng có mã 003, và vì sao 0, 0đ, -, ô trống được
đếm riêng. Mở artifacts/01_profile.json và chỉ ra các con số thực tế. Giữ nguyên raw.
```

## 3. Gọi experiment và học từ lần chạy đã có

```text
$experiment Đọc .experiments/policy-number/ và artifacts/02_comparison.json.
Giải thích giả thuyết, dự đoán, kết quả và kết luận của hai cách lấy số hợp đồng.
Dùng kết quả đã có nếu code và dữ liệu chưa đổi. Giải thích N02, N04, N06, N07.
Chỉ rõ vì sao điểm này không phải điểm PrepBench và không chứng minh đúng mọi câu.
```

## 4. Một thí nghiệm mới có thêm bằng chứng

```text
$experiment So sánh lại hai cách với dữ liệu mới. Tạo data/notes_cases_extra.json
gồm 4 ghi chú giả mới: invoice đứng trước policy, account không có policy,
policy có số 0 đầu, và hai policy trong một câu. Viết đáp án theo đúng quy tắc
ở CHARTER trước khi chạy. Lưu charter và kết quả vào .experiments/policy-extra/.
Dùng hai hàm hiện có, mỗi cách chạy một lần. Giải thích từng ca, không đổi raw
hay sửa đáp án sau khi xem kết quả. Thực hiện tuần tự.
```

## 5. Đọc đề xuất sửa

```text
Chạy examples.repair_plan bằng .venv. Giải thích 1 đề xuất và 4 ô cần xem xét.
Cho biết tại sao status 31 chưa được chuyển thành Thành công hay ô trống.
Đối chiếu hash nguồn trước/sau và cho biết có ô nào đã thực sự bị sửa không.
```

## 6. Kết nối với tài liệu mentor

```text
Đọc blueprint thư viện hieupth.dataprep đã được mentor cung cấp. Đối chiếu ví dụ
profile_data với DP-07 và DP-08: phần nào mới minh họa, phần nào còn thiếu để
được nghiệm thu. Lập danh sách đầu ra cụ thể, không tuyên bố lab đã hoàn thành
task của mentor. Sau đó hướng dẫn tôi triển khai từng phần.
```
