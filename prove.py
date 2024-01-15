
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain.memory import ConversationBufferMemory
from langchain.memory import ChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate
import pandas as pd
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.platypus import Paragraph
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import PageBreak

from langchain.llms import OpenAI
import streamlit as st

output_parser = StrOutputParser()

st.title('🦜🔗 Quickstart App')

openai_api_key = st.sidebar.text_input('OpenAI API Key', type='password')

def generate_response(input):

    template  = """
    Settimana N: [Obiettivo]
    Giorno N [Focus]:
    1. Esercizio 1: SeriexRipetizioni - RIR: numero ripetizioni in riserva - Modalità esecuzione: (controllata/veloce) - Recupero: Tempo 
    2. Esercizio 2: SeriexRipetizioni - RIR: numero ripetizioni in riserva - Modalità esecuzione: (controllata/veloce) - Recupero: Tempo 
    3. Esercizio 3: SeriexRipetizioni - RIR: numero ripetizioni in riserva - Modalità esecuzione: (controllata/veloce) - Recupero: Tempo
    ...
    NON INSERIRE NOTE ALLA FINE DELLA SETTIMANA
    """

    chest = ["Plyo Push Ups", "Bench Press", "Dumbbell Fly", "Pec Deck Machine", "Cable Cross-over", "Chest Dip", "Incline Bench Press 45°", "Decline Bench Press", "Machine Chest Press", "Iso-Lateral Chest Press", "Dumbbell Pullover", "Incline 30° DB Bench Press", "Alternated DB Incline 30° Bench Press"]
    back = ["Single Arm MB Slam", "Lat Pulldown", "Pull-up", "Dumbbell Row", "Barbell Row", "DB Bent Over Row", "Face Pull", "Reverse Fly", "Single-Arm Dumbbell Row", "Chin-up", "Machine Row", "Seated Cable Row", "Iso-Lateral Row Machine", "Machine Shoulder Press", "Cable Face Pull with External Rotation", "Reverse Cable Crossover"]
    shoulders = ["Overhead Press", "Shoulder Shrug", "Upright Row", "Seated Dumbbell Press", "Arnold Press", "Lateral Raise", "Front Raise", "Machine Shoulder Press", "Cable Lateral Raise", "Cable Upright Row"]
    biceps = ["Bicep Curl", "Hammer Curl", "Concentration Curl", "Preacher Curl", "Cable Bicep Curl", "Seated Incline Curl", "Spider Curl", "Zottman Curl"]
    triceps = ["Tricep Extension", "Skull Crusher", "Wrist Curl", "Reverse Wrist Curl", "Cable Tricep Pushdown", "Single-Arm Cable Tricep Extension", "Dumbbell Tricep Kickback"]

    upper_body_exercises = chest + back + shoulders + biceps + triceps

    quads = ["Box Jump", "Squat", "Leg Press", "Front Squat", "Hack Squat", "Goblet Squat", "Smith Machine Squat", "Machine Squat", "V-Squat Machine", "Inverted Leg Press Machine", "Horizontal Leg Press", "Jump Squat", "Sissy Squat", "Leg Extension"]
    hamstrings = ["Deadlift", "Romanian Deadlift", "Leg Curl", "Sumo Deadlift", "Single-Leg Deadlift", "Nordic Hamstring Curl", "Seated Leg Curl", "Prone Leg Curl"]
    glutes = ["Broad Jumps", "Lunges", "Bulgarian Split Squat", "Hip Thrust", "Step-up", "Glute Bridge", "Barbell Hip Thrust", "Cable Kickback", "Single-Leg Squat", "Pistol Squat", "Reverse Lunges", "Curtsy Lunges", "Single-Leg Hip Thrust", "Glute Kickback Machine", "Kettlebell Swing", "Weighted Step-up", "Sled Push"]
    calves = ["Calf Raise", "Seated Calf Raise", "Standing Calf Raise Machine", "Donkey Calf Raise", "Leg Press Calf Raise"]
    others = ["Depth Jump", "Lateral Lunges", "Dumbbell Lunges", "Leg Abduction", "Leg Adduction", "Walking Lunges", "Wall Sit"]

    lower_body_exercises = quads + hamstrings + glutes + calves + others

    power_exercises = ["Box Jump", "Depth Jump", "CMJ", "Squat Jump", "Plyo Push Ups", "Chest MB Throw", "Side MB Throw"]

    # Unione delle due liste in una stringa
    exercise_list_str = "Upper Body Exercises:\n" + "\n".join(upper_body_exercises) + "\n\nLower Body Exercises:\n" + "\n".join(lower_body_exercises) +  "\n\nPower Exercises:\n" + "\n".join(power_exercises)

    prompt = ChatPromptTemplate.from_messages([
        ("system", f" Sei un preparatore atletico con esperienza nell'allenamento in palestra, specializzato in incremento della massa muscolare e della forza attraverso esercizi fondamentali come squat, stacco e panca, e esercizi complementari. Utilizzi metodologie di allenamento in multifrequenza e adotti la daily ondulated periodization. Quando crei programmi di allenamento, segui le linee guida specificate in {guidelines}, utilizza lo schema {template} e seleziona esercizi da {exercise_list_str}. È essenziale che tu consideri attentamente le esigenze, il livello e gli obiettivi dell'atleta per sviluppare progressioni settimanali. Il programma deve essere dettagliato per tutte le settimane, includendo esercizi specifici, serie, ripetizioni, RIR, modalità e tempi di recupero, per fornire un piano chiaro e strutturato per l'intero periodo richiesto."),
        ("user", "{input}") 
    ])
    chain = prompt | llm  | output_parser 
    programma = []
    programma.append(chain.invoke({"input": f"{input}"}))
    llm = ChatOpenAI(api_key = openai_api_key, temperature= 0.5, model="gpt-3.5-turbo")
    st.info(programma[0])

sesso = "uomo"
eta = "20"
esperienza = "avanzato"
problematiche = "nessuna"
durata = "4"
allenamenti = "3"
durata_allenamenti = "1"
obiettivo_primario = "performance rugby"
obiettivo_secondario = "forza"
preferenze = "Allenamenti full body"

with st.form('my_form'):
    sesso = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
    eta =st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
    esperienza = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
    problematiche = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
    durata = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
    allenamenti = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
    durata_allenamenti = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
    obiettivo_primario = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
    obiettivo_secondario = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
    preferenze = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')

    input = "Sono un individuo di sesso {sesso} e ho {eta} anni. Ho {esperienza} esperienza in palestra. Considerando che ho {problematica} fastidi articolari, vorrei un programma di allenamento di {durata} settimane. Ogni settimana dovrà includere {allenamenti} sessioni di allenamento, ciascuna della durata di {durata_allenamenti} ore. Il mio obiettivo principale è {obiettivo_primario} e il mio obiettivo secondario è {obiettivo_secondario}. Si prega di fornire la prima settimana di un programma che tenga conto della mia situazione fisica e degli obiettivi. Non inserire note"

    submitted = st.form_submit_button('Submit')
    if not openai_api_key.startswith('sk-'):
        st.warning('Please enter your OpenAI API key!', icon='⚠')
    if submitted and openai_api_key.startswith('sk-'):
        generate_response(input)
