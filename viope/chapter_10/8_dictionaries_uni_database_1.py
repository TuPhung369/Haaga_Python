def main():
    db = {}
    insert_degree_program(db, "ITBBA")
    insert_degree_program(db, "EXPER")
    insert_course(db, "ITBBA", ("Python Programming", 5))
    insert_course(db, "ITBBA", ("Time Management", 3))
    insert_course(db, "EXPER", ("Creative Hospitality and Tourism", 5))
    insert_course(db, "EXPER", ("Managing Dynamic Restaurant Business", 10))
    print_degree_program(db, "ITBBA")
    print_degree_program(db, "EXPER")


def insert_degree_program(db, program_name):
    if program_name in db:
        print(f"{program_name} is already in the database")
    else:
        db[program_name] = []  # Initialize an empty list for courses


def insert_course(db, program_name, course_info):
    if program_name not in db:
        print(f"Unknown degree program: {program_name}")
        return

    course_name, credits = course_info
    # Check for duplicate course
    if any(course[0] == course_name for course in db[program_name]):
        print(f"{course_name} is already in the database")
    else:
        db[program_name].append(course_info)  # Add course to the degree program


def print_degree_program(db, program_name):
    if program_name in db:
        courses = db[program_name]
        total_credits = sum(course[1] for course in courses)
        print(f"{program_name} ({len(courses)} courses)")
        for course in courses:
            print(f"  {course[0]}, {course[1]} credits")
        print(f"  Total credits: {total_credits}")
    else:
        print(f"Unknown degree program: {program_name}")


if __name__ == "__main__":
    main()
