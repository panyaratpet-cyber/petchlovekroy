import streamlit as st

st.set_page_config(page_title="ระบบสั่งอาหาร", page_icon="🍽️", layout="centered")

new_foods = ["ข้าวผัดกะเพราเนื้อไข่ดาว", "ต้มยำกุ้งน้ำข้น", "สปาเก็ตตี้คาโบนาร่า"]
new_drinks = ["ชาไทยเย็น (สูตรเข้มข้น)", "กาแฟส้มยูซุ", "มัทฉะลาเต้"]

all_menu = {
    "อาหาร": ["ข้าวผัดกะเพราเนื้อไข่ดาว", "ต้มยำกุ้งน้ำข้น", "สปาเก็ตตี้คาโบนาร่า", "ข้าวไข่เจียวหมูสับ", "ผัดไทยกุ้งสด"],
    "เครื่องดื่ม": ["ชาไทยเย็น (สูตรเข้มข้น)", "กาแฟส้มยูซุ", "มัทฉะลาเต้", "อเมริกาโน่เย็น", "ชามะนาว"]
}

if "cart" not in st.session_state:
    st.session_state.cart = []

st.title("🍽️ สั่งอาหารออนไลน์")

st.info(f"""
✨ **แนะนำประจำวันนี้!**
* 🍲 **อาหาร:** {", ".join(new_foods)}
* 🥤 **เครื่องดื่ม:** {", ".join(new_drinks)}
""")

category = st.radio("เลือกหมวดหมู่:", ["อาหาร", "เครื่องดื่ม"], horizontal=True)
selected_item = st.selectbox("เลือกรายการ:", all_menu[category])

if st.button("➕ เพิ่มลงตะกร้า", use_container_width=True):
    st.session_state.cart.append(selected_item)
    st.toast(f"เพิ่ม '{selected_item}' เรียบร้อย!", icon="✅")

st.divider()
st.subheader("📋 รายการในตะกร้า")

if st.session_state.cart:
    for i, item in enumerate(st.session_state.cart, 1):
        st.write(f"{i}. {item}")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("✅ ยืนยันการสั่งซื้อ", type="primary", use_container_width=True):
            st.balloons()
            st.success("🎉 รับออเดอร์เรียบร้อยครับ!")
            st.session_state.cart = []
    with col2:
        if st.button("🗑️ ล้างตะกร้า", use_container_width=True):
            st.session_state.cart = []
            st.rerun()
else:
    st.write("ยังไม่มีรายการในตะกร้า")
