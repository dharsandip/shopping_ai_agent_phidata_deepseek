
from phi.agent import Agent
from phi.tools.firecrawl import FirecrawlTools
from phi.model.groq import Groq
import streamlit as st
from dotenv import load_dotenv

load_dotenv()


def recommend(product, color, special_feature, budget):
    
    agent = Agent(
        name="Shopping recommendations",
        model=Groq(id="deepseek-r1-distill-llama-70b"),
        instructions=[
            "You are a product recommender agent specializing in finding products that match user preferences.",
            "Prioritize finding products that satisfy as many user requirements as possible, but ensure a minimum match of 80%.",
            "Search for products only from authentic and trusted e-commerce websites such as Google Shopping, Amazon, Walmart and other reputable platforms.",
            "Verify that each product recommendation is in stock and available for purchase.",
            "Clearly mention the key attributes of each product (e.g., price, brand, features) in the response.",
            "Format the recommendations neatly, show only top 5 results.",
        ],
        tools=[FirecrawlTools()],
        markdown=True
    )
    
    
    output = agent.run(
        "Please find the "+ product + " with " + color +" color "+ "and " + special_feature + " and " + budget + " budget"
    )

    return output.content



def main():
    
    html_temp = """
    <div style="background-color:yellow;padding:8px">
    <h2 style="color:gray;text-align:center;">Shopping Recommendations by AI Agent</h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)    
    
    st.image("app_logo.jpg", width=300)
   
    product = st.text_input("**Product**","")
    color = st.text_input("**Color**","")
    special_feature = st.text_input("**Specific requirements**","")
    budget = st.text_input("**Budget**","")
    
    st.markdown("""
    <style>
    div.stButton > button:first-child {
        background-color: #DD3300;
        color:#eeffee;
    }
    </style>""", unsafe_allow_html=True)

    if st.button("Recommend"):
        results = recommend(product, color, special_feature, budget)
        st.success('Results {}'.format(results))
    

if __name__=='__main__':
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    