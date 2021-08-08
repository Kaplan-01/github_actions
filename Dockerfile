#  UBUNTU  
FROM ubuntu:20.04    
LABEL description = "Desarrollo Web: IDGS-81"  
LABEL mainteiner = "Carmen Kaplan"  
LABEL version = "0.1"    

#  PYTHON  
RUN apt update  
RUN apt install -y python3  
RUN apt install -y python3-pip

#  TEST  
RUN pip3 install pytest    