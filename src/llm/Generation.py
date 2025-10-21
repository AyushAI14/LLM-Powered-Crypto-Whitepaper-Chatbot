from src.vector_store.MilvusDB import Vectordb
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
from src.logging import logger
import os

load_dotenv()


class Generation:
    def __init__(self):
        self.api_key_groq = os.getenv("GROQ_API_KEY")
        self.api_key_gemini = os.getenv("GEMINI_API_KEY")
        self.Vdb = Vectordb()

    def groq(self, query, temperature,model_name='openai/gpt-oss-20b'):
        logger.info(f'Groq had been Intialized : Model Name = {model_name}')
        context = self.Vdb.query(query_text=query)
        llm = ChatGroq(groq_api_key=self.api_key_groq, model_name=model_name,temperature=temperature)
        prompt = f"""
                You are a crypto research assistant specialized in analyzing and explaining cryptocurrency whitepapers.

        Your task is to answer the user’s question using the provided CONTEXT.  
        The CONTEXT contains extracted sections from one or more whitepapers.  

        -----------------------
        CONTEXT:
        {context}
        -----------------------

        USER QUESTION:
        {query}

        -----------------------

        Guidelines:
        1. Use only the information from the context as your primary source of truth.
        2. If the answer is implied but not explicitly stated, you may infer it — but keep it reasonable and clearly indicate inference (e.g., “This likely means…”).
        3. Use professional, research-style language. Be clear, concise, and factual.
        4. When mentioning key entities (e.g., token names, consensus mechanism, or team), clearly identify them.
        5. If the context doesn’t contain the answer, say:  
          “The whitepaper doesn’t clearly mention this detail.”
        6. Structure long answers with short sections or bullet points when needed.

        Output format:
        - Give a **direct answer first**
        - Then briefly explain how it was derived from the context
        - If relevant, mention any **related insights** (tokenomics, use case, roadmap, etc.)

        Example Style:
        > The project uses a Proof-of-Stake consensus.  
        > This is stated in the whitepaper’s “Consensus Mechanism” section, where validators stake tokens to propose and validate blocks.

        Now generate your final response:

        """
        response = llm.invoke([prompt])
        print('LLM Is Generating ...')
        return response.content
        
    def gemini(self, query, temperature,model_name='gemini-2.5-flash-lite'):
        logger.info(f'gemini had been Intialized : Model Name = {model_name}')
        context = self.Vdb.query(query)
        llm = ChatGoogleGenerativeAI(api_key=self.api_key_gemini, model=model_name,temperature=temperature)
        prompt = f"""
        You are an expert crypto research assistant analyzing cryptocurrency whitepapers.
        
        Context:
        {context}
        
        User Question:
        {query}
        
        Instructions:
        - Use the above context as your main reference to answer the question.
        - If the answer is partly implied, explain it clearly in your own words.
        - Prefer useful, informative answers over saying “not mentioned”.
        - Be precise and factual — do not invent information not supported by the context.
        - If absolutely nothing in the context relates to the question, then and only then say:
          "The whitepaper does not clearly mention this detail."
        - Present the response in a concise, structured format (use bullet points or short paragraphs).
        """


        response = llm.invoke([prompt])
        print('LLM Is Generating ...')
        return response.content
        
g = Generation()
# print(g.groq("What is Bitcoin?",0.2))      
# print(g.gemini("What is Bitcoin's consensus mechanism?",0.9)) 