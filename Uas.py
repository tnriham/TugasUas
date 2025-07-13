import streamlit as st
import numpy as np

st.set_page_config(page_title="EOQ Calculator", page_icon="📦")

st.title("📦 Aplikasi Perhitungan EOQ (Economic Order Quantity)")
st.markdown("Simulasi sistem persediaan barang untuk menentukan jumlah pemesanan optimal (EOQ).")

tab1, tab2 = st.tabs(["🔢 Input Manual", "📘 Studi Kasus SmartTech"])

# Tab 1 – Input Manual
with tab1:
    st.header("Masukkan Data Persediaan Anda")

    D = st.number_input("Permintaan Tahunan (unit)", min_value=1, value=5000)
    S = st.number_input("Biaya Pemesanan per Pesanan (Rp)", min_value=1.0, value=75000.0)
    H = st.number_input("Biaya Penyimpanan per Unit per Tahun (Rp)", min_value=1.0, value=1500.0)

    EOQ = np.sqrt((2 * D * S) / H)
    num_orders = D / EOQ
    total_cost = (D / EOQ) * S + (EOQ / 2) * H

    st.subheader("📈 Hasil Perhitungan")
    col1, col2, col3 = st.columns(3)
    col1.metric("EOQ (unit)", f"{EOQ:.2f}")
    col2.metric("Jumlah Pesanan per Tahun", f"{num_orders:.2f}")
    col3.metric("Total Biaya Persediaan", f"Rp {total_cost:,.2f}")

# Tab 2 – Studi Kasus
with tab2:
    st.header("📘 Studi Kasus: Toko Elektronik SmartTech")
    st.write("""
    Toko SmartTech menjual lampu pintar. Berikut data tahunannya:
    - Permintaan tahunan (D): 2.400 unit
    - Biaya pemesanan per pesanan (S): Rp 100.000
    - Biaya penyimpanan per unit per tahun (H): Rp 2.000
    """)

    # Data Studi Kasus
    D2 = 2400
    S2 = 100000
    H2 = 2000

    EOQ2 = np.sqrt((2 * D2 * S2) / H2)
    num_orders2 = D2 / EOQ2
    total_cost2 = (D2 / EOQ2) * S2 + (EOQ2 / 2) * H2

    st.subheader("📊 Hasil Perhitungan Studi Kasus")
    st.write(f"**EOQ:** {EOQ2:.2f} unit")
    st.write(f"**Jumlah Pemesanan per Tahun:** {num_orders2:.2f} kali")
    st.write(f"**Total Biaya Persediaan:** Rp {total_cost2:,.2f}")

# Penjelasan Rumus
with st.expander("ℹ️ Penjelasan Rumus EOQ"):
    st.latex(r'''EOQ = \sqrt{\frac{2DS}{H}}''')
    st.markdown("""
    - **D** = Permintaan tahunan (unit)
    - **S** = Biaya pemesanan per pesanan
    - **H** = Biaya penyimpanan per unit per tahun
    
    **Total Biaya Persediaan:**
    """)
    st.latex(r'''TC = \left( \frac{D}{EOQ} \times S \right) + \left( \frac{EOQ}{2} \times H \right)''')
