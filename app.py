import streamlit as st
import random

# ===== ページ設定 =====
st.set_page_config(page_title="英単語クイズ", page_icon="📘", layout="centered")

# ===== 単語帳 =====
words = {
    "reception": "もてなし、歓迎会、フロント",
    "portion": "一盛り、一部",
    "laundry": "洗濯物",
    "nap": "昼寝",
    "wake": "起こす",
}

TOTAL_QUESTIONS = 5

# ===== 初期化 =====
if "score" not in st.session_state:
    st.session_state.score = 0
    st.session_state.q = None
    st.session_state.options = []
    st.session_state.count = 0
    st.session_state.finished = False

# ===== 新しい問題 =====
def new_question():
    q = random.choice(list(words.keys()))
    correct = words[q]
    wrong = list(words.values())
    wrong.remove(correct)

    options = random.sample(wrong, 3) + [correct]
    random.shuffle(options)

    st.session_state.q = q
    st.session_state.correct = correct
    st.session_state.options = options

# ===== リセット =====
def reset_game():
    st.session_state.score = 0
    st.session_state.count = 0
    st.session_state.finished = False
    new_question()

# ===== タイトル =====
st.markdown("<h1 style='text-align:center;'>📘 英単語 四択クイズ</h1>", unsafe_allow_html=True)

# ===== 最初の問題 =====
if st.session_state.q is None and not st.session_state.finished:
    new_question()

# ===== 進捗バー =====
if not st.session_state.finished:
    progress = st.session_state.count / TOTAL_QUESTIONS
    st.progress(progress)

# ===== クイズ画面 =====
if not st.session_state.finished:

    st.markdown(
        f"""
        <div style="
            padding:20px;
            border-radius:15px;
            background-color:#f0f2f6;
            text-align:center;
            font-size:24px;">
            問題 {st.session_state.count + 1} / {TOTAL_QUESTIONS}<br><br>
            <b>{st.session_state.q}</b>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    col1, col2 = st.columns(2)

    for i, opt in enumerate(st.session_state.options):
        if i % 2 == 0:
            target_col = col1
        else:
            target_col = col2

        if target_col.button(opt, use_container_width=True):
            st.session_state.count += 1

            if opt == st.session_state.correct:
                st.success("🎉 正解！")
                st.balloons()
                st.session_state.score += 1
            else:
                st.error(f"❌ 不正解… 正解：{st.session_state.correct}")

            if st.session_state.count >= TOTAL_QUESTIONS:
                st.session_state.finished = True
            else:
                new_question()

# ===== 終了画面 =====
else:
    st.markdown("<h2 style='text-align:center;'>🎉 クイズ終了！</h2>", unsafe_allow_html=True)

    percent = int((st.session_state.score / TOTAL_QUESTIONS) * 100)

    st.markdown(
        f"""
        <div style="
            padding:20px;
            border-radius:15px;
            background-color:#e6ffe6;
            text-align:center;
            font-size:20px;">
            スコア： {st.session_state.score} / {TOTAL_QUESTIONS}<br>
            正答率： {percent}%
        </div>
        """,
        unsafe_allow_html=True
    )

    if percent == 100:
        st.success("完璧！！すごい🔥")

    st.write("")
    if st.button("🔄 もう一回やる"):
        reset_game()
