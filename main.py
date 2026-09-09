import streamlit as st
from datetime import datetime

# ตั้งค่าหน้าตาของเว็บ
st.set_page_config(
    page_title="ร้านชานมไข่มุก - Boba Shop",
    page_icon="🧋",
    layout="centered"
)

# หัวข้อหลัก
st.title("🧋 ร้านชานมไข่มุก (Boba Order)")
st.caption("สั่งง่าย ชงสดใหม่ทุกแก้ว")

st.divider()

# ----------------- ส่วนที่ 1: เลือกเมนูเครื่องดื่ม -----------------
st.header("1. เลือกเมนูเครื่องดื่ม")

# รายการเมนูพร้อมราคา และสถานะแนะนำ
menu_list = {
    "ชานมไต้หวันต้นตำรับ ⭐ (แนะนำ)": {"price": 50, "recommended": True},
    "ชานมบราวน์ชูการ์ ⭐ (แนะนำ)": {"price": 60, "recommended": True},
    "ชาไทยพรีเมียม": {"price": 45, "recommended": False},
    "ชาเขียวมัทฉะนมสด": {"price": 55, "recommended": False},
    "ชามะลิใส": {"price": 40, "recommended": False},
}

# แสดงโซนเมนูแนะนำพร้อมราคา
st.subheader("🔥 เมนูแนะนำ")
rec_cols = st.columns(2)
col_idx = 0
for name, details in menu_list.items():
    if details["recommended"]:
        with rec_cols[col_idx % 2]:
            st.info(f"**{name}**\n\n💰 **ราคา {details['price']} บาท**")
        col_idx += 1

st.write("")

# สร้างตัวเลือกรายการเมนูแบบแสดงราคาด้านข้าง
menu_options = [f"{name} — {details['price']} บาท" for name, details in menu_list.items()]

selected_option = st.radio(
    "เลือกเมนูที่ต้องการสั่ง:",
    options=menu_options
)

# ดึงข้อมูลชื่อเมนูและราคาจากการเลือก
selected_menu_name = selected_option.split(" — ")[0]
base_price = menu_list[selected_menu_name]["price"]

st.divider()

# ----------------- ส่วนที่ 2: ปรับแต่งเครื่องดื่ม -----------------
st.header("2. ปรับแต่งระดับความหวาน & ท็อปปิ้ง")

# เลือกระดับความหวาน
sweetness = st.select_slider(
    "ระดับความหวาน (Sweetness):",
    options=["0%", "25%", "50%", "75%", "100%"],
    value="100%"
)

# รายการท็อปปิ้งพร้อมราคา
toppings_data = {
    "ไข่มุกบราวน์ชูการ์ (+10 บาท)": 10,
    "พุดดิ้งนมสด (+15 บาท)": 15,
    "เฉาก๊วย (+10 บาท)": 10,
    "ว่านหางจระเข้ (+15 บาท)": 15,
    "วิปครีม (+20 บาท)": 20,
}

# ให้เลือกท็อปปิ้งได้หลายรายการพร้อมกัน
selected_toppings = st.multiselect(
    "เลือกท็อปปิ้ง (เลือกได้หลายอย่าง):",
    options=list(toppings_data.keys()),
    placeholder="เลือกท็อปปิ้งที่ต้องการ..."
)

# คำนวณราคาท็อปปิ้ง
toppings_price = sum(toppings_data[t] for t in selected_toppings)
total_price = base_price + toppings_price

st.divider()

# ----------------- ส่วนที่ 3: สรุปออเดอร์และบันทึก -----------------
st.header("3. สรุปรายการสั่งซื้อ")

# แสดงรายละเอียดพร้อมแจกแจงราคา
st.write(f"**เมนูที่เลือก:** {selected_menu_name} (`{base_price} บาท`)")
st.write(f"**ระดับความหวาน:** {sweetness}")
st.write(f"**ท็อปปิ้ง:** {', '.join(selected_toppings) if selected_toppings else 'ไม่ใส่ท็อปปิ้ง'} (`+{toppings_price} บาท`)")

st.metric(label="ราคารวมสุทธิ", value=f"{total_price} บาท")

# ปุ่มยืนยันการสั่งซื้อ
if st.button("🛒 ยืนยันการสั่งซื้อ", type="primary", use_container_width=True):
    order_summary = {
        "เวลา": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "เมนู": selected_menu_name,
        "ราคาเมนูหลัก": f"{base_price} บาท",
        "ความหวาน": sweetness,
        "ท็อปปิ้ง": ", ".join(selected_toppings) if selected_toppings else "ไม่ใส่",
        "ราคาท็อปปิ้ง": f"{toppings_price} บาท",
        "ราคารวมทั้งสิ้น": f"{total_price} บาท"
    }
    
    st.success("🎉 บันทึกออเดอร์เรียบร้อยแล้ว!")
    st.json(order_summary)
