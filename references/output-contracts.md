# Mẫu cấu trúc đầu ra

> Ở mọi chế độ, trước khi xuất phương án đầy đủ (kể cả chiến lược/phân cảnh đầy đủ của chế độ chuẩn), bản bàn giao cho designer hoặc báo cáo kiểm tra chính thức đều phải nạp tệp này. Sửa chữ cục bộ thì đọc theo nhu cầu; cuối bản giao phương án chính thức phải kèm mục 9 «Biên bản tự chấm», tư vấn đặt tên đơn thuần không cần kèm cả bộ điểm; thẻ thực thi một ảnh đầy đủ phải giữ nhiệm vụ, khung hình, nội dung, bố cục, Prompt, mục cấm và bằng chứng.

## 0. Mẫu bảng hỏi khởi động (tùy chọn, chỉ gửi một vòng)

Kiểm tên trước: tên sản phẩm gốc/tên ngành hàng dùng được đã có thì dùng tiếp; thiếu tên và chưa được phép đặt tên theo ảnh thì hỏi trước “Bạn cho mình tên sản phẩm, hoặc cho phép mình đặt tên theo ảnh nhé”. Có thể gộp vào vòng này, nhưng tên không phải mục tùy chọn, không trả lời không được coi là cho phép.

Các chiều sở thích bên dưới chỉ giữ nội dung **chưa có** trong tin nhắn và tài liệu, cái đã có thì xóa. Trong ngoặc là cách xử lý mặc định khi không trả lời.

```markdown
Trước khi bắt đầu, bạn có thể bổ sung các thông tin dưới đây, **tất cả đều tùy chọn**: trả lời càng đủ thì phương án càng sát; không muốn trả lời thì cứ nói “bỏ qua” hoặc “làm luôn”, mình sẽ xử lý theo mặc định trong ngoặc. Có thể chỉ trả lời số.

1. Nền tảng/thị trường: (mặc định: ảnh chính Shopee Việt Nam)
2. Phạm vi đầu ra: mấy ảnh chính? Có cần trang chi tiết không? (mặc định: khoảng 5 ảnh chính, mỗi ảnh có thẻ thực thi và Prompt tạo ảnh)
3. Khách hàng mục tiêu và bối cảnh dùng: (mặc định: suy từ tài liệu, đánh dấu là giả định)
4. 1–3 điểm bán muốn đẩy mạnh nhất, điểm nào có giấy phép/kiểm nghiệm/thông số hỗ trợ: (mặc định: rút từ tài liệu)
5. Phong cách và tông (như tối giản cao cấp, đời thường kiểu review, khuyến mãi thẳng thắn, phong cách Việt truyền thống, công nghệ; có ảnh tham chiếu càng tốt): (mặc định: theo thông lệ ngành hàng và nền tảng)
6. Định vị giá và khuyến mãi (có chương trình, quà tặng, combo không): (mặc định: không thể hiện giá và khuyến mãi)
7. Bắt buộc giữ hoặc cấm xuất hiện (màu thương hiệu, logo, cấu trúc, từ cấm dùng): (mặc định: lấy ảnh gốc sản phẩm làm chuẩn)
8. Chữ trên ảnh: ghép chữ hậu kỳ, hoàn toàn không thêm chữ, hay để mô hình tạo luôn tiêu đề ngắn? (mặc định: chừa khoảng trống, ghép chữ hậu kỳ)
9. Tài liệu khác: ảnh sản phẩm, ảnh bao bì, phân tích cơ hội/đối thủ, cẩm nang thương hiệu, gửi thẳng cho mình là được.
```

Người dùng trả lời xong thì không gửi bảng hỏi vòng hai. Điểm bán người dùng kể miệng ghi vào sổ bằng chứng là “người dùng kể”, không có bản gốc đi kèm thì vẫn là cần bổ sung bằng chứng.

## 1. Chiến lược hình ảnh và sổ bằng chứng

