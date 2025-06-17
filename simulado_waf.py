import streamlit as st

st.set_page_config(page_title="Simulado AWS Well-Architected Framework", layout="centered")

st.title("📘 Simulado: AWS Well-Architected Framework (WAF)")
st.write("Responda às perguntas abaixo e veja seu desempenho no final.")

questions = [
    {
        "question": "1. Qual é o objetivo principal do pilar de Excelência Operacional no AWS Well-Architected Framework?",
        "options": [
            "A) Minimizar custos de armazenamento",
            "B) Implementar monitoramento e automação para operações contínuas",
            "C) Aumentar a largura de banda de rede",
            "D) Reduzir o tempo de resposta das APIs"
        ],
        "answer": "B) Implementar monitoramento e automação para operações contínuas"
    },
    {
        "question": "2. O que o pilar de Segurança recomenda para controle de acesso?",
        "options": [
            "A) Uso de senhas complexas",
            "B) Criptografia simétrica em todos os serviços",
            "C) Uso de múltiplas contas com permissões irrestritas",
            "D) Princípio do menor privilégio"
        ],
        "answer": "D) Princípio do menor privilégio"
    },
    {
        "question": "3. O que está relacionado ao pilar de Confiabilidade (Reliability)?",
        "options": [
            "A) Prover capacidade de executar tarefas de forma econômica",
            "B) Prevenir e se recuperar de falhas automaticamente",
            "C) Implementar dashboards para visualização de custos",
            "D) Minimizar o uso de instâncias spot"
        ],
        "answer": "B) Prevenir e se recuperar de falhas automaticamente"
    },
    {
        "question": "4. Qual destas práticas pertence ao pilar de Eficiência de Performance?",
        "options": [
            "A) Desabilitar logs para reduzir custos",
            "B) Implementar elasticidade para adaptar recursos automaticamente",
            "C) Manter instâncias sobredimensionadas por segurança",
            "D) Armazenar tudo no Amazon S3 Glacier"
        ],
        "answer": "B) Implementar elasticidade para adaptar recursos automaticamente"
    },
    {
        "question": "5. Como o pilar de Otimização de Custos ajuda as organizações?",
        "options": [
            "A) Reduzindo a segurança para melhorar o desempenho",
            "B) Alocando recursos manualmente para maior controle",
            "C) Usando métricas para identificar desperdícios e ajustar recursos",
            "D) Limitando a escalabilidade da aplicação"
        ],
        "answer": "C) Usando métricas para identificar desperdícios e ajustar recursos"
    },
    {
        "question": "6. Qual é um dos focos do pilar de Sustentabilidade?",
        "options": [
            "A) Aumentar o uso de recursos para garantir disponibilidade",
            "B) Reduzir o uso de recursos computacionais para menor impacto ambiental",
            "C) Substituir hardware com mais frequência",
            "D) Reduzir o uso de automações"
        ],
        "answer": "B) Reduzir o uso de recursos computacionais para menor impacto ambiental"
    },
    {
        "question": "7. Qual ferramenta da AWS ajuda a aplicar o AWS Well-Architected Framework?",
        "options": [
            "A) AWS CloudTrail",
            "B) AWS Trusted Advisor",
            "C) AWS Well-Architected Tool",
            "D) AWS CloudWatch"
        ],
        "answer": "C) AWS Well-Architected Tool"
    },
    {
        "question": "8. Qual prática NÃO é recomendada pelo pilar de Excelência Operacional?",
        "options": [
            "A) Automatizar mudanças",
            "B) Testar respostas a falhas",
            "C) Executar tarefas críticas manualmente",
            "D) Documentar procedimentos"
        ],
        "answer": "C) Executar tarefas críticas manualmente"
    },
    {
        "question": "9. O que o pilar de Segurança recomenda sobre dados em trânsito e em repouso?",
        "options": [
            "A) Somente criptografar dados em trânsito",
            "B) Deixar dados desprotegidos para acelerar performance",
            "C) Criptografar ambos com chaves gerenciadas",
            "D) Armazenar dados em cache sem criptografia"
        ],
        "answer": "C) Criptografar ambos com chaves gerenciadas"
    },
    {
        "question": "10. Como a AWS Well-Architected Framework ajuda arquitetos de soluções?",
        "options": [
            "A) Substituindo o arquiteto humano por IA",
            "B) Oferecendo um conjunto de regras rígidas para todos os workloads",
            "C) Ajudando a tomar decisões informadas com base nos seis pilares",
            "D) Criando códigos automáticos para aplicações"
        ],
        "answer": "C) Ajudando a tomar decisões informadas com base nos seis pilares"
    }
]

score = 0
respostas_usuario = []

with st.form("quiz_form"):
    for i, q in enumerate(questions):
        resposta = st.radio(q["question"], q["options"], key=i)
        respostas_usuario.append(resposta)
    submitted = st.form_submit_button("Ver Resultado")

if submitted:
    for i, q in enumerate(questions):
        if respostas_usuario[i] == q["answer"]:
            score += 1

    st.success(f"✅ Você acertou {score} de {len(questions)} questões.")
    st.progress(score / len(questions))

    if score == len(questions):
        st.balloons()

