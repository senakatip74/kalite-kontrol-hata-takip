"""Kalite Kontrol ve Hata Takip Sistemi."""
import streamlit as st
from storage import ERROR_TYPES, create_defect, list_defects

st.set_page_config(page_title="Kalite Kontrol", page_icon="🔎", layout="wide")
st.title("Kalite Kontrol ve Hata Takip Sistemi")
st.caption("Üretimde tespit edilen hataları kaydedin ve inceleyin.")

st.subheader("Yeni hata kaydı")
with st.form("defect_form", clear_on_submit=True):
    product_name = st.text_input("Ürün adı", placeholder="Örn. Metal parça A")
    error_type = st.selectbox("Hata türü", ERROR_TYPES)
    description = st.text_area("Hata açıklaması")
    quantity = st.number_input("Hata adedi", min_value=1, value=1, step=1)
    submitted = st.form_submit_button("Kaydı ekle")

if submitted:
    try:
        new_id = create_defect(product_name, error_type, description, int(quantity))
    except ValueError as exc:
        st.error(str(exc))
    else:
        st.success(f"#{new_id} numaralı hata kaydı oluşturuldu.")

st.subheader("Kaydedilen hatalar")
records = list_defects()
if records:
    st.dataframe(records, use_container_width=True, hide_index=True)
else:
    st.info("Henüz hata kaydı bulunmuyor.")
