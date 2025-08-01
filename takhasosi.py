# -*- coding: utf-8 -*-
from collections import OrderedDict
import streamlit as st
import pandas as pd

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="منصة تخصصي",
    page_icon="app_icon.jpg",
    layout="centered"
)

# ------------------ APPLE TOUCH ICON + META TAGS ------------------
st.markdown("""
    <link rel="icon" href="app_icon.jpg">
    <link rel="apple-touch-icon" href="app_icon.jpg">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black">
    <meta name="apple-mobile-web-app-title" content="منصة تخصصي">
""", unsafe_allow_html=True)

# ------------------ HIDE DEFAULT STREAMLIT MENU ------------------
# Hide Streamlit default menu, footer, and header
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)



st.set_page_config(page_title="منصه تخصصي", layout="centered")
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700&display=swap');

        body {
            direction: rtl;
            text-align: right;
            background-color: #F9F7F1;
        }

        * {
            font-family: 'Tajawal', sans-serif !important;
        }

        .main > div:first-child > div > div > div > div {
            display: flex;
            justify-content: center;
        }

        h1, h2 {
            text-align: center !important;
            font-weight: 700;
            color: #2C2C2C;
            text-shadow: 0px 1px 4px rgba(0, 0, 0, 0.1);
        }

        label, .stNumberInput label {
            font-size: 16px;
            font-weight: 500;
            color: #444;
        }

        .stTextInput > div > div > input,
        .stNumberInput > div > div > input {
            text-align: right;
            font-size: 15px;
        }

        .stNumberInput {
            margin-bottom: 20px;
        }
    </style>
