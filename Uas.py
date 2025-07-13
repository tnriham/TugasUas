import streamlit as st
import numpy as np

# Title & Description
st.title("📦 Aplikasi Perhitungan EOQ (Economic Order Quantity)")
st.markdown("""
Simulasi sistem persediaan barang untuk menentukan jumlah pemesanan optimal berdasarkan model EOQ (Economic Order Quantity).
""")

# Input Section
st.header("🔢 Masukkan Data Persediaan")
D = st.number_input("Permintaan Tahunan (unit)", min_value=1, value=5000)
S = st.number_input("Biaya Pemesanan per Pesanan (Rp)", min_value=1.0, value=75000.0)
H = st.number_input("Biaya Penyimpanan per Unit per Tahun (Rp)", min_value=1.0, value=1500.0)

# EOQ Calculation
EOQ = np.sqrt((2 * D * S) / H)
num_orders = D / EOQ
total_cost = (D / EOQ) * S + (EOQ / 2) * H

# Output Section
st.header("📈 Hasil Perhitungan")
col1, col2, col3 = st.columns(3)
col1.metric("🔹 EOQ (unit)", f"{EOQ:.2f}")
col2.metric("🔹 Jumlah Pesanan per Tahun", f"{num_orders:.2f} kali")
col3.metric("🔹 Total Biaya Persediaan", f"Rp {total_cost:,.2f}")

# Explanation
with st.expander("📘 Penjelasan Rumus EOQ"):
    st.markdown(r"""
**Rumus EOQ:**
\[
EOQ = \sqrt{\frac{2DS}{H}}
\]

Dimana:  
- \(D\) = Permintaan tahunan  
- \(S\) = Biaya pemesanan per pesanan  
- \(H\) = Biaya penyimpanan per unit per tahun

**Total Biaya Persediaan:**
\[
TC = \left( \frac{D}{EOQ} \times S \right) + \left( \frac{EOQ}{2} \times H \right)
\]
""")

# Footer
st.markdown("---")
st.caption("Dibuat oleh: Aplikasi EOQ dengan Streamlit – © 2025")
