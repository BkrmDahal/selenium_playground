sudo apt-get update
sudo apt-get -y install firefox 

# install driver
# important make sure chromedriver version and google-chrome-stable version matches
VERSION="v0.32.2"
wget -O geodriver.tar.gz https://github.com/mozilla/geckodriver/releases/download/$VERSION/geckodriver-$VERSION-linux64.tar.gz

sudo tar -xvzf geodriver.tar.gz -C /usr/bin
echo 'export PATH=$PATH:/usr/bin' >> ~/.bashrc
source ~/.bashrc
geckodriver --version
