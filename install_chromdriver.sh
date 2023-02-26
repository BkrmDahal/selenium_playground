# install chrome
wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
echo 'deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main' | sudo tee /etc/apt/sources.list.d/google-chrome.list
sudo apt-get update
sudo apt-get install google-chrome-stable

# install driver
# important make sure chromedriver version and google-chrome-stable version matches
wget https://chromedriver.storage.googleapis.com/110.0.5481.77/chromedriver_linux64.zip
unzip chromedriver_linux64.zip -d /usr/bin
echo 'export PATH=$PATH:/usr/bin' >> ~/.bashrc
source ~/.bashrc
chromedriver --version

