import streamlit as st
import os
from main import Article
from datetime import datetime

# Force light theme
st.set_page_config(
    page_title="FauxNews - AI News Generator",
    page_icon="📰",
    layout="wide",
    initial_sidebar_state="expanded"
)
st.markdown("""
<style>
body, .stApp {
    background: #f4f4f4 !important;
    color: #222 !important;
}
.site-header {
    background: #fff;
    border-bottom: 2px solid #e3e8ee;
    padding: 2rem 0 1rem 0;
    margin-bottom: 2.5rem;
    text-align: center;
    box-shadow: 0 2px 8px rgba(0,0,0,0.03);
}
.site-title {
    font-size: 2.8rem;
    font-weight: 900;
    color: #1a1a1a;
    font-family: 'Georgia', serif;
    margin-bottom: 0.2rem;
    letter-spacing: 1px;
}
.site-desc {
    font-size: 1.2rem;
    color: #555;
    font-family: 'Arial', sans-serif;
    margin-bottom: 0.5rem;
}
.article-container {
    background: #fff;
    border-radius: 10px;
    padding: 2.5rem 2rem;
    box-shadow: 0 4px 16px rgba(0,0,0,0.08);
    margin-bottom: 2rem;
    max-width: 800px;
    margin-left: auto;
    margin-right: auto;
}
.headline {
    font-size: 2.3rem;
    font-weight: 800;
    color: #1a1a1a;
    margin-bottom: 1.2rem;
    line-height: 1.15;
    font-family: 'Georgia', serif;
}
.byline {
    color: #555;
    font-size: 1.1rem;
    margin-bottom: 1.2rem;
    border-bottom: 1px solid #eee;
    padding-bottom: 1rem;
    font-family: 'Arial', sans-serif;
}
.article-body {
    font-size: 1.18rem;
    line-height: 1.7;
    color: #232323;
    text-align: justify;
    font-family: 'Georgia', serif;
    margin-bottom: 2rem;
}
.stButton>button {
    background: #457b9d;
    color: white;
    border: none;
    padding: 0.6rem 1.2rem;
    border-radius: 5px;
    font-size: 1.1rem;
    font-weight: 600;
    margin: 0.25rem 0;
}
.stButton>button:hover {
    background: #1d3557;
}
</style>
""", unsafe_allow_html=True)

def main():
    st.markdown("""
    <div class="site-header">
        <div class="site-title">FauxNews</div>
        <div class="site-desc">AI-Powered Fake News Generator for Media Literacy Education</div>
    </div>
    """, unsafe_allow_html=True)
    with st.sidebar:
        st.markdown("### Article Controls")
        topic = st.text_input(
            "News Topic",
            placeholder="e.g., Kamala Harris, Climate Change, UFOs, Big Tech",
            help="Enter the main topic for your fake news article"
        )
        if st.button("Generate Article", type="primary", use_container_width=True):
            if topic:
                with st.spinner("Generating your fake news article..."):
                    try:
                        article = Article(topic)
                        st.session_state.article = article
                        st.success("Article generated successfully!")
                    except Exception as e:
                        st.error(f"Error generating article: {str(e)}")
            else:
                st.warning("Please enter a topic first!")
        if 'article' in st.session_state:
            st.markdown("---")
            st.markdown("### Regenerate Components")
            if st.button("Regenerate Everything", use_container_width=True):
                with st.spinner("Regenerating article..."):
                    try:
                        st.session_state.article.regenerate()
                        st.session_state.article = st.session_state.article
                        st.success("Article regenerated!")
                    except Exception as e:
                        st.error(f"Error regenerating: {str(e)}")
            col1, col2 = st.columns(2)
            with col1:
                if st.button("Headline"):
                    with st.spinner("Regenerating headline..."):
                        st.session_state.article.regenerate_component("title")
                        st.session_state.article = st.session_state.article
                        st.success("Headline updated!")
                if st.button("Body"):
                    with st.spinner("Regenerating article body..."):
                        st.session_state.article.regenerate_component("body")
                        st.session_state.article = st.session_state.article
                        st.success("Article body updated!")
                if st.button("Author"):
                    st.session_state.article.regenerate_component("author")
                    st.session_state.article = st.session_state.article
                    st.success("Author updated!")
            with col2:
                if st.button("Network"):
                    st.session_state.article.regenerate_component("network")
                    st.session_state.article = st.session_state.article
                    st.success("Network updated!")
                if st.button("Image"):
                    with st.spinner("Generating new image..."):
                        st.session_state.article.regenerate_component("image")
                        st.session_state.article = st.session_state.article
                        st.success("Image updated!")
                if st.button("Date"):
                    st.session_state.article.regenerate_component("release_date")
                    st.session_state.article = st.session_state.article
                    st.success("Date updated!")
    if 'article' in st.session_state:
        article = st.session_state.article
        article_html = f'''
<div class="article-container">
    <h1 class="headline">{article.title}</h1>
    <div class="byline">
        By <strong>{article.author}</strong> | {article.news_network} | {article.release_date}
    </div>
    <div>
        <img src="{article.image_url or 'https://via.placeholder.com/800x400/cccccc/666666?text=No+Image'}" style="width:100%;border-radius:8px;margin-bottom:1.5rem;" alt="AI-Generated News Image"/>
    </div>
    <div class="article-body">{article.body}</div>
</div>
'''
        st.markdown(article_html, unsafe_allow_html=True)
        with st.expander("Article Metadata"):
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Topic", article.topic)
            with col2:
                st.metric("Author", article.author)
                st.metric("Network", article.news_network)
                st.metric("Date", article.release_date)
    else:
        st.markdown("""
        <h2>Welcome to FauxNews!</h2>
        <p>This educational tool demonstrates how AI can generate realistic-looking fake news articles. 
        Use it to understand media literacy and the potential risks of AI-generated content.</p>
        <h3>How to use:</h3>
        <ol>
            <li>Enter a news topic in the sidebar</li>
            <li>Click "Generate Article" to create your fake news story</li>
            <li>Use the regenerate buttons to modify specific components</li>
        </ol>
        <div style="background: #fff3cd; border: 1px solid #ffeaa7; padding: 1rem; border-radius: 5px; margin-top: 1rem;">
            <strong>⚠️ Educational Purpose Only:</strong> This tool is designed for media literacy education 
            and understanding AI capabilities. Always verify information from reliable sources.
        </div>
        """, unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #666; font-size: 0.9rem;">
        <p>🔬 Built for experimentation, education, and media literacy awareness</p>
        <p>⚠️ This tool demonstrates AI capabilities and should be used responsibly</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main() 