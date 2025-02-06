# aida-genai-workshop
Workshop files for the AIDA Data Hub Generative AI workshop


## Getting started

Connect to the AIDA VM, then ...

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
