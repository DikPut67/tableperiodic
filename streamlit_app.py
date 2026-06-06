import streamlit as st

# ──────────────────────────────────────────────
# DATA
# ──────────────────────────────────────────────

ELEMENT_INFO = {
    "O":  {"nama": "Oksigen",    "nomor": 8,  "massa": 15.999, "golongan": "Non-Logam"},
    "C":  {"nama": "Karbon",     "nomor": 6,  "massa": 12.011, "golongan": "Non-Logam"},
    "H":  {"nama": "Hidrogen",   "nomor": 1,  "massa": 1.008,  "golongan": "Non-Logam"},
    "N":  {"nama": "Nitrogen",   "nomor": 7,  "massa": 14.007, "golongan": "Non-Logam"},
    "Ca": {"nama": "Kalsium",    "nomor": 20, "massa": 40.078, "golongan": "Logam Alkali Tanah"},
    "P":  {"nama": "Fosfor",     "nomor": 15, "massa": 30.974, "golongan": "Non-Logam"},
    "K":  {"nama": "Kalium",     "nomor": 19, "massa": 39.098, "golongan": "Logam Alkali"},
    "S":  {"nama": "Sulfur",     "nomor": 16, "massa": 32.06,  "golongan": "Non-Logam"},
    "Na": {"nama": "Natrium",    "nomor": 11, "massa": 22.990, "golongan": "Logam Alkali"},
    "Cl": {"nama": "Klorin",     "nomor": 17, "massa": 35.45,  "golongan": "Halogen"},
    "Mg": {"nama": "Magnesium",  "nomor": 12, "massa": 24.305, "golongan": "Logam Alkali Tanah"},
    "Fe": {"nama": "Besi",       "nomor": 26, "massa": 55.845, "golongan": "Logam Transisi"},
    "Zn": {"nama": "Seng",       "nomor": 30, "massa": 65.38,  "golongan": "Logam Transisi"},
    "I":  {"nama": "Iodin",      "nomor": 53, "massa": 126.90, "golongan": "Halogen"},
    "F":  {"nama": "Fluor",      "nomor": 9,  "massa": 18.998, "golongan": "Halogen"},
    "Si": {"nama": "Silikon",    "nomor": 14, "massa": 28.085, "golongan": "Metaloid"},
    "Al": {"nama": "Aluminium",  "nomor": 13, "massa": 26.982, "golongan": "Logam Pasca-Transisi"},
    "Cr": {"nama": "Kromium",    "nomor": 24, "massa": 51.996, "golongan": "Logam Transisi"},
    "Ni": {"nama": "Nikel",      "nomor": 28, "massa": 58.693, "golongan": "Logam Transisi"},
    "Cu": {"nama": "Tembaga",    "nomor": 29, "massa": 63.546, "golongan": "Logam Transisi"},
    "Sn": {"nama": "Timah",      "nomor": 50, "massa": 118.71, "golongan": "Logam Pasca-Transisi"},
}

