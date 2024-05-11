# Projeto

Chatbot: Descubra os cursos da Alura

A Alura é demais, né? São mais de 1000 cursos disponíveis! Mas e aí, como encontrar o curso certo pra você? Apresentando a Lulu! 🤖 A Lulu é um chatbot que faz umas perguntinhas de boa, pra te conhecer melhor. Depois do papo, ela te sugere uns cursos da Alura que são a sua cara! 😉



# DEV

Este projeto faz uso das seguintes tecnicas apresentadas no curso:

- Uso da API `google.generativeai` para criacao de um chatbot
- System Instruction: para descrever compartamento do BOT. Ele faz perguntas para colher dados antes da responsta final
- Uso de exmplos one-shot, few-shot para melhora do prompt.
- Uso de dados especificos (no caso a lista de cursos da alura - obtido atraves de scraping do site).


# USO

Existem 3 versoes do chatbot:

1) `main.ipynb` notebook com versao inicial roda no Google Collab.
2) `main.py` versao CLI
3) `web.py` interface WEB usando o streamlit


## instalacao

```
pip install -r requirements.txt
```

## configuracao

Crie um arquivo `.env` com a sua chave de API, exemplo:

```
GOOGLE_API_KEY=minha-chave
```



# Exemplo

[![asciicast](https://asciinema.org/a/jQYkCLAMAFkHE8iYvvUGbaAXp.svg)](https://asciinema.org/a/jQYkCLAMAFkHE8iYvvUGbaAXp)



Exemplo completo no arquivo `sample.txt`.


## 

Lulu:  Olá! 😊 Sou a Lulu, sua consultora de cursos online. Estou aqui para te ajudar a encontrar o curso perfeito para você! 🎉 Para isso, vou te fazer algumas perguntas para entender melhor seus interesses e objetivos. Se prepare para uma jornada rumo ao conhecimento! 🚀

Para começarmos, me fale um pouco sobre você: você se considera mais fã de **Gatos 🐱 ou Cachorros 🐶?** 
 

Esperando prompt:gatos

Resposta:  Miauu! 😸 Ótima escolha! Os gatos são criaturas incríveis, inteligentes e independentes. Assim como quem busca conhecimento! 

E falando em conhecimento, qual a sua principal motivação para fazer um curso online? 🤔

a) Quero turbinar minha carreira profissional! 🚀

b) Busco desenvolvimento pessoal e autoconhecimento. 🧘

c) Desejo aprender algo novo só por curiosidade! 🤓

d) Outros (especifique):  📝 
 

Esperando prompt:a

....



Resposta:  Uau, um(a) programador(a) buscando dominar a IA! Que incrível! 🤩 Para finalizar, me conta: qual linguagem de programação você domina e gostaria de usar para se aventurar na IA?  

a) Python 🐍 (a queridinha da IA!)

b) Java ☕ (robusta e poderosa!)

c) JavaScript 🚀 (versátil e em alta!)

d) Outras (especifique): 📝 
 

Esperando prompt:php
Resposta:  Show! PHP e IA, uma combinação poderosa para turbinar sua carreira! 💪

Baseado em suas respostas, preparei 3 cursos que podem te interessar:

**1. Curso GPT e Python: criando ferramentas com a API:**
* **Descrição:** Aprenda a integrar a poderosa API do GPT em suas aplicações PHP e criar ferramentas incríveis com inteligência artificial.
* **Por que é uma boa escolha:** Você já domina PHP e este curso te dará as ferramentas para usar o GPT, um dos modelos de linguagem mais avançados do mundo, em seus projetos.

**2. Curso OpenAI e Python: otimize o desenvolvimento de testes com IA:**
* **Descrição:** Descubra como usar o poder da IA da OpenAI para otimizar o desenvolvimento de testes em suas aplicações PHP, tornando o processo mais eficiente e inteligente.
* **Por que é uma boa escolha:** Como programador(a) experiente, você sabe a importância de testes eficientes. Este curso te mostrará como a IA pode te auxiliar nessa tarefa.

**3. Curso Python para Data Science: primeiros passos:**
* **Descrição:** Comece sua jornada no mundo da Data Science com Python, uma linguagem essencial para quem quer trabalhar com IA.
* **Por que é uma boa escolha:** Este curso te dará a base em Python necessária para se aprofundar em IA, abrindo portas para novas possibilidades em sua carreira.

E aí, o que achou? 😉  

Se tiver mais alguma dúvida ou quiser refinar ainda mais as recomendações, me fale! Estou aqui para te ajudar a encontrar o curso ideal. 😊
