import os
from sys import argv
from shutil import copy2
from tqdm import tqdm

def extract(m3u_file):
    with open(m3u_file, "r") as f:
        m3u = f.read()
    m3u =  m3u.split("\n")
    m3u = [s for s in m3u if s[:1] != "#" and s != ""]
    songs = [s.split("/")[-1] for s in m3u]
    fldr = ".".join(m3u_file.split(".")[:-1])
    if not os.path.exists(fldr):
        os.makedirs(fldr)
    for src, song in tqdm(zip(m3u,songs)):
        copy2(src, fldr + "/" + song)
        

if __name__ == "__main__":
    m3u_file = ""
    try:
        m3u_file = argv[1]
    except IndexError as e:
        print("Please provide m3u file name as a parameter")
        exit(1)
    extract(m3u_file)    

