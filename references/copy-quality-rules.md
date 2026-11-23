# Quy tắc chất lượng nội dung (chi tiết và ví dụ đúng/sai)


## Mức ưu tiên

| Tầng | Quy tắc | Hậu quả khi vi phạm |
|---|---|---|
| Điểm chặn | Giao là trạng thái cuối; không viết suy luận thành sự thật; Prompt tự đủ nghĩa | Không được giao, sửa trước |
| Chất lượng | Liên quan gì đến tôi, thông tin gia tăng, con số có cảm nhận, ngôn ngữ người tiêu dùng, ba cửa hỏi–đáp, đặt đúng chỗ các làm rõ | Nội dung nhạt nhưng dùng được, nên sửa trước khi giao |
| Tiền đề | Xếp thông tin theo thứ tự ra quyết định; rút tài liệu tham chiếu thành ràng buộc cứng | Hoàn thành trước khi viết |
| Công tắc theo bối cảnh | Phần bổ sung ngành hàng tương ứng trong `references/category-notes.md` | Chỉ bật khi đúng ngành hàng |

## Điểm chặn

### 1. Giao là trạng thái cuối

Nội dung thành phẩm sẽ đi thẳng vào tạo ảnh, dàn trang, đăng bán. Trước khi giao, quét “cần bổ sung”, “cần xác nhận”, “cần kiểm tra”, “(chưa cung cấp xx)” và giọng khuyến nghị nội bộ; mục thiếu **xóa cả dòng**, không để chú thích trống. Sự thật đã xác nhận như số lượng sản phẩm có thể vào vùng quy cách/chú thích đọc được, nhưng không in ghi chú cần xác nhận nội bộ lên ảnh.

- Sai: nhãn số «Tải trọng (cần bổ sung)».
- Đúng: xóa cả nhãn số; tài liệu thiếu ghi vào danh sách cần xác nhận ngoài bản.

### 2. Không viết suy luận thành sự thật

Nguồn chia bốn loại: chứng từ, lời nhà cung cấp, quan sát hình ảnh, phỏng đoán. Chỉ chứng từ và lời nhà cung cấp đã kiểm chéo mới vào thành phẩm; quan sát hình ảnh và phỏng đoán chỉ ghi chú ngoài bản. Mâu thuẫn với hàng thật thì theo hàng thật và hỏi lại.

Tuyên bố sự thật tuân theo ranh giới bằng chứng trên; tên đặt theo ảnh được người dùng cho phép vẫn làm theo Bước 0 của `SKILL.md`, tên không chứng minh chất liệu, kỹ thuật hay tính năng, nội bộ giữ nguồn đặt tên.

- Sai: tài liệu chỉ ghi “inox”, nhìn vân đánh bóng trên ảnh liền viết “công nghệ xước gương”.
- Sai: người bán ghi “đúc nguyên khối”, ảnh rõ ràng có mối ghép vẫn chép lại.
- Đúng: chỉ viết theo tài liệu “inox”; mâu thuẫn thì hỏi lại người bán, ghi ngoài bản là cần xác nhận.

### 3. Prompt tự đủ nghĩa

Khâu sau mặc định là mô hình tạo ảnh AI. Mỗi Prompt sao chép riêng sang một phiên mới cũng phải tạo được ảnh.

- Sai: “Phong cách như ảnh trên, đổi sang góc nhìn từ trên xuống.”
- Đúng: viết đủ cấu trúc sản phẩm (số bộ phận, hình dạng, tỷ lệ), chất liệu và bề mặt, hướng và độ cứng/mềm của ánh sáng, bố cục và tỷ lệ sản phẩm, vị trí khoảng trống, nền, mục cấm (không thêm phụ kiện, không đổi cấu trúc, không có chữ), và lặp lại Style Lock.
- Style Lock của cùng một bộ ảnh viết lại trong từng Prompt, không viết “như trên”.

## Chất lượng

### 4. Giọng điểm bán, không phải giọng hướng dẫn sử dụng

Tên sản phẩm ở ảnh đầu phải hoàn thành nhận diện trước, không xóa vì thiếu giọng tiếp thị; các câu tiếp thị khác hỏi từng câu “câu này có làm người dùng muốn mua hơn không”. Câu giải thích sản phẩm được cấu tạo thế nào thì hoặc đổi thành “vì sao đáng mua”, hoặc xóa.

- Sai: «Ba tầng kệ, chỉnh được độ cao» (nói cấu tạo).
- Đúng: «Chỉnh độ cao kệ, đồ to nhỏ đều xếp gọn» (nói người dùng được gì; với điều kiện tài liệu xác nhận kệ chỉnh được).

### 5. Thông tin gia tăng, không lặp lại hình

Tên/ngành hàng ở ảnh đầu và quy cách, điều kiện cần thiết là ngoại lệ; thông tin khác không lặp lại máy móc điều hình đã thể hiện. Chữ bổ sung điều hình không nói được: chuyển động, dịp dùng, cảm giác chạm, quy cách, cách phối.

- Sai: ảnh đã thấy rõ ba ngăn, chữ lại viết «Ba ngăn lưu trữ»; tiêu đề và phụ đề nói cùng một ý.
- Đúng: phụ đề viết dịp dùng hoặc thông tin quy cách (với điều kiện tài liệu hỗ trợ).

### 6. Con số có cảm nhận, độ phù hợp có kết luận

