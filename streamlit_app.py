import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Tabel Periodik Unsur Kimia",
    layout="wide",
    page_icon="⚗️",
    initial_sidebar_state="collapsed"
)

# ============================================================
# DATA UNSUR KIMIA (Golongan 1A - 8A)
# ============================================================
ELEMENTS = [
    # === GOLONGAN 1A (Logam Alkali + Hidrogen) ===
    {"symbol": "H",  "name": "Hidrogen",    "atomic_number": 1,   "group": "1A", "period": 1,
     "atomic_mass": 1.008,    "boiling_point": -252.9, "melting_point": -259.1,
     "density": 0.0000899,  "oxidation_states": "+1, -1",                "electron_config": "1s¹"},
    {"symbol": "Li", "name": "Litium",      "atomic_number": 3,   "group": "1A", "period": 2,
     "atomic_mass": 6.941,    "boiling_point": 1342,   "melting_point": 180.5,
     "density": 0.534,      "oxidation_states": "+1",                    "electron_config": "[He] 2s¹"},
    {"symbol": "Na", "name": "Natrium",     "atomic_number": 11,  "group": "1A", "period": 3,
     "atomic_mass": 22.990,   "boiling_point": 883,    "melting_point": 97.8,
     "density": 0.971,      "oxidation_states": "+1",                    "electron_config": "[Ne] 3s¹"},
    {"symbol": "K",  "name": "Kalium",      "atomic_number": 19,  "group": "1A", "period": 4,
     "atomic_mass": 39.098,   "boiling_point": 759,    "melting_point": 63.5,
     "density": 0.862,      "oxidation_states": "+1",                    "electron_config": "[Ar] 4s¹"},
    {"symbol": "Rb", "name": "Rubidium",    "atomic_number": 37,  "group": "1A", "period": 5,
     "atomic_mass": 85.468,   "boiling_point": 688,    "melting_point": 39.3,
     "density": 1.532,      "oxidation_states": "+1",                    "electron_config": "[Kr] 5s¹"},
    {"symbol": "Cs", "name": "Sesium",      "atomic_number": 55,  "group": "1A", "period": 6,
     "atomic_mass": 132.905,  "boiling_point": 671,    "melting_point": 28.5,
     "density": 1.873,      "oxidation_states": "+1",                    "electron_config": "[Xe] 6s¹"},
    {"symbol": "Fr", "name": "Fransium",    "atomic_number": 87,  "group": "1A", "period": 7,
     "atomic_mass": 223.0,    "boiling_point": 677,    "melting_point": 27.0,
     "density": 1.87,       "oxidation_states": "+1",                    "electron_config": "[Rn] 7s¹"},

    # === GOLONGAN 2A (Logam Alkali Tanah) ===
    {"symbol": "Be", "name": "Berilium",    "atomic_number": 4,   "group": "2A", "period": 2,
     "atomic_mass": 9.012,    "boiling_point": 2470,   "melting_point": 1287,
     "density": 1.848,      "oxidation_states": "+2",                    "electron_config": "[He] 2s²"},
    {"symbol": "Mg", "name": "Magnesium",   "atomic_number": 12,  "group": "2A", "period": 3,
     "atomic_mass": 24.305,   "boiling_point": 1090,   "melting_point": 650,
     "density": 1.738,      "oxidation_states": "+2",                    "electron_config": "[Ne] 3s²"},
    {"symbol": "Ca", "name": "Kalsium",     "atomic_number": 20,  "group": "2A", "period": 4,
     "atomic_mass": 40.078,   "boiling_point": 1484,   "melting_point": 842,
     "density": 1.55,       "oxidation_states": "+2",                    "electron_config": "[Ar] 4s²"},
    {"symbol": "Sr", "name": "Stronsium",   "atomic_number": 38,  "group": "2A", "period": 5,
     "atomic_mass": 87.62,    "boiling_point": 1377,   "melting_point": 777,
     "density": 2.64,       "oxidation_states": "+2",                    "electron_config": "[Kr] 5s²"},
    {"symbol": "Ba", "name": "Barium",      "atomic_number": 56,  "group": "2A", "period": 6,
     "atomic_mass": 137.327,  "boiling_point": 1870,   "melting_point": 727,
     "density": 3.594,      "oxidation_states": "+2",                    "electron_config": "[Xe] 6s²"},
    {"symbol": "Ra", "name": "Radium",      "atomic_number": 88,  "group": "2A", "period": 7,
     "atomic_mass": 226.0,    "boiling_point": 1737,   "melting_point": 700,
     "density": 5.5,        "oxidation_states": "+2",                    "electron_config": "[Rn] 7s²"},

    # === GOLONGAN 3B (Logam Transisi) ===
    {"symbol": "Sc", "name": "Skandium", "atomic_number": 21, "gruop": "3B", "period": 4,
    "atomic_mass": 44.956,   "boiling_point": 2730,   "melting_point": 1539,
     "density": 3.0,       "oxidation_states": "+3", "electron_config": "[Ar] 3d¹ 4s²"},

    # === GOLONGAN 3A (Golongan Boron) ===
    {"symbol": "B",  "name": "Boron",       "atomic_number": 5,   "group": "3A", "period": 2,
     "atomic_mass": 10.811,   "boiling_point": 2550,   "melting_point": 2075,
     "density": 2.37,       "oxidation_states": "+3",                    "electron_config": "[He] 2s² 2p¹"},
    {"symbol": "Al", "name": "Aluminium",   "atomic_number": 13,  "group": "3A", "period": 3,
     "atomic_mass": 26.982,   "boiling_point": 2519,   "melting_point": 660.3,
     "density": 2.698,      "oxidation_states": "+3",                    "electron_config": "[Ne] 3s² 3p¹"},
    {"symbol": "Ga", "name": "Galium",      "atomic_number": 31,  "group": "3A", "period": 4,
     "atomic_mass": 69.723,   "boiling_point": 2204,   "melting_point": 29.8,
     "density": 5.907,      "oxidation_states": "+3, +1",               "electron_config": "[Ar] 3d¹⁰ 4s² 4p¹"},
    {"symbol": "In", "name": "Indium",      "atomic_number": 49,  "group": "3A", "period": 5,
     "atomic_mass": 114.818,  "boiling_point": 2072,   "melting_point": 156.6,
     "density": 7.31,       "oxidation_states": "+3, +1",               "electron_config": "[Kr] 4d¹⁰ 5s² 5p¹"},
    {"symbol": "Tl", "name": "Talium",      "atomic_number": 81,  "group": "3A", "period": 6,
     "atomic_mass": 204.383,  "boiling_point": 1473,   "melting_point": 304,
     "density": 11.85,      "oxidation_states": "+3, +1",               "electron_config": "[Xe] 4f¹⁴ 5d¹⁰ 6s² 6p¹"},
    {"symbol": "Nh", "name": "Nihonium",    "atomic_number": 113, "group": "3A", "period": 7,
     "atomic_mass": 286.0,    "boiling_point": 1130,   "melting_point": 430,
     "density": 16.0,       "oxidation_states": "+3, +1",               "electron_config": "[Rn] 5f¹⁴ 6d¹⁰ 7s² 7p¹"},

    # === GOLONGAN 4A (Golongan Karbon) ===
    {"symbol": "C",  "name": "Karbon",      "atomic_number": 6,   "group": "4A", "period": 2,
     "atomic_mass": 12.011,   "boiling_point": 4027,   "melting_point": 3642,
     "density": 2.267,      "oxidation_states": "+4, +2, -4",           "electron_config": "[He] 2s² 2p²"},
    {"symbol": "Si", "name": "Silikon",     "atomic_number": 14,  "group": "4A", "period": 3,
     "atomic_mass": 28.086,   "boiling_point": 3265,   "melting_point": 1414,
     "density": 2.329,      "oxidation_states": "+4, -4",               "electron_config": "[Ne] 3s² 3p²"},
    {"symbol": "Ge", "name": "Germanium",   "atomic_number": 32,  "group": "4A", "period": 4,
     "atomic_mass": 72.630,   "boiling_point": 2833,   "melting_point": 938.3,
     "density": 5.323,      "oxidation_states": "+4, +2",               "electron_config": "[Ar] 3d¹⁰ 4s² 4p²"},
    {"symbol": "Sn", "name": "Timah",       "atomic_number": 50,  "group": "4A", "period": 5,
     "atomic_mass": 118.710,  "boiling_point": 2602,   "melting_point": 231.9,
     "density": 7.265,      "oxidation_states": "+4, +2",               "electron_config": "[Kr] 4d¹⁰ 5s² 5p²"},
    {"symbol": "Pb", "name": "Timbal",      "atomic_number": 82,  "group": "4A", "period": 6,
     "atomic_mass": 207.2,    "boiling_point": 1749,   "melting_point": 327.5,
     "density": 11.34,      "oxidation_states": "+4, +2",               "electron_config": "[Xe] 4f¹⁴ 5d¹⁰ 6s² 6p²"},
    {"symbol": "Fl", "name": "Flerovium",   "atomic_number": 114, "group": "4A", "period": 7,
     "atomic_mass": 289.0,    "boiling_point": 210,    "melting_point": -73,
     "density": 14.0,       "oxidation_states": "+4, +2",               "electron_config": "[Rn] 5f¹⁴ 6d¹⁰ 7s² 7p²"},

    # === GOLONGAN 5A (Golongan Nitrogen) ===
    {"symbol": "N",  "name": "Nitrogen",    "atomic_number": 7,   "group": "5A", "period": 2,
     "atomic_mass": 14.007,   "boiling_point": -195.8, "melting_point": -210,
     "density": 0.001251,   "oxidation_states": "+5, +3, -3",           "electron_config": "[He] 2s² 2p³"},
    {"symbol": "P",  "name": "Fosfor",      "atomic_number": 15,  "group": "5A", "period": 3,
     "atomic_mass": 30.974,   "boiling_point": 280.5,  "melting_point": 44.2,
     "density": 1.82,       "oxidation_states": "+5, +3, -3",           "electron_config": "[Ne] 3s² 3p³"},
    {"symbol": "As", "name": "Arsen",       "atomic_number": 33,  "group": "5A", "period": 4,
     "atomic_mass": 74.922,   "boiling_point": 887,    "melting_point": 817,
     "density": 5.727,      "oxidation_states": "+5, +3, -3",           "electron_config": "[Ar] 3d¹⁰ 4s² 4p³"},
    {"symbol": "Sb", "name": "Antimon",     "atomic_number": 51,  "group": "5A", "period": 5,
     "atomic_mass": 121.760,  "boiling_point": 1587,   "melting_point": 630.6,
     "density": 6.685,      "oxidation_states": "+5, +3, -3",           "electron_config": "[Kr] 4d¹⁰ 5s² 5p³"},
    {"symbol": "Bi", "name": "Bismut",      "atomic_number": 83,  "group": "5A", "period": 6,
     "atomic_mass": 208.980,  "boiling_point": 1564,   "melting_point": 271.5,
     "density": 9.807,      "oxidation_states": "+5, +3",               "electron_config": "[Xe] 4f¹⁴ 5d¹⁰ 6s² 6p³"},
    {"symbol": "Mc", "name": "Moscovium",   "atomic_number": 115, "group": "5A", "period": 7,
     "atomic_mass": 290.0,    "boiling_point": 1400,   "melting_point": 400,
     "density": 13.5,       "oxidation_states": "+3, +1",               "electron_config": "[Rn] 5f¹⁴ 6d¹⁰ 7s² 7p³"},

    # === GOLONGAN 6A (Kalkogen) ===
    {"symbol": "O",  "name": "Oksigen",     "atomic_number": 8,   "group": "6A", "period": 2,
     "atomic_mass": 15.999,   "boiling_point": -183,   "melting_point": -218.8,
     "density": 0.001429,   "oxidation_states": "-2, -1",               "electron_config": "[He] 2s² 2p⁴"},
    {"symbol": "S",  "name": "Sulfur",      "atomic_number": 16,  "group": "6A", "period": 3,
     "atomic_mass": 32.06,    "boiling_point": 444.6,  "melting_point": 115.2,
     "density": 2.067,      "oxidation_states": "+6, +4, -2",           "electron_config": "[Ne] 3s² 3p⁴"},
    {"symbol": "Se", "name": "Selenium",    "atomic_number": 34,  "group": "6A", "period": 4,
     "atomic_mass": 78.971,   "boiling_point": 685,    "melting_point": 221,
     "density": 4.819,      "oxidation_states": "+6, +4, -2",           "electron_config": "[Ar] 3d¹⁰ 4s² 4p⁴"},
    {"symbol": "Te", "name": "Telurium",    "atomic_number": 52,  "group": "6A", "period": 5,
     "atomic_mass": 127.60,   "boiling_point": 988,    "melting_point": 449.5,
     "density": 6.232,      "oxidation_states": "+6, +4, -2",           "electron_config": "[Kr] 4d¹⁰ 5s² 5p⁴"},
    {"symbol": "Po", "name": "Polonium",    "atomic_number": 84,  "group": "6A", "period": 6,
     "atomic_mass": 209.0,    "boiling_point": 962,    "melting_point": 254,
     "density": 9.196,      "oxidation_states": "+6, +4, +2, -2",       "electron_config": "[Xe] 4f¹⁴ 5d¹⁰ 6s² 6p⁴"},
    {"symbol": "Lv", "name": "Livermorium", "atomic_number": 116, "group": "6A", "period": 7,
     "atomic_mass": 293.0,    "boiling_point": 800,    "melting_point": 400,
     "density": 12.9,       "oxidation_states": "+4, +2, -2",           "electron_config": "[Rn] 5f¹⁴ 6d¹⁰ 7s² 7p⁴"},

    # === GOLONGAN 7A (Halogen) ===
    {"symbol": "F",  "name": "Fluor",       "atomic_number": 9,   "group": "7A", "period": 2,
     "atomic_mass": 18.998,   "boiling_point": -188.1, "melting_point": -219.7,
     "density": 0.001696,   "oxidation_states": "-1",                   "electron_config": "[He] 2s² 2p⁵"},
    {"symbol": "Cl", "name": "Klor",        "atomic_number": 17,  "group": "7A", "period": 3,
     "atomic_mass": 35.45,    "boiling_point": -34.1,  "melting_point": -100.98,
     "density": 0.003214,   "oxidation_states": "+7, +5, +3, +1, -1",  "electron_config": "[Ne] 3s² 3p⁵"},
    {"symbol": "Br", "name": "Brom",        "atomic_number": 35,  "group": "7A", "period": 4,
     "atomic_mass": 79.904,   "boiling_point": 59,     "melting_point": -7.2,
     "density": 3.122,      "oxidation_states": "+7, +5, +3, +1, -1",  "electron_config": "[Ar] 3d¹⁰ 4s² 4p⁵"},
    {"symbol": "I",  "name": "Iodin",       "atomic_number": 53,  "group": "7A", "period": 5,
     "atomic_mass": 126.904,  "boiling_point": 184.3,  "melting_point": 113.7,
     "density": 4.933,      "oxidation_states": "+7, +5, +1, -1",       "electron_config": "[Kr] 4d¹⁰ 5s² 5p⁵"},
    {"symbol": "At", "name": "Astatin",     "atomic_number": 85,  "group": "7A", "period": 6,
     "atomic_mass": 210.0,    "boiling_point": 337,    "melting_point": 302,
     "density": 7.0,        "oxidation_states": "+7, +5, +3, +1, -1",  "electron_config": "[Xe] 4f¹⁴ 5d¹⁰ 6s² 6p⁵"},
    {"symbol": "Ts", "name": "Tennesin",    "atomic_number": 117, "group": "7A", "period": 7,
     "atomic_mass": 294.0,    "boiling_point": 883,    "melting_point": 350,
     "density": 7.1,        "oxidation_states": "+5, +3, +1, -1",       "electron_config": "[Rn] 5f¹⁴ 6d¹⁰ 7s² 7p⁵"},

    # === GOLONGAN 8A (Gas Mulia) ===
    {"symbol": "He", "name": "Helium",      "atomic_number": 2,   "group": "8A", "period": 1,
     "atomic_mass": 4.003,    "boiling_point": -268.9, "melting_point": -272.2,
     "density": 0.0001785,  "oxidation_states": "0",                    "electron_config": "1s²"},
    {"symbol": "Ne", "name": "Neon",        "atomic_number": 10,  "group": "8A", "period": 2,
     "atomic_mass": 20.180,   "boiling_point": -246.1, "melting_point": -248.6,
     "density": 0.0009002,  "oxidation_states": "0",                    "electron_config": "[He] 2s² 2p⁶"},
    {"symbol": "Ar", "name": "Argon",       "atomic_number": 18,  "group": "8A", "period": 3,
     "atomic_mass": 39.948,   "boiling_point": -185.8, "melting_point": -189.4,
     "density": 0.001784,   "oxidation_states": "0",                    "electron_config": "[Ne] 3s² 3p⁶"},
    {"symbol": "Kr", "name": "Kripton",     "atomic_number": 36,  "group": "8A", "period": 4,
     "atomic_mass": 83.798,   "boiling_point": -153.2, "melting_point": -157.4,
     "density": 0.003733,   "oxidation_states": "0, +2",                "electron_config": "[Ar] 3d¹⁰ 4s² 4p⁶"},
    {"symbol": "Xe", "name": "Xenon",       "atomic_number": 54,  "group": "8A", "period": 5,
     "atomic_mass": 131.293,  "boiling_point": -108.1, "melting_point": -111.8,
     "density": 0.005894,   "oxidation_states": "0, +2, +4, +6, +8",   "electron_config": "[Kr] 4d¹⁰ 5s² 5p⁶"},
    {"symbol": "Rn", "name": "Radon",       "atomic_number": 86,  "group": "8A", "period": 6,
     "atomic_mass": 222.0,    "boiling_point": -61.7,  "melting_point": -71,
     "density": 0.00973,    "oxidation_states": "0, +2",                "electron_config": "[Xe] 4f¹⁴ 5d¹⁰ 6s² 6p⁶"},
    {"symbol": "Og", "name": "Oganesson",   "atomic_number": 118, "group": "8A", "period": 7,
     "atomic_mass": 294.0,    "boiling_point": 80,     "melting_point": 52,
     "density": 4.9,        "oxidation_states": "0, +2, +4, +6",        "electron_config": "[Rn] 5f¹⁴ 6d¹⁰ 7s² 7p⁶"},
]

