import streamlit as st
import random

st.set_page_config(page_title="英単語クイズ", page_icon="📘")

words = {
    "reception": "もてなし、歓迎会、（ホテルの）フロント、受信状況",
    "portion": "（食事の）一盛り、（食堂などの）一人前、一部",
    "laundry": "洗濯、洗濯物、クリーニング店",
    "nap": "昼寝、仮眠",
    "wake": "目が覚める、〜を起こす",
    "vending machine": "自動販売機",
    "grocery": "食料雑貨店",
    "appointment": "予約、面会の約束、任命・指名",
    "consult": "〜に相談する、（辞書など）を引く",
    "register": "〜を登録する、記録する、（授業などに）登録する",
    "dye": "〜を染める、染まる",
    "subscribe": "（to〜）〜を定期購読する、加入している",
    "guarantee": "〜を保証する、保証",
    "wipe": "〜を拭く、拭き取る、ぬぐう、消す",
    "sweep": "（床・地面）を掃く、（風・波などが）〜を押し流す",
    "transfer": "乗り換える、転勤・移籍する、〜を移す、（銀行で）振り込む",
    "divorce": "離婚する、〜と離婚させる、離婚",
    "fate": "運命、宿命（悪い運命のニュアンス）",
    "destiny": "運命（託された必然の流れ）",
    "luxury": "高級（品）、豪華さ、贅沢",
    "credit": "クレジットカード、功績、（大学の）単位",
    "questionnaire": "アンケート",
    "reservation": "予約、保留、遠慮",
    "fuss": "大騒ぎ、やきもき",
    "reward": "報酬、賞金、〜に報酬を与える",
    "farewell": "別れのあいさつ、送別",
    "enclose": "同封する、囲む、閉じ込める",
    "envelope": "封筒",
    "trick": "いたずら、手口・策略、芸・手品",
    "load": "大量の荷物、重荷",
    "content": "内容、中身、（with〜）満足して",
    "household": "家庭、家族、家庭の",
    "good": "商品、利益、かなりの〜"
}

TOTAL_QUESTIONS = 10  # ← 出題数（自由に変えられる）

# ===== 初期化 =====
if "initialized" not in st.session_state:

    # 重複なしで問題を選ぶ
    st.session_state.question_list = random.sample(
        list(words.keys()), TOTAL_QUESTIONS
    )

    st.session_state.score = 0
    st.session_state.count = 0
    st.session_state.finished = False
    st.session_state.answered = False
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
    st.session_state.answered = False


if "q" not in st.session_state:
    generate_question()

st.title("📘 英単語 四択クイズ")

# ===== クイズ中 =====
if not st.session_state.finished:

    st.write(f"問題 {st.session_state.count + 1} / {TOTAL_QUESTIONS}")
    st.subheader(st.session_state.q)

    if not st.session_state.answered:

        for opt in st.session_state.options:
            if st.button(opt):
                st.session_state.selected = opt
                st.session_state.answered = True

                if opt == st.session_state.correct:
                    st.session_state.score += 1

                st.rerun()

    else:
        if st.session_state.selected == st.session_state.correct:
            st.success("⭕ 正解！")
        else:
            st.error(f"❌ 不正解… 正解：{st.session_state.correct}")

        if st.button("➡ 次の問題へ"):

            st.session_state.count += 1

            if st.session_state.count >= TOTAL_QUESTIONS:
                st.session_state.finished = True
            else:
                generate_question()

            st.rerun()

# ===== 終了画面 =====
else:
    st.header("🎉 クイズ終了！")
    percent = int((st.session_state.score / TOTAL_QUESTIONS) * 100)
    st.write(f"スコア： {st.session_state.score} / {TOTAL_QUESTIONS}")
    st.write(f"正答率： {percent}%")

    if st.button("もう一回やる"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()