```markdown
# Chiến lược hình ảnh thương mại điện tử

## 1. Định nghĩa nhiệm vụ
- Nền tảng / thị trường:
- Tên sản phẩm/ngành hàng và nguồn đặt tên: tên sản phẩm gốc của người dùng / tên đặt theo ảnh được người dùng cho phép (không phải tên chính thức); thiếu tên thì hỏi trước
- Khách hàng mục tiêu:
- Đầu ra lần này:
- Chế độ thực thi: Chuẩn / Giao một lần / Kiểm tra / Bàn giao cho designer
- Cách render chữ: Chừa khoảng trống (mặc định) / Mô hình tạo chữ (ngoại lệ; phải được yêu cầu rõ và chữ rất ngắn)

## 2. Động lực chốt đơn
- Động lực chính (thị giác / nỗi đau / thông số / niềm tin / cảm xúc / giá-combo):
- Động lực phụ:
- Top 3 lý do mua:

## 3. Sổ bằng chứng
| Tuyên bố/điểm bán | Loại nguồn (chứng từ/lời nhà cung cấp/quan sát hình ảnh/phỏng đoán) và nguồn/số ảnh/URL | SKU/thị trường/điều kiện/ngày | Trạng thái | Xử lý cuối cùng |
|---|---|---|---|---|

## 4. Feature -> Advantage -> Benefit -> Evidence
| Feature | Advantage | Benefit | Evidence |
|---|---|---|---|

## 5. Campaign Style Lock
- Nhận diện sản phẩm:
- Bố cục:
- Màu sắc:
- Ánh sáng:
- Font chữ/mật độ thông tin:
- Render chữ/vùng khoảng trống:
- Nền/bối cảnh:
- Bắt buộc giữ:
- Được phép thay đổi:
- Mục cấm:

## 6. Giả định hiện tại và mục cần xác nhận
```

## 2. Storyboard

```markdown
# Kế hoạch ảnh / Storyboard

| Mã | Nhiệm vụ hình ảnh | Câu hỏi quyết định cần giải quyết | Điểm bán cốt lõi | Bố cục/điểm nhìn đầu | Bằng chứng | Rủi ro |
|---|---|---|---|---|---|---|
| KV1 | Hero | Đây là sản phẩm gì? | Tên sản phẩm/ngành hàng trước; điểm bán ở tầng hai, có thể lược | Toàn bộ sản phẩm và hình thái nhận diện | Tên gốc/ảnh gốc/SKU đã xác nhận | Chỉ có không khí hoặc đặc tính, thiếu từ chỉ sản phẩm |
| KV2 | Benefit | | | | | |
| KV3 | Proof | | | | | |
| KV4 | Scene | | | | | |
| KV5 | Spec/CTA | | | | | |
```

Số lượng điều chỉnh theo nền tảng và lượng thông tin thực tế, không cố định 5 ảnh.

## 3. Thẻ thực thi một ảnh

