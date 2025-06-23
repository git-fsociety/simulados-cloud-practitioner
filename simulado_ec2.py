import streamlit as st

st.set_page_config(page_title="Simulado AWS Practitioner – Tipos de Instância", layout="wide")
st.title("🧠 Simulado AWS Cloud Practitioner – Tipos de Instâncias EC2")
st.markdown("Responda todas as questões e clique em **Finalizar Simulado** para ver seu resultado.")

# Lista de perguntas e opções (sem resposta)
questoes = [
    {
        "pergunta": "1. Qual é a principal vantagem das instâncias sob demanda (On-Demand Instances)?",
        "opcoes": [
            "A) Maior desempenho de CPU",
            "B) Baixo custo para workloads de longo prazo",
            "C) Flexibilidade de pagamento sem compromisso a longo prazo",
            "D) Capacidade dedicada ao cliente"
        ]
    },
    {
        "pergunta": "2. Quando uma empresa deveria considerar o uso de instâncias reservadas (Reserved Instances)?",
        "opcoes": [
            "A) Para cargas imprevisíveis com uso intermitente",
            "B) Quando precisa de escalabilidade rápida",
            "C) Quando deseja economizar em workloads estáveis de longo prazo",
            "D) Para simulações científicas esporádicas"
        ]
    },
    {
        "pergunta": "3. Qual opção oferece o menor custo por hora, mas pode ser interrompida pela AWS?",
        "opcoes": [
            "A) Instância Dedicada",
            "B) Instância Spot",
            "C) Instância Reservada",
            "D) Instância Sob Demanda"
        ]
    },
    {
        "pergunta": "4. Qual é a principal vantagem do AWS Savings Plans comparado às instâncias reservadas?",
        "opcoes": [
            "A) Maior capacidade computacional",
            "B) Maior desconto",
            "C) Maior flexibilidade de uso entre instâncias, regiões e serviços",
            "D) Tempo de execução ilimitado"
        ]
    },
    {
        "pergunta": "5. Qual opção oferece servidores físicos dedicados a um único cliente?",
        "opcoes": [
            "A) Instâncias Spot",
            "B) Instâncias Sob Demanda",
            "C) Savings Plans",
            "D) Host Dedicado"
        ]
    },
    {
        "pergunta": "6. Qual tipo de instância é mais indicado para aplicações sensíveis à interrupção, como batch processing?",
        "opcoes": [
            "A) Host Dedicado",
            "B) Instância Reservada",
            "C) Instância Spot",
            "D) Instância On-Demand"
        ]
    },
    {
        "pergunta": "7. Qual das opções abaixo não exige compromisso de longo prazo nem capacidade dedicada?",
        "opcoes": [
            "A) On-Demand",
            "B) Reserved",
            "C) Savings Plan",
            "D) Dedicated Host"
        ]
    }
]

# Gabarito separado
gabarito = ["C", "C", "B", "C", "D", "C", "A"]

# Formulário
with st.form("form_simulado"):
    respostas_usuario = []
    for i, q in enumerate(questoes):
        resposta = st.radio(q["pergunta"], q["opcoes"], key=f"q{i}")
        respostas_usuario.append(resposta)
    enviado = st.form_submit_button("🚀 Finalizar Simulado")

# Correção
if enviado:
    st.markdown("---")
    st.subheader("📊 Correção do Simulado")

    acertos = 0
    for i, q in enumerate(questoes):
        resposta_usuario = respostas_usuario[i]
        letra_usuario = resposta_usuario[0]
        letra_correta = gabarito[i]
        opcao_correta = next(opcao for opcao in q["opcoes"] if opcao.startswith(letra_correta))

        st.markdown(f"**{q['pergunta']}**")
        if letra_usuario == letra_correta:
            st.success(f"✅ Sua resposta: {resposta_usuario}")
            acertos += 1
        else:
            st.error(f"❌ Sua resposta: {resposta_usuario}")
            st.info(f"✅ Resposta correta: {opcao_correta}")

    st.markdown("---")
    st.subheader(f"🎯 Resultado Final: {acertos} de {len(questoes)} questões corretas.")
    if acertos == len(questoes):
        st.balloons()

