from dotenv import load_dotenv
import os
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

# 1) Carrega variáveis do .env
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY não encontrada. Coloque ela no .env")

# 2) Modelo + parser
modelo = ChatOpenAI(
    model="gpt-4o-mini",
    api_key=api_key,
)
parser = StrOutputParser()

# 3) Template de tradução
template_mensagem = ChatPromptTemplate.from_messages([
    ("system", "Você é um tradutor profissional. Traduza o texto do usuário para {idioma}."),
    ("user", "{texto}"),
])

# 4) Chain: template -> modelo -> parser
chain = template_mensagem | modelo | parser

# 5) Chamada
resultado = chain.invoke({
    "idioma": "francês",
    "texto": "Dê o like",
})

print("Resultado:", resultado)  