```markdown
### KV1 — [Tên nhiệm vụ]
- Tên sản phẩm gốc/tên đặt theo ảnh/ngành hàng đã xác nhận: ghi nguồn đặt tên; tên gốc phù hợp thì dùng thẳng, cần tên ngắn thì ghi quan hệ ánh xạ; chưa được phép thì không thay tên gốc
- Nhiệm vụ hình ảnh:
- Băn khoăn của người dùng mục tiêu lúc này:
- Khung hình:
- Điểm nhìn đầu tiên:
- Tự kiểm KV1 nhận diện (áp dụng cho ảnh đầu): khi được ghép chữ, bản thân tiêu đề chính nói rõ sản phẩm; che phụ đề vẫn nhận ra ngành hàng. Ảnh không chữ ghi căn cứ nhận diện chủ thể/bao bì gốc, ảnh thành phẩm chờ nghiệm thu; các ảnh đặc tính sau không cần lặp tên sản phẩm
- Chữ trên ảnh:
- Lớp chữ cuối cùng: gom toàn bộ chữ người tiêu dùng nhìn thấy, gồm nguồn trích dẫn, điều kiện và tuyên bố cần thiết; không trộn phân tích rủi ro
- Tự kiểm tuân thủ quảng cáo Việt Nam: khi thị trường Việt Nam áp dụng, liệt kê loại sản phẩm, căn cứ/giới hạn tuyên bố, nguồn/điều kiện hiển thị, thiếu rà soát thủ công hoặc xác nhận theo luật; Đạt / Chặn / Chờ rà soát thủ công
- Cách render chữ: Chừa khoảng trống (mặc định) / Mô hình tạo chữ (ngoại lệ, phải được yêu cầu rõ và chữ rất ngắn); bản giao thực tế chỉ chọn một
- Tự kiểm quy cách chữ: dùng bộ đếm tính số tiếng của tiêu đề và từng dòng phụ đề theo chuỗi cuối; ghi số dòng phụ đề, tối đa 1 nhãn số/bằng chứng và nguồn trong sổ
- Nghiệm thu chữ và dự phòng: chưa tạo ảnh thì ghi “render chữ chờ nghiệm thu”; khi được yêu cầu rõ để mô hình tạo chữ thì liệt kê chuỗi chính xác, vị trí, cỡ chữ và cách soát từng chữ, từng dấu, sai thì chuyển sang ghép chữ hậu kỳ
- Bố cục: vị trí khoảng trống, cỡ chữ tiêu đề/phụ đề/tuyên bố, tuyên bố ở đáy và điều kiện sát tuyên bố
- Ghi chú thiết kế:
- Prompt tạo ảnh (tự đủ nghĩa: cấu trúc/chất liệu/ánh sáng/bố cục/khoảng trống/mục cấm sản phẩm, sao chép riêng vẫn dùng được):
- Negative Prompt / mục cấm:
- Nguồn bằng chứng:
- Ghi chú tuân thủ/nền tảng:
```

## 4. Thẻ thực thi module trang chi tiết / PDP

```markdown
### M1 — [Tên module]
- Chức năng kể chuyện: nối tiếp / lợi ích / cơ chế / bằng chứng / bối cảnh / so sánh / FAQ / CTA
- Băn khoăn của người dùng:
- Khung hình:
- Chữ trên ảnh:
- Lớp chữ cuối cùng: gom toàn bộ chữ người tiêu dùng nhìn thấy, gồm nguồn trích dẫn, điều kiện và tuyên bố cần thiết; không trộn phân tích rủi ro
- Tự kiểm tuân thủ quảng cáo Việt Nam: khi thị trường Việt Nam áp dụng, liệt kê loại sản phẩm, căn cứ/giới hạn tuyên bố, nguồn/điều kiện hiển thị, thiếu rà soát thủ công hoặc xác nhận theo luật; Đạt / Chặn / Chờ rà soát thủ công
- Cách render chữ: Chừa khoảng trống (mặc định) / Mô hình tạo chữ (ngoại lệ, phải được yêu cầu rõ và chữ rất ngắn); bản giao thực tế chỉ chọn một
- Tự kiểm quy cách chữ: 1 tiêu đề + tối đa 3 ý; dùng bộ đếm tính số tiếng của tiêu đề và từng ý theo chuỗi cuối, đối chiếu nguồn số liệu, vượt giới hạn thì cắt bớt hoặc tách module
- Bố cục: vùng an toàn cho chữ, cỡ chữ, tuyên bố ở đáy; điều kiện quan trọng sát tuyên bố tương ứng
- Nghiệm thu chữ và dự phòng: mô hình tạo chữ phải soát từng chữ, từng dấu; chưa thấy ảnh thành phẩm thì đánh dấu chờ nghiệm thu, sai thì quay về dàn trang hậu kỳ
- Ghi chú thiết kế:
- Prompt tạo ảnh (tự đủ nghĩa: cấu trúc/chất liệu/ánh sáng/bố cục/khoảng trống/mục cấm sản phẩm, sao chép riêng vẫn dùng được):
- Negative Prompt / mục cấm:
- Nguồn bằng chứng:
```

