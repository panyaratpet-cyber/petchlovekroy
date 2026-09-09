import streamlit as st
from datetime import datetime, timedelta

# ตั้งค่าหน้าตาของเว็บ
st.set_page_config(
    page_title="เตาอบแก้มป่องง - สั่งทำเค้กวันเกิด & โอกาสพิเศษ",
    page_icon="🎂",
    layout="centered"
)

# Header ร้าน
st.title("🎂 เตาอบแก้มป่องง")
st.caption("เค้กโฮมเมด อบด้วยใจ แก้มป่องทุกปอนด์ ✨")

st.divider()

# ----------------- ส่วนที่ 1: เลือกขนาดและรูปทรงเค้ก -----------------
st.header("1. เลือกขนาดเค้ก (Cake Size)")

sizes = {
    "0.5 ปอนด์ (ทานได้ 1-2 คน) — 250 บาท": 250,
    "1 ปอนด์ (ทานได้ 3-4 คน) ⭐ แนะนำ — 450 บาท": 450,
    "2 ปอนด์ (ทานได้ 6-8 คน) — 750 บาท": 750,
    "3 ปอนด์ (ทานได้ 10 คนขึ้นไป) — 1,050 บาท": 1050,
}

selected_size_str = st.radio("ขนาดเค้กที่ต้องการ:", options=list(sizes.keys()))
base_price = sizes[selected_size_str]

st.divider()

# ----------------- ส่วนที่ 2: รสชาติเนื้อเค้กและครีม -----------------
st.header("2. เลือกเนื้อเค้กและรสชาติครีม")

col1, col2 = st.columns(2)

with col1:
    cake_flavor = st.selectbox(
        "🍰 รสชาติเนื้อเค้ก:",
        ["วนิลาหอมนุ่ม", "ช็อกโกแลตเข้มข้น", "สตรอว์เบอร์รี", "ชาไทยนมสด", "ใบเตยหอม"]
    )

with col2:
    cream_flavor = st.selectbox(
        "🧁 รสชาติวิปครีม/ฟรอสติ้ง:",
        ["นมสดนิวซีแลนด์", "ช็อกโกแลตการ์นาช", "ครีมชีส", "วิปครีมสตรอว์เบอร์รี"]
    )

st.divider()

# ----------------- ส่วนที่ 3: ตกแต่งเพิ่มเติม & ข้อความหน้าเค้ก -----------------
st.header("3. ตกแต่งเค้ก & ข้อความพิเศษ")

# ท็อปปิ้งตกแต่งเค้ก
st.subheader("🍓 เลือกท็อปปิ้งตกแต่งเค้ก")
decorations = {
    "สตรอว์เบอร์รีสดแน่นๆ (+80 บาท)": 80,
    "ผลไม้รวม (สตรอว์เบอร์รี/บลูเบอร์รี/กีวี) (+100 บาท)": 100,
    "ช็อกโกแลตเฟอเรโร่ & โอริโอ้ (+70 บาท)": 70,
    "เทียนวันเกิดตัวเลข/เทียนเกลียวฟรี (แถมฟรี)": 0,
}

selected_decorations = st.multiselect(
    "เลือกรายการตกแต่งเพิ่มเติม (เลือกได้หลายอย่าง):",
    options=list(decorations.keys()),
    placeholder="เลือกของตกแต่ง..."
)

decor_price = sum(decorations[d] for d in selected_decorations)

# ข้อความบนหน้าเค้ก
st.subheader("✍️ ข้อความบนหน้าเค้ก (Cake Message)")
cake_message = st.text_input(
    "เขียนข้อความบนเค้ก (ไม่เกิน 25 ตัวอักษร):",
    placeholder="เช่น Happy Birthday P'Pang!",
    max_chars=25
)

st.divider()

# ----------------- ส่วนที่ 4: กำหนดวันเวลาที่ต้องการรับเค้ก -----------------
st.header("4. นัดหมายวันรับเค้ก")

# กำหนดให้สั่งล่วงหน้าอย่างน้อย 2 วัน
min_date = datetime.now() + timedelta(days=2)
pickup_date = st.date_input(
    "📆 วันที่ต้องการรับเค้ก (สั่งล่วงหน้าอย่างน้อย 2 วัน):",
    value=min_date,
    min_value=min_date
)

pickup_time = st.time_input("⏰ เวลาที่สะดวกมารับเค้ก:", value=datetime.strptime("14:00", "%H:%M").time())

st.divider()

# ----------------- ส่วนที่ 5: สรุปออเดอร์ -----------------
st.header("5. สรุปรายการสั่งเค้ก")

total_price = base_price + decor_price

st.write(f"**ร้าน:** เตาอบแก้มป่องง 🎂")
st.write(f"**ขนาด:** {selected_size_str.split(' — ')[0]} (`{base_price} บาท`)")
st.write(f"**เนื้อเค้ก:** {cake_flavor} | **ครีม:** {cream_flavor}")
st.write(f"**ท็อปปิ้งตกแต่ง:** {', '.join(selected_decorations) if selected_decorations else 'ไม่มี'} (`+{decor_price} บาท`)")
st.write(f"**ข้อความบนเค้ก:** {f'\"{cake_message}\"' if cake_message else 'ไม่เขียนข้อความ'}")
st.write(f"**วัน-เวลารับเค้ก:** {pickup_date.strftime('%d/%m/%Y')} เวลา {pickup_time.strftime('%H:%M')} น.")

st.metric(label="ราคารวมสุทธิ", value=f"{total_price} บาท")

# ปุ่มยืนยัน
if st.button("🛍️ ส่งออเดอร์ให้ร้านเตาอบแก้มป่องง", type="primary", use_container_width=True):
    order_summary = {
        "เวลาที่สั่ง": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "ร้าน": "เตาอบแก้มป่องง",
        "ขนาด": selected_size_str.split(' — ')[0],
        "ราคาเค้ก": f"{base_price} บาท",
        "เนื้อเค้ก": cake_flavor,
        "รสครีม": cream_flavor,
        "ท็อปปิ้ง": ", ".join(selected_decorations) if selected_decorations else "ไม่มี",
        "ข้อความหน้าเค้ก": cake_message if cake_message else "-",
        "วันรับเค้ก": pickup_date.strftime("%Y-%m-%d"),
        "เวลารับเค้ก": pickup_time.strftime("%H:%M"),
        "ราคารวมทั้งสิ้น": f"{total_price} บาท"
    }
    
    st.success("🎉 ส่งออเดอร์สำเร็จแล้ว! ทางร้านเตาอบแก้มป่องงจะรีบติดต่อกลับเพื่อยืนยันครับ")
    st.json(order_summary)
