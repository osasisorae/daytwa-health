helper_mgs = "You can ask me for personalized health information or advice, and I'll provide you with relevant resources to help you maintain a healthy lifestyle."
start_msg = "Hi! I'm Daytwa Health, your personal preventive health assistant. How can I help you today?"
myprofile_msg = "Creating your health profile is a great way to track and improve your well-being. You can format your profile by asking questions about your health and providing detailed answers. This information will help me provide you with personalized health advice. Please start by sharing your first question and answer, and I'll assist you from there!\n For example:\n\n"

questions_and_answers = [
    "Am I up to date on my vaccinations? - Yes, I received my flu shot last month, and I'm on schedule for all recommended vaccines.",
    "Do I engage in regular physical activity? - I exercise for 30 minutes every day, including a mix of cardio and strength training.",
    "What is my current body mass index (BMI), and is it within a healthy range? - My BMI is 23, which falls within the healthy weight range for my height.",
    "Do I follow a balanced and nutritious diet? - I maintain a diet rich in fruits, vegetables, lean proteins, and whole grains. I avoid processed foods.",
    "Am I getting enough sleep on a regular basis? - I aim for 7-8 hours of sleep each night and have established a consistent sleep schedule.",
    "Do I engage in risky behaviors, such as smoking or excessive alcohol consumption? - I do not smoke, and I limit my alcohol intake to one glass of wine per week.",
    "Do I have a family history of chronic diseases (e.g., heart disease, diabetes, cancer) that I should be concerned about? - My family has a history of heart disease, so I'm cautious about my heart health.",
    "Have I had any recent screenings or check-ups for common health issues? - I had a comprehensive health check-up last month, which included blood tests and various screenings.",
    "Am I practicing safe sexual behaviors, including the use of protection and regular STI screenings if sexually active? - I always use protection during sexual activity, and I get tested for STIs annually.",
    "Are there any environmental factors at home or work that may impact my health (e.g., exposure to toxins, allergens)? - I work in a well-ventilated environment and have taken steps to minimize allergens at home.",
    "Am I managing my stress effectively? - I practice daily meditation, yoga, and deep breathing exercises to manage stress.",
    "Do I perform self-exams for conditions like breast or testicular cancer? - Yes, I perform regular self-exams and have identified no abnormalities.",
    "Have I been screened for vision and hearing problems recently? - I had my last eye exam six months ago, and I received a hearing test within the past year.",
    "Do I practice good oral hygiene, including regular dental check-ups? - I brush and floss twice a day, and I visit my dentist for check-ups every six months.",
    "Am I taking any medications, and am I adhering to my prescribed treatment plans? - I take medication for high blood pressure as prescribed, and I follow my doctor's recommendations.",
    "Have I received counseling or therapy for mental health concerns if needed? - Yes, I attend regular counseling sessions to manage my anxiety and depression.",
    "Am I using sunscreen and protecting my skin from excessive sun exposure? - I use SPF 30 sunscreen daily and wear protective clothing when outdoors for extended periods.",
    "Have I checked my blood pressure and cholesterol levels recently? - I monitor my blood pressure at home regularly, and I had my cholesterol levels checked last month.",
    "Am I following recommended guidelines for regular health check-ups based on my age and gender? - I follow my healthcare provider's recommendations for annual check-ups and screenings.",
    "Are there any specific preventive measures or screenings recommended based on my personal and family medical history? - My family medical history suggests a higher risk of heart disease, so I undergo heart-related screenings as advised by my doctor."
]

preventive_health_urls = [
    {'url': 'https://www.webmd.com/search?query=preventive%2Bhealth'},
    {'url': 'https://www.mayoclinic.org/search/search-results?q=preventive%20health'},
    {'url': 'https://vsearch.nlm.nih.gov/vivisimo/cgi-bin/query-meta?v%3Aproject=medlineplus&v%3Asources=medlineplus-bundle&query=preventive+health'},
    {'url': 'https://search.cdc.gov/search/?query=preventive%20health&dpage=1'},
    {'url': 'https://www.nhs.uk/search/results?q=preventive%20health&page=0'},
    {'url': 'https://pubmed.ncbi.nlm.nih.gov/?term=preventive+health'},
    {'url': 'https://www.hopkinsmedicine.org/search?form_instance=enterprise&q=preventive+health'},
    {'url': 'https://my.clevelandclinic.org/search?q=preventive%20health'},
    {'url': 'https://www.health.com/search?q=preventive+health'},
    {'url': 'https://www.who.int/home/search?indexCatalogue=genericsearchindex1&searchQuery=preventive%20health&wordsMode=AnyWord'},
    {'url': 'https://www.everydayhealth.com/search/?q=preventive%20health'},
    {'url': 'https://patient.info/search.asp?searchterm=preventive+health&searchcoll=All'},
    {'url': 'https://www.healthday.com/search?q=preventive%20health'},
    {'url': 'https://www.medicalnewstoday.com/search?q=preventive%20health'},
    {'url': 'https://familydoctor.org/?s=preventive+health'},
    {'url': 'https://www.nutrition.gov/'},
    {'url': 'https://kidshealth.org/content/kidshealth/us/en/searchresults.html?q=preventive%20health&start=0'},
    {'url': 'https://www.healthline.com/search?q1=Preventive%20Health'}, {'url': 'https://www.healthline.com/search?q1=Wellness'}, 
    {'url': 'https://www.healthline.com/search?q1=Preventive%20Medicine'}, {'url': 'https://www.healthline.com/search?q1=Health%20Tips'}, 
    {'url': 'https://www.healthline.com/search?q1=Disease%20Prevention'}, {'url': 'https://www.healthline.com/search?q1=Healthy%20Lifestyle'}, 
    {'url': 'https://www.healthline.com/search?q1=Immunizations'}, {'url': 'https://www.healthline.com/search?q1=Nutrition'}, 
    {'url': 'https://www.healthline.com/search?q1=Physical%20Activity'}, {'url': 'https://www.healthline.com/search?q1=Stress%20Reduction'}, 
    {'url': 'https://www.healthline.com/search?q1=Mental%20Health'}, {'url': 'https://www.healthline.com/search?q1=Preventive%20Screenings'}, 
    {'url': 'https://www.healthline.com/search?q1=Healthy%20Aging'}, {'url': 'https://www.healthline.com/search?q1=Family%20Health'}, 
    {'url': 'https://www.healthline.com/search?q1=Community%20Health'}
]