BAGIAN_TUBUH = {
    "🦴 Tulang & Gigi": {
        "deskripsi": "Tulang dan gigi adalah jaringan keras utama dalam tubuh manusia yang berfungsi sebagai penyangga, pelindung organ vital, dan tempat produksi sel darah.",
        "unsur": [
            {"simbol": "Ca", "persen": 39.0, "fungsi": "Komponen utama hidroksiapatit — mineral penyusun tulang dan gigi, menjaga kepadatan dan kekuatan struktur tulang."},
            {"simbol": "P",  "persen": 17.0, "fungsi": "Bergabung dengan kalsium membentuk kalsium fosfat, menyusun sekitar 85% cadangan fosfor tubuh ada di tulang."},
            {"simbol": "O",  "persen": 28.0, "fungsi": "Terdapat dalam gugus fosfat dan hidroksil pada hidroksiapatit, serta dalam matriks organik kolagen."},
            {"simbol": "C",  "persen": 15.0, "fungsi": "Menyusun kolagen — protein organik utama yang memberi elastisitas dan ketahanan tulang terhadap benturan."},
            {"simbol": "H",  "persen": 1.0,  "fungsi": "Terdapat dalam gugus hidroksil (-OH) pada mineral hidroksiapatit dan dalam struktur kolagen."},
        ]
    },
    "🩸 Darah": {
        "deskripsi": "Darah adalah jaringan cair yang beredar dalam sistem peredaran darah, bertugas mengangkut oksigen, nutrisi, hormon, dan membuang sisa metabolisme.",
        "unsur": [
            {"simbol": "O",  "persen": 65.0, "fungsi": "Diangkut oleh hemoglobin dari paru-paru ke seluruh sel tubuh, merupakan komponen utama molekul air dalam plasma."},
            {"simbol": "H",  "persen": 10.0, "fungsi": "Komponen utama molekul air (H₂O) yang mendominasi plasma darah (~90% plasma adalah air)."},
            {"simbol": "Fe", "persen": 0.006,"fungsi": "Inti atom pusat hemoglobin yang mengikat dan melepas oksigen. Kekurangan Fe menyebabkan anemia."},
            {"simbol": "C",  "persen": 18.0, "fungsi": "Menyusun protein plasma (albumin, globulin, fibrinogen), glukosa, dan senyawa organik lain dalam darah."},
            {"simbol": "N",  "persen": 3.0,  "fungsi": "Menyusun asam amino dan protein darah seperti hemoglobin, albumin, dan antibodi."},
            {"simbol": "Na", "persen": 0.3,  "fungsi": "Ion utama ekstraseluler yang menjaga tekanan osmotik darah dan keseimbangan cairan dalam tubuh."},
            {"simbol": "K",  "persen": 0.2,  "fungsi": "Ion utama intraseluler yang berperan dalam transmisi impuls saraf dan kontraksi otot jantung."},
            {"simbol": "Cl", "persen": 0.3,  "fungsi": "Anion utama dalam plasma darah yang menjaga keseimbangan elektrolit dan pH darah bersama bikarbonat."},
        ]
    },
    "💪 Otot": {
        "deskripsi": "Jaringan otot adalah jaringan yang mampu berkontraksi dan relaksasi untuk menghasilkan gerakan tubuh, baik gerakan sadar maupun tidak sadar.",
        "unsur": [
            {"simbol": "O",  "persen": 65.0, "fungsi": "Diperlukan untuk respirasi aerobik dalam mitokondria sel otot untuk menghasilkan ATP sebagai energi kontraksi."},
            {"simbol": "C",  "persen": 18.0, "fungsi": "Menyusun protein struktural otot seperti aktin dan miosin yang bertanggung jawab terhadap mekanisme kontraksi."},
            {"simbol": "H",  "persen": 10.0, "fungsi": "Komponen air intraseluler dan menyusun seluruh rantai protein otot bersama karbon dan nitrogen."},
            {"simbol": "N",  "persen": 3.0,  "fungsi": "Menyusun asam amino pembentuk protein otot, termasuk aktin, miosin, troponin, dan tropomiosin."},
            {"simbol": "P",  "persen": 0.2,  "fungsi": "Terdapat dalam ATP (adenosin trifosfat) dan kreatin fosfat — sumber energi langsung untuk kontraksi otot."},
            {"simbol": "Ca", "persen": 0.1,  "fungsi": "Ion kalsium memicu kontraksi otot dengan berikatan pada troponin C untuk mengaktifkan mekanisme filamen geser."},
            {"simbol": "K",  "persen": 0.35, "fungsi": "Menjaga potensial membran sel otot dan berperan dalam depolarisasi yang memicu kontraksi."},
            {"simbol": "Mg", "persen": 0.05, "fungsi": "Kofaktor enzim ATPase miosin — diperlukan agar ATP dapat terhidrolisis dan menghasilkan energi untuk kontraksi."},
        ]
    },
    "🧠 Otak & Saraf": {
        "deskripsi": "Sistem saraf terdiri dari otak, sumsum tulang belakang, dan jaringan saraf yang mengatur dan mengoordinasikan seluruh fungsi tubuh.",
        "unsur": [
            {"simbol": "O",  "persen": 65.0, "fungsi": "Otak mengonsumsi ~20% oksigen tubuh meski hanya 2% dari berat tubuh — dibutuhkan untuk metabolisme glukosa neuron."},
            {"simbol": "C",  "persen": 18.0, "fungsi": "Menyusun lipid mielin yang melapisi akson saraf, serta neurotransmiter dan reseptor protein di sinaps."},
            {"simbol": "H",  "persen": 10.0, "fungsi": "Komponen utama air dan seluruh molekul organik pembentuk jaringan otak termasuk fosfolipid membran sel saraf."},
            {"simbol": "N",  "persen": 3.0,  "fungsi": "Menyusun neurotransmiter seperti dopamin, serotonin, GABA, dan glutamat yang mengirimkan sinyal antar neuron."},
            {"simbol": "P",  "persen": 1.1,  "fungsi": "Komponen fosfolipid pada membran sel saraf (mielin) dan terlibat dalam ATP untuk transmisi sinyal saraf."},
            {"simbol": "Na", "persen": 0.15, "fungsi": "Ion natrium masuk ke dalam sel saraf saat depolarisasi, memicu potensial aksi untuk transmisi impuls."},
            {"simbol": "K",  "persen": 0.35, "fungsi": "Ion kalium keluar saat repolarisasi, mengembalikan potensial membran neuron ke kondisi istirahat."},
            {"simbol": "I",  "persen": 0.00002, "fungsi": "Hormon tiroid yang mengandung iodin berperan krusial dalam perkembangan otak janin dan fungsi kognitif."},
        ]
    },
    "🫁 Paru-paru": {
        "deskripsi": "Paru-paru adalah organ pernapasan yang memfasilitasi pertukaran gas antara udara dan darah — mengambil oksigen dan membuang karbon dioksida.",
        "unsur": [
            {"simbol": "O",  "persen": 65.0, "fungsi": "Gas oksigen diserap dari udara melalui alveolus masuk ke kapiler darah untuk didistribusikan ke seluruh tubuh."},
            {"simbol": "C",  "persen": 18.0, "fungsi": "Menyusun surfaktan paru (fosfolipid) yang melapisi alveolus mencegah kolaps, serta CO₂ sebagai produk buangan."},
            {"simbol": "H",  "persen": 10.0, "fungsi": "Komponen air dalam lapisan cairan tipis alveolus yang memudahkan difusi gas antara udara dan darah."},
            {"simbol": "N",  "persen": 3.0,  "fungsi": "Menyusun protein elastin dan kolagen pada jaringan paru yang memberikan elastisitas untuk pengembangan dan pengempisan."},
            {"simbol": "Ca", "persen": 0.1,  "fungsi": "Berperan dalam regulasi tonus otot polos bronkus dan sekresi mukus pada saluran pernapasan."},
        ]
    },
    "🫀 Jantung": {
        "deskripsi": "Jantung adalah organ otot berongga yang memompa darah ke seluruh tubuh melalui sistem peredaran darah secara terus-menerus sepanjang hidup.",
        "unsur": [
            {"simbol": "O",  "persen": 65.0, "fungsi": "Jantung membutuhkan pasokan oksigen konstan melalui arteri koroner untuk mempertahankan kontraksi yang berkelanjutan."},
            {"simbol": "C",  "persen": 18.0, "fungsi": "Menyusun protein kontraktil (aktin, miosin) dan membran sel kardiomiosit yang melakukan kontraksi berirama."},
            {"simbol": "H",  "persen": 10.0, "fungsi": "Komponen air intraseluler kardiomiosit dan seluruh biomolekul yang terlibat dalam metabolisme sel otot jantung."},
            {"simbol": "N",  "persen": 3.0,  "fungsi": "Menyusun protein struktural dan enzim dalam kardiomiosit termasuk troponin — penanda kerusakan otot jantung."},
            {"simbol": "K",  "persen": 0.35, "fungsi": "Mengatur ritme jantung — ketidakseimbangan kalium (hipokalemia/hiperkalemia) dapat menyebabkan aritmia berbahaya."},
            {"simbol": "Ca", "persen": 0.1,  "fungsi": "Ion kalsium memicu setiap kontraksi jantung melalui mekanisme kalsium-induced calcium release dari retikulum sarkoplasma."},
            {"simbol": "Fe", "persen": 0.004,"fungsi": "Komponen mioglobin otot jantung yang menyimpan oksigen lokal untuk kebutuhan energi kontraksi miokardium."},
        ]
    },
    "🦷 Kulit": {
        "deskripsi": "Kulit adalah organ terbesar tubuh manusia yang berfungsi sebagai pelindung fisik, termoregulasi, sensoris, dan sintesis vitamin D.",
        "unsur": [
            {"simbol": "O",  "persen": 65.0, "fungsi": "Terdapat dalam semua biomolekul kulit termasuk kolagen, elastin, keratin, dan cairan interstisial dermis."},
            {"simbol": "C",  "persen": 18.0, "fungsi": "Menyusun keratin (protein pelindung epidermis), kolagen dan elastin (dermis), serta lipid pelindung pada stratum korneum."},
            {"simbol": "H",  "persen": 10.0, "fungsi": "Komponen air yang menjaga kelembapan dan turgor kulit, serta menyusun seluruh protein struktural kulit."},
            {"simbol": "N",  "persen": 3.0,  "fungsi": "Menyusun asam amino dalam keratin, kolagen, dan elastin yang memberikan kekuatan dan elastisitas pada kulit."},
            {"simbol": "S",  "persen": 0.3,  "fungsi": "Terdapat dalam asam amino sistein — membentuk ikatan disulfida yang mengunci struktur keratin sehingga kulit tahan air."},
            {"simbol": "Zn", "persen": 0.002,"fungsi": "Kofaktor enzim superoksida dismutase yang melindungi kulit dari radikal bebas, serta mendukung penyembuhan luka."},
        ]
    },
}

