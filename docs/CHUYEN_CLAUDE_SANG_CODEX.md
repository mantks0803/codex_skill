# Những gì đã chuyển để dùng với Codex

Nguồn được khóa tại commit 6f05f460be7f0872503d2f338f071917cbad4e4b.
Bản gốc còn tại upstream/codeskills; bạn có thể mở cạnh bản mới để đối chiếu.

| Thành phần bản gốc | Bản đang dùng | Lý do |
|---|---|---|
| src/CLAUDE.md | AGENTS.md ở gốc dự án | Tên hướng dẫn dự án mà Codex nhận |
| src/skills/experiment/SKILL.md | .agents/skills/experiment/SKILL.md | Vị trí skill cấp dự án |
| Tham chiếu CLAUDE.md §0/§3 | Hướng dẫn đọc AGENTS.md và workflow tự đủ nghĩa | Skill không phụ thuộc tên file Claude |
| EnterWorktree, isolation: worktree | Dùng công cụ worktree sẵn có khi cần; có cách chạy tuần tự | Không giả định có công cụ riêng của Claude |
| Luôn đánh giá trước mọi lời giải | Đánh giá mục tiêu/giả định khi công việc đáng kể | Việc đơn giản được xử lý trực tiếp |
| Phải commit mọi dự đoán | Lưu dự đoán trước khi chạy; commit chỉ khi quy trình cần | Bài học nhỏ hoạt động khi chưa có commit |
| exp/... | codex/exp/... nếu cần tạo nhánh | Convention của môi trường Codex |
| --max-budget-usd, tên công cụ tìm kiếm cố định | Giới hạn số lần thử và công cụ có thật trong phiên | Tránh dùng cờ/lệnh không được hỗ trợ |
| Dọn các nhánh theo mẫu tên | Chỉ dọn tài nguyên của đúng thí nghiệm sau khi lưu bài học | Bảo toàn công việc ngoài thí nghiệm |

Giữ lại phần cốt lõi: hiểu mục tiêu, kiểm tra giả định, code vừa đủ, sửa đúng phạm vi,
kiểm chứng, chẩn đoán khi thất bại, lưu lại bài học cả khi loại một phương án.

AGENTS.md còn có quy tắc riêng của bài học dữ liệu: giữ mã dạng chuỗi, phân biệt
trống/0/ký hiệu, không sửa raw, và gọi ví dụ là ví dụ. Khi đưa sang dự án khác,
đọc lại phần Purpose, Data rules, Environment và thay lệnh kiểm tra cho đúng dự án.

Không cần đổi tên CLAUDE.md của repo gốc. Cũng không cần thêm CLAUDE.md vào cấu hình
fallback toàn máy, vì dự án này đã có AGENTS.md. install-claude.sh là trình cài cho
.claude và không được chạy trong tutorial này.

Tài liệu chính thức:
- https://learn.chatgpt.com/docs/agent-configuration/agents-md
- https://learn.chatgpt.com/docs/build-skills