healt_equity_intro = """
Welcome to Daytwa Health - Empowering Healthcare Equity

We appreciate your interest in joining our distinguished team of Health Equity Navigators. At Daytwa Health, we are steadfast in our commitment to advancing healthcare equity and addressing social justice within our healthcare system. Our Health Equity Navigators play a pivotal role in facilitating this mission by connecting underserved communities with the support and guidance they deserve.


Roles and Responsibilities of Health Equity Navigators:

In the capacity of a Health Equity Navigator, you will be entrusted with the following responsibilities:

- Act as a vital liaison, bridging the gap between our innovative chatbot and the communities that are underserved.

- Provide highly personalized and culturally sensitive healthcare guidance to community members, ensuring that their unique needs are comprehensively addressed.

- Contribute to the collection of invaluable data, which is essential for an in-depth understanding of the specific healthcare requirements of these communities.

- Actively engage in advocacy efforts that seek to rectify systemic healthcare disparities and injustices.


Application Procedure:

To apply for enrollment in our prestigious Health Equity Navigator training program, we kindly request that you submit your Curriculum Vitae (CV). Your CV serves as an essential tool for us to gain insight into your background, qualifications, and your dedication to the significance of this role.

Submission of Your CV:

You may submit your CV by sending it right here on this chat.
"""

healt_equity_applied = """
Next Steps:

Upon submission of your CV, our adept team will meticulously review your application within the next two weeks. Those who are selected for our training program will be contacted with precise instructions for the next phase of the application process.

We express our sincere gratitude for considering Daytwa Health as a platform for contributing to healthcare equity and social justice. Your dedication is highly regarded, and we eagerly anticipate the significant impact you can make within underserved communities.
"""

prompt_template_cv = """
   The goal is to summarize this CV {text}. If the CV aligns with the cultural competencies in the communities, I will suggest that [name] moves to the next section and start the training program here on Telegram with the command /train. 
   If it doesn't align with the cultural competencies, Just inform [name] about the experience they should gain and recommend trying again in 3 months.

Looking at the CV and assess whether their competencies align with the following cultural competencies:

1. Immigrant and Refugee Communities:
   - Sensitivity to the challenges of adjusting to a new culture
   - Understanding language barriers
   - Knowledge of culturally specific health practices and beliefs

2. Indigenous Communities:
   - Knowledge of traditional healing practices
   - Respect for indigenous cultural beliefs
   - Understanding the historical trauma and health disparities faced by these communities

3. Racial and Ethnic Minority Communities:
   - Awareness of culturally specific healthcare practices
   - Addressing health disparities experienced by these groups
   - Respecting cultural diversity within these communities

4. LGBTQ+ Communities:
   - Understanding the unique health needs and disparities faced by LGBTQ+ individuals
   - Using inclusive language
   - Addressing discrimination and stigma

5. Low-Income and Underserved Communities:
   - Sensitivity to socioeconomic disparities
   - Knowledge of available community resources
   - Addressing barriers to access, such as transportation and affordability

Based on the CV, please assess whether [name] competencies align with these cultural competencies. If they align, suggest that they move to the next section and start the training program here on Telegram /train. If they don't align, provide recommendations for gaining the necessary experience and encourage them to try again in 3 months.
You can get the [name] from the CV document passed.

Remember just to tell the user what you know about him/her and let them know if the pass. Respond with one of the following outputs.
1. There is no mention of direct experience or involvement in working with immigrant and refugee communities, indigenous communities, racial and ethnic minority communities, LGBTQ+ communities, or low-income and underserved communities.
Therefore, I would suggest gaining more experience related to these communities to assess your cultural competencies. You may consider actively participating in related community projects, volunteering, or seeking opportunities to broaden your cultural awareness in these areas.
If you are interested in improving your cultural competencies and would like to learn more about the training program, use /train.
2. Based on your experience you seem like a good fit, someone from the team will contact you soon.
"""