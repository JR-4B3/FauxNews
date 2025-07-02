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
    background: #e6eaf2 !important;
    color: #fff !important;
}
.site-header {
    background: #0b234a;
    border-bottom: 4px solid #c00;
    padding: 2rem 0 1rem 0;
    margin-bottom: 2.5rem;
    text-align: left;
    box-shadow: 0 2px 8px rgba(0,0,0,0.08);
    display: flex;
    align-items: center;
    gap: 2rem;
}
.site-logo {
    width: 90px;
    height: 90px;
    border-radius: 10px;
    background: #fff;
    object-fit: contain;
    box-shadow: 0 2px 8px rgba(0,0,0,0.10);
    margin-left: 2rem;
}
.site-title {
    font-size: 2.8rem;
    font-weight: 900;
    color: #fff;
    font-family: 'Georgia', serif;
    margin-bottom: 0.2rem;
    letter-spacing: 1px;
}
.site-desc {
    font-size: 1.2rem;
    color: #fff;
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
    color: #0b234a;
}
.headline {
    font-size: 2.3rem;
    font-weight: 800;
    color: #0b234a;
    margin-bottom: 1.2rem;
    line-height: 1.15;
    font-family: 'Georgia', serif;
}
.byline {
    color: #c00;
    font-size: 1.1rem;
    margin-bottom: 1.2rem;
    border-bottom: 1px solid #eee;
    padding-bottom: 1rem;
    font-family: 'Arial', sans-serif;
}
.article-body {
    font-size: 1.18rem;
    line-height: 1.7;
    color: #222;
    text-align: justify;
    font-family: 'Georgia', serif;
    margin-bottom: 2rem;
}
.stButton>button {
    background: #c00;
    color: white;
    border: none;
    padding: 0.6rem 1.2rem;
    border-radius: 5px;
    font-size: 1.1rem;
    font-weight: 600;
    margin: 0.25rem 0;
}
.stButton>button:hover {
    background: #0b234a;
}
/* Make all headings in the main area black */
h1, h2, h3, h4, h5, h6 {
    color: #000 !important;
}
.stMarkdown.sidebar-heading h3 {
    color: #fff !important;
}
.sidebar-heading {
    color: #fff !important;
}
.site-header-bg {
    background: #0b234a;
    border-bottom: 4px solid #c00;
    padding: 2rem 0 1rem 0;
    margin-bottom: 2.5rem;
    box-shadow: 0 2px 8px rgba(0,0,0,0.08);
    border-radius: 0 0 12px 12px;
}
.site-header-bg-outer {
    background: #0b234a;
    border-bottom: 4px solid #c00;
    padding: 2rem 0 1rem 0;
    margin-bottom: 2.5rem;
    box-shadow: 0 2px 8px rgba(0,0,0,0.08);
    border-radius: 0 0 12px 12px;
    width: 100vw;
    position: relative;
    left: 50%;
    right: 50%;
    margin-left: -50vw;
    margin-right: -50vw;
}
.site-logo-img {
    margin-left: 2rem;
    border-radius: 10px;
    background: #fff;
    box-shadow: 0 2px 8px rgba(0,0,0,0.10);
    object-fit: contain;
}
/* Make all main area text black, including emotion classes */
.stApp .st-emotion-cache-p5msec,
.stApp .eqpbllx2,
.stApp .st-emotion-cache-1clstc5,
.stApp .eqpbllx1,
.stApp .st-emotion-cache-q8sbsg,
.stApp .e1nzilvr5 {
    color: #000 !important;
}
</style>
""", unsafe_allow_html=True)

def main():
    # FauxNews header with white background and black text
    header_cols = st.columns([1, 5])
    with header_cols[0]:
        st.image("FauxNews_logo.webp", width=90)
    with header_cols[1]:
        st.markdown(
            """
            <div class="fauxnews-title">FauxNews</div>
            <div class="fauxnews-desc">AI-Powered Fake News Generator for Media Literacy Education</div>
            """,
            unsafe_allow_html=True
        )
    st.markdown(
        """
        <style>
        .fauxnews-title {
            color: #000;
            font-size: 2.5rem;
            font-weight: 800;
            margin-bottom: 0.2rem;
            margin-left: 1.5rem;
        }
        .fauxnews-desc {
            color: #000;
            font-size: 1.1rem;
            margin-left: 1.5rem;
        }
        /* Make all main area text black, including emotion classes */
        .stApp .st-emotion-cache-p5msec,
        .stApp .eqpbllx2,
        .stApp .st-emotion-cache-1clstc5,
        .stApp .eqpbllx1,
        .stApp .st-emotion-cache-q8sbsg,
        .stApp .e1nzilvr5 {
            color: #000 !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    with st.sidebar:
        st.markdown('<h3 class="sidebar-heading">Article Controls</h3>', unsafe_allow_html=True)
        st.markdown("""
        <style>
        /* Make all sidebar text white */
        [data-testid="stSidebar"] *,
        .st-emotion-cache-p5msec,
        .eqpbllx2,
        .st-emotion-cache-1clstc5,
        .eqpbllx1 {
            color: #fff !important;
        }
        /* Make sidebar headings white */
        [data-testid="stSidebar"] h1,
        [data-testid="stSidebar"] h2,
        [data-testid="stSidebar"] h3,
        [data-testid="stSidebar"] h4,
        [data-testid="stSidebar"] h5,
        [data-testid="stSidebar"] h6 {
            color: #fff !important;
        }
        </style>
        """, unsafe_allow_html=True)
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
            st.markdown('<h3 class="sidebar-heading">Regenerate Components</h3>', unsafe_allow_html=True)
            if st.button("Regenerate Everything", type="primary", use_container_width=True):
                with st.spinner("Regenerating article..."):
                    try:
                        st.session_state.article.regenerate()
                        st.success("Article regenerated!")
                    except Exception as e:
                        st.error(f"Error regenerating: {str(e)}")
            # All regeneration buttons vertically aligned and full width
            if st.button("Headline", use_container_width=True):
                with st.spinner("Regenerating headline..."):
                    st.session_state.article.regenerate_component("title")
                    st.success("Headline updated!")
            if st.button("Body", use_container_width=True):
                with st.spinner("Regenerating article body..."):
                    st.session_state.article.regenerate_component("body")
                    st.success("Article body updated!")
            if st.button("Image", use_container_width=True):
                with st.spinner("Generating new image..."):
                    st.session_state.article.regenerate_component("image")
                    st.success("Image updated!")
    if 'article' in st.session_state:
        article = st.session_state.article
        # Try to display the image using st.image for compatibility
        image_url = article.image_url or 'https://via.placeholder.com/800x400/cccccc/666666?text=No+Image'
        article_html = f'''
<div class="article-container">
    <h1 class="headline">{article.title}</h1>
    <div class="byline">
        By <strong>{article.author}</strong> | {article.news_network} | {article.release_date}
    </div>
</div>
'''
        st.markdown(article_html, unsafe_allow_html=True)
        try:
            st.image(image_url, use_column_width=True, caption="AI-Generated News Image")
        except Exception:
            st.image("https://via.placeholder.com/800x400/cccccc/666666?text=Image+Not+Available", use_column_width=True, caption="Image could not be loaded.")
        st.markdown(f'<div class="article-body">{article.body}</div>', unsafe_allow_html=True)
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
        <div style="color: #000;">
        <h2>Welcome to FauxNews!</h2>
        <p>This educational tool demonstrates how AI can generate realistic-looking fake news articles. 
        Use it to understand media literacy and the potential risks of AI-generated content.</p>
        <h3>How to use:</h3>
        <ol>
            <li>Enter a news topic in the sidebar</li>
            <li>Click "Generate Article" to create your fake news story</li>
            <li>Use the regenerate buttons to modify specific components</li>
        </ol>
        <div style="background: #fff3cd; border: 1px solid #ffeaa7; padding: 1rem; border-radius: 5px; margin-top: 1rem; color: #000;">
            <strong>⚠️ Educational Purpose Only:</strong> This tool is designed for media literacy education 
            and understanding AI capabilities. Always verify information from reliable sources.
        </div>
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