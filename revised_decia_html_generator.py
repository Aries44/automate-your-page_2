def generate_concept_HTML(concept_title, concept_description):
    html_text_1 = '''
<div class="concept">
    <div class="concept-title">
        ''' + concept_title
    html_text_2 = '''
    </div>
    <div class="concept-description">
     <p>   
        ''' + concept_description
    html_text_3 = '''
     <p>
    </div>
</div>'''
    
    full_html_text = html_text_1 + html_text_2 + html_text_3
    return full_html_text

def generate_HTML(concept):
    concept_title = concept[0]
    concept_description = concept[1]
    return generate_concept_HTML(concept_title, concept_description)

list_of_concepts = [ ['Coding in HTML', 'Coding happens when programmers write text in a language that a computer can understand. The computer can then follow the instructions the programmer wrote.'],
                     ['Avoiding Repetition', 'Programmers need to try and avoid repetition. When they do not, this may lead to copying and pasting certain style attributes into many HTML elements. Programmers need to be consistent so that every lesson will look the same.'],
                     ['Variables', 'A <b>variable</b> is a name that refers to a value. In Python, we can use any sequence of letters and numbers and underscores (_) we want to make a variable name, so long as it does not start with a number.'] ]
                     

def generate_all_html(list_of_concepts):
    HTML = ""
    for concept in list_of_concepts:
        concept_HTML = generate_HTML(concept)
        HTML = HTML + concept_HTML
    return HTML

print generate_all_html(list_of_concepts)
