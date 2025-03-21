FROM ctfd/ctfd 

COPY jumpbox /opt/CTFd/CTFd/plugins/jumpbox
RUN pip install -r /opt/CTFd/CTFd/plugins/jumpbox/requirements.txt
