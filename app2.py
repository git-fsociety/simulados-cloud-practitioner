import streamlit as st
import re

st.set_page_config(page_title="Simulado AWS Cloud Practitioner", layout="wide")

st.title("🧠 Simulado AWS Cloud Practitioner - 2025")
st.markdown("Este simulado contém 65 questões de múltipla escolha para praticar para a certificação AWS CCP (CLF-C02).")

# Carregamento do arquivo local
with open("AWSCloudPractitioner-v1.txt", "r", encoding="utf-8") as f:
    content = f.read()

# Extrair questões usando regex
padrao_questao = r"QUESTÃO (\d+)(.*?)\n(A.*?)\n\n(?=QUESTÃO|\Z)"
questoes = re.findall(padrao_questao, content, re.DOTALL)

# Gabarito com respostas corretas
gabarito = {
    "1": ["C"], "2": ["B"], "3": ["B"], "4": ["B"], "5": ["C"], "6": ["A", "C", "D"],
    "7": ["C"], "8": ["C"], "9": ["B"], "10": ["B"], "11": ["B"], "12": ["B"], "13": ["A", "C", "E"],
    "14": ["C"], "15": ["B"], "16": ["B"], "17": ["B"], "18": ["C"], "19": ["A", "B", "C"],
    "20": ["B"], "21": ["D"], "22": ["B"], "23": ["B"], "24": ["B"], "25": ["A", "B", "C"],
    "26": ["B"], "27": ["B"], "28": ["C"], "29": ["B"], "30": ["B"], "31": ["A", "B", "C", "D", "E"],
    "32": ["B"], "33": ["B"], "34": ["B"], "35": ["B"], "36": ["A", "B", "C"],
    "37": ["B"], "38": ["C"], "39": ["B"], "40": ["B"], "41": ["A", "B", "C"],
    "42": ["B"], "43": ["C"], "44": ["B"], "45": ["B"], "46": ["A", "B", "C"],
    "47": ["B"], "48": ["A"], "49": ["C"], "50": ["B"], "51": ["A", "B", "C"],
    "52": ["B"], "53": ["B"], "54": ["B"], "55": ["B"], "56": ["A", "B", "C"],
    "57": ["B"], "58": ["C"], "59": ["B"], "60": ["B"], "61": ["A", "C", "E"],
    "62": ["B"], "63": ["A"], "64": ["B"], "65": ["D"]
}

respostas = {}
with st.form("simulado"):
    for numero, enunciado, alternativas in questoes:
        st.subheader(f"Questão {numero}")
        st.write(enunciado.strip())
        opcoes = re.findall(r"([A-F])\) (.+)", alternativas)
        multiplas = "Selecione" in enunciado or "Selecione TRÊS" in enunciado or "Selecione CINCO" in enunciado

        if multiplas:
            escolhidas = st.multiselect(
                f"Escolha suas respostas para a Questão {numero}:",
                [f"{letra}) {texto}" for letra, texto in opcoes],
                key=numero
            )
            respostas[numero] = [r[0] for r in escolhidas]
        else:
            escolhida = st.radio(
                f"Escolha uma resposta para a Questão {numero}:",
                [f"{letra}) {texto}" for letra, texto in opcoes],
                key=numero
            )
            respostas[numero] = [escolhida[0]]

    enviado = st.form_submit_button("Enviar Respostas")

# Correção após envio
if enviado:
    st.success("✅ Resultado do Simulado")
    acertos = 0

    for numero in sorted(gabarito.keys(), key=lambda x: int(x)):
        correta = set(gabarito[numero])
        marcada = set(respostas.get(numero, []))
        correta_str = ", ".join(correta)
        marcada_str = ", ".join(marcada) if marcada else "Não respondida"

        if correta == marcada:
            resultado = "✅ Correta"
            acertos += 1
            cor = "green"
        else:
            resultado = "❌ Incorreta"
            cor = "red"

        st.markdown(f"**Questão {numero}**")
        st.markdown(f"- Sua resposta: `{marcada_str}`")
        st.markdown(f"- Resposta correta: `{correta_str}`")
        st.markdown(f"- Resultado: :{cor}[{resultado}]")
        st.markdown("---")

    total = len(gabarito)
    st.success(f"🎯 Você acertou {acertos} de {total} ({(acertos/total)*100:.1f}%)")
