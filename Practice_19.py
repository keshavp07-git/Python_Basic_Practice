from fabric.api import *
def web_setup(WEBURL, DIRNAME):
    print("###################################################################################")
    local("apt install zip unzip -y") # Testing this command working remotely or not using fab -H web01 -u devops web_setup:url , unzip dir name

    print("###################################################################################")
    print("Installing dependencies")
    print("###################################################################################")
    sudo("yum install httpd wget unzip -y") # Installing httpd with sudo privileges

    print("###################################################################################")
    print("Start & enable service.")
    print("###################################################################################")
    sudo("systemctl start httpd") # Starting httpd service
    sudo("systemctl enable httpd") # Enable httpd service

    print("###################################################################################")
    print("Downloading and pushing website to webservers.")
    print("###################################################################################")
    local(("wget -O website.zip %s") % WEBURL) # Downloading template and rename as website.zip , use %s to replace any replace with help variable % WEBURL
    local("unzip -o website.zip") # Unzip website.zip if exists overwrite it

    print("###################################################################################")
    with lcd(DIRNAME):  # Without login local change directory lcd , Now Go to that directory which get extracted which can be store in DIRNAME variable , Now extracted items
        #zip all contents into tooplate.zip from that folder name which get from website.zip and we pass that folder name in DIRNAME so everything from that folder zip into tooplate.zip
        local("zip -r tooplate.zip * ")
        put("tooplate.zip", "/var/www/html/", use_sudo=True) # Now move tooplate to /var/WWW/html path where it get deployed using sudo privileges

    with cd("/var/www/html/"): # Now go to that directory "/var/WWW/html"
        sudo("unzip -o tooplate.zip") # Then unzip all contents from tooplate.zip this path "/var/WWW/html/"

    sudo("systemctl restart httpd")

    print("Website setup is done.")
