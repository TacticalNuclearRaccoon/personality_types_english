#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 10:08:57 2024

@author: deni-kun
"""

import streamlit as st
import os

st.set_page_config(layout='wide', page_icon=':unicorn_face:')

def create_result_text_file(filename, personality_scores, coef):
    with open(filename, 'w') as file:
        file.write("Your results are :\n")
        file.write(f"A_score = {coef * personality_scores.get('A')}\n")
        file.write(f"B_score = {coef * personality_scores.get('B')}\n")
        file.write(f"C_score = {coef * personality_scores.get('C')}\n")
        file.write(f"D_score = {coef * personality_scores.get('D')}\n")


A_text = """The engineer enjoys solving problems using the scientific method and logical reasoning.
They are analytical and capable of conceptualizing abstract concepts. This personality tends to be introverted and values analysis and knowledge.\n
***Strengths***: compile facts, analyze, argue rationally, formulate theories, measure precisely, solve problems logically, reason, understand technical elements, analyze critically, work with numbers, statistics, and precision."""

B_text = """The cartographer is cautious and organized. They have specific habits and meticulously follow rules.
They plan meticulously and excel in administrative tasks where attention to detail is valued.\n
***Strengths***: notice flaws, approach problems practically, follow through, develop detailed plans and procedures, and consider problems from a planning perspective."""

C_text = """The bard enjoys human interaction. They are empathetic, relational, and friendly. They are expressive and communicate well with others.\n
***Strengths***: understand interpersonal difficulties, anticipate others' feelings, intuitively grasp others' emotions, perceive non-verbal cues from stress, generate enthusiasm, persuade, reconcile, teach, share, understand emotional elements, and consider values."""

D_text = """The inventor is an adventurer with a vivid imagination who daydreams. They are visionaries with highly original ideas.
They are risk-takers who like to project themselves into new possibilities.\n
***Strengths***: read signs of change, see the big picture, recognize new possibilities, tolerate ambiguity, integrate ideas and concepts, challenge established rules, synthesize diverse elements into something new, invent new solutions, intuitively solve problems, integrate multiple inputs simultaneously."""

st.title('Personality Test (Demo)')

personality_scores = {
    'A': 0,
    'B': 0,
    'C': 0,
    'D': 0
}

st.header('Hobbies')

st.write('Select the hobbies you practice or would like to practice.')

col1, col2 = st.columns(2)

with col1:
    hobbies = {
        'photography': st.checkbox('Photography'),
        'relaxing': st.checkbox('Relaxing'),
        'ham_radio': st.checkbox('Ham Radio'),
        'hunting': st.checkbox('Hunting'),
        'fishing': st.checkbox('Fishing'),
        'gardening': st.checkbox('Gardening'),
        'woodworking': st.checkbox('Woodworking'),
        'music': st.checkbox('Music'),
        'jogging': st.checkbox('Jogging'),
        'car_repair': st.checkbox('Car Repair'),
        'singing': st.checkbox('Singing'),
        'volunteering': st.checkbox('Volunteering'),
        'reading': st.checkbox('Reading'),
        'DIY': st.checkbox('DIY'),
        'sports_spectator': st.checkbox('Sports Spectator'),
        'collecting': st.checkbox('Collecting')
    }

with col2:
    hobbies2 = {
        'games_of_chance': st.checkbox('Games of Chance'),
        'crafts': st.checkbox('Crafts'),
        'cooking': st.checkbox('Cooking'),
        'conversations': st.checkbox('Conversations'),
        'theater': st.checkbox('Theater'),
        'card_games': st.checkbox('Card Games'),
        'deep_sea_fishing': st.checkbox('Deep Sea Fishing'),
        'traveling': st.checkbox('Traveling'),
        'botany': st.checkbox('Botany'),
        'golf': st.checkbox('Golf'),
        'computers': st.checkbox('Computers'),
        'dance': st.checkbox('Dance'),
        'strategy_games': st.checkbox('Strategy Games'),
        'logic_puzzles': st.checkbox('Logic Puzzles'),
        'board_games': st.checkbox('Board Games'),
        'bowling': st.checkbox('Bowling')
    }

if hobbies["photography"]:
    personality_scores["D"] += 1

if hobbies['relaxing']:
    personality_scores["D"] += 1

if hobbies['ham_radio']:
    personality_scores["A"] += 1

if hobbies['hunting']:
    personality_scores["A"] += 1

if hobbies['fishing']:
    personality_scores["B"] += 1

if hobbies['gardening']:
    personality_scores['C'] += 1

if hobbies['woodworking']:
    personality_scores['A'] += 1

if hobbies['music']:
    personality_scores['C'] += 1

if hobbies['jogging']:
    personality_scores['B'] += 1

if hobbies['car_repair']:
    personality_scores['A'] += 1

if hobbies['singing']:
    personality_scores['C'] += 1

if hobbies['volunteering']:
    personality_scores['C'] += 1

if hobbies['reading']:
    personality_scores['C'] += 1

if hobbies['DIY']:
    personality_scores['A'] += 1

if hobbies['sports_spectator']:
    personality_scores['B'] += 1

if hobbies['collecting']:
    personality_scores['B'] += 1

if hobbies2['games_of_chance']:
    personality_scores['D'] += 1

if hobbies2['crafts']:
    personality_scores['D'] += 1

if hobbies2['cooking']:
    personality_scores['B'] += 1

if hobbies2['conversations']:
    personality_scores['C'] += 1

if hobbies2['theater']:
    personality_scores['D'] += 1

if hobbies2['card_games']:
    personality_scores['B'] += 1

if hobbies2['deep_sea_fishing']:
    personality_scores['D'] += 1

if hobbies2['traveling']:
    personality_scores['C'] += 1

if hobbies2['botany']:
    personality_scores['B'] += 1

if hobbies2['golf']:
    personality_scores['A'] += 1

if hobbies2['computers']:
    personality_scores['A'] += 1

if hobbies2['dance']:
    personality_scores['D'] += 1

if hobbies2['strategy_games']:
    personality_scores['D'] += 1

if hobbies2['logic_puzzles']:
    personality_scores['A'] += 1

if hobbies2['board_games']:
    personality_scores['C'] += 1

if hobbies2['bowling']:
    personality_scores['B'] += 1

st.header('Work Activities')

st.write("Check the activities below that you do well or very well.")

col1, col2 = st.columns(2)

with col1:
    activites = {
        'analyser': st.checkbox('Analyze'),
        'administrer': st.checkbox('Administer'),
        'conceptualiser': st.checkbox('Conceptualize'),
        'exprimer': st.checkbox('Express Ideas'),
        'synth': st.checkbox('Synthesize'),
        'orga': st.checkbox('Organize'),
        'Rationalize': st.checkbox('Rationalize'),
        'concretiser': st.checkbox('Concretize')
    }

with col2:
    activites2 = {
        'echanger': st.checkbox('Exchange (contact)'),
        'problem_solve': st.checkbox('Problem-Solve'),
        'innov': st.checkbox('Innovate'),
        'former': st.checkbox('Teach'),
        'create':st.checkbox('Create'),
        'calculate':st.checkbox('Calculate'),
        'planifie':st.checkbox('Planifier'),
        'animer':st.checkbox('Animate (meetings)')        
        }

if activites['analyser']:
    personality_scores['A'] +=1
if activites['administrer']:
    personality_scores['B'] +=1
if activites['conceptualiser']:
    personality_scores['D']+=1
if activites['exprimer']:
    personality_scores['C'] +=1
if activites['synth']:
    personality_scores['D'] +=1
if activites['orga']:
    personality_scores['B'] +=1
if activites['Rationalize']:
    personality_scores['A'] +=1
if activites['concretiser']:
    personality_scores['B'] +=1
if activites2['echanger']:
    personality_scores['C'] +=1
if activites2['problem_solve']:
    personality_scores['A'] +=1
if activites2['innov']:
    personality_scores['D'] +=1
if activites2['former']:
    personality_scores['C'] +=1
if activites2['create']:
    personality_scores['D'] +=1
if activites2['calculate']:
    personality_scores['A'] +=1
if activites2['planifie']:
    personality_scores['B'] +=1
if activites2['animer']:
    personality_scores['C'] +=1
    
st.header('Keywords')

st.write("In the list below, select 10 adjectives that best describe you")

col1, col2 = st.columns(2)
with col1:
    mots_cles = {
        'Logique': st.checkbox('Logical'),
        'Seviable': st.checkbox('Helpful'),
        'Organisé': st.checkbox('Organized'),
        'Confiant': st.checkbox('Confident'),
        'Rationnel': st.checkbox('Rational'),
        'Conservateur': st.checkbox('Conservative'),
        'Expressif': st.checkbox('Expressive'),
        'Analytique': st.checkbox('Analytical'),
        'Émotif': st.checkbox('Emotional'),
        'Lecteur technique': st.checkbox('Technical Reader'),
        'Réaliste': st.checkbox('Realistic'),
        'Créatif': st.checkbox('Creative'),
        'Intuitif : sentiments': st.checkbox('Intuitive: Feelings'),
        'Passionné': st.checkbox('Passionate'),
        'Critique': st.checkbox('Critical'),
        'Amical': st.checkbox('Friendly'),
        'Objectif': st.checkbox('Objective'),
        'Imaginatif': st.checkbox('Imaginative'),
        'Cooperatif': st.checkbox('Cooperative'),
        'Enthousiaste': st.checkbox('Enthusiastic'),
        'Pondéré': st.checkbox('Balanced')
        }
with col2:
    mots_cles2 = {
        'Artistique': st.checkbox('Artistic'),
        'Souple': st.checkbox('Flexible'),
        'Discret': st.checkbox('Discreet'),
        'Précis': st.checkbox('Precise'),
        'Controlled': st.checkbox('Controlled'),
        'Sérieux': st.checkbox('Serious'),
        'Tenacious': st.checkbox('Tenacious'),
        'Minutieux': st.checkbox('Meticulous'),
        'Intuitive: Solutions': st.checkbox('Intuitive: Solutions'),
        'Simultané': st.checkbox('Simultaneous'),
        'Competitive': st.checkbox('Competitive'),
        'Aventurier': st.checkbox('Adventurous'),
        'Ordinné': st.checkbox('Orderly'),
        'Liberal': st.checkbox('Liberal'),
        'Discipliné': st.checkbox('Disciplined'),
        'Curious': st.checkbox('Curious'),
        'Conventionnel': st.checkbox('Conventional'),
        'Original': st.checkbox('Original'),
        'Indépendant': st.checkbox('Independent')
        }

selected_mots = sum(mots_cles.values())+sum(mots_cles2.values())

if selected_mots > 10:
    st.error('You can only select 10 keywords', icon='😢')

if mots_cles['Logique']:
    personality_scores['A'] +=1
    
if mots_cles['Seviable']:
    personality_scores['C'] +=1

if mots_cles['Organisé']:
    personality_scores['B'] +=1

if mots_cles['Confiant']:
    personality_scores['C'] +=1

if mots_cles['Rationnel']:
    personality_scores['A'] +=1

if mots_cles['Conservateur']:
    personality_scores['B'] +=1

if mots_cles['Expressif']:
    personality_scores['C'] +=1

if mots_cles['Analytique']:
    personality_scores['A'] +=1

if mots_cles['Émotif']:
    personality_scores['C'] +=1

if mots_cles['Lecteur technique']:
    personality_scores['B'] +=1

if mots_cles['Réaliste']:
    personality_scores['A'] +=1

if mots_cles['Créatif']:
    personality_scores['D'] +=1

if mots_cles['Intuitif : sentiments']:
    personality_scores['C'] +=1

if mots_cles['Passionné']:
    personality_scores['C'] +=1

if mots_cles['Critique']:
    personality_scores['A'] +=1

if mots_cles['Amical']:
    personality_scores['C'] +=1

if mots_cles['Objectif']:
    personality_scores['A'] +=1

if mots_cles['Imaginatif']:
    personality_scores['D'] +=1

if mots_cles['Cooperatif']:
    personality_scores['C'] +=1

if mots_cles['Enthousiaste']:
    personality_scores['C'] +=1

if mots_cles['Pondéré']:
    personality_scores['A'] +=1

if mots_cles2['Artistique']:
    personality_scores['D'] +=1

if mots_cles2['Souple']:
    personality_scores['C'] +=1

if mots_cles2['Discret']:
    personality_scores['A'] +=1

if mots_cles2['Précis']:
    personality_scores['A'] +=1

if mots_cles2['Controlled']:
    personality_scores['B'] +=1

if mots_cles2['Sérieux']:
    personality_scores['A'] +=1

if mots_cles2['Tenacious']:
    personality_scores['B'] +=1

if mots_cles2['Minutieux']:
    personality_scores['B'] +=1

if mots_cles2['Intuitive: Solutions']:
    personality_scores['D'] +=1

if mots_cles2['Simultané']:
    personality_scores['D'] +=1

if mots_cles2['Competitive']:
    personality_scores['B'] +=1

if mots_cles2['Aventurier']:
    personality_scores['D'] +=1

if mots_cles2['Ordinné']:
    personality_scores['B'] +=1

if mots_cles2['Liberal']:
    personality_scores['D'] +=1

if mots_cles2['Discipliné']:
    personality_scores['B'] +=1

if mots_cles2['Curious']:
    personality_scores['D'] +=1

if mots_cles2['Conventionnel']:
    personality_scores['B'] +=1

if mots_cles2['Original']:
    personality_scores['D'] +=1

if mots_cles2['Indépendant']:
    personality_scores['D'] +=1


st.header('20 Questions')
st.write('Select the activities you like or would like to practice.')

col1, col2 = st.columns(2)
with col1:
    questions = {
        'Practice logic games': st.checkbox('Practice logic games'),
        'Create a family tree': st.checkbox('Create a family tree'),
        'Take the car and drive without a destination': st.checkbox('Take the car and drive without a destination'),
        'Build': st.checkbox('Build an item from a kit following the assembly instructions'),
        'Play with children': st.checkbox('Play with children'),
        'Daydream': st.checkbox('Daydream'),
        'Design logos': st.checkbox('Design logos'),
        'Order': st.checkbox('Organize photographs'),
        'Go out': st.checkbox('Go out with friends and party'),
        'Fly a kite': st.checkbox('Fly a kite')
    }
with col2:
    questions2 = {
        'Cook': st.checkbox('Prepare a dish of your own invention'),
        'Computer': st.checkbox('Operate (or learn to operate) a computer'),
        'Repair': st.checkbox('Repair machine or appliance malfunctions'),
        'Listen to music': st.checkbox('Listen to music'),
        'Spot errors in a book or on a bank statement': st.checkbox('Spot errors in a book or on a bank statement'),
        'Feel emotions when looking at a landscape, painting, or scene': st.checkbox('Feel emotions when looking at a landscape, painting, or scene'),
        'Join a stock investment club': st.checkbox('Join a stock investment club'),
        'Play devil\'s advocate in a discussion': st.checkbox("Play devil's advocate in a discussion"),
        'Lead a group or club': st.checkbox('Lead a group or club'),
        'Practice modeling': st.checkbox('Practice modeling')
    }

if questions['Practice logic games']:
    personality_scores['A'] += 1
if questions['Create a family tree']:
    personality_scores['B'] += 1
if questions['Take the car and drive without a destination']:
    personality_scores['D'] += 1
if questions['Build']:
    personality_scores['B'] += 1
if questions['Play with children']:
    personality_scores['C'] += 1
if questions['Daydream']:
    personality_scores['D'] += 1
if questions['Design logos']:
    personality_scores['D'] += 1
if questions['Order']:
    personality_scores['B'] += 1
if questions['Go out']:
    personality_scores['C'] += 1
if questions['Fly a kite']:
    personality_scores['D'] += 1
if questions2['Cook']:
    personality_scores['D'] += 1
if questions2['Computer']:
    personality_scores['A'] += 1
if questions2['Repair']:
    personality_scores['A'] += 1
if questions2['Listen to music']:
    personality_scores['C'] += 1
if questions2['Spot errors in a book or on a bank statement']:
    personality_scores['B'] += 1
if questions2['Feel emotions when looking at a landscape, painting, or scene']:
    personality_scores['C'] += 1
if questions2['Join a stock investment club']:
    personality_scores['A'] += 1
if questions2['Play devil\'s advocate in a discussion']:
    personality_scores['A'] += 1
if questions2['Lead a group or club']:
    personality_scores['C'] += 1
if questions2['Practice modeling']:
    personality_scores['B'] += 1


submit = st.button('Calculate the results')
if submit:
    if max(personality_scores.values()) == 0:
        st.error('You need to fill at least one category in order to have some results', icon='🥺')
    coef = 100/max(personality_scores.values())
    A_score = coef*personality_scores.get('A')
    B_score = coef*personality_scores.get('B')
    C_score = coef*personality_scores.get('C')
    D_score = coef*personality_scores.get('D')
    st.write(f'Engineer: {A_score}')
    st.write(f'Cartographer: {B_score}')
    st.write(f'Bard: {C_score}')
    st.write(f'Inventor: {D_score}')
    
    scores = {'Engineer':A_score, 'Cartographer':B_score, 'Bard': C_score, 'Inventor':D_score}
    
    pilots = [k for k, v in scores.items() if v>99]
    
    
    # Create a temporary text file with the results
    result_filename = 'results.txt'
    create_result_text_file(result_filename, personality_scores, coef)

    # Send the email
    #result = send_email(subject, body, to_email, smtp_server, smtp_port, smtp_user, smtp_pass)

    #if result:
    #    st.success('Results sent successfully!')
    #else:
    #    st.error('Error sending the results. Please check your email configuration.')

    # Display the download button
    if os.path.exists(result_filename):
        st.download_button(
            label="Download results",
            data=open(result_filename, 'rb'),
            key="download_results",
            file_name="results.txt",
            help="Click to download the results as a text file.",
        )
    
    #st.write(f'votre type de personnalité est / vos types de personnalités sont: {pilots}')  
    
    st.header('Your pilots')
    st.write('A pilot is your driving/dominant personality type.')
    
    if 'Engineer' in pilots:
        st.image('Inge.png', width=400)
        st.write(A_text)
    if 'Cartographer' in pilots:
        st.image('carto.png', width=400)
        st.write(B_text)
    if 'Bard' in pilots:
        st.image('bard.png', width=400)
        st.write(C_text)
    if 'Inventor' in pilots:
        st.image('artistii.png', width=400)
        st.write(D_text)
        
    st.header('Vos co-pilotes')
    st.write('A co-pilot is the second most dominant personality type.')
    
    copilots = [k for k, v in scores.items() if v<100 and v>=75]
    
    if len(copilots) == 0:
        st.write("We did not detect a co-pilot.")
    
    if 'Engineer' in copilots:
        st.image('Inge.png', width=400)
        st.write(A_text)
    if 'Cartographer' in copilots:
        st.image('carto.png', width=400)
        st.write(B_text)
    if 'Bard' in copilots:
        st.image('bard.png', width=400)
        st.write(C_text)
    if 'Inventor' in copilots:
        st.image('artistii.png', width=400)
        st.write(D_text)
        
    st.header('Rifts')
    st.write('A rift is a personality type that you might have hard time aligning with. It might not be intuitive for you to understand people for whom this personality type is the pilot.')
    
    failles = [k for k, v in scores.items() if v<40 and v>15]
    
    if len(failles) == 0:
        st.write("We did not detect any rifts")
    
    if 'Engineer' in failles:
        st.image('Inge.png', width=400)
        st.write(A_text)
    if 'Cartographer' in failles:
        st.image('carto.png', width=400)
        st.write(B_text)
    if 'Bard' in failles:
        st.image('bard.png', width=400)
        st.write(C_text)
    if 'Inventor' in failles:
        st.image('artistii.png', width=400)
        st.write(D_text)
        
    st.header('Limits')
    st.write('Limits are the personality types that you are the furthest away from. It might be dificult for you to understand and work together with people for whom this personality type is the pilot.')
    limites = [k for k, v in scores.items() if v<15]
    
    if len(limites) == 0:
        st.write("We did not detect any limits")
    
    if 'Engineer' in limites:
        st.image('Inge.png', width=400)
        st.write(A_text)
    if 'Cartographer' in limites:
        st.image('carto.png', width=400)
        st.write(B_text)
    if 'Bard' in limites:
        st.image('bard.png', width=400)
        st.write(C_text)
    if 'Inventor' in limites:
        st.image('artistii.png', width=400)
        st.write(D_text)