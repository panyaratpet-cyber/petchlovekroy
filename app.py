import streamlit as st

# --- ตั้งค่าหน้าตาธีมแอปพลิเคชัน ---
st.set_page_config(page_title="Colab Delivery", page_icon="🍔", layout="centered")

# ปรับแต่งสีสันสไตล์แอปสั่งอาหาร (โทนส้ม-ครีม)
st.markdown("""
    <style>
    .main { background-color: #FFF9F5; }
    .stButton>button {
        border-radius: 12px;
        font-weight: bold;
    }
    div[data-testid="stNotification"] {
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# --- ข้อมูลเมนูราคาและรายการแนะนำ ---
new_foods = ["ข้าวผัดกะเพราเนื้อไข่ดาว (65.-)", "สปาเก็ตตี้คาโบนาร่า (89.-)", "ส้มตำไทยไข่เค็ม (60.-)"]
new_drinks = ["ชาไทยเย็นสูตรเข้มข้น (45.-)", "มัทฉะลาเต้เย็น (60.-)"]

menu_data = {
    "อาหารจานเดียว": {
        "ข้าวผัดกะเพราหมูสับ/ไก่": 55,
        "ข้าวผัดกะเพราเนื้อไข่ดาว": 65,
        "ข้าวผัดกุ้งสด": 60,
        "ข้าวไข่เจียวหมูสับ": 45,
        "ผัดไทยกุ้งสด": 70,
        "ข้าวหมูกระเทียมไข่ดาว": 55,
        "สปาเก็ตตี้คาโบนาร่า": 89,
        "สปาเก็ตตี้ขี้เมาทะเล": 95,
        "ส้มตำไทยไข่เค็ม": 60,
        "ต้มยำกุ้งน้ำข้น (ราดข้าว)": 80
    },
    "เครื่องดื่ม": {
        "ชาไทยเย็นสูตรเข้มข้น": 45,
        "กาแฟส้มยูซุ": 65,
        "มัทฉะลาเต้เย็น": 60,
        "อเมริกาโน่เย็น": 50,
        "ลาเต้เย็น": 55,
        "ชามะนาว": 40,
        "นมสดฮอกไกโดเย็น": 45,
        "น้ำอัดลม + น้ำแข็ง": 25
    },
    "ของทานเล่น": {
        "เฟรนช์ฟรายส์ทอด": 49,
        "นักเก็ตไก่ (6 ชิ้น)": 59,
        "ปีกไก่ทอดน้ำปลา": 79,
        "เกี๊ยวซ่าทอด": 59
    }
}

# Session State สำหรับเก็บข้อมูลตะกร้าสินค้า
if "cart" not in st.session_state:
    st.session_state.cart = []

# --- ส่วนหัวและเมนูแนะนำ ---
st.title("🍔 Colab Delivery")
st.caption("สั่งซื้อง่าย ส่งตรงถึงมือคุณ")

st.warning(f"""
🔥 **แนะนำเมนูมาใหม่ประจำวันนี้!**
* 🍲 **อาหาร:** {", ".join(new_foods)}
* 🥤 **เครื่องดื่ม:** {", ".join(new_drinks)}
""")

st.divider()

# --- ส่วนเลือกสั่งอาหาร ---
st.subheader("🛒 เลือกสั่งอาหารและเครื่องดื่ม")

cat = st.radio("หมวดหมู่:", list(menu_data.keys()), horizontal=True)

# ดึงรายการเมนูตามหมวดหมู่
items_in_cat = menu_data[cat]
item_names = [f"{item} — {price} บาท" for item, price in items_in_cat.items()]

selected_option = st.selectbox(f"เลือกรายการ ({cat}):", item_names)

# ช่องหมายเหตุ
note = st.text_input("📝 หมายเหตุเพิ่มเติม (เช่น เผ็ดน้อย, ไม่ใส่น้ำตาล, แยกน้ำแข็ง):", placeholder="ระบุรายละเอียดที่นี่...")

if st.button("➕ เพิ่มลงตะกร้า", use_container_width=True, type="primary"):
    # แยกชื่อเมนูกับราคาออกจากข้อความ
    item_name = selected_option.split(" — ")[0]
    item_price = items_in_cat[item_name]
    
    # บันทึกลงตะกร้า
    st.session_state.cart.append({
        "name": item_name,
        "price": item_price,
        "note": note if note else "ไม่มี"
    })
    st.toast(f"เพิ่ม '{item_name}' ลงตะกร้าเรียบร้อย!", icon="✅")

st.divider()

# --- ส่วนแสดงตะกร้าสินค้าและคำนวณราคา ---
st.subheader("📋 รายการสั่งซื้อของคุณ")

if st.session_state.cart:
    total_price = 0
    for i, item in enumerate(st.session_state.cart, 1):
        st.write(f"**{i}. {item['name']}** — {item['price']} บาท")
        st.caption(f"📌 หมายเหตุ: {item['note']}")
        total_price += item['price']
    
    st.markdown(f"### 💵 **ราคารวมทั้งหมด: {total_price} บาท**")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("✅ ยืนยันการสั่งซื้อ", use_container_width=True):
            st.balloons()
            st.success(f"🎉 สั่งซื้อสำเร็จ! ยอดชำระทั้งหมด {total_price} บาท ร้านกำลังเตรียมจัดส่งครับ")
            st.session_state.cart = []
    with col2:
        if st.button("🗑️ ล้างตะกร้า", use_container_width=True):
            st.session_state.cart = []
            st.rerun()
else:
    st.info("ยังไม่มีรายการในตะกร้า เลือกเมนูด้านบนได้เลยครับ")
