import streamlit as st

st.set_page_config(
    page_title="Bellagio Bazaar - AI-Powered E-commerce Platform",
    page_icon="🔱",
    layout="wide"
)
logo_url = "static/bellagio.png"
st.sidebar.image(logo_url, use_column_width=True)

st.header("Welcome to Bellagio Bazaar", divider="orange")
st.sidebar.info("**DISCLAIMER:** This workshop uses Amazon Bedrock foundation models and is not intended to collect any personally identifiable information (PII) from users. Please do not provide any PII when interacting with this workshop. The content generated by this workshop is for informational purposes only.")

st.write("### What is Bellagio Bazaar?")
st.markdown(
    """
    Bellagio Bazaar is an advanced e-commerce platform that leverages the power of AWS Bedrock, Claude 3 Sonnet, and pgvector on Aurora PostgreSQL. Our platform offers comprehensive insights into product trends, inventory management, and personalized recommendations.
    
    Explore our suite of AI-powered tools designed to revolutionize your e-commerce experience:
    """
)
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("🔍 Product Insights")
    st.write("""
    Dive deep into your product data with our interactive dashboards. Analyze top-selling items, trending categories, and revenue metrics at a glance.
    
    - Top 10 Trending Categories
    - Highest Grossing Products
    - Best Selling Products by Category
    - General Spending Habits Analysis
    """)

with col2:
    st.subheader("🤖 AI-Powered Recommendations")
    st.write("""
    Harness the power of AI to generate personalized product recommendations and answer complex queries about your inventory.
    
    - Product Similarity Search
    - Personalized AI Recommendations
    - Natural Language Query Processing
    """)

with col3:
    st.subheader("📊 Knowledge Base & Bedrock Agents")
    st.write("""
    Leverage our advanced knowledge base and Bedrock Agents to get instant answers to your business questions and automate complex tasks.
    
    - Upload and Query Policy Documents
    - Interact with Bedrock Agents
    - Perform AI-assisted Tasks and Actions
    """)

st.write("---")
st.markdown("""### Sample Product Categories""")
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.image("static/automotive.png")
    st.write("Automotive Tools")

with col2:
    st.image("static/Sports.png")
    st.write("Sports")

with col3:
    st.image("static/Electronics.png")
    st.write("Electronics")

with col4:
    st.image("static/HomeDecor_1.png")
    st.write("Home Decor")

with col5:
    st.image("static/Accessories_1.png")
    st.write("Accessories")

st.write("---")
st.subheader("🚀 Getting Started")
st.markdown(
    """
    1. **Product Insights**: Start by exploring our Product Insights dashboard to get a comprehensive view of your e-commerce performance.
    2. **Product Recommendations**: Use our AI-powered recommendation engine to discover similar products and get personalized suggestions.
    3. **Upload Documents**: Enhance our knowledge base by uploading relevant documents to improve query responses.
    4. **Query Knowledge Base**: Ask questions about your product catalog, inventory, or business policies.
    5. **Bedrock Agents**: Interact with Bedrock agents for agentic workflows.
    """
)

st.write("---")
st.subheader("🛠️ Technologies Powering Bellagio Bazaar")
tech_col1, tech_col2 = st.columns(2)

with tech_col1:
    st.write("**AWS Services:**")
    st.markdown("""
    - Amazon Bedrock (Claude 3 and Titan Text)
    - Aurora PostgreSQL with pgvector
    - AWS Lambda
    - Amazon S3
    """)

with tech_col2:
    st.write("**Key Features:**")
    st.markdown("""
    - Vector Similarity Search
    - Retrieval Augmented Generation (RAG)
    - Natural Language Processing
    - Real-time Market Insights
    - Interactive Visualizations
    """)

st.write("---")
st.subheader("📚 Key Concepts")
con_col1, con_col2, con_col3 = st.columns(3)

with con_col1:
    st.write("Why use [pgvector](https://github.com/pgvector/pgvector) with Aurora PostgreSQL?")
    st.markdown("""
    - Flexible deployment with managed vector search capabilities across Aurora PostgreSQL Provisioned, Serverless or Global Database
    - Integrated vector and relational data storage with ML/Gen AI features accessible via SQL
    - Enterprise-grade robustness with comprehensive data integrity and security features
    - Full SQL support for complex queries on both relational and vector data
    - Enhanced scalability with optimized vector search performance and indexing options
    """)

with con_col2:
    st.write("[Knowledge Bases for Amazon Bedrock](https://aws.amazon.com/bedrock/knowledge-bases/)")
    st.markdown("""
    - Enhances foundation models with private data access for precise responses
    - Enables secure integration of company-specific information into AI applications
    - Supports Retrieval Augmented Generation (RAG) for contextually relevant outputs
    - Streamlines the process of creating and maintaining custom knowledge bases
    """)

with con_col3:
    st.write("[Agents for Amazon Bedrock](https://aws.amazon.com/bedrock/agents/)")
    st.markdown("""
    - Automates complex workflows and repetitive tasks using AI
    - Securely connects to company data sources for accurate responses
    - Augments user requests with relevant information from knowledge bases
    - Enables creation of specialized AI agents for various business tasks
    """)

st.write("---")
st.subheader('✍️ Retrieval Augmented Generation (RAG) Architecture')
st.image("static/RAG_Arch.png", use_column_width="auto", caption="RAG Architecture")
st.write("---")