Con số dùng để nhận diện quy cách trong tên KV1 được giữ; tiêu đề tiếp thị khác tránh chỉ liệt kê thông số. Con số phải đi kèm vị trí, cảm nhận cơ thể hoặc vật đối chiếu; nội dung độ phù hợp đưa ra mức, kết luận và hệ quả. Cảm nhận và ngưỡng chỉ dùng số liệu đã có trong tài liệu, không có thì hỏi lại.

- Sai: tiêu đề chỉ ghi «500ml» và coi đó là lý do mua. Đúng: dung tích chính xác đặt ở vùng quy cách; có ảnh đối chiếu dung tích đã kiểm thì mới thêm so sánh trực quan, không có thì giữ thông số chính xác, không bịa dung tích “chai tiêu chuẩn” hay cảm nhận.
- Sai: «Chọn size theo chiều cao của bạn». Đúng: viết theo bảng size trong tài liệu thành các mức, ví dụ “cao dưới 160cm chọn S”; tài liệu không có bảng size thì hỏi lại, không tự đặt ngưỡng.

### 7. Ngôn ngữ người tiêu dùng

Thuật ngữ chỉ xuất hiện ở vùng quy cách, vùng quảng cáo chuyển thành cách nói thường ngày.

- Sai: «Điểm nhấn thị giác, thứ bậc thông tin rõ ràng».
- Đúng: «Nhìn là thấy ngay điểm chính».

### 8. Câu đầy đủ, đọc trôi

Viết xong đọc to một lượt; thà bỏ một ý chứ không để câu cụt.

- Sai: «Dính nước mồ hôi lau cất kịp».
- Đúng: «Khi dính nước hoặc mồ hôi, lau khô rồi cất ngay».

### 9. Ba cửa cho hỏi–đáp

Mỗi câu hỏi FAQ phải qua cả ba cửa:

- Có căn cứ để trả lời. Sai: hỏi «Có bị phai màu không?» đáp «Không cam kết không phai màu». Không trả lời được thì không đặt câu đó.
- Đưa phán đoán rõ ràng. Sai: «Tùy cơ địa mỗi người». Đúng: đưa ngưỡng theo mức và hệ quả khi chọn sai.
- Chỉ trả lời băn khoăn có thật của người mua sản phẩm này. Sai: sản phẩm không có nắp lại hỏi «Nắp có bị rò không».

### 10. Đặt đúng chỗ các làm rõ

Làm rõ về bộ, cách phối, quy cách đặt ở bảng quy cách hoặc vùng chú thích đọc được, không chiếm vị trí điểm bán; điều kiện ảnh hưởng đến hiểu biết về hàng nhận được hoặc giá vẫn phải sát hình/tuyên bố liên quan, không giấu trong chữ nhỏ. Trong ảnh phối đồ, đồ phối không thuộc sản phẩm phải ghi “không kèm theo”.

- Sai: vùng điểm bán ghi «Sản phẩm gồm một sợi».
- Đúng: bảng quy cách ghi “Số lượng: 1 sợi”; chữ nhỏ dưới ảnh phối ghi “Trang sức/phụ kiện khác trong ảnh không kèm theo”.

## Tiền đề

### 11. Xếp thông tin theo thứ tự ra quyết định

Là gì → liên quan gì đến tôi → vì sao chọn nó → dựa vào đâu để tin → mua thế nào. Ảnh đầu cho người xem biết ngay ngành hàng, câu hình ảnh đặt ở phụ đề; mỗi module trang chi tiết chỉ giải quyết một câu hỏi quyết định.

- Sai: tiêu đề ảnh đầu nói cấu trúc sản phẩm chia ra sao, người dùng không biết đây là ngành hàng gì.
- Đúng: tiêu đề ảnh đầu dùng tên đã xác nhận hoặc tên đặt theo ảnh được cho phép, rõ ngành hàng; điểm bán ở tầng hai và có thể lược, chi tiết cấu trúc để các ảnh sau.

### 12. Rút tài liệu tham chiếu thành ràng buộc cứng trước

Khi người dùng đưa phân tích cơ hội, tham chiếu đối thủ, tài liệu thương hiệu, hãy liệt kê 3–5 ràng buộc cứng trước khi viết.

| Mục rút ra | Ví dụ cách viết |
|---|---|
| Khách hàng mục tiêu | Nhóm người và dịp dùng mà tài liệu chỉ ra |
| Khác biệt bắt buộc nhấn mạnh | Điểm khác biệt đã được kiểm chứng trong tài liệu |
| Cách làm bắt buộc tránh | Sai lầm hoặc giới hạn nền tảng mà tài liệu chỉ ra |
| Cấu trúc có thể học | Mẫu câu, thứ bậc thông tin, phân vai module |

Học cấu trúc, không học lớp vỏ; không chuyển sự thật, số liệu, cam kết và yếu tố thương hiệu của người khác sang.

Màu thương hiệu riêng của người dùng hoặc tham chiếu hình ảnh được cho phép giữ rõ ràng thì làm theo Reference Fidelity, không bị quy tắc này xóa.

## Ba câu hỏi trước khi giao

1. Thành phẩm còn placeholder hoặc ghi chú nội bộ không?
2. Mỗi cách nói về kỹ thuật, chất liệu, tính năng có trong tài liệu không, có khớp hàng thật không?
3. Mỗi Prompt sao chép riêng ra ngoài có tạo được ảnh không?