# ============================================================
# KONFIGURASI WARNA & NAMA GOLONGAN
# ============================================================
GROUP_COLORS = {
    "1A": "#ef5350",   # Merah  - Alkali
    "2A": "#ff7043",   # Oranye - Alkali Tanah
    "3B": "#bababa",   # Silver - Logam Transisi
    "3A": "#fdd835",   # Kuning - Boron
    "4A": "#66bb6a",   # Hijau  - Karbon
    "5A": "#29b6f6",   # Biru   - Nitrogen
    "6A": "#ab47bc",   # Ungu   - Kalkogen
    "7A": "#26c6da",   # Cyan   - Halogen
    "8A": "#78909c",   # Abu    - Gas Mulia
}
GROUP_TEXT_COLORS = {
    "1A": "#fff", "2A": "#fff", "3A": "#222", "3B": "#222",
    "4A": "#fff", "5A": "#fff", "6A": "#fff",
    "7A": "#fff", "8A": "#fff",
}
GROUP_NAMES = {
    "1A": "Logam Alkali",
    "2A": "Logam Alkali Tanah",
    "3A": "Golongan Boron",
    "3B": "Logam Transisi"
    "4A": "Golongan Karbon",
    "5A": "Golongan Nitrogen",
    "6A": "Kalkogen",
    "7A": "Halogen",
    "8A": "Gas Mulia",
}