## 5. Báo cáo kiểm tra/sửa bản

```markdown
# Kiểm tra hình ảnh và nội dung thương mại điện tử

## Kết luận
- Có điểm chặn cứng không: Có / Không
- Vấn đề chuyển đổi lớn nhất:
- Vấn đề tuân thủ/bằng chứng lớn nhất:
- Vấn đề hình ảnh lớn nhất:

## Danh sách vấn đề
| Ưu tiên | Vị trí | Vấn đề | Vì sao | Phương án sửa tối thiểu |
|---|---|---|---|---|

## Bản đã sửa
[Chỉ viết lại phần cần sửa; người dùng yêu cầu bản thay thế đầy đủ thì mới xuất toàn bộ]

## Tự kiểm tuân thủ quảng cáo Việt Nam (khi áp dụng)
| Cách nói gốc/vị trí | Căn cứ pháp luật hoặc chiến lược thận trọng | Thay thế an toàn/xóa | Nguồn và điều kiện hiển thị | Kết quả xử lý/chặn |
|---|---|---|---|---|

## Lớp chữ cuối cùng
[Gom đầy đủ chữ người tiêu dùng nhìn thấy sau khi sửa; nội dung cần bổ sung bằng chứng, chờ rà soát thủ công, chưa xong xác nhận theo luật không đưa vào]

## Cổng chất lượng năm chiều (ngưỡng 80 điểm, kèm căn cứ; định dạng đầy đủ xem mục 9)
- Bằng chứng và tuân thủ: __ điểm｜Căn cứ:
- Logic chuyển đổi: __ điểm｜Căn cứ:
- Thứ bậc thị giác: __ điểm｜Căn cứ:
- Tính nhất quán: __ điểm｜Căn cứ:
- Tính thực thi: __ điểm｜Căn cứ:
```

## 6. Bàn giao bản địa hóa xuyên biên giới

```markdown
## Ghi chú bản địa hóa
- Điểm bán gốc:
- Hiểu biết về thị trường mục tiêu:
- Sự thật được giữ:
- Lý do mua sau khi viết lại:
- Bản địa hóa đơn vị/quy cách:
- Điều chỉnh bối cảnh văn hóa:
- Mục tuân thủ chờ kiểm tra:

## Chữ trên ảnh tiếng Anh/ngôn ngữ địa phương
- Headline:
- Support: ảnh chính tối đa 2 dòng; module PDP tối đa 3 ý; tự kiểm theo giới hạn số từ tương ứng
- Evidence note: nguồn và điều kiện áp dụng tách riêng; không ép nhét vào nội dung tiếp thị
```

Thẻ một ảnh và module chi tiết đều theo giá trị khuyến nghị mặc định và chuẩn cỡ chữ trên điện thoại trong `SKILL.md`; đây là khuyến nghị bố cục nội bộ, không phải quy định nền tảng, tuyên bố cần thiết không được giấu bằng cách thu nhỏ chữ. Mỗi thẻ phải chọn một trong hai cách render chữ và giao tự kiểm quy cách chữ; mô hình tạo chữ mặc định chỉ một tiêu đề ≤6 tiếng hoặc ≤6 từ tiếng Anh, dài hơn thì giao chừa khoảng trống. Thẻ có giá kèm thêm đơn vị tiền tệ, SKU/số lượng, ngưỡng ưu đãi, thời hạn, phí vận chuyển và nguồn; thiếu điều kiện thì không viết thành giá cuối vô điều kiện. Mục thiếu xóa hẳn khỏi trường nội dung, ghi vào danh sách cần xác nhận ngoài bản, không giữ placeholder trong chữ trên ảnh hay trường nội dung của thẻ thực thi.

## 7. Chấm điểm định lượng (chỉ khi người dùng yêu cầu rõ)

