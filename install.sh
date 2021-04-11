python3 -m venv FINAL_TEST
source ./FINAL_TEST/bin/activate
cd FINAL_TEST
git clone https://github.com/TIC4302/email-activity-bot.git
cd email-activity-bot
chmod +x bandit_install.sh
./bandit_install.sh
easy_install pyzmail
pip3 install -r requirements.txt
 

