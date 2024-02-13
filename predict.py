import vertexai
from vertexai.language_models import TextGenerationModel


vertexai.init(project="xcigence", location="us-central1")
parameters = {
        "candidate_count": 1,
        "max_output_tokens": 1024,
        "temperature": 0.9,
        "top_p": 1
    }

model = TextGenerationModel.from_pretrained("text-bison")
def generate_question_answer(text, num_question, domain, requirement):

    prompt = f"""You are an internal information auditor. please create {num_question}  Questionnaire format of {text} for {domain} given by {requirement}."""


    response = model.predict(prompt, **parameters)
    return response.text





# generate_question_answer("Subject matter & Objectives policy ", 10, "supplier relationship", "ISO-27001")