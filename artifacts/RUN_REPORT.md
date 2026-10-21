# Kết quả đã chạy — 21/10/2026

Thư mục: D:\codex-skills-lab-20261021
Python: 3.13.15. Môi trường: .venv. PyYAML: 6.0.3.
Nguồn skill: hieupth/codeskills, commit 6f05f460be7f0872503d2f338f071917cbad4e4b.

## Cài đặt

Skill gốc được tải bằng helper chính thức install-skill-from-github.py, với
--dest trỏ tới .agents/skills trong dự án. Sau đó đã sửa SKILL.md cho Codex và
tạo AGENTS.md từ các nguyên tắc của CLAUDE.md. Validator chính thức báo
`Skill is valid!`.

Đây là kiểm tra cấu trúc file skill. Chưa phải bằng chứng rằng một chat Codex có
thư mục làm việc ở nơi khác đã tự nạp skill. Hãy mở dự án D: này trong Codex và
kiểm tra theo README_VI.md. Phiên làm mẫu đã áp dụng quy trình sau khi đọc nội dung
skill trực tiếp: ghi giả thuyết trước, chạy, so sánh, lưu kết luận.

## Ba ví dụ

| Lệnh sau đường dẫn Python | Kết quả thực tế |
|---|---|
| -m examples.profile_data | 6 dòng, 4 cột; mã 001–006 được giữ nguyên; amount có 1 ô trống, 1 dấu -, 1 chuỗi 0, 1 chuỗi 0đ |
| -m examples.compare_policies | first_number đúng 5/10; explicit_policy đúng 10/10; A sai N02, N04, N07, N08, N09 |
| -m examples.repair_plan | 1 đề xuất chuẩn hóa status, 4 ô cần xem xét, 0 thay đổi áp dụng |

Nguồn giữ nguyên: SHA-256 trước và sau giống nhau trong 01_profile.json và
03_repair_plan.json. Hash là dấu vân tay của nội dung file, giúp nhận biết thay đổi.

## Kiểm tra

Lệnh: `.\.venv\Scripts\python.exe -m unittest discover -s tests -v`
Kết quả: 5 tests, OK.

Các kiểm tra phủ: ID có số 0 đầu; phân biệt các ký hiệu tiền; điểm số trên fixture;
policy/account và trường hợp nhiều mã; kế hoạch không sửa nguồn; dòng CSV thừa
cột phải báo lỗi thay vì bị bỏ âm thầm.

## Phạm vi

Các file dữ liệu đều là ví dụ giả do tutorial tạo. Không dùng workbook thật của
mentor. Đây không phải điểm PrepBench, không phải kiểm chứng trên dữ liệu ngoài
mẫu, không phải package hieupth.dataprep hay Go Harness đã triển khai.
Không tự tạo phê duyệt nghiệp vụ từ kết quả test.
