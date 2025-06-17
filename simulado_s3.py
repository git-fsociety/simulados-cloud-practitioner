import streamlit as st

st.set_page_config(page_title="Simulado AWS - Classes de Armazenamento S3", layout="centered")

st.title("📦 Simulado AWS - Classes de Armazenamento S3")
st.markdown("Simulado focado nas classes de armazenamento do Amazon S3. Selecione as alternativas corretas e veja sua pontuação ao final.")

questions = [
    {
        "question": "1. Uma empresa precisa armazenar dados de backup que são acessados raramente, mas precisam estar disponíveis rapidamente em caso de emergência. Qual classe de armazenamento S3 é mais apropriada?",
        "options": ["S3 Standard", "S3 Glacier Deep Archive", "S3 Standard-IA", "S3 One Zone-IA"],
        "answer": "S3 Standard-IA"
    },
    {
        "question": "2. Uma startup quer arquivar logs antigos para cumprir exigências legais. Os dados só serão acessados em situações específicas e podem demorar até 12 horas para serem recuperados. Qual classe é a mais econômica e adequada?",
        "options": ["S3 Glacier Flexible Retrieval", "S3 Intelligent-Tiering", "S3 Standard-IA", "S3 Glacier Deep Archive"],
        "answer": "S3 Glacier Deep Archive"
    },
    {
        "question": "3. Qual classe de armazenamento do Amazon S3 realiza a movimentação automática de objetos entre camadas com base nos padrões de acesso, sem custo de recuperação?",
        "options": ["S3 Intelligent-Tiering", "S3 Standard", "S3 Glacier", "S3 One Zone-IA"],
        "answer": "S3 Intelligent-Tiering"
    },
    {
        "question": "4. Uma empresa precisa armazenar arquivos que serão acessados com frequência por um site ativo. Qual classe de armazenamento é mais apropriada?",
        "options": ["S3 Standard-IA", "S3 Glacier Flexible Retrieval", "S3 Standard", "S3 Intelligent-Tiering"],
        "answer": "S3 Standard"
    },
    {
        "question": "5. Um time de TI deseja reduzir custos com backups que podem ser reprocessados facilmente e toleram perda de disponibilidade de zona. Qual classe usar?",
        "options": ["S3 Standard", "S3 One Zone-IA", "S3 Intelligent-Tiering", "S3 Glacier"],
        "answer": "S3 One Zone-IA"
    },
]

score = 0
responses = []

with st.form("simulado_form"):
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


