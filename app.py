import streamlit as st
import random

# 単語帳
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
  "good": "商品、利益、かなりの〜",
  "occasion": "場合、行事、祝い事",
  "accidental": "偶然の、偶発的な",
  "current": "最新の、今の；流通している；流れ、風潮",
  "temporary": "一時的な、仮の",
  "permanent": "永久的な、永続する",
  "previous": "前の、以前の",
  "former": "（the〜）前者；元の、前の、以前の",
  "contemporary": "現代の、同時代の；同時代の人",
  "lately": "最近（ここ数週間〜数ヶ月前）",
  "immediately": "すぐに、直接に",
  "deadline": "締め切り、期限",
  "decade": "10年間、10年",
  "supply": "〜を供給する、供給",
  "replace": "〜に取って代わる；〜を取り替える",
  "exchange": "〜を交換する；交換",
  "substitute": "〜を替える、代用する；代用品",
  "submit": "提出する；服従する",
  "alternative": "代わりのもの、選択肢；代わりの",
  "deliver": "〜を配達する；（演説など）をする"
}

# 初期化
if "score" not in st.session_state:
    st.session_state.score = 0
    st.session_state.q = None
    st.session_state.options = []

st.title("英単語 四択クイズ")

# 新しい問題を作る
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

# 最初の問題
if st.session_state.q is None:
    new_question()

st.subheader(f"問題： {st.session_state.q}")

# 選択肢ボタン
for opt in st.session_state.options:
    if st.button(opt):
        if opt == st.session_state.correct:
            st.success("⭕ 正解！")
            st.session_state.score += 1
        else:
            st.error(f"❌ 不正解… 正解：{st.session_state.correct}")
        new_question()

st.write(f"現在の得点：{st.session_state.score}")

