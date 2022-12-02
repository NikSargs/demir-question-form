from io import BytesIO
from django.conf import settings
from django.core.mail import EmailMessage
from django.shortcuts import render
from docxtpl import DocxTemplate


def sendresume(request, doc=DocxTemplate('template.docx')):
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
        sender_name = name + ' ' + last_name
        title_name = name + ' ' + last_name + ' ' + 'прислал Анкету'

        context = {
            "filling_date": filling_date,
            "last_name": last_name,
            "name": name,
            "second_name": second_name,
            "birthdate": birthdate,
            "birthplace": birthplace,
            "nationality": nationality,
            "sex_resume": sex_resume,
            "address_resume": address_resume,
            "phone_resume": phone_resume,
            "army_resume": army_resume,
            "licence": licence,
            "spouce_info": spouce_info,
            "children_info": children_info,
            "father_info": father_info,
            "mother_info": mother_info,
            "sisters_info": sisters_info,
            "brothers_info": brothers_info,
            "incomplete_secondary_education": incomplete_secondary_education,
            "secondary_education": secondary_education,
            "vocational_education": vocational_education,
            "high_education": high_education,
            "master_degree": master_degree,
            "doctor_degree": doctor_degree,
            "en_lang": en_lang,
            "ru_lang": ru_lang,
            "kg_lang": kg_lang,
            "different_lang": different_lang,
            "orgname": orgname,
            "post": post,
            "work_period": work_period,
            "left_cause": left_cause,
            "recommendation": recommendation,
            "relatives_in_db": relatives_in_db,
            "relatives_in_banks": relatives_in_banks,
            "relatives_in_gov_institutions": relatives_in_gov_institutions,
            "beginning_of_the_work": beginning_of_the_work,
            "info_about_work": info_about_work,
            "wage": wage,

        }

        doc.render(context)
        file_io = BytesIO()
        doc.save(file_io)

        email = EmailMessage(
            title_name,
            "Новый кандидат прислал свою анкету",
            settings.EMAIL_HOST_USER,
            ['nik.bishkek00@gmail.com']
        )
        email.attach(sender_name + ".docx", file_io.getvalue(),
                     'application/vnd.openxmlformats-officedocument.wordprocessingml.document')
        email.send()

        return render(
            request,
            'resume.html',
            {
                'title': 'send-resume'
            }
        )
    else:
        return render(
            request,
            'resume.html',
            {
                'title': 'send-resume'
            }
        )

