# cv/views.py
from django.shortcuts import render

def resume_view(request):
    # All resume data is stored in Python variables here
    profile = {
        'name': 'NIRMAL BOGHARA',
        'location': 'Brooklyn, NY',
        'email': 'nb3964@nyu.edu',
        'phone': '+1347-628-3769',
        'portfolio': 'https://nirmal-aiswe.vercel.app', # Replace with your actual URL
        'linkedin': 'https://www.linkedin.com/in/nirmal-boghara/',   # Replace with your actual URL
        'github': 'https://github.com/nirmal141'        # Replace with your actual URL
    }

    education_list = [
        {
            'degree': 'MS in Computer Science',
            'university': 'New York University',
            'location': 'New York, NY',
            'date': 'Expected May 2026',
            'courses': [
                'Algorithms', 'Deep Learning', 'Database Systems', 
                'Machine Learning', 'Big Data'
            ]
        },
        {
            'degree': 'BE in Computer Engineering',
            'university': 'University of Mumbai',
            'location': 'Maharashtra, India',
            'date': 'Jun 2024',
            'courses': [
                'Operating Systems', 'Machine Learning', 'Artificial Intelligence',
                'Applied Cryptography', 'Data Structures'
            ]
        }
    ]

    experience_list = [
        {
            'title': 'Al Innovator Intern II',
            'company': 'Chewy',
            'location': 'Boston, MA',
            'date': 'June 2025 - Aug 2025',
            'description': [
                'Led the build of an Agentic Copilot for Marketing & Sponsored Ads Team to create rich cohorts of customers for precision marketing and campaign backtesting by creating a rich knowledge base of customer touchpoints within Chewy.',
                'Designed and deployed 2 successful pilot campaigns reducing unsubscribe rate by 2%.',
                'Developed multiple ML Propensity models to predict churn rate, unsubscribe rate, repurchase on a SKU level, saving 16 million dollars in annual revenue loss from just 1 campaign.',
                'Delivered rich cohorts to onboard more vendors which resulted in extra ROAS of almost 100%.',
                'Presented pilot outcomes to CEO and executive leadership of Chewy.'
            ]
        },
        {
            'title': 'Technical Ambassador',
            'company': 'Qualcomm',
            'location': 'New York, NY',
            'date': 'Feb 2025 - Present',
            'description': [
                'Developed a low-latency Al teaching assistant utilizing Distilled Qwen 1.5B Local LLMs and ONNX Runtime, providing offline access to rural educators while achieving an impressive accuracy rate of 92% through Agentic RAG architecture.',
                'Building hybrid agentic architecture of top professors & educators to provide 24/7 access to their knowledge and guidance using their open source learning(Github, Courses, Youtube, Podcasts, Papers) where users can switch between online/offline modes.',
                'Mentored 100+ students at the Edge Al Hackathon at NEU Seattle.'
            ]
        },
        {
            'title': 'Software Engineering Intern',
            'company': 'Bitnine',
            'location': 'San Francisco, CA (Remote)',
            'date': 'Apr 2024 - June 2024',
            'description': [
                'Optimized PostgreSQL databases with Oracle compatibility on AWS, improving complex query performance by 23% for enterprise-scale fintech applications.',
                'Optimized & enhanced ODBC C driver for PostgreSQL databases.',
                'Resolved 20+ critical issues in the Python driver for Apache AGE project as an open-source contributor, enhancing its stability and reliability.',
                'Initiated Oracle OCI driver development in C for PostgreSQL databases from scratch, achieving compatibility with Oracle and scalability, and providing a framework for subsequent phases.'
            ]
        },
        {
            'title': 'Software Development Engineering Intern',
            'company': 'Feat Systems',
            'location': 'Maharashtra, India',
            'date': 'May 2023 - Aug 2023',
            'description': [
                'Enhanced Java/Spring Boot applications by applying Agile methodologies and optimizing CI/CD workflows with Jira and GitHub, leading to a 15% reduction in customer complaints and improved release efficiency.',
                'Implemented scalable MySQL solutions and developed SDLC documentation, leveraging GitHub for version control and Jira for task management, resulting in a 30% faster onboarding process and sustained team productivity.'
            ]
        },
        {
            'title': 'Full Stack Developer Intern',
            'company': 'Goldenmace IT Solutions',
            'location': 'Maharashtra, India',
            'date': 'May 2022 - July 2022',
            'description': [
                'Engineered a full-stack TypeScript/Svelte dashboard with Node.js backend, optimizing data retrieval latency by 30% and improving user engagement for SaaS clients through intuitive UI/UX.',
                'Implemented TypeScript and Svelte for code optimization and caching mechanisms, boosting dashboard performance by 30%.',
                'Integrated PostgreSQL and MongoDB for data storage, ensuring fast and efficient data retrieval.'
            ]
        }
    ]

    skills = {
        'Languages': 'Java, Python, C#, SQL, JavaScript, HTML, R, Golang',
        'Frameworks & Libraries': 'Django, Node.js, React.js, Svelte, TypeScript, Springboot, PHP, Three.js, WebGPU',
        'Tools': 'Git, AWS, Kubernetes, Docker, MS Excel, Jira, Microsoft Azure, Matlab',
        'Machine Learning': 'TensorFlow, PyTorch, Langchain, Scikit-learn, NumPy, Pandas, Matplotlib, ONNX Runtime',
        'Data': 'PostgreSQL, MySQL, MongoDB, Apache Kafka, Hadoop, Tableau, PowerBI, Scala, GraphQL'
    }

    projects_list = [
        {
            'name': 'FitFarm - Smart Agriculture System',
            'tech': 'Machine Learning, Python, IoT, JavaScript',
            'description': [
                'Trained ML algorithms (SVM, Random Forest) using Python, TensorFlow, and Scikit-learn to predict the most suitable crops according to soil conditions with 93% accuracy.',
                'Published a research paper in the IJRASET.'
            ],
            'link': 'https://github.com/nirmal141/FitFarm'
        },
        {
            'name': 'Automated Employee Tracking System',
            'tech': 'Python, NumPy, TensorFlow, PyTorch, YoloV7',
            'description': [
                'Built a computer vision system using YOLOv7 and TensorFlow, automating attendance tracking for 200+ employees and reducing manual effort by 50%.',
                'Analyzed the face recognition attendance system using Python, NumPy, and Pandas.'
            ],
            'link': 'https://github.com/nirmal141/Automated-Employee-Tracking-System'
        },
        {
            'name': 'Fittify - One Stop Health Platform',
            'tech': 'MERN Stack',
            'description': [
                'Engineered a comprehensive health solution using React and Node, piloting it with 150 students.',
                'Achieved 95% user satisfaction and 25% improvement in health metrics through personalized medical record tracking, diet, and workout plans.',
                'Successfully scaled to 500+ users while maintaining performance and intuitive UI made with Tailwind CSS.'
            ],
            'link': 'https://github.com/nirmal141' 
        }
    ]
    
    awards_list = [
        'Currently an Al Business Fellow at Perplexity, and a Technical Project Manager at HackNYU.',
        '3x Hackathon Winner - Built Al Agents, Al Hedge Fund, Tutor AI.',
        'National Level Baseball Player at MIT-WPU, India - Runners up in Semi Finals representing University of Mumbai.'
    ]

    context = {
        'profile': profile,
        'education': education_list,
        'experience': experience_list,
        'skills': skills,
        'projects': projects_list,
        'awards': awards_list,
    }

    return render(request, 'cv/resume.html', context)