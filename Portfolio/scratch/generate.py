import re

new_data = """const projectData = {
  1: {
    badge: "Bài tập 1 / Mục 1.4",
    title: "Thao tác cơ bản với tập tin và thư mục",
    meta: {
      date: "Tháng 02, 2026",
      status: "Thực hành hệ điều hành",
      tools: "Windows File Explorer",
      instructor: "Đội ngũ Giảng viên UET"
    },
    goal: "Làm quen với các thao tác cơ bản trên hệ điều hành Windows như tạo, đổi tên, sao chép, di chuyển và xóa tệp tin/thư mục.",
    process: \`
      <ol style="margin-left: 20px; display: flex; flex-direction: column; gap: 12px; font-size: 13px;">
        <li><strong>Mở File Explorer:</strong> Nhấn tổ hợp phím Windows + E hoặc nhấp vào biểu tượng thư mục màu vàng trên thanh tác vụ.<br><img src="assets/images/Bài 1/1.1.png" style="max-width: 100%; border-radius: 4px; margin-top: 8px;"></li>
        <li><strong>Truy cập ổ đĩa/thư mục:</strong> Ở cột bên trái, nhấp vào This PC, sau đó nhấp đúp vào một ổ đĩa không phải ổ hệ thống (ví dụ: ổ D: hoặc E:). Nếu chỉ có ổ C:, hãy vào thư mục Documents.<br><img src="assets/images/Bài 1/1.2.png" style="max-width: 100%; border-radius: 4px; margin-top: 8px;"></li>
        <li><strong>Tạo thư mục mới:</strong> Nhấp chuột phải vào một khoảng trống -> chọn New -> Folder. Đặt tên thư mục là ThucHanh_TrangGiangLong. Nhấn Enter.<br><img src="assets/images/Bài 1/1.3.png" style="max-width: 100%; border-radius: 4px; margin-top: 8px;"></li>
        <li><strong>Vào thư mục vừa tạo:</strong> Nhấp đúp vào thư mục ThucHanh_TrangGiangLong.<br><img src="assets/images/Bài 1/1.4.png" style="max-width: 100%; border-radius: 4px; margin-top: 8px;"></li>
        <li><strong>Tạo tệp tin văn bản:</strong> Nhấp chuột phải vào khoảng trống -> New -> Text Document. Đặt tên là GhiChu.txt. Nhấn Enter.<br><img src="assets/images/Bài 1/1.5.png" style="max-width: 100%; border-radius: 4px; margin-top: 8px;"></li>
        <li><strong>Đổi tên tệp tin:</strong> Nhấp chuột phải vào tệp GhiChu.txt -> chọn Rename. Đổi tên thành GhiChuQuanTrong.txt. Nhấn Enter.<br><img src="assets/images/Bài 1/1.6.png" style="max-width: 100%; border-radius: 4px; margin-top: 8px;"></li>
        <li><strong>Tạo thư mục con:</strong> Trong thư mục ThucHanh_TrangGiangLong, nhấp chuột phải -> New -> Folder. Đặt tên là TaiLieu.<br><img src="assets/images/Bài 1/1.7.png" style="max-width: 100%; border-radius: 4px; margin-top: 8px;"></li>
        <li><strong>Sao chép tệp tin (Copy & Paste):</strong> Nhấp chuột phải vào tệp GhiChuQuanTrong.txt -> chọn Copy. Nhấp đúp vào thư mục TaiLieu, nhấp chuột phải vào khoảng trống bên trong -> chọn Paste.<br><img src="assets/images/Bài 1/1.8.png" style="max-width: 100%; border-radius: 4px; margin-top: 8px;"></li>
        <li><strong>Di chuyển tệp tin (Cut & Paste):</strong> Quay lại thư mục ThucHanh_TrangGiangLong. Tạo một tệp mới tên là DiChuyen.txt. Nhấp chuột phải vào tệp DiChuyen.txt -> chọn Cut. Nhấp đúp vào thư mục TaiLieu, nhấp chuột phải vào khoảng trống -> chọn Paste. Tệp gốc đã biến mất khỏi vị trí cũ.<br><img src="assets/images/Bài 1/1.9.png" style="max-width: 100%; border-radius: 4px; margin-top: 8px;"></li>
        <li><strong>Xóa tệp tin:</strong> Trong thư mục TaiLieu, nhấp chuột phải vào tệp GhiChuQuanTrong.txt -> chọn Delete. Tệp sẽ được chuyển vào Thùng rác (Recycle Bin).<br><img src="assets/images/Bài 1/1.10.png" style="max-width: 100%; border-radius: 4px; margin-top: 8px;"></li>
        <li><strong>Xóa vĩnh viễn:</strong> Chọn tệp DiChuyen.txt, nhấn giữ phím Shift và nhấn phím Delete. Một cảnh báo sẽ hiện ra. Nếu đồng ý, tệp sẽ bị xóa vĩnh viễn mà không qua Thùng rác.<br><img src="assets/images/Bài 1/1.11.png" style="max-width: 100%; border-radius: 4px; margin-top: 8px;"></li>
        <li><strong>Khôi phục từ Thùng rác (Tùy chọn):</strong> Tìm biểu tượng Recycle Bin trên màn hình nền, nhấp đúp để mở. Tìm tệp GhiChuQuanTrong.txt đã xóa, nhấp chuột phải vào nó và chọn Restore. Tệp sẽ quay trở lại vị trí ban đầu.<br><img src="assets/images/Bài 1/1.12.png" style="max-width: 100%; border-radius: 4px; margin-top: 8px;"></li>
      </ol>
    \`,
    output: \`
      <div style="padding: 16px; background-color: rgba(255,255,255,0.02); border-radius: 8px; border: 1px solid rgba(255,255,255,0.05);">
        <p style="font-size: 13px; color: var(--text-muted);">Thông qua bài thực hành này, tôi đã nắm vững các thao tác cơ bản nhất của hệ điều hành Windows, giúp việc quản lý và lưu trữ tệp tin trên máy tính trở nên có tổ chức và hiệu quả hơn.</p>
      </div>
    \`
  },
  2: {
    badge: "Bài tập 2 / Mục 2.4",
    title: "Tìm kiếm và đánh giá thông tin học thuật",
    meta: {
      date: "Tháng 03, 2026",
      status: "Đánh giá 10 tài liệu",
      tools: "Google Scholar, IEEE, arXiv",
      instructor: "Đội ngũ Giảng viên UET"
    },
    goal: "Thực hành quá trình tìm kiếm thông tin chuyên sâu và đánh giá khắt khe độ tin cậy của các nguồn tài liệu học thuật theo chủ đề chuyên ngành Trí tuệ nhân tạo.",
    process: \`
      <div style="font-size: 13px; display: flex; flex-direction: column; gap: 12px;">
        <p><strong>I. GIỚI THIỆU CHỦ ĐỀ NGHIÊN CỨU</strong><br>
        <strong>1. Tên chủ đề:</strong> Đánh giá hiệu năng của các thuật toán tìm kiếm heuristic và cấu trúc dữ liệu đồ thị trong bài toán tối ưu hóa đường đi.<br>
        <strong>2. Sự liên quan đến ngành học:</strong> Chủ đề này liên quan mật thiết đến các học phần cốt lõi của ngành Khoa học Máy tính, đặc biệt là Cấu trúc dữ liệu và Giải thuật cùng với Cơ sở Trí tuệ Nhân tạo (AI). Việc tìm ra con đường ngắn nhất và tối ưu nhất là bài toán kinh điển, có tính ứng dụng cao trong lập trình hệ thống, phát triển game, robot định vị và bản đồ số.</p>
        
        <p><strong>II. QUÁ TRÌNH TÌM KIẾM THÔNG TIN</strong></p>
        <ol style="margin-left: 20px;">
          <li><strong>Xác định từ khóa (Keywords):</strong> "Pathfinding algorithms", "A* algorithm performance", "Dijkstra vs A* comparison", "Graph data structures memory optimization", "Heuristic search".</li>
          <li><strong>Lựa chọn nguồn tìm kiếm:</strong>
            <ul style="margin-top: 4px;">
              <li>Cơ sở dữ liệu học thuật: Google Scholar, IEEE Xplore, và ResearchGate để tìm các bài báo hội nghị và tạp chí chuyên ngành.</li>
              <li>Sách chuyên khảo: Tìm kiếm sách giáo trình chuẩn quốc tế về thuật toán và AI thông qua thư viện trường và các nền tảng sách giáo dục (Elsevier, Springer).</li>
              <li>Nguồn mở trên Internet: Sử dụng các trang blog công nghệ và cơ sở dữ liệu mở của các trường đại học (Stanford) để xem các ví dụ triển khai mã nguồn thực tế.</li>
            </ul>
          </li>
        </ol>

        <p><strong>III. TIÊU CHÍ ĐÁNH GIÁ ĐỘ TIN CẬY</strong></p>
        <ol style="margin-left: 20px;">
          <li><strong>Tác giả (Author):</strong> Chuyên môn, học hàm, học vị và tổ chức/trường đại học trực thuộc.</li>
          <li><strong>Cơ quan xuất bản (Publisher):</strong> Uy tín của tạp chí, nhà xuất bản (ví dụ: MIT Press, IEEE, Pearson là uy tín cao).</li>
          <li><strong>Phương pháp nghiên cứu (Methodology):</strong> Sự rõ ràng trong cách thiết kế thí nghiệm, thuật toán có được minh chứng bằng toán học hoặc dữ liệu thực nghiệm hay không.</li>
          <li><strong>Trích dẫn (Citations):</strong> Số lượng trích dẫn trên Google Scholar phản ánh mức độ ảnh hưởng và sự công nhận của cộng đồng khoa học.</li>
          <li><strong>Tính cập nhật (Recency):</strong> Năm xuất bản của tài liệu.</li>
        </ol>
      </div>
    \`,
    output: \`
      <div>
        <p style="margin-bottom: 12px; font-weight: bold;">IV. BẢNG TỔNG HỢP VÀ ĐÁNH GIÁ NGUỒN THÔNG TIN (Trích xuất)</p>
        <div style="overflow-x: auto;">
          <table class="prompt-comparison-table" style="font-size: 11px; width: 100%;">
            <thead>
              <tr>
                <th>STT</th>
                <th>Tên tài liệu (Rút gọn)</th>
                <th>Phân loại</th>
                <th>Tác giả & Cơ quan XB</th>
                <th>Tính cập nhật</th>
                <th>Xếp hạng Độ tin cậy</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>1</td>
                <td>A survey of shortest-path algorithms...</td>
                <td>Bài báo khoa học</td>
                <td>Madkour et al. / arXiv (Cornell University)</td>
                <td>2017 (Khá mới)</td>
                <td><strong style="color:var(--accent-green)">Cao</strong></td>
              </tr>
              <tr>
                <td>3</td>
                <td>Finding shortest paths on real road networks...</td>
                <td>Bài báo khoa học</td>
                <td>Zeng & Church / Int. Journal of GIS</td>
                <td>2009 (Hơi cũ)</td>
                <td><strong style="color:var(--accent-green)">Cao</strong></td>
              </tr>
              <tr>
                <td>6</td>
                <td>Introduction to Algorithms (4th ed.)</td>
                <td>Sách chuyên khảo</td>
                <td>Cormen et al. / MIT Press</td>
                <td>2022 (Rất mới)</td>
                <td><strong style="color:var(--accent-cyan)">Rất Cao</strong></td>
              </tr>
              <tr>
                <td>7</td>
                <td>Artificial Intelligence: A Modern Approach</td>
                <td>Sách chuyên khảo</td>
                <td>Russell & Norvig / Pearson</td>
                <td>2021 (Rất mới)</td>
                <td><strong style="color:var(--accent-cyan)">Rất Cao</strong></td>
              </tr>
              <tr>
                <td>10</td>
                <td>Dijkstra’s shortest path algorithm</td>
                <td>Nguồn mở (Web)</td>
                <td>GeeksforGeeks</td>
                <td>2023 (Mới)</td>
                <td><strong style="color:#ffbd2e">Trung bình</strong></td>
              </tr>
            </tbody>
          </table>
        </div>
        <p style="margin-top: 16px; font-size: 13px;"><strong>V. KẾT LUẬN</strong><br>
        Quá trình thực hiện bài tập đã giúp hình thành phương pháp luận rõ ràng trong việc tra cứu và phân loại tài liệu chuyên ngành Trí tuệ nhân tạo. Việc phân định được sự khác biệt giữa tài liệu lý thuyết nền tảng (như các sách của MIT Press hay bài báo từ IEEE) với các tài liệu ứng dụng thực hành (như Github, GeeksforGeeks) là kỹ năng cốt lõi. Trong quá trình học tập và làm đồ án thực tế, các thuật toán (C++, Python) cần được tham khảo từ giáo trình để đảm bảo tính đúng đắn toán học, sau đó mới tham khảo các nguồn mở để tối ưu hóa thời gian lập trình.</p>
      </div>
    \`
  },
  3: {
    badge: "Bài tập 3 / Mục 3.4",
    title: "Kỹ năng viết Prompt hiệu quả trong học tập",
    meta: {
      date: "Tháng 04, 2026",
      status: "Thử nghiệm Prompt",
      tools: "ChatGPT, Gemini",
      instructor: "Đội ngũ Giảng viên UET"
    },
    goal: "Thử nghiệm và phân tích cấu trúc của các phiên bản Prompt khác nhau (Cơ bản, Cải tiến, Nâng cao) để nhận thấy sự thay đổi rõ rệt trong chất lượng phản hồi của AI.",
    process: \`
      <div style="font-size: 13px; display: flex; flex-direction: column; gap: 16px;">
        <div>
          <strong style="color:var(--accent-cyan)">Tác vụ 1: Tóm tắt một bài đọc/tài liệu học thuật (Chủ đề: Quy trình CRISP-DM)</strong>
          <ul style="margin-left: 20px; margin-top: 8px; display: flex; flex-direction: column; gap: 8px;">
            <li><strong>Prompt cơ bản:</strong> Tóm tắt về quy trình CRISP-DM.</li>
            <li><strong>Prompt cải tiến:</strong> Hãy tóm tắt 6 giai đoạn của quy trình CRISP-DM. Trình bày nội dung dưới dạng gạch đầu dòng, nêu rõ tên từng giai đoạn và ý nghĩa chính của nó để dễ học thuộc.</li>
            <li><strong>Prompt nâng cao (Role prompting, Contextual):</strong> Đóng vai là một chuyên gia Khoa học Dữ liệu. Hãy tóm tắt quy trình CRISP-DM cho một sinh viên đại học năm nhất. Cấu trúc bài tóm tắt bao gồm: (1) Khái niệm ngắn gọn về CRISP-DM, (2) Giải thích chi tiết 6 giai đoạn (mỗi giai đoạn kèm theo một ví dụ thực tế ngắn gọn ứng dụng trong ngành bán lẻ), và (3) Giải thích tại sao quy trình này mang tính lặp lại (iterative).</li>
          </ul>
        </div>
        <div>
          <strong style="color:var(--accent-cyan)">Tác vụ 2: Giải thích một khái niệm phức tạp (Chủ đề: Trị riêng và Vectơ riêng)</strong>
          <ul style="margin-left: 20px; margin-top: 8px; display: flex; flex-direction: column; gap: 8px;">
            <li><strong>Prompt cơ bản:</strong> Giải thích khái niệm Trị riêng và Vectơ riêng.</li>
            <li><strong>Prompt cải tiến:</strong> Trị riêng (eigenvalue) và vectơ riêng (eigenvector) trong Đại số tuyến tính là gì? Hãy giải thích ý nghĩa hình học của chúng thay vì chỉ đưa ra công thức, và cho một ví dụ minh họa đơn giản trên ma trận 2x2.</li>
            <li><strong>Prompt nâng cao (Role prompting, Chain-of-thought):</strong> Hãy đóng vai một giảng viên Toán đại cương. Sinh viên của bạn đang gặp khó khăn khi hình dung về Trị riêng và Vectơ riêng. Hãy giải thích khái niệm này từng bước một: Đầu tiên, sử dụng một phép ẩn dụ trực quan trong đời sống (ví dụ: kéo dãn một tấm bạt cao su). Sau đó, giải thích bản chất hình học của phương trình $Ax = \\lambda x$. Cuối cùng, nêu một ứng dụng thực tế của chúng trong Khoa học máy tính để sinh viên thấy được tầm quan trọng của bài học.</li>
          </ul>
        </div>
        <div>
          <strong style="color:var(--accent-cyan)">Tác vụ 3: Tạo bộ câu hỏi ôn tập (Chủ đề: Lập trình OOP với C++)</strong>
          <ul style="margin-left: 20px; margin-top: 8px; display: flex; flex-direction: column; gap: 8px;">
            <li><strong>Prompt cơ bản:</strong> Tạo câu hỏi ôn tập về OOP.</li>
            <li><strong>Prompt cải tiến:</strong> Tạo một bộ gồm 5 câu hỏi trắc nghiệm và 2 câu hỏi tự luận để ôn tập 4 tính chất cơ bản của Lập trình hướng đối tượng (OOP) trong C++. Vui lòng cung cấp đáp án chi tiết ở cuối.</li>
            <li><strong>Prompt nâng cao (Role prompting, Few-shot examples):</strong> Đóng vai là một người phỏng vấn kỹ thuật đánh giá ứng viên thực tập sinh C++. Hãy tạo một bài test ôn tập về OOP. Bài test cần: 3 câu hỏi lý thuyết tình huống, 1 bài tập yêu cầu viết code ngắn minh họa tính Đa hình. Phần đáp án cần đi kèm với giải thích tại sao các phương án khác sai hoặc những lỗi logic phổ biến ứng viên hay mắc phải.</li>
          </ul>
        </div>
      </div>
    \`,
    output: \`
      <div style="font-size: 13px;">
        <p style="margin-bottom: 12px; font-weight: bold;">Kết quả thử nghiệm (Tác vụ 2 - Trị riêng và Vector riêng):</p>
        <img src="assets/images/Bài 3/3.1.png" style="max-width: 100%; border-radius: 6px; margin-bottom: 8px;">
        <img src="assets/images/Bài 3/3.2.png" style="max-width: 100%; border-radius: 6px; margin-bottom: 8px;">
        <img src="assets/images/Bài 3/3.3.png" style="max-width: 100%; border-radius: 6px; margin-bottom: 16px;">
        
        <p style="margin-bottom: 8px;"><strong>Phân tích lý do tại sao một số prompt hiệu quả hơn:</strong></p>
        <ol style="margin-left: 20px; display: flex; flex-direction: column; gap: 8px;">
          <li><strong>Thiết lập bối cảnh (Context) và Vai trò (Role):</strong> Việc gán vai trò (Chuyên gia, Giảng viên) giúp AI điều chỉnh tone giọng, kho từ vựng và độ sâu chuyên môn phù hợp. Yêu cầu định nghĩa đối tượng người nghe ("sinh viên năm nhất") giúp AI tự động loại bỏ các thuật ngữ quá hàn lâm.</li>
          <li><strong>Định dạng đầu ra (Output Structure):</strong> Prompt nâng cao yêu cầu rõ ràng về định dạng (gạch đầu dòng, 3 phần rõ rệt, có đáp án ở cuối). Điều này giúp nội dung sinh ra trực quan, dễ quét thông tin (scan) và sử dụng ngay lập tức.</li>
          <li><strong>Hướng dẫn từng bước (Chain-of-thought):</strong> Thay vì yêu cầu AI "nhảy" thẳng đến kết luận, việc yêu cầu đi từ "Ẩn dụ -> Giải thích toán học -> Ứng dụng" buộc mô hình ngôn ngữ phải lập luận theo một trình tự logic, từ đó sinh ra văn bản mạch lạc và sâu sắc hơn.</li>
        </ol>
      </div>
    \`
  },
  4: {
    badge: "Bài tập 4 / Mục 4.4",
    title: "Ứng dụng công cụ cộng tác trực tuyến trong dự án nhóm",
    meta: {
      date: "Tháng 04, 2026",
      status: "Thực hành phối hợp nhóm",
      tools: "Google Drive, Docs, Discord",
      instructor: "Đội ngũ Giảng viên UET"
    },
    goal: "Thực hành thiết lập không gian làm việc số, quản lý tiến độ thực hiện các tác vụ của bản thân và phối hợp chặt chẽ với các thành viên khác để đảm bảo tính nhất quán của dự án.",
    process: \`
      <div style="font-size: 13px; display: flex; flex-direction: column; gap: 16px;">
        <p>Trong dự án nhóm, tôi đảm nhận vai trò <strong>Điều phối viên kỹ thuật</strong> và <strong>Soạn thảo nội dung chính</strong>. Để tối ưu hóa hiệu quả làm việc, tôi đã triển khai bộ 03 công cụ: Google Drive (Lưu trữ), Google Docs (Soạn thảo & Quản lý Task), Discord (Giao tiếp).</p>
        
        <div>
          <strong>1. Quản lý lưu trữ khoa học trên Google Drive</strong><br>
          Tôi đã thiết lập hệ thống thư mục logic: <code>01_Tai_lieu_nghien_cuu</code>, <code>02_Ban_nhap_bao_cao</code>, <code>03_Hinh_anh_minh_chung</code>, và <code>04_San_pham_cuoi</code>. Đảm bảo phân quyền Editor cho nhóm và bảo mật cho tệp tin gốc.
          <img src="assets/images/Bài 4/4.1.png" style="max-width: 100%; border-radius: 6px; margin-top: 8px;">
        </div>

        <div>
          <strong>2. Soạn thảo và Quản lý nhiệm vụ trên Google Docs</strong><br>
          Tích hợp Bảng quản lý nhiệm vụ (Task Tracking Table) ngay tại trang đầu của tài liệu để tự quản lý danh sách việc cần làm một cách trực quan.
          <img src="assets/images/Bài 4/4.2.png" style="max-width: 100%; border-radius: 6px; margin-top: 8px;">
        </div>

        <div>
          <strong>3. Tương tác và Thảo luận trên Discord</strong><br>
          Chủ động tạo các kênh văn bản riêng biệt để tránh loãng thông tin. Sử dụng tính năng "Thread" để thảo luận sâu về một lỗi kỹ thuật cụ thể.
          <img src="assets/images/Bài 4/4.3.png" style="max-width: 100%; border-radius: 6px; margin-top: 8px;">
        </div>
      </div>
    \`,
    output: \`
      <div style="font-size: 13px;">
        <p><strong>PHÂN TÍCH HIỆU QUẢ CỦA CÔNG CỤ</strong></p>
        <ul style="margin-left: 20px; display: flex; flex-direction: column; gap: 8px;">
          <li><strong>Tính đồng bộ thời gian thực:</strong> Google Docs cho phép tôi thấy được sự thay đổi của đồng đội ngay lập tức, tránh trùng lặp ý tưởng.</li>
          <li><strong>Khả năng truy hồi dữ liệu:</strong> Tính năng sao lưu tự động của Drive giúp tôi hoàn toàn yên tâm. Nếu xảy ra sai sót, dễ dàng khôi phục lại phiên bản trước.</li>
          <li><strong>Phân loại thông tin hiệu quả:</strong> Việc sử dụng các channel và tính năng Reply trên Discord giúp tôi không bị bỏ lỡ các thông báo quan trọng.</li>
        </ul>

        <p style="margin-top: 16px;"><strong>THÁCH THỨC VÀ CÁCH GIẢI QUYẾT</strong></p>
        <ol style="margin-left: 20px; display: flex; flex-direction: column; gap: 8px;">
          <li><strong>Xung đột nội dung khi nhiều người cùng sửa một đoạn văn:</strong> Giải quyết bằng cách đề xuất quy tắc sử dụng chế độ "Suggesting" thay vì sửa trực tiếp.</li>
          <li><strong>Bỏ lỡ thông báo trên Discord do cài đặt mặc định:</strong> Chủ động cấu hình lại thông báo (Notification Settings) và yêu cầu mọi người sử dụng lệnh @username khi cần phản hồi gấp.</li>
          <li><strong>Khó khăn trong việc theo dõi tiến độ tổng thể:</strong> Dành 15 phút mỗi buổi sáng để cập nhật trạng thái các task vào bảng trên Google Docs và thông báo ngắn gọn cho cả nhóm qua Discord.</li>
        </ol>
      </div>
    \`
  },
  5: {
    badge: "Bài tập 5 / Mục 5.4",
    title: "Ứng dụng AI tạo sinh trong sáng tạo nội dung số",
    meta: {
      date: "Tháng 05, 2026",
      status: "Tạo Blog & Infographic",
      tools: "Gemini, Nano Banana, Canva AI",
      instructor: "Đội ngũ Giảng viên UET"
    },
    goal: "Sử dụng kết hợp 3 công cụ AI tạo sinh (Text, Image, Design) để tạo ra một bài blog dài khoảng 800 - 1000 từ, kèm theo một Infographic trực quan hóa các dữ liệu chính.",
    process: \`
      <div style="font-size: 13px; display: flex; flex-direction: column; gap: 16px;">
        <div>
          <strong>Giai đoạn 1: Lên ý tưởng và viết nội dung (Text Generation)</strong><br>
          Sử dụng Google Gemini: "Đóng vai một chuyên gia giáo dục, hãy lập một dàn ý chi tiết cho một bài blog dài 1000 từ về chủ đề: 'Tác động của AI tạo sinh đến cách sinh viên đại học học tập và nghiên cứu'. Dàn ý cần có mở bài, 3 lợi ích, 2 thách thức và kết luận."<br>
          Kết quả: Gemini đưa ra một dàn ý rất logic. Tôi so sánh với ChatGPT và nhận thấy Gemini trả về kết quả cập nhật hơn, định dạng bullet point rõ ràng dễ đọc (scannable) hơn cho định dạng blog. Do đó, tôi chọn kết quả của Gemini để làm khung chính.
          <img src="assets/images/Bài 5/5.1.png" style="max-width: 100%; border-radius: 6px; margin-top: 8px;">
          <img src="assets/images/Bài 5/5.2.png" style="max-width: 100%; border-radius: 6px; margin-top: 8px;">
        </div>
        
        <div>
          <strong>Giai đoạn 2: Tạo hình ảnh minh họa (Image Generation)</strong><br>
          Công cụ: Nano Banana (Thông qua Google Gemini)<br>
          Prompt đã sử dụng: "A highly detailed, modern, and cinematic flat vector illustration of a diverse university student sitting at a glowing futuristic desk, interacting with a friendly, glowing AI hologram shaped like a brain. Neon blue and orange color palette, educational theme, clean background, 16:9 aspect ratio."<br>
          Kết quả: AI trả về 4 phương án. Tôi chọn phương án có bố cục cân đối nhất, màu sắc phù hợp với chủ đề công nghệ và giáo dục.
          <img src="assets/images/Bài 5/5.3.png" style="max-width: 100%; border-radius: 6px; margin-top: 8px;">
        </div>

        <div>
          <strong>Giai đoạn 3: Thiết kế Infographic (Design Assistance)</strong><br>
          Công cụ: Canva AI (Magic Design & Magic Write).<br>
          Tôi sử dụng tính năng "Magic Design" của Canva, nhập prompt: "Infographic template for 3 benefits of AI in education, minimalist style, corporate blue colors". Tôi tóm tắt bài viết blog do Gemini tạo ra thành 3 gạch đầu dòng ngắn gọn và đưa vào các hộp văn bản của template Canva.
          <img src="assets/images/Bài 5/5.4.png" style="max-width: 100%; border-radius: 6px; margin-top: 8px;">
        </div>
      </div>
    \`,
    output: \`
      <div style="font-size: 13px;">
        <p><strong>Phân tích vai trò của AI trong quá trình sáng tạo</strong></p>
        
        <p><strong>Điểm mạnh:</strong></p>
        <ul style="margin-left: 20px; display: flex; flex-direction: column; gap: 8px;">
          <li>Phá vỡ rào cản "trang giấy trắng" (Writer's Block): AI giúp lên dàn ý và tạo bản nháp với tốc độ cực nhanh (chỉ vài giây), tiết kiệm đến 60% thời gian nghiên cứu ban đầu.</li>
          <li>Khả năng tổng hợp: Tóm tắt lượng lớn thông tin thành định dạng Infographic ngắn gọn rất hiệu quả.</li>
          <li>Trực quan hóa ý tưởng: Nano Banana giúp một người không biết vẽ cũng có thể tạo ra hình ảnh minh họa chuyên nghiệp với độ phân giải cao.</li>
        </ul>

        <p style="margin-top: 12px;"><strong>Hạn chế:</strong></p>
        <ul style="margin-left: 20px; display: flex; flex-direction: column; gap: 8px;">
          <li>Thiếu chiều sâu và cảm xúc: Văn bản của AI đôi khi thiếu đi sự thấu cảm và những góc nhìn mang tính cá nhân, độc bản.</li>
          <li>Hiện tượng "Hallucination" (Ảo giác AI): AI đôi khi tựa bịa ra số liệu hoặc trích dẫn không có thật, đòi hỏi người dùng phải luôn kiểm chứng.</li>
          <li>Khó kiểm soát chi tiết ảnh: Rất khó để yêu cầu AI tạo ảnh sửa lại một chi tiết nhỏ (như ánh mắt, số lượng ngón tay) mà không làm thay đổi toàn bộ bố cục.</li>
        </ul>

        <p style="margin-top: 12px; font-style: italic;">"Trước đây, quy trình của tôi mang tính tuyến tính: Nghiên cứu -> Viết nháp -> Tìm ảnh -> Thiết kế -> Chỉnh sửa. Hiện tại, với AI, quy trình trở thành sự hợp tác song song (Co-creation): Tôi đóng vai trò là 'Giám đốc sáng tạo' (Đưa ra prompt, kiểm duyệt, định hướng), trong khi AI là 'Trợ lý thực thi' (Sản xuất nguyên liệu thô)."</p>
      </div>
    \`
  },
  6: {
    badge: "Bài tập 6 / Mục 6.4",
    title: "Sử dụng Trí tuệ nhân tạo có trách nhiệm trong học thuật",
    meta: {
      date: "Tháng 05, 2026",
      status: "Xây dựng quy tắc cá nhân",
      tools: "Critical Thinking, Ethics",
      instructor: "Đội ngũ Giảng viên UET"
    },
    goal: "Nắm vững các nguyên tắc đạo đức khi sử dụng AI trong môi trường học thuật, hiểu rõ ranh giới giữa việc ứng dụng AI như một công cụ hỗ trợ và hành vi gian lận.",
    process: \`
      <div style="font-size: 13px; display: flex; flex-direction: column; gap: 12px;">
        <p><strong>1. Phân tích ranh giới giữa hỗ trợ hợp lý và gian lận học thuật:</strong></p>
        <ul style="margin-left: 20px;">
          <li><strong>Hỗ trợ hợp lý:</strong> Xảy ra khi sinh viên dùng AI như một người "gia sư" hoặc "trợ lý nghiên cứu". Ví dụ: nhờ AI giải thích một khái niệm khó, gợi ý dàn ý, tóm tắt một bài báo dài. Khối lượng chất xám chính vẫn thuộc về sinh viên.</li>
          <li><strong>Gian lận học thuật:</strong> Xảy ra khi sinh viên vượt qua ranh giới sáng tạo, giao khoán toàn bộ việc viết bài, giải toán, hoặc viết code cho AI, sau đó nộp sản phẩm như thể đó là năng lực của chính mình.</li>
        </ul>

        <p><strong>2. Vấn đề về quyền sở hữu trí tuệ và trích dẫn:</strong></p>
        <p>AI học từ hàng triệu dữ liệu trên internet, bao gồm cả các tác phẩm có bản quyền. Việc AI tạo ra một đoạn văn bản không có nghĩa đoạn văn đó "sạch" về mặt bản quyền. Người dùng AI không thể tuyên bố bản quyền đối với văn bản do AI viết. Nếu sử dụng văn bản của AI mà không trích dẫn, người học có nguy cơ đạo văn (plagiarism) từ các tác giả gốc mà AI đã tổng hợp thông tin.</p>

        <p><strong>3. Tác động đến quá trình học tập và phát triển kỹ năng:</strong></p>
        <ul style="margin-left: 20px;">
          <li><strong>Mặt tích cực:</strong> Giúp cá nhân hóa việc học, tiết kiệm thời gian tìm kiếm tài liệu cơ bản, giúp sinh viên tập trung vào tư duy bậc cao hơn.</li>
          <li><strong>Mặt tiêu cực:</strong> Việc lạm dụng AI sẽ làm thui chột các kỹ năng cốt lõi: kỹ năng đọc hiểu sâu, kỹ năng viết luận, và đặc biệt là tư duy phản biện (critical thinking). Nếu sinh viên quen với việc có sẵn câu trả lời, họ sẽ mất khả năng tự giải quyết vấn đề.</li>
        </ul>
      </div>
    \`,
    output: \`
      <div style="font-size: 13px;">
        <p><strong>BỘ NGUYÊN TẮC CÁ NHÂN VỀ SỬ DỤNG AI CÓ TRÁCH NHIỆM</strong></p>
        <p>Để đảm bảo việc học tập hiệu quả và trung thực, tôi tự đề ra 6 nguyên tắc sau:</p>
        <ol style="margin-left: 20px; display: flex; flex-direction: column; gap: 8px;">
          <li><strong>Chỉ hỗ trợ, không thay thế:</strong> Tuyệt đối không dùng AI để viết hộ toàn bộ bài luận hay giải hộ bài tập nộp lấy điểm.</li>
          <li><strong>Luôn kiểm chứng thông tin (Fact-check):</strong> AI có thể bịa đặt thông tin (Hallucination). Mọi dữ kiện, số liệu, định lý AI đưa ra phải được đối chiếu với giáo trình hoặc nguồn uy tín.</li>
          <li><strong>Minh bạch trong trích dẫn:</strong> Luôn khai báo việc sử dụng AI trong các bài tập lớn hoặc nghiên cứu khoa học. (Ví dụ: <em>"Trong quá trình lập dàn ý và tìm kiếm các ý chính, tác giả có sử dụng mô hình ngôn ngữ lớn Google Gemini..."</em>)</li>
          <li><strong>Bảo vệ dữ liệu cá nhân & trường học:</strong> Không nhập các dữ liệu nhạy cảm, bài làm chưa công bố, hoặc thông tin cá nhân của người khác vào các nền tảng AI công cộng.</li>
          <li><strong>Tự viết bản thảo đầu tiên:</strong> Cố gắng tự phác thảo ý tưởng và viết nháp trước khi hỏi AI, nhằm bảo vệ sự sáng tạo và giọng văn cá nhân.</li>
          <li><strong>Chịu trách nhiệm cuối cùng:</strong> Tôi là người hoàn toàn chịu trách nhiệm về tính chính xác, đạo đức và chất lượng của sản phẩm cuối cùng nộp cho giảng viên, không đổ lỗi cho AI.</li>
        </ol>
      </div>
    \`
  }
};"""

import sys
with open('d:/UET/Ki 2/Nhập môn CNS & AI/Portfolio/js/main.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace everything from `const projectData = {` until `};`
start_idx = content.find('const projectData = {')
if start_idx == -1:
    print('Could not find projectData')
    sys.exit(1)

end_idx = content.find('};', start_idx)
if end_idx == -1:
    print('Could not find end of projectData')
    sys.exit(1)

new_content = content[:start_idx] + new_data + content[end_idx+2:]

with open('d:/UET/Ki 2/Nhập môn CNS & AI/Portfolio/js/main.js', 'w', encoding='utf-8') as f:
    f.write(new_content)
    
print('Successfully rewritten projectData in main.js')
