import requests
import time
start_time = time.time()

print("--- %s seconds ---" % (time.time() - start_time))
url = 'https://cs7ns1.scss.tcd.ie/index.php/?shortname=lpezm&download=resume_speed'
captchaNames = requests.get(url).text
print(captchaNames)
for i in captchaNames.split(',\n'):
    file_url = 'https://cs7ns1.scss.tcd.ie/index.php/?shortname=lpezm&download=resume_speed&myfilename=' + i
    files = requests.get(file_url)
    file = open(i,"wb")
    file.write(files.content)
    file.close()
    print("Time for file retrieval is:","--- %s seconds ---" % (time.time() - start_time))
print("Time for file retrieval is:","--- %s seconds ---" % (time.time() - start_time))