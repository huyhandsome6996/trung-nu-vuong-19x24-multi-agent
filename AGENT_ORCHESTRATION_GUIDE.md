# Sáu vai trò trên một main

Quy trình hiện hành: [START_HERE](START_HERE.md) → [WORKFLOW_A_TO_Z](10_agent_workflow/WORKFLOW_A_TO_Z.md). Chỉ dùng main. Sáu vai trò mô tả chuyên môn; một agent có thể lần lượt đảm nhiệm cả sáu.

| Vai trò | Nhiệm vụ | Đọc chính |
| --- | --- | --- |
| AGENT-01 Tư liệu | Đọc scan, đối chiếu nguồn, ghi ngoại lệ | 01/07 và SOURCE_DECISIONS |
| AGENT-02 Chuyển thể | Giọng văn 13–16 tuổi, tính hợp lý và căn cứ | 02/03 |
| AGENT-03 Kịch bản | Khóa lời dẫn, thoại, từ khóa và template | 03 và task TEXT |
| AGENT-04 Mỹ thuật | Dùng sheet active, soạn prompt, sinh ảnh, kiểm đồng nhất | 04/09 và task ART |
| AGENT-05 Chế bản | Ghép chữ Việt, bìa, safe/bleed và PDF | 05, task LAYOUT/ASSEMBLY |
| AGENT-06 QA | Kiểm nguồn, mỹ thuật, ngôn ngữ, chế bản và bàn giao | 06, task QA/RELEASE |

Không tự spawn nhiều agent khi chủ dự án chỉ giao tiếp quản thông thường. Main-only dùng một người ghi tại một thời điểm; cộng tác nếu được giao phải có phạm vi và sync rõ.

Chu trình: nhận task → mở brief/ảnh → làm → kiểm → checkpoint → commit/push main → task tiếp. Thay asset phải có v002, giữ bằng chứng v001. Thiếu công cụ hoặc dữ liệu thì block đúng bước và tiếp tục phần độc lập.

[Phục hồi sau ngắt phiên](10_agent_workflow/RECOVERY_AND_MAIN.md) · [Lệnh và báo cáo](10_agent_workflow/COMMANDS.md)
