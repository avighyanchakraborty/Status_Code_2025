import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Engineering Roadmap 2024-25",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        color: #1f77b4;
        margin-bottom: 2rem;
    }
    .sub-header {
        font-size: 1.5rem;
        font-weight: bold;
        color: #2c3e50;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }
    .branch-card {
        background-color: #f8f9fa;
        padding: 1.5rem;
         color: #000000;
        border-radius: 10px;
        border-left: 5px solid #1f77b4;
        margin: 1rem 0;
    }
    .metric-card {
        background-color: #e3f2fd;
        padding: 1rem;
        border-radius: 8px;
        text-align: center;
        margin: 0.5rem;
    }
    .sidebar .sidebar-content {
        background-color: #f8f9fa;
    }
</style>
""", unsafe_allow_html=True)

# Navigation
def main():
    st.markdown('<h1 class="main-header">🎓 Engineering Roadmap 2024-25</h1>', unsafe_allow_html=True)
    
    # Sidebar navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox(
        "Choose a section:",
        ["🏠 Home", "🖥️ CSE", "💻 IT", "🔌 ECE", "📚 Semester Roadmap", "🎯 GATE Preparation", "📊 Analytics", "📞 Contact"]
    )
    
    if page == "🏠 Home":
        show_home()
    elif page == "🖥️ CSE":
        show_cse()
    elif page == "💻 IT":
        show_it()
    elif page == "🔌 ECE":
        show_ece()
    elif page == "📚 Semester Roadmap":
        show_semester_roadmap()
    elif page == "🎯 GATE Preparation":
        show_gate_preparation()
    elif page == "📊 Analytics":
        show_analytics()
    elif page == "📞 Contact":
        show_contact()

def show_home():
    st.markdown('<h2 class="sub-header">Welcome to Engineering Roadmap 2024-25</h2>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="branch-card">
            <h3>🖥️ Computer Science Engineering (CSE)</h3>
            <p>Focus on software development, algorithms, and computer systems</p>
            <ul>
                <li>Data Structures & Algorithms</li>
                <li>Operating Systems</li>
                <li>Computer Networks</li>
                <li>Database Systems</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="branch-card">
            <h3>💻 Information Technology (IT)</h3>
            <p>Focus on web development, databases, and information systems</p>
            <ul>
                <li>Web Technologies</li>
                <li>Database Management</li>
                <li>Software Engineering</li>
                <li>Information Security</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="branch-card">
            <h3>🔌 Electronics & Communication (ECE)</h3>
            <p>Focus on electronics, communication systems, and signal processing</p>
            <ul>
                <li>Digital Electronics</li>
                <li>Communication Systems</li>
                <li>Signal Processing</li>
                <li>VLSI Design</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Key Features
    st.markdown('<h3 class="sub-header">Key Features</h3>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        - **Complete Course Structure**: 8-semester detailed curriculum
        - **Weightage Analysis**: Subject-wise importance and scoring
        - **Semester Roadmap**: Year-wise learning progression
        - **GATE Preparation**: 12-month systematic study plan
        """)
    
    with col2:
        st.markdown("""
        - **Assessment Criteria**: Detailed grading system
        - **Career Development**: Industry paths and opportunities
        - **Learning Resources**: Books, platforms, and tools
        - **Interactive Analytics**: Visual data representation
        """)
    
    # Quick Stats
    st.markdown('<h3 class="sub-header">Quick Statistics</h3>', unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Semesters", "8", "Per Branch")
    
    with col2:
        st.metric("Core Subjects", "15-20", "Per Branch")
    
    with col3:
        st.metric("Elective Options", "8-12", "Per Branch")
    
    with col4:
        st.metric("Project Work", "4-6", "Per Branch")

def show_cse():
    st.markdown('<h2 class="sub-header">🖥️ Computer Science Engineering (CSE)</h2>', unsafe_allow_html=True)
    
    # Semester tabs
    tab1, tab2, tab3, tab4 = st.tabs(["Foundation (Sem 1-2)", "Core CS (Sem 3-4)", "Advanced CS (Sem 5-6)", "Specialization (Sem 7-8)"])
    
    with tab1:
        st.markdown("### Foundation Years (25% Weightage)")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### Semester 1")
            subjects = {
                "Engineering Mathematics I": 8,
                "Engineering Physics": 4,
                "Engineering Chemistry": 3,
                "Programming Fundamentals": 6,
                "Digital Logic Design": 4
            }
            
            for subject, weight in subjects.items():
                st.progress(weight/1000)
                st.write(f"**{subject}** ({weight}%)")
        
        with col2:
            st.markdown("#### Semester 2")
            subjects = {
                "Engineering Mathematics II": 8,
                "Data Structures": 10,
                "Object-Oriented Programming": 6,
                "Computer Organization": 8
            }
            
            for subject, weight in subjects.items():
                st.progress(weight/1000)
                st.write(f"**{subject}** ({weight}%)")
    
    with tab2:
        st.markdown("### Core CS Years (30% Weightage)")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### Semester 3")
            subjects = {
                "Database Management Systems": 6,
                "Operating Systems": 8,
                "Computer Networks": 7,
                "Software Engineering": 5,
                "Theory of Computation": 4
            }
            
            for subject, weight in subjects.items():
                st.progress(weight/1000)
                st.write(f"**{subject}** ({weight}%)")
        
        with col2:
            st.markdown("#### Semester 4")
            subjects = {
                "Advanced Data Structures": 5,
                "System Programming": 6,
                "Web Technologies": 4,
                "Elective I": 3
            }
            
            for subject, weight in subjects.items():
                st.progress(weight/1000)
                st.write(f"**{subject}** ({weight}%)")
    
    with tab3:
        st.markdown("### Advanced CS Years (25% Weightage)")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### Semester 5")
            subjects = {
                "Advanced Algorithms": 8,
                "Computer Architecture": 6,
                "Distributed Systems": 5,
                "Elective II": 6
            }
            
            for subject, weight in subjects.items():
                st.progress(weight/1000)
                st.write(f"**{subject}** ({weight}%)")
        
        with col2:
            st.markdown("#### Semester 6")
            subjects = {
                "Compiler Design": 5,
                "Computer Graphics": 4,
                "Elective III": 6,
                "Project Work I": 10
            }
            
            for subject, weight in subjects.items():
                st.progress(weight/1000)
                st.write(f"**{subject}** ({weight}%)")
    
    with tab4:
        st.markdown("### Specialization Years (20% Weightage)")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### Semester 7")
            subjects = {
                "Advanced Topics": 10,
                "Internship": 5,
                "Research Methodology": 5
            }
            
            for subject, weight in subjects.items():
                st.progress(weight/100)
                st.write(f"**{subject}** ({weight}%)")
        
        with col2:
            st.markdown("#### Semester 8")
            subjects = {
                "Capstone Project": 15,
                "Professional Ethics": 3,
                "Elective IV": 2
            }
            
            for subject, weight in subjects.items():
                st.progress(weight/1000)
                st.write(f"**{subject}** ({weight}%)")

def show_it():
    st.markdown('<h2 class="sub-header">💻 Information Technology (IT)</h2>', unsafe_allow_html=True)
    
    # Semester tabs
    tab1, tab2, tab3, tab4 = st.tabs(["Foundation (Sem 1-2)", "Core IT (Sem 3-4)", "Advanced IT (Sem 5-6)", "Specialization (Sem 7-8)"])
    
    with tab1:
        st.markdown("### Foundation Years (20% Weightage)")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### Semester 1")
            subjects = {
                "Engineering Mathematics I": 8,
                "Programming Fundamentals": 8,
                "Digital Electronics": 4
            }
            
            for subject, weight in subjects.items():
                st.progress(weight/100)
                st.write(f"**{subject}** ({weight}%)")
        
        with col2:
            st.markdown("#### Semester 2")
            subjects = {
                "Engineering Mathematics II": 8,
                "Data Structures & Algorithms": 10,
                "Object-Oriented Programming": 8
            }
            
            for subject, weight in subjects.items():
                st.progress(weight/100)
                st.write(f"**{subject}** ({weight}%)")
    
    with tab2:
        st.markdown("### Core IT Years (35% Weightage)")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### Semester 3")
            subjects = {
                "Database Management Systems": 8,
                "Web Development": 9,
                "Computer Networks": 6,
                "Software Engineering": 6
            }
            
            for subject, weight in subjects.items():
                st.progress(weight/100)
                st.write(f"**{subject}** ({weight}%)")
        
        with col2:
            st.markdown("#### Semester 4")
            subjects = {
                "Information Security": 8,
                "Mobile Application Development": 7,
                "Cloud Computing": 6
            }
            
            for subject, weight in subjects.items():
                st.progress(weight/100)
                st.write(f"**{subject}** ({weight}%)")
    
    with tab3:
        st.markdown("### Advanced IT Years (30% Weightage)")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### Semester 5")
            subjects = {
                "Advanced Web Technologies": 8,
                "Data Science": 7,
                "DevOps & Automation": 6,
                "Elective I": 4
            }
            
            for subject, weight in subjects.items():
                st.progress(weight/100)
                st.write(f"**{subject}** ({weight}%)")
        
        with col2:
            st.markdown("#### Semester 6")
            subjects = {
                "Business Intelligence": 6,
                "Cybersecurity": 5,
                "Elective II": 4,
                "Project Work I": 10
            }
            
            for subject, weight in subjects.items():
                st.progress(weight/100)
                st.write(f"**{subject}** ({weight}%)")
    
    with tab4:
        st.markdown("### Specialization Years (15% Weightage)")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### Semester 7")
            subjects = {
                "Advanced Topics": 8,
                "Industry Internship": 7
            }
            
            for subject, weight in subjects.items():
                st.progress(weight/100)
                st.write(f"**{subject}** ({weight}%)")
        
        with col2:
            st.markdown("#### Semester 8")
            subjects = {
                "Capstone Project": 10,
                "Professional Development": 5
            }
            
            for subject, weight in subjects.items():
                st.progress(weight/100)
                st.write(f"**{subject}** ({weight}%)")

def show_ece():
    st.markdown('<h2 class="sub-header">🔌 Electronics & Communication Engineering (ECE)</h2>', unsafe_allow_html=True)
    
    # Semester tabs
    tab1, tab2, tab3, tab4 = st.tabs(["Foundation (Sem 1-2)", "Core ECE (Sem 3-4)", "Advanced ECE (Sem 5-6)", "Specialization (Sem 7-8)"])
    
    with tab1:
        st.markdown("### Foundation Years (25% Weightage)")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### Semester 1")
            subjects = {
                "Engineering Mathematics I": 8,
                "Engineering Physics": 6,
                "Basic Electronics": 6,
                "Programming for Engineers": 5
            }
            
            for subject, weight in subjects.items():
                st.progress(weight/100)
                st.write(f"**{subject}** ({weight}%)")
        
        with col2:
            st.markdown("#### Semester 2")
            subjects = {
                "Engineering Mathematics II": 8,
                "Digital Electronics": 8,
                "Analog Electronics": 8
            }
            
            for subject, weight in subjects.items():
                st.progress(weight/100)
                st.write(f"**{subject}** ({weight}%)")
    
    with tab2:
        st.markdown("### Core ECE Years (30% Weightage)")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### Semester 3")
            subjects = {
                "Signals & Systems": 7,
                "Electromagnetic Theory": 7,
                "Communication Systems": 8,
                "Microprocessors & Microcontrollers": 6
            }
            
            for subject, weight in subjects.items():
                st.progress(weight/100)
                st.write(f"**{subject}** ({weight}%)")
        
        with col2:
            st.markdown("#### Semester 4")
            subjects = {
                "Digital Signal Processing": 8,
                "VLSI Design": 3,
                "Wireless Communication": 5,
                "Elective I": 4
            }
            
            for subject, weight in subjects.items():
                st.progress(weight/100)
                st.write(f"**{subject}** ({weight}%)")
    
    with tab3:
        st.markdown("### Advanced ECE Years (25% Weightage)")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### Semester 5")
            subjects = {
                "Advanced Communication": 8,
                "Embedded Systems": 6,
                "Elective II": 6
            }
            
            for subject, weight in subjects.items():
                st.progress(weight/100)
                st.write(f"**{subject}** ({weight}%)")
        
        with col2:
            st.markdown("#### Semester 6")
            subjects = {
                "Advanced Signal Processing": 6,
                "Elective III": 6,
                "Elective IV": 4,
                "Project Work II": 9
            }
            
            for subject, weight in subjects.items():
                st.progress(weight/100)
                st.write(f"**{subject}** ({weight}%)")
    
    with tab4:
        st.markdown("### Specialization Years (20% Weightage)")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### Semester 7")
            subjects = {
                "Advanced Topics": 10,
                "Industry Internship": 5,
                "Research Work": 5
            }
            
            for subject, weight in subjects.items():
                st.progress(weight/100)
                st.write(f"**{subject}** ({weight}%)")
        
        with col2:
            st.markdown("#### Semester 8")
            subjects = {
                "Capstone Project": 15,
                "Professional Ethics": 3,
                "Elective V": 2
            }
            
            for subject, weight in subjects.items():
                st.progress(weight/100)
                st.write(f"**{subject}** ({weight}%)")

def show_semester_roadmap():
    st.markdown('<h2 class="sub-header">📚 Semester-wise Roadmap</h2>', unsafe_allow_html=True)
    
    # Year-wise tabs
    tab1, tab2, tab3, tab4 = st.tabs(["Year 1", "Year 2", "Year 3", "Year 4"])
    
    with tab1:
        st.markdown("### Year 1: Foundation Building")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### Semester 1")
            st.markdown("""
            - **Mathematics**: Calculus, Linear Algebra, Differential Equations
            - **Physics**: Mechanics, Waves, Optics
            - **Chemistry**: Atomic Structure, Chemical Bonding
            - **Programming**: C Programming Fundamentals
            - **Digital Logic**: Boolean Algebra, Combinational Circuits
            """)
        
        with col2:
            st.markdown("#### Semester 2")
            st.markdown("""
            - **Mathematics**: Probability, Statistics, Numerical Methods
            - **Data Structures**: Arrays, Linked Lists, Stacks, Queues
            - **OOP**: Java/C++ Programming
            - **Computer Organization**: CPU Design, Memory Hierarchy
            """)
    
    with tab2:
        st.markdown("### Year 2: Core Concepts")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### Semester 3")
            st.markdown("""
            - **Databases**: ER Model, SQL, Normalization
            - **Operating Systems**: Process Management, Memory Management
            - **Networks**: OSI Model, TCP/IP, Routing
            - **Software Engineering**: SDLC, UML, Testing
            """)
        
        with col2:
            st.markdown("#### Semester 4")
            st.markdown("""
            - **Advanced Data Structures**: Trees, Graphs, Algorithms
            - **System Programming**: Assembly, System Calls
            - **Web Technologies**: HTML, CSS, JavaScript
            - **Electives**: Specialized topics
            """)
    
    with tab3:
        st.markdown("### Year 3: Advanced Topics")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### Semester 5")
            st.markdown("""
            - **Advanced Algorithms**: Graph Algorithms, Dynamic Programming
            - **Computer Architecture**: Advanced CPU Design
            - **Distributed Systems**: Distributed Algorithms
            - **Electives**: Advanced topics
            """)
        
        with col2:
            st.markdown("#### Semester 6")
            st.markdown("""
            - **Compiler Design**: Lexical Analysis, Parsing
            - **Computer Graphics**: 2D/3D Graphics
            - **Electives**: Specialized topics
            - **Project Work**: Industry projects
            """)
    
    with tab4:
        st.markdown("### Year 4: Specialization & Projects")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### Semester 7")
            st.markdown("""
            - **Advanced Topics**: Specialized electives
            - **Internship**: Industry experience
            - **Research**: Research methodology
            """)
        
        with col2:
            st.markdown("#### Semester 8")
            st.markdown("""
            - **Capstone Project**: Major project work
            - **Professional Ethics**: Engineering ethics
            - **Electives**: Final specialization
            """)

def show_gate_preparation():
    st.markdown('<h2 class="sub-header">🎯 GATE Preparation Roadmap</h2>', unsafe_allow_html=True)
    
    # Phase-wise tabs
    tab1, tab2, tab3, tab4 = st.tabs(["Phase 1 (Months 1-3)", "Phase 2 (Months 4-6)", "Phase 3 (Months 7-9)", "Phase 4 (Months 10-12)"])
    
    with tab1:
        st.markdown("### Phase 1: Foundation Building")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### Week 1-4: Engineering Mathematics")
            st.markdown("**Weightage: 15% | Target Score: 12-15**")
            st.markdown("""
            - **Linear Algebra** (5%): Matrices, Determinants, Vector Spaces
            - **Calculus** (4%): Limits, Continuity, Differentiation
            - **Probability & Statistics** (3%): Probability Distributions
            - **Discrete Mathematics** (3%): Logic, Sets, Relations
            """)
        
        with col2:
            st.markdown("#### Week 5-8: Programming & Data Structures")
            st.markdown("**Weightage: 15% | Target Score: 12-15**")
            st.markdown("""
            - **C Programming** (5%): Data Types, Operators, Control Structures
            - **Data Structures** (10%): Arrays, Linked Lists, Trees, Graphs
            """)
        
        st.markdown("#### Week 9-12: Algorithms")
        st.markdown("**Weightage: 10% | Target Score: 8-10**")
        st.markdown("""
        - **Searching & Sorting** (3%): Linear Search, Binary Search, Quick Sort
        - **Graph Algorithms** (4%): BFS, DFS, Shortest Path
        - **Dynamic Programming** (3%): Memoization, Tabulation
        """)
    
    with tab2:
        st.markdown("### Phase 2: Core Subjects")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### Week 13-16: Computer Organization")
            st.markdown("**Weightage: 10% | Target Score: 8-10**")
            st.markdown("""
            - **Digital Logic** (3%): Boolean Algebra, Combinational Circuits
            - **CPU Design** (4%): ALU, Control Unit, Registers
            - **Memory Hierarchy** (3%): Cache, RAM, ROM, Virtual Memory
            """)
        
        with col2:
            st.markdown("#### Week 17-20: Operating Systems")
            st.markdown("**Weightage: 10% | Target Score: 8-10**")
            st.markdown("""
            - **Process Management** (3%): Process Scheduling, Synchronization
            - **Memory Management** (4%): Paging, Segmentation, Virtual Memory
            - **File Systems** (3%): File Organization, Directory Structure
            """)
        
        st.markdown("#### Week 21-24: Database Systems")
        st.markdown("**Weightage: 8% | Target Score: 6-8**")
        st.markdown("""
        - **Data Modeling** (3%): ER Model, Relational Model, Normalization
        - **SQL** (3%): DDL, DML, DCL, Advanced Queries
        - **Database Design** (2%): Indexing, Query Optimization
        """)
    
    with tab3:
        st.markdown("### Phase 3: Advanced Topics")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### Week 25-28: Computer Networks")
            st.markdown("**Weightage: 8% | Target Score: 6-8**")
            st.markdown("""
            - **Network Models** (3%): OSI Model, TCP/IP Model
            - **Data Link Layer** (2%): Error Detection, Flow Control
            - **Network Layer** (3%): Routing Algorithms, IP Addressing
            """)
        
        with col2:
            st.markdown("#### Week 29-32: Theory of Computation")
            st.markdown("**Weightage: 6% | Target Score: 4-6**")
            st.markdown("""
            - **Automata Theory** (3%): DFA, NFA, Regular Expressions
            - **Computability** (2%): Turing Machines, Halting Problem
            - **Complexity Theory** (1%): P, NP, NP-Complete Problems
            """)
        
        st.markdown("#### Week 33-36: Software Engineering")
        st.markdown("**Weightage: 4% | Target Score: 3-4**")
        st.markdown("""
        - **Software Development Life Cycle** (2%): Waterfall, Agile, Spiral Models
        - **Software Testing** (1%): Unit Testing, Integration Testing
        - **Project Management** (1%): Estimation, Scheduling, Risk Management
        """)
    
    with tab4:
        st.markdown("### Phase 4: Practice & Revision")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### Week 37-40: Mock Tests")
            st.markdown("""
            - **Daily**: 1 full-length mock test
            - **Weekly**: Topic-wise revision
            - **Analysis**: Identify weak areas
            """)
        
        with col2:
            st.markdown("#### Week 41-44: Previous Year Papers")
            st.markdown("""
            - **Daily**: 1 previous year paper
            - **Weekly**: Pattern analysis
            - **Focus**: Frequently asked topics
            """)
        
        st.markdown("#### Week 45-48: Final Revision")
        st.markdown("""
        - **Daily**: Quick revision of formulas
        - **Weekly**: Full-length tests
        - **Focus**: Time management
        """)

def show_analytics():
    st.markdown('<h2 class="sub-header">📊 Analytics Dashboard</h2>', unsafe_allow_html=True)
    
    # Sample data for analytics
    branches = ['CSE', 'IT', 'ECE']
    foundation_weightage = [25, 20, 25]
    core_weightage = [30, 35, 30]
    advanced_weightage = [25, 30, 25]
    specialization_weightage = [20, 15, 20]
    
    # Create DataFrame
    df = pd.DataFrame({
        'Branch': branches,
        'Foundation': foundation_weightage,
        'Core': core_weightage,
        'Advanced': advanced_weightage,
        'Specialization': specialization_weightage
    })
    
    # Weightage comparison chart
    st.markdown("### Weightage Comparison Across Branches")
    
    fig = px.bar(df, x='Branch', y=['Foundation', 'Core', 'Advanced', 'Specialization'],
                 title="Course Weightage Distribution",
                 barmode='group')
    fig.update_layout(height=500)
    st.plotly_chart(fig, use_container_width=True)
    
    # Pie chart for CSE
    st.markdown("### CSE Course Distribution")
    
    cse_data = {
        'Foundation': 25,
        'Core CS': 30,
        'Advanced CS': 25,
        'Specialization': 20
    }
    
    fig_pie = px.pie(values=list(cse_data.values()), names=list(cse_data.keys()),
                     title="CSE Course Weightage")
    st.plotly_chart(fig_pie, use_container_width=True)
    
    # Semester progression
    st.markdown("### Semester Progression")
    
    semesters = list(range(1, 9))
    cse_progression = [25, 25, 30, 30, 25, 25, 20, 20]
    it_progression = [20, 20, 35, 35, 30, 30, 15, 15]
    ece_progression = [25, 25, 30, 30, 25, 25, 20, 20]
    
    fig_line = go.Figure()
    fig_line.add_trace(go.Scatter(x=semesters, y=cse_progression, mode='lines+markers', name='CSE'))
    fig_line.add_trace(go.Scatter(x=semesters, y=it_progression, mode='lines+markers', name='IT'))
    fig_line.add_trace(go.Scatter(x=semesters, y=ece_progression, mode='lines+markers', name='ECE'))
    
    fig_line.update_layout(title="Semester-wise Weightage Progression",
                          xaxis_title="Semester",
                          yaxis_title="Weightage (%)",
                          height=500)
    st.plotly_chart(fig_line, use_container_width=True)

def show_contact():
    st.markdown('<h2 class="sub-header">📞 Contact & Support</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Get in Touch")
        st.markdown("""
        - **Email**: support@engineeringroadmap.com
        - **Phone**: +1-234-567-8900
        - **Address**: Engineering Roadmap HQ, Tech City, TC 12345
        """)
        
        st.markdown("### Office Hours")
        st.markdown("""
        - **Monday - Friday**: 9:00 AM - 6:00 PM
        - **Saturday**: 10:00 AM - 4:00 PM
        - **Sunday**: Closed
        """)
    
    with col2:
        st.markdown("### Contact Form")
        
        with st.form("contact_form"):
            name = st.text_input("Name")
            email = st.text_input("Email")
            subject = st.selectbox("Subject", ["General Inquiry", "Technical Support", "Feedback", "Partnership"])
            message = st.text_area("Message")
            submit_button = st.form_submit_button("Send Message")
            
            if submit_button:
                st.success("Thank you for your message! We'll get back to you soon.")
    
    st.markdown("### FAQ")
    
    with st.expander("How to use this roadmap?"):
        st.markdown("""
        1. Choose your engineering branch from the sidebar
        2. Explore the semester-wise course structure
        3. Check the weightage and assessment criteria
        4. Follow the GATE preparation plan if needed
        5. Use the analytics dashboard for insights
        """)
    
    with st.expander("What are the career prospects?"):
        st.markdown("""
        - **CSE**: Software Engineer, Data Scientist, System Architect
        - **IT**: Full-stack Developer, DevOps Engineer, IT Consultant
        - **ECE**: Electronics Engineer, Communication Engineer, Embedded Systems Developer
        """)
    
    with st.expander("How to prepare for GATE?"):
        st.markdown("""
        1. Start with foundation subjects (Mathematics, Programming)
        2. Focus on core subjects (OS, Networks, Databases)
        3. Practice with mock tests and previous papers
        4. Maintain a study schedule and track progress
        """)

if __name__ == "__main__":
    main() 