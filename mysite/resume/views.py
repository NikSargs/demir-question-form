import tempfile

import weasyprint
from django.shortcuts import render
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from weasyprint import HTML, CSS, html
from django.template.loader import render_to_string
from django.shortcuts import HttpResponse
from PIL import Image
from django.core.mail import EmailMultiAlternatives

from django.template.loader import render_to_string
from django.utils.html import strip_tags


def sendmail(request, template="email_template.html"):
    if request.method == "POST":
        filling_date = request.POST.get('filling_date')
        last_name = request.POST.get('last_name')
        name = request.POST.get('name')
        second_name = request.POST.get('second_name')
        birthdate = request.POST.get('birthdate')
        birthplace = request.POST.get('birthplace')
        nationality = request.POST.get('nationality')
        sex_resume = request.POST.get('sex_resume')
        address_resume = request.POST.get('address_resume')
        phone_resume = request.POST.get('phone_resume')
        army_resume = request.POST.get('army_resume')
        licence = request.POST.get('licence')
        spouce_info = request.POST.get('spouce_info')
        children_info = request.POST.get('children_info')
        father_info = request.POST.get('father_info')
        mother_info = request.POST.get('mother_info')
        sisters_info = request.POST.get('sisters_info')
        brothers_info = request.POST.get('brothers_info')
        incomplete_secondary_education = request.POST.get('incomplete_secondary_education')
        secondary_education = request.POST.get('secondary_education')
        vocational_education = request.POST.get('vocational_education')
        high_education = request.POST.get('high_education')
        master_degree = request.POST.get('master_degree')
        doctor_degree = request.POST.get('doctor_degree')
        en_lang = request.POST.get('en_lang')
        ru_lang = request.POST.get('ru_lang')
        kg_lang = request.POST.get('kg_lang')
        different_lang = request.POST.get('different_lang')
        orgname = request.POST.get('orgname')
        post = request.POST.get('post')
        work_period = request.POST.get('work_period')
        left_cause = request.POST.get('left_cause')
        recommendation = request.POST.get('recommendation')
        relatives_in_db = request.POST.get('relatives_in_db')
        relatives_in_banks = request.POST.get('relatives_in_banks')
        relatives_in_gov_institutions = request.POST.get('relatives_in_gov_institutions')
        beginning_of_the_work = request.POST.get('beginning_of_the_work')
        info_about_work = request.POST.get('info_about_work')
        wage = request.POST.get('wage')
        sender_name = name + ' ' + last_name + ' ' + 'прислал Анкету'




        pdf_html = render_to_string(template, locals())
        pdf_file = HTML(string=pdf_html).write_pdf(stylesheets=[CSS(string='@page { size: letter portrait; margin: 1cm }')])

        temp = tempfile.NamedTemporaryFile()
        temp.write(pdf_file)
        temp.seek(0)

        msg = EmailMultiAlternatives(
            sender_name,
            "Новый кандидат прислал свою анкету",
            settings.EMAIL_HOST_USER,
            ['nik.bishkek00@gmail.com']
        )
        msg.attach_file(temp.name, 'application/pdf')
        msg.send()

        return render(
            request,
            'email.html',
            {
                'title': 'send-mail'
            }
        )
    else:
        return render(
            request,
            'email.html',
            {
                'title': 'send-mail'
            }
        )
