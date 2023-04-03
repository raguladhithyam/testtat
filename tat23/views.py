from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from email.message import EmailMessage
import smtplib

@csrf_exempt
def send_email(request):
    print(request.method)
    if request.method=="POST":
        data=JSONParser().parse(request)
        name=data["name"]
        email=data["email"]
        tat23Id=data["tat23Id"]
        message = "<h2><b>Registration Confirmation</b></h2><h4>Hi " + name + ",</h4><p>Greetings from Tat Team,<br>Thank You for Registering for Tat 23.</p><h2><b>Important Details</b></h2><p>TAT ID: " + tat23Id + "<br><p><h4>All the BEST for your future endeavors.<br>Kindly pay the onetime registration fee. Incase if the registered event is a team event, Everyone in the team are supposed to pay individually to move further.<br><br>You can take part in 15+ events of TAT 23.</h4><p>Regards,<br>Organising Team,<br>TAT 2023.<br><br>Copyright © TAT 2023, All rights reserved.<p>"
        user='tamilmandramandnithilam@gmail.com'
        pas='wntwshevsrwnwmwu'
        msg = EmailMessage()
        msg['Subject'] = 'Tat 23 Registration Successful'
        msg['From'] = user
        msg['To'] = email
        msg.set_content(message)
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(user, pas)
            smtp.send_message(msg)
        
        return JsonResponse("Sent Successfully!!", safe=False)