BENDA_SEHARI = {
    "💧 Air (H₂O)": {
        "rumus": "H₂O",
        "deskripsi": "Air adalah senyawa paling melimpah di bumi dan pelarut universal yang menopang seluruh kehidupan. Tubuh manusia terdiri dari 60–70% air.",
        "unsur": [{"simbol": "H", "jumlah": 2}, {"simbol": "O", "jumlah": 1}],
        "fakta": "Air memiliki tegangan permukaan tinggi akibat ikatan hidrogen antar molekulnya, memungkinkan serangga berjalan di atas air."
    },
    "🧂 Garam Dapur (NaCl)": {
        "rumus": "NaCl",
        "deskripsi": "Natrium klorida adalah senyawa ionik yang digunakan sebagai bumbu dan pengawet makanan sejak ribuan tahun lalu. Konsumsi berlebihan meningkatkan risiko hipertensi.",
        "unsur": [{"simbol": "Na", "jumlah": 1}, {"simbol": "Cl", "jumlah": 1}],
        "fakta": "Garam laut mengandung lebih dari 80 jenis mineral selain NaCl murni, termasuk magnesium dan kalsium."
    },
    "🪟 Kaca (SiO₂)": {
        "rumus": "SiO₂",
        "deskripsi": "Silikon dioksida atau kuarsa adalah bahan utama pembuatan kaca. Kaca terbentuk dari SiO₂ yang dicairkan pada suhu ~1700°C kemudian didinginkan tanpa membentuk kristal.",
        "unsur": [{"simbol": "Si", "jumlah": 1}, {"simbol": "O", "jumlah": 2}],
        "fakta": "Pasir pantai sebagian besar adalah SiO₂. Kaca bersifat amorf (bukan kristal) sehingga secara teknis dianggap cairan super-dingin."
    },
    "🔩 Baja (Fe + C)": {
        "rumus": "Fe-C",
        "deskripsi": "Baja adalah paduan logam antara besi dan karbon (0,02–2,14% karbon). Baja struktural mengandung Cr dan Ni untuk meningkatkan ketahanan terhadap korosi.",
        "unsur": [
            {"simbol": "Fe", "jumlah": 1},
            {"simbol": "C",  "jumlah": None},
            {"simbol": "Cr", "jumlah": None},
            {"simbol": "Ni", "jumlah": None},
        ],
        "fakta": "Menara Eiffel terbuat dari besi tempa (bukan baja). Baja nirkarat (stainless steel) mengandung minimal 10,5% kromium yang membentuk lapisan oksida pelindung."
    },
    "🥄 Aluminium Foil (Al)": {
        "rumus": "Al",
        "deskripsi": "Aluminium adalah logam ringan yang secara alami terlindungi lapisan oksida tipis (Al₂O₃). Digunakan untuk pembungkus makanan, pesawat, hingga kaleng minuman.",
        "unsur": [{"simbol": "Al", "jumlah": 1}],
        "fakta": "Aluminium adalah unsur logam paling melimpah di kerak bumi (~8%). Daur ulang aluminium hanya membutuhkan 5% energi dibanding produksi dari bijih bauksit."
    },
    "🪥 Pasta Gigi (CaF₂ / NaF)": {
        "rumus": "NaF / CaF₂",
        "deskripsi": "Pasta gigi mengandung fluorida (NaF atau CaF₂) yang memperkuat enamel gigi dengan membentuk fluorapatit yang lebih tahan terhadap asam bakteri.",
        "unsur": [
            {"simbol": "Ca", "jumlah": 1},
            {"simbol": "F",  "jumlah": 2},
            {"simbol": "Na", "jumlah": 1},
        ],
        "fakta": "Fluorida bereaksi dengan hidroksiapatit gigi membentuk fluorapatit yang 10 kali lebih tahan terhadap asam dibanding enamel biasa."
    },
    "🧪 Baking Soda (NaHCO₃)": {
        "rumus": "NaHCO₃",
        "deskripsi": "Natrium bikarbonat adalah senyawa yang digunakan sebagai pengembang kue, penghilang bau, dan antasida. Ketika dipanaskan atau bertemu asam, ia melepas CO₂.",
        "unsur": [
            {"simbol": "Na", "jumlah": 1},
            {"simbol": "H",  "jumlah": 1},
            {"simbol": "C",  "jumlah": 1},
            {"simbol": "O",  "jumlah": 3},
        ],
        "fakta": "Reaksi NaHCO₃ + asam asetat (cuka) menghasilkan gelembung CO₂ — efek yang dimanfaatkan dalam percobaan gunung berapi mainan."
    },
    "🥫 Kaleng Minuman (Al + Sn)": {
        "rumus": "Al / Sn",
        "deskripsi": "Kaleng minuman modern terbuat dari aluminium. Kaleng makanan tradisional menggunakan baja berlapis timah (tin-plate) untuk mencegah korosi dan kontaminasi.",
        "unsur": [
            {"simbol": "Al", "jumlah": 1},
            {"simbol": "Sn", "jumlah": None},
            {"simbol": "Fe", "jumlah": None},
        ],
        "fakta": "Lapisan timah pada kaleng makanan hanya setebal 0,0003 mm, namun cukup untuk mencegah reaksi antara baja dan isi makanan selama bertahun-tahun."
    },
}

