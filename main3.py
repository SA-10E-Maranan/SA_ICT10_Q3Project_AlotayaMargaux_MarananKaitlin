# Seatwork 2 - Second Quarter
from pyscript import display, document

def intrams_checker(e):
    e.preventDefault()  # prevent form submit

    document.getElementById('output').innerHTML = ''
    document.getElementById('image').innerHTML = ''

    # get radio values
    reg_el = document.querySelector('input[name="registration"]:checked')
    clr_el = document.querySelector('input[name="clearance"]:checked')

    registration = reg_el.value if reg_el else None
    clearance = clr_el.value if clr_el else None

    grade_level = document.getElementById('level').value
    section = document.getElementById('section').value

    # stop if any field is empty
    if registration is None or clearance is None or grade_level == "" or section == "":
        display("Please answer all questions before submitting the form.", target="output")
        return

    grade_level = int(grade_level)

    if registration is None or clearance is None:
        display("Please answer all questions before submitting the form.", target="output")

    if registration != 'registered':
        display(f'Not eligible: student is not registered for Intrams. Ask your PE teacher regarding the online registraton.', target='output')

    elif clearance != 'cleared':
        display(f'Not eligible: medical clearance required. Go to the clinic and secure your clearance.', target='output')

    elif section == 'emerald'and grade_level == 7:
        display(f'Congratulations! You are part of the ...', target='output')
        document.getElementById("image").innerHTML = "<img src='heartslabyul.webp' width='200'>"

    elif section == 'ruby'and grade_level == 7:
        display(f'Congratulations! You are part of the ...', target='output')
        document.getElementById("image").innerHTML = "<img src='octavinelle.webp' width='200'>"

    elif section == 'sapphire'and grade_level == 7:
        display(f'Congratulations! You are part of the ...', target='output')
        document.getElementById("image").innerHTML = "<img src='ignihyde.webp' width='200'>"

    elif section == 'topaz'and grade_level == 7:
        display(f'Congratulations! You are part of the ...', target='output')
        document.getElementById("image").innerHTML = "<img src='savanaclaw.webp' width='200'>"

    elif section == 'emerald'and grade_level == 10:
        display(f'Congratulations! You are part of the ...', target='output')
        document.getElementById("image").innerHTML = "<img src='heartslabyul.webp' width='200'>"

    elif section == 'ruby'and grade_level == 10:
        display(f'Congratulations! You are part of the ...', target='output')
        document.getElementById("image").innerHTML = "<img src='octavinelle.webp' width='200'>"

    elif section == 'sapphire'and grade_level == 10:
        display(f'Congratulations! You are part of the ...', target='output')
        document.getElementById("image").innerHTML = "<img src='ignihyde.webp' width='200'>"

    elif section == 'topaz'and grade_level == 10:
        display(f'Congratulations! You are part of the ...', target='output')
        document.getElementById("image").innerHTML = "<img src='savanaclaw.webp' width='200'>"

    elif section == 'emerald'and grade_level == 8:
        display(f'Congratulations! You are part of the ...', target='output')
        document.getElementById("image").innerHTML = "<img src='diasomnia.webp' width='200'>"

    elif section == 'ruby'and grade_level == 8:
        display(f'Congratulations! You are part of the ...', target='output')
        document.getElementById("image").innerHTML = "<img src='pomefiore.webp' width='200'>"

    elif section == 'sapphire'and grade_level == 8:
        display(f'Congratulations! You are part of the ...', target='output')
        document.getElementById("image").innerHTML = "<img src='scarabia.webp' width='200'>"

    elif section == 'topaz'and grade_level == 8:
        display(f'Congratulations! You are part of the ...', target='output')
        document.getElementById("image").innerHTML = "<img src='ramshackle.png' width='200'>"

    elif section == 'emerald'and grade_level == 9:
        display(f'Congratulations! You are part of the ...', target='output')
        document.getElementById("image").innerHTML = "<img src='diasomnia.webp' width='200'>"

    elif section == 'ruby'and grade_level == 9:
        display(f'Congratulations! You are part of the ...', target='output')
        document.getElementById("image").innerHTML = "<img src='pomefiore.webp' width='200'>"

    elif section == 'sapphire'and grade_level == 9:
        display(f'Congratulations! You are part of the ...', target='output')
        document.getElementById("image").innerHTML = "<img src='scarabia.webp' width='200'>"

    elif section == 'topaz'and grade_level == 9:
        display(f'Congratulations! You are part of the ...', target='output')
        document.getElementById("image").innerHTML = "<img src='ramshackle.png' width='200'>"