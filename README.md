# aida-genai-workshop
Workshop files for the AIDA Data Hub Generative AI workshop


## Getting started

Connect to the AIDA VM, then ...

### configure proxy to the internet

have a privoxy running on the connecting (your) host

in .bashrc on the destination, configure it:

```bash
# proxy
# Define the proxy URL
PROXY_URL="http://127.0.0.1:8118"

# Set the http_proxy and https_proxy environment variables
export http_proxy=$PROXY_URL
export https_proxy=$PROXY_URL

# Set the HTTP_PROXY and HTTPS_PROXY environment variables (uppercase)
export HTTP_PROXY=$PROXY_URL
export HTTPS_PROXY=$PROXY_URL

# Optionally, you can also set the ftp_proxy and FTP_PROXY if needed
export ftp_proxy=$PROXY_URL
export FTP_PROXY=$PROXY_URL

export NO_PROXY=localhost,127.0.0.1,::1
```

### clone this repository

```
git clone https://github.com/phromo/aida-genai-workshop.git
```

### mount the model and data files

Copy model files locally - they are huge, we want fast access!

```
sudo apt install nfs-common -y
mkdir ~/workshop_files
sudo mount 10.39.196.249:/mnt ~/workshop_files
sudo mkdir /mnt/ollama
sudo chown sectraadmin:sectraadmin /mnt/ollama

# copy ollama
rsync -av --progress=info2 ~/workshop_files/ollama/ /mnt/ollama/

# copy deepseek2
rsync -av --progress=info2 ~/workshop_files/ollama_deepseek_r1/ /mnt/ollama/

# ensure models are where ollama expects
ln -s /mnt/ollama ~/.ollama
```

Install ollama, see https://github.com/ollama/ollama/blob/main/docs/linux.md


```
# note: cant use this from aida since the download gets blocked
# curl -L https://ollama.com/download/ollama-linux-amd64.tgz -o ollama-linux-amd64.tgz
# sudo tar -C /usr -xzf ollama-linux-amd64.tgz
# instead copy
sudo tar -C /usr -xzf ~/workshop_files/ollama-linux-amd64.tgz

```
