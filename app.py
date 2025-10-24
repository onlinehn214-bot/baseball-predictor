import streamlit as st
import random

st.set_page_config(page_title="⚾ 야구 경기 랜덤 예측기", page_icon="⚾", layout="centered")

st.title("⚾ 야구 경기 랜덤 예측기 (무승부 포함)")
st.write("두 팀을 입력하면 랜덤하게 승패를 예측하고, 가끔은 무승부도 나옵니다! 😎")

team1 = st.text_input("팀 1 이름 입력")
team2 = st.text_input("팀 2 이름 입력")

if st.button("예측하기"):
    if not team1 or not team2:
        st.warning("⚠️ 팀 이름을 모두 입력해주세요!")
    elif team1 == team2:
        st.error("❌ 두 팀 이름이 같습니다! 다른 팀으로 입력해주세요.")
    else:
        draw_prob = 0.1
        rand_val = random.random()

        win_messages = [
            "🔥 {winner} 팀이 불꽃같은 경기력을 보여줬습니다!",
            "⚾ {winner} 팀이 끝내기 안타로 승리를 가져갑니다!",
            "💥 {winner} 팀이 {loser} 팀을 압도했습니다!",
            "🏆 오늘의 히어로는 단연 {winner} 팀입니다!",
            "👏 {winner} 팀이 극적인 역전승을 거뒀습니다!",
            "🚀 {winner} 팀이 완벽한 투타 밸런스로 승리했습니다!",
            "🎯 {winner} 팀이 상대를 완벽히 분석해냈습니다!",
        ]

        draw_messages = [
            "🤝 두 팀이 팽팽한 접전을 펼친 끝에 무승부를 기록했습니다!",
            "😮 오늘 경기는 승부를 가리지 못했습니다. 두 팀 모두 수고했어요!",
            "⚖️ 승부의 여신이 미소 짓지 않았네요. 무승부입니다!",
            "🌀 연장까지 갔지만, 결국 무승부로 마무리됩니다!",
        ]

        if rand_val < draw_prob:
            message = random.choice(draw_messages)
            st.info(message)
        else:
            winner = random.choice([team1, team2])
            loser = team2 if winner == team1 else team1
            message = random.choice(win_messages).format(winner=winner, loser=loser)
            st.success(message)