""", unsafe_allow_html=True)




st.markdown("""
<h1 style='text-align: right;'> ابحث عن التخصص المناسب لك في جامعة الكويت؟</h1>
""", unsafe_allow_html=True)


st.subheader("أدخل درجاتك")
gpa = st.number_input(" معدل الثانوية العامة ٪", min_value=0.0, max_value=100.0, step=0.01, format="%g")
math = st.number_input(" درجة القدرات – رياضيات ٪", min_value=0.0, max_value=100.0, step=0.01, format="%g")
english = st.number_input(" درجة القدرات – إنجليزي ٪", min_value=0.0, max_value=100.0, step=0.01, format="%g")
arabic = st.number_input(" درجة القدرات – عربي ٪  (إذا كانت مطلوبة)", min_value=0.0, max_value=100.0, step=0.01, format="%g")
french = st.number_input(" درجة القدرات – فرنسي ٪ (إذا كانت مطلوبة)", min_value=0.0, max_value=100.0, step=0.01, format="%g")




st.subheader("اختيار مجال اهتمامك")
interest = st.selectbox(" شنو نوع التخصصات اللي تميل لها أكثر؟", [
    "المجال الطبي والصحي 🏥",
    "الهندسة والتقنية ⚙️",
    "التحليل والرياضيات 📊",
    "القانون والقراءة 📚",
    "الفنون والتصميم 🎨",
    "العلوم الطبيعية 🧪",
    "التربية والتعليم 👩‍🏫"
])

# ----------(ALL 15 COLLEGES) ----------
colleges = OrderedDict({
    "كلية الطب": {
      "stream": "علمي",
      "weights": {"gpa": 75, "english": 15, "math": 10},
      "min_score": 95.68,
      "interests": ["المجال الطبي والصحي 🏥"],
      "desc": "تهدف الكلية إلى إعداد أطباء مؤهلين تأهيلاً علميًا وعمليًا عالي المستوى، قادرين على تشخيص وعلاج الأمراض، والمساهمة في تطوير الرعاية الصحية والبحث الطبي.",
      "years": 7
    },

    "كلية طب الأسنان": {
      "stream": "علمي",
      "weights": {"gpa": 75, "english": 15, "math": 10},
      "min_score": 95.09,
      "interests": ["المجال الطبي والصحي 🏥"],
      "desc": "تهدف الكلية إلى تأهيل أطباء أسنان متخصصين في تشخيص ومعالجة أمراض الفم والأسنان واللثة، باستخدام أحدث التقنيات والأساليب العلاجية، للمساهمة في تعزيز صحة الفم والأسنان على مستوى الفرد والمجتمع.",
      "years": 6
    },
    "كلية الصيدلة": {
      "stream": "علمي",
      "weights": {"gpa": 70, "english": 15, "math": 15},
      "min_score": 93,
      "interests": ["المجال الطبي والصحي 🏥"],
      "desc": "تُعنى الكلية بتدريب طلابها على علوم الأدوية وتصنيعها، وفهم التفاعلات الدوائية وآلية عمل العقاقير، لإعداد صيادلة مؤهلين يسهمون بفعالية في تقديم الرعاية الدوائية وتحسين الصحة العامة.",
      "years": 6
    },

    "كلية العلوم الطبية المساعدة": {
      "stream": "علمي",
      "weights": {"gpa": 70, "english": 20, "math": 10},
      "min_score": 85.68,  # أقل مسار: إدارة المعلومات الصحية
      "interests": ["المجال الطبي والصحي 🏥"],
      "desc": "تُعنى الكلية بتأهيل طلبة في تخصصات طبية مساندة تشمل العلاج الطبيعي والمهني، المختبرات، الأشعة، وإدارة المعلومات الصحية، بما يواكب احتياجات النظام الصحي الحديث.",
      "years": 4,
      "paths": [
        {"name": "العلاج المهني", "min_score": 90.06},
        {"name": "علوم المختبرات الطبية", "min_score": 87.83},
        {"name": "العلاج الطبيعي", "min_score": 91.28},
        {"name": "تكنولوجيا الأشعة التشخيصية", "min_score": 88.57},
        {"name": " المعلوماتيه إدارة المعلومات الصحية", "min_score": 85.68},
        {"name": "التمريض", "min_score": 85.68}
      ]
    },

    "كلية الصحة العامة": {
      "stream": "علمي",
      "weights": {"gpa": 70, "english": 15, "math": 15},
      "min_score": 83.82,
      "interests": ["المجال الطبي والصحي 🏥"],
      "desc": "تهدف الكلية إلى تأهيل مختصين في مجال الوقاية من الأمراض وتعزيز الصحة العامة من خلال التعليم والبحث وخدمة المجتمع، وذلك لتطوير السياسات الصحية ورفع الوعي المجتمعي.",
      "years": 4
},

   "كلية العمارة": {
    "stream": "علمي",
    "weights": {"gpa": 70, "english": 15, "math": 15},
    "min_score": 66.29,
    "interests": ["الفنون والتصميم 🎨"],
    "desc": "توفر الكلية مسارات متعددة لتأهيل الطلبة في مجالات العمارة، العمارة الداخلية، والتصميم المرئي، من خلال مزيج من الإبداع الفني والدراسة التقنية لتطوير بيئات عمرانية حديثة ومتكاملة.",
    "years": 5,
    "paths": [
        {"name": "التصميم المرئي", "min_score": 66.29},
        {"name": "العمارة الداخلية", "min_score": 72.71},
        {"name": "العمارة", "min_score": 80.02}
    ]
},


    "كلية الهندسة والبترول": {
      "stream": "علمي",
      "weights": {"gpa": 65, "english": 10, "math": 20},
      "min_score": 63.17,  # أقل حد لأي مسار داخل الكلية
      "interests": ["الهندسة والتقنية ⚙️", "التحليل والرياضيات 📊"],
      "desc": "تقدّم الكلية برامج تخصصية في مجالات الهندسة المدنية، الكهربائية، الميكانيكية، الكيميائية، الصناعية، هندسة الحاسوب، وهندسة البترول، لتأهيل مهندسين قادرين على الابتكار والمساهمة في تطوير البنية التحتية والصناعية في الكويت.",
      "years": 5,
      "paths": [
        {"name": "هندسة البترول", "min_score": 77.42},
        {"name": "هندسة كمبيوتر", "min_score": 76.48},
        {"name": "الهندسة الصناعية والنظم الإدارية", "min_score": 65.07},
        {"name": "الهندسة الكهربائية", "min_score": 70.1},
        {"name": "الهندسة الكيميائية", "min_score": 66.42},
        {"name": "الهندسة المدنية", "min_score": 72.5},
        {"name": "الهندسة الميكانيكية", "min_score": 63.17}
        ]
    },

    "كلية العلوم(علوم رياضية وطبيعية)": {
      "stream": "علمي",
      "weights": {"gpa": 100},
      "min_score": 70.0,  # أقل تخصص
      "interests": ["العلوم الطبيعية 🧪", "التحليل والرياضيات 📊"],
      "desc": "توفر تخصصات في مجالات العلوم الأساسية مثل الرياضيات، الفيزياء، الكيمياء، وعلوم الحياة، مع تطبيقات بحثية وعلمية.",
      "years": 4,
      "paths": [
        {"name": "الرياضيات", "min_score": 73.72},
        {"name": "الفيزياء الاساسية", "min_score": 79.63},
        {"name": "الفيزياء الهندسية", "min_score": 74.33},
        {"name": "الليزر والاتصالات البصرية", "min_score": 74.33},
        {"name": "الإحصاء وبحوث العمليات", "min_score": 70.0},
        {"name": "علوم في الامن السبراني", "min_score": 86.18},
        {"name": "الكيمياء", "min_score": 78.43},
        {"name": "الجيولوجيا", "min_score": 82.61},
        {"name": "الإحصاء التطبيقي", "min_score": 73.41},
        {"name": "الكيمياء التطبيقية", "min_score": 76.82},
        {"name": "الفيزياء الهندسية", "min_score": 74.8},
        {"name": "الاستشعار عن بعد", "min_score": 74.8},
        {"name": "علوم الحاسوب", "min_score": 79.69},
        {"name": "الرياضيات المالية والاكتوارية", "min_score": 71.88},
        {"name": "علوم البحار", "min_score": 78.8}
      ]
    },
        "كلية العلوم(علوم بيولوجية)": {
      "stream": "علمي",
      "weights": {"gpa": 100},
      "min_score": 82.08,  # أقل تخصص
      "interests": ["العلوم الطبيعية 🧪", "التحليل والرياضيات 📊"],
      "desc": "توفر تخصصات في مجالات العلوم الأساسية مثل الرياضيات، الفيزياء، الكيمياء، وعلوم الحياة، مع تطبيقات بحثية وعلمية.",
      "years": 4,
      "paths": [
        {"name": "بيولوجيا الحيوان", "min_score": 84.4},
        {"name": "بيولوجيا النبات", "min_score": 82.08},
        {"name": "علم الميكرو بيولوجيا", "min_score": 93.2},
        {"name": "علم الكيمياء الحيوية", "min_score": 91.28},
        {"name": "علم البيولوجيا الجزيئية", "min_score": 90.21}
      ]
    },

    "كلية العلوم الحياتية": {
      "stream": "علمي",
      "weights": {"gpa": 70, "english": 15, "math": 15},
      "min_score": 57.4,  # أقل مسار: علوم المعلومات
      "interests": ["العلوم الطبيعية 🧪", "الفنون والتصميم 🎨", "التحليل والرياضيات 📊"],
      "desc": "تقدم الكلية مجموعة من التخصصات التطبيقية المرتبطة بالحياة والصحة والبيئة، مثل التغذية، اضطرابات التواصل، إدارة التقنية البيئية، وعلوم المعلومات، لتأهيل خريجين يسهمون في تعزيز جودة الحياة والتنمية المستدامة.",
      "years": 4,
      "paths": [
        {"name": "علم التغذية", "min_score": 81.1},
        {"name": "اضطرابات التواصل", "min_score": 81.84},
        {"name": "علوم البيئية", "min_score": 58.46},
        {"name": "علوم المعلومات", "min_score": 57.4}،
        {"name": "علوم الأغذية", "min_score": 74.1},
        {"name": "علم البيانات والذكاء الاصطناعي", "min_score": 72.24}
        ]
      },

    "كلية العلوم الإدارية": {
    "stream": "علمي",
    "weights": {"gpa": 70, "english": 15, "math": 15},
    "min_score": 57.3,  # أقل معدل (الإدارة العامة – علمي)
    "interests": ["التحليل والرياضيات 📊"],
    "desc": "تُعد الكلية واحدة من أبرز الكليات في مجال الأعمال، وتهدف إلى إعداد خريجين متخصصين في المحاسبة، الإدارة، الاقتصاد، التمويل، التسويق، نظم المعلومات، والعمليات والإمدادات، ليواكبوا متطلبات سوق العمل الحديث.",
    "years": 4,
    "paths": [
        {"name": "التسويق", "min_score": 57.27},
        {"name": "الإدارة العامة", "min_score": 61.32},
        {"name": "نظم المعلومات الإدارية", "min_score": 56.48},
        {"name": "التمويل والمنشآت المالية", "min_score": 60.6},
        {"name": "الاقتصاد", "min_score": 60.15},
        {"name": "المحاسبة", "min_score": 73.18},
        {"name": "إدارة العمليات والإمدادات", "min_score": 64.68},
        {"name": "الادارة", "min_score": 63.03}
    ]
},
    "كلية العلوم الإدارية": {
    "stream": "أدبي",
    "weights": {"gpa": 70, "english": 15, "math": 15},
    "min_score": 57.3,  # أقل معدل (الإدارة العامة – علمي)
    "interests": ["التحليل والرياضيات 📊"],
    "desc": "تُعد الكلية واحدة من أبرز الكليات في مجال الأعمال، وتهدف إلى إعداد خريجين متخصصين في المحاسبة، الإدارة، الاقتصاد، التمويل، التسويق، نظم المعلومات، والعمليات والإمدادات، ليواكبوا متطلبات سوق العمل الحديث.",
    "years": 4,
    "paths": [
        {"name": "التسويق", "min_score": 64.64},
        {"name": "الإدارة العامة", "min_score": 63.44},
        {"name": "نظم المعلومات الإدارية", "min_score": 61.64},
        {"name": "التمويل والمنشآت المالية", "min_score": 61.59},
        {"name": "الاقتصاد", "min_score": 69.4},
        {"name": "المحاسبة", "min_score": 70.58},
        {"name": "إدارة العمليات والإمدادات", "min_score": 67.75},
        {"name": "الادارة", "min_score": 62.55}
    ]
},


    "كلية الآداب": {
    "weights": {
      "stream": "أدبي",
        "default": {"gpa": 85, "arabic": 15},
        "اللغة الإنجليزية": {"gpa": 85, "english": 15},
        "اللغة الفرنسية وثقافتها": {"gpa": 85, "french": 15}  # Assuming you add a field for French aptitude
    },
    "min_score": 66.35,  # Minimum for "الإعلام"
    "interests": ["القانون والقراءة 📚"],
    "desc": "توفر الكلية برامج متنوعة في مجالات العلوم الإنسانية واللغات والإعلام، مما يُمكّن الطلبة من تطوير مهاراتهم الفكرية والتواصلية والثقافية لخدمة المجتمع في مجالات متعددة.",
    "years": 4,
    "paths": [
        {"name": "اللغة العربية", "min_score": 66.35},
        {"name": "اللغة الإنجليزية", "min_score": 66.79},
        {"name": "اللغة الفرنسية وثقافتها", "min_score": 66.59},
        {"name": "التاريخ", "min_score": 66.78},
        {"name": "الفلسفة", "min_score": 69.4},
        {"name": "الإعلام", "min_score": 66.37}
    ]
},

    "كلية الحقوق": {
      "stream": "أدبي",
      "weights": {"gpa": 100},
      "min_score": 85.14,
      "interests": ["القانون والقراءة 📚"],
      "desc": "دراسة القانون المدني، والجنائي، والدستوري وغيرها من الأنظمة القانونية.",
      "years": 4
    },

    "كلية الشريعة": {
      "stream": "أدبي",
      "weights": {"gpa": 85, "arabic": 15},
      "min_score": 66.33,  # أقل درجة بين المسارات
      "interests": ["القانون والقراءة 📚", "التربية والتعليم 👩‍🏫"],
      "desc": "تُعنى الكلية بتأهيل الطلبة في مجالات العلوم الشرعية، من الفقه وأصوله إلى العقيدة والحديث والتفسير، بهدف إعداد كوادر متخصصة في التعليم والدعوة والعمل القضائي والبحث العلمي.",
      "years": 4,
      "paths": [
        {"name": "الفقه وأصول الفقه", "min_score": 66.66},
        {"name": "الفقه المقارن والسياسة الشرعية", "min_score": 66.53},
        {"name": "التفسير والحديث", "min_score": 66.33},
        {"name": "العقيدة والدعوة", "min_score": 68.1}
      ]
   },
    "كلية التربية": {
    "stream": "أدبي",
    "weights": {"gpa": 80, "english": 10, "arabic": 10},
    "min_score": 77.95,  # Minimum is for علمي رياضيات ابتدائي
    "interests": ["التربية والتعليم 👩‍🏫"],
    "desc": "تهدف الكلية إلى إعداد معلمين متخصصين في المراحل التعليمية المختلفة، من رياض الأطفال إلى المرحلة الثانوية، في مجالات علمية وأدبية متعددة تلبي احتياجات النظام التربوي.",
    "years": 4,
    "paths": [
        {"name": "برنامج متوسط/ثانوي – اللغة الإنجليزية ", "min_score": 79.88},
        {"name": "برنامج متوسط/ثانوي – اللغة العربية ", "min_score": 77.95},
        {"name": "برنامج متوسط/ثانوي –الدراسات الاسلامية ", "min_score": 81.85},
        {"name": "برنامج متوسط/ثانوي – الاجتماعيات/الجغرافيا ", "min_score": 83.17},
        {"name": "برنامج متوسط/ثانوي – الاجتماعيات/التاريخ ", "min_score": 84.02},
        {"name": "برنامج متوسط/ثانوي – الاجتماعيات/الفلسفة ", "min_score": 81.85},
        {"name": "برنامج متوسط/ثانوي – علم النفس/علوم اجتماعية ", "min_score": 84.96},
        {"name": "برنامج رياض الأطفال", "min_score": 84.63},
        {"name": "برنامج الابتدائي – الدراسات الإسلامية ", "min_score": 82.61},
        {"name": "برنامج الابتدائي – اجتماعيات ", "min_score": 84.74},
        {"name": "برنامج الابتدائي – اللغة العربية ", "min_score": 79.36},
        {"name": "برنامج متوسط– اللغة الإنجليزية ", "min_score": 80.41}
        
    ]
},
    "كلية التربية": {
    "stream": "علمي",
    "weights": {"gpa": 80, "english": 7.5, "math": 7.5, "arabic": 5},
    "min_score": 71.37,  # Minimum is for علمي رياضيات ابتدائي
    "interests": ["التربية والتعليم 👩‍🏫"],
    "desc": "تهدف الكلية إلى إعداد معلمين متخصصين في المراحل التعليمية المختلفة، من رياض الأطفال إلى المرحلة الثانوية، في مجالات علمية وأدبية متعددة تلبي احتياجات النظام التربوي.",
    "years": 4,
    "paths": [
    
        {"name": "برنامج متوسط/ثانوي – البيولوجيا ", "min_score": 80.23},
        {"name": "برنامج متوسط/ثانوي – الرياضيات ", "min_score": 71.37},
        {"name": "برنامج متوسط/ثانوي – الفيزياء ", "min_score": 76.15},
        {"name": "برنامج متوسط/ثانوي – الجيولوجيا ", "min_score": 79.8},
        {"name": "برنامج متوسط/ثانوي – الكيمياء ", "min_score": 76.78},
        {"name": "برنامج الابتدائي – العلوم ", "min_score": 79.3},
        {"name": "برنامج الابتدائي – الرياضيات ", "min_score": 74.78}
    ]
},


    "كلية العلوم الاجتماعية": {
      "stream": "أدبي",
      "weights": {"gpa": 90, "arabic": 10},
      "min_score": 70.2,  # أقل مسار = علم المعلومات الجغرافية
      "interests": ["القانون والقراءة 📚"],
      "desc": "توفر الكلية تخصصات متنوعة في العلوم الاجتماعية مثل علم النفس، الاجتماع، الجغرافيا، والسياسة، بهدف إعداد كوادر قادرة على فهم وتحليل السلوك البشري والمجتمعي والمساهمة في تطوير السياسات والخدمات المجتمعية.",
      "years": 4,
      "paths": [
        {"name": "علم الاجتماع", "min_score": 70.21},
        {"name": "علم النفس", "min_score": 72.24},
        {"name": "علم المعلومات الجغرافية", "min_score": 70.28},
        {"name": "العلوم السياسية", "min_score": 70.23},
        {"name": "الجغرافيا التطبيقية", "min_score": 70.2},
        {"name": "الخدمة الاجتماعية", "min_score": 70.35}
       ]
    }

})
st.subheader("اختر المسار الثانوي")
stream = st.radio("هل أنت من المسار العلمي أم الأدبي؟", ["علمي", "أدبي"])

if st.button(" اقترح التخصصات"):
    matched = []

    for name, data in colleges.items():
        # Skip colleges that don’t match the selected stream
        if "stream" in data and data["stream"] != stream:
            continue

        # Skip colleges outside the selected interest
        if interest not in data["interests"]:
            continue

        weights = data["weights"]

        # Handle colleges with multiple weight schemes (علمي / أدبي)
        if isinstance(weights, dict) and stream in weights:
            selected_weights = weights[stream]
        elif isinstance(weights, dict) and "gpa" in weights:
            selected_weights = weights
        else:
            continue

        # Calculate the weighted composite score
        score = 0
        if "gpa" in selected_weights:
            score += gpa * (selected_weights["gpa"] / 100)
        if "math" in selected_weights:
            score += math * (selected_weights["math"] / 100)
        if "english" in selected_weights:
            score += english * (selected_weights["english"] / 100)
        if "arabic" in selected_weights:
            score += arabic * (selected_weights["arabic"] / 100)
        if "french" in selected_weights:
            score += french * (selected_weights["french"] / 100)

        final_score = round(score, 2)

        if final_score >= data["min_score"]:
            matched.append((name, data, final_score))

    if matched:
        st.success(" هذه التخصصات تناسبك حسب درجاتك واهتماماتك")
        for name, data, final_score in matched:
            paths_html = ""
            if "paths" in data and data["paths"]:
                if isinstance(data["paths"][0], dict):
                    eligible_paths = [
                        f"{p['name']} (الحد الأدنى: {p['min_score']}%)"
                        for p in data["paths"] if final_score >= p["min_score"]
                    ]
                else:
                    eligible_paths = data["paths"]

                if eligible_paths:
                    paths_html = (
                        "<p><strong> المسارات:</strong></p><ul>"
                        + "".join([f"<li>{p}</li>" for p in eligible_paths])
                        + "</ul>"
                    )

            st.markdown(f"""
            <div style='border-right: 6px solid #003366; padding: 20px 25px; margin: 20px 0; background-color: #f9f9f9; border-radius: 10px;'>
                <h3 style='margin-bottom: 10px;'>{name}</h3>
                <p><strong> الوصف:</strong> {data['desc']}</p>
                <p><strong> معدلك المكافئ:</strong> {final_score}%</p>
                <p><strong> سنوات الدراسة:</strong> {data['years']} سنوات</p>
                {paths_html}
            </div>
            """, unsafe_allow_html=True)

        # 📌 Add official source note below the results
        st.markdown("""
        <div style='text-align:center; font-size:13px; color:#666; margin-top:30px;'>
            📌 <em>المعلومات مبنية على بيانات رسمية من جامعة الكويت للسنة الدراسية 2024–2025. قد تتغير المعدلات  في السنوات القادمة.</em>
        </div>
        """, unsafe_allow_html=True)

    else:
        st.warning("عذرًا، لم نجد تخصصات تتوافق مع درجاتك واهتماماتك. ننصحك بمراجعة البيانات المدخلة أو تجربة مجال آخر.")
