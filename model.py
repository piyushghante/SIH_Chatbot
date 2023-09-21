# from langchain import PromptTemplate
# from langchain.embeddings import HuggingFaceEmbeddings
# from langchain.vectorstores import FAISS
# from langchain.llms import CTransformers
# from langchain.chains import RetrievalQA
# import chainlit as cl
# from langdetect import detect
# from deep_translator import GoogleTranslator

# DB_FAISS_PATH = "vectorstores/db_faiss"

# def set_custom_prompt():
#     custom_prompt_template = """ Use the following pieces of information to answer the user's question. IF you don't know the answer, please just say that you don't know the answer, don't try to make up an answer.

#  Context : {context}
#  Question: {question}

#  Only returns the helpful answer below and nothing else.
#  Helpful answer:

#  """
#     prompt = PromptTemplate(template=custom_prompt_template, input_variables=['context', 'question'])
#     return prompt

# def load_llm():
#     llm = CTransformers(
#         model="llama-2-7b-chat.ggmlv3.q8_0.bin",
#         model_type="llama",
#         max_new_tokens=512,
#         temperature=0.5
#     )
#     return llm

# def retrieval_qa_chain(llm, prompt, db):
#     qa_chain = RetrievalQA.from_chain_type(
#         llm=llm,
#         chain_type="stuff",
#         retriever=db.as_retriever(search_kwargs={'k': 2}),
#         return_source_documents=True,
#         chain_type_kwargs={'prompt': prompt}
#     )
#     return qa_chain

# def qa_bot():
#     embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2', model_kwargs={'device': 'cpu'})

#     db = FAISS.load_local(DB_FAISS_PATH, embeddings)
#     llm = load_llm()
#     qa_prompt = set_custom_prompt()
#     qa = retrieval_qa_chain(llm, qa_prompt, db)

#     return qa

# def detect_language(text):
#     try:
#         language = detect(text)
#         return language
#     except:
#         return 'en'  # Default to English if language detection fails

# def translate_text(text, source_lang, target_lang):
#     if source_lang != target_lang:
#         translator = GoogleTranslator(source=source_lang, target=target_lang)
#         translated_text = translator.translate(text)
#         return translated_text
#     return text

# @cl.on_chat_start
# async def start():
#     chain = qa_bot()
#     msg = cl.Message(content="Starting the bot.....")
#     await msg.send()
#     msg.content = "Hi, Welcome to the Mines Bot. What is your query?"
#     await msg.update()
#     cl.user_session.set("chain", chain)

# @cl.on_message
# async def main(message):
#     chain = qa_bot()
#     cb = cl.AsyncLangchainCallbackHandler(
#         stream_final_answer=True, answer_prefix_tokens=["FINAL", "ANSWER"]
#     )
#     cb.answer_reached = True

#     user_input = message
#     source_language = detect_language(user_input)
#     target_language = 'en'

#     translated_input = translate_text(user_input, source_language, target_language)
#     res = await chain.acall(translated_input, callbacks=[cb])

#     model_response = res["result"]
#     sources = res["source_documents"]

#     translated_response = translate_text(model_response, target_language, source_language)

#     response = f"Original Query: {user_input}\nTranslated Query: {translated_input}\nTranslated Answer: {translated_response}"

#     # if sources:
#     #     response += f"\nSources:" + str(sources)
#     # else:
#     #     response += f"\nNo Sources Found"

#     await cl.Message(content=response).send()

from langchain import PromptTemplate
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import CTransformers
from langchain.chains import RetrievalQA
import chainlit as cl
from langdetect import detect
from deep_translator import GoogleTranslator

DB_FAISS_PATH = "vectorstores/db_faiss"

def set_custom_prompt():
    custom_prompt_template = """ Use the following pieces of information to answer the user's question. IF you don't know the answer, please just say that you don't know the answer, don't try to make up an answer.

 Context : {context}
 Question: {question}

 Only returns the helpful answer below and nothing else.
 Helpful answer:

 """
    prompt = PromptTemplate(template=custom_prompt_template, input_variables=['context', 'question'])
    return prompt

def load_llm():
    llm = CTransformers(
        model="llama-2-7b-chat.ggmlv3.q8_0.bin",
        model_type="llama",
        max_new_tokens=512,
        temperature=0.5
    )
    return llm

def retrieval_qa_chain(llm, prompt, db):
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=db.as_retriever(search_kwargs={'k': 2}),
        return_source_documents=True,
        chain_type_kwargs={'prompt': prompt}
    )
    return qa_chain

def qa_bot():
    embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2', model_kwargs={'device': 'cpu'})

    db = FAISS.load_local(DB_FAISS_PATH, embeddings)
    llm = load_llm()
    qa_prompt = set_custom_prompt()
    qa = retrieval_qa_chain(llm, qa_prompt, db)

    return qa

def detect_language(text):
    try:
        language = detect(text)
        return language
    except:
        return 'en'  # Default to English if language detection fails

def translate_text(text, source_lang, target_lang):
    if source_lang != target_lang:
        translator = GoogleTranslator(source=source_lang, target=target_lang)
        translated_text = translator.translate(text)
        return translated_text
    return text

@cl.on_chat_start
async def start():
    chain = qa_bot()
    msg = cl.Message(content="Starting the bot.....")
    await msg.send()
    msg.content = "Hi, Welcome to the Mines Bot. What is your query?"
    await msg.update()
    cl.user_session.set("chain", chain)

@cl.on_message
async def main(message):
    chain = qa_bot()
    cb = cl.AsyncLangchainCallbackHandler(
        stream_final_answer=True, answer_prefix_tokens=["FINAL", "ANSWER"]
    )
    cb.answer_reached = True

    user_input = message
    source_language = detect_language(user_input)
    target_language = 'en'

    translated_input = translate_text(user_input, source_language, target_language)
    res = await chain.acall(translated_input, callbacks=[cb])

    model_response = res["result"]
    #sources = res["source_documents"]

    translated_response = translate_text(model_response, target_language, source_language)

    response = ""
    
    if source_language != 'en':
        response += f"Original Query: {user_input}\n"
        response += f"Translated Query: {translated_input}\n"
        response += f"Translated Answer: {translated_response}\n"
    else:
        response += translated_response
    
    # if sources:
    #     response += f"\nSources:" + str(sources)
    # else:
    #     response += f"\nNo Sources Found"

    await cl.Message(content=response).send()

