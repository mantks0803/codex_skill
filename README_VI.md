# Bắt đầu ở đây: codeskills cho Codex và ba bài thực hành

Đã chuẩn bị và chạy ngày 21/10/2026 tại **D:\codex-skills-lab-20261021**.
Bạn có thể mở file này trong VS Code và làm lần lượt. Những lệnh ở lộ trình chính
chạy lại bài đã có; phần cuối chỉ cách tự tạo file và cài sang folder khác.

## 1. Hiểu ba thứ trước khi thao tác

**AGENTS.md** là tờ hướng dẫn chung cho Codex trong dự án: nói tiếng Việt, sửa đúng
phạm vi, giữ dữ liệu gốc, kiểm tra kết quả. Bạn không chạy file Markdown bằng Python.

**Skill experiment** là quy trình được dùng khi so sánh vài cách giải: ghi giả thuyết
→ dự đoán → thử → đo → kết luận. Nó không phải mô hình AI mới, không cần train và
không phải thư viện Python cài bằng pip. File chính của skill là SKILL.md.

**Môi trường .venv** là bộ Python riêng cho bài thực hành. Nó dùng để chạy code.
Skill và AGENTS.md hướng dẫn Codex làm việc; .venv chạy chương trình bạn viết.

Repo gốc hiện có một bộ quy tắc và một skill, chưa có bộ công cụ tự làm sạch dữ liệu.
Mình đã cài skill theo dự án để các file cấu hình mới nằm trên D:. Bạn phải mở
đúng dự án này trong Codex để nó được phát hiện ở phạm vi dự án.

## 2. Mở trong VS Code

1. Trong VS Code, chọn **File → Open Folder…**.
2. Chọn **D:\codex-skills-lab-20261021**, rồi **Select Folder**.
3. Mở README_VI.md ở cột Explorer bên trái. Nhấn **Ctrl+Shift+V** để xem bản dễ đọc.
4. Chọn **Terminal → New Terminal**. Dùng terminal PowerShell.
5. Gõ lệnh sau và nhấn Enter:

```powershell
Set-Location 'D:\codex-skills-lab-20261021'
Get-Location
.\.venv\Scripts\python.exe --version
```

Kết quả cần thấy: đường dẫn D: ở trên và Python **3.13.15** trên máy hiện tại.
VS Code đã có extension Python. Chọn interpreter bằng **Ctrl+Shift+P** → gõ
**Python: Select Interpreter** → chọn **.venv\Scripts\python.exe** trong folder này.
Nếu danh sách chưa hiện, dùng **Enter interpreter path…** rồi chọn file đó.

Các lệnh trong bài gọi Python theo đường dẫn đầy đủ nên không cần chạy Activate.ps1
hay thay đổi ExecutionPolicy. Nếu bạn tự dựng môi trường mới, lệnh là:

```powershell
py -3.13 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements-dev.txt
```

Môi trường ở folder đã chuẩn bị sẵn thì không cần tạo lại. Ba ví dụ chỉ dùng thư
viện đi kèm Python. PyYAML 6.0.3 trong requirements-dev.txt dùng cho trình kiểm tra
cấu trúc skill chính thức của Codex.

## 3. Nhận diện các file và việc đã chuyển từ Claude

