data = {
    "PERSONAL DATA": {
        "Name": "Louise Humphrey M. Del Castillo",
        "Age": 21,
        "Sex": "Male",
        "Birthday": "July 6, 2005",
        "Address": "Quezon City",
        "Email": "louisehumphreymdelcastillo@tua.edu.ph"
    },
    "EDUCATION": {
        "Elementary": "Panggulayan Elementary School (2012-2018)",
        "Highschool": "Immaculate Heart of Mary Academy (2018-2024)",
        "College": "Trinity University of Asia (2024-present)"
    },
    "SKILLS & INTERESTS": {
        "Skills": "JavaScript, Python, Java, Linux, Web Development",
        "Interests": "Hardware, Computers, Coding",
        "Hobbies": "Sleeping, Cooking, Sports, Gaming"
    }
}

for section, fields in data.items():
    print(section)
    for key, value in fields.items():
        print(f"{key:<20}{value}")
    print("\n")