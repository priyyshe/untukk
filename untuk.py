import streamlit as st

st.markdown("<h2 style='text-align:center;'>Hai Khairi! 👋</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Selamat datang di website spesial ini, ada beberapa pertanyaan buat kamu yaa 💌</p>", unsafe_allow_html=True)

if "step" not in st.session_state:
    st.session_state.step = 1

if st.session_state.step == 1:
    warna = st.text_input("Gimana kabarnya hari ini? 😊")
    if warna:
        st.session_state.step = 2

if st.session_state.step == 2:
    if "salah_count" not in st.session_state:
        st.session_state.salah_count = 0
    sayang = st.text_input("Panggilan atau sebutan yang selalu kmu kasi ke aku apa? 🥰")
    allowed = ["chupa chups", "Chupa cups", "chupa Chups", "Chupa Chups"]
    if sayang:
        if sayang.strip() in allowed:
            st.session_state.step = 3
        else:
            st.session_state.salah_count += 1
            pesan = [
                "Yah, coba lagi yaa 😢",
                "Masa gitu aja gatau 😅",
                "Ayo semangat, pasti bisa! 💪",
                "Coba diingat-ingat lagi 🧐",
                "Hehe, jangan nyerah yaa 😆"
            ]
            idx = min(st.session_state.salah_count-1, len(pesan)-1)
            st.error(pesan[idx])

if st.session_state.step == 3:
    st.success("Terima kasih sudah jawab pertanyaannya! 🥳\n\nwkwk kocak jangan lupa kasi rating nya ya! 💖✨")
    st.balloons()