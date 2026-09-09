import streamlit as st
import pandas as pd
from datetime import datetime

# ตั้งค่าหน้าตาของเว็บ
st.set_page_config(
    page_title="ร้านชานมไข่มุก - Boba Shop",
    page_icon="🧋",
    layout="centered"
)

# หัวข้อหลัก
st.title("🧋 ร้านชานมไข่มุก (Boba Order App)")
st.subheader("สั่งชานมสดใหม่ได้ง่ายๆ ผ่านเว็บ")

st.divider()

# ----------------- ส่วนที่ 1: เลือกเมนูและปรับแต่ง -----------------
st.header("1. เลือกรายการเครื่องดื่ม")

# รูปภาพประกอบเมนู
st.image("https://images.unsplash.com/photo-1558857563-b371033873b8?auto=format&fit=crop&w=600&q=80", caption="ชานมไต้หวันพรีเมียม", use_container_width=True)

# ราคาเริ่มต้น
base_price = 50
st.write(f"**ราคาเริ่มต้น:** {base_price} บาท")

# เลือกระดับความหวาน
sweetness = st.select_slider(
    "ระดับความหวาน (Sweetness):",
    options=["0%", "25%", "50%", "75%", "100%"],
    value="100%"
)

# เลือกท็อปปิ้ง
st.write("**เลือกท็อปปิ้งเพิ่มเติม:**")
toppings_price = 0

col1, col2 = st.columns(2)
with col1:
    boba = st.checkbox("ไข่มุกบราวน์ชูการ์ (+10 บาท)")
    pudding = st.checkbox("พุดดิ้งนมสด (+15 บาท)")
with col2:
    jelly = st.checkbox("เฉาก๊วย (+10 บาท)")
    aloe = st.checkbox("ว่านหางจระเข้ (+15 บาท)")

# คำนวณราคา
selected_toppings = []
if boba:
    toppings_price += 10
    selected_toppings.append("ไข่มุกบราวน์ชูการ์")
if pudding:
    toppings_price += 15
    selected_toppings.append("พุดดิ้งนมสด")
if jelly:
    toppings_price += 10
    selected_toppings.append("เฉาก๊วย")
if aloe:
    toppings_price += 15
    selected_toppings.append("ว่านหางจระเข้")

total_price = base_price + toppings_price

st.divider()

# ----------------- ส่วนที่ 2: สรุปออเดอร์และบันทึกข้อมูล -----------------
st.header("2. สรุปรายการสั่งซื้อ")

# แสดงราคารวม
st.metric(label="ราคารวมสุทธิ", value=f"{total_price} บาท")

# ปุ่มกดสั่งซื้อ
if st.button("🛒 ยืนยันการสั่งซื้อ", type="primary", use_container_width=True):
    # บันทึกข้อมูลออเดอร์ลงระบบ
    order_data = {
        "เวลา": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "ความหวาน": sweetness,
        "ท็อปปิ้ง": ", ".join(selected_toppings) if selected_toppings else "ไม่ใส่",
        "ราคารวม": f"{total_price} บาท"
    }
    
    st.success("🎉 บันทึกออเดอร์เรียบร้อยแล้ว!")
    st.json(order_data) # แสดงสรุปออเดอร์เป็น JSON