# ──────────────────────────────────────────────
# FUNGSI BANTU
# ──────────────────────────────────────────────

WARNA_GOLONGAN = {
    "Logam Alkali":          "#FFA07A",
    "Logam Alkali Tanah":    "#FFD700",
    "Logam Transisi":        "#87CEEB",
    "Logam Pasca-Transisi":  "#90EE90",
    "Metaloid":              "#DDA0DD",
    "Non-Logam":             "#98FB98",
    "Halogen":               "#FFB6C1",
    "Gas Mulia":             "#E6E6FA",
}

def hitung_bobot_molekul(unsur_list):
    """Hitung bobot molekul dari list {simbol, jumlah}."""
    total = 0.0
    rincian = []
    for item in unsur_list:
        s = item["simbol"]
        n = item.get("jumlah")
        if n is None or s not in ELEMENT_INFO:
            continue
        massa = ELEMENT_INFO[s]["massa"]
        kontribusi = massa * n
        total += kontribusi
        rincian.append((s, ELEMENT_INFO[s]["nama"], massa, n, kontribusi))
    return total, rincian

def kartu_unsur(simbol, info_tambahan="", persen=None):
    """Tampilkan kartu kecil info unsur."""
    if simbol not in ELEMENT_INFO:
        return
    el = ELEMENT_INFO[simbol]
    warna = WARNA_GOLONGAN.get(el["golongan"], "#EEEEEE")
    label_persen = f"<br><span style='font-size:12px;color:#555;'>{persen:.3f}%</span>" if persen is not None else ""
    st.markdown(f"""
    <div style="
        background:{warna}22;
        border:1.5px solid {warna};
        border-radius:10px;
        padding:10px 14px;
        margin-bottom:6px;
    ">
        <span style="font-size:22px;font-weight:bold;">{simbol}</span>
        <span style="font-size:14px;color:#444;margin-left:8px;">{el['nama']}</span>
        {label_persen}
        <span style="float:right;font-size:11px;background:{warna};padding:2px 7px;border-radius:12px;">{el['golongan']}</span>
        <br>
        <span style="font-size:12px;color:#555;">
            No. Atom: <b>{el['nomor']}</b> &nbsp;|&nbsp;
            Massa: <b>{el['massa']} u</b>
        </span>
        {'<br><span style="font-size:12px;color:#333;margin-top:4px;display:block;">'+info_tambahan+'</span>' if info_tambahan else ''}
    </div>
    """, unsafe_allow_html=True)


