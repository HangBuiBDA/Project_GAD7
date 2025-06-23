import streamlit as st

# Tiêu đề chính
st.title("Ứng dụng GAD-7 Đánh giá Lo âu - Sinh viên VNUIS")
st.write("Ứng dụng được phát triển nhằm hỗ trợ sinh viên VNUIS tự đánh giá mức độ lo âu thông qua 7 câu hỏi tiêu chuẩn từ thang đo GAD-7 (Generalized Anxiety Disorder).")

# --- Phần 1: Thông tin cơ bản ---
st.header("📝 Thông tin cá nhân & Lối sống")

age = st.number_input("1. Tuổi của bạn:", min_value=16, max_value=100, step=1)
gender = st.selectbox("2. Giới tính:", ["Nam", "Nữ", "Khác", "Không muốn tiết lộ"])
major = st.text_input("3. Ngành học:")
year = st.selectbox("4. Năm học:", ["Năm nhất", "Năm hai", "Năm ba", "Năm tư", "Khác"])
part_time = st.radio("5. Bạn có đang làm thêm không?", ["Có", "Không"])
sleep_hours = st.slider("6. Trung bình bạn ngủ bao nhiêu tiếng mỗi đêm?", 0, 12, 7)
social_media = st.slider("7. Thời gian dùng mạng xã hội mỗi ngày (giờ):", 0, 12, 2)

# --- Phần 2: Câu hỏi GAD-7 ---
st.header("📋 Bảng câu hỏi GAD-7")

score = 0
options = ["Không bao giờ", "Vài ngày", "Hơn một nửa số ngày", "Gần như mỗi ngày"]

for i in range(1, 8):
    answer = st.radio(
        f"Câu hỏi {i}: Trong 2 tuần qua, bạn cảm thấy lo lắng...?",
        options,
        key=f"q{i}"
    )
    score += options.index(answer)

# --- Phần 3: Kết quả ---
if st.button("📊 Xem kết quả"):
    st.subheader("🎯 Kết quả đánh giá GAD-7")
    st.write(f"Tổng điểm GAD-7 của bạn là: **{score}**")

    if score <= 4:
        st.success("✅ Mức độ lo âu: Nhẹ")
    elif score <= 9:
        st.info("ℹ️ Mức độ lo âu: Trung bình")
    elif score <= 14:
        st.warning("⚠️ Mức độ lo âu: Tương đối cao")
    else:
        st.error("🚨 Mức độ lo âu: Cao – Nên tham khảo ý kiến chuyên gia tâm lý")

    # Hiển thị lại thông tin cá nhân
    st.subheader("📌 Thông tin bạn cung cấp:")
    st.markdown(f"- **Tuổi**: {age}")
    st.markdown(f"- **Giới tính**: {gender}")
    st.markdown(f"- **Ngành học**: {major}")
    st.markdown(f"- **Năm học**: {year}")
    st.markdown(f"- **Làm thêm**: {part_time}")
    st.markdown(f"- **Giấc ngủ trung bình**: {sleep_hours} tiếng/đêm")
    st.markdown(f"- **Thời gian dùng MXH**: {social_media} giờ/ngày")
