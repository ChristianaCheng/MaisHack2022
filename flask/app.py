from flask import Flask,redirect,url_for,render_template,request,session

app = Flask(__name__)
#--------------------------------------
def get_response(question,num_generations = 3):
    from helper import request_generation
    import pandas as pd

    column_names = ['command','email']
    df = pd.read_csv('examples.csv',names=column_names)
    preset = "This email writing program can generate full email templates from commands. Here are some examples:\n"
    counter = 0
    threshold = 15
    email = ''
    #seperator = '--SEPARATOR--\n'
    seperator = '--\n'
    for index, row in df.iterrows():
        counter += 1
        if counter > threshold:
            break
        preset +=  seperator
        preset += 'Command: '+row['command'] + '\n'
        preset += 'Email:' + row['email'].replace('\n',' ') + '\n'

    p = "Command: A letter to the government asking " + question + '\n'
    prompt = preset+'--\n'+p
    generated = request_generation(
      model='large', 
      prompt = prompt,
      #prompt='This email writing program can generate full email templates from commands. Here are some examples:\n--\nCommand: A letter to the government asking how long do I have to wait for canadian visitor visa\nEmail:Dear ______,  I am writing to inquire about the waiting period for a Canadian visitor visa. I am interested in applying for a visa to visit Canada, and would like to know how long the process typically takes. I understand that processing times may vary depending on individual circumstances, but would appreciate any general information you can provide about the timeline for this type of visa.  Thank you for your time and consideration.\n--\nCommand: A letter to the government asking why my disability benefit has been declined.\nEmail:Dear ______,   I am writing to ask why my disability benefit has been declined. I have been receiving this benefit for many years and it has been a great help to me in managing my condition. I was recently told that my benefit would be discontinued, and I would like to know why this decision was made. As you may know, I have a disability that prevents me from working full- time. This benefit has allowed me to maintain my independence and live a reasonably normal life. Without it, I would be forced to rely on others for financial support, which would be very difficult for me. I would appreciate it if you could let me know why my benefit was declined, and if there is any way that I can appeal this decision.  Thank you for your time.  Sincerely,  [Your Name]\n--\nCommand: A letter to the government asking if my wife eligible for maternity/parental benefits\nEmail:To Whom It May Concern,  I am writing to inquire about my wife\'s eligibility for maternity/parental benefits. She is currently pregnant and due to deliver our child in [insert month and year]. I would like to know if she is eligible for any benefits that could help us during this time and how we can go about applying for them. Thank you for your time and consideration.  Sincerely,  [Your Name]\n--\nCommand: A letter to the government asking the status of my PGWP application\nEmail:Dear Sir/Madam,  I would like to inquire about the status of my application for a Post-Graduation Work Permit (PGWP). I submitted my application on ____________ (date) and my student visa expires on ____________ (date). I would appreciate it if you could let me know the status of my application and how long I can expect to wait for a decision. Thank you in advance for your time and assistance.  Sincerely,  ____________ (name) \n--\nCommand: A letter to the government asking how can get a work permit in canada\nEmail:Hello,  I am writing to inquire about how I can obtain a work permit in Canada. I am a citizen of [COUNTRY NAME] and I am interested in working in Canada in order to gain experience in my field of work. I would appreciate it if you could provide me with information on the steps I need to take in order to apply for a work permit, as well as any other relevant information that I should be aware of. Thank you for your time and assistance. Sincerely,  [YOUR NAME]\n--\nCommand: A letter to the government asking how to formally dispute your notice of assessment, reassessment or determination?\nEmail:Dear Government, I am writing to dispute my notice of assessment, reassessment or determination. I believe that I have been assessed incorrectly and would like to request a review of my case. I would appreciate if you could provide me with information on how to formally dispute my assessment and what the next steps would be in the process. Thank you for your time and assistance. Sincerely, [Your Name]\n--\nCommand: A letter to the government asking why I don\'t have tax refund this year.\nEmail:Dear Government, I\'m writing to ask why I haven\'t received my tax refund this year. I was expecting to receive a refund of $XXX, but so far I haven\'t seen any money come back to me. I would appreciate if you could look into this and let me know what is happening with my refund. Thank you.\n--\nCommand: A letter to the government asking for if I still have CEEB eligibility after withdrawing from college\nEmail:Dear Government Official,  I am writing to inquire about my CEEB eligibility after withdrawing from college. I was previously enrolled in college full-time, but I withdrew from all of my classes and am no longer enrolled. I would like to know if I am still eligible to take the CEEB and if so, how I can go about doing so.  Thank you for your time and attention to this matter.  Sincerely,  [Your Name]\n--\nCommand: A letter to the government asking for if I can apply for EI 8 month later since lost my income.\nEmail:Dear Government,  I am writing to inquire about whether or not I can apply for Employment Insurance (EI) eight months after I lost my income. I understand that the usual time frame for applying for EI is within four weeks of losing one\'s job or income. However, due to extenuating circumstances, I was not able to apply for EI within that time frame. I would like to know if I am still eligible to apply for EI benefits, and if so, how I can go about doing so.  Thank you for your time and consideration.  Sincerely,  [Your Name]\n--\nCommand: A letter to the government asking how long would it take for CRA to process my tax documents\n\nEmail:Dear Government,   I am writing to inquire about how long it would take for the Canada Revenue Agency to process my tax documents. I have submitted all of the necessary paperwork and am just waiting for a response. I would appreciate if you could let me know how long I can expect to wait for a decision.   Thank you for your time.   Sincerely,   [Your Name]\n--\nCommand: A letter to the government asking when I need to extend my student visa\nEmail:Dear Government,  I am writing to ask when I need to extend my student visa. My current visa is set to expire on XX/XX/XXXX. I am currently enrolled in school and my program is set to end on XX/XX/XXXX. I would like to know if I need to extend my visa in order to continue attending school or if I can remain on my current visa until it expires. Thank you for your time and I look forward to hearing from you soon.\n--\nCommand: A letter to the government asking how to notify the government of a death\nEmail:Dear Government,  We are writing to ask how we can notify the government of a death. We are unsure what the process is or who to contact. We would appreciate any guidance you can provide.  Thank you,  [Your Name]\n--\nCommand: A letter to the government what are my benefits payment dates\nEmail:Dear Government,  I am writing to inquire about my benefits payment dates. I am currently receiving benefits from the government and would like to know when my next payment is scheduled to come through. I appreciate any information you can provide on this matter. Thank you for your time and attention.\n--\nCommand: A letter to the government asking how can I cancel my EI\nEmail:Dear Government,  I would like to cancel my Employment Insurance benefits. How can I do this?  Thank you,  [Your Name]\n--\nCommand: A letter to the government asking how to change address in my CRA account\nEmail:Dear Sir or Madam,  I would like to know how to change my address in my CRA account. I have recently moved and would like to update my information with the government. Can you please let me know the steps I need to take in order to change my address? Thank you for your time.  Sincerely,  [insert your name here]\n--\nCommand:  A letter to the government asking how can I apply for student visa\n', 
      max_tokens=256, 
      temperature=0.8, 
      k=0, 
      p=0.75, 
      frequency_penalty=0, 
      presence_penalty=0, 
      stop_sequences=["--"], 
      return_likelihoods='NONE',
      num_generations=num_generations)
    
    final = []

    for item in generated:
        final.append(item.text.replace('--','').split('Email:',1)[1])
  
    return final

#------------------------------------
question = None
@app.route("/",methods = ["POST","GET"])
def home():
    if request.method == "POST":
        if request.form['button'] == "email":
            def my_input_question(text):
                text = text.lower()
                return text
            global question 
            question = my_input_question(request.form['question'])
            print('question: ',question)
            return redirect(url_for("answer"))
        elif request.form['button']=="answer":
            pass
    else:
        return render_template("child.html")



@app.route("/response")
def answer():
    content = get_response(question,num_generations = 3)
    return render_template("response.html",content=content)


# # <name> in the route captures a value from the URL and passes it to the view function. 
# @app.route("/<question>/")
# def user(question):
#   # pass the var question to the question var in the html file
#   return render_template("base.html")

# # access page by admin or admin/
# # redirect if people want to get inside this admin page
# @app.route("/admin/")
# def admin():
#   return redirect(url_for("user",question="Admin!"))
if __name__ == "__main__":
    app.run()


# flask --app helpium run
#As a shortcut, if the file is named app.py or wsgi.py
# flask run

# If you have the debugger disabled or trust the users on your network, you can make the server publicly available simply 
# by adding --host=0.0.0.0 to the command line:
# $ flask run --host=0.0.0.0
# This tells your operating system to listen on all public IPs.