```text
codex-skills-lab-20261021/
├── AGENTS.md                         Quy tắc Codex cho dự án
├── .agents/skills/experiment/
│   ├── SKILL.md                      Quy trình so sánh phương án đã chuyển cho Codex
│   └── LICENSE                       Giấy phép gốc
├── .venv/                            Môi trường Python, đã tạo
├── .vscode/settings.json             Interpreter và terminal cho VS Code
├── data/
│   ├── raw/customers.csv             6 dòng dữ liệu giả để học
│   └── notes_cases.json              10 ghi chú giả và đáp án khai báo
├── examples/
│   ├── __init__.py                   Cho phép chạy bằng python -m examples...
│   ├── lab_io.py                     Đọc CSV, tính hash, ghi JSON
│   ├── profile_data.py               Bài 1: quan sát và đếm
│   ├── compare_policies.py           Bài 2: so sánh hai cách lấy mã
│   └── repair_plan.py                Bài 3: đề xuất sửa
├── tests/test_examples.py            5 kiểm tra bảo toàn dữ liệu và kết quả
├── artifacts/                       Kết quả thực chạy và RUN_REPORT.md
├── .experiments/                    Giả thuyết, dự đoán, log, kết luận bài 2
├── docs/CHUYEN_CLAUDE_SANG_CODEX.md   Bảng giải thích các chỗ chuyển đổi
├── PROMPTS_VI.md                     Prompt mẫu để dán vào Codex
├── requirements-dev.txt              Phụ thuộc của trình kiểm tra skill
├── THIRD_PARTY_NOTICES.md            Nguồn, phiên bản và thay đổi
├── LICENSE.codeskills               Giấy phép nguồn giữ nguyên
├── .gitignore                       Bỏ qua môi trường và bản clone tham khảo
├── .git/                            Repo Git cục bộ mới, chưa commit/push
├── .tmp/                            File tạm dùng cho cài đặt và kiểm tra
└── upstream/codeskills/              Bản clone gốc để tham khảo
```

Mở AGENTS.md rồi mở .agents/skills/experiment/SKILL.md. Đây là **hai file cần
thiết lập cho Codex**. .vscode/settings.json phục vụ VS Code; không thay thế chúng.

Bản gốc src/CLAUDE.md được chuyển thành AGENTS.md và chọn lại quy tắc phù hợp.
Skill được sửa tham chiếu CLAUDE.md, công cụ EnterWorktree, các cờ riêng của Claude,
yêu cầu commit bắt buộc và cách dọn nhánh. Bản gốc vẫn nằm trong upstream/.
Xem chi tiết trong docs/CHUYEN_CLAUDE_SANG_CODEX.md.

## 4. Để Codex nhận đúng dự án và skill

VS Code là nơi mở file/chạy terminal. Bạn có thể dùng ứng dụng Codex cạnh VS Code:
trong Codex, dùng chức năng thêm hoặc mở dự án từ thư mục, chọn chính folder D:
này, rồi bắt đầu chat trong dự án đó. Không cần cài API key để chạy các ví dụ.

Ở lần kiểm tra, VS Code máy này chưa có extension Codex. Hướng dẫn này dùng Codex
desktop đã có sẵn; không phụ thuộc việc cài thêm extension vào profile trên C:.
Nếu bạn đã cài extension sau đó, cũng phải mở cùng folder trong VS Code.

Dán vào **ô chat Codex**, không phải terminal:

```text
Cho biết thư mục làm việc hiện tại. Đọc AGENTS.md của dự án và liệt kê đường dẫn
skill experiment mà bạn thấy. Tóm tắt 5 quy tắc quan trọng cho người mới.
Nếu chưa thấy skill, nói rõ điều đó.
```

Bạn cần thấy đường dẫn kết thúc bằng:

```text
codex-skills-lab-20261021\AGENTS.md
codex-skills-lab-20261021\.agents\skills\experiment\SKILL.md
```

Skill mới có thể dùng từ lượt tiếp theo khi Codex đang ở đúng dự án. Theo tài liệu,
Codex tự phát hiện thay đổi skill; nếu chưa hiện, khởi động lại Codex và mở lại
dự án. Với AGENTS.md mới, bắt đầu phiên/chat trong folder này để nạp hướng dẫn.
Việc validator báo hợp lệ không chứng minh một chat ở folder khác đã nạp skill.

Bạn có thể gọi bằng `$experiment` trong prompt. Khi dùng CLI/extension, `/skills`
hoặc dấu `$` là cách tìm skill; không gõ chúng vào PowerShell.

## 5. Bài 1: biết dữ liệu đang có gì trước khi sửa

Mở **data/raw/customers.csv**. Một dòng là một khách hàng giả; có bốn cột:
customer_id = mã, status = trạng thái, amount = chuỗi tiền, branch = nơi bán.
Đây không phải file thật 99 dòng của mentor.