Chỉ dùng mục này khi người dùng yêu cầu rõ điểm định lượng để trình bày bên ngoài: dùng thang 1–5, không cho 80/100 không có mốc. Tự chấm nội bộ trước khi giao dùng ngưỡng 80 điểm ở mục 9, lấy điều kiện bắt buộc làm mốc, khác với mục này.

Ý nghĩa thang 1–5:

- **1**: có vấn đề nghiêm trọng, không được giao.
- **2**: logic chính không đứng vững, cần làm lại.
- **3**: cơ bản dùng được, nhưng có thiếu sót rõ.
- **4**: thực thi được ngay, chỉ còn chỗ tối ưu cục bộ.
- **5**: bằng chứng, chuyển đổi, hình ảnh, tính nhất quán và chi tiết thực thi đều đầy đủ.

Mỗi điểm phải kèm căn cứ cụ thể.

## 8. Quét trạng thái cuối trước khi giao

Trước khi giao phương án đầy đủ hoặc lớp chữ cuối cùng, soát từng mục:

- [ ] Nội dung thành phẩm không còn “cần bổ sung”, “cần xác nhận”, “cần kiểm tra”, “(chưa cung cấp xx)” và giọng khuyến nghị nội bộ; mục thiếu đã xóa cả dòng. Có công cụ thực thi thì chạy `python scripts/scan-final-copy.py "Nội dung 1" "Nội dung 2"`.
- [ ] Thông tin làm rõ (như “sản phẩm gồm một sợi”, “phụ kiện trong ảnh không kèm theo”) nằm ở vùng quy cách hoặc vùng chú thích đọc được, không chiếm vị trí điểm bán; điều kiện ảnh hưởng đến hiểu biết về hàng nhận được/giá vẫn sát hình hoặc tuyên bố liên quan.
- [ ] Cách nói về kỹ thuật, chất liệu, tính năng chỉ lấy từ tài liệu và đã đối chiếu ảnh sản phẩm; chỗ mâu thuẫn với hàng thật đã hỏi lại.
- [ ] Mỗi Prompt tạo ảnh không phụ thuộc thẻ khác; cần ảnh sản phẩm gốc thì đã ghi rõ số ảnh/yêu cầu tư liệu, kèm ảnh chỉ định là bàn giao độc lập được, và đã lặp lại Style Lock cùng mục cấm.
- [ ] Nội dung đã qua «Tự kiểm chất lượng nội dung», con số có đối chiếu hoặc cảm nhận, nội dung độ phù hợp có kết luận.

## 9. Biên bản tự chấm (bắt buộc kèm bản giao phương án chính thức)

Đặt đoạn này sau bản cuối; thiếu coi như chưa tự chấm. Điểm lấy điều kiện bắt buộc ở Bước 6 của `SKILL.md` làm mốc: thiếu bất kỳ điều kiện bắt buộc nào thì chiều đó tối đa 79, phải viết lại, tối đa 2 vòng.

```markdown
### Biên bản tự chấm
| Chiều | Điểm | Căn cứ (một câu, ghi rõ đã thỏa điều kiện bắt buộc nào) | Đã viết lại gì |
|---|---|---|---|
| Bằng chứng và tuân thủ |  |  |  |
| Logic chuyển đổi |  |  |  |
| Thứ bậc thị giác |  |  |  |
| Tính nhất quán |  |  |  |
| Tính thực thi |  |  |  |
- Kiểm tra cơ học: scan-final-copy đạt / count-copy đã đối chiếu / không có công cụ thực thi, chưa chạy
- Số vòng viết lại: 0 / 1 / 2
- Mục chưa đạt: không (hoặc ghi rõ chiều, lý do, tài liệu cần có)
```

Chế độ chuẩn giao theo giai đoạn thì mỗi giai đoạn kèm một biên bản; chiều không áp dụng ở giai đoạn đó ghi “không áp dụng ở giai đoạn này” và nêu lý do. Sau 2 vòng vẫn dưới 80 thì giao phần đã đạt, ghi mục chưa đạt ngoài bản, không đánh dấu là bản cuối.
