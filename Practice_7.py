DevOps=("Linux","Vagrant","Bash Scripting","AWS","Jenkins","Python","Ansible")
Development=["React","Java","Asp","Js","SpringBoot","Go"]
cntr_emp1={"Name":"Harry", "Skill":"Ai","code":123}
cntr_emp2={"Name":"Larry", "Skill":"Blockchain","code":456}
usr_skill=input("Enter Skills: ")

if usr_skill in DevOps:
    print("Skill in Devops")
elif usr_skill in Development:
    print("Skill in Development")
elif usr_skill in cntr_emp1.values() or usr_skill in cntr_emp2.values():
    print("Skill in Employee Section")
else:
    print("We don't have skills")