```csv
customer_id,status,amount,branch
001,Thành công,0đ,Ha Noi
002,Thất bại,-,ha noi
003,,,
004, thành công ,150000đ,Da  Nang
005,31, 250000đ ,da nang
006,Chờ kích hoạt,0,HCM
```

Mục tiêu: đếm dữ liệu theo đúng thứ đang lưu. 001 là mã chữ, không đổi thành số 1.
Dòng 003 thiếu thông tin; dòng 005 có status 31 nhưng chưa biết ý nghĩa.

Chạy trong terminal:

```powershell
.\.venv\Scripts\python.exe -m examples.profile_data
```

`-m` nghĩa là chạy phần code tên examples.profile_data trong dự án. Output chính:

```text
Rows: 6 | Columns: 4
IDs: 001, 002, 003, 004, 005, 006
Amount: empty=1, dash=1, text 0=1, text 0d=1
Source unchanged: True
```

Mở **artifacts/01_profile.json**. JSON ghi thành từng cặp tên: giá trị.
row_count là số dòng dữ liệu, column_count là số cột. Trong columns.amount,
empty_string_count=1 là ô trống, dash_count=1 là dấu -, literal_zero_count=1 là
chuỗi 0, zero_with_currency_marker_count=1 là chuỗi 0đ. Terminal viết 0d cho dễ
hiển thị; JSON và CSV vẫn giữ nguyên ký tự đ.

Không cộng bốn loại thành số 0. Bạn mới quan sát cách viết, chưa có quy định nghiệp
vụ về dấu -. CSV này không khai báo giá trị null riêng; vì vậy không giả vờ phân
biệt được database-null với ô trống từ cùng một chuỗi rỗng.

Code để đọc theo thứ tự: examples/profile_data.py → hàm build_profile → vòng for
qua từng cột → các phép đếm → phần main ghi báo cáo. Trong examples/lab_io.py,
read_csv_rows đọc chuỗi nguyên trạng và báo lỗi nếu số cột của dòng bị sai.

Bạn đã đạt bài này khi tự chỉ ra được 1 ô amount trống, 1 dấu -, 1 số 0 dạng chữ,
1 chuỗi 0đ và lý do mã 001 phải giữ số 0 đầu.

## 6. Bài 2: dùng experiment để so sánh hai cách lấy số hợp đồng

Tình huống xuất phát từ bài PrepBench ghi chú cuộc gọi bạn đã học, nhưng quy tắc
bài này được khai báo riêng: **chỉ lấy mã khi có đúng một cụm policy #digits**.
Nhiều mã hoặc không có nhãn policy thì trả null để xem xét. Giữ mã dưới dạng chữ.
Đây là dữ liệu mới để học, không phải thay đổi lời giải PrepBench đã chạy.

Mở data/notes_cases.json. note là ghi chú; expected là đáp án theo quy tắc giả định
trên. null nghĩa là chưa trả về một mã, không phải số 0.

Mở examples/compare_policies.py:

- first_number tìm dãy số sau dấu # đầu tiên.
- explicit_policy tìm các cụm policy #số, chỉ trả kết quả khi có đúng một cụm.
- compare cho cả hai cách cùng 10 câu, so với đáp án và ghi từng ca đúng/sai.

Trước lúc chạy, mình đã lưu mục tiêu và giới hạn vào .experiments/policy-number/
CHARTER.md. Hai file 01-first-number.md và 02-context.md chứa giả thuyết và dự đoán,
sau đó được bổ sung kết quả thực tế. Đây là cách áp dụng workflow experiment.

Chạy để xem lại:

```powershell
.\.venv\Scripts\python.exe -m examples.compare_policies
```

Kết quả:

```text
first_number: 5/10 correct
  Mismatches: N02, N04, N07, N08, N09
explicit_policy: 10/10 correct
  Mismatches: none
```

Đọc **artifacts/02_comparison.json** rồi xem các ví dụ sau:

| Ghi chú | Cách A | Cách B | Cần hiểu |
|---|---|---|---|
| Added to account #3001. | 3001 | null | Chữ account không chứng minh đây là mã policy |
| Invoice #9000; policy #2001. | 9000 | 2001 | Có hai số, nhưng nhãn nói chúng khác loại |
| Policy #0012 needs a statement. | 0012 | 0012 | Giữ số 0 đầu của mã |
| Asked about policy #2080 and policy #2081. | 2080 | null | Có hai hợp đồng nên chưa chọn một mã theo luật bài tập |

KEEP/REJECT trong nhật ký là giữ/loại cách xử lý **cho quy tắc của bài này**.
10/10 trên 10 câu giả không chứng minh thuật toán hiểu mọi câu tiếng Anh. Ví dụ
phủ định, lịch sử thay mã hay câu tiếng Việt vẫn cần thiết kế và kiểm tra thêm.
Quy tắc PrepBench case_005 ban đầu cho lấy bất kỳ #digits; không được dùng điểm ở
đây để kết luận lời giải theo đề PrepBench sai.

Muốn thực sự gọi skill từ chat, mở PROMPTS_VI.md và dùng prompt 3 để đọc kết quả,
hoặc prompt 4 để tạo thêm bốn ca mới rồi thử có ghi chép. `$experiment` là hướng
dẫn Codex áp dụng workflow; Python là công cụ chạy phép so sánh.

## 7. Bài 3: lập phương án sửa, phân biệt với đã sửa

Mở examples/repair_plan.py. KNOWN_STATUSES khai báo ba nhãn trạng thái hợp lệ cho
bài học. Đây là giả định giảng dạy đã ghi rõ, chưa phải phê duyệt nghiệp vụ thật.

Chạy:

```powershell
.\.venv\Scripts\python.exe -m examples.repair_plan
```

Kết quả:

```text
Proposed formatting changes: 1
Items needing interpretation: 4
Applied changes: 0
Source unchanged: True
```

Mở **artifacts/03_repair_plan.json**:

- Một đề xuất: mã 004, status từ ` thành công ` sang `Thành công`.
- Bốn ô cần xem xét: mã 002 có amount=-; mã 003 có status trống và amount trống;
  mã 005 có status=31. Đây là **4 ô ở 3 dòng**, không phải bốn khách hàng.
- applied_changes=0: chương trình chưa sửa ô nào trong file gốc.
- source_sha256_before và source_sha256_after giống nhau: nội dung nguồn giữ nguyên.

Không đổi 31 thành trạng thái thành công; không đổi '-' thành 0. Bước tiếp theo
trong dự án thật là chốt ý nghĩa và điều kiện sửa với người chịu trách nhiệm dữ liệu.
Skill/Markdown không tự thay thế các kiểm soát thực thi của thư viện hoặc Harness.

## 8. Chạy kiểm tra và đọc kết luận thật

```powershell
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
```

Cần thấy **Ran 5 tests** và **OK**. Test là những phép kiểm tự động, ví dụ file
nguồn phải giữ nguyên, mã có số 0 đầu phải giữ nguyên, dòng CSV thừa cột phải báo
lỗi. Nó không có nghĩa mọi trường hợp trên đời đã được kiểm tra.

Xem artifacts/RUN_REPORT.md để biết lần chạy đã làm gì. Năm kiểm tra cũng có thể
đọc trong tests/test_examples.py. `self.assertEqual(a, b)` kiểm a bằng b; không bằng
thì báo lỗi để người viết code tìm nguyên nhân.

## 9. Tự tạo file đầu tiên trong VS Code

Phần này dành cho bạn tập gõ và chạy; ba bài hoàn chỉnh phía trên đã có sẵn.

1. Trong Explorer, chuột phải vùng trống → **New Folder** → đặt tên **practice**.
2. Chuột phải practice → **New File** → đặt tên **my_first_profile.py**.
3. Dán code dưới đây, nhấn **Ctrl+S**:

```python
import csv
from pathlib import Path

# __file__ là file Python này; parents[1] là gốc folder dự án.
root = Path(__file__).resolve().parents[1]
source = root / "data" / "raw" / "customers.csv"

with source.open(encoding="utf-8", newline="") as stream:
    rows = list(csv.DictReader(stream))

print("So dong:", len(rows))
print("Ma khach hang dau:", rows[0]["customer_id"])

empty_amount = 0
for row in rows:
    if row["amount"] == "":
        empty_amount += 1

print("So o amount trong:", empty_amount)
```

4. Trong terminal tại gốc dự án, gõ:

```powershell
.\.venv\Scripts\python.exe .\practice\my_first_profile.py
```

Cần thấy `So dong: 6`, `Ma khach hang dau: 001`, `So o amount trong: 1`.
import lấy dụng cụ có sẵn của Python; source là đường tới CSV; DictReader biến mỗi
dòng thành nhóm tên cột → giá trị; vòng for đi qua từng dòng; if kiểm điều kiện;
print in kết quả. Bạn có thể đặt breakpoint bằng cách nhấp bên trái số dòng để
tập debug sau khi hiểu đoạn code.

Bài tự sửa nhỏ: tạo biến dash_amount, đếm khi row['amount'] == '-', rồi in kết quả.
Đáp án mong đợi là 1. Đây là việc nhỏ; không cần experiment.

## 10. Cài bộ đã chuyển đổi sang folder D: khác

Chỉ làm phần này nếu muốn có một dự án thực hành mới. Cài theo dự án là đặt đúng
AGENTS.md và thư mục skill. Không cần cài lại Python package để skill xuất hiện.
Lệnh dưới từ chối nếu folder đích đã tồn tại để tránh ghi đè bài bạn đang làm.

```powershell
$targetProject = 'D:\codex-skills-practice'
if (Test-Path -LiteralPath $targetProject) { throw 'Folder da ton tai; chon ten moi.' }
New-Item -ItemType Directory -Path "$targetProject\.agents\skills" -Force
Copy-Item -LiteralPath 'D:\codex-skills-lab-20261021\AGENTS.md' -Destination "$targetProject\AGENTS.md"
Copy-Item -LiteralPath 'D:\codex-skills-lab-20261021\.agents\skills\experiment' -Destination "$targetProject\.agents\skills\experiment" -Recurse
Copy-Item -LiteralPath 'D:\codex-skills-lab-20261021\THIRD_PARTY_NOTICES.md' -Destination "$targetProject\THIRD_PARTY_NOTICES.md"
Copy-Item -LiteralPath 'D:\codex-skills-lab-20261021\LICENSE.codeskills' -Destination "$targetProject\LICENSE.codeskills"
git -C $targetProject init -b codex/learning
code --new-window $targetProject
```

AGENTS.md được copy vẫn chứa lệnh và thư mục của lab. Mở nó và sửa Purpose,
Data rules, Environment, lệnh test theo dự án mới. Những script ví dụ chưa được
copy bởi các lệnh trên; chỉ cài quy tắc + skill. Đừng chạy lệnh test cho file chưa có.
Khi đã có dự án mentor thực tế, ghép quy tắc vào AGENTS.md hiện có; không ghi đè
hướng dẫn nhóm bằng bản lab.

## 11. Cách tải bản gốc từ GitHub nếu muốn học lại quy trình cài

Phần này là nguồn gốc thao tác đã thực hiện, không cần chạy lại trong lab hiện tại.
Phiên bản đã kiểm tra là **6f05f460be7f0872503d2f338f071917cbad4e4b**.

Trên một folder mới, helper skill-installer có thể tải bằng lệnh như sau (đổi
folder đích thành folder D: bạn vừa tạo, chưa có experiment):

```powershell
py -3.13 -B 'C:\Users\nguye\.codex\skills\.system\skill-installer\scripts\install-skill-from-github.py' --repo hieupth/codeskills --path src/skills/experiment --ref 6f05f460be7f0872503d2f338f071917cbad4e4b --dest 'D:\TEN_DU_AN_MOI\.agents\skills'
```

