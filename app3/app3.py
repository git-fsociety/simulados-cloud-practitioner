# simulado_aws_streamlit.py
import re
import streamlit as st
from io import StringIO

st.set_page_config(page_title="Simulado AWS CLF‑C02", layout="wide")
st.title("📘 Simulado AWS Cloud Practitioner – CLF‑C02 (2025)")
st.write(
    "1. Faça *upload* do arquivo .txt com as questões.\n"
    "2. Responda todas as questões.\n"
    "3. Clique em **Enviar respostas** para conferir a pontuação."
)

# ---------- PARSER ----------
def parse_aws_exam(txt: str):
    questoes = []
    q_atual = None

    for line in txt.splitlines():
        line = line.rstrip()

        if re.match(r"(?i)^quest[aã]o\s+\d+", line):
            if q_atual:
                questoes.append(q_atual)
            numero = re.findall(r"\d+", line)[0]
            q_atual = {"id": int(numero), "pergunta": "", "opcoes": []}

        elif re.match(r"^[A-Da-d]\)", line):
            q_atual["opcoes"].append(line[3:].strip())
        elif q_atual is not None:
            q_atual["pergunta"] += (" " if q_atual["pergunta"] else "") + line.strip()

    if q_atual:
        questoes.append(q_atual)
    questoes.sort(key=lambda q: q["id"])
    return questoes


# ---------- GABARITO ----------
# gabarito = {
#     "1": ["B"], "2": ["A"], "3": ["B"], "4": ["D"], "5": ["A"], "6": ["D"],
#     "7": ["C"], "8": ["C"], "9": ["B"], "10": ["D"], "11": ["C"], "12": ["B"],
#     "13": ["C"], "14": ["B"], "15": ["C"], "16": ["D"], "17": ["A"], "18": ["B"],
#     "19": ["D"], "20": ["B"], "21": ["C"], "22": ["C"], "23": ["C"], "24": ["B"],
#     "25": ["A"], "26": ["B"], "27": ["A"], "28": ["D"], "29": ["A"], "30": ["C"],
#     "31": ["B"], "32": ["B"], "33": ["B"], "34": ["C"], "35": ["B"], "36": ["B"],
#     "37": ["A"], "38": ["C"], "39": ["A"], "40": ["B"], "41": ["D"], "42": ["D"],
#     "43": ["B"], "44": ["B"], "45": ["C"], "46": ["C"], "47": ["D"], "48": ["B"],
#     "49": ["C"], "50": ["B"], "51": ["C"], "52": ["D"], "53": ["A"], "54": ["B"],
#     "55": ["D"], "56": ["C"], "57": ["A"], "58": ["C"], "59": ["B"], "60": ["C"],
#     "61": ["D"], "62": ["B"], "63": ["D"], "64": ["C"], "65": ["C"]
# }




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

uploaded_file = st.file_uploader("📄 Envie o arquivo .txt com as questões", type=["txt"])

if uploaded_file:
    texto = StringIO(uploaded_file.getvalue().decode("utf-8")).read()
    questoes = parse_aws_exam(texto)

    respostas = []
    acertos = 0

    with st.form("simulado"):
        for q in questoes:
            st.subheader(f"Questão {q['id']}")
            resposta = st.radio(
                q["pergunta"],
                q["opcoes"],
                key=f"q{q['id']}",
                index=None
            )
            respostas.append(resposta)

        enviado = st.form_submit_button("Enviar respostas")

    if enviado:
        if None in respostas:
            st.warning("Responda todas as questões antes de enviar.")
            st.stop()

        for idx, resp in enumerate(respostas):
            q_id = str(questoes[idx]["id"])
            letra_correta = gabarito.get(q_id, [""])[0].upper()
            letra_resp = ["A", "B", "C", "D"][questoes[idx]["opcoes"].index(resp)]
            if letra_resp == letra_correta:
                acertos += 1

        perc = acertos / len(questoes) * 100
        st.success(f"Você acertou **{acertos}** de **{len(questoes)}** – {perc:.2f}%")
        st.progress(perc / 100)

        if perc >= 70:
            st.balloons()
            st.write("🎉 Parabéns! Excelente desempenho.")
        else:
            st.info("Continue estudando e tente novamente.")
else:
    st.info("Envie o arquivo para iniciar o simulado.")
