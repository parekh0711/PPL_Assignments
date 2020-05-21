host_path=r"C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
websites=["www.facebook.com","www.twitter.com"]
final_list=[redirect+ " "+ i for i in websites]
final_string="\n".join(final_list)
while True:
        with open(host_path,"r+") as fileptr:
            content = fileptr.read()
            for website in websites:
                if website in content:
                    pass
                else:
                    fileptr.write(redirect+"        "+website+"\n")
    