--repo là nguồn GitHub; --path chọn đúng thư mục skill; --ref khóa phiên bản;
--dest quyết định vị trí cài. Nếu không chỉ định --dest, helper có mặc định riêng
ở profile người dùng. Cài xong bản gốc vẫn có các chỉ dẫn Claude: dùng bản đã chuyển
ở lab hoặc chỉnh theo docs/CHUYEN_CLAUDE_SANG_CODEX.md, rồi tạo AGENTS.md.
Chỉ đổi tên CLAUDE.md không sửa được các lệnh riêng nằm trong SKILL.md.

Trong lần chuẩn bị này, thư mục tạm của installer cũng được trỏ vào .tmp trên D:.
Không chạy install-claude.sh để cài Codex: script gốc đặt file dưới .claude.

Lệnh kiểm tra cấu trúc skill sau khi đã có PyYAML:

```powershell
.\.venv\Scripts\python.exe -X utf8 -B 'C:\Users\nguye\.codex\skills\.system\skill-creator\scripts\quick_validate.py' '.\.agents\skills\experiment'
```

Cần thấy `Skill is valid!`. Đây là kiểm tra cấu trúc, còn chất lượng workflow phải
đánh giá bằng công việc thực tế như thí nghiệm có ghi chép ở trên.

## 12. Sau lab, nối sang việc mentor giao

Đọc hieupth_dataprep_blueprint_v0.0.1.md trước; đối chiếu workbook mẫu của mentor;
rồi đọc data_understanding_agent_blueprint_v0.0.1.md. Hai file gốc đang ở:

```text
C:\Users\nguye\OneDrive\Desktop\work\pythera_dataprep_blueprints_v0.0.1\
```

| Bài học trong lab | Task giúp bạn chuẩn bị | Còn cần làm trong dự án thật |
|---|---|---|
| profile dữ liệu và giữ mã | DP-07, DP-08 | Contract, kiểu dữ liệu, dữ liệu lớn và test đúng blueprint |
| CSV lỗi phải báo | DP-02, DP-08 | Các delimiter, encoding và trường hợp parser yêu cầu |
| fixture và đáp án rõ ràng | DP-04 | Fixture/oracle theo protocol 0.0.1 của nhóm |
| giả thuyết và phản chứng | AG-03, AG-06 | Suy luận ngữ nghĩa, hội thoại và evidence đầy đủ |
| chỉ lập repair plan | DP-16 | Contract, điều kiện áp dụng, quyền và kiểm soát thật |

Lab dùng Python thuần để dễ học. Blueprint dự kiến Polars và các thành phần khác;
không được coi lab là bản thay thế kiến trúc đã thống nhất. Chỉ nhận task với mentor
khi bạn giải thích được input, output và tiêu chí đạt của task đó.

## 13. Khi gặp lỗi

| Hiện tượng | Cách xử lý |
|---|---|
| No module named examples | Get-Location; chuyển về gốc D:\codex-skills-lab-20261021 |
| attempted relative import... | Chạy bằng -m examples.profile_data, không chạy trực tiếp file trong examples |
| Không thấy .venv trong danh sách | Python: Select Interpreter → Enter interpreter path… |
| Activate.ps1 bị chặn | Gọi .\.venv\Scripts\python.exe trực tiếp như hướng dẫn |
| $experiment bị lỗi trong terminal | Dán prompt này vào chat Codex |
| Skill không xuất hiện | Kiểm tra đúng folder dự án, SKILL.md và name; khởi động lại Codex nếu cần |
| Mã 001 hiện thành 1 trong Excel | Xem file raw bằng VS Code; bảng đọc tự đoán kiểu có thể hiển thị khác |
| CSV mở ra có dấu phẩy thay bảng | Bình thường: CSV là văn bản; dòng đầu là tên cột, dấu phẩy ngăn các cột |

Nguồn: https://github.com/hieupth/codeskills và hai trang OpenAI:
https://learn.chatgpt.com/docs/build-skills ;
https://learn.chatgpt.com/docs/agent-configuration/agents-md .
