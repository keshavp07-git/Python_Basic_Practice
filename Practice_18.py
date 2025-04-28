from fabric.api import *

def greetings(msg):
    print("Good {}".format(msg))
# In linux list fab commands go to the fab file directory and type fab -l
# All commands will appear
# fab greetings:Mornings , fab run the commands greetings with use : to give required arguments.
def system_info(): # Another command
    print("Disk Space")
    local("df -h") # local used to fire command in local machine under this method we can write commands of Bash shell and Linux
    print("---------------------------------------------------------------------------------------")
    print("---------------------------------------------------------------------------------------")

    print("Memory info")
    local("free -m")
    print("---------------------------------------------------------------------------------------")
    print("---------------------------------------------------------------------------------------")
    print("Uptime info")
    local("uptime")
    print("---------------------------------------------------------------------------------------")
    print("---------------------------------------------------------------------------------------")


# for remote commands ,
'''Create a user in another machine web01 adduser like devops and set password for it 12345678
then, give privileges to devops by editing file sudo "visudo" then set user "devops" NOPASSWD:ALL below root ,
after edit file to disable password based authentication by vi /etc/ssh/sshd_config after that find and edit the
disable option remove # from PasswordAuthentication yes
then restart sshd service
now we can authenticate with ssh login 
DO SAME FOR ANOTHER MACHINE web02 
Now with scriptbox we do name to ip mapping of our machine web01 and web02 by editing 
file vi /etc/hosts as root user
after assign 
ip web01
ip web02
then test by 
ping web01 -c 4
ping web02 -c 4
'''
# Now Create ssh key in scriptbox
'''
create ssh key for key based login ssh-keygen
and copy that key to both machines and its user by using after creating
ssh-copy-id devops@web01
give password of devops web01 1234
then same for devops@web02 12345678
now we can login without password....
using command
ssh -i ~/.ssh/id_rsa devops@web01 or directly
ssh devops@web01
'''