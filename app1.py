import streamlit as st
from questions import questions  # Importa as questões do arquivo separado

st.title("Simulado AWS Certified Cloud Practitioner (CLF-C02)")
st.markdown("Versão 1.2")

score = 0
answers = []

with st.form("quiz_form"):
    for i, q in enumerate(questions):
        user_answer = st.radio(f"{i+1}. {q['question']}", q['options'], key=i)
        answers.append((q['question'], user_answer, q['answer']))
    submitted = st.form_submit_button("Finalizar Simulado")

if submitted:
    for i, (question, user_answer, correct_answer) in enumerate(answers):
        if user_answer == correct_answer:
            score += 1

    total = len(questions)
    percentage = (score / total) * 100

    st.subheader(f"Resultado: {score} de {total} questões corretas")
    st.write(f"📊 **Percentual de acertos:** {percentage:.2f}%")

    for i, (question, user_answer, correct_answer) in enumerate(answers):
        result = "✅ Correto" if user_answer == correct_answer else f"❌ Errado (Correto: {correct_answer})"
        st.write(f"{i+1}. {question}\nSua resposta: {user_answer}\n{result}\n")