GROUPS  = ["1A", "2A", "3A", "3B", "4A", "5A", "6A", "7A", "8A"]
PERIODS = [1, 2, 3, 4, 5, 6, 7]

# Build lookup dict  {(period, group): element}
elem_by_pos = {(e["period"], e["group"]): e for e in ELEMENTS}

# ============================================================
# CSS GLOBAL
# ============================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Exo+2:wght@400;600;700;900&family=Source+Code+Pro:wght@400;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Exo 2', sans-serif;
}
.block-container { padding-top: 1.5rem !important; }

/* ---- HEADER ---- */
.pt-header {
    text-align: center;
    padding: 28px 20px 10px;
    background: linear-gradient(135deg, #0d1b2a 0%, #1b263b 60%, #142535 100%);
    border-radius: 16px;
    margin-bottom: 24px;
}
.pt-title {
    font-size: 2.6rem;
    font-weight: 900;
    letter-spacing: 2px;
    color: #e0f7fa;
    text-shadow: 0 0 30px #29b6f655;
    margin: 0;
}
.pt-subtitle {
    color: #90caf9;
    font-size: 1rem;
    margin-top: 6px;
    letter-spacing: 1px;
}

/* ---- LEGENDA ---- */
.legend-wrap { display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 20px; }
.legend-chip {
    padding: 5px 14px;
    border-radius: 20px;
    font-size: 0.78rem;
    font-weight: 700;
    letter-spacing: 0.5px;
    white-space: nowrap;
}

/* ---- TABEL PERIODIK ---- */
.pt-table { border-collapse: separate; border-spacing: 5px; width: 100%; }
.pt-table th {
    background: #1e2d40;
    color: #90caf9;
    text-align: center;
    font-size: 0.82rem;
    font-weight: 700;
    padding: 7px 4px;
    border-radius: 6px;
    letter-spacing: 1px;
}
.pt-table td { vertical-align: middle; }
.period-lbl {
    background: #1e2d40;
    color: #78909c;
    font-weight: 700;
    font-size: 0.78rem;
    text-align: center;
    padding: 6px 8px;
    border-radius: 6px;
    white-space: nowrap;
}
.elem-box {
    border-radius: 10px;
    padding: 7px 4px;
    width: 82px;
    min-height: 72px;
    display: inline-flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    cursor: default;
    transition: transform 0.15s, box-shadow 0.15s;
    box-shadow: 0 2px 8px rgba(0,0,0,0.25);
}
.elem-box:hover {
    transform: translateY(-3px) scale(1.06);
    box-shadow: 0 6px 20px rgba(0,0,0,0.4);
    z-index: 10;
    position: relative;
}
.e-num  { font-size: 0.65rem; font-weight: 600; opacity: 0.75; margin-bottom: 1px; }
.e-sym  { font-size: 1.5rem; font-weight: 900; line-height: 1.1; letter-spacing: -0.5px; }
.e-name { font-size: 0.55rem; font-weight: 600; opacity: 0.82; margin-top: 2px; }
.e-mass { font-size: 0.55rem; opacity: 0.70; font-family: 'Source Code Pro', monospace; }

/* ---- KARTU DETAIL ---- */
.detail-card {
    border-radius: 16px;
    padding: 24px;
    margin-bottom: 16px;
    box-shadow: 0 8px 32px rgba(0,0,0,0.25);
}
.dc-symbol { font-size: 5rem; font-weight: 900; line-height: 1; text-shadow: 0 2px 12px rgba(0,0,0,0.2); }
.dc-name   { font-size: 1.5rem; font-weight: 700; margin-top: 4px; }
.dc-badge  {
    display: inline-block;
    background: rgba(255,255,255,0.25);
    border-radius: 20px;
    padding: 3px 14px;
    font-size: 0.8rem;
    font-weight: 600;
    margin-top: 8px;
}
.info-grid2 { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-top: 16px; }
.info-chip {
    background: rgba(255,255,255,0.2);
    border-radius: 10px;
    padding: 10px 12px;
    backdrop-filter: blur(4px);
}
.ic-label { font-size: 0.65rem; font-weight: 600; opacity: 0.75; margin-bottom: 3px; text-transform: uppercase; letter-spacing: 0.5px; }
.ic-value { font-size: 0.9rem; font-weight: 700; font-family: 'Source Code Pro', monospace; }

/* ---- TABEL DATA ---- */
.stDataFrame { border-radius: 10px; overflow: hidden; }

/* ---- FOOTER ---- */
.pt-footer {
    text-align: center;
    color: #546e7a;
    font-size: 0.78rem;
    padding: 16px;
    margin-top: 20px;
    border-top: 1px solid #1e2d40;
}
</style>
""", unsafe_allow_html=True)

# ============================================================
# HEADER
# ============================================================
st.markdown("""
<div class="pt-header">
    <div class="pt-title">⚗️ TABEL PERIODIK UNSUR KIMIA</div>
    <div class="pt-subtitle">Golongan 1A – 8A &nbsp;|&nbsp; Golongan Utama (Main Group Elements)</div>
</div>
""", unsafe_allow_html=True)

# ============================================================
# LEGENDA
# ============================================================
st.markdown("#### 🎨 Legenda Golongan")
legend_html = '<div class="legend-wrap">'
for g, gname in GROUP_NAMES.items():
    bg  = GROUP_COLORS[g]
    txt = GROUP_TEXT_COLORS[g]
    legend_html += f'<span class="legend-chip" style="background:{bg};color:{txt};">{g} — {gname}</span>'
legend_html += "</div>"
st.markdown(legend_html, unsafe_allow_html=True)

# ============================================================
# TABEL PERIODIK VISUAL
# ============================================================
st.markdown("#### 🗂️ Tampilan Tabel Periodik")

html = '<table class="pt-table"><thead><tr><th>Period</th>'
for g in GROUPS:
    html += f"<th>{g}</th>"
html += "</tr></thead><tbody>"

for p in PERIODS:
    html += f'<tr><td><div class="period-lbl">P {p}</div></td>'
    for g in GROUPS:
        elem = elem_by_pos.get((p, g))
        if elem:
            bg  = GROUP_COLORS[g]
            txt = GROUP_TEXT_COLORS[g]
            html += f"""
            <td>
              <div class="elem-box" style="background:{bg};color:{txt};"
                   title="{elem['name']} | No.Atom: {elem['atomic_number']} | Massa: {elem['atomic_mass']} u">
                <div class="e-num">{elem['atomic_number']}</div>
                <div class="e-sym">{elem['symbol']}</div>
                <div class="e-name">{elem['name']}</div>
                <div class="e-mass">{elem['atomic_mass']}</div>
              </div>
            </td>"""
        else:
            html += '<td></td>'
    html += "</tr>"

html += "</tbody></table>"
st.markdown(html, unsafe_allow_html=True)

st.markdown("---")

# ============================================================
# DETAIL UNSUR
# ============================================================
st.markdown("#### 🔍 Detail Unsur")

col_sel, col_detail = st.columns([1, 2], gap="large")

with col_sel:
    sel_group = st.selectbox("🔬 Pilih Golongan:", GROUPS,
                              format_func=lambda g: f"{g} — {GROUP_NAMES[g]}")
    grp_elems  = [e for e in ELEMENTS if e["group"] == sel_group]
    elem_labels = [f"{e['symbol']}  ({e['name']})" for e in grp_elems]
    sel_idx = st.selectbox("⚛️ Pilih Unsur:", range(len(elem_labels)),
                            format_func=lambda i: elem_labels[i])
    el = grp_elems[sel_idx]
    
    # Mini info tambahan
    st.info(f"**Periode:** {el['period']}  |  **Nomor Atom:** {el['atomic_number']}")

with col_detail:
    bg  = GROUP_COLORS[el["group"]]
    txt = GROUP_TEXT_COLORS[el["group"]]
    gn  = GROUP_NAMES[el["group"]]

    card = f"""
    <div class="detail-card" style="background:linear-gradient(135deg,{bg}dd,{bg}99);color:{txt};">
      <div style="text-align:center;margin-bottom:14px;">
        <div class="dc-symbol">{el['symbol']}</div>
        <div class="dc-name">{el['name']}</div>
        <div class="dc-badge">{el['group']} &bull; {gn} &bull; Periode {el['period']}</div>
      </div>
      <div class="info-grid2">
        <div class="info-chip">
          <div class="ic-label">⚛️ Nomor Atom</div>
          <div class="ic-value">{el['atomic_number']}</div>
        </div>
        <div class="info-chip">
          <div class="ic-label">⚖️ Massa Atom</div>
          <div class="ic-value">{el['atomic_mass']} u</div>
        </div>
        <div class="info-chip">
          <div class="ic-label">🌡️ Titik Didih</div>
          <div class="ic-value">{el['boiling_point']} °C</div>
        </div>
        <div class="info-chip">
          <div class="ic-label">❄️ Titik Leleh</div>
          <div class="ic-value">{el['melting_point']} °C</div>
        </div>
        <div class="info-chip">
          <div class="ic-label">⚗️ Massa Jenis</div>
          <div class="ic-value">{el['density']} g/cm³</div>
        </div>
        <div class="info-chip">
          <div class="ic-label">⚡ Tingkat Oksidasi</div>
          <div class="ic-value" style="font-size:0.78rem;">{el['oxidation_states']}</div>
        </div>
        <div class="info-chip" style="grid-column: span 2;">
          <div class="ic-label">🔬 Struktur Elektron (Konfigurasi)</div>
          <div class="ic-value">{el['electron_config']}</div>
        </div>
      </div>
    </div>
    """
    st.markdown(card, unsafe_allow_html=True)

st.markdown("---")

# ============================================================
# TABEL DATA LENGKAP
# ============================================================
st.markdown("#### 📊 Tabel Data Lengkap Semua Unsur")

filter_groups = st.multiselect(
    "Filter berdasarkan Golongan:",
    options=GROUPS,
    default=GROUPS,
    format_func=lambda g: f"{g} ({GROUP_NAMES[g]})"
)

filtered = [e for e in ELEMENTS if e["group"] in filter_groups]
df = pd.DataFrame(filtered)
df = df.rename(columns={
    "symbol":           "Lambang",
    "name":             "Nama Unsur",
    "atomic_number":    "No. Atom",
    "group":            "Golongan",
    "period":           "Periode",
    "atomic_mass":      "Massa Atom (u)",
    "boiling_point":    "Titik Didih (°C)",
    "melting_point":    "Titik Leleh (°C)",
    "density":          "Massa Jenis (g/cm³)",
    "oxidation_states": "Tingkat Oksidasi",
    "electron_config":  "Struktur Elektron",
})
df = df[["No. Atom", "Lambang", "Nama Unsur", "Golongan", "Periode",
         "Massa Atom (u)", "Titik Didih (°C)", "Titik Leleh (°C)",
         "Massa Jenis (g/cm³)", "Tingkat Oksidasi", "Struktur Elektron"]]
df = df.sort_values("No. Atom").reset_index(drop=True)

st.dataframe(df, use_container_width=True, height=430)

csv_data = df.to_csv(index=False).encode("utf-8")
st.download_button(
    label="⬇️ Unduh Data sebagai CSV",
    data=csv_data,
    file_name="tabel_periodik_golongan_A.csv",
    mime="text/csv"
)

# ============================================================
# FOOTER
# ============================================================
st.markdown("""
<div class="pt-footer">
    ⚗️ Tabel Periodik Golongan Utama (1A – 8A) &nbsp;|&nbsp; Data berdasarkan IUPAC &nbsp;|&nbsp;
    Dibuat dengan Streamlit & Python
</div>
""", unsafe_allow_html=True)
