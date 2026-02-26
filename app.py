import streamlit as st
import random

st.set_page_config(page_title="英単語クイズ", page_icon="📘")

words = {
    "reception": "もてなし、歓迎会、フロント",
    "portion": "一盛り、一部",
    "laundry": "洗濯物",
    "nap": "昼寝",
    "wake": "起こす",
    "borrow": "借りる",
    "lend": "貸す"
}

TOTAL_QUESTIONS = 5

# ===== 初期化 =====
if "initialized" not in st.session_state:

    # 出題する単語を最初にランダムで決定（重複なし）
    st.session_state.question_list = random.sample(
        list(words.keys()), TOTAL_QUESTIONS
    )

    st.session_state.score = 0
    st.session_state.count = 0
    st.session_state.finished = False
    st.session_state.initialized = True


def generate_question():
    q = st.session_state.question_list[st.session_state.count]
    correct = words[q]

    wrong = list(words.values())
    wrong.remove(correct)

    options = random.sample(wrong, 3) + [correct]
    random.shuffle(options)

    st.session_state.q = q
    st.session_state.correct = correct
    st.session_state.options = options


if "q" not in st.session_state:
    generate_question()

st.title("📘 英単語 四択クイズ")

# ===== クイズ中 =====
if not st.session_state.finished:

    st.write(f"問題 {st.session_state.count + 1} / {TOTAL_QUESTIONS}")
    st.subheader(st.session_state.q)

    for opt in st.session_state.options:
        if st.button(opt):

            if opt == st.session_state.correct:
                st.success("⭕ 正解！")
                st.session_state.score += 1
            else:
                st.error(f"❌ 不正解… 正解：{st.session_state.correct}")

            st.session_state.count += 1

            if st.session_state.count >= TOTAL_QUESTIONS:
                st.session_state.finished = True
            else:
                generate_question()

            st.rerun()

# ===== 終了画面 =====
else:
    st.header("🎉 クイズ終了！")
    st.write(f"スコア： {st.session_state.score} / {TOTAL_QUESTIONS}")

    if st.button("もう一回やる"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()