# ──────────────────────────────────────────────
# HALAMAN UTAMA
# ──────────────────────────────────────────────

def show():
    st.title("🌍 Unsur di Sekitar & Dalam Dirimu")
    st.markdown(
        "Jelajahi unsur-unsur kimia yang menyusun **tubuh manusia** dan **benda-benda sehari-hari** di sekitarmu."
    )

    tab1, tab2 = st.tabs(["🫀 Tubuh Manusia", "🏠 Benda Sehari-hari"])

    # ════════════════════════════════
    # TAB 1 — TUBUH MANUSIA
    # ════════════════════════════════
    with tab1:
        st.subheader("Unsur Penyusun Tubuh Manusia")
        st.markdown(
            "Pilih bagian tubuh untuk melihat unsur-unsur kimia penyusunnya beserta fungsi biologisnya."
        )

        pilihan_bagian = st.selectbox(
            "Pilih bagian tubuh:",
            list(BAGIAN_TUBUH.keys()),
            key="bagian_tubuh"
        )

        data = BAGIAN_TUBUH[pilihan_bagian]

        st.info(data["deskripsi"])

        st.markdown("#### 🔬 Unsur Penyusun")

        for item in data["unsur"]:
            kartu_unsur(item["simbol"], info_tambahan=item["fungsi"], persen=item["persen"])

        # Grafik persentase
        st.markdown("#### 📊 Komposisi Persentase")
        import pandas as pd
        df_chart = pd.DataFrame([
            {
                "Unsur": f"{ELEMENT_INFO[i['simbol']]['nama']} ({i['simbol']})",
                "Persentase (%)": i["persen"]
            }
            for i in data["unsur"] if i["simbol"] in ELEMENT_INFO
        ]).sort_values("Persentase (%)", ascending=False)

        st.bar_chart(df_chart.set_index("Unsur"), use_container_width=True)

    # ════════════════════════════════
    # TAB 2 — BENDA SEHARI-HARI
    # ════════════════════════════════
    with tab2:
        st.subheader("Unsur dalam Benda Sehari-hari")
        st.markdown(
            "Pilih benda untuk melihat unsur-unsur penyusunnya dan menghitung bobot molekulnya."
        )

        pilihan_benda = st.selectbox(
            "Pilih benda:",
            list(BENDA_SEHARI.keys()),
            key="benda_sehari"
        )

        benda = BENDA_SEHARI[pilihan_benda]

        col_info, col_rumus = st.columns([3, 1])
        with col_info:
            st.info(benda["deskripsi"])
        with col_rumus:
            st.markdown(f"""
            <div style="
                text-align:center;
                background:#f0f4ff;
                border:2px solid #4A90D9;
                border-radius:12px;
                padding:18px 10px;
                margin-top:4px;
            ">
                <div style="font-size:13px;color:#555;">Rumus Kimia</div>
                <div style="font-size:28px;font-weight:bold;color:#1a1a2e;">{benda['rumus']}</div>
            </div>
            """, unsafe_allow_html=True)

        # Hitung bobot molekul
        bm, rincian = hitung_bobot_molekul(benda["unsur"])

        if bm > 0:
            st.markdown("#### ⚖️ Perhitungan Bobot Molekul")

            # Tampilkan tabel perhitungan
            import pandas as pd
            df_bm = pd.DataFrame([
                {
                    "Simbol": r[0],
                    "Nama Unsur": r[1],
                    "Massa Atom (u)": r[2],
                    "Jumlah Atom": int(r[3]),
                    "Kontribusi (u)": round(r[4], 4)
                }
                for r in rincian
            ])
            st.dataframe(df_bm, use_container_width=True, hide_index=True)

            st.markdown(f"""
            <div style="
                background:#e8f5e9;
                border:2px solid #43A047;
                border-radius:10px;
                padding:14px 20px;
                font-size:18px;
                font-weight:bold;
                color:#1B5E20;
                margin-top:8px;
            ">
                ⚖️ Bobot Molekul {benda['rumus']} = <span style="font-size:24px;">{bm:.4f} g/mol</span>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("#### 🔬 Detail Unsur Penyusun")
        for item in benda["unsur"]:
            kartu_unsur(item["simbol"])

        st.markdown("#### 💡 Fakta Menarik")
        st.success(f"**{pilihan_benda}** — {benda['fakta']}")


# ──────────────────────────────────────────────
# ENTRY POINT (jika dijalankan langsung)
# ──────────────────────────────────────────────
if __name__ == "__main__":
    st.set_page_config(page_title="Unsur Kehidupan", page_icon="🌍", layout="wide")
    show()
