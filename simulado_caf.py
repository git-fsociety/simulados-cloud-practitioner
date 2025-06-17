import streamlit as st

st.set_page_config(page_title="Simulado AWS CAF", layout="centered")

st.title("🧭 Simulado AWS - Cloud Adoption Framework (CAF)")
st.markdown("Este simulado cobre os fundamentos do AWS CAF. Selecione as alternativas corretas e veja sua pontuação ao final.")

questions = [
    {
        "question": "1. O que é o AWS Cloud Adoption Framework (CAF)?",
        "options": [
            "Um serviço para migração automatizada de aplicações",
            "Uma estrutura que ajuda organizações a planejar a adoção da nuvem",
            "Uma ferramenta para modelagem de custos em nuvem",
            "Um serviço de monitoramento de recursos na AWS"
        ],
        "answer": "Uma estrutura que ajuda organizações a planejar a adoção da nuvem"
    },
    {
        "question": "2. Qual dos seguintes é um pilar (perspectiva) do AWS CAF?",
        "options": [
            "Desempenho",
            "Segurança",
            "Governança",
            "Elasticidade"
        ],
        "answer": "Governança"
    },
    {
        "question": "3. Qual perspectiva do AWS CAF é responsável por garantir conformidade e gerenciamento de riscos?",
        "options": [
            "Pessoas",
            "Plataforma",
            "Governança",
            "Operações"
        ],
        "answer": "Governança"
    },
    {
        "question": "4. Qual perspectiva do AWS CAF está relacionada a habilidades, cultura organizacional e estrutura de equipe?",
        "options": [
            "Negócios",
            "Pessoas",
            "Segurança",
            "Plataforma"
        ],
        "answer": "Pessoas"
    },
    {
        "question": "5. Quantas perspectivas compõem o AWS Cloud Adoption Framework (CAF)?",
        "options": [
            "4",
            "6",
            "7",
            "3"
        ],
        "answer": "6"
    },
]

score = 0
responses = []

with st.form("caf_simulado_form"):
    for idx, q in enumerate(questions):
        st.markdown(f"**{q['question']}**")
        selected = st.radio(f"Opções {idx+1}", q["options"], key=idx)
        responses.append(selected)

    submitted = st.form_submit_button("Enviar Respostas")

if submitted:
    for idx, q in enumerate(questions):
        if responses[idx] == q["answer"]:
            score += 1

    st.success(f"✅ Você acertou {score} de {len(questions)} perguntas.")

    for idx, q in enumerate(questions):
        if responses[idx] != q["answer"]:
            st.markdown(f"❌ **{q['question']}**")
            st.markdown(f"- Sua resposta: `{responses[idx]}`")
            st.markdown(f"- Resposta correta: ✅ `{q['answer']